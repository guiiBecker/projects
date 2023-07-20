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

  



