Consulta de Resultados de Loterias
Este projeto permite consultar os resultados de diferentes loterias brasileiras, incluindo Mega-Sena, Quina, Lotofácil, e outras, utilizando uma API pública da Caixa Econômica Federal.

Objetivo do Código
O código tem como objetivo consultar e exibir os resultados de sorteios específicos de diversas loterias, fornecendo os números sorteados e a data da apuração de cada concurso. A consulta é feita através de uma API pública.

Estrutura do Código
1. Função consultar_resultados_loteria(tipo_loteria, numero_concurso)
Essa função realiza a consulta dos resultados de um concurso específico de uma loteria.

Passos principais:

Recebe dois parâmetros: o tipo da loteria (como Mega-Sena, Quina, etc.) e o número do concurso.
Faz uma requisição GET para a API pública da Caixa Econômica Federal.
Se a requisição for bem-sucedida, retorna a lista de dezenas sorteadas e a data de apuração.
Caso ocorra algum erro, ou se os dados não forem encontrados, retorna None.
2. Função exibir_menu()
Exibe o menu principal com as opções das diferentes loterias disponíveis para consulta.

3. Função main()
Controla o fluxo principal do programa, exibindo o menu e permitindo que o usuário escolha uma loteria e forneça o número do concurso para consulta.

Passos principais:

Exibe o menu de loterias.
Recebe a escolha do usuário e, se válida, chama a função consultar_resultados_loteria para obter os resultados.
Exibe os números sorteados e a data da apuração ou uma mensagem de erro, se o concurso não estiver disponível.
Como Usar
Clone o repositório:

git clone https://github.com/usuario/repositorio.git
Instale o módulo requests (se ainda não estiver instalado):

pip install requests
Execute o código:

python consulta_loterias.py
Siga as instruções exibidas no terminal para consultar o resultado dos concursos de loterias.

Contribuições são bem-vindas! Se você deseja melhorar o código ou adicionar mais funcionalidades, fique à vontade para enviar um pull request.
