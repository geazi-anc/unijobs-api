# unijobs-api
a sample API for CI/CD pipeline development

## Início Rápido
A API foi desenvolvida em conteinerização via Docker. Os arquivos *Dockerfile* e *docker-compose.yml* já estão configurados para a instalação das dependências da API, assim como a configuração de variáveis de ambiente dentro do contêiner.

Para subir a aplicação, após ter clonado-a do repositório online, vá até a raiz do projeto e digite:
`docker-compose up -d`

O download da imagem do python será iniciada e a instalação das dependências será realizada.

A API ficará disponível no localhost, na porta 8000.

## Interagindo com a API por meio da documentação
O framework FastAPI provém algumas ferramentas para a geração de documentação automática. Uma das ferramentas utilizadas é o Swagger UI, que permite interagir com API fazendo chamadas HTTP sem o uso do Postman ou outro cliente.

Para acessar a documentação interativa, vá para *http://localhost:8000/docs*

## Executando os testes Unitários
Os testes unitários da API podem ser executados dentro do contêiner da API. Para isso, digite no terminal:
`docker-compose api pytest src/tests`