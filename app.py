import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Título do Aplicativo
st.title("🎬 Dashboard Interativo da Netflix")
st.markdown("Este aplicativo foi desenvolvido para explorar o catálogo de filmes e séries da Netflix através de dados.")

# 2. Carregando os dados (Certifique-se de que o netflix_titles.csv está na mesma pasta)
@st.cache_data
def carregar_dados():
    return pd.read_csv('netflix_titles.csv')

df = carregar_dados()

# 3. Criando uma barra lateral (Sidebar) para filtros
st.sidebar.header("Filtros do Painel")
tipo_selecionado = st.sidebar.selectbox(
    "Escolha o Tipo de Conteúdo:",
    options=["Todos", "Movie", "TV Show"]
)

# Filtrando o DataFrame de acordo com a escolha do usuário
if tipo_selecionado != "Todos":
    df_filtrado = df[df['type'] == tipo_selecionado]
else:
    df_filtrado = df

# 4. Mostrando métricas rápidas na tela principal
st.subheader(f"Exibindo dados para: {tipo_selecionado}")
st.metric(label="Total de Títulos Encontrados", value=len(df_filtrado))

# 5. Mostrando a tabela interativa (com barra de rolagem)
if st.checkbox("Mostrar tabela de dados brutos"):
    st.dataframe(df_filtrado.head(100))

# 6. Gerando o gráfico interativo
st.subheader("📈 Distribuição por Ano de Lançamento")
fig, ax = plt.subplots(figsize=(10, 5))
df_filtrado['release_year'].value_counts().sort_index().plot(kind='bar', ax=ax, color='purple')
ax.set_title("Lançamentos por Ano")
ax.set_xlabel("Ano")
ax.set_ylabel("Quantidade")
st.pyplot(fig)