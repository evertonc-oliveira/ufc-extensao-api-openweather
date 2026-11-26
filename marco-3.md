# Entrega de marco — Marco 3

## Identificação

- **Equipe:** Everton Campos de Oliveira, Raynnara, Jonathan
- **Marco e data:** Marco 3, 27/11/2026
- **Trilha:** (B) curadoria e divulgação — roteiro prático com API pública
- **Endereço público do produto:** https://github.com/evertonc-oliveira/ufc-extensao-api-openweather
- **Commit ou tag desta entrega:** 9a1863a4b85f637b0194b7f666ffecb5773b373b

## Campo 1 — O que funciona hoje

1. Criar o arquivo de configuração local a partir do modelo rodando `copy .env.example .env` (Windows) ou `cp .env.example .env` (Linux) na pasta do projeto e preencher `OPENWEATHER_API_KEY=<sua_chave>` — gera o arquivo `.env` com a credencial da OpenWeather sem expor chaves no código-fonte.
2. Instalar as dependências executando `pip install requests python-dotenv` (Windows) ou `pip3 install requests python-dotenv` (Linux) — instala os pacotes `requests` e `python-dotenv` necessários para as requisições HTTP e leitura das variáveis de ambiente.
3. Executar `python clima.py` (Windows) ou `python3 clima.py` (Linux) no terminal — exibe os dados meteorológicos atuais de Fortaleza (`Local`, `Temperatura` em °C, `Condição` do céu e `Créditos: Dados fornecidos por OpenWeather (ODbL).`), além de validar os cenários de erro via `python -m unittest test_clima.py`.

## Campo 2 — O que mudou desde o marco anterior

- **Passou a existir:** Aplicação do teste prático e coleta de evidências com os dois convidados restantes (Ícaro em 21/11 e Natan em 25/11), alcançando 100% da meta de público externo; correção e padronização da seção de licenças no `README.md` (separando código sob MIT, roteiro sob CC BY 4.0 e dados da OpenWeather sob CC BY-SA 4.0 e ODbL); consolidação final do `evidencias.csv` e do `diario-de-bordo.md` até a semana de 27/11.
- **Foi cortado, e por quê:** Nenhuma entrega prevista no escopo foi cortada. Mantivemos o produto focado exclusivamente na consulta do clima atual (sem histórico de temperaturas ou previsão futura), pois os três participantes externos concluíram o tutorial sem bloqueios e relataram que o passo a passo já estava claro e completo.

## Campo 3 — Alcance

| Indicador | Planejado | Obtido até hoje | Onde está a evidência |
| :-- | :-- | :-- | :-- |
| Convites enviados para teste do roteiro | 3 | 3 | `evidencias.csv` e `evidencias/` |
| Pessoas externas que executaram o roteiro | 3 | 3 | `evidencias.csv` e `evidencias/` |
| Feedbacks qualitativos coletados | 3 | 3 | `evidencias.csv` e `evidencias/` |

**O que o público externo disse.** Os três convidados externos executaram o roteiro de ponta a ponta sem necessidade de ajustes no material:
- *"Achei fácil e intuitivo. Foi interessante. Achava que era mais complicado. Mudou um pouco minha percepção."* — Luiz.
- *"Sim, todas foram claras e achei bem tranquilo. Me senti feliz quando deu certo e mais informado. Achava um pouco complicado mas a facilidade do tutorial ajudou muito a conseguir fazer funcionar."* — Ícaro.
- *"Achei simples e bem explicado. Foi interessante entender como funciona a comunicação entre diferentes sistemas. Achava que era algo mais complicado. A experiência ajudou a compreender melhor como as APIs facilitam a troca de informações entre aplicações."* — Natan.

## Campo 4 — Obstáculo e replanejamento

Após o Marco 2, enfrentamos dificuldade para conciliar as demandas acadêmicas do semestre com a agenda dos dois convidados restantes, resultando na semana de 20/11 sem atividades técnicas registradas. Para contornar, dividimos a aplicação entre a equipe: Raynnara realizou o teste presencialmente com Ícaro (21/11) e, diante da inviabilidade de encontro presencial com o último convidado, Jonathan conduziu o teste de forma online via WhatsApp com Natan (25/11), garantindo a coleta completa dos prints e relatos antes do fechamento de 27/11.

## Campo 5 — Autopontuação

| Dimensão | n.a.? | Pts (0–2) | Por quê, em uma linha |
| :-- | :-- | :-- | :-- |
| D1 Qualidade técnica | | 1.5 | O código lida com erros e possui testes com mock, cumprindo o escopo funcional, embora possa ser melhorado em alguns aspectos. |
| D2 Alcance e adequação ao público | | 2.0 | O produto funciona de ponta a ponta e atingimos 100% da meta planejada (3 de 3 usuários externos alcançados com retorno positivo). |
| D3 Documentação e reprodutibilidade | | 2.0 | O roteiro (README) está consolidado, com as licenças corrigidas e detalhamento completo para o público reproduzir o projeto. |
| D4 Registro do processo | | 2.0 | As evidências, o arquivo `evidencias.csv` e o diário de bordo consolidado refletem com fidelidade todo o processo da equipe. |
| D5 Autoavaliação e reflexão | x | n.a. | n.a. |

## Antes de entregar

- [x] O endereço do produto abre numa máquina que não é a nossa.
- [x] O que o Campo 1 promete foi testado hoje, não na semana passada.
- [x] O `README.md` corresponde ao que o produto faz agora.
- [x] O diário tem entrada de todas as semanas desde o último marco.
- [x] Toda evidência do Campo 3 tem data e está em `evidencias/`.
- [x] O commit informado está publicado.