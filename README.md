# Sailor

# Sistema de Agendamento de Reuniões com WhatsApp

Este projeto é um sistema simples para **agendar reuniões**, **enviar lembretes via WhatsApp**, **verificar presença** e **gerar relatórios semanais**. Ele foi desenvolvido para facilitar a organização de reuniões e garantir que os participantes sejam lembrados e confirmem sua presença de forma fácil e rápida.

---

## Funcionalidades Principais

- **Agendamento de Reuniões**: Agende reuniões com título, data, hora e lista de participantes.
- **Lembretes Automáticos**: Envia lembretes via WhatsApp uma hora antes da reunião.
- **Confirmação de Presença**: Os participantes confirmam presença respondendo ao WhatsApp.
- **Relatório Semanal**: Gera um relatório das reuniões realizadas, presenças e faltas.

---

## Pré-requisitos

Antes de começar, você precisará de:
- **Python 3.8 ou superior** instalado no seu computador.
- Uma conta no [Twilio](https://www.twilio.com/) com um número de WhatsApp configurado.
- Um número de WhatsApp válido para enviar e receber mensagens.

---

## Como Configurar o Projeto

### 1. Instale as Dependências

O projeto usa a biblioteca `twilio` para enviar e receber mensagens via WhatsApp. Para instalar as dependências, execute o seguinte comando no terminal:

```bash
pip install -r requirements.txt
```

### 2. Configure o Twilio

1. **Crie uma conta no Twilio**: Acesse [Twilio](https://www.twilio.com/) e crie uma conta gratuita.
2. **Ative o WhatsApp no Twilio**: No painel do Twilio, vá para **Messaging > Try it Out > Send a WhatsApp Message** e siga as instruções para configurar o número do Twilio para WhatsApp.
3. **Obtenha suas credenciais**:
   - No painel do Twilio, copie o `ACCOUNT_SID` e o `AUTH_TOKEN`.
   - Anote o número do Twilio no formato `whatsapp:+14155238886`.

4. **Configure as credenciais no projeto**:
   No arquivo `main.py`, substitua os seguintes valores pelas suas credenciais do Twilio:

   ```python
   TWILIO_ACCOUNT_SID = "SUA_ACCOUNT_SID"
   TWILIO_AUTH_TOKEN = "SEU_AUTH_TOKEN"
   TWILIO_WHATSAPP_NUMBER = "whatsapp:SEU_NUMERO_TWILIO"
   ```

### 3. Adicione os Participantes

No arquivo `main.py`, adicione os números dos participantes no formato internacional (ex: `+5511999999999`). Certifique-se de que os números estejam associados a contas de WhatsApp válidas.

---

## Como Usar o Sistema

### 1. Agendar uma Reunião

Para agendar uma reunião, use a função `agendar_reuniao` no arquivo `main.py`. Exemplo:

```python
agendar_reuniao(
    titulo="Reunião de Planejamento",
    data_hora="2023-10-30 15:00",
    participantes=["+5511999999999", "+5511888888888"]
)
```

### 2. Enviar Lembretes via WhatsApp

Para enviar lembretes de reunião via WhatsApp, use a função `enviar_lembretes_whatsapp`:

```python
enviar_lembretes_whatsapp()
```

Os participantes receberão uma mensagem como:
```
Lembrete: Reunião 'Reunião de Planejamento' às 15:00. Confirme presença respondendo 'SIM'.
```

### 3. Processar Respostas dos Participantes

Para processar as respostas dos participantes, use a função `processar_respostas_whatsapp`:

```python
processar_respostas_whatsapp()
```

O sistema verificará as respostas e marcará a presença dos participantes.

### 4. Gerar Relatório Semanal

Para gerar um relatório das reuniões da semana, use a função `gerar_relatorio_semanal`:

```python
gerar_relatorio_semanal()
```

O relatório será exibido no terminal, mostrando:
- Total de reuniões agendadas.
- Reuniões realizadas e faltantes.
- Detalhes de cada reunião.

---

## Estrutura do Projeto

- `main.py`: Script principal do sistema.
- `reunioes.json`: Armazena os dados das reuniões.
- `requirements.txt`: Lista de dependências do Python.
- `README.md`: Documentação do projeto.

---

## Exemplo Completo

Aqui está um exemplo completo de como usar o sistema:

1. Agende uma reunião:
   ```python
   agendar_reuniao(
       titulo="Reunião de Planejamento",
       data_hora="2023-10-30 15:00",
       participantes=["+5511999999999", "+5511888888888"]
   )
   ```

2. Envie lembretes:
   ```python
   enviar_lembretes_whatsapp()
   ```

3. Processe as respostas:
   ```python
   processar_respostas_whatsapp()
   ```

4. Gere o relatório semanal:
   ```python
   gerar_relatorio_semanal()
   ```

---

## Perguntas Frequentes

### 1. Posso usar outro serviço além do Twilio?
No momento, o sistema foi projetado para funcionar com o Twilio. No entanto, você pode adaptá-lo para usar outros serviços de mensagens.

### 2. Como receber respostas dos participantes?
O Twilio permite configurar um webhook para receber respostas dos participantes. Consulte a [documentação do Twilio](https://www.twilio.com/docs/whatsapp/api) para mais detalhes.

### 3. Posso rodar o projeto em um servidor?
Sim, você pode rodar o projeto em um servidor ou em um serviço de nuvem como o Vercel (no caso usaremos esse), Google Cloud ou AWS.

---

## Contribuição

Se você quiser contribuir para este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```
