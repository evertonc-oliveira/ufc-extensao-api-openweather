# Consulta Climática: Roteiro Prático com API
Um roteiro prático ensinando a consumir a API da OpenWeather para exibir o clima local através de coordenadas geográficas.

## Para quem é
Pessoas em geral interessadas em aprender programação e tecnologia, residentes principalmente em Fortaleza, que buscam projetos práticos para aplicar conceitos básicos.

## Como usar
### Passo 0: Crie sua chave de acesso
Acesse o site [openweathermap.org](https://openweathermap.org), clique em "Sign Up", preencha seus dados e confirme seu e-mail. Após fazer o login, clique no seu nome de usuário no canto superior direito, vá em "My API keys" e guarde a sequência de letras e números gerada lá (ela é o seu passe livre). Um detalhe importante: chaves recém-criadas costumam demorar cerca de 10 a 15 minutos para serem ativadas pelo sistema deles, então se o código der erro na sua primeiríssima tentativa, não se desespere, basta esperar um pouco e tentar rodar de novo.

### Passo 1: Verifique o Python  
Antes de tudo, o seu computador precisa entender a linguagem Python. Se você ainda não tem ele instalado, acesse o site oficial em [python.org](https://www.python.org), baixe a versão mais recente e faça a instalação. Uma dica muito importante: durante a instalação no Windows, lembre-se de marcar a caixinha que diz Add Python to PATH antes de clicar em instalar.

### Passo 2: Instale o conectador
Abra o terminal do seu computador (pesquise por Prompt de Comando ou CMD no menu do Windows, ou Terminal no Mac). Para o nosso código conseguir buscar dados na internet, você precisa instalar um pacote extra. Digite exatamente o comando abaixo na tela preta e aperte Enter:
```
pip install requests
```

### Passo 3: Prepare e execute o projeto  
Abra o arquivo `clima.py` em um editor de código (como o VS Code ou bloco de notas), substitua o texto COLOQUE_SUA_CHAVE_DA_API_AQUI pela sua chave gratuita da OpenWeather e salve. Depois, abra o terminal na mesma pasta onde o arquivo está salvo (dica: no Windows, apague o caminho na barra de endereços da pasta, digite cmd e dê Enter; no VS Code, vá no menu superior em "Terminal" e depois "New Terminal"). Com o terminal aberto no local exato, digite `python clima.py` e aperte Enter.

### O resultado será algo parecido com isso:

```
--- CLIMA ATUAL EM FORTALEZA ---
Temperatura: 30.05°C
Condição: Céu limpo

--- Créditos ---
Dados meteorológicos fornecidos por OpenWeather.
Licença: Open Data Commons Open Database License (ODbL).
```

## De onde vêm os dados
| Fonte | Órgão | Endereço | Data do dado |
| :-- | :-- | :-- | :-- |
| Current Weather Data API | OpenWeather | https://openweathermap.org/current | Em tempo real
| | | | |

## Licença
- **Dados:** ODbL (Open Database License), que exige atribuição obrigatória (créditos exibidos pelo nosso código).
- **Código e material desta equipe:** Creative Commons, permitindo uso e compartilhamento pelo público.

## O que este produto não faz
- Não abrange o desenvolvimento de sistemas web complexos.
- Não oferece manutenção a longo prazo ou prestação de suporte contínuo para a ferramenta.

## Contato
Equipe: Everton Campos de Oliveira, Jonathan Pereira da Silva e Raynnara Garces Ferreira.  
Problemas e dúvidas podem ser reportadas no repositório oficial da equipe.

## Onde está publicado
O roteiro básico estruturado e o código de referência encontram-se hospedados neste repositório do GitHub.

## Procedência dos números
| Número que aparece no material | Fonte | Como foi calculado |
| :-- | :-- | :-- |
| Temperatura atual | OpenWeather | Extraído diretamente do campo `temp` localizado dentro do dicionário `main` no JSON da resposta da API. |
| Descrição do clima | OpenWeather | Extraído do campo `description` contido no primeiro item da lista `weather` no JSON da resposta da API. |
| | | |

## Como adaptar para outro contexto
A aplicação pode ser adaptada para qualquer localidade do mundo. O usuário só precisa alterar as variáveis lat (Latitude) e lon (Longitude) no código para as coordenadas correspondentes à sua cidade.