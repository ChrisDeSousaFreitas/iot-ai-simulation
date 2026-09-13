# Clyvo SmartCare - IoT & AI Integration

**🎥 Vídeo de Apresentação (Pitch):** [https://youtu.be/ubgFWe9V_t8]

---

## 👥 Equipe

| Integrante | RM |
| :--- | :--- |
| Bruno Andrade Zanateli | 563736 |
| Christian S. Freitas | 566098 |
| Pedro Pereira Biasolli | 562521 |
| Rodrigo Tiezzi | 562975 |
| Matheus Enrico Souza | 562532 |

## ⚠️ Aviso sobre a API Key (Segurança)

No arquivo `clyvo_ai.py`, a variável `GOOGLE_API_KEY` está preenchida com o valor `"COLE_SUA_API_KEY_AQUI"`. A chave real foi intencionalmente removida do repositório público por questões de segurança. O GitHub possui um sistema de *Secret Scanning* que bloqueia commits contendo chaves ativas para evitar vazamentos e acessos indevidos. Para executar o código localmente e testar a integração, basta utilizar a chave temporária enviada no arquivo `.zip` da entrega oficial.

---

## 🧠 Módulo de Inteligência Artificial e IoT (Disruptive Architectures)

### 1. O Problema a ser Resolvido
A ausência de monitoramento contínuo entre consultas veterinárias dificulta o diagnóstico precoce de anomalias. O **Clyvo AI** atua integrando Internet of Behaviors (IoB) com telemetria IoT, resolvendo a angústia do tutor e a falta de dados da clínica através de uma triagem inteligente e em tempo real.

### 2. Abordagem de IA Adotada e Justificativa
Foi adotada a **IA Generativa (LLM)** atuando como um motor de inferência contextual.
*Justificativa Técnica:* Modelos estritamente preditivos ou motores de regras (ex: BPM > 120 = Perigo) são ineficazes na medicina veterinária, onde a normalidade varia drasticamente entre espécies exóticas e portes. O LLM permite cruzar a biometria fria do IoT com o contexto clínico complexo anotado em texto, gerando alertas humanizados.

### 3. Dados Utilizados (Origem e Estrutura)
* **Dados Estáticos (Banco de Dados):** Nome, Espécie, Idade e Histórico Clínico (ex: "Sensível a altas temperaturas").
* **Dados Dinâmicos (Telemetria IoT):** Frequência cardíaca (BPM) e Status de agitação do acelerômetro.

### 4. Diagrama Arquitetural e Fluxo de Dados

```mermaid
graph TD
    A[Coleira Smart IoT] -->|Frequência Cardíaca e Agitação| B(Motor Clyvo AI - Backend)
    C[(Banco de Dados)] -->|Idade, Espécie, Histórico| B
    B -->|JSON Contextualizado + Prompt| D[Google Gemini API / LLM]
    D -->|Análise: Urgência e Recomendação| B
    B -->|Alerta Humanizado| E[Interface do App do Tutor]