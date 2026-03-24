# -*- coding: utf-8 -*-
"""
01_Analise_Temporal.py
DATANGOLA - Módulo de Análise Temporal
"""

import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Análise Temporal - DATANGOLA",
    page_icon="📈",
    layout="wide"
)

# SIDEBAR
st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍🔬 Sobre o Desenvolvedor")
st.sidebar.info("""
**Upale Kahilo Lamber** 🇦🇴

👨‍🏫 Professor-Investigador - UNIC

🎓 Doutorando em Saúde Pública

🏆 Vencedor Hackathon AgriTech 2026

📊 DATANGOLA Platform

📧 upale.lamber@unic.ac.ao
""")

# TÍTULO
st.title("📈 DATANGOLA: Análise Temporal")
st.subheader("Evolução Temporal dos Indicadores de Insegurança Alimentar")

# ... RESTO DO SEU CÓDIGO ...

# FOOTER NO FINAL
ano_atual = datetime.now().year

footer_html = f"""
<div style='
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
    padding: 15px 20px;
    text-align: center;
    border-top: 3px solid #ffd700;
    font-size: 13px;
    color: #ffffff;
    z-index: 999;
'>
    <div>
        <strong>🇦🇴 DATANGOLA</strong> | 
        © {ano_atual} | 
        Desenvolvido por Upale Kahilo Lamber 🇦🇴
    </div>
</div>
<div style='padding-bottom: 100px;'></div>
"""

st.markdown(footer_html, unsafe_allow_html=True)
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from datetime import datetime

st.set_page_config(page_title="Análise Temporal", page_icon="📊", layout="wide")
# ============================================================
# SIDEBAR - INFORMAÇÕES DO DESENVOLVEDOR
# ============================================================

st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍🔬 Sobre o Desenvolvedor")
st.sidebar.info("""
**Upale Kahilo Lamber** 🇦🇴

👨‍🏫 Professor-Investigador - UNIC

🎓 Doutorando em Saúde Pública (Epidemiologia)

🏆 Vencedor Hackathon AgriTech Timbuktoo 2026

📊 Especialista em Gêmeo Digital & Python

📧 upale.lamber@unic.ac.ao
""")
st.title("📊 Análise Temporal da Insegurança Alimentar - Angola")
st.markdown("**Sistema 100% Dinâmico - Detecta Automaticamente TODAS as Províncias**")

# Função para carregar dados SEM CACHE (sempre lê do arquivo)
def load_data_fresh():
    """Carrega dados do CSV SEMPRE do arquivo mais recente"""
    caminhos = [
        "Dados_FIES_Limpos.csv",
        "../data/Dados_FIES_Limpos.csv", 
        "../Dados_FIES_Limpos.csv",
        "data/Dados_FIES_Limpos.csv",
    ]
    
    for caminho in caminhos:
        if os.path.exists(caminho):
            try:
                df = pd.read_csv(caminho, encoding='utf-8')
                df.columns = df.columns.str.strip()
                
                # Detectar estrutura dinamicamente
                colunas_excluir = ['Provincia', 'Nivel', 'província', 'nível', 'Province', 'Level']
                anos = [col for col in df.columns if col not in colunas_excluir and df[col].dtype in ['int64', 'float64']]
                anos.sort()
                
                # Detectar TODAS as províncias únicas
                todas_provincias = sorted(df['Provincia'].unique().tolist())
                
                # Detectar TODOS os níveis únicos
                niveis = sorted(df['Nivel'].unique().tolist())
                
                return df, caminho, anos, todas_provincias, niveis
                
            except Exception as e:
                st.error(f"Erro ao ler arquivo {caminho}: {e}")
                continue
    
    st.error("❌ Arquivo não encontrado!")
    return None, None, [], [], []

# Sidebar - Sincronização
st.sidebar.header("🔄 Sincronização")
if st.sidebar.button("🔄 Atualizar Dados do Arquivo", use_container_width=True, type="primary"):
    st.cache_data.clear()
    st.rerun()

# Carregar dados sempre frescos
df, caminho, anos, todas_provincias, niveis = load_data_fresh()

if df is None:
    st.stop()

# Mostrar informações atualizadas
data_modificacao = datetime.fromtimestamp(os.path.getmtime(caminho)) if os.path.exists(caminho) else "N/A"
st.sidebar.success(f"✅ **Sincronizado!**\n\n📁 {caminho}\n📊 {len(df)} registros\n🌍 {len(todas_provincias)} províncias detectadas\n📅 {anos[0]}-{anos[-1]}\n🕐 Atualizado: {data_modificacao.strftime('%d/%m %H:%M')}")

# Mostrar todas as províncias detectadas
with st.sidebar.expander("🌍 Ver Todas as Províncias Detectadas", expanded=False):
    st.write(f"**Total: {len(todas_provincias)} províncias**")
    for i, prov in enumerate(todas_provincias, 1):
        st.write(f"{i}. {prov}")

# ============================================
# SEÇÃO 1: RESUMO NACIONAL
# ============================================
st.header("🌍 RESUMO NACIONAL")
st.markdown("---")

# Calcular médias nacionais por ano
resumo_nacional = []
for ano in anos:
    media_ano = df[ano].mean()
    resumo_nacional.append({'Ano': ano, 'Média Nacional': media_ano})

df_resumo = pd.DataFrame(resumo_nacional)

# Métricas nacionais
col1, col2, col3 = st.columns(3)
media_inicial = df[anos[0]].mean()
media_final = df[anos[-1]].mean()
variacao_total = ((media_final - media_inicial) / media_inicial) * 100 if media_inicial != 0 else 0

col1.metric(f"Média Nacional {anos[0]}", f"{media_inicial:.1f}%")
col2.metric(f"Média Nacional {anos[-1]}", f"{media_final:.1f}%")
col3.metric(f"Variação ({anos[0]}-{anos[-1]})", f"{variacao_total:+.1f}%", delta_color="inverse")

# Gráfico de linha - Evolução Nacional COM DADOS
col_graf1, col_graf2 = st.columns([2, 1])

with col_graf1:
    fig_nacional = go.Figure()
    
    fig_nacional.add_trace(go.Scatter(
        x=df_resumo['Ano'],
        y=df_resumo['Média Nacional'],
        mode='lines+markers+text',
        text=[f'{val:.1f}%' for val in df_resumo['Média Nacional']],
        textposition='top center',
        name='Média Nacional',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=10, color='#1f77b4')
    ))
    
    fig_nacional.update_layout(
        title="📈 Evolução da Média Nacional de Insegurança Alimentar",
        xaxis_title="Ano",
        yaxis_title="Média Nacional (%)",
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_nacional, use_container_width=True)

with col_graf2:
    ultimo_ano = anos[-1]
    df_ultimo_ano = df.groupby('Nivel')[ultimo_ano].mean().reset_index()
    df_ultimo_ano.columns = ['Nivel', 'Média']
    
    fig_barras = px.bar(
        df_ultimo_ano,
        x="Nivel",
        y="Média",
        title=f"Média por Nível ({ultimo_ano})",
        color="Nivel",
        color_discrete_map={"Leve": "#388e3c", "Moderada": "#f57c00", "Severa": "#d32f2f"},
        text_auto='.1f'
    )
    fig_barras.update_traces(textposition='outside')
    fig_barras.update_layout(height=400, showlegend=False)
    st.plotly_chart(fig_barras, use_container_width=True)

# Tabela de resumo nacional
with st.expander("📋 Ver Tabela de Resumo Nacional"):
    st.dataframe(df_resumo.style.format({'Média Nacional': '{:.2f}%'}), use_container_width=True)

# ============================================
# SEÇÃO 2: FILTROS POR PROVÍNCIA - 100% DINÂMICO
# ============================================
st.markdown("---")
st.header("🔍 ANÁLISE POR PROVÍNCIA")
st.markdown("---")

# Filtros na sidebar - SEMPRE ATUALIZADOS
st.sidebar.header("🔍 Filtros Dinâmicos")

# BOTÃO PARA SELECIONAR TODAS AS PROVÍNCIAS
col_sel1, col_sel2 = st.sidebar.columns(2)
with col_sel1:
    if st.button("✅ Selecionar Todas", use_container_width=True):
        st.session_state.provincias_selecionadas = todas_provincias.copy()
with col_sel2:
    if st.button("❌ Limpar Todas", use_container_width=True):
        st.session_state.provincias_selecionadas = []

# Inicializar session state se não existir
if 'provincias_selecionadas' not in st.session_state:
    st.session_state.provincias_selecionadas = todas_provincias[:min(3, len(todas_provincias))]

# Seleção de províncias - MULTIPLE SELECT DINÂMICO
provincias_selecionadas = st.sidebar.multiselect(
    "Selecione as Províncias",
    options=todas_provincias,
    default=st.session_state.provincias_selecionadas,
    help=f"Total: {len(todas_provincias)} províncias detectadas automaticamente"
)

# Atualizar session state
st.session_state.provincias_selecionadas = provincias_selecionadas

# Filtro de níveis - DINÂMICO
niveis_selecionados = st.sidebar.multiselect(
    "Níveis de Insegurança",
    options=niveis,
    default=niveis,
    help="Níveis detectados automaticamente"
)

# Filtro de anos - DINÂMICO
anos_selecionados = st.sidebar.multiselect(
    "Anos para Análise",
    options=anos,
    default=anos,
    help="Anos detectados automaticamente"
)

# Mostrar resumo dos filtros
if provincias_selecionadas:
    st.sidebar.info(f"📊 **{len(provincias_selecionadas)}** de **{len(todas_provincias)}** províncias selecionadas")

# Filtrar dados
df_filtrado = df[
    df['Provincia'].isin(provincias_selecionadas) & 
    df['Nivel'].isin(niveis_selecionados)
].copy()

if not df_filtrado.empty:
    # Transformar para formato longo
    df_melt = df_filtrado.melt(
        id_vars=["Provincia", "Nivel"],
        value_vars=anos_selecionados,
        var_name="Ano",
        value_name="Prevalencia"
    )
    
    # Ordenar
    df_melt['Ano'] = pd.Categorical(df_melt['Ano'], categories=sorted(anos_selecionados), ordered=True)
    df_melt = df_melt.sort_values(['Provincia', 'Nivel', 'Ano'])
    
    # Mostrar províncias analisadas
    st.subheader(f"📊 Análise de {len(provincias_selecionadas)} Província(s)")
    st.write(", ".join(provincias_selecionadas))
    
    # Gráficos por província
    if len(provincias_selecionadas) <= 9:
        fig_prov = px.line(
            df_melt,
            x="Ano",
            y="Prevalencia",
            color="Nivel",
            facet_col="Provincia",
            facet_col_wrap=3,
            markers=True,
            title="Evolução por Província",
            color_discrete_map={"Leve": "#388e3c", "Moderada": "#f57c00", "Severa": "#d32f2f"},
            height=400 * ((len(provincias_selecionadas) // 3) + 1)
        )
        
        fig_prov.update_traces(
            texttemplate='%{y:.1f}%',
            textposition='top center',
            hovertemplate='<b>%{fullData.name}</b><br>Ano: %{x}<br>Prevalência: %{y:.1f}%<extra></extra>'
        )
        
        fig_prov.update_layout(hovermode="x unified")
        st.plotly_chart(fig_prov, use_container_width=True)
    else:
        # Gráfico agregado para muitas províncias
        fig_agg = go.Figure()
        
        for nivel in niveis_selecionados:
            df_nivel = df_melt[df_melt['Nivel'] == nivel]
            media_por_ano = df_nivel.groupby('Ano')['Prevalencia'].mean().reset_index()
            
            fig_agg.add_trace(go.Scatter(
                x=media_por_ano['Ano'],
                y=media_por_ano['Prevalencia'],
                mode='lines+markers+text',
                name=nivel,
                text=[f'{val:.1f}%' for val in media_por_ano['Prevalencia']],
                textposition='top center',
                line=dict(width=3),
                marker=dict(size=8)
            ))
        
        fig_agg.update_layout(
            title=f"Média das {len(provincias_selecionadas)} Províncias Selecionadas",
            xaxis_title="Ano",
            yaxis_title="Média de Prevalência (%)",
            height=400,
            hovermode='x unified'
        )
        
        st.plotly_chart(fig_agg, use_container_width=True)
    
    # Tabela de dados detalhados
    with st.expander("📋 Ver Dados Detalhados"):
        st.dataframe(df_filtrado, use_container_width=True)
    
    # Métricas e comparações
    st.subheader("📊 Indicadores por Província")
    
    if len(anos_selecionados) >= 2:
        ano_inicial = min(anos_selecionados)
        ano_final = max(anos_selecionados)
        
        # Criar tabela comparativa
        dados_comparacao = []
        for prov in provincias_selecionadas:
            df_prov = df_filtrado[df_filtrado['Provincia'] == prov]
            for nivel in niveis_selecionados:
                df_nivel = df_prov[df_prov['Nivel'] == nivel]
                if not df_nivel.empty:
                    val_inicial = df_nivel[str(ano_inicial)].values[0]
                    val_final = df_nivel[str(ano_final)].values[0]
                    variacao_prov = ((val_final - val_inicial) / val_inicial) * 100 if val_inicial != 0 else 0
                    
                    dados_comparacao.append({
                        'Província': prov,
                        'Nível': nivel,
                        f'{ano_inicial}': f'{val_inicial:.1f}%',
                        f'{ano_final}': f'{val_final:.1f}%',
                        'Variação (%)': variacao_prov
                    })
        
        df_comparacao = pd.DataFrame(dados_comparacao)
        st.dataframe(df_comparacao, use_container_width=True)
        
        # Ranking
        st.subheader("🏆 Ranking de Variação")
        col_rank1, col_rank2 = st.columns(2)
        
        with col_rank1:
            st.success(" Maiores Reduções")
            df_melhores = df_comparacao.nsmallest(5, 'Variação (%)')
            st.dataframe(df_melhores, use_container_width=True)
        
        with col_rank2:
            st.error("⚠️ Maiores Aumentos")
            df_piores = df_comparacao.nlargest(5, 'Variação (%)')
            st.dataframe(df_piores, use_container_width=True)

else:
    if provincias_selecionadas:
        st.warning("⚠️ Nenhum dado encontrado para os filtros selecionados")
    else:
        st.info("👈 Selecione províncias no menu lateral para iniciar a análise")
    st.stop()

# Informações finais
st.markdown("---")
st.sidebar.markdown("---")
st.sidebar.success("✨ **Sistema 100% Dinâmico!**\n\n✅ Detecta automaticamente:\n- Novas províncias\n- Novos anos\n- Novos níveis\n\n🔄 Clique em 'Atualizar' para sincronizar")
# ============================================================
# FOOTER - RODAPÉ
# ============================================================

from datetime import datetime

ano_atual = datetime.now().year

footer_html = f"""
<div style='
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
    padding: 15px 20px;
    text-align: center;
    border-top: 3px solid #ffd700;
    font-size: 13px;
    color: #ffffff;
    z-index: 999;
    font-family: "Helvetica Neue", sans-serif;
    box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
'>
    <div style='margin-bottom: 5px;'>
        <strong>🌍 Gêmeo Digital - FIES Angola</strong> | 
        Desenvolvido por <strong>Upale Kahilo Lamber</strong> 🇦🇴 | 
        © {ano_atual}
    </div>
    <div style='font-size: 11px; opacity: 0.9;'>
        📊 Universidade Internacional do Cuanza (UNIC) | 
        📧 upale.lamber@unic.ac.ao | 
        🔒 Uso Académico e de Pesquisa
    </div>
</div>
<div style='padding-bottom: 100px;'></div>
"""

st.markdown(footer_html, unsafe_allow_html=True)