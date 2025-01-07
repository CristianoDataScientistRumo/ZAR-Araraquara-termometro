![Terminal Ferroviário em Rio Verde](https://www.gov.br/transportes/pt-br/assuntos/noticias/2022/08/novo-terminal-ferroviario-em-rio-verde-go-vai-movimentar-3-5-milhoes-de-toneladas-por-ano/terminal_rumo_rioverde.jpeg)

# Análise de Erros de Termômetros de Linha Férrea

Este repositório contém análises e visualizações baseadas em dados de medições de temperatura em termômetros de linha férrea. O objetivo principal é identificar padrões de erro, analisar a dispersão dos dados e entender como os erros evoluem ao longo do tempo.

---

## Estrutura do Repositório

### Código de Análise

1. **Geração de gráficos interativos** utilizando **Plotly**.  
2. **Análise estatística** dos dados de temperatura e erros.

---

## Dados Utilizados

As análises foram realizadas com base nas seguintes colunas principais:

| **Coluna**            | **Descrição**                                       |
|-----------------------|-----------------------------------------------------|
| `regiao`             | Região onde o termômetro está localizado            |
| `operacao`           | Identificação da operação associada                 |
| `original`           | Identificação única do termômetro                   |
| `temperatura`        | Temperatura registrada                              |
| `temperaturatermometro` | Temperatura registrada pelo termômetro             |
| `amplitude`          | Diferença entre temperaturas                        |
| `status`             | Status indicando a ocorrência de erro               |
| `dataref`            | Data da medição                                     |

---

## Visualizações

### 1. Percentual de Erros por Termômetro

- **Descrição**: Este gráfico exibe o percentual de erros registrados por termômetro, agrupados por região.  
- **Objetivo**: Identificar quais termômetros apresentam maior taxa de erros.  
- **Exemplo de Código**:

```python
import plotly.express as px

fig = px.bar(df, x='original', y='percentual_erros', color='regiao', 
             title='Percentual de Erros por Termômetro',
             labels={'original': 'Termômetro', 'percentual_erros': 'Percentual de Erros (%)'})
fig.show()

2. Dispersão das Temperaturas por Termômetro
Descrição: Boxplot para mostrar a dispersão das temperaturas medidas por cada termômetro.
Objetivo: Analisar a consistência das medições.
Exemplo de Código:

fig = px.box(df, x='original', y='temperaturatermometro', color='regiao', 
             title='Dispersão das Temperaturas por Termômetro',
             labels={'original': 'Termômetro', 'temperaturatermometro': 'Temperatura (°C)'})
fig.show()
___
3. Percentual de Erros por Tipo de Erro
Descrição: Gráfico de barras agrupadas para indicar os diferentes tipos de erros.
Objetivo: Identificar os erros mais comuns e sua distribuição.
Exemplo de Código:
python
Copiar código
fig = px.bar(df, x='tipo_erro', y='percentual_erros', color='regiao', 
             title='Percentual de Erros por Tipo de Erro',
             labels={'tipo_erro': 'Tipo de Erro', 'percentual_erros': 'Percentual de Erros (%)'})
fig.show()
___
4. Evolução Temporal dos Erros
Descrição: Gráfico de linhas mostrando a evolução dos erros ao longo do tempo.
Objetivo: Observar tendências sazonais ou padrões temporais.
Exemplo de Código:

fig = px.line(df, x='dataref', y='quantidade_erros', color='regiao', 
              title='Evolução Temporal dos Erros',
              labels={'dataref': 'Data', 'quantidade_erros': 'Quantidade de Erros'})
fig.show()
___
## Tecnologias Utilizadas
* Python: Linguagem principal para análise de dados.
* Pandas: Manipulação e agrupamento de dados.
* Plotly: Criação de gráficos interativos.

## Como Executar:

git clone https://github.com/seu-usuario/analise-erros-termometros.git
### Instale as dependências:
pip install -r requirements.txt
### Execute os scripts de análise:
python analise_erros.py
## Licença
### Este projeto está licenciado sob a MIT License.

### Autor: Cristiano Santana - Rumo Logística



