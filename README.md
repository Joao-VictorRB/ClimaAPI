# Previsão do Tempo com API OpenWeather e SQLite

Este projeto tem como objetivo criar um pipeline completo de previsão do tempo. Ele coleta dados meteorológicos em tempo real através da API OpenWeather, armazena essas informações em um banco de dados SQLite, e oferece uma interface interativa para consulta e visualização dos dados.

## Objetivo

O objetivo do projeto é construir uma aplicação que:
- Consome dados da API OpenWeather.
- Armazena os dados em um banco de dados SQLite.
- Oferece uma interface para consultar e visualizar as previsões do tempo de diferentes cidades.
- Permite visualização dos dados por meio de um dashboard interativo (Streamlit).

## Tecnologias Usadas

- **Python 3.x**: Linguagem principal do projeto.
- **API OpenWeather**: Para obtenção dos dados de previsão do tempo.
- **SQLite**: Banco de dados para armazenamento dos dados de previsão.
- **Streamlit**: Para a criação de um dashboard interativo e visualização dos dados.

## Funcionalidades

- **Coleta de Dados Meteorológicos**: A aplicação coleta dados como temperatura, umidade, velocidade do vento e condições climáticas a partir da API OpenWeather.
- **Armazenamento em Banco de Dados**: Os dados coletados são armazenados em um banco de dados SQLite para facilitar consultas futuras.
- **Visualização Interativa**: Os dados podem ser visualizados de forma simples e intuitiva por meio de um **dashboard Streamlit**, onde o usuário pode selecionar cidades e visualizar as previsões do tempo atuais e futuras.

### Exemplos de Funcionalidades:

- Visualizar a previsão do tempo para a cidade escolhida.
- Exibir temperatura, umidade, condições climáticas e previsão para os próximos dias.
- Armazenamento local dos dados para consultas rápidas sem necessidade de reconsumo da API.

## Estrutura do Projeto

A estrutura do projeto é dividida em diferentes módulos para garantir organização e modularidade.

## Projeto no Ar
https://climaapi-j6rgfs8d7zncv6j6apyqbz.streamlit.app/
