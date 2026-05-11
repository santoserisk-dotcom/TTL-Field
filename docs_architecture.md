# Arquitetura Base - TTL Field

## Contexto
Plataforma complementar ao Auvo para observabilidade operacional, sem duplicar workflow de OS.

## Serviços
- **App Flutter (técnico):** coleta telemetria silenciosa, tracking adaptativo e heartbeat.
- **Backend FastAPI:** autenticação JWT, ingestão de posições, eventos, alertas, geofence, WebSocket.
- **Traccar:** engine GPS e provider de tracking.
- **PostgreSQL:** persistência transacional, histórico e métricas.
- **Dashboard React:** NOC operacional, mapa em tempo real e analytics.

## Modelo de dados inicial
- users
- roles
- technicians
- devices
- positions
- routes
- geofences
- alerts
- events
- sessions
- metrics

## Retenção
- Posições detalhadas: 90 dias.
- Eventos operacionais: 365 dias.
- Métricas agregadas: permanente.

## Fases
1. Fundação de autenticação + telemetria + mapa realtime.
2. Geofence, playback e alertas operacionais.
3. Analytics executivos e integração Auvo (API/webhooks).
