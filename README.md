# 🤖 AWS Study Copilot

Asistente conversacional inteligente especializado en conceptos de AWS, RAG y LLMs, construido con Streamlit y Amazon Bedrock.

## Descripción

Esta aplicación permite a los usuarios interactuar con un asistente experto en temas como:

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Amazon Bedrock
- AI Practitioner
- Cloud concepts

El asistente responde de manera pedagógica y estructurada, ayudando a estudiantes a prepararse para certificaciones AWS.

---

## Tecnologías utilizadas

- Python
- Streamlit
- Amazon Bedrock (Claude)
- Boto3
- Docker

---

## Configuración

Este proyecto utiliza variables de entorno. Crear un archivo `.env` basado en `.env.example`:

```env
AWS_PROFILE=blend-profile
AWS_REGION=us-east-1
MODEL_ID=anthropic.claude-3-haiku-20240307-v1:0
