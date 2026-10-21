"""Conversão entre objetos de domínio e arquivos JSON; sem regras de negócio."""
import json
from pathlib import Path
from typing import Any

from modelos import Checkpoint, Corrida, Equipe, Passagem, Professor


class ErroPersistencia(Exception):
    """Indica arquivo inválido ou relacionamento persistido inconsistente."""


class PersistenciaJSON:
    """Lê e grava as cinco coleções em JSON, usando IDs estáveis por posição."""

    NOMES: tuple[str, ...] = ("corridas", "equipes", "professores", "checkpoints", "passagens")

    def __init__(self, diretorio: Path) -> None:
        self.diretorio: Path = Path(diretorio)
        self.diretorio.mkdir(parents=True, exist_ok=True)

    def _ler(self, nome: str) -> list[dict[str, Any]]:
        caminho = self.diretorio / f"{nome}.json"
        if not caminho.exists():
            caminho.write_text("[]\n", encoding="utf-8")
        try:
            conteudo = json.loads(caminho.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeError, OSError) as erro:
            raise ErroPersistencia(f"Arquivo inválido: {caminho.name}") from erro
        if not isinstance(conteudo, list) or any(not isinstance(x, dict) for x in conteudo):
            raise ErroPersistencia(f"Estrutura inválida em {caminho.name}.")
        return conteudo

    def carregar(self) -> tuple[list[Corrida], list[Equipe], list[Professor], list[Checkpoint], list[Passagem]]:
        """Reconstitui objetos e suas relações, validando as referências."""
        bruto = {nome: self._ler(nome) for nome in self.NOMES}
        try:
            for nome, registros in bruto.items():
                if [r["id"] for r in registros] != list(range(1, len(registros) + 1)):
                    raise ValueError(f"IDs inválidos em {nome}")
            corridas = [Corrida(r["nome"], r.get("total_checkpoints_previstos", max(1, sum(1 for cp in bruto["checkpoints"] if cp.get("corrida_id") == r["id"])))) for r in bruto["corridas"]]
            equipes = [Equipe(r["nome"]) for r in bruto["equipes"]]
            professores = [Professor(r["nome"]) for r in bruto["professores"]]
            def obter(colecao: list[Any], identificador: int) -> Any:
                if type(identificador) is not int or not 1 <= identificador <= len(colecao):
                    raise ValueError(f"Referência inexistente: {identificador}")
                return colecao[identificador - 1]
            for r in bruto["equipes"]:
                equipe = obter(equipes, r["id"])
                for id_corrida in r["corrida_ids"]:
                    corrida = obter(corridas, id_corrida)
                    if corrida in equipe.corridas:
                        raise ValueError("Participação duplicada")
                    equipe.adicionar_corrida(corrida)
                    corrida.adicionar_equipe(equipe)
            checkpoints = []
            for r in bruto["checkpoints"]:
                corrida = obter(corridas, r["corrida_id"])
                professor = obter(professores, r["professor_id"])
                if any(c.numero == r["numero"] for c in corrida.checkpoints):
                    raise ValueError("Checkpoint duplicado")
                checkpoint = Checkpoint(r["numero"], corrida, professor)
                checkpoints.append(checkpoint)
                corrida.adicionar_checkpoint(checkpoint)
                professor.adicionar_checkpoint(checkpoint)
            passagens = []
            for r in bruto["passagens"]:
                corrida = obter(corridas, r["corrida_id"])
                equipe = obter(equipes, r["equipe_id"])
                checkpoint = obter(checkpoints, r["checkpoint_id"])
                professor = obter(professores, r["professor_id"])
                if checkpoint.corrida is not corrida or checkpoint.professor is not professor or corrida not in equipe.corridas:
                    raise ValueError("Relacionamento de passagem inconsistente")
                if any(p.equipe is equipe for p in checkpoint.passagens):
                    raise ValueError("Passagem duplicada")
                passagem = Passagem(corrida, equipe, checkpoint, professor, r["momento"])
                passagens.append(passagem)
                corrida.adicionar_passagem(passagem)
                equipe.adicionar_passagem(passagem)
                checkpoint.adicionar_passagem(passagem)
            return corridas, equipes, professores, checkpoints, passagens
        except (KeyError, TypeError, ValueError, IndexError) as erro:
            raise ErroPersistencia(f"Dados persistidos incompatíveis: {erro}") from erro

    def salvar(self, corridas: tuple[Corrida, ...], equipes: tuple[Equipe, ...], professores: tuple[Professor, ...], checkpoints: tuple[Checkpoint, ...], passagens: tuple[Passagem, ...]) -> None:
        """Serializa coleções com IDs e grava os arquivos de forma atômica."""
        def ids(itens: tuple[Any, ...]) -> dict[Any, int]:
            return {obj: i for i, obj in enumerate(itens, 1)}
        ci, ei, pi, ki = ids(corridas), ids(equipes), ids(professores), ids(checkpoints)
        registros: dict[str, list[dict[str, Any]]] = {
            "corridas": [{"id": ci[c], "nome": c.nome, "total_checkpoints_previstos": c.total_checkpoints_previstos} for c in corridas],
            "equipes": [{"id": ei[e], "nome": e.nome, "corrida_ids": [ci[c] for c in e.corridas]} for e in equipes],
            "professores": [{"id": pi[p], "nome": p.nome} for p in professores],
            "checkpoints": [{"id": ki[k], "numero": k.numero, "corrida_id": ci[k.corrida], "professor_id": pi[k.professor]} for k in checkpoints],
            "passagens": [{"id": i, "corrida_id": ci[p.corrida], "equipe_id": ei[p.equipe], "checkpoint_id": ki[p.checkpoint], "professor_id": pi[p.professor], "momento": p.momento} for i, p in enumerate(passagens, 1)],
        }
        for nome, dados in registros.items():
            caminho = self.diretorio / f"{nome}.json"
            temporario = caminho.with_suffix(".json.tmp")
            temporario.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            temporario.replace(caminho)
