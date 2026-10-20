import streamlit as st

import chunker
import config
import embedder
import generator
import loader
import pipeline
import vectorstore

from retriever import retrieve,format_context
from generator import generate_answer





st.set_page_config(page_title="Chat App", page_icon="💬", layout="centered")

st.title("💬 Chat App")

# Inicializa o histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de entrada de texto tipo chat
if prompt := st.chat_input("Digite sua mensagem..."):
    # Exibe a mensagem do usuário
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Adiciona a mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Resposta fictícia do assistente
    response = f"Você disse: {prompt}"
    
    
    ###############################################################################
    # chamada da lib de RAG
    resultados = retrieve(prompt, 5)
    
    final = generate_answer(prompt, resultados)
    with st.chat_message("assistant"):
        st.markdown(final)
    
    # Adiciona a resposta do assistente ao histórico
    st.session_state.messages.append({"role": "assistant", "content": response})