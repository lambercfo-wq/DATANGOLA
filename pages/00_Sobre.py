# -*- coding: utf-8 -*-
"""
00_Sobre.py - Sobre a DATANGOLA
Plataforma Integrada de Análise e Relatório para Desenvolvimento
"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Sobre - DATANGOLA", layout="wide")

# SIDEBAR
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

# CONTEÚDO PRINCIPAL
st.title("ℹ️ Sobre a DATANGOLA")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### 🎯 Descrição da Plataforma
    
    **DATANGOLA: Plataforma Integrada de Análise e Relatório para Desenvolvimento**
    
    Esta plataforma foi desenvolvida como parte de pesquisa de doutoramento em Saúde Pública,
    com o objetivo de fornecer uma solução integrada para análise de dados e geração de 
    relatórios em múltiplos sectores de desenvolvimento em Angola.
    
    ### 📊 Módulos e Funcionalidades
    
    | Módulo | Funcionalidade | Sectores |
    |--------|---------------|----------|
    | **Saúde Pública** | FIES, Nutrição, Epidemiologia | MINSA, INE |
    | **Agricultura** | Monitoramento agrícola, Cadeias de valor | MINAGRI, FAO |
    | **Educação** | Matrículas, Infraestruturas, Resultados | MINED |
    | **Humanitário** | Necessidades, Resposta, Clusters | OCHA, UNICEF |
    | **M&E** | LogFrame, Indicadores, Doadores | Todos |
    | **Planeamento** | Planos de Acção, Roadmaps | Todos |
    
    ### 🔧 Tecnologias Utilizadas
    
    - **Backend:** Python 3.13, Pandas, NumPy, SciPy
    - **Frontend:** Streamlit, Plotly, Matplotlib
    - **Dados:** CSV, Excel, APIs (INE, MINSA, FAO)
    - **Exportação:** PDF, Word, Excel, PowerPoint
    
    ### 📚 Referências e Fontes de Dados
    
    1. **INE Angola** - Instituto Nacional de Estatística
    2. **MINSA** - Ministério da Saúde
    3. **FAO/WFP** - Organização das Nações Unidas
    4. **UNICEF** - Fundo das Nações Unidas para a Infância
    5. **OCHA** - Escritório de Coordenação de Assuntos Humanitários
    """)

with col2:
    st.image("https://img.icons8.com/color/96/000000/data-configuration.png", width=120)
    
    st.markdown(f"""
    ---
    ### 👨‍💻 Desenvolvedor
    
    **Upale Kahilo Lamber** 🇦🇴
    
    **Instituição:** 
    Universidade Internacional do Cuanza (UNIC)
    
    **Função:**
    Professor-Investigador
    
    **Especialização:**
    - Saúde Pública (Epidemiologia)
    - Agroindústria
    - Ciência de Dados
    - Sistemas de Informação
    
    ---
    
    ### 🏆 Reconhecimentos
    
    - 🥇 Vencedor Hackathon AgriTech Timbuktoo (2026)
    - 📄 Publicação em MLS Health and Nutrition Research (2024)
    
    ---
    
    **Versão:** 1.0.0
    
    **Última atualização:**
    {datetime.now().strftime("%B %Y")}
    
    ---
    
    ### 🔒 Direitos Autorais
    
    © {datetime.now().year} Upale Kahilo Lamber
    
    Todos os direitos reservados.
    
    Uso permitido apenas para fins 
    académicos e de pesquisa.
    """)

# DOWNLOADS
st.markdown("---")
st.subheader("📥 Documentação para Download")

col1, col2, col3 = st.columns(3)

with col1:
    cv_resumo = """
CURRICULUM VITAE RESUMO
========================

UPALE KAHILO LAMBER 🇦🇴
Desenvolvedor da DATANGOLA | Especialista em Análise de Dados

CONTACTO
--------
Email: upale.lamber@unic.ac.ao
Instituição: Universidade Internacional do Cuanza (UNIC)

SOBRE A DATANGOLA
-----------------
Plataforma Integrada de Análise e Relatório para Desenvolvimento

FUNCIONALIDADES:
- Monitoramento de indicadores de desenvolvimento
- Geração automática de relatórios
- Análise estatística avançada
- Visualização de dados interactiva
- Exportação para múltiplos formatos

SECTORES ABRANGIDOS:
- Saúde Pública e Nutrição
- Agricultura e Segurança Alimentar
- Educação
- Ajuda Humanitária
- Programas Governamentais
- Monitoria & Avaliação
- Pesquisa Científica
- Planeamento Estratégico

TECNOLOGIAS:
- Python, Streamlit, Pandas, NumPy
- Power BI, SQL, SPSS
- KoboToolbox, ODK

EXPERIÊNCIA: +13 anos em desenvolvimento rural e sustentável em Angola
"""
    st.download_button(
        label="📄 Download CV Resumo (TXT)",
        data=cv_resumo,
        file_name="CV_Upale_Kahilo_Lamber_DATANGOLA.txt",
        mime="text/plain"
    )

with col2:
    bibliografia = """
REFERÊNCIAS BIBLIOGRÁFICAS - DATANGOLA
========================================

FONTES OFICIAIS DE DADOS:

1. INE Angola. (2026). Relatório sobre Escala de Experiência de Insegurança Alimentar 
   (FIES) 2020-2023. Luanda: Instituto Nacional de Estatística.

2. INE, MINSA, MINPLAN e ICF. (2025). Inquérito de Indicadores Múltiplos e de Saúde 
   em Angola, 2023–2024. Luanda: INE, MINSA, MINPLAN e ICF.

3. Ministério da Saúde de Angola. (2024). Anuário Sanitário 2023-2024. Luanda.

REFERÊNCIAS TÉCNICAS:

4. FAO. (2023). Experience-based Food Insecurity Scale (FIES). Rome: FAO.

5. WHO. (2023). Nutrition Indicators for Health Monitoring. Geneva: World Health 
   Organization.

6. Smith, L. C., & Haddad, L. (2015). Reducing Child Undernutrition: Past Drivers 
   and Priorities for the Post-MDG Era. World Development, 68, 180-204.

DESENVOLVEDOR:

Upale Kahilo Lamber (2026). DATANGOLA: Plataforma Integrada de Análise e Relatório 
para Desenvolvimento. Universidade Internacional do Cuanza (UNIC).

© 2026 Upale Kahilo Lamber - Todos os direitos reservados
"""
    st.download_button(
        label="📚 Download Bibliografia (TXT)",
        data=bibliografia,
        file_name="Bibliografia_DATANGOLA.txt",
        mime="text/plain"
    )

with col3:
    termos_uso = """
TERMOS DE USO - DATANGOLA
==========================

1. PROPRIEDADE INTELECTUAL
--------------------------
Esta plataforma é propriedade intelectual de Upale Kahilo Lamber, desenvolvida no 
âmbito do programa de doutoramento em Saúde Pública da Universidade Internacional 
do Cuanza (UNIC).

2. FINALIDADE
-------------
Plataforma destinada exclusivamente para:
- Pesquisa académica
- Monitoramento epidemiológico
- Apoio à tomada de decisão em saúde pública
- Ensino e capacitação profissional

3. RESTRIÇÕES
-------------
É proibido:
- Uso comercial sem autorização escrita
- Reprodução total ou parcial sem citação adequada
- Modificação do código-fonte sem permissão
- Distribuição de dados brutos a terceiros

4. CITAÇÃO RECOMENDADA
----------------------
Ao utilizar dados ou análises desta plataforma, cite:

"Lamber, U.K. (2026). DATANGOLA: Plataforma Integrada de Análise e Relatório 
para Desenvolvimento. Universidade Internacional do Cuanza (UNIC)."

5. FONTES DE DADOS
------------------
Os dados apresentados são de responsabilidade das instituições oficiais:
- Instituto Nacional de Estatística (INE) Angola
- Ministério da Saúde (MINSA)
- FAO - Organização das Nações Unidas para Alimentação e Agricultura

6. CONTACTO PARA AUTORIZAÇÃO
----------------------------
Email: upale.lamber@unic.ac.ao
Instituição: Universidade Internacional do Cuanza (UNIC)

7. VIGÊNCIA
-----------
Estes termos entram em vigor em Janeiro de 2026 e são válidos até nova comunicação.

© 2026 Upale Kahilo Lamber - Todos os direitos reservados
"""
    st.download_button(
        label="📋 Download Termos de Uso (TXT)",
        data=termos_uso,
        file_name="Termos_de_Uso_DATANGOLA.txt",
        mime="text/plain"
    )

# RODAPÉ DE CITAÇÃO
st.markdown("---")
st.info("""
💡 **Como Citar Esta Plataforma:**

Lamber, U.K. (2026). *DATANGOLA: Plataforma Integrada de Análise e Relatório para Desenvolvimento*. 
Universidade Internacional do Cuanza (UNIC). Disponível em: http://localhost:8501

**Para citações académicas, use o formato APA 7ª edição.**
""")

st.caption("""
🇦🇴 Desenvolvido em Angola por Angolanos para Angola | 
© 2026 Upale Kahilo Lamber | Universidade Internacional do Cuanza (UNIC)
""")

# FOOTER
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