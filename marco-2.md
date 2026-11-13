# Entrega de marco

## Identificação

- **Equipe:** Everton Campos de Oliveira, Jonathan Pereira da Silva e Raynnara Garces Ferreira
- **Marco e data:** Marco 2, 13/11/2026
- **Trilha:** B (curadoria e divulgação)
- **Endereço público do produto:** https://github.com/evertonc-oliveira/ufc-extensao-api-openweather
- **Commit ou tag desta entrega:** 346741c961a8aef82769c94ecb877ff6122fd0a3

## Campo 1 — O que funciona hoje

1. Acessar a URL `https://github.com/evertonc-oliveira/ufc-extensao-api-openweather/blob/main/README.md` e visualizar o roteiro completo com explicações detalhadas sobre como o produto funciona e o passo a passo de configuração para Windows e Linux.
2. Executar comandos preparatórios no terminal dentro da pasta do projeto — como `copy .env.example .env` e `pip install requests python-dotenv` — e obter respostas visuais imediatas confirmando a cópia do arquivo de ambiente (`1 arquivo(s) copiado(s)`) e a instalação das bibliotecas (`Successfully installed...`).
3. Rodar o comando `python clima.py` (ou `python3 clima.py` no Linux) no terminal e receber na tela o local (`Fortaleza`), a temperatura atual em graus Celsius, a condição climática e os créditos da OpenWeather.

## Campo 2 — O que mudou desde o marco anterior

- **Passou a existir:** O script de testes `test_clima.py` e o arquivo de configuração `.gitattributes`. As licenças foram modificadas e divididas (`DATA_LICENSE.md` e `LICENSE-ROTEIRO`), o `README.md` foi melhor detalhado e o arquivo `.env` foi oficialmente adotado para segurança das chaves.
- **Foi cortado, e por quê:** As instruções para macOS foram removidas do roteiro por falta de experiência com o sistema, mantendo o suporte apenas para Windows e Linux. Além disso,  o arquivo `testesimples.py` foi deletado pois não cumpria bem os requisitos de testes.

## Campo 3 — Alcance

| Indicador | Planejado | Obtido até hoje | Onde está a evidência |
| :-- | :-- | :-- | :-- |
| Pessoas que utilizaram o roteiro | 3 | 1 | `evidencias.csv` e `evidencias/` |

**O que o público externo disse:** "Achei fácil e intuitivo. Foi interessante. Achava que era mais complicado. Mudou um pouco minha percepção." — Luiz. O plano para atingir a meta até o próximo marco é aplicar o roteiro com os demais convidados previamente contatados (Icaro e Natan).

## Campo 4 — Obstáculo e replanejamento

Um dos maiores obstáculos técnicos foi realizar a limpeza profunda do histórico do Git (reescrita de commits e *garbage collection* no GitHub) para remover completamente dados sensíveis que haviam ficado registrados em versões anteriores, aliado ao cuidado contínuo para não expor chaves de API — o que exigiu ajustes no `.gitignore` e a padronização do `.env.example`. Além disso, a baixa contribuição geral da equipe e dificuldade de comunicação gerou sobrecarga e exigiu alguns replanejamentos.

## Campo 5 — Autopontuação

| Dimensão | n.a.? | Pts (0–2) | Por quê, em uma linha |
| :-- | :-- | :-- | :-- |
| D1 Qualidade técnica | | 1.5 | O código lida com erros e possui testes com mock, porém não é perfeito e a estrutura pode evoluir. |
| D2 Alcance e adequação ao público | | 1.0 | O produto funciona de ponta a ponta, porém apenas 1 usuário externo foi alcançado até o momento (a meta eram 3). |
| D3 Documentação e reprodutibilidade | | 2.0 | O roteiro (README) está bem consolidado, detalhado e cobre o necessário para o público reproduzir o projeto. |
| D4 Registro do processo | | 2.0 | As evidências, o arquivo CSV e o diário de bordo refletem com fidelidade os testes, bloqueios e o avanço real do processo. |
| D5 Autoavaliação e reflexão | x | n.a. | n.a. |

## Antes de entregar

- [x] O endereço do produto abre numa máquina que não é a nossa.
- [x] O que o Campo 1 promete foi testado hoje, não na semana passada.
- [x] O `README.md` corresponde ao que o produto faz agora.
- [x] O diário tem entrada de todas as semanas desde o último marco.
- [x] Toda evidência do Campo 3 tem data e está em `evidencias/`.
- [x] O commit informado está publicado.