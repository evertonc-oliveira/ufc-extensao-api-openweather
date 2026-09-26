# Plano de ação — modelo

Rascunho em 11/09, versão final no Marco 1 (02/10). O roteiro completo, com exemplos e o critério de
cada campo, está no PDF `extensao/plano-de-acao.pdf` — leia antes de preencher.

**Duas páginas bastam.** Plano longo costuma esconder escopo mal resolvido. O que estiver aqui é o
que será cobrado nos três marcos.

---

## Identificação

- **Equipe:** Everton Campos de Oliveira (583258), Jonathan Pereira da Silva (582796), Raynnara Garces Ferreira (578630)
- **Trilha:** (B) curadoria e divulgação
- **Área temática da PREX:** Tecnologia e Produção
- **Por que essa área, em uma linha:** O projeto foca em capacitar iniciantes a utilizarem tecnologias de integração de dados (APIs) na prática.
- **Repositório:** https://github.com/evertonc-oliveira/ufc-extensao-api-openweather.git

## Campo 1 — O problema

Pessoas interessadas em aprender programação têm dificuldade em entender como conectar o código ao mundo real, precisando de exemplos práticos e visuais para compreenderem a utilidade de consumir dados de uma API.

## Campo 2 — O público externo

Pessoas em geral interessadas em aprender programação e tecnologia, que buscam projetos práticos para aplicar conceitos básicos, residentes principalmente em Fortaleza.
- **Duas ou três pessoas reais desse grupo:** Icaro Bezerra, Luiz Amorim e Natan Freire.
- **Já falamos com alguma? Quando falaremos?** Sim. O primeiro contato e o convite oficial aos três convidados foram realizados no dia 25/09.
- **Como essa pessoa vai descobrir que o produto existe:** Através de convite direto e pessoal realizado pela equipe para testar a oficina.

## Campo 3 — Trilha e produto

- **O que é, em uma frase que caiba num tuíte, e onde ficará publicado:** Um roteiro prático e uma oficina ensinando a consumir a API da OpenWeather para exibir o clima local numa página web simples. O material ficará no GitHub da equipe.
- **O que NÃO faz parte:** O desenvolvimento de sistemas web complexos, manutenção a longo prazo ou a prestação de suporte contínuo da ferramenta.

## Campo 4 — Fontes de dados

| | |
| :-- | :-- |
| Nome e órgão | OpenWeather (Current Weather Data API) |
| Endereço | https://openweathermap.org/current |
| Licença — e o que ela permite ao nosso produto | **Dados da API:** ODbL (Open Database License). Permite uso gratuito com limite de 60 requisições por minuto, exigindo atribuição obrigatória. Nosso roteiro terá um passo ensinando a inserir esses créditos na página.<br><br>**Nosso Produto:** Todo o material didático criado pela equipe (textos e exemplos) será disponibilizado sob licença **Creative Commons**, permitindo o uso e compartilhamento pelo público. |
| Atualização — periodicidade declarada e data do dado mais recente | Tempo real. |
| Dado pessoal? — se sim, granularidade e o que será agregado | Não. Dados puramente climáticos geolocalizados. |

## Campo 5 — Papéis

| Integrante | Papel | O que fica sob sua responsabilidade |
| :-- | :-- | :-- |
| Everton | Desenvolvedor de Referência | Estruturar o código base (gabarito) e garantir que as rotas da API estão fáceis de explicar. |
| Jonathan | Articulador Externo | Fazer o contato com os convidados, organizar a coleta de feedback e gerenciar as evidências. |
| Raynnara | Redatora Didática | Traduzir os passos técnicos para um roteiro em texto (Markdown) fácil de ser seguido pelo público. |

## Campo 6 — Cronograma

| Data | O que estará pronto |
| :-- | :-- |
| 02/10 (Marco 1) | Roteiro básico estruturado e código de referência (gabarito) subidos no repositório. |
| 13/11 (Marco 2) | Oficina ou teste do material aplicado com o público externo selecionado. |
| 27/11 (Marco 3) | Produto final refinado com base no retorno do público e diário de bordo preenchido com as evidências. |
| 04/12 (Socialização) | Apresentação pública dos resultados alcançados. |

**Dependências externas:** Geração da chave gratuita da OpenWeather (ocorre imediatamente no cadastro) e a disponibilidade de horário dos convidados para testar o roteiro.

## Campo 7 — Indicadores

| | Medida | Como será coletada | Valor que seria bom |
| :-- | :-- | :-- | :-- |
| Contagem | Pessoas que utilizaram o roteiro | Formulário de presença na oficina ou prints enviados mostrando a página pronta. | Pelo menos 3 pessoas de fora da universidade. |
| Qualitativa | Nível de clareza do material | Retorno escrito (mensagem no WhatsApp ou forms curto) após o teste. | Respostas indicando que o passo a passo da extração dos dados foi fácil de acompanhar. |

## Antes de entregar: a prova dos nove

- [ ] Riscamos tudo o que não conseguiríamos terminar até 13/11.
- [ ] O que sobrou ainda ajuda alguém.
- [ ] Uma pessoa de fora entende o Campo 1 e o Campo 3 sem explicação oral.
- [ ] A data da primeira conversa com o público está marcada.
- [ ] Os indicadores podem ser coletados sem depender de terceiro.

---

## Exemplo de campo preenchido

Para calibrar o tamanho e o tom — é o nível de concretude esperado, não um modelo a copiar.

> **Campo 1 — O problema.** Uma coordenadora pedagógica que quer comparar sua escola com a média do
> município precisa baixar uma planilha de 300 mil linhas e saber filtrar.
>
> **Campo 3 — Trilha e produto.** Uma API pública que devolve, por escola de Fortaleza, matrículas e
> infraestrutura do censo mais recente, com documentação e exemplo pronto para copiar. **Não** inclui
> série histórica nem painel visual.
>
> **Campo 7 — Indicadores.** Contagem: acessos únicos ao endereço público, pelo registro do
> servidor, entre 02/10 e 27/11; seria bom passar de 30. Qualitativa: retorno escrito de pelo menos
> duas pessoas de fora que usaram, coletado por e-mail depois do primeiro contato.
