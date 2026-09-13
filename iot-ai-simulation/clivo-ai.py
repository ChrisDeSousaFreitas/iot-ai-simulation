!pip install -q -U google-genai

import json
from google import genai

GOOGLE_API_KEY = "AQ.Ab8RN6KPi9qjdzw8rJdNZp-HgoFPvrdu9VnQQGkLitr7bIjYNg"
client = genai.Client(api_key=GOOGLE_API_KEY)

dados_banco_clyvo = {
    "nome": "Spider",
    "especie": "Tarântula Viúva Negra",
    "idade": "Adulta",
    "historico_clinico": "Nenhuma comorbidade. Sensível a altas temperaturas."
}

dados_telemetria_iot = {
    "frequencia_cardiaca_bpm": 150,
    "status_iot": "Alerta: Agitação/Stress"
}

print("📡 Recebendo dados do Smart Collar...\n")
print(f"BPM Atual: {dados_telemetria_iot['frequencia_cardiaca_bpm']} | Status: {dados_telemetria_iot['status_iot']}")
print("🧠 Iniciando análise de Inteligência Artificial...\n")

prompt_arquitetura = f"""
Você é o 'Clyvo AI', um assistente clínico veterinário especializado em todas as espécies, incluindo animais exóticos.
O nosso sistema IoT detectou uma anomalia. Analise o contexto abaixo:

Perfil do Paciente: {json.dumps(dados_banco_clyvo)}
Telemetria em Tempo Real (IoT): {json.dumps(dados_telemetria_iot)}

Atue como um sistema de apoio à tomada de decisão. Retorne estritamente:
1. Nível de Urgência (Baixo, Médio, Alto).
2. Uma explicação simples e humanizada para o tutor sobre o que esse BPM significa para ESSA espécie específica.
3. Recomendação de ação imediata.
"""

resposta_ia = client.models.generate_content(
    model='gemini-3.6-flash',
    contents=prompt_arquitetura
)

print("================ DIAGNÓSTICO CLYVO AI ================")
print(resposta_ia.text)
print("======================================================")