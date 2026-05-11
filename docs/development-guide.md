# Guia Inicial de Execução e Desenvolvimento — TTL Field

Este guia garante onboarding completo para qualquer desenvolvedor: clonar, configurar, executar, validar e evoluir a plataforma sem conhecimento implícito.

## 1. Pré-requisitos detalhados

### 1.1 Ferramentas obrigatórias
- Git 2.40+
- Docker Engine 24+
- Docker Compose 2.20+
- Python 3.12+
- Node.js 20 LTS+
- npm 10+
- Flutter 3.24+
- Android Studio (SDK + emulator)
- JDK 17 (para toolchain Android)

### 1.2 SDKs e runtimes
- Dart 3.4+ (via Flutter)
- OpenSSL (geração de segredos/certificados em ambientes avançados)

### 1.3 Serviços externos
- Traccar (subido via Docker Compose neste projeto)
- PostgreSQL 16 (container no compose; local opcional)

---

## 2. Configuração do ambiente

### 2.1 Clonar o repositório
```bash
git clone <repo-url>
cd TTL-Field
```

### 2.2 Estrutura de diretórios (resumo)
- `backend/`: API FastAPI e lógica operacional
- `frontend/`: dashboard web
- `mobile/`: app técnico (telemetria)
- `infra/`: compose e infraestrutura local
- `docs/`: guias e troubleshooting

### 2.3 Variáveis de ambiente
```bash
cp backend/.env.example backend/.env
```

Ajuste obrigatório mínimo:
- `JWT_SECRET`: usar valor seguro em ambiente real
- `DATABASE_URL`: ajustar se banco não estiver no compose
- `TRACCAR_BASE_URL`: manter `http://traccar:8082` no Docker

### 2.4 Configuração do banco
- Via Docker: já provisionado em `infra/docker-compose.yml`
- Fora do Docker: criar banco `ttl_field` em PostgreSQL 16+

### 2.5 Configuração do Traccar
- Via Docker: sobe automaticamente como serviço `traccar`
- Porta padrão web/API: `8082`
- Porta ingestão GPS: `5055`

---

## 3. Execução local por serviço

## 3.1 Backend (FastAPI)

### Com Docker (recomendado)
```bash
docker compose -f infra/docker-compose.yml up backend db traccar --build
```

### Sem Docker
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
uvicorn app.main:app --reload --port 8000
```

### Migrations (planejado)
Quando Alembic estiver configurado:
```bash
alembic upgrade head
```

### Testes locais backend
```bash
python -m compileall app
# Futuro: pytest
```

## 3.2 Frontend (React + TypeScript)

### Com Docker
```bash
docker compose -f infra/docker-compose.yml up frontend --build
```

### Sem Docker
```bash
cd frontend
npm install
npm run dev
```

### Configuração de API base URL/WebSocket
Criar `.env.local` no frontend (fase seguinte):
```bash
VITE_API_BASE_URL=http://localhost:8000
VITE_WS_BASE_URL=ws://localhost:8000
```

## 3.3 Mobile (Flutter)

### Setup básico
```bash
cd mobile
flutter pub get
flutter doctor
```

### Rodar em emulator Android
```bash
flutter emulators
flutter emulators --launch <emulator_id>
flutter run
```

### Build debug
```bash
flutter build apk --debug
```

### Permissões Android (a implementar na fase de tracking)
- localização em primeiro plano e background;
- execução resiliente em background;
- tolerância a Doze/battery optimization.

### Apontar app para backend local
- Em emulador Android padrão, usar host da máquina (`10.0.2.2`) quando não estiver em Docker interno.

---

## 4. Banco de dados

### 4.1 Criação e persistência
- Compose já cria DB com volume `pg_data`.
- Persistência em reinícios é garantida pelo volume Docker.

### 4.2 Seeds iniciais (planejado)
Recomendação:
- usuário admin inicial;
- perfis RBAC básicos;
- técnicos/dispositivos de teste.

### 4.3 Migrations
- padrão será Alembic + SQLAlchemy 2.0 async.

---

## 5. Docker e troubleshooting

### Subir tudo
```bash
docker compose -f infra/docker-compose.yml up --build
```

### Subir em background
```bash
docker compose -f infra/docker-compose.yml up -d
```

### Rebuild completo
```bash
docker compose -f infra/docker-compose.yml build --no-cache
```

### Logs
```bash
docker compose -f infra/docker-compose.yml logs -f backend
docker compose -f infra/docker-compose.yml logs -f frontend
docker compose -f infra/docker-compose.yml logs -f traccar
```

### Derrubar ambiente
```bash
docker compose -f infra/docker-compose.yml down
```

### Derrubar removendo volumes (reset total)
```bash
docker compose -f infra/docker-compose.yml down -v
```

Problemas comuns:
- Porta ocupada (`8000`, `5173`, `5432`, `8082`): alterar mapeamentos.
- Falha de conexão backend↔db: validar `DATABASE_URL` e serviço `db` ativo.
- Frontend sem API: conferir URL base e CORS no backend.

---

## 6. Ambiente de teste funcional

### 6.1 Simular dispositivos
- usar app Flutter em emulador e enviar posições para `POST /api/v1/tracking/positions`.

### 6.2 Testar tracking
- enviar payloads variando `latitude/longitude/speed_kmh` para validar ingestão.

### 6.3 Testar WebSocket
- conectar no canal `ws://localhost:8000/api/v1/ws/operations`.

### 6.4 Validar playback/geofence/alertas
- nesta fase estão planejados; recomendação é usar fixtures com rotas sintéticas ao implementar.

### 6.5 Validar sincronização
- cenário alvo: fila offline no mobile + reenvio quando conexão voltar.

---

## 7. Estrutura do projeto e responsabilidades

- `backend/app/api`: endpoints HTTP/WS
- `backend/app/core`: configuração e segurança
- `backend/app/models`: entidades/domínio
- `backend/app/services`: regras operacionais
- `backend/app/repositories`: acesso a dados
- `frontend/src/types`: DTOs/interfaces
- `frontend/src/features`: módulos de produto
- `mobile/lib/features`: módulos por contexto (auth/tracking/heartbeat)

Fluxo macro:
1. app captura telemetria;
2. backend valida e processa;
3. persiste no PostgreSQL e integra com Traccar;
4. emite atualização por websocket;
5. dashboard renderiza estado operacional.

---

## 8. Fluxo de desenvolvimento

### 8.1 Branches
- `main`: produção
- `develop`: integração
- `feature/*`: novas funcionalidades
- `fix/*`: correções

### 8.2 Commits
- padrão: Conventional Commits
- exemplos: `feat:`, `fix:`, `chore:`, `refactor:`

### 8.3 Lint, formatação e testes
Recomendação de baseline:
- Backend: Ruff + Pytest
- Frontend: ESLint + Prettier + Vitest
- Mobile: `flutter analyze` + testes widget/unit

### 8.4 CI/CD
Pipeline mínimo recomendado (GitHub Actions):
1. lint
2. testes
3. build backend/frontend/mobile
4. artefatos e release/deploy

---

## 9. Deploy

### 9.1 Frontend
Compatível com:
- Vercel
- Netlify
- Cloudflare Pages

### 9.2 Backend
Compatível com:
- Docker em VPS
- Oracle Cloud
- AWS
- Hetzner

### 9.3 Mobile
- distribuição interna (QA)
- Play Store/TestFlight (futuro)

### 9.4 Domínio e HTTPS
- usar proxy reverso (Nginx/Traefik)
- TLS com Let's Encrypt
- CORS e headers de segurança no backend

---

## 10. Endpoints e estrutura inicial de API

### HTTP
- `GET /health`
- `POST /api/v1/tracking/positions`

### WebSocket
- `WS /api/v1/ws/operations`

### OpenAPI
- `http://localhost:8000/docs`

---

## 11. Onboarding de novos desenvolvedores

Checklist rápido:
1. instalar pré-requisitos;
2. clonar repo e criar `.env`;
3. subir Docker Compose;
4. validar `health` e frontend;
5. executar checks locais;
6. criar branch `feature/*`;
7. abrir PR com evidências de teste.

---

## 12. Troubleshooting rápido

- **Backend não sobe:** revisar logs e `DATABASE_URL`.
- **Frontend em branco:** conferir `npm install` e porta `5173`.
- **Traccar inacessível:** validar container e porta `8082`.
- **Mobile sem conexão:** ajustar host para `10.0.2.2` no emulador Android.
