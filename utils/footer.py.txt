# utils/footer.py
"""
Módulo de Footer para o Gêmeo Digital - FIES Angola
Desenvolvido por: Upale Kahilo Lamber
"""

import streamlit as st
from datetime import datetime

def footer():
    """
    Exibe o rodapé em todas as páginas do sistema
    """
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
            <strong>🌍 Gêmeo Digital - Monitoramento FIES Angola</strong> | 
            Desenvolvido por <strong>Upale Kahilo Lamber</strong> 🇦🇴 | 
            © {ano_atual} | 
            Doutoramento em Saúde Pública
        </div>
        <div style='font-size: 11px; opacity: 0.9;'>
            📊 Universidade Internacional do Cuanza (UNIC) | 
            📧 upale.lamber@unic.ac.ao | 
            🔒 Uso Académico e de Pesquisa
        </div>
    </div>
    
    <!-- Padding para não sobrepor conteúdo -->
    <div style='padding-bottom: 100px;'></div>
    """
    
    st.markdown(footer_html, unsafe_allow_html=True)


def sidebar_info():
    """
    Exibe informações sobre o desenvolvedor na sidebar
    """
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
