# -*- coding: utf-8 -*-
"""
03_Correlacao_FIES_Nutricao.py
DATANGOLA - Módulo de Análise de Correlação
Plataforma Integrada de Análise e Relatório para Desenvolvimento
"""

# 1. IMPORTS PADRÃO
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import streamlit as st
from datetime import datetime

# 2. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Correlação - DATANGOLA",
    page_icon="🔗",
    layout="wide"
)

# 3. SIDEBAR - INFORMAÇÕES DO DESENVOLVEDOR
st.sidebar.markdown("---")
st.sidebar.markdown("### 👨‍🔬 Sobre o Desenvolvedor")
st.sidebar.info("""
**Upale Kahilo Lamber** 🇦🇴

👨‍🏫 Professor-Investigador - UNIC

🎓 Doutorando em Saúde Pública (Epidemiologia)

🏆 Vencedor Hackathon AgriTech Timbuktoo 2026

📊 Especialista em DATANGOLA & Python

📧 upale.lamber@unic.ac.ao
""")

# ... RESTO DO SEU CÓDIGO DE ANÁLISE (MANTER) ...

# NO FINAL DO ARQUIVO - FOOTER
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
        <strong>🇦🇴 DATANGOLA</strong> | 
        Plataforma Integrada de Análise e Relatório para Desenvolvimento | 
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
# -*- coding: utf-8 -*-
"""
03_Correlacao_FIES_Nutricao.py
"""

# IMPORTS
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import streamlit as st
from datetime import datetime  # ← ADICIONE ESTE

# FUNÇÕES DE FOOTER E SIDEBAR (COPIADAS)
def footer():
    """Exibe o rodapé"""
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
            <strong>🌍 Gêmeo Digital - FIES Angola</strong> | 
            Desenvolvido por <strong>Upale Kahilo Lamber</strong> 🇦🇴 | 
            © {ano_atual}
        </div>
        <div style='font-size: 11px;'>
            📊 UNIC | 📧 upale.lamber@unic.ac.ao
        </div>
    </div>
    <div style='padding-bottom: 100px;'></div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)


def sidebar_info():
    """Exibe info na sidebar"""
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 👨‍🔬 Sobre o Desenvolvedor")
    st.sidebar.info("""
    **Upale Kahilo Lamber** 🇦🇴
    
    👨‍🏫 Professor-Investigador - UNIC
    
    🎓 Doutorando em Saúde Pública
    
    🏆 Vencedor Hackathon AgriTech 2026
    
    📧 upale.lamber@unic.ac.ao
    """)

# CONFIGURAÇÃO
st.set_page_config(page_title="Correlação FIES-Nutrição", layout="wide")

# ... RESTO DO SEU CÓDIGO DE ANÁLISE ...

# NO FINAL DO ARQUIVO:
sidebar_info()
footer()
# 4. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Correlação FIES-Nutrição", layout="wide")

# ============================================================
# CARREGAMENTO DE DADOS
# ============================================================

@st.cache_data
def carregar_dados_fies():
    """Carrega dados FIES"""
    dados_fies = {
        'provincia': ['Bengo', 'Benguela', 'Bié', 'Cabinda', 'Cuanza Norte', 'Cuanza Sul', 
                     'Cuando Cubango', 'Cunene', 'Huambo', 'Huíla', 'Luanda', 'Lunda Norte', 
                     'Lunda Sul', 'Malanje', 'Moxico', 'Namibe', 'Uíge', 'Zaire'],
        'ano': [2023] * 18,
        'inseguranca_total': [93.0, 77.1, 93.7, 86.4, 88.8, 59.0, 94.4, 67.3, 82.5, 73.9, 
                             62.3, 99.5, 86.8, 75.6, 48.8, 83.9, 76.1, 96.9],
        'inseguranca_moderada': [78.8, 62.3, 72.4, 59.9, 58.6, 50.7, 47.0, 60.1, 52.4, 57.4, 
                                50.2, 28.8, 55.6, 53.0, 34.3, 50.1, 68.0, 65.8],
        'inseguranca_severa': [14.4, 14.7, 21.3, 26.5, 30.2, 8.1, 47.4, 7.2, 30.0, 16.5, 
                              12.0, 70.7, 31.3, 22.6, 14.6, 33.8, 8.1, 31.1]
    }
    return pd.DataFrame(dados_fies)

@st.cache_data
def carregar_dados_nutricao():
    """Carrega dados de nutrição"""
    dados_nut = {
        'Província': ['Bengo', 'Benguela', 'Bié', 'Cabinda', 'Cuanza Norte', 'Cuanza Sul', 
                     'Cuando Cubango', 'Cunene', 'Huambo', 'Huíla', 'Luanda', 'Lunda Norte', 
                     'Lunda Sul', 'Malanje', 'Moxico', 'Namibe', 'Uíge', 'Zaire'],
        'Desnutrição Crónica (Nanismo) [%]': [30.9, 50.9, 51.6, 15.2, 32.8, 45.9, 43.6, 26.0, 
                                              51.2, 40.0, 24.9, 42.9, 33.3, 38.5, 41.2, 24.1, 44.4, 31.3],
        'Prevalência de Anemia (6-59 meses) [%]': [59.2, 50.3, 50.1, 56.1, 59.7, 57.0, 53.2, 48.1, 
                                                    39.2, 45.7, 55.7, 67.2, 66.8, 62.3, 55.6, 43.6, 72.5, 47.1],
        'Diversidade Alimentar Mínima [%]': [36.3, 11.4, 14.0, 37.2, 30.1, 12.0, 16.9, 15.1, 
                                              14.3, 10.7, 32.8, 13.8, 24.1, 20.4, 12.3, 33.2, 16.3, 35.8]
    }
    df = pd.DataFrame(dados_nut)
    df['Província'] = df['Província'].str.strip().str.title()
    return df

df_fies = carregar_dados_fies()
df_nutricao = carregar_dados_nutricao()

# ============================================================
# PREPARAÇÃO DOS DADOS
# ============================================================

def preparar_dados(df_fies, df_nut):
    """Prepara dados para correlação"""
    fies_2023 = df_fies[df_fies['ano'] == 2023].copy()
    fies_pivot = fies_2023.pivot_table(
        index='provincia',
        values=['inseguranca_moderada', 'inseguranca_severa', 'inseguranca_total'],
        aggfunc='mean'
    ).reset_index()
    fies_pivot.columns = ['Provincia', 'FIES_Moderada', 'FIES_Severa', 'FIES_Total']
    
    df_nut = df_nut.copy()
    df_nut['Provincia'] = df_nut['Província'].str.strip().str.title()
    
    df_merged = pd.merge(fies_pivot, df_nut, on='Provincia', how='inner')
    return df_merged

df_analise = preparar_dados(df_fies, df_nutricao)

if df_analise.empty:
    st.error("❌ Não foi possível unir os dados!")
    st.stop()

# ============================================================
# TÍTULO PRINCIPAL
# ============================================================

st.title("📊 Correlação: Insegurança Alimentar (FIES) e Desnutrição - Angola 2023")
st.markdown("---")

# ============================================================
# RESUMO EXECUTIVO
# ============================================================

st.subheader("📋 Resumo Executivo")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Média FIES Total", f"{df_analise['FIES_Total'].mean():.1f}%")
with col2:
    st.metric("Média Desnutrição Crónica", f"{df_analise['Desnutrição Crónica (Nanismo) [%]'].mean():.1f}%")
with col3:
    st.metric("Média Anemia", f"{df_analise['Prevalência de Anemia (6-59 meses) [%]'].mean():.1f}%")
with col4:
    corr = stats.pearsonr(df_analise['FIES_Total'], df_analise['Desnutrição Crónica (Nanismo) [%]'])[0]
    st.metric("Correlação FIES-Stunting", f"{corr:.3f}")

st.markdown("---")

# ============================================================
# GRÁFICOS PRINCIPAIS
# ============================================================

st.subheader("📈 Visualizações Gráficas")

# Gráfico 1: Dispersão FIES vs Stunting
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Figura 1: Relação entre Insegurança Alimentar e Desnutrição Crónica**")
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    sns.regplot(data=df_analise, x='FIES_Total', y='Desnutrição Crónica (Nanismo) [%]', 
                ax=ax1, scatter_kws={'s':100, 'alpha':0.7}, line_kws={'color':'red'})
    
    # Adicionar rótulos nas províncias
    for i, row in df_analise.iterrows():
        ax1.annotate(row['Provincia'], (row['FIES_Total'], row['Desnutrição Crónica (Nanismo) [%]']), 
                    fontsize=8, alpha=0.7)
    
    ax1.set_xlabel('Insegurança Alimentar Total (%)', fontsize=11)
    ax1.set_ylabel('Desnutrição Crónica - Stunting (%)', fontsize=11)
    ax1.set_title('Correlação: FIES vs Desnutrição Crónica', fontsize=12, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    st.pyplot(fig1)

with col2:
    st.markdown("**Figura 2: Relação entre Insegurança Alimentar e Anemia**")
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    sns.regplot(data=df_analise, x='FIES_Total', y='Prevalência de Anemia (6-59 meses) [%]', 
                ax=ax2, scatter_kws={'s':100, 'alpha':0.7, 'color':'orange'}, line_kws={'color':'darkred'})
    
    for i, row in df_analise.iterrows():
        ax2.annotate(row['Provincia'], (row['FIES_Total'], row['Prevalência de Anemia (6-59 meses) [%]']), 
                    fontsize=8, alpha=0.7)
    
    ax2.set_xlabel('Insegurança Alimentar Total (%)', fontsize=11)
    ax2.set_ylabel('Prevalência de Anemia (%)', fontsize=11)
    ax2.set_title('Correlação: FIES vs Anemia', fontsize=12, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    st.pyplot(fig2)
# ============================================================
# FIGURAS 1A e 2A: SCATTER PLOTS COMPLETAMENTE ANOTADOS
# ============================================================

st.markdown("---")
st.subheader("📊 Gráficos de Dispersão com Análise Detalhada")
st.info("📖 **Scatter Plot com Regressão Linear:** Mostra a relação entre duas variáveis contínuas. Cada ponto representa uma província.")

col1, col2 = st.columns(2)

# ========== FIGURA 1A: FIES vs DESNUTRIÇÃO COM ANOTAÇÕES ==========
with col1:
    st.markdown("**Figura 1A: FIES vs Desnutrição Crónica (Completo)**")
    
    fig1a, ax1a = plt.subplots(figsize=(9, 7))
    
    # Scatter plot
    scatter1a = ax1a.scatter(df_analise['FIES_Total'], 
                            df_analise['Desnutrição Crónica (Nanismo) [%]'],
                            s=150, alpha=0.7, c='steelblue', edgecolors='black', 
                            linewidth=1.5)
    
    # Linha de regressão
    z1a = np.polyfit(df_analise['FIES_Total'], 
                     df_analise['Desnutrição Crónica (Nanismo) [%]'], 1)
    p1a = np.poly1d(z1a)
    ax1a.plot(df_analise['FIES_Total'].sort_values(), 
             p1a(df_analise['FIES_Total'].sort_values()), 
             "r-", linewidth=2.5, label=f'Regressão: y={z1a[0]:.3f}x+{z1a[1]:.2f}')
    
    # Intervalo de confiança
    ax1a.fill_between(df_analise['FIES_Total'].sort_values(),
                     p1a(df_analise['FIES_Total'].sort_values()) - 2*np.std(df_analise['Desnutrição Crónica (Nanismo) [%]']),
                     p1a(df_analise['FIES_Total'].sort_values()) + 2*np.std(df_analise['Desnutrição Crónica (Nanismo) [%]']),
                     alpha=0.2, color='red', label='Intervalo de Confiança (95%)')
    
    # Adicionar nomes das províncias
    for i, row in df_analise.iterrows():
        ax1a.annotate(row['Provincia'], 
                     (row['FIES_Total'], row['Desnutrição Crónica (Nanismo) [%]']),
                     fontsize=8, alpha=0.8,
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))
    
    # Estatísticas no gráfico
    corr1a = stats.pearsonr(df_analise['FIES_Total'], 
                           df_analise['Desnutrição Crónica (Nanismo) [%]'])
    r2_1a = corr1a[0]**2
    
    stats_text1a = (f'Estatísticas:\n'
                   f'• Correlação (r): {corr1a[0]:.3f}\n'
                   f'• R²: {r2_1a:.3f}\n'
                   f'• p-valor: {corr1a[1]:.4f}\n'
                   f'• N: {len(df_analise)} províncias')
    
    ax1a.text(0.02, 0.98, stats_text1a, transform=ax1a.transAxes,
             fontsize=9, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # Províncias extremas
    prov_min_fies = df_analise.loc[df_analise['FIES_Total'].idxmin(), 'Provincia']
    prov_max_fies = df_analise.loc[df_analise['FIES_Total'].idxmax(), 'Provincia']
    prov_min_stunt = df_analise.loc[df_analise['Desnutrição Crónica (Nanismo) [%]'].idxmin(), 'Provincia']
    prov_max_stunt = df_analise.loc[df_analise['Desnutrição Crónica (Nanismo) [%]'].idxmax(), 'Provincia']
    
    ax1a.annotate(f'Mín FIES\n({prov_min_fies})', 
                 (df_analise['FIES_Total'].min(), 
                  df_analise.loc[df_analise['FIES_Total'].idxmin(), 'Desnutrição Crónica (Nanismo) [%]']),
                 xytext=(-80, 30), textcoords='offset points', fontsize=8,
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3'),
                 bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    ax1a.annotate(f'Máx FIES\n({prov_max_fies})', 
                 (df_analise['FIES_Total'].max(), 
                  df_analise.loc[df_analise['FIES_Total'].idxmax(), 'Desnutrição Crónica (Nanismo) [%]']),
                 xytext=(-80, -50), textcoords='offset points', fontsize=8,
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3'),
                 bbox=dict(boxstyle='round', facecolor='red', alpha=0.7))
    
    ax1a.set_xlabel('Insegurança Alimentar Total (%)', fontsize=11, fontweight='bold')
    ax1a.set_ylabel('Desnutrição Crónica - Stunting (%)', fontsize=11, fontweight='bold')
    ax1a.set_title('FIES vs Desnutrição Crónica\n(Angola 2023)', fontsize=12, fontweight='bold')
    ax1a.grid(True, alpha=0.3)
    ax1a.legend(loc='lower right', fontsize=8)
    
    plt.tight_layout()
    st.pyplot(fig1a)

# ========== FIGURA 2A: FIES vs ANEMIA COM ANOTAÇÕES ==========
with col2:
    st.markdown("**Figura 2A: FIES vs Anemia (Completo)**")
    
    fig2a, ax2a = plt.subplots(figsize=(9, 7))
    
    # Scatter plot
    scatter2a = ax2a.scatter(df_analise['FIES_Total'], 
                            df_analise['Prevalência de Anemia (6-59 meses) [%]'],
                            s=150, alpha=0.7, c='orange', edgecolors='black', 
                            linewidth=1.5)
    
    # Linha de regressão
    z2a = np.polyfit(df_analise['FIES_Total'], 
                     df_analise['Prevalência de Anemia (6-59 meses) [%]'], 1)
    p2a = np.poly1d(z2a)
    ax2a.plot(df_analise['FIES_Total'].sort_values(), 
             p2a(df_analise['FIES_Total'].sort_values()), 
             "darkred", linewidth=2.5, label=f'Regressão: y={z2a[0]:.3f}x+{z2a[1]:.2f}')
    
    # Intervalo de confiança
    ax2a.fill_between(df_analise['FIES_Total'].sort_values(),
                     p2a(df_analise['FIES_Total'].sort_values()) - 2*np.std(df_analise['Prevalência de Anemia (6-59 meses) [%]']),
                     p2a(df_analise['FIES_Total'].sort_values()) + 2*np.std(df_analise['Prevalência de Anemia (6-59 meses) [%]']),
                     alpha=0.2, color='darkred', label='Intervalo de Confiança (95%)')
    
    # Adicionar nomes das províncias
    for i, row in df_analise.iterrows():
        ax2a.annotate(row['Provincia'], 
                     (row['FIES_Total'], row['Prevalência de Anemia (6-59 meses) [%]']),
                     fontsize=7, alpha=0.8,
                     bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7))
    
    # Estatísticas no gráfico
    corr2a = stats.pearsonr(df_analise['FIES_Total'], 
                           df_analise['Prevalência de Anemia (6-59 meses) [%]'])
    r2_2a = corr2a[0]**2
    
    stats_text2a = (f'Estatísticas:\n'
                   f'• Correlação (r): {corr2a[0]:.3f}\n'
                   f'• R²: {r2_2a:.3f}\n'
                   f'• p-valor: {corr2a[1]:.4f}\n'
                   f'• N: {len(df_analise)} províncias')
    
    ax2a.text(0.02, 0.98, stats_text2a, transform=ax2a.transAxes,
             fontsize=9, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
    
    # Províncias extremas
    prov_min_anemia = df_analise.loc[df_analise['Prevalência de Anemia (6-59 meses) [%]'].idxmin(), 'Provincia']
    prov_max_anemia = df_analise.loc[df_analise['Prevalência de Anemia (6-59 meses) [%]'].idxmax(), 'Provincia']
    
    ax2a.annotate(f'Mín Anemia\n({prov_min_anemia})', 
                 (df_analise['FIES_Total'].min(), 
                  df_analise.loc[df_analise['FIES_Total'].idxmin(), 'Prevalência de Anemia (6-59 meses) [%]']),
                 xytext=(-80, 30), textcoords='offset points', fontsize=8,
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3'),
                 bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))
    
    ax2a.annotate(f'Máx Anemia\n({prov_max_anemia})', 
                 (df_analise['FIES_Total'].max(), 
                  df_analise.loc[df_analise['FIES_Total'].idxmax(), 'Prevalência de Anemia (6-59 meses) [%]']),
                 xytext=(-80, -50), textcoords='offset points', fontsize=8,
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3'),
                 bbox=dict(boxstyle='round', facecolor='red', alpha=0.7))
    
    ax2a.set_xlabel('Insegurança Alimentar Total (%)', fontsize=11, fontweight='bold')
    ax2a.set_ylabel('Prevalência de Anemia (6-59 meses) (%)', fontsize=11, fontweight='bold')
    ax2a.set_title('FIES vs Anemia\n(Angola 2023)', fontsize=12, fontweight='bold')
    ax2a.grid(True, alpha=0.3)
    ax2a.legend(loc='lower right', fontsize=8)
    
    plt.tight_layout()
    st.pyplot(fig2a)

# ============================================================
# TABELA EXPLICATIVA
# ============================================================

st.markdown("---")
st.markdown("**📖 Como Interpretar os Gráficos de Dispersão:**")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**🔵 Pontos (Bolinhas)**")
    st.write("""
    - Cada ponto = **1 província**
    - Posição X = **Valor de FIES**
    - Posição Y = **Valor do Indicador** (Desnutrição ou Anemia)
    - Tamanho = **Todos iguais** (18 províncias)
    """)

with col2:
    st.markdown("**🔴 Linha de Regressão**")
    st.write("""
    - Mostra a **tendência geral**
    - **Inclinação positiva** (sobe) = Correlação positiva
    - **Inclinação negativa** (desce) = Correlação negativa
    - **Plana** = Sem correlação
    - **Equação:** y = ax + b
    """)

with col3:
    st.markdown("**🌸 Sombra (Intervalo)**")
    st.write("""
    - **Intervalo de confiança (95%)**
    - Mostra a **precisão** da estimativa
    - **Sombra estreita** = Alta precisão
    - **Sombra larga** = Baixa precisão
    - 95% dos dados deveriam estar dentro
    """)

st.markdown("---")
st.markdown("**📊 Resumo das Correlações:**")

resumo_corr = pd.DataFrame({
    'Indicador': ['Desnutrição Crónica', 'Anemia (6-59 meses)'],
    'Correlação (r)': [f'{corr1a[0]:.3f}', f'{corr2a[0]:.3f}'],
    'R²': [f'{r2_1a:.3f}', f'{r2_2a:.3f}'],
    'p-valor': [f'{corr1a[1]:.4f}', f'{corr2a[1]:.4f}'],
    'Significância': ['Não significativo' if corr1a[1] > 0.05 else 'Significativo',
                     'Não significativo' if corr2a[1] > 0.05 else 'Significativo'],
    'Força': ['Muito Fraca' if abs(corr1a[0]) < 0.3 else 'Moderada' if abs(corr1a[0]) < 0.6 else 'Forte',
             'Muito Fraca' if abs(corr2a[0]) < 0.3 else 'Moderada' if abs(corr2a[0]) < 0.6 else 'Forte']
})

st.dataframe(resumo_corr, use_container_width=True)

st.info("""
💡 **Interpretação Final:**
- **r ≈ 0** (entre -0.3 e +0.3): Correlação muito fraca ou inexistente
- **R²**: Percentagem da variação explicada pelo modelo (ex: R²=0.001 = 0.1% explicado)
- **p-valor > 0.05**: Correlação NÃO é estatisticamente significativa
- **Conclusão:** FIES **NÃO explica** significativamente desnutrição ou anemia em Angola
""")
# Gráfico 3: Mapa de calor das correlações
st.markdown("**Figura 3: Matriz de Correlação entre Todos os Indicadores**")
fig3, ax3 = plt.subplots(figsize=(10, 8))

variaveis = ['FIES_Total', 'FIES_Severa', 'Desnutrição Crónica (Nanismo) [%]', 
             'Prevalência de Anemia (6-59 meses) [%]', 'Diversidade Alimentar Mínima [%]']
matriz_corr = df_analise[variaveis].corr()

sns.heatmap(matriz_corr, annot=True, cmap='RdYlGn_r', center=0, fmt='.3f', 
            linewidths=0.5, ax=ax3, square=True, cbar_kws={"shrink": .8})
plt.title('Matriz de Correlação de Pearson', fontsize=14, fontweight='bold', pad=20)
plt.tight_layout()
st.pyplot(fig3)

# Gráfico 4: Ranking das províncias
st.markdown("**Figura 4: Ranking das 10 Províncias com Maior Vulnerabilidade**")

df_analise['Indice_Vulnerabilidade'] = (
    df_analise['FIES_Total'] * df_analise['Desnutrição Crónica (Nanismo) [%]'] / 100
)

hotspots = df_analise.nlargest(10, 'Indice_Vulnerabilidade')

fig4, ax4 = plt.subplots(figsize=(10, 6))
colors = plt.cm.Reds(np.linspace(0.4, 0.9, len(hotspots)))
bars = ax4.barh(hotspots['Provincia'], hotspots['Indice_Vulnerabilidade'], color=colors)
ax4.set_xlabel('Índice de Vulnerabilidade (FIES × Stunting)', fontsize=11)
ax4.set_title('Top 10 Províncias Mais Vulneráveis', fontsize=12, fontweight='bold')
ax4.grid(axis='x', alpha=0.3)

# Adicionar valores nas barras
for i, (idx, row) in enumerate(hotspots.iterrows()):
    ax4.text(row['Indice_Vulnerabilidade'] + 0.5, i, f"{row['Indice_Vulnerabilidade']:.1f}", 
            va='center', fontsize=9, fontweight='bold')

plt.tight_layout()
st.pyplot(fig4)

# ============================================================
# FIGURA 5A: BOXPLOTS COM TODOS OS VALORES EXPLICADOS
# ============================================================

st.markdown("---")
st.markdown("**Figura 5A: Distribuição com Valores Estatísticos Detalhados**")
st.info("📊 **Legenda:** Cada elemento do boxplot representa um indicador estatístico da distribuição dos dados.")

fig5a, axes5a = plt.subplots(1, 2, figsize=(16, 7))

# ========== BOXPLOT FIES COM ANOTAÇÕES ==========
bp_fies = axes5a[0].boxplot(df_analise['FIES_Total'], 
                             vert=True, 
                             patch_artist=True,
                             labels=['FIES Total'])
                            
# Colorir a caixa
for element in bp_fies['boxes']:
    element.set_facecolor('skyblue')
    element.set_alpha(0.7)

# Calcular estatísticas
fies_min = df_analise['FIES_Total'].min()
fies_q1 = df_analise['FIES_Total'].quantile(0.25)
fies_median = df_analise['FIES_Total'].median()
fies_mean = df_analise['FIES_Total'].mean()
fies_q3 = df_analise['FIES_Total'].quantile(0.75)
fies_max = df_analise['FIES_Total'].max()

# Adicionar anotações no gráfico FIES
axes5a[0].text(1.15, fies_max, f'Máximo\n{fies_max:.1f}%', 
              ha='left', va='bottom', fontsize=9, fontweight='bold',
              bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))

axes5a[0].text(1.15, fies_q3, f'Q3 (75%)\n{fies_q3:.1f}%', 
              ha='left', va='center', fontsize=9,
              bbox=dict(boxstyle='round', facecolor='orange', alpha=0.3))

axes5a[0].text(1.15, fies_median, f'Mediana (50%)\n{fies_median:.1f}%', 
              ha='left', va='center', fontsize=9, fontweight='bold',
              bbox=dict(boxstyle='round', facecolor='green', alpha=0.3))

axes5a[0].text(1.15, fies_mean, f'Média\n{fies_mean:.1f}%', 
              ha='left', va='center', fontsize=9,
              bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

axes5a[0].text(1.15, fies_q1, f'Q1 (25%)\n{fies_q1:.1f}%', 
              ha='left', va='center', fontsize=9,
              bbox=dict(boxstyle='round', facecolor='orange', alpha=0.3))

axes5a[0].text(1.15, fies_min, f'Mínimo\n{fies_min:.1f}%', 
              ha='left', va='top', fontsize=9, fontweight='bold',
              bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))

# Linha da média
axes5a[0].axhline(y=fies_mean, color='gold', linestyle='--', 
                 linewidth=2, label=f'Média: {fies_mean:.1f}%')

axes5a[0].set_ylabel('Insegurança Alimentar Total (%)', fontsize=11)
axes5a[0].set_title('FIES Total - Elementos do Boxplot', fontsize=12, fontweight='bold')
axes5a[0].grid(axis='y', alpha=0.3)
axes5a[0].set_xticks([])
axes5a[0].legend(loc='upper right')

# ========== BOXPLOT DESNUTRIÇÃO COM ANOTAÇÕES ==========
bp_stunt = axes5a[1].boxplot(df_analise['Desnutrição Crónica (Nanismo) [%]'], 
                              vert=True, 
                              patch_artist=True,
                              labels=['Desnutrição'])
                            
for element in bp_stunt['boxes']:
    element.set_facecolor('salmon')
    element.set_alpha(0.7)

# Calcular estatísticas
stunt_min = df_analise['Desnutrição Crónica (Nanismo) [%]'].min()
stunt_q1 = df_analise['Desnutrição Crónica (Nanismo) [%]'].quantile(0.25)
stunt_median = df_analise['Desnutrição Crónica (Nanismo) [%]'].median()
stunt_mean = df_analise['Desnutrição Crónica (Nanismo) [%]'].mean()
stunt_q3 = df_analise['Desnutrição Crónica (Nanismo) [%]'].quantile(0.75)
stunt_max = df_analise['Desnutrição Crónica (Nanismo) [%]'].max()

# Adicionar anotações no gráfico Desnutrição
axes5a[1].text(1.15, stunt_max, f'Máximo\n{stunt_max:.1f}%', 
              ha='left', va='bottom', fontsize=9, fontweight='bold',
              bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))

axes5a[1].text(1.15, stunt_q3, f'Q3 (75%)\n{stunt_q3:.1f}%', 
              ha='left', va='center', fontsize=9,
              bbox=dict(boxstyle='round', facecolor='orange', alpha=0.3))

axes5a[1].text(1.15, stunt_median, f'Mediana (50%)\n{stunt_median:.1f}%', 
              ha='left', va='center', fontsize=9, fontweight='bold',
              bbox=dict(boxstyle='round', facecolor='green', alpha=0.3))

axes5a[1].text(1.15, stunt_mean, f'Média\n{stunt_mean:.1f}%', 
              ha='left', va='center', fontsize=9,
              bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))

axes5a[1].text(1.15, stunt_q1, f'Q1 (25%)\n{stunt_q1:.1f}%', 
              ha='left', va='center', fontsize=9,
              bbox=dict(boxstyle='round', facecolor='orange', alpha=0.3))

axes5a[1].text(1.15, stunt_min, f'Mínimo\n{stunt_min:.1f}%', 
              ha='left', va='top', fontsize=9, fontweight='bold',
              bbox=dict(boxstyle='round', facecolor='red', alpha=0.3))

# Linha da média
axes5a[1].axhline(y=stunt_mean, color='gold', linestyle='--', 
                 linewidth=2, label=f'Média: {stunt_mean:.1f}%')

axes5a[1].set_ylabel('Desnutrição Crónica (%)', fontsize=11)
axes5a[1].set_title('Desnutrição Crónica - Elementos do Boxplot', fontsize=12, fontweight='bold')
axes5a[1].grid(axis='y', alpha=0.3)
axes5a[1].set_xticks([])
axes5a[1].legend(loc='upper right')

plt.tight_layout()
st.pyplot(fig5a)

# Tabela explicativa
st.markdown("**📖 O Que Cada Elemento Representa:**")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**FIES Total:**")
    st.write(f"🔴 **Máximo:** {fies_max:.1f}% (Lunda Norte)")
    st.write(f"🟠 **Q3 (75%):** {fies_q3:.1f}% (75% das províncias ≤ este valor)")
    st.write(f"🟢 **Mediana:** {fies_median:.1f}% (50% acima, 50% abaixo)")
    st.write(f"🟡 **Média:** {fies_mean:.1f}% (valor médio)")
    st.write(f"🟠 **Q1 (25%):** {fies_q1:.1f}% (25% das províncias ≤ este valor)")
    st.write(f"🔴 **Mínimo:** {fies_min:.1f}% (Cuanza Sul)")

with col2:
    st.markdown("**Desnutrição Crónica:**")
    st.write(f"🔴 **Máximo:** {stunt_max:.1f}% (Bié)")
    st.write(f"🟠 **Q3 (75%):** {stunt_q3:.1f}%")
    st.write(f"🟢 **Mediana:** {stunt_median:.1f}%")
    st.write(f"🟡 **Média:** {stunt_mean:.1f}%")
    st.write(f"🟠 **Q1 (25%):** {stunt_q1:.1f}%")
    st.write(f"🔴 **Mínimo:** {stunt_min:.1f}% (Cabinda)")

st.markdown("---")

# ============================================================
# FIGURA 5B: BOXPLOTS SIMPLIFICADOS (VERSÃO ACTUAL)
# ============================================================

st.markdown("**Figura 5B: Distribuição Simplificada (Visualização Rápida)**")

fig5b, axes5b = plt.subplots(1, 2, figsize=(14, 6))

# Boxplot FIES simplificado
sns.boxplot(y=df_analise['FIES_Total'], ax=axes5b[0], color='skyblue')
axes5b[0].text(0.5, fies_median + 2, f'Mediana: {fies_median:.1f}%', 
              ha='center', va='bottom', fontsize=9, fontweight='bold',
              bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
axes5b[0].text(0.5, fies_mean + 2, f'Média: {fies_mean:.1f}%', 
              ha='center', va='bottom', fontsize=9,
              bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
axes5b[0].set_ylabel('Insegurança Alimentar Total (%)', fontsize=11)
axes5b[0].set_title('Distribuição FIES Total', fontsize=12, fontweight='bold')
axes5b[0].grid(axis='y', alpha=0.3)

# Boxplot Desnutrição simplificado
sns.boxplot(y=df_analise['Desnutrição Crónica (Nanismo) [%]'], 
           ax=axes5b[1], color='salmon')
axes5b[1].text(0.5, stunt_median + 2, f'Mediana: {stunt_median:.1f}%', 
              ha='center', va='bottom', fontsize=9, fontweight='bold',
              bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
axes5b[1].text(0.5, stunt_mean + 2, f'Média: {stunt_mean:.1f}%', 
              ha='center', va='bottom', fontsize=9,
              bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.5))
axes5b[1].set_ylabel('Desnutrição Crónica (%)', fontsize=11)
axes5b[1].set_title('Distribuição Desnutrição Crónica', fontsize=12, fontweight='bold')
axes5b[1].grid(axis='y', alpha=0.3)

plt.tight_layout()
st.pyplot(fig5b)
# ============================================================
# INTERPRETAÇÃO DOS RESULTADOS
# ============================================================

st.subheader("🔍 Interpretação dos Resultados")

# Calcular correlações
corr_fies_stunting = stats.pearsonr(df_analise['FIES_Total'], df_analise['Desnutrição Crónica (Nanismo) [%]'])
corr_fies_anemia = stats.pearsonr(df_analise['FIES_Total'], df_analise['Prevalência de Anemia (6-59 meses) [%]'])

with st.expander("📖 Interpretação Detalhada da Correlação", expanded=True):
    
    st.markdown("### 1. **Correlação entre Insegurança Alimentar e Desnutrição Crónica**")
    st.write(f"""
    - **Coeficiente de correlação (r)**: {corr_fies_stunting[0]:.3f}
    - **Valor-p**: {corr_fies_stunting[1]:.4f}
    - **Nível de significância**: {'Estatisticamente significativo' if corr_fies_stunting[1] < 0.05 else 'Não significativo'}
    """)
    
    if abs(corr_fies_stunting[0]) < 0.3:
        st.info("📊 **Interpretação**: Correlação fraca - A insegurança alimentar explica pouco da variação na desnutrição crónica. Outros factores (acesso a serviços de saúde, saneamento, educação) podem ter maior influência.")
    elif abs(corr_fies_stunting[0]) < 0.6:
        st.warning("📊 **Interpretação**: Correlação moderada - Existe uma relação moderada entre insegurança alimentar e desnutrição crónica, sugerindo que ambos os problemas estão relacionados mas não são determinados exclusivamente um pelo outro.")
    else:
        st.error("📊 **Interpretação**: Correlação forte - A insegurança alimentar está fortemente associada à desnutrição crónica, indicando que intervenções na segurança alimentar podem ter impacto directo na redução do stunting.")
    
    st.markdown("---")
    
    st.markdown("### 2. **Correlação entre Insegurança Alimentar e Anemia**")
    st.write(f"""
    - **Coeficiente de correlação (r)**: {corr_fies_anemia[0]:.3f}
    - **Valor-p**: {corr_fies_anemia[1]:.4f}
    """)
    
    if abs(corr_fies_anemia[0]) < 0.3:
        st.info("📊 **Interpretação**: Correlação fraca - A anemia pode estar mais relacionada com factores como parasitoses, doenças infecciosas e qualidade da dieta do que apenas com quantidade de alimentos.")
    elif abs(corr_fies_anemia[0]) < 0.6:
        st.warning("📊 **Interpretação**: Correlação moderada - A insegurança alimentar contribui para a anemia, mas outros factores nutricionais e de saúde também são importantes.")
    else:
        st.error("📊 **Interpretação**: Correlação forte - A falta de acesso a alimentos está fortemente ligada à anemia, sugerindo necessidade de intervenções combinadas.")
    
    st.markdown("---")
    
    st.markdown("### 3. **Províncias Prioritárias**")
    st.write("""
    As províncias identificadas com maior índice de vulnerabilidade combinada (FIES × Stunting) 
    requerem intervenções urgentes e integradas. Estas áreas apresentam simultaneamente:
    - Alta prevalência de insegurança alimentar
    - Elevadas taxas de desnutrição crónica infantil
    - Necessidade de programas combinados de segurança alimentar e nutricional
    """)

st.markdown("---")

# ============================================================
# RECOMENDAÇÕES
# ============================================================

st.subheader("💡 Recomendações de Políticas Públicas")

with st.expander("🎯 Recomendações Baseadas em Evidências", expanded=True):
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔴 Intervenções Imediatas (Curto Prazo)")
        st.markdown("""
        1. **Transferências Sociais**
           - Expandir programas de protecção social nas províncias prioritárias
           - Foco em Lunda Norte, Cuando Cubango, Huambo e Bié
        
        2. **Distribuição de Alimentos**
           - Programas de alimentação escolar emergencial
           - Distribuição de suplementos nutricionais para crianças 6-59 meses
        
        3. **Rastreio Nutricional**
           - Campanhas de screening de desnutrição aguda
           - Monitoramento mensal da segurança alimentar
        """)
        
        st.markdown("### 🟡 Intervenções Médio Prazo (1-3 anos)")
        st.markdown("""
        1. **Agricultura Familiar**
           - Distribuição de sementes e ferramentas
           - Formação em técnicas agrícolas resilientes
           - Apoio à diversificação de culturas
        
        2. **Programas de Nutrição**
           - Suplementação com micronutrientes
           - Educação nutricional comunitária
           - Promoção da diversificação alimentar
        
        3. **Infraestrutura Básica**
           - Melhoria do acesso a água potável
           - Saneamento básico nas comunidades
        """)
    
    with col2:
        st.markdown("### 🟢 Intervenções Longo Prazo (3+ anos)")
        st.markdown("""
        1. **Desenvolvimento Rural**
           - Investimento em irrigação
           - Estradas de acesso aos mercados
           - Cadeias de valor agrícolas
        
        2. **Capital Humano**
           - Educação maternal e infantil
           - Formação profissional em nutrição
           - Capacitação de agentes comunitários
        
        3. **Sistemas de Protecção Social**
           - Programas de rede de segurança permanentes
           - Seguro agrícola
           - Sistemas de alerta precoce
        
        4. **Governança**
           - Fortalecimento institucional
           - Coordenação intersectorial
           - Monitoramento e avaliação contínua
        """)
    
    st.markdown("---")
    
    st.markdown("### 📊 Recomendações Específicas por Indicador")
    
    st.markdown("**Para Reduzir Insegurança Alimentar Severa:**")
    st.write("""
    - Priorizar províncias com IA severa > 30%: Lunda Norte (70.7%), Cuando Cubango (47.4%), 
      Namibe (33.8%), Huambo (30.0%), Cuanza Norte (30.2%)
    - Programas de geração de rendimento
    - Apoio à produção local de alimentos
    """)
    
    st.markdown("**Para Reduzir Desnutrição Crónica:**")
    st.write("""
    - Foco em províncias com stunting > 45%: Huambo (51.2%), Bié (51.6%), Benguela (50.9%)
    - Intervenções nos primeiros 1000 dias de vida
    - Promoção do aleitamento materno exclusivo
    - Suplementação nutricional para grávidas
    """)
    
    st.markdown("**Para Combater Anemia:**")
    st.write("""
    - Províncias prioritárias: Uíge (72.5%), Lunda Norte (67.2%), Lunda Sul (66.8%)
    - Suplementação com ferro e ácido fólico
    - Fortalecimento de alimentos (farinhas enriquecidas)
    - Controlo de parasitoses e malária
    """)

st.markdown("---")

# ============================================================
# CONCLUSÕES
# ============================================================

st.subheader("✅ Conclusões Principais")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("""
    **📈 Situação Actual**
    
    - 74.6% da população angolana enfrenta insegurança alimentar moderada ou severa
    - 37.2% das crianças sofrem de desnutrição crónica em média
    - 55.2% das crianças têm anemia
    """)

with col2:
    st.warning("""
    **⚠️ Desafios**
    
    - Correlação moderada entre FIES e indicadores nutricionais
    - Necessidade de abordagens multissectoriais
    - Disparidades provinciais significativas
    """)

with col3:
    st.success("""
    **🎯 Oportunidades**
    
    - Dados permitem focalização precisa
    - Possibilidade de intervenções integradas
    - Monitoramento contínuo via FIES
    """)

st.markdown("---")

# ============================================================
# TABELA DE DADOS
# ============================================================

st.subheader("📋 Dados Detalhados por Província")

with st.expander("Ver tabela completa com todos os indicadores"):
    st.dataframe(df_analise.sort_values('Indice_Vulnerabilidade', ascending=False), 
                use_container_width=True)

# ============================================================
# EXPORTAÇÃO
# ============================================================

st.markdown("---")
st.subheader("💾 Exportar Resultados")

col1, col2 = st.columns(2)

with col1:
    csv_dados = df_analise.to_csv(index=False, encoding='utf-8-sig', sep=';')
    st.download_button(
        label="📥 Download Dados Completos (CSV)",
        data=csv_dados,
        file_name='correlacao_fies_nutricao_angola_2023.csv',
        mime='text/csv'
    )

with col2:
    # Criar resumo para relatório
    resumo = f"""
RELATÓRIO DE CORRELAÇÃO FIES-NUTRIÇÃO - ANGOLA 2023
====================================================

RESUMO EXECUTIVO:
- Média FIES Total: {df_analise['FIES_Total'].mean():.1f}%
- Média Desnutrição Crónica: {df_analise['Desnutrição Crónica (Nanismo) [%]'].mean():.1f}%
- Correlação FIES-Stunting: {corr_fies_stunting[0]:.3f} (p={corr_fies_stunting[1]:.4f})

PROVÍNCIAS PRIORITÁRIAS:
{hotspots[['Provincia', 'FIES_Total', 'Desnutrição Crónica (Nanismo) [%]', 'Indice_Vulnerabilidade']].to_string(index=False)}

RECOMENDAÇÕES PRINCIPAIS:
1. Intervenções imediatas nas províncias com maior vulnerabilidade
2. Programas integrados de segurança alimentar e nutricional
3. Foco nos primeiros 1000 dias de vida
4. Fortalecimento da agricultura familiar
5. Expansão da protecção social
    """
    st.download_button(
        label="📥 Download Resumo Executivo (TXT)",
        data=resumo,
        file_name='resumo_correlacao_fies_nutricao_2023.txt',
        mime='text/plain'
    )

st.markdown("---")
st.caption("📊 Dashboard desenvolvido para análise da correlação entre insegurança alimentar e desnutrição em Angola - Dados FIES 2023 e Anuário Sanitário 2023-2024")
# ============================================================
# CHAMAR FUNÇÕES DO FOOTER E SIDEBAR (NO FINAL)
# ============================================================

# ... todo o código de análise ...

# Chamar funções
sidebar_info()
footer()