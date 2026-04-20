# 🧩 Atividade PBL – Aula 6
# 1. Plano de Testes

## Objetivo
Validar as principais funcionalidades do sistema LocalEats, verificando se o comportamento está de acordo com o esperado pelo usuário.

## Escopo

**O que será testado:**
- Carregamento da lista de restaurantes
- Filtro por categoria
- Campo de busca
- Navegação entre páginas (Favoritos e Pedidos)

**O que NÃO será testado:**
- Performance e tempo de resposta
- Segurança e autenticação
- Compatibilidade com dispositivos móveis

## Estratégia
Testes manuais do tipo funcional, realizados diretamente no navegador, seguindo os casos de teste definidos abaixo.

# 2. Casos de Teste

## CT-01 – Carregamento da página inicial ✅ (sucesso)

**Pré-condição:** Ter acesso à internet e ao endereço do sistema.

**Passos:**
1. Abrir o navegador
2. Acessar `https://local-eats-unisenac.vercel.app/`
3. Aguardar o carregamento

**Resultado esperado:** A página exibe a lista de restaurantes no lugar da mensagem "Carregando...".

---

## CT-02 – Filtrar restaurantes por categoria ✅ (sucesso)

**Pré-condição:** Página inicial carregada com restaurantes visíveis.

**Passos:**
1. Na página inicial, clicar no botão "Japonesa"
2. Observar os resultados

**Dados de entrada:** Filtro: `Japonesa`

**Resultado esperado:** Apenas restaurantes de culinária japonesa são exibidos.

---

## CT-03 – Buscar restaurante pelo nome ✅ (sucesso)

**Pré-condição:** Página inicial carregada com restaurantes visíveis.

**Passos:**
1. Clicar no campo de busca
2. Digitar o nome de um restaurante existente
3. Observar o resultado

**Dados de entrada:** Texto: `"Sushi"`

**Resultado esperado:** A lista filtra e exibe apenas restaurantes com o nome buscado.

---

## CT-04 – Acessar a página "Meus Favoritos" ✅ (sucesso)

**Pré-condição:** Estar em qualquer página do sistema.

**Passos:**
1. Clicar em "Meus Favoritos" no menu
2. Aguardar o carregamento

**Resultado esperado:** A página de favoritos é exibida corretamente com os restaurantes salvos ou mensagem de lista vazia.

---

## CT-05 – Acessar a página "Meus Pedidos" ✅ (sucesso)

**Pré-condição:** Estar em qualquer página do sistema.

**Passos:**
1. Clicar em "Meus Pedidos" no menu
2. Aguardar o carregamento

**Resultado esperado:** A página exibe o histórico de pedidos ou uma mensagem indicando que não há pedidos.

---

## CT-06 – Buscar por termo que não existe ❌ (erro)

**Pré-condição:** Página inicial carregada.

**Passos:**
1. Clicar no campo de busca
2. Digitar um texto sem correspondência

**Dados de entrada:** Texto: `"xyzabc123"`

**Resultado esperado:** O sistema exibe a mensagem "Nenhum restaurante encontrado" ou similar.

---

## CT-07 – Filtrar por categoria sem resultados ❌ (erro)

**Pré-condição:** Página inicial carregada.

**Passos:**
1. Clicar no botão "Mexicana"
2. Observar o comportamento quando não há restaurantes nessa categoria

**Resultado esperado:** O sistema exibe uma mensagem informando que não há restaurantes nessa categoria.

---

# 3. Execução dos Testes

| ID | Resultado | Evidência |
|----|-----------|-----------|
| CT-01 | ❌ Falhou | A mensagem "Carregando os melhores restaurantes..." nunca some. Nenhum restaurante é exibido. |
| CT-02 | ❌ Falhou | Os botões de filtro existem, mas sem dados carregados não há o que filtrar. |
| CT-03 | ❌ Falhou | O campo de busca aceita texto, mas não retorna resultados nem exibe feedback. |
| CT-04 | ⚠️ Parcial | A página abre corretamente, mas fica presa em "Carregando seus locais do coração...". |
| CT-05 | ⚠️ Parcial | A página abre corretamente, mas fica presa em "Carregando seus pedidos...". |
| CT-06 | ❌ Falhou | Nenhuma mensagem de feedback é exibida para o usuário. |
| CT-07 | ❌ Falhou | Nenhuma mensagem de feedback é exibida para o usuário. |

---

# 4. Análise dos Resultados

- **Total de testes executados:** 7
- **Passaram:** 0
- **Resultado parcial:** 2 (CT-04 e CT-05)
- **Falharam:** 5

**Principais problemas encontrados:**
- A listagem de restaurantes não carrega em nenhuma página do sistema
- O sistema não exibe mensagens de erro ou de lista vazia para o usuário
- Busca e filtros ficam inutilizáveis por dependerem dos dados que não carregam

---

# 5. Reflexão

**O plano de testes ajudou a organizar melhor o processo?**
Sim. Sem o plano, provavelmente testaríamos de forma aleatória. Com os casos definidos antes, ficou mais fácil identificar que a falha no carregamento era o problema raiz que derrubava várias outras funcionalidades.

**Algum problema só foi percebido durante a execução?**
Sim. Só durante a execução percebemos que CT-04 e CT-05 tinham a navegação funcionando, mas o conteúdo dinâmico falhava — o que nos fez classificar como "parcial" em vez de simplesmente "falhou".

**O que melhorariam no processo de testes?**
Incluiríamos um teste de verificação da API/fonte de dados antes dos demais, para identificar mais rapidamente quando uma falha é de integração e não da interface.

---

