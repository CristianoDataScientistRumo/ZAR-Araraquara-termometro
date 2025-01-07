![Terminal Ferroviário em Rio Verde](https://www.gov.br/transportes/pt-br/assuntos/noticias/2022/08/novo-terminal-ferroviario-em-rio-verde-go-vai-movimentar-3-5-milhoes-de-toneladas-por-ano/terminal_rumo_rioverde.jpeg)

# Análise de Erros de Termômetros de Linha Férrea

Este repositório contém análises e visualizações baseadas em dados de medições de temperatura em termômetros de linha férrea. O objetivo principal é identificar padrões de erro, analisar a dispersão dos dados e entender como os erros evoluem ao longo do tempo.

---

## Estrutura do Repositório

### Código de Análise

- **Geração de gráficos interativos** utilizando **Plotly**.
- **Análise estatística** dos dados de temperatura e erros.

### Gráficos Gerados

1. **Percentual de Erros por Termômetro**  
   Gráfico de barras mostrando o percentual de erros por termômetro.

2. **Dispersão das Temperaturas por Termômetro**  
   Boxplot para visualizar a dispersão das medições de temperatura.

3. **Percentual de Erros por Tipo de Erro**  
   Gráfico de barras indicando os diferentes tipos de erros para cada termômetro.

4. **Evolução Temporal dos Erros**  
   Gráfico de linhas mostrando a quantidade de erros ao longo do tempo.

---

## Dados Utilizados

As análises foram realizadas com base nas seguintes colunas principais:

| Coluna                | Descrição                                             |
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
- **Exemplo de Visualização**:

```python
fig = px.bar(df, x='original', y='percentual_erros', color='regiao', title='Percentual de Erros por Termômetro')
fig.show()

