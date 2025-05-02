import streamlit as st
from ETL.coleta import pegar_dados_api
from ETL.coleta import mostrar_previsao_futura
from database.conexao import salvar_previsao

# Função principal do Streamlit
def main():
   st.set_page_config(layout="centered", page_title="Previsão do Tempo", page_icon=":sunny:")

   st.markdown("<h1 style='text-align: center; color: #3366cc;'>🌤️ Dashboard do Clima</h1>", unsafe_allow_html=True)
   st.markdown("<h4 style='text-align: center; color: gray;'>Veja a previsão do tempo de qualquer capital do mundo</h4>", unsafe_allow_html=True)

   cidade = st.text_input(label='',label_visibility="collapsed",placeholder="Ex: São Paulo",key="cidade_input")
   
   if cidade:
        clima_atual = pegar_dados_api(cidade)

        if clima_atual:
            st.write(f"🌆 Cidade: {clima_atual['cidade']}")
            st.write(f"🌡️ Temperatura: {clima_atual['temperatura']}°C")
            st.write(f"💨 Sensação Térmica: {clima_atual['sensacao_termica']}°C")
            st.write(f"💧 Umidade: {clima_atual['umidade']}%")
            st.write(f"☁️ Clima: {clima_atual['clima']}")
            st.write(f"💬 Descrição: {clima_atual['descricao']}")
            st.write(f"💨 Vento: {clima_atual['vento']} m/s")

        st.markdown("<h4 style='text-align: center; margin-top: 3rem; color: gray;'>Confira as previsões do tempo para os próximos dias (1 - 5)</h4>", unsafe_allow_html=True)

        dias = st.number_input(label='',label_visibility='collapsed', min_value=1, max_value=5, value=1)

        previsao = mostrar_previsao_futura(cidade, dias)

        if previsao:

         if isinstance(previsao, dict):  # Quando é uma média diária
            st.write(f"\n📍 Previsão média para {cidade.title()} no {dias}º dia:")
            st.write(f"🌡️ Temperatura média: {previsao['temperatura_media']:.1f}°C")
            st.write(f"💧 Umidade média: {previsao['umidade_media']:.0f}%")
            st.write(f"💬 Clima predominante: {previsao['descricao_mais_comum']}")
            
   st.markdown("<h4 style='text-align: center; margin-top: 3rem; color: gray;'>💾 Adicione uma nova cidade/capital ao banco de dados </h4>", unsafe_allow_html=True)
   cidade_database = st.text_input(label='',label_visibility='collapsed',placeholder="Ex: São Paulo",key="cidade_database").title()   

   if cidade_database:
      
      previsao_database = pegar_dados_api(cidade_database)
      resultado_previsao_database = salvar_previsao(previsao_database)
    
      if resultado_previsao_database:
        st.write(f"🌆 Cidade: {resultado_previsao_database['cidade']}")
        st.write(f"🌡️ Temperatura: {resultado_previsao_database['temperatura']}°C")
        st.write(f"💨 Sensação Térmica: {resultado_previsao_database['sensacao_termica']}°C")
        st.write(f"💧 Umidade: {resultado_previsao_database['umidade']}%")
        st.write(f"☁️ Clima: {resultado_previsao_database['clima']}")
        st.write(f"💬 Descrição: {resultado_previsao_database['descricao']}")
        st.write(f"💨 Vento: {resultado_previsao_database['vento']} m/s")
        st.write("")
        st.write(f"✅ A Previsão foi salva com sucesso no banco de dados!")

   st.markdown("---")
   st.markdown(
    """
    <p style='text-align: center;'>
        Feito por Joao-VictorRB<br>
        <a href='https://github.com/Joao-VictorRB' target='_blank'>🐱 GitHub</a> | 
        <a href='https://www.linkedin.com/in/jo%C3%A3ovictorbatista/' target='_blank'>💼 LinkedIn</a>
    </p>
    """,
    unsafe_allow_html=True
)
if __name__ == "__main__":
    main()
