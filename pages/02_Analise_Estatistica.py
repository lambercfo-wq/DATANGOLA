# -*- coding: utf-8 -*-
"""
02_Analise_Estatistica.py
DATANGOLA - Módulo de Análise Estatística
"""

import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Análise Estatística - DATANGOLA",
    page_icon="📊",
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
st.title("📊 DATANGOLA: Análise Estatística")
st.subheader("Estatísticas Descritivas e Inferenciais")

# ... RESTO DO SEU CÓDIGO ...

# FOOTER NO FINAL (mesmo código acima)
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from sklearn.linear_model import LinearRegression
from datetime import datetime
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Análise Estatística & IA", page_icon="🧠", layout="wide")

st.title("🧠 Análise Estatística Avançada & Inteligência Artificial")
st.markdown("**Interpretação Automática • Previsões • Recomendações • Políticas Públicas • Chi-Quadrado**")

# ============================================
# CARREGAR DADOS
# ============================================
@st.cache_data
def load_data():
    caminhos = [
        "Dados_FIES_Limpos.csv",
        "../data/Dados_FIES_Limpos.csv",
        "data/Dados_FIES_Limpos.csv"
    ]
    
    for caminho in caminhos:
        if os.path.exists(caminho):
            df = pd.read_csv(caminho, encoding='utf-8')
            df.columns = df.columns.str.strip()
            return df, caminho
    return None, None

df, caminho = load_data()

if df is None:
    st.error("❌ Arquivo não encontrado!")
    st.stop()

# Detectar anos
anos = [col for col in df.columns if col not in ['Provincia', 'Nivel'] and df[col].dtype in ['int64', 'float64']]
anos.sort()

# Sidebar - Sincronização
st.sidebar.header("🔄 Dados")
if st.sidebar.button("🔄 Atualizar Dados", use_container_width=True):
    st.cache_data.clear()
    st.rerun()

st.sidebar.info(f"📊 {len(df)} registros\n🌍 {df['Provincia'].nunique()} províncias\n📅 {anos[0]}-{anos[-1]}")

# ============================================
# FUNÇÃO DE COLORIR (CORREÇÃO DO ERRO)
# ============================================
def colorir_risk(val):
    """Função para colorir a tabela de risco"""
    if pd.isna(val):
        return ''
    elif 'CRÍTICO' in str(val):
        return 'background-color: #ffcccc; color: #cc0000; font-weight: bold'
    elif 'ATENÇÃO' in str(val):
        return 'background-color: #ffe6cc; color: #cc6600; font-weight: bold'
    elif 'MODERADO' in str(val):
        return 'background-color: #ffffcc; color: #999900'
    else:
        return 'background-color: #ccffcc; color: #006600'

# ============================================
# SEÇÃO 1: ESTATÍSTICAS DESCRITIVAS (TIPO SPSS)
# ============================================
st.header("📊 ESTATÍSTICAS DESCRITIVAS AVANÇADAS")
st.markdown("---")

col_stats1, col_stats2, col_stats3 = st.columns(3)

with col_stats1:
    st.subheader("📈 Medidas de Tendência Central")
    
    dados_ultimo_ano = df[anos[-1]]
    
    metricas = {
        "Média": f"{dados_ultimo_ano.mean():.2f}%",
        "Mediana": f"{dados_ultimo_ano.median():.2f}%",
        "Moda": f"{dados_ultimo_ano.mode().values[0]:.2f}%" if len(dados_ultimo_ano.mode()) > 0 else "N/A"
    }
    
    for k, v in metricas.items():
        st.metric(k, v)

with col_stats2:
    st.subheader("📉 Medidas de Dispersão")
    
    metricas_disp = {
        "Desvio Padrão": f"{dados_ultimo_ano.std():.2f}%",
        "Variância": f"{dados_ultimo_ano.var():.2f}",
        "Amplitude": f"{dados_ultimo_ano.max() - dados_ultimo_ano.min():.2f}%"
    }
    
    for k, v in metricas_disp.items():
        st.metric(k, v)

with col_stats3:
    st.subheader("📊 Distribuição")
    
    metricas_dist = {
        "Mínimo": f"{dados_ultimo_ano.min():.2f}%",
        "Máximo": f"{dados_ultimo_ano.max():.2f}%",
        "Coef. Variação": f"{(dados_ultimo_ano.std() / dados_ultimo_ano.mean() * 100):.1f}%"
    }
    
    for k, v in metricas_dist.items():
        st.metric(k, v)

# Tabela estatística completa
with st.expander("📋 Ver Tabela Estatística Completa (Tipo SPSS)"):
    stats_data = []
    
    for nivel in df['Nivel'].unique():
        df_nivel = df[df['Nivel'] == nivel]
        
        for ano in anos:
            dados = df_nivel[ano]
            stats_data.append({
                'Nível': nivel,
                'Ano': ano,
                'Média': dados.mean(),
                'Mediana': dados.median(),
                'Desvio Padrão': dados.std(),
                'Variância': dados.var(),
                'Mínimo': dados.min(),
                'Máximo': dados.max(),
                'Skewness': dados.skew(),
                'Kurtosis': dados.kurtosis(),
                'N': len(dados)
            })
    
    df_stats = pd.DataFrame(stats_data)
    st.dataframe(df_stats.style.format({
        'Média': '{:.2f}', 'Mediana': '{:.2f}', 'Desvio Padrão': '{:.2f}',
        'Variância': '{:.2f}', 'Mínimo': '{:.2f}', 'Máximo': '{:.2f}',
        'Skewness': '{:.3f}', 'Kurtosis': '{:.3f}'
    }), use_container_width=True)

# ============================================
# SEÇÃO 2: IDENTIFICAÇÃO DE PROVÍNCIAS CRÍTICAS
# ============================================
st.markdown("---")
st.header("⚠️ IDENTIFICAÇÃO DE PROVÍNCIAS CRÍTICAS")
st.markdown("---")

# Calcular risco por província
def calcular_risco(df, anos):
    risco_data = []
    
    for prov in df['Provincia'].unique():
        df_prov = df[df['Provincia'] == prov]
        
        # Severa mais recente
        df_severa = df_prov[df_prov['Nivel'] == 'Severa']
        
        if not df_severa.empty:
            severa_atual = df_severa[anos[-1]].values[0]
            severa_anterior = df_severa[anos[0]].values[0]
            variacao = ((severa_atual - severa_anterior) / severa_anterior) * 100 if severa_anterior != 0 else 0
            
            # Score de risco (0-100)
            score_risco = min(100, (severa_atual * 2) + max(0, variacao))
            
            # Classificação
            if score_risco >= 70:
                classificacao = "🔴 CRÍTICO"
            elif score_risco >= 50:
                classificacao = "🟠 ATENÇÃO"
            elif score_risco >= 30:
                classificacao = "🟡 MODERADO"
            else:
                classificacao = "🟢 BAIXO"
            
            risco_data.append({
                'Província': prov,
                'Severa Atual': severa_atual,
                'Variação (%)': variacao,
                'Score Risco': score_risco,
                'Classificação': classificacao
            })
    
    return pd.DataFrame(risco_data).sort_values('Score Risco', ascending=False)

df_risco = calcular_risco(df, anos)

# Mostrar províncias críticas
col_crit1, col_crit2 = st.columns([2, 1])

with col_crit1:
    st.subheader("🏆 Ranking de Risco por Província")
    
    st.dataframe(
        df_risco.style.applymap(colorir_risk, subset=['Classificação'])
        .format({'Severa Atual': '{:.1f}%', 'Variação (%)': '{:+.1f}%', 'Score Risco': '{:.1f}'}),
        use_container_width=True,
        height=400
    )

with col_crit2:
    st.subheader("📊 Distribuição de Risco")
    
    risco_counts = df_risco['Classificação'].value_counts()
    
    fig_pie = px.pie(
        values=risco_counts.values,
        names=risco_counts.index,
        title="Distribuição de Risco",
        color_discrete_map={
            "🔴 CRÍTICO": "#dc3545",
            "🟠 ATENÇÃO": "#fd7e14",
            "🟡 MODERADO": "#ffc107",
            "🟢 BAIXO": "#28a745"
        }
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Alertas automáticos
st.subheader("🚨 Alertas Automáticos")

provincias_criticas = df_risco[df_risco['Classificação'].str.contains('CRÍTICO|ATENÇÃO')]

if not provincias_criticas.empty:
    for idx, row in provincias_criticas.head(5).iterrows():
        if 'CRÍTICO' in row['Classificação']:
            st.error(f"🔴 **{row['Província']}**: Severa {row['Severa Atual']:.1f}% | Variação {row['Variação (%)']:+.1f}%")
        else:
            st.warning(f"🟠 **{row['Província']}**: Severa {row['Severa Atual']:.1f}% | Variação {row['Variação (%)']:+.1f}%")
else:
    st.success("✅ Nenhuma província em situação crítica no momento")

# ============================================
# SEÇÃO 3: ANÁLISE CHI-QUADRADO (χ²)
# ============================================
st.markdown("---")
st.header("📊 ANÁLISE DE ASSOCIAÇÃO CHI-QUADRADO (χ²)")
st.markdown("**Testa se existe associação significativa entre variáveis categóricas**")
st.markdown("---")

col_chi1, col_chi2 = st.columns(2)

with col_chi1:
    st.subheader("🔍 Chi-Quadrado: Província vs Nível")
    
    # Criar tabela de contingência
    tabela_contingencia = pd.crosstab(df['Provincia'], df['Nivel'])
    
    # Calcular Chi-Quadrado
    chi2, p_value, dof, expected = stats.chi2_contingency(tabela_contingencia)
    
    st.metric("Estatística χ²", f"{chi2:.4f}")
    st.metric("Valor-p", f"{p_value:.6f}")
    st.metric("Graus de Liberdade", dof)
    
    # Interpretação
    if p_value < 0.05:
        st.success(f"✅ **Associação SIGNIFICATIVA** (p < 0.05)\n\nExiste relação estatisticamente significativa entre Província e Nível de insegurança alimentar.")
    else:
        st.error(f"❌ **Associação NÃO SIGNIFICATIVA** (p ≥ 0.05)\n\nNão há evidência de relação entre Província e Nível.")
    
    with st.expander("📋 Ver Tabela de Contingência"):
        st.dataframe(tabela_contingencia)

with col_chi2:
    st.subheader("🔍 Chi-Quadrado: Ano vs Nível")
    
    # Criar categorias para anos (baixo/médio/alto)
    def categorizar_ano(valor):
        if valor <= 25:
            return "Baixo"
        elif valor <= 35:
            return "Médio"
        else:
            return "Alto"
    
    # Aplicar para o último ano
    df_temp = df.copy()
    df_temp['Categoria'] = df_temp[anos[-1]].apply(categorizar_ano)
    
    tabela_contingencia_ano = pd.crosstab(df_temp['Categoria'], df_temp['Nivel'])
    
    chi2_ano, p_ano, dof_ano, expected_ano = stats.chi2_contingency(tabela_contingencia_ano)
    
    st.metric("Estatística χ²", f"{chi2_ano:.4f}")
    st.metric("Valor-p", f"{p_ano:.6f}")
    st.metric("Graus de Liberdade", dof_ano)
    
    if p_ano < 0.05:
        st.success(f"✅ **Associação SIGNIFICATIVA** (p < 0.05)")
    else:
        st.error(f"❌ **Associação NÃO SIGNIFICATIVA** (p ≥ 0.05)")
    
    with st.expander("📋 Ver Tabela de Contingência"):
        st.dataframe(tabela_contingencia_ano)

# Gráfico de calor do Chi-Quadrado
st.subheader(" Mapa de Calor: Frequências Observadas vs Esperadas")

col_heat1, col_heat2 = st.columns(2)

with col_heat1:
    fig_observed = px.imshow(
        tabela_contingencia,
        text_auto=True,
        aspect='auto',
        color_continuous_scale='YlOrRd',
        title="Frequências Observadas"
    )
    fig_observed.update_layout(height=400)
    st.plotly_chart(fig_observed, use_container_width=True)

with col_heat2:
    # Converter expected para DataFrame
    expected_df = pd.DataFrame(expected, index=tabela_contingencia.index, columns=tabela_contingencia.columns)
    
    fig_expected = px.imshow(
        expected_df,
        text_auto='.1f',
        aspect='auto',
        color_continuous_scale='YlOrRd',
        title="Frequências Esperadas (se independentes)"
    )
    fig_expected.update_layout(height=400)
    st.plotly_chart(fig_expected, use_container_width=True)

# Resíduos do Chi-Quadrado
with st.expander("📊 Análise de Resíduos (Diferenças Observado-Esperado)"):
    residuos = tabela_contingencia - expected_df
    
    st.write("**Resíduos Positivos**: Mais ocorrências do que esperado")
    st.write("**Resíduos Negativos**: Menos ocorrências do que esperado")
    
    # Calcular range simétrico para centralizar em 0
    vmax = max(abs(residuos.min().min()), abs(residuos.max().max()))
    
    fig_residuos = px.imshow(
        residuos,
        text_auto='.1f',
        aspect='auto',
        color_continuous_scale='RdBu_r',
        title="Resíduos (Observado - Esperado)",
        range_color=[-vmax, vmax]  # ✅ Centraliza o mapa de calor em 0
    )
    fig_residuos.update_layout(height=400)
    st.plotly_chart(fig_residuos, use_container_width=True)

# ============================================
# SEÇÃO 4: PREVISÕES E TENDÊNCIAS (2025-2026)
# ============================================
st.markdown("---")
st.header("🔮 PREVISÕES E TENDÊNCIAS FUTURAS")
st.markdown("---")

def fazer_previsao(df, prov, nivel, anos):
    """Faz previsão usando regressão linear"""
    df_filtrado = df[(df['Provincia'] == prov) & (df['Nivel'] == nivel)]
    
    if df_filtrado.empty:
        return None
    
    X = np.array([int(ano) for ano in anos]).reshape(-1, 1)
    y = df_filtrado[anos].values[0]
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Prever 2025 e 2026
    anos_futuros = [2025, 2026]
    previsoes = model.predict(np.array(anos_futuros).reshape(-1, 1))
    
    # R² da regressão
    r2 = model.score(X, y)
    
    # Tendência
    if model.coef_[0] > 0.5:
        tendencia = "📈 AUMENTO"
    elif model.coef_[0] < -0.5:
        tendencia = "📉 REDUÇÃO"
    else:
        tendencia = "➡️ ESTÁVEL"
    
    return {
        '2025': previsoes[0],
        '2026': previsoes[1],
        'R²': r2,
        'Tendência': tendencia,
        'Coeficiente': model.coef_[0]
    }

# Seleção para previsão
col_prev1, col_prev2 = st.columns(2)

with col_prev1:
    prov_previsao = st.selectbox("Província para Previsão", sorted(df['Provincia'].unique()))
with col_prev2:
    nivel_previsao = st.selectbox("Nível", sorted(df['Nivel'].unique()))

if st.button("🔮 Gerar Previsão", type="primary"):
    resultado = fazer_previsao(df, prov_previsao, nivel_previsao, anos)
    
    if resultado:
        col_res1, col_res2, col_res3 = st.columns(3)
        
        with col_res1:
            st.metric("Previsão 2025", f"{resultado['2025']:.1f}%")
        with col_res2:
            st.metric("Previsão 2026", f"{resultado['2026']:.1f}%")
        with col_res3:
            st.metric("Confiança (R²)", f"{resultado['R²']:.2f}")
        
        st.info(f"**Tendência**: {resultado['Tendência']} (Coeficiente: {resultado['Coeficiente']:.2f})")
        
        # Gráfico com previsão
        df_hist = df[(df['Provincia'] == prov_previsao) & (df['Nivel'] == nivel_previsao)]
        
        fig_prev = go.Figure()
        
        # Dados históricos
        fig_prev.add_trace(go.Scatter(
            x=[int(a) for a in anos],
            y=df_hist[anos].values[0],
            mode='lines+markers',
            name='Histórico',
            line=dict(color='#1f77b4', width=3)
        ))
        
        # Previsões
        fig_prev.add_trace(go.Scatter(
            x=[2025, 2026],
            y=[resultado['2025'], resultado['2026']],
            mode='lines+markers',
            name='Previsão',
            line=dict(color='#ff7f0e', width=3, dash='dash')
        ))
        
        fig_prev.update_layout(
            title=f"Previsão para {prov_previsao} - {nivel_previsao}",
            xaxis_title="Ano",
            yaxis_title="Prevalência (%)",
            height=400
        )
        
        st.plotly_chart(fig_prev, use_container_width=True)
    else:
        st.error("Dados insuficientes para previsão")

# ============================================
# SEÇÃO 5: INTERPRETAÇÃO AUTOMÁTICA (IA)
# ============================================
st.markdown("---")
st.header("🤖 INTERPRETAÇÃO AUTOMÁTICA DOS DADOS")
st.markdown("---")

def gerar_interpretacao(df, anos):
    """Gera interpretação automática dos dados"""
    
    # Análise nacional
    media_inicial = df[anos[0]].mean()
    media_final = df[anos[-1]].mean()
    variacao_nacional = ((media_final - media_inicial) / media_inicial) * 100
    
    # Província com maior redução
    df_severa = df[df['Nivel'] == 'Severa']
    variacoes = []
    
    for prov in df_severa['Provincia'].unique():
        df_prov = df_severa[df_severa['Provincia'] == prov]
        var = ((df_prov[anos[-1]].values[0] - df_prov[anos[0]].values[0]) / df_prov[anos[0]].values[0]) * 100
        variacoes.append({'Província': prov, 'Variação': var})
    
    df_variacoes = pd.DataFrame(variacoes)
    melhor = df_variacoes.loc[df_variacoes['Variação'].idxmin()]
    pior = df_variacoes.loc[df_variacoes['Variação'].idxmax()]
    
    # Calcular médias por ano para encontrar melhor e pior ano
    medias_por_ano = df[anos].mean()
    ano_pior = medias_por_ano.idxmax()  # Ano com maior média (pior situação)
    ano_melhor = medias_por_ano.idxmin()  # Ano com menor média (melhor situação)
    
    # Nível com maior e menor prevalência
    nivel_maior = df.groupby('Nivel')[anos[-1]].mean().idxmax()
    nivel_menor = df.groupby('Nivel')[anos[-1]].mean().idxmin()
    
    interpretacao = f"""
    ### 📊 ANÁLISE NACIONAL ({anos[0]}-{anos[-1]})
    
    **Tendência Geral:**
    - A insegurança alimentar média nacional {'aumentou' if variacao_nacional > 0 else 'reduziu'} em **{abs(variacao_nacional):.1f}%** no período.
    - Média inicial ({anos[0]}): **{media_inicial:.1f}%**
    - Média final ({anos[-1]}): **{media_final:.1f}%**
    
    ### 🏆 DESTAQUES POSITIVOS
    - **{melhor['Província']}**: Maior redução de insegurança severa ({melhor['Variação']:.1f}%)
    - Províncias com redução > 50%: {len(df_variacoes[df_variacoes['Variação'] < -50])}
    
    ### ⚠️ ATENÇÃO NECESSÁRIA
    - **{pior['Província']}**: Maior aumento de insegurança severa ({pior['Variação']:+.1f}%)
    - Províncias com aumento > 50%: {len(df_variacoes[df_variacoes['Variação'] > 50])}
    
    ### 📈 PADRÕES IDENTIFICADOS
    - Nível com maior prevalência: **{nivel_maior}**
    - Nível com menor prevalência: **{nivel_menor}**
    - Ano com pior situação: **{ano_pior}**
    - Ano com melhor situação: **{ano_melhor}**
    """
    
    return interpretacao

   # ============================================
# FUNÇÃO PARA CARREGAR POLÍTICAS
# ============================================
def carregar_politicas():
    """Carrega o arquivo de políticas públicas"""
    caminhos = [
        "data/politicas_angola.txt",
        "../data/politicas_angola.txt",
        "politicas_angola.txt",
        "data/Politicas_angola.txt",
        "../data/Politicas_angola.txt"
    ]
 # ============================================
# FUNÇÃO PARA CARREGAR POLÍTICAS
# ============================================
def carregar_politicas():
    """Políticas públicas de Angola - Conteúdo embutido"""
    return """POLÍTICAS DE SEGURANÇA ALIMENTAR - ANGOLA

1. PNDSA 2013-2025 (Política Nacional de Desenvolvimento Sanitário)
   - Objetivo: Reduzir insegurança alimentar em 50% até 2025
   - Meta: Prevalência severa < 5% em todas as províncias
   - Estratégia: Programas de nutrição materno-infantil

2. PRS II (Plano de Desenvolvimento Nacional 2018-2022)
   - Foco: Agricultura familiar e produção local
   - Meta: Aumentar produção agrícola em 30%
   - Orçamento: 15% do orçamento nacional para agricultura

3. Programa de Combate à Fome (2020-2025)
   - Público-alvo: Províncias com insegurança severa > 15%
   - Ações: Distribuição de alimentos, capacitação agrícola
   - Monitoramento: Trimestral via FIES

4. Lei de Segurança Alimentar e Nutricional (Lei 12/2019)
   - Artigo 5º: Direito à alimentação adequada
   - Artigo 12: Obrigatoriedade de monitoramento contínuo
   - Artigo 18: Sanções para regiões em crise prolongada

5. Estratégia Nacional de Redução da Pobreza
   - Meta 2025: Reduzir pobreza multidimensional em 40%
   - Indicador FIES: Componente chave de monitoramento
"""

# ============================================
# SEÇÃO DE POLÍTICAS PÚBLICAS
# ============================================
st.markdown("---")
st.header("📋 RECOMENDAÇÕES DE POLÍTICAS PÚBLICAS")
st.markdown("---")

# Carregar políticas
politicas = carregar_politicas()

col_pol1, col_pol2 = st.columns([2, 1])

with col_pol1:
    st.subheader("💡 Recomendações Automáticas")
    
    # Gerar recomendações baseadas nos dados
    recomendacoes = []
    
    for idx, row in df_risco.head(3).iterrows():
        if 'CRÍTICO' in row['Classificação']:
            recomendacoes.append(f"🔴 **{row['Província']}**: Intervenção urgente necessária.")
        elif 'ATENÇÃO' in row['Classificação']:
            recomendacoes.append(f"🟠 **{row['Província']}**: Monitoramento intensificado.")
    
    for rec in recomendacoes:
        st.info(rec)
    
    st.subheader("📌 Recomendações Gerais")
    # Carregar políticas
politicas = carregar_politicas()

# Calcular variação nacional
media_inicial = df[anos[0]].mean()
media_final = df[anos[-1]].mean()
variacao_nacional = ((media_final - media_inicial) / media_inicial) * 100

col_pol1, col_pol2 = st.columns([2, 1])

with col_pol1:
    st.subheader("💡 Recomendações Automáticas")
    
    # Gerar recomendações baseadas nos dados
    recomendacoes = []
    
    for idx, row in df_risco.head(3).iterrows():
        if 'CRÍTICO' in row['Classificação']:
            recomendacoes.append(f"🔴 **{row['Província']}**: Intervenção urgente necessária.")
        elif 'ATENÇÃO' in row['Classificação']:
            recomendacoes.append(f"🟠 **{row['Província']}**: Monitoramento intensificado.")
    
    for rec in recomendacoes:
        st.info(rec)
    
    st.subheader("📌 Recomendações Gerais")
    
    if variacao_nacional > 0:
        st.warning("⚠️ **Tendência Nacional de Aumento**: Revisar estratégias do PNDSA 2013-2025")
    else:
        st.success("✅ **Tendência Nacional de Redução**: Manter políticas atuais")
    
    nivel_critico = df.groupby('Nivel')[anos[-1]].mean().idxmax()
    st.info(f"📊 **Foco Prioritário**: {nivel_critico}")

with col_pol2:
    st.subheader("📜 Políticas Vigentes")
    
    if politicas:
        with st.expander("📖 Ver Políticas Completas"):
            st.text(politicas)
    else:
        st.info("💡 Arquivo de políticas não encontrado")
    if variacao_nacional > 0:
        st.warning("⚠️ **Tendência Nacional de Aumento**: Revisar estratégias do PNDSA 2013-2025")
    else:
        st.success("✅ **Tendência Nacional de Redução**: Manter políticas atuais")
    
    nivel_critico = df.groupby('Nivel')[anos[-1]].mean().idxmax()
    st.info(f"📊 **Foco Prioritário**: {nivel_critico}")

with col_pol2:
    st.subheader("📜 Políticas Vigentes")
    
    if politicas:
        with st.expander("📖 Ver Políticas Completas"):
            st.text(politicas)
    else:
        st.info("💡 Arquivo de políticas não encontrado")
    
    # Gerar recomendações baseadas nos dados
    recomendacoes = []
    
    for idx, row in df_risco.head(3).iterrows():
        if 'CRÍTICO' in row['Classificação']:
            recomendacoes.append(f"🔴 **{row['Província']}**: Intervenção urgente necessária.")
        elif 'ATENÇÃO' in row['Classificação']:
            recomendacoes.append(f"🟠 **{row['Província']}**: Monitoramento intensificado.")
    
    for rec in recomendacoes:
        st.info(rec)
    
    st.subheader("📌 Recomendações Gerais")
    
    if variacao_nacional > 0:
        st.warning("⚠️ **Tendência Nacional de Aumento**: Revisar estratégias do PNDSA 2013-2025")
    else:
        st.success("✅ **Tendência Nacional de Redução**: Manter políticas atuais")
    
    nivel_critico = df.groupby('Nivel')[anos[-1]].mean().idxmax()
    st.info(f"📊 **Foco Prioritário**: {nivel_critico}")

with col_pol2:
    st.subheader("📜 Políticas Vigentes")
    
    if politicas:
        with st.expander("📖 Ver Políticas Completas"):
            st.text(politicas)
    else:
        st.info("💡 Arquivo de políticas não encontrado")

col_pol1, col_pol2 = st.columns([2, 1])

with col_pol1:
    st.subheader("💡 Recomendações Automáticas")
    
    # Gerar recomendações baseadas nos dados
    recomendacoes = []
    
    # Províncias críticas precisam de intervenção
    for idx, row in df_risco.head(3).iterrows():
        if 'CRÍTICO' in row['Classificação']:
            recomendacoes.append(f"🔴 **{row['Província']}**: Intervenção urgente necessária. Priorizar programas de distribuição alimentar e capacitação agrícola.")
        elif 'ATENÇÃO' in row['Classificação']:
            recomendacoes.append(f"🟠 **{row['Província']}**: Monitoramento intensificado. Implementar programas preventivos de nutrição.")
    
    for rec in recomendacoes:
        st.info(rec)
    
    # Recomendações gerais
    st.subheader("📌 Recomendações Gerais")
    
    media_inicial = df[anos[0]].mean()
    media_final = df[anos[-1]].mean()
    variacao_nacional = ((media_final - media_inicial) / media_inicial) * 100
    
    if variacao_nacional > 0:
        st.warning("⚠️ **Tendência Nacional de Aumento**: Revisar estratégias do PNDSA 2013-2025")
    else:
        st.success("✅ **Tendência Nacional de Redução**: Manter políticas atuais e escalar para províncias críticas")
    
    # Nível mais crítico
    nivel_critico = df.groupby('Nivel')[anos[-1]].mean().idxmax()
    st.info(f"📊 **Foco Prioritário**: {nivel_critico} - Requer programas específicos de mitigação")

with col_pol2:
    st.subheader("📜 Políticas Vigentes")
    
    if politicas:
        with st.expander("📖 Ver Políticas Completas"):
            st.text(politicas)
    else:
        st.info("💡 Dica: Crie o arquivo `data/politicas_angola.txt` para ver as políticas públicas")

# ============================================
# SEÇÃO 7: CORRELAÇÕES E ANÁLISE AVANÇADA
# ============================================
st.markdown("---")
st.header("🔗 ANÁLISE DE CORRELAÇÕES")
st.markdown("---")

# Matriz de correlação entre anos
col_corr1, col_corr2 = st.columns(2)

with col_corr1:
    st.subheader("Correlação entre Anos")
    
    df_corr = df[anos].corr()
    
    fig_corr = px.imshow(
        df_corr,
        text_auto='.2f',
        aspect='auto',
        color_continuous_scale='RdBu_r',
        title="Matriz de Correlação entre Anos"
    )
    fig_corr.update_layout(height=400)
    st.plotly_chart(fig_corr, use_container_width=True)

with col_corr2:
    st.subheader("Correlação entre Níveis")
    
    # Pivotar dados para correlação entre níveis
    df_pivot = df.pivot_table(values=anos[-1], index='Provincia', columns='Nivel')
    df_corr_niveis = df_pivot.corr()
    
    fig_corr2 = px.imshow(
        df_corr_niveis,
        text_auto='.2f',
        aspect='auto',
        color_continuous_scale='RdBu_r',
        title=f"Correlação entre Níveis ({anos[-1]})"
    )
    fig_corr2.update_layout(height=400)
    st.plotly_chart(fig_corr2, use_container_width=True)

# Teste estatístico
with st.expander("📊 Testes Estatísticos Avançados"):
    st.subheader("Teste de Normalidade (Shapiro-Wilk)")
    
    for ano in anos:
        stat, p_value = stats.shapiro(df[ano])
        normal = "✅ Normal" if p_value > 0.05 else "❌ Não Normal"
        st.write(f"**{ano}**: W={stat:.3f}, p={p_value:.3f} - {normal}")
    
    st.subheader("ANOVA entre Níveis")
    
    grupos = [df[df['Nivel'] == nivel][anos[-1]] for nivel in df['Nivel'].unique()]
    f_stat, p_anova = stats.f_oneway(*grupos)
    
    significativo = "✅ Significativo (p < 0.05)" if p_anova < 0.05 else "❌ Não Significativo"
    st.write(f"F={f_stat:.2f}, p={p_anova:.4f} - {significativo}")

# ============================================
# RODAPÉ
# ============================================
st.markdown("---")
st.sidebar.markdown("---")
st.sidebar.success("✨ **Gêmeo Digital Inteligente**\n\n🧠 Análise estatística completa\n📊 Chi-Quadrado (χ²)\n🔮 Previsões até 2026\n⚠️ Alertas automáticos\n📋 Recomendações baseadas em políticas")

# Exportar relatório
if st.button("📥 Exportar Relatório Estatístico"):
    # Criar DataFrame para exportação
    df_export = df_stats.copy()
    csv = df_export.to_csv(index=False, encoding='utf-8-sig')
    
    st.download_button(
        label="📥 Baixar CSV",
        data=csv,
        file_name=f"relatorio_estatistico_fies_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )
    