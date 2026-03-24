# app_datangola.py
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="DATANGOLA",
    page_icon="🇦🇴",
    layout="wide"
)

st.title("🇦🇴 DATANGOLA")
st.subheader("Plataforma Integrada de Análise e Relatório para Desenvolvimento")

st.markdown("""
---
### 🎯 Bem-vindo à DATANGOLA

Esta plataforma permite:
- 📊 Análise de dados de desenvolvimento
- 📋 Geração de relatórios
- 📈 Monitoramento e avaliação

### 🚀 Módulos Disponíveis

Selecione um módulo no menu lateral:
- **📋 Sobre** - Informações sobre a plataforma
- **📈 Análise Temporal** - Evolução temporal
- **📊 Análise Estatística** - Estatísticas
- **🔗 Correlação FIES-Nutrição** - Análise de correlação
""")

# Footer
ano_atual = datetime.now().year
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; color: #666;'>
<strong>🇦🇴 DATANGOLA</strong> | © {ano_atual} | Upale Kahilo Lamber 🇦🇴
</div>
""", unsafe_allow_html=True)
# Após o "Bem-vindo à DATANGOLA", adicionar:

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Sectores Abrangidos", "6")
    st.info("Saúde, Agricultura, Educação, Humanitário, M&E, Planeamento")

with col2:
    st.metric("🏛️ Instituições", "6+")
    st.success("INE, MINSA, MINAGRI, MINED, FAO, UNICEF")

with col3:
    st.metric("👥 Utilizadores", "Em crescimento")
    st.warning("Académicos, Gestores, Pesquisadores")

# Destaques
st.markdown("---")
st.subheader("🌟 Porquê Usar a DATANGOLA?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **✅ Vantagens:**
    - Geração automática de relatórios
    - Análise estatística avançada
    - Visualização interactiva
    - Exportação para múltiplos formatos
    - Dados actualizados
    """)

with col2:
    st.markdown("""
    **🎯 Aplicações:**
    - Relatórios programáticos
    - Planos de acção
    - Monitoria & Avaliação
    - Pesquisas científicas
    - Estudos epidemiológicos
    """)
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