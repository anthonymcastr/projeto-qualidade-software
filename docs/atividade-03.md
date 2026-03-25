# 📄 Estratégia Inicial de Testes – LocalEats

## Funcionalidades Principais

Com base no contexto da plataforma **LocalEats**, as funcionalidades principais são:

* Busca de restaurantes (por localização, culinária e preço)
* Visualização de restaurantes (cardápio, fotos e avaliações)
* Sistema de avaliações e comentários
* Favoritar restaurantes
* Recomendações personalizadas
* Compatibilidade entre Web e Mobile

---

# 🧪 Níveis de Teste

## 2.1 Busca de restaurantes

**Teste unitário:**

* Regras de filtro, ordenação e combinação de critérios (localização, preço, categoria)

**Teste de integração:**

* Integração entre API de busca, banco de dados e serviços de geolocalização

**Teste de sistema:**

* Fluxo completo de busca com diferentes filtros aplicados

**Teste de aceitação:**

* Usuário consegue encontrar restaurantes relevantes de forma rápida e correta

---

## 2.2 Visualização de restaurantes

**Teste unitário:**

* Renderização de dados (cardápio, imagens, avaliações)

**Teste de integração:**

* Integração entre frontend e backend para carregamento de dados

**Teste de sistema:**

* Usuário acessa um restaurante e visualiza todas as informações corretamente

**Teste de aceitação:**

* Usuário entende facilmente as informações e navega sem confusão

---

## 2.3 Sistema de avaliações

**Teste unitário:**

* Criação, edição e persistência de avaliações

**Teste de integração:**

* Integração entre sistema de usuários e banco de dados de avaliações

**Teste de sistema:**

* Usuário publica avaliação e ela permanece após atualização

**Teste de aceitação:**

* Usuário consegue avaliar e visualizar avaliações de outros sem perda de dados

---

## 2.4 Favoritar restaurantes

**Teste unitário:**

* Lógica de adicionar/remover favoritos

**Teste de integração:**

* Integração entre conta do usuário e armazenamento de favoritos

**Teste de sistema:**

* Usuário salva e acessa lista de favoritos

**Teste de aceitação:**

* Usuário consegue salvar e reencontrar restaurantes facilmente

---

## 2.5 Recomendações personalizadas

**Teste unitário:**

* Algoritmos de recomendação e regras de personalização

**Teste de integração:**

* Integração entre histórico do usuário e motor de recomendação

**Teste de sistema:**

* Sistema sugere restaurantes com base no comportamento do usuário

**Teste de aceitação:**

* Usuário percebe valor nas recomendações exibidas

---

## 2.6 Compatibilidade Web e Mobile

**Teste unitário:**

* Componentes responsivos e específicos por plataforma

**Teste de integração:**

* Integração entre APIs e diferentes clientes (web e mobile)

**Teste de sistema:**

* Execução dos mesmos fluxos em múltiplos dispositivos

**Teste de aceitação:**

* Usuário tem experiência consistente em qualquer dispositivo

---

# ⚠️ Prioridades e Riscos

## 🔴 Alta criticidade

* **Busca de restaurantes**

  * Problema já identificado: resultados incorretos
  * Impacto direto na usabilidade principal do sistema

* **Sistema de avaliações**

  * Problema: avaliações desaparecendo
  * Impacta confiança e reputação da plataforma

* **Performance (lentidão em horários de pico)**

  * Afeta toda a experiência do usuário
  * Pode causar abandono do sistema

---

## 🟠 Média criticidade

* **Visualização de restaurantes**

  * Problema: telas confusas
  * Impacta experiência, mas não impede uso total

* **Compatibilidade Web e Mobile**

  * Problema: inconsistências entre plataformas
  * Impacta percepção de qualidade

---

## 🟢 Menor criticidade

* **Favoritos e recomendações**

  * Impacto mais relacionado à retenção do usuário
  * Não bloqueiam uso principal

---

# 🔺 Pirâmide de Testes

## Estratégia proposta

**Base: Testes unitários (maior volume)**

* Validar lógica de busca, avaliações e recomendações
* Reduzir bugs rapidamente

**Intermediário: Testes de integração**
Foco em:

* Busca + banco de dados
* Avaliações + persistência
* APIs entre web e mobile

**Topo: Testes de sistema e aceitação (menor volume)**
Fluxos críticos:

* Buscar restaurante
* Visualizar detalhes
* Avaliar restaurante

---

## 📌 Justificativa

* **Custo:** testes unitários são rápidos e baratos
* **Risco:** erros de lógica já estão causando problemas reais
* **Eficiência:** evitar excesso de testes end-to-end reduz manutenção
* **Foco atual:** corrigir regressões rapidamente após lançamento

---

# 🚀 Testes em Produção

✅ **Uso recomendado: Sim (com controle)**

Dado que o sistema já está em produção e apresenta falhas reais, testes em produção são essenciais.

## 📌 Situações ideais

* **Feature flags**

  * Testar correções em busca e avaliações para grupos reduzidos

* **Monitoramento de performance**

  * Identificar gargalos em horários de pico

* **Testes A/B**

  * Melhorar telas confusas com variações de UI

* **Logs e observabilidade**

  * Detectar falhas em smartphones específicos

* **Testes de smoke pós-deploy**

  * Garantir que funcionalidades principais continuam funcionando
