# Banco de funcionários
  Este é um protótipo de um projeto que visa a construção de um banco de dados e um software para realizar a manutenção dele sem que seja necessário o acesso ao banco de dados toda vez que houver a necessidade de uma alteração.

#### Funcionalidades necessárias:
- Criar um banco de dados
- Adicionar um novo funcionário ao banco de dados.
- Remover um funcionário do banco de dados.
- Realizar uma busca pelo banco de dados.
- Imprimir relatórios por departamentos.

______________________

### Técnologias utilizadas
[![My Skills](https://skillicons.dev/icons?i=py,mysql)](https://skillicons.dev)


______________________

### Criação do Banco de dados (MySQL)
  Para a criação do banco de dados optei por utilizar o software XAMPP, pois já estava familiarizado com ele por usar durante as aulas de Banco de Dados na faculdade. Começamos criando o database Empresa para hospedar as informações da companhia. Em seguida foram criados a tabela de Funcionários e a tabela de Departamentos. 

**Funcionários**
>Informações sobre a tabela

| Nomenclatura  | Tipo de dadp | 
| ------------- | ------------- |
| Identificador do funcionário [Primary Key]  | INT |
| Nome do funcionário | VARCHAR | 
| Cargo do funcionário | VARCHAR |
| Data em que ele foi contratado | DATE |
| Identificador do departamento do funcionário [Foreigner Key]| INT |
| Salário do funcionário | INT |


**Departamento**
> Dados da tabela

| Nomenclatura  | Tipo de dadp | 
| ------------- | ------------- |
| Identificador do departamento [Primary Key] | INT |
| Nome do departamento | VARCHAR |


### Relacionamentos
  Relacionamento entre funcionários e departamentos é de grau binário e funciona da maneira na qual o funcionário existe para trabalhar para um determinado departamento, sendo assim um departamento existe para que um funcionários seja atruíbuido a ele. É um relacionamento de 1-N sendo que um funcionpario deve estar presente em apenas um departamento e um departamento pode conter 1 ou muitos funcionários.

_______________

### Código
  O código foi pensado e desenvolvido totalmente em python. Tanto a forma de realizar a conexão ao banco de dados hospedado em minha máquina, como a função de apresentar uma interface padrão para o usuário.
  A ideia do projeto é para o usuário conseguir gerar relatórios, adicionar e remover funcionários do banco de dados da empresa.
  Função **search**
  A ideia é o administrador conseguir gerar um relatório sobre os funcionários presentes no banco de dados, atualmente essa função relata os funcionários e as informações ligadas a eles. O funiconamento dele está ocorrendo, com um trigger que quando acionado gera uma tabela com todos os funcionários.
  Função **del_employer**
  Está função realiza a exclusão de um item presente no banco de dados, para a exclusão são necessários dois dados, o nome do empregado e o ID dele na empresa. Assim que executada o código executa a consulta no banco de dados com as devidas informações e realiza a exclusão.
  Função **newemp**
  Está função realiza a inclusão de um funcionário no banco de dados. Para isso se faz necessário que o administrador insira todos os dados do funcionário necessários. Quando devidamente preenchido e executado, o novo funcionário é adicionado no banco de dados. 
  **Erros**
  Nesse código apenas foram idealizados os tratamentos de erros básicos presente em um SQL, sempre que ocorrer um erro será informado para o usuário em que função o erro ocorreu e o também o erro que ocorreu no banco de dados.
  **Layouts**
  Os Layouts foram pensados para serem o mais simples possíveis, pois a ideia desse projeto era criar um gerenciador de banco de dados que não um usuário comum conseguiria utilizar sem problemas, eles são limpos sem muitas informações e intuitivos para usuário.
  **Erros**
  O tratamento de dados nesse caso ocorre quando o usuário insere valores que não estão presentes no banco de dados ou insere de maneira equivocada os dados necessários para realizar um novo cadastro. A opção Search apenas gera um relatório geral sem especificações. 

  



