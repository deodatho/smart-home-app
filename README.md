# 🏠 Smart Home App

Sistema completo de automação residencial desenvolvido com **Python**, **KivyMD** e integração com **ESP32**, que permite o controle de dispositivos como lâmpadas, portão e janelas através de uma interface intuitiva e segura.

---

## 📱 Funcionalidades

- 🔐 Tela de **login e registro** com validação de senha forte
- 🧾 Autenticação com **tokens de sessão seguros** e tempo de expiração
- 💡 Controle manual das **lâmpadas**
- 🚪 Abertura e fechamento do **portão principal**
- 🪟 Abertura e fechamento das **janelas**
- ☀️ Cartão de clima (WeatherCard) dinâmico
- ⚙️ Tela de **configurações**
- 📊 Banco de dados SQLite com hash de senhas usando `pbkdf2_sha256`
- 🔐 Comunicação segura com o ESP32 via **HMAC + token**

---

## 🛠️ Tecnologias Usadas

- **Python 3**
- [**KivyMD**](https://kivymd.readthedocs.io/en/latest/) (interface moderna para Kivy)
- **ESP32** com servidor REST simples
- **SQLite3** para banco de dados local
- **Passlib** para hashing de senhas
- **HMAC (SHA-256)** para segurança nas requisições
- **Email-validator** para validação de emails

---

## 📦 Estrutura do Projeto

```
📁 screens/
   ├── login.py
   ├── register.py
   ├── home.py
   ├── weather_card.py
📁 assets/
   ├── database.py
   ├── send.py
📄 main.py
📄 smart_home.kv
```

---

## ▶️ Como Rodar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/smart-home-app.git
cd smart-home-app
```

2. **Crie um ambiente virtual (opcional mas recomendado):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Rode o app:**

```bash
python main.py
```

---

## 🌐 Comunicação com ESP32

O app se comunica com um ESP32 via IP local (ex: `192.168.38.58`) usando endpoints REST. Todas as requisições são autenticadas com:

- Token de sessão válido
- Token HMAC customizado com timestamp

⚠️ Certifique-se de que o ESP32 esteja na mesma rede que o dispositivo rodando o app.

---


## 🧠 Ideias Futuras

- Integração com assistente de voz
- Notificações em tempo real
- Histórico de comandos
- Controle via Web ou API externa

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## ✨ Autor

Desenvolvido com 💻 e paixão por **Deodatho de Oliveira e Daniel Tanguila**
