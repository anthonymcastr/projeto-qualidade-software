# 📄 Testes Funcionais vs Estruturais – LocalEats

## Funcionalidade Escolhida

Com base no contexto da plataforma **LocalEats**, a funcionalidade escolhida foi a **busca de restaurantes**.

Escolhemos essa funcionalidade porque ela é uma das partes mais importantes do sistema e também uma das que mais se relaciona com os problemas apresentados no cenário, principalmente a questão dos **resultados incorretos nas buscas**.

### O que a funcionalidade faz

A busca permite que o usuário encontre restaurantes com base em alguns critérios, como por exemplo:

* localização
* tipo de culinária
* faixa de preço
* nome do restaurante

Na prática, é uma funcionalidade central da plataforma, porque ajuda o usuário a encontrar o que ele realmente quer consumir.

### O que o usuário espera dela

Quando uma pessoa usa a busca, ela espera que o sistema:

* mostre resultados corretos
* respeite os filtros aplicados
* seja fácil de usar
* funcione de forma rápida
* apresente restaurantes realmente relacionados com a pesquisa
* funcione bem tanto no **web** quanto no **mobile**

Se a busca não funcionar direito, a experiência do usuário acaba sendo prejudicada logo no início do uso da plataforma.

---

# 🧪 Testes Caixa-Preta (Visão do Usuário)

Os **testes caixa-preta** são aqueles feitos pensando na funcionalidade do ponto de vista do usuário, ou seja, sem olhar o código por trás.

Nesse caso, a ideia é verificar se a busca está funcionando do jeito que a pessoa espera ao usar o sistema.

## Entradas possíveis

Algumas entradas possíveis para essa funcionalidade seriam:

* nome do restaurante
* categoria de comida
* localização ou bairro
* faixa de preço
* combinação de filtros
* campo de busca vazio
* texto digitado com erro
* pesquisa sem resultado

## Testes propostos

### Busca por nome

**Entrada:**

* “Pizzaria Napoli”

**Comportamento esperado:**

* o sistema deve mostrar esse restaurante nos resultados, caso ele exista

### Busca por categoria

**Entrada:**

* “japonesa”

**Comportamento esperado:**

* o sistema deve retornar restaurantes dessa categoria

### Busca por faixa de preço

**Entrada:**

* filtro “até R$ 50”

**Comportamento esperado:**

* devem aparecer apenas restaurantes dentro dessa faixa de preço

### Busca por localização

**Entrada:**

* “Centro”

**Comportamento esperado:**

* o sistema deve mostrar restaurantes dessa região

### Busca com múltiplos filtros

**Entrada:**

* “hamburgueria” + “Centro” + “até R$ 40”

**Comportamento esperado:**

* os resultados devem respeitar todos os filtros ao mesmo tempo

### Busca sem resultado

**Entrada:**

* “comida marciana”

**Comportamento esperado:**

* o sistema deve informar que não encontrou resultados, sem travar ou apresentar erro estranho

### Campo vazio

**Entrada:**

* busca sem digitar nada

**Comportamento esperado:**

* o sistema pode mostrar restaurantes em destaque ou pedir que o usuário informe algo para pesquisar

### Erro de digitação

**Entrada:**

* “xis salda”

**Comportamento esperado:**

* o sistema deveria tentar encontrar algo parecido ou pelo menos sugerir uma correção

### Teste entre plataformas

**Entrada:**

* mesma busca feita no web e no mobile

**Comportamento esperado:**

* os resultados devem ser consistentes nas duas plataformas

## Tipos de erro que podem ser encontrados

Com esse tipo de teste, alguns problemas que podem ser percebidos são:

* resultados errados
* filtros que não funcionam corretamente
* restaurantes sem relação com a pesquisa
* diferenças entre o web e o mobile
* falta de mensagem quando não existe resultado
* lentidão para responder
* comportamento estranho quando vários filtros são usados juntos

## Conclusão da visão caixa-preta

A principal vantagem da caixa-preta é que ela ajuda a verificar se a funcionalidade realmente faz sentido para o usuário.

Mesmo que o sistema esteja “funcionando tecnicamente”, se ele mostrar resultados errados ou confusos, a experiência já fica comprometida. Então esse tipo de teste é importante justamente para validar o uso real da funcionalidade.

---

# ⚙️ Testes Caixa-Branca (Visão do Sistema)

Os **testes caixa-branca** já olham para a parte interna da funcionalidade, ou seja, como a busca foi implementada e quais regras existem por trás dela.

Aqui o foco deixa de ser só “o que aparece para o usuário” e passa a ser também “como o sistema está chegando nesse resultado”.

## Possível implementação da funcionalidade

A busca de restaurantes pode ter sido construída com regras como:

* validação do texto digitado
* leitura dos filtros escolhidos
* consulta ao banco de dados
* integração com API de busca
* uso de geolocalização
* ordenação dos resultados
* tratamento de erro e de resultados vazios

## Possíveis estruturas lógicas

Pensando na lógica interna, é bem provável que existam decisões como:

* `if` o campo de busca estiver vazio
* `if` o filtro de preço estiver selecionado
* `if` a categoria estiver preenchida
* `if` a localização estiver disponível
* `if` não houver resultados
* `if` ocorrer erro no banco ou na API

## Testes propostos

### Validação de campo vazio

**O que testar:**

* se o sistema trata corretamente a situação em que o usuário não digita nada na busca

### Aplicação de filtros

**O que testar:**

* se preço, categoria e localização estão sendo aplicados corretamente

### Combinação de critérios

**O que testar:**

* se vários filtros ao mesmo tempo estão sendo combinados da forma certa

### Ordenação dos resultados

**O que testar:**

* se os restaurantes estão sendo exibidos na ordem correta, como por relevância, proximidade ou avaliação

### Uso da geolocalização

**O que testar:**

* se a localização do usuário está sendo considerada corretamente na busca

### Tratamento de dados incompletos

**O que testar:**

* se restaurantes com informações faltando (como preço, categoria ou endereço) não causam erro

### Tratamento de exceções

**O que testar:**

* se falhas no banco de dados, na API ou em outros serviços estão sendo tratadas corretamente

### Cobertura de caminhos lógicos

**O que testar:**

* se os principais fluxos da funcionalidade estão cobertos, como:
  * busca com resultado
  * busca sem resultado
  * busca com filtro
  * busca sem filtro
  * busca com erro

## Tipos de erro que podem ser encontrados

Com os testes caixa-branca, alguns erros que podem aparecer são:

* falhas em condições lógicas
* filtros sendo ignorados por erro no código
* ordenação incorreta
* tratamento errado de valores vazios ou nulos
* fluxos não cobertos
* falhas silenciosas em integrações
* comportamentos errados em situações específicas

## Conclusão da visão caixa-branca

A caixa-branca é importante porque ajuda a encontrar problemas que nem sempre ficam tão claros só olhando a interface.

Às vezes o usuário percebe que “a busca está estranha”, mas só olhando a lógica interna é que dá para entender de onde aquele problema realmente está vindo.

---

# 🔍 Comparação entre as abordagens

## Principal diferença

### Caixa-preta

Na **caixa-preta**, o teste é feito sem acesso ao código.  
O foco está em verificar se a funcionalidade funciona corretamente para o usuário.

### Caixa-branca

Na **caixa-branca**, o teste é feito com acesso à lógica interna.  
O foco está em verificar se as regras e decisões do sistema estão implementadas corretamente.

## Que tipo de problema cada abordagem encontra

### Caixa-preta ajuda a encontrar:

* erros visíveis para o usuário
* falhas de usabilidade
* respostas incorretas
* inconsistências na experiência
* comportamento inesperado

### Caixa-branca ajuda a encontrar:

* erros de lógica
* falhas em validações
* condições mal implementadas
* caminhos do código que não foram testados
* problemas internos da funcionalidade

## Resumo da comparação

De forma geral, dá para dizer que:

* a **caixa-preta** olha mais para o comportamento da funcionalidade
* a **caixa-branca** olha mais para a estrutura interna dela

As duas são importantes, porque uma complementa a outra.  
Se a equipe usar só uma abordagem, existe uma boa chance de deixar passar problemas importantes.

---

# 💭 Reflexão no contexto do LocalEats

## Qual abordagem parece mais útil para os problemas atuais do sistema?

Pensando especificamente no cenário do **LocalEats**, a **caixa-branca** parece ser muito útil para investigar os problemas que já foram identificados, principalmente porque vários deles parecem estar ligados à lógica interna da busca.

Entre esses problemas estão:

* resultados incorretos nas buscas
* comportamentos inesperados
* falhas em situações específicas
* inconsistências entre funcionalidades

Esses sinais normalmente indicam que pode existir algum problema em regras internas, como por exemplo:

* filtros sendo aplicados de forma errada
* combinação incorreta de critérios
* ordenação inadequada
* validações incompletas
* falhas em casos mais específicos

## Apenas uma abordagem seria suficiente?

### Não.

Na prática, usar apenas uma abordagem não seria o suficiente.

### Se fosse usada apenas caixa-preta

Seria possível perceber que a busca está com problema, mas talvez não fosse tão fácil descobrir a causa real do erro.

### Se fosse usada apenas caixa-branca

Seria possível analisar a lógica interna, mas ainda assim poderiam passar problemas que afetam diretamente a experiência do usuário.

## Conclusão da reflexão

Por isso, no caso do **LocalEats**, o mais adequado seria usar as duas abordagens juntas:

* **Caixa-preta** para validar se a funcionalidade está funcionando bem para o usuário
* **Caixa-branca** para identificar os problemas internos da implementação

Essa combinação é importante porque o sistema apresenta tanto problemas visíveis quanto indícios de falhas estruturais.

---

# ✅ Conclusão Final

A funcionalidade de **busca de restaurantes** foi escolhida por ser uma das mais importantes do **LocalEats** e também por estar diretamente ligada aos problemas apresentados no cenário.

Ao comparar os **testes caixa-preta** e **caixa-branca**, ficou claro que cada abordagem tem um papel diferente:

* a **caixa-preta** ajuda a validar o comportamento da funcionalidade
* a **caixa-branca** ajuda a analisar a lógica interna do sistema

As duas abordagens são importantes porque ajudam a encontrar tipos diferentes de falhas.

Por isso, para testar a busca de restaurantes de forma mais completa e confiável, o ideal é combinar as duas perspectivas.