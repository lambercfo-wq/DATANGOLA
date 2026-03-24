# -*- coding: utf-8 -*-
"""
01_Analise_Temporal.py
DATANGOLA - Módulo de Análise Temporal
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
from datetime import datetime

# ⚠️ NÃO USE st.set_page_config() AQUI! (Só no app_datangola.py)

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

📊 Especialista em DATANGOLA & Python

📧 upale.lamber@unic.ac.ao
""")

# TÍTULO DA PÁGINA
st.title("📈 DATANGOLA: Análise Temporal")
st.subheader("Evolução Temporal dos Indicadores de Insegurança Alimentar")
st.markdown("---")

# ... [COLE AQUI O RESTO DO SEU CÓDIGO DE ANÁLISE] ...
# (Todo o código de load_data, gráficos, filtros, etc.)

# ============================================================
# FOOTER - RODAPÉ
# ============================================================

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
