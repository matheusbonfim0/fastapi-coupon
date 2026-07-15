# Coupons API

API FastAPI para emissão de cupons por empresa.

1. Copie `.env.example` para `.env` e troque todas as senhas.
2. Execute `docker compose up -d`.
3. Instale `requirements.txt`.
4. Inicie com `python -m coupons.main`.

Execute testes com `python -m unittest discover -s tests`. A criação de cupom agora
valida duplicidade, persiste todos os campos e usa autenticação HTTP assíncrona com timeout.
