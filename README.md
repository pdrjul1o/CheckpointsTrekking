# Checkpoints Trekking — Segunda Versão

Projeto da segunda etapa, com a camada de serviços introduzida sobre a primeira versão.

## Estrutura

```text
CheckpointsTrekking/
├── main.py
├── aplicacao.py
├── trekking.py
├── modelos/
├── servicos/
├── excecoes/
├── interface/
├── testes/
└── ARQUITETURA.md
```

Os dados permanecem somente em memória, usando listas internas da aplicação.

## Execução

No diretório do projeto:

```bash
python main.py
```

## Testes

Para executar o fluxo completo e as situações inválidas:

```bash
python testes/test_fluxo.py
```

O teste cobre:
- cadastro de corrida, equipe e professor;
- cadastro de checkpoint;
- participação da equipe na corrida;
- registro de passagem;
- consultas por corrida, equipe e checkpoint;
- tentativa de repetir uma passagem;
- tentativa de registrar passagem de equipe que não participa da corrida.

## Camadas

```text
Interface
    ↓
Serviços
    ↓
Aplicação
    ↓
Modelos
    ↓
Exceções
```

As telas apresentam mensagens ao usuário. As regras de negócio ficam nos serviços,
e as exceções personalizadas são capturadas pela interface.
