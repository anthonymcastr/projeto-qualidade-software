# Diagnóstico de Qualidade — Startup Local Eats

---

## Etapa 1 – Diagnóstico Organizacional

### Quais papéis provavelmente existem hoje na startup?

| Papel                      | Situação atual                                            |
| -------------------------- | --------------------------------------------------------- |
| Desenvolvedor              | Presente — responsável por criar e manter funcionalidades |
| Gerente de Produto         | Presente — define prioridades e valida entregas           |
| Analista de Sistemas       | Provavelmente ausente ou acumulado pelo desenvolvedor     |
| QA / Analista de Qualidade | Ausente ou informal — sem papel definido                  |
| DevOps                     | Ausente ou acumulado pelo desenvolvedor                   |

---

### Quem provavelmente está responsável pela qualidade atualmente?

A responsabilidade pela qualidade está **diluída e sem dono claro**. Na prática:

* Os desenvolvedores testam o próprio código quando têm tempo
* Não há critérios formais de aceite
* Não existe registro de defeitos
* O gerente de produto pode validar pontualmente, mas de forma inconsistente

---

### Quais problemas podem ocorrer quando as responsabilidades de qualidade não estão claras?

* Defeitos chegam à produção porque ninguém é responsável formalmente por testar antes da entrega
* Retrabalho elevado — bugs em produção custam mais para corrigir do que se detectados antes
* Pedidos duplicados e erros no checkout por ausência de testes nos fluxos críticos
* Falta de rastreabilidade — sem registro, os mesmos erros se repetem
* Conflito de prioridades — o desenvolvedor foca na entrega e não tem tempo para testar
* Perda de confiança dos usuários — problemas recorrentes afastam clientes e restaurantes

---

### A qualidade deve ser responsabilidade de uma pessoa ou de toda a equipe?

A qualidade deve ser uma **responsabilidade compartilhada por toda a equipe**, mesmo com um papel de QA definido:

* O **desenvolvedor** escreve código limpo e faz testes unitários
* O **analista** garante requisitos claros e testáveis
* O **gerente de produto** valida se a entrega atende ao negócio
* O **QA** coordena o processo, planeja testes e garante cobertura

---

## Etapa 2 – Proposta de Organização da Qualidade

### 1. Definição de papéis da equipe

#### 👨‍💻 Desenvolvedor

**Principais responsabilidades:**

* Implementar funcionalidades conforme os requisitos
* Escrever testes unitários para o próprio código
* Corrigir defeitos identificados pelo QA
* Participar de revisões de código (code review)

**Relação com a qualidade:**
Primeira linha de defesa. Código bem estruturado, testado e revisado reduz significativamente a quantidade de defeitos nas etapas seguintes.

---

#### 🔍 QA / Analista de Qualidade

**Principais responsabilidades:**

* Planejar e executar testes das funcionalidades
* Identificar, registrar e acompanhar defeitos
* Definir critérios de aceite junto ao time
* Realizar testes exploratórios e de regressão
* Validar funcionalidades antes da entrega em produção

**Relação com a qualidade:**
Guardião do processo de qualidade. Garante que os fluxos críticos sejam testados e que nada vá para produção sem validação.

---

#### 📋 Analista de Sistemas

**Principais responsabilidades:**

* Levantar, documentar e validar requisitos
* Garantir que histórias de usuário tenham critérios de aceite claros
* Fazer a ponte entre negócio e desenvolvimento

**Relação com a qualidade:**
Requisitos ambíguos são uma das principais causas de defeitos. O analista previne problemas antes do desenvolvimento começar.

---

#### ⚙️ DevOps

**Principais responsabilidades:**

* Gerenciar ambientes de desenvolvimento, homologação e produção
* Configurar e manter pipelines de CI/CD
* Garantir deploys seguros e rastreáveis
* Monitorar a saúde da aplicação em produção

**Relação com a qualidade:**
Garante que o processo de entrega seja confiável e repetível, reduzindo erros causados por deploys manuais e ambientes inconsistentes.

---

#### 🗂️ Gerente de Produto

**Principais responsabilidades:**

* Definir prioridades do backlog
* Validar entregas do ponto de vista do negócio
* Garantir que o produto atenda às necessidades dos clientes e restaurantes

**Relação com a qualidade:**
Valida se o que foi entregue resolve o problema correto, complementando a validação técnica do QA.

---

### 2. Responsabilidades relacionadas à qualidade

| Atividade                                    | Responsável principal | Apoio                  |
| -------------------------------------------- | --------------------- | ---------------------- |
| Definir critérios de aceite                  | Analista de Sistemas  | QA, Gerente de Produto |
| Testar funcionalidades antes da entrega      | QA                    | Desenvolvedor          |
| Registrar e acompanhar defeitos              | QA                    | Desenvolvedor          |
| Escrever testes unitários                    | Desenvolvedor         | —                      |
| Revisar código (code review)                 | Desenvolvedor         | QA                     |
| Realizar testes exploratórios                | QA                    | —                      |
| Validar requisitos antes do desenvolvimento  | Analista de Sistemas  | QA                     |
| Validar entrega do ponto de vista do negócio | Gerente de Produto    | QA                     |
| Garantir estabilidade dos ambientes          | DevOps                | —                      |
| Monitorar erros em produção                  | DevOps                | QA                     |

---

### 3. Práticas básicas de QA

#### ✅ Prática 1 — Critérios de aceite antes do desenvolvimento

Antes de qualquer funcionalidade entrar em desenvolvimento, QA, analista e gerente de produto alinham o que precisa funcionar para a entrega ser aceita. Evita retrabalho e garante expectativas alinhadas.

#### ✅ Prática 2 — Testes manuais dos fluxos críticos a cada entrega

Antes de qualquer deploy em produção, o QA executa testes manuais nos fluxos mais importantes: realização de pedido, pagamento e recebimento pelo restaurante.

#### ✅ Prática 3 — Registro e acompanhamento de bugs em ferramenta dedicada

Todo defeito identificado deve ser registrado (GitHub Issues, Jira ou similar) com descrição clara, passos para reproduzir e prioridade. Evita que bugs sejam esquecidos e permite rastrear reincidências.

#### ✅ Prática 4 — Testes exploratórios periódicos

O QA realiza sessões de teste exploratório para descobrir comportamentos inesperados que os testes formais não cobriram. Recomenda-se ao menos uma sessão por sprint.

#### ✅ Prática 5 — Revisão de código entre desenvolvedores (code review)

Nenhum código vai para produção sem revisão de outro desenvolvedor. Reduz defeitos, melhora a qualidade do código e distribui o conhecimento do sistema entre a equipe.

---

## Etapa 3 – Anúncios de Contratação da Startup

### Vaga 1 — QA / Analista de Qualidade de Software

**Empresa:** Local Eats
**Local:** Porto Alegre — RS
**Modelo:** Híbrido
**Nível:** Júnior / Pleno

#### Sobre a vaga

A Local Eats está estruturando sua área de qualidade e busca um profissional de **QA** para garantir que a plataforma funcione de forma confiável para clientes e restaurantes. A pessoa atuará junto a desenvolvedores e analistas para planejar testes, identificar riscos e validar entregas.

#### Principais responsabilidades

* Planejar e executar testes manuais das funcionalidades
* Identificar, registrar e acompanhar defeitos até a resolução
* Definir critérios de aceite junto ao time de produto
* Realizar testes exploratórios e de regressão
* Validar funcionalidades antes da entrega em produção
* Contribuir para a melhoria contínua dos processos de qualidade

#### Requisitos obrigatórios

* Conhecimento de fundamentos de teste de software (tipos de teste, ciclo de vida do defeito)
* Habilidade para documentar defeitos de forma clara e reproduzível
* Boa comunicação e perfil colaborativo
* Organização e atenção a detalhes

#### Requisitos desejáveis

* Experiência com testes de aplicações web e mobile
* Conhecimento de ferramentas de gestão de defeitos (Jira, GitHub Issues ou similares)
* Noções de SQL para validação de dados
* Conhecimento básico de Git
* Noções de automação de testes (Selenium, Cypress ou similares)

#### Certificações desejáveis

* ISTQB — CTFL (Certified Tester Foundation Level)

---

### Vaga 2 — Desenvolvedor(a) Full Stack

**Empresa:** Local Eats
**Local:** Porto Alegre — RS
**Modelo:** Híbrido
**Nível:** Pleno

#### Sobre a vaga

A Local Eats busca um(a) **Desenvolvedor(a) Full Stack** para integrar o time de produto e contribuir com o desenvolvimento e manutenção da plataforma de pedidos online. Buscamos alguém comprometido com a qualidade da entrega — escrevendo testes, participando de code reviews e colaborando com o QA.

#### Principais responsabilidades

* Desenvolver e manter funcionalidades do sistema (front-end e back-end)
* Escrever testes unitários e de integração
* Participar de revisões de código (code review)
* Colaborar com o QA na identificação e correção de defeitos
* Apoiar o processo de deploy e monitoramento da aplicação

#### Requisitos obrigatórios

* Experiência com desenvolvimento web (front-end e back-end)
* Conhecimento de pelo menos uma linguagem back-end (Node.js, Python, Java ou similar)
* Experiência com frameworks front-end (React, Vue ou similar)
* Conhecimento de banco de dados relacionais (SQL)
* Familiaridade com Git e fluxo de trabalho em equipe (pull requests, branches)

#### Requisitos desejáveis

* Experiência com escrita de testes automatizados (unitários e de integração)
* Conhecimento de práticas de CI/CD
* Experiência com APIs REST
* Conhecimento básico de Docker
* Experiência em ambiente de startup ou produto digital

#### Certificações desejáveis

* Certificações em cloud (AWS, GCP ou Azure — nível Associate)
* Cursos de boas práticas de desenvolvimento (Clean Code, TDD)
