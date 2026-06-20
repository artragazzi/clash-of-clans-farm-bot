# COC Bot

Bot em Python para automatizar ataques no Clash of Clans usando reconhecimento de imagens na tela com `pyautogui`.

## Ambiente usado nos testes

Este projeto foi testado usando:

- BlueStacks 5
- Monitor Full HD, resolucao 1920x1080
- Clash of Clans aberto no emulador

Como o bot depende de imagens e coordenadas da tela, mudancas de resolucao, escala do Windows, tamanho da janela do BlueStacks ou layout do jogo podem fazer o reconhecimento falhar.

## Requisitos

- Python instalado
- BlueStacks 5
- Clash of Clans configurado e logado
- Dependencias Python:

```bash
pip install pyautogui python-dotenv requests opencv-python
```

O `opencv-python` e necessario para o uso de `confidence` nas buscas de imagem do `pyautogui`.

## Preparacao antes de rodar

1. Abra o BlueStacks 5.
2. Deixe o Clash of Clans aberto na tela principal da vila.
3. Use preferencialmente monitor Full HD em 1920x1080.
4. Evite mudar o tamanho da janela do BlueStacks depois de capturar ou ajustar as imagens.
5. Deixe o Guardiao sem skins.
6. Equipe o Guardiao com os equipamentos de joias.
7. Leve somente a tropa usada pelo bot e o Guardiao.

Levar apenas a tropa e o Guardiao ajuda o ataque terminar mais rapido, evitando que o bot fique esperando unidades extras finalizarem a batalha.

## Como executar

Na pasta do projeto, rode:

```bash
python app.py
```

Depois de iniciar, o bot faz o seguinte ciclo:

1. Clica em atacar.
2. Procura partida.
3. Inicia o ataque.
4. Verifica se a vila atende ao indicador esperado.
5. Se nao atender, pula para a proxima vila.
6. Quando encontrar uma vila valida, seleciona a tropa e o Guardiao.
7. Dropa as unidades no ponto configurado.
8. Monitora o fim do ataque.
9. A cada 3 ataques, envia uma captura pelo Telegram, se configurado.

Para parar rapidamente caso algo saia do controle, jogue o mouse para o canto superior esquerdo da tela. O `pyautogui.FAILSAFE` esta ativado no codigo.

## Telegram

O bot pode enviar screenshots e aceitar pausa por comandos do Telegram. Para isso, crie um arquivo `.env` na raiz do projeto com:

```env
TELEGRAM_TOKEN=seu_token_do_bot
TELEGRAM_CHAT_ID=seu_chat_id
```

Comandos disponiveis:

- `/stop`: pausa o bot.
- `/continue`: retoma a execucao.

Se nao quiser usar Telegram, mantenha essas variaveis sem configurar e remova ou ignore essa parte do fluxo.

## Imagens usadas pelo bot

As imagens ficam na pasta `images` e sao usadas para localizar botoes, tropas e indicadores na tela:

- `botao_atacar.png`
- `botao_procurar_partida.png`
- `botao_iniciar_ataque.png`
- `indicar_achou_vila.png`
- `proxima_vila.png`
- `dg_eletrico.png`
- `guardiao.png`
- `finalizar_ataque.png`

Se o bot nao encontrar algum elemento, provavelmente a imagem nao bate com o que aparece na sua tela. Nesse caso, tire uma nova captura do elemento no mesmo ambiente em que o bot vai rodar e substitua o arquivo correspondente.

## Usando outra tropa

O bot esta configurado para usar a imagem `images/dg_eletrico.png`, referenciada no codigo como `SELECAO_ELETRICO`.

Para usar outra tropa:

1. Tire um print recortado da nova tropa na barra de tropas.
2. Substitua a imagem `images/dg_eletrico.png` pela nova imagem, ou crie outro arquivo dentro de `images`.
3. Se usar outro nome de arquivo, ajuste esta linha no `app.py`:

```python
SELECAO_ELETRICO = os.path.join("images","dg_eletrico.png")
```

4. Se o ponto de drop ou o tempo de segurar o mouse precisar mudar, ajuste a funcao `dropar_tropas()` no `app.py`.

Atualmente o drop usa a coordenada fixa:

```python
pyautogui.moveTo(280,480, duration=0.5)
```

Se sua resolucao, janela ou estrategia forem diferentes, essa coordenada pode precisar ser alterada.

## Observacoes importantes

- Nao use skins no Guardiao, pois a imagem `guardiao.png` precisa bater com o visual dele na barra de tropas.
- Use os equipamentos de joias no Guardiao, conforme o ambiente testado.
- Evite mexer no mouse ou no teclado enquanto o bot esta executando.
- O bot depende da tela estar visivel. Nao minimize o BlueStacks.
- Qualquer alteracao visual no jogo pode exigir novas imagens na pasta `images`.
