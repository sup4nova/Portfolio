# Portfolio - sup4nova.com

Personal portfolio - a Vue 3 single-page app showcasing my projects.
🔗 Live at **[sup4nova.com](https://sup4nova.com)**

## Stack

| Layer | Tech |
|-------|------|
| Frontend | Vue 3 + TypeScript + Vite + UnoCSS + PrimeVue |
| Backend | FastAPI (Python 3.12) + Uvicorn |
| Server | Nginx |
| Containerization | Docker (multi-stage build) |

## Project structure

```text
Portfolio/
├── front/                    # Vue 3 SPA
│   ├── Dockerfile            # multi-stage build → Nginx
│   ├── nginx.conf            # Nginx config inside the container
│   └── public/.htaccess      # fallback for shared Apache hosting
└── back/                     # FastAPI
    └── Dockerfile
```

## Deployment

### Current - OVH shared hosting (Apache)
The frontend runs on OVH shared hosting. `front/public/.htaccess` handles
SPA routing (`mod_rewrite`) and security headers (`mod_headers`).
Shared hosting can't run Docker or a FastAPI process, so the backend isn't
deployed in production yet.

### Target - VPS with Nginx + Docker
The architecture is designed for a VPS where each service runs in its own
container behind an Nginx reverse proxy:

```text
Internet → Nginx (reverse proxy) → front container (port 8002)
                                  → back container  (port 8000)
```

Both `Dockerfile`s are already set up for this.

## Local development

Most of the work is done locally. Each service runs independently, or via Docker.

### Frontend
```bash
cd front
npm install
npm run dev        # dev server → http://localhost:5173
npm run build      # production build
```

### Backend
```bash
cd back
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### With Docker
```bash
# Frontend
docker build -t portfolio-front ./front
docker run -p 8002:80 portfolio-front

# Backend
docker build -t portfolio-back ./back
docker run -p 8000:8000 -e ALLOWED_ORIGINS=http://localhost:5173 portfolio-back
```
