# API_Externa

precisa do docker compose para executar 

services:
  frontend:
    build: ./frontend_chatJarvis
    ports:
      - "8080:80"
    depends_on:
      - api_principal

  api_principal:
    build: ./api_principal
    ports:
      - "8000:3000"
    environment:
      - API_EXTERNA_URL=http://api_externa:3000/chat
    depends_on:
      - api_externa

  api_externa:
    build: ./api_externa
    ports:
      - "9000:3000"
    env_file:
      - ./api_externa/.env
