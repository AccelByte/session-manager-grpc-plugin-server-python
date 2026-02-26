# session-manager-grpc-plugin-server-python

An Extend Override app for the **session manager** written in Python. AGS calls this gRPC server with lifecycle hooks whenever game sessions or party sessions are created, updated, or deleted.

This is a template project — clone it, replace the sample logic in the service implementation, and deploy.

## Build & Test

```bash
make build                           # Build the project
docker compose up --build            # Run locally with Docker
make proto                           # Regenerate proto code
```

Linting: `pylint` (config in `.pylintrc`).

## Architecture

AGS invokes this app's gRPC methods instead of its default logic:

```
Game Client → AGS → [gRPC] → This App → Response → AGS
```

The sample implementation handles six lifecycle hooks (OnSessionCreated, OnSessionUpdated, OnSessionDeleted, OnPartyCreated, OnPartyUpdated, OnPartyDeleted) and demonstrates injecting custom attributes into session data on creation events.

### Key Files

| Path | Purpose |
|---|---|
| `src/accelbyte_grpc_plugin/app.py` | Entry point — starts gRPC server, wires interceptors and observability |
| `src/app/services/session_manager.py` | **Service implementation** — your custom logic goes here |
| `proto/session-manager.proto` | gRPC service definition (AccelByte-provided, do not modify) |
| `src/accelbyte_grpc_plugin/interceptors/` | Auth interceptor, tracing, logging utilities |
| `docker-compose.yaml` | Local development setup |
| `.env.template` | Environment variable template |

## Rules

See `.agents/rules/` for coding conventions, commit standards, and proto file policies.

## Environment

Copy `.env.template` to `.env` and fill in your credentials.

| Variable | Description |
|---|---|
| `AB_BASE_URL` | AccelByte base URL (e.g. `https://test.accelbyte.io`) |
| `AB_NAMESPACE` | Target namespace |
| `AB_CLIENT_ID` | OAuth client ID |
| `AB_CLIENT_SECRET` | OAuth client secret |
| `PLUGIN_GRPC_SERVER_AUTH_ENABLED` | Enable gRPC auth (`true` by default) |
| `ENABLE_HEALTH_CHECK` | Enable gRPC health check endpoint |
| `ENABLE_PROMETHEUS` | Enable Prometheus metrics endpoint |
| `ENABLE_REFLECTION` | Enable gRPC reflection |
| `ENABLE_ZIPKIN` | Enable Zipkin tracing |

## Dependencies

- [AccelByte Python SDK](https://github.com/AccelByte/accelbyte-python-sdk) (`accelbyte-py-sdk`) — AGS platform SDK and gRPC plugin utilities
