# Arquitetura — persistência ORM

A interface chama os serviços; estes validam as regras do domínio e delegam o acesso persistente à aplicação `Trekking`. Os modelos herdam de `Base` e seus atributos mapeados usam `Mapped`, `mapped_column` e `relationship`. Propriedades de leitura e métodos do domínio preservam o encapsulamento por convenção (`_atributo`); coleções são expostas como tuplas.

A fábrica de sessões e a engine são configuradas em `persistencia/banco.py`. `Trekking` mantém uma sessão por execução, realiza consultas com `select` e `scalars`, adiciona e remove objetos e delega commit/rollback a `persistencia/sessao.py`. O gerenciador de contexto no `main.py` encerra a sessão e a engine mesmo se ocorrer um erro. O ORM carrega relações e sincroniza referências bidirecionais; não há serialização JSON.

A associação N:N entre corrida e equipe utiliza uma tabela intermediária com chave primária composta. As regras de negócio permanecem nos serviços, incluindo a verificação de inscrição, professor e corrida do checkpoint. O SQLite usa chaves estrangeiras ativadas e restrições de unicidade.
