# Análise de Erros de Termômetros de Linha Férrea

Este repositório contém análises e visualizações baseadas em um DataFrame com dados de medições de temperatura em termômetros de linha férrea. O objetivo principal é identificar padrões de erro, analisar a dispersão dos dados e entender como os erros evoluem ao longo do tempo.

## Estrutura do Repositório

- **Código de Análise:**
  - Geração de gráficos interativos usando Plotly.
  - Análise estatística dos dados de temperatura e erros.

- **Gráficos Gerados:**
  - Percentual de erros por termômetro.
  - Dispersão de temperaturas por termômetro (boxplot).
  - Percentual de erros por tipo de erro.
  - Evolução temporal dos erros.

## Dados Utilizados

Os dados analisados incluem as seguintes colunas principais:
- `regiao`: Região onde o termômetro está localizado.
- `operacao`: Identificação da operação associada.
- `original`: Identificação única do termômetro.
- `temperatura`: Temperatura registrada.
- `temperaturatermometro`: Temperatura registrada pelo termômetro.
- `amplitude`: Diferença entre temperaturas.
- `status`: Status indicando a ocorrência de erro.
- `dataref`: Data da medição.

## Visualizações

1. **Percentual de Erros por Termômetro**
   - Barras agrupadas mostrando o percentual de erros por termômetro.

2. **Dispersão das Temperaturas por Termômetro**
   - Boxplot para visualizar a dispersão das medições de temperatura.

3. **Percentual de Erros por Tipo de Erro**
   - Barras coloridas indicando os diferentes tipos de erros para cada termômetro.

4. **Evolução Temporal dos Erros**
   - Gráfico de linhas mostrando a quantidade de erros ao longo do tempo.

## Tecnologias Utilizadas

- **Python:** Linguagem principal para análise de dados.
- **Pandas:** Manipulação e agrupamento de dados.
- **Plotly:** Criação de gráficos interativos.

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/analise-erros-termometros.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute os scripts de análise.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
