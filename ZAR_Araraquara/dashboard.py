import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o dataframe
df = pd.read_csv("C:/Users/Cristiano/OneDrive - Belago Technologies/Documentos/projeto_fnt/data/dataframe_atualizado.csv")

# Título do Dashboard
st.title("Dashboard de Temperaturas de Trilhos de Trem")

# Opções de visualização
visualizacao = st.sidebar.selectbox(
    "Escolha o tipo de visualização:",
    ["Gráfico de Temperaturas por Data", "Distribuição de Temperaturas", "Temperaturas por Bloco"]
)

# Opção para selecionar intervalo de datas
data_inicio = st.sidebar.date_input("Data de Início", pd.to_datetime(df["data"]).min())
data_fim = st.sidebar.date_input("Data de Fim", pd.to_datetime(df["data"]).max())

# Converter data_inicio e data_fim para datetime64
data_inicio = pd.to_datetime(data_inicio)
data_fim = pd.to_datetime(data_fim)

# Filtrando os dados conforme as datas selecionadas
df["data"] = pd.to_datetime(df["data"])
df_filtrado = df[(df["data"] >= data_inicio) & (df["data"] <= data_fim)]

# Verificando se há dados após o filtro
if df_filtrado.empty:
    st.warning("Não há dados disponíveis para o intervalo de datas selecionado.")
else:
    # Função para gráfico de temperaturas por data
    def grafico_temperaturas_por_data():
        fig = px.line(df_filtrado, x="data", y=["temperatura_maxima", "temperatura_minima"],
                      labels={"data": "Data", "value": "Temperatura (°C)", "variable": "Temperatura"},
                      title="Temperaturas Máxima e Mínima por Data")
        st.plotly_chart(fig)

    # Função para gráfico de distribuição de temperaturas
    def grafico_distribuicao_temperaturas():
        fig = px.histogram(df_filtrado, x="temperatura_maxima", nbins=30, opacity=0.6, color_discrete_sequence=["blue"],
                           labels={"temperatura_maxima": "Temperatura Máxima"}, title="Distribuição das Temperaturas Máxima")
        # Agora, adicionamos o histograma da temperatura mínima diretamente dentro do mesmo gráfico
        fig.add_trace(px.histogram(df_filtrado, x="temperatura_minima", nbins=30, opacity=0.6, color_discrete_sequence=["orange"]).data[0])
        fig.update_layout(barmode="overlay", xaxis_title="Temperatura (°C)", yaxis_title="Frequência")
        st.plotly_chart(fig)

    # Função para gráfico de temperaturas por bloco
    def grafico_temperaturas_por_bloco():
        fig = px.box(df_filtrado, x="bloco", y="temperatura_maxima", color="bloco",
                     title="Temperaturas Máxima por Bloco", labels={"temperatura_maxima": "Temperatura (°C)"})
        fig.update_traces(boxmean="sd")
        st.plotly_chart(fig)

        fig2 = px.box(df_filtrado, x="bloco", y="temperatura_minima", color="bloco",
                      title="Temperaturas Mínima por Bloco", labels={"temperatura_minima": "Temperatura (°C)"})
        fig2.update_traces(boxmean="sd")
        st.plotly_chart(fig2)

    # Mostrar o gráfico conforme a seleção do usuário
    if visualizacao == "Gráfico de Temperaturas por Data":
        grafico_temperaturas_por_data()
    elif visualizacao == "Distribuição de Temperaturas":
        grafico_distribuicao_temperaturas()
    elif visualizacao == "Temperaturas por Bloco":
        grafico_temperaturas_por_bloco()
