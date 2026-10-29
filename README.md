# Consulta Climática: Roteiro Prático com API

Um roteiro prático ensinando a consumir a API da OpenWeather para exibir o clima local através de coordenadas geográficas.

### Para quem é?

Pessoas interessadas em aprender conceitos básicos de programação, sem necessidade de experiência prévia.

### Como usar passo a passo?

##### Passo 1: Instalação do Python

1. Acesse o site oficial: https://www.python.org/downloads/ e baixe a versão mais recente.

2. Execute o arquivo baixado.

3. IMPORTANTE (Windows): Na primeira tela do instalador, marque a caixa de seleção "Add Python to PATH" ou "Add python.exe to PATH" antes de clicar em "Install Now".

##### Passo 2: Criação da chave da API

1. Acesse o site https://openweathermap.org/ e clique em "Sign Up".

2. Preencha o formulário para criar uma conta e confirme seu endereço de e-mail.

3. Após o login, clique no seu nome de usuário no canto superior direito e selecione "My API keys".

4. Copie a sequência de letras e números gerada na tela. Esta é a sua chave. (Pode levar alguns minutos para a chave ser ativada pelo sistema).

##### Passo 3: Download do projeto

1. Acesse a página do repositório: https://github.com/evertonc-oliveira/ufc-extensao-api-openweather

2. Clique no botão verde escrito "Code" e selecione a opção "Download ZIP".

3. Localize o arquivo baixado no seu computador, clique com o botão direito sobre ele e selecione "Extrair Tudo..." (ou "Extrair Aqui").

4. Entre na pasta que foi extraída.

##### Passo 4: Configuração da chave

1. Dentro da pasta extraída, localize o arquivo chamado `.env.example`.

2. Renomeie este arquivo para apenas `.env` (remova a parte ".example").

3. Abra o arquivo `.env` usando um editor de texto simples (como o Bloco de Notas no Windows, o TextEdit no Mac ou o Gedit no Linux).

4. Apague o texto "sua_chave_aqui" e cole a chave que você copiou no Passo 2. O conteúdo do arquivo deve ficar exatamente assim, sem espaços extras ou aspas:
   `OPENWEATHER_API_KEY=chave_copiada_aqui`

5. Salve e feche o arquivo.

##### Passo 5: Preparação do ambiente

1. Abra o terminal do seu sistema operacional diretamente na pasta do projeto:

   * No Windows: Abra a pasta do projeto, clique na barra de endereços no topo da janela, digite `cmd` e pressione Enter.

   * No Mac: Abra a pasta, clique com o botão direito do mouse na janela e selecione "Novo Terminal na Pasta".

   * No Linux: Abra a pasta do projeto, clique com o botão direito do mouse em um espaço vazio dentro da janela e selecione "Abrir no Terminal".

2. No terminal que se abrirá, digite o comando abaixo e pressione Enter para instalar as dependências necessárias:

   ```
   pip install requests python-dotenv
   
   ```

   *(Nota para Windows: Se o comando acima retornar um erro, tente utilizar `python -m pip install requests python-dotenv`)*

##### Passo 6: Execução do código

1. No mesmo terminal, digite o comando abaixo e pressione Enter:

   ```
   python clima.py
   
   ```

2. O resultado exibido no terminal será semelhante a este:

   ```
   --- CLIMA ATUAL ---
   Local: Fortaleza
   Temperatura: 30.05°C
   Condição: Céu limpo
   -------------------
   Créditos: Dados fornecidos por OpenWeather (ODbL).
   
   ```

#### Como funciona?

Quando você executa o comando final, o seguinte processo ocorre em frações de segundo:

1. O seu computador (através do Python) se conecta à internet e envia uma requisição para os servidores da OpenWeather.

2. Nessa requisição, o Python envia a sua Chave de API (para provar que você tem autorização) e as coordenadas da cidade de Fortaleza.

3. O servidor da OpenWeather valida a sua chave e reúne os dados meteorológicos atuais daquele local.

4. O servidor devolve esses dados para o seu computador em um formato de texto bruto.

5. O script Python lê esse texto, filtra apenas as informações relevantes (como a temperatura e a condição) e as exibe de forma limpa e legível no seu terminal.

#### Tratamento de Erros Integrado

O script `clima.py` possui validações para orientar o usuário em caso de falhas:

* Conexão Segura: As requisições utilizam obrigatoriamente o protocolo HTTPS.

* Ausência de Internet: Exibe instruções caso o computador esteja desconectado da rede.

* Timeout: Limite de resposta configurado para 10 segundos para evitar travamentos.

* Chave Inválida (Erro 401): Notifica o usuário e fornece instruções claras caso a chave no arquivo `.env` esteja incorreta ou inativa.

#### De onde vêm os dados

| Origem | Dados | Licença | 
| ----- | ----- | ----- | 
| OpenWeather API | Temperatura e descrição do clima | ODbL | 

#### Licença

* Dados: ODbL (Open Database License).

* Código e material desta equipe: Creative Commons.

Este software está licenciado sob a licença [MIT](LICENSE).

### Dados Meteorológicos

Os dados de clima são fornecidos por [OpenWeather](https://openweathermap.org) sob as licenças [CC BY-SA 4.0](https://creativecommons.org) e [ODbL](https://opendatacommons.org). Consulte o arquivo [DATA_LICENSE.md](DATA_LICENSE.md) para obter detalhes sobre o uso.

#### Limitações

* O sistema não salva histórico de temperaturas.

* O sistema não fornece previsões meteorológicas futuras.

#### Contato

Equipe do Projeto de Extensão da UFC.

#### Procedência dos números

| Dado | Fonte | 
| ----- | ----- | 
| Coordenadas | Geolocalização de Fortaleza (-3.7319, -38.5267) | 
