# EP3 — Simulação de Captura de Pokémons

## Visão Geral

Este programa simula um jogo onde um treinador lança pokébolas para capturar Pokémons dispostos em um terreno retangular. A simulação utiliza física de projéteis simplificada (com gravidade) e representa o terreno como uma matriz bidimensional.

**Autor:** João Lucas Rodrigues (NUSP: 10787268)  
**Disciplina:** MAC115 - Introdução à Computação (Turma 2020-222)

---

## Constantes

| Constante  | Valor | Significado                              |
|------------|-------|------------------------------------------|
| `DELTA_T`  | 0.1   | Intervalo de tempo da simulação (segundos) |
| `GRAVIDADE` | 2     | Aceleração da gravidade (m/s²)           |

A gravidade é simplificada (2 em vez de 9.8) para tornar o jogo mais jogável.

---

## Estrutura de Dados

### Arquivo de entrada (`entrada.txt`)

```
m n
Nome1 raio1 x1 y1
Nome2 raio2 x2 y2
...
```

- A primeira linha contém as dimensões da matriz: `m` (linhas/altura) e `n` (colunas/largura)
- Cada linha subsequente descreve um Pokémon: nome, raio da área de captura, coordenada x, coordenada y

### Matriz

- Criada com dimensões `m × n`, inicializada com zeros
- Cada Pokémon ocupa uma região quadrada de lado `2 × raio`, centrada em `(x, y)`, preenchida com seu ID (1, 2, 3, …)
- A linha 0 representa o chão — é onde o treinador fica
- Pokemon na posição (x,y) aparece como um quadrado de colunas `x-raio..x+raio` e linhas `y-raio..y+raio`

---

## Explicação das Funções

### `leArquivo(nomeArquivo='entrada.txt')`

Lê o arquivo de entrada e retorna uma lista de listas:
- `resultado[0]` → `[m, n]` (dimensões como strings)
- `resultado[1]` → lista de pokémons, cada um no formato `[nome, raio, x, y]`, com raio/x/y convertidos para inteiros

### `criaMatriz(m, n)`

Cria uma matriz `m × n` preenchida com zeros. Implementada com dois loops aninhados: um para linhas, outro para colunas.

### `preenchePokemon(matriz, id, x, y, raio)`

Função auxiliar que insere um Pokémon na matriz. Percorre a região quadrada de lado `2 × raio` centrada em `(x, y)` e preenche cada célula com `id + 1` (o `+1` serve para que o primeiro Pokémon tenha ID 1, não 0).

Algoritmo:
```
para i de (y - raio) até (y + raio):
    para j de (x - raio) até (x + raio):
        matriz[i][j] = id + 1
```

### `populaMatriz(matriz, pokemons)`

Percorre a lista de Pokémons e chama `preenchePokemon` para cada um, atribuindo IDs sequenciais (1, 2, 3…).

### `removePokemon(matriz, id, pokemons)`

Remove um Pokémon da matriz, substituindo todos os valores na sua região quadrada por zero. Usa o mesmo princípio de varredura retangular de `preenchePokemon`.

### `imprimeMatriz(matriz)`

Imprime a matriz com **espelhamento vertical**: começa da última linha e imprime até a primeira. Isso porque a linha 0 representa o chão — visualmente, imprimir de baixo para cima faz o chão aparecer na parte inferior da tela.

- Células com valor `0` são impressas como `.`
- Células com Pokémon são impressas com o número do ID

### `atualizaPosicao(x, y, vx, vy, dt=DELTA_T)`

Aplica as equações de movimento de projétil:

```
x' = x + vx × dt
y' = y + vy × dt − (g/2) × dt²
```

Retorna `[x', y']`.

### `atualizaVelocidade(vx, vy, dt=DELTA_T)`

Aplica a ação da gravidade sobre a velocidade vertical:

```
vx' = vx
vy' = vy − g × dt
```

Retorna `[vx', vy']`.

### `grau2Radiano(theta)`

Converte ângulo de graus para radianos: `θ_rad = θ × π / 180`

### `copiaMatriz(matriz, m, n)`

Cria uma cópia independente da matriz. Usada para gerar a matriz de exibição (`P`), que mostra a trajetória da pokébola sem modificar a matriz original (`M`).

---

## Fluxo Principal (`main`)

1. **Entrada do usuário:** nome do arquivo, número N de pokébolas, coordenada x inicial do treinador
2. **Inicialização:** lê o arquivo, cria a matriz `M` com as dimensões lidas, popula `M` com os Pokémons
3. **Loop principal:** executa enquanto houver pokébolas (`N > 0`) e Pokémons não capturados (`num_poke > 0`)

### Para cada lançamento:

1. Exibe pokébolas restantes e estado da matriz
2. Marca a posição do treinador com `"T"` na linha 0
3. Cria uma cópia `P` da matriz para exibição da trajetória
4. Lê a velocidade e o ângulo de lançamento
5. Calcula `vx` e `vy` iniciais via decomposição trigonométrica

### Simulação da trajetória (loop interno):

A cada passo de tempo `dt`:

1. Se a pokébola está no limite horizontal da matriz e com velocidade apontando para fora → **errou**, imprime e encerra o lançamento
2. Atualiza posição e velocidade com as funções físicas
3. Arredonda `(x, y)` para inteiros (posição na matriz)
4. **Verificações da nova posição:**
   - Se `y` está acima da matriz (`y > m-1`) → a pokébola ainda está no ar, continua (`continue`)
   - Se `y < 0` → a pokébola caiu no chão sem capturar, **errou**
   - Se a célula `M[y][x]` é 0 → posição vazia, marca `"o"` na matriz de exibição e continua
   - Se a célula contém um Pokémon (valor ≠ 0, ≠ "T", ≠ "o") → **capturou!**
     - Remove o Pokémon da matriz original `M`
     - Move o treinador para a posição x da captura
     - Decrementa o contador de Pokémons
5. Se x saiu dos limites horizontais → **errou**

### Após cada lançamento:

- Se capturou → o treinador fica na nova posição (x da captura)
- Se errou e ainda há pokébolas e Pokémons → pergunta nova posição x do treinador

### Término do jogo:

- `num_poke == 0` → "Parabéns! Todos os Pokémons foram capturados"
- `N == 0` → "Jogo encerrado"

---

## Observações sobre o Código

- A condição `if x >= 0 or x <= n-1` na linha 257 é **sempre verdadeira** (qualquer número satisfaz `x >= 0` ou `x <= n-1`). O código funciona corretamente porque a verificação de borda real ocorre em duas etapas: antes da atualização (linha 260) e depois (linha 277).
- O uso de `break` e `continue` controla o fluxo do loop de simulação. `break` encerra o lançamento atual; `continue` pula para o próximo passo de tempo (quando a pokébola está acima da matriz).
- A matriz mistura tipos: inteiros (IDs dos Pokémons e 0 para vazio), strings (`"T"` para treinador, `"o"` para trajetória). Isso é possível pela tipagem dinâmica do Python.
- Não há validação de entrada — o programa presume que o arquivo existe e está bem formatado.
- Os índices da matriz são acessados como `matriz[linha][coluna]`, onde linha = y (coordenada vertical) e coluna = x (coordenada horizontal).
