# Atividade 06 – Testes Unitários e TDD

## 👥 Integrantes
- Lucas Devantier Pinto 
- Anthony Martins de Castro
- Christiano Dias Ferraz
- Felipe Ponciano de Almeida

---

## 📁 Estrutura do Projeto

.  
├── src/  
│   ├── pedido.py  
│   ├── desconto.py  
│   └── entrega.py  
└── tests/  
    ├── test_pedido.py  
    ├── test_desconto.py  
    └── test_entrega.py  

---

## 🔹 1. Funcionalidades escolhidas

Lucas: Cálculo do total do pedido com valor mínimo.

Cada integrante ficou responsável por uma regra de negócio do sistema.

---

### 👤 Lucas Devantier – Cálculo do total do pedido com valor mínimo

**Arquivo da implementação:** `/src/pedido.py`  
**Arquivo de testes:** `/tests/test_pedido.py`

#### Descrição
Soma os valores dos itens do pedido e valida se o total atinge o valor mínimo.

#### Regras de negócio
- Soma dos itens define o total  
- Pedido deve atingir valor mínimo  
- Caso contrário, deve gerar erro  

---

### 👤 Integrante 2 – Aplicação de desconto percentual

**Arquivo da implementação:** `/src/desconto.py`  
**Arquivo de testes:** `/tests/test_desconto.py`

#### Descrição
Aplica um desconto percentual sobre o valor total do pedido.

#### Regras de negócio
- Percentual deve estar entre 0 e 100  
- Valor final não pode ser negativo  

---

### 👤 Integrante 3 – Cálculo de taxa de entrega

**Arquivo da implementação:** `/src/entrega.py`  
**Arquivo de testes:** `/tests/test_entrega.py`

#### Descrição
Calcula a taxa de entrega com base na distância.

#### Regras de negócio
- Até 3km → taxa fixa  
- Acima de 3km → taxa adicional por km  
- Distância negativa → erro  

---

## 🔹 2. Testes Unitários

Cada integrante implementou seus testes unitários no respectivo arquivo dentro da pasta `/tests`.

---

### 🧪 Integrante 1 – Testes (pedido)

#### Teste 1 – Valor acima do mínimo

- Cenário: Pedido válido  
- Resultado esperado: Retorna total  

##### TDD
- Red: teste falhou por função inexistente  
- Green: implementação mínima  
- Refactor: cálculo real + validação  

##### Refatoração
- Código evoluiu de fixo para dinâmico  
- Inclusão de regra de negócio  

##### Execução
- Resultado: Passou  

---

#### Teste 2 – Valor abaixo do mínimo

- Cenário: Pedido inválido  
- Resultado esperado: Erro  

##### TDD
- Red: teste esperando erro  
- Green: exceção implementada  
- Refactor: melhoria da validação  

##### Refatoração
- Tratamento explícito de erro  

##### Execução
- Resultado: Passou  

---

### 🧪 Integrante 2 – Testes (desconto)

#### Teste 1 – Aplicação de desconto válido

- Cenário: Desconto dentro do limite  
- Resultado esperado: Valor reduzido corretamente  

##### TDD
- Red: falha inicial  
- Green: cálculo simples  
- Refactor: validação de percentual  

##### Refatoração
- Garantia de limites do desconto  

##### Execução
- Resultado: Passou  

---

#### Teste 2 – Percentual inválido

- Cenário: Desconto maior que 100%  
- Resultado esperado: Erro  

##### TDD
- Red: falha  
- Green: validação adicionada  
- Refactor: melhoria da mensagem de erro  

##### Refatoração
- Tratamento de entrada inválida  

##### Execução
- Resultado: Passou  

---

### 🧪 Integrante 3 – Testes (entrega)

#### Teste 1 – Distância até 3km

- Cenário: Taxa fixa  
- Resultado esperado: Valor fixo  

##### TDD
- Red: falha inicial  
- Green: retorno fixo  
- Refactor: lógica condicional  

##### Refatoração
- Inclusão de regra de distância  

##### Execução
- Resultado: Passou  

---

#### Teste 2 – Distância negativa

- Cenário: Entrada inválida  
- Resultado esperado: Erro  

##### TDD
- Red: falha  
- Green: validação implementada  
- Refactor: melhoria da estrutura  

##### Refatoração
- Garantia de integridade dos dados  

##### Execução
- Resultado: Passou  

---

## 🔹 3. Reflexão

### Foi difícil escrever testes antes do código?
Sim, pois exige mudança de mentalidade.

---

### O TDD ajudou no desenvolvimento?
Sim, ajudou a estruturar melhor a lógica antes da implementação.

---

### Os testes aumentaram a confiança no código?
Sim, pois qualquer erro pode ser detectado rapidamente.

---

### O que melhorariam?
- Cobrir mais cenários  
- Melhor organização dos testes  

---

### Como isso ajuda no projeto?
Permite evoluir o sistema com mais segurança e qualidade.