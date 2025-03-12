import json
import os
from datetime import datetime, timedelta
from twilio.rest import Client

# Configurações do Twilio
TWILIO_ACCOUNT_SID = "SUA_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "SEU_AUTH_TOKEN"
TWILIO_WHATSAPP_NUMBER = "whatsapp:SEU_NUMERO_TWILIO"  # Número do Twilio no formato WhatsApp
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Arquivo para armazenar reuniões
REUNIOES_FILE = "reunioes.json"

# Carrega ou cria o arquivo de reuniões
def carregar_reunioes():
    if os.path.exists(REUNIOES_FILE):
        with open(REUNIOES_FILE, "r") as f:
            return json.load(f)
    return []

# Salva as reuniões no arquivo
def salvar_reunioes(reunioes):
    with open(REUNIOES_FILE, "w") as f:
        json.dump(reunioes, f, indent=4)

# Agenda uma nova reunião
def agendar_reuniao(titulo, data_hora, participantes):
    reunioes = carregar_reunioes()
    reuniao = {
        "titulo": titulo,
        "data_hora": data_hora,
        "participantes": participantes,
        "confirmacoes": {},  # Armazena as confirmações dos participantes
        "status": "agendada"
    }
    reunioes.append(reuniao)
    salvar_reunioes(reunioes)
    print(f"Reunião '{titulo}' agendada para {data_hora}.")

# Envia lembretes de reunião via WhatsApp
def enviar_lembretes_whatsapp():
    reunioes = carregar_reunioes()
    agora = datetime.now()
    for reuniao in reunioes:
        data_hora = datetime.strptime(reuniao["data_hora"], "%Y-%m-%d %H:%M")
        if data_hora - agora <= timedelta(hours=1) and reuniao["status"] == "agendada":
            for participante in reuniao["participantes"]:
                mensagem = f"Lembrete: Reunião '{reuniao['titulo']}' às {data_hora.strftime('%H:%M')}. Confirme presença respondendo 'SIM'."
                client.messages.create(
                    body=mensagem,
                    from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
                    to=f"whatsapp:{participante}"
                )
            reuniao["status"] = "lembrete_enviado"
            salvar_reunioes(reunioes)
            print(f"Lembretes enviados para a reunião '{reuniao['titulo']}' via WhatsApp.")

# Processa respostas de confirmação via WhatsApp
def processar_respostas_whatsapp():
    reunioes = carregar_reunioes()
    for reuniao in reunioes:
        if reuniao["status"] == "lembrete_enviado":
            for participante in reuniao["participantes"]:
                # Simulação: Verifica se o participante respondeu 'SIM'
                # No Twilio, você pode configurar um webhook para receber respostas
                resposta = "SIM"  # Simulação de resposta
                if resposta.upper() == "SIM":
                    reuniao["confirmacoes"][participante] = True
                else:
                    reuniao["confirmacoes"][participante] = False
            reuniao["status"] = "concluida"
            salvar_reunioes(reunioes)
            print(f"Respostas processadas para a reunião '{reuniao['titulo']}'.")

# Gera relatório semanal
def gerar_relatorio_semanal():
    reunioes = carregar_reunioes()
    agora = datetime.now()
    inicio_semana = agora - timedelta(days=agora.weekday())
    fim_semana = inicio_semana + timedelta(days=6)

    reunioes_semana = [
        r for r in reunioes
        if inicio_semana <= datetime.strptime(r["data_hora"], "%Y-%m-%d %H:%M") <= fim_semana
    ]

    relatorio = {
        "total_reunioes": len(reunioes_semana),
        "reunioes_realizadas": [r for r in reunioes_semana if r["status"] == "concluida"],
        "reunioes_faltantes": [r for r in reunioes_semana if r["status"] != "concluida"],
    }

    print("\n=== Relatório Semanal ===")
    print(f"Total de reuniões: {relatorio['total_reunioes']}")
    print(f"Reuniões realizadas: {len(relatorio['reunioes_realizadas']}")
    print(f"Reuniões faltantes: {len(relatorio['reunioes_faltantes'])}")
    print("\nDetalhes das reuniões realizadas:")
    for r in relatorio["reunioes_realizadas"]:
        print(f"- {r['titulo']} ({r['data_hora']})")
    print("\nDetalhes das reuniões faltantes:")
    for r in relatorio["reunioes_faltantes"]:
        print(f"- {r['titulo']} ({r['data_hora']})")

# Exemplo de uso
if __name__ == "__main__":
    # Agenda uma reunião
    agendar_reuniao(
        titulo="Reunião de Planejamento",
        data_hora="2023-10-30 15:00",
        participantes=["+5511999999999", "+5511888888888"]  # Números no formato internacional
    )

    # Envia lembretes via WhatsApp
    enviar_lembretes_whatsapp()

    # Processa respostas (simulação)
    processar_respostas_whatsapp()

    # Gera relatório semanal
    gerar_relatorio_semanal()
