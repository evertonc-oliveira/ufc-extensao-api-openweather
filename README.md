### Consulta Climática: Roteiro Prático com API

Um roteiro prático ensinando a consumir a API da OpenWeather para exibir o clima local através de coordenadas geográficas.

#### Para quem é
Pessoas em geral interessadas em aprender programação e tecnologia, residentes principalmente em Fortaleza, que buscam projetos práticos para aplicar conceitos básicos.

#### Como usar

##### Passo 0: Crie sua chave de acesso
Acesse o site openopenweathermap.org, clique em "Sign Up", preencha seus dados e confirme seu e-mail. Após entrar, acesse a aba **API keys** para obter ou gerar sua chave.

##### Passo 1: Verifique o Python
Antes de tudo, o seu computador precisa entender a linguagem Python. Abra o terminal e verifique se o Python está instalado:
```bash
python --version
```

##### Passo 2: Instale as bibliotecas necessárias
Abra o terminal do seu computador na pasta do projeto e instale os pacotes requeridos:
```bash
pip install requests python-dotenv
```
*(Nota no Windows: Se o comando `pip` não for reconhecido, utilize `python -m pip install requests python-dotenv`)*

##### Passo 3: Configure o arquivo de variáveis de ambiente (.env)
Para proteger sua chave da API e evitar expô-la publicamente no GitHub:

1. Crie um arquivo chamado **`.env`** na raiz do projeto (ou copie o modelo `.env.exemplo`).
2. Adicione a sua chave da OpenWeather da seguinte forma:
```env
OPENWEATHER_API_KEY=sua_chave_aqui
```

##### Passo 4: Execute o projeto
Com o terminal aberto na pasta do projeto, execute o script:
```bash
python clima.py
```

##### O resultado será algo parecido com isso:
```text
--- CLIMA ATUAL ---
📍 Local: Fortaleza
🌡️  Temperatura: 30.05°C
☁️  Condição: Céu limpo
-------------------
Créditos: Dados fornecidos por OpenWeather (ODbL).
```

##### Tratamento de Erros Integrado
O script `clima.py` conta com validações automáticas para diferentes cenários:
* **Conexão Segura (HTTPS):** As requisições são feitas obrigatoriamente via protocolo HTTPS.
* **Timeout Ajustado:** Requisições têm limite de resposta de 10 segundos para evitar travamentos.
* **Tratamento de Falta de Internet:** Exibe uma mensagem de alerta amigável e orientações caso não haja conexão com a rede.
* **Tratamento do Erro 401 (Não Autorizado):** Notifica caso a chave fornecida no `.env` esteja incorreta ou inativa, orientando os passos para solução.

#### De onde vêm os dados
| Origem | Dados | Licença |
| :--- | :--- | :--- |
| OpenWeather API | Temperatura e descrição do clima | ODbL |

#### Licença
* Dados: ODbL (Open Database License).
* Código e material desta equipe: Creative Commons.

Este software está licenciado sob a licença [MIT](LICENSE).

### Dados Meteorológicos
Os dados de clima são fornecidos por [OpenWeather](https://openweathermap.org) sob as licenças [CC BY-SA 4.0](https://creativecommons.org) e [ODbL](https://opendatacommons.org). Consulte o arquivo [DATA_LICENSE.md](DATA_LICENSE.md) para obter mais detalhes sobre o uso dos dados.

#### O que este produto não faz
* Não salva histórico de temperaturas.
* Não faz previsões para os próximos dias.

#### Contato
Equipe do Projeto de Extensão.

#### Procedência dos números
| Dado | Fonte |
| :--- | :--- |
| Coordenadas | Geolocalização de Fortaleza (-3.7319, -38.5267) |
