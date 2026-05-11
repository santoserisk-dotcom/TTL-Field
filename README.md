# TTL Field — Plataforma de Inteligência Operacional para ISP

Plataforma corporativa de rastreamento inteligente para equipes técnicas externas, com foco em observabilidade operacional, telemetria e analytics, **sem duplicar o workflow de OS já operado no Auvo**.

## 1) Objetivo do Projeto

A solução foi desenhada para:

- monitorar deslocamento de técnicos em tempo real;
- gerar histórico, playback e métricas de campo;
- prover geofences e alertas operacionais;
- suportar auditoria de deslocamento e produtividade;
- preparar integração futura com API/Webhooks do Auvo.

## 2) Arquitetura

```text
[App Flutter Técnico] -> [FastAPI Backend] -> [Traccar Engine/API] -> [PostgreSQL]
                                       \-> [WebSocket] -> [Dashboard React]
```

- **Traccar** é usado apenas como engine GPS/provider de tracking.
- Toda inteligência operacional fica no backend + dashboard próprios.

## 3) Estrutura de diretórios

```text
backend/    # API FastAPI + regras de negócio + integrações
frontend/   # Dashboard React + TypeScript + Tailwind
mobile/     # App Flutter de telemetria silenciosa
infra/      # Docker Compose e utilitários de ambiente
docs/       # Guias técnicos, onboarding e troubleshooting
docs_architecture.md
```

## 4) Pré-requisitos

| Componente | Versão recomendada |
|---|---|
| Git | 2.40+ |
| Docker Engine | 24+ |
| Docker Compose plugin | 2.20+ |
| Python | 3.12+ |
| Node.js | 20 LTS+ |
| npm | 10+ |
| Flutter SDK | 3.24+ |
| Dart | 3.4+ |
| PostgreSQL (local opcional) | 16+ |

> Se usar apenas Docker Compose, PostgreSQL local não é obrigatório.

## 5) Quick Start (local)

### 5.1 Clonar e preparar

```bash
git clone <repo-url>
cd TTL-Field
cp backend/.env.example backend/.env
```

### 5.2 Subir stack com Docker

```bash
docker compose -f infra/docker-compose.yml up --build
```

Serviços esperados:
- Backend: `http://localhost:8000`
- Swagger/OpenAPI: `http://localhost:8000/docs`
- Frontend: `http://localhost:5173`
- Traccar: `http://localhost:8082`
- Postgres: `localhost:5432`

## 6) Desenvolvimento por camada

Documentação completa no guia técnico:

- **Guia inicial de execução e desenvolvimento**: `docs/development-guide.md`
- **Arquitetura base e roadmap**: `docs_architecture.md`

## 7) Endpoints iniciais disponíveis

- `GET /health`
- `POST /api/v1/tracking/positions`
- `WS /api/v1/ws/operations`

## 8) Variáveis de ambiente (backend)

Arquivo de referência: `backend/.env.example`

- `APP_NAME`
- `ENVIRONMENT`
- `DATABASE_URL`
- `JWT_SECRET`
- `JWT_ALGORITHM`
- `TRACCAR_BASE_URL`

## 9) Qualidade de engenharia

Padrões adotados nessa fase:
- tipagem explícita no backend e frontend;
- base para arquitetura modular;
- estrutura preparada para RBAC/JWT, migrations, geofence e alertas;
- monorepo organizado para evolução contínua.

## 10) Próximos passos recomendados

1. Implementar autenticação JWT + refresh + RBAC completo.
2. Criar modelos SQLAlchemy e migrations Alembic.
3. Integrar ingestão real com Traccar API.
4. Implementar serviços de geofence/alerta/playback.
5. Adicionar testes automatizados (backend/frontend/mobile).
6. Preparar CI/CD com GitHub Actions.
