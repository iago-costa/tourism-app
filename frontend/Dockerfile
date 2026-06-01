FROM node:22-alpine AS builder

WORKDIR /app

COPY package.json package-lock.json* ./
COPY vendor ./vendor
RUN npm ci

COPY . .
RUN npm run build

# ── Production stage ──
FROM node:22-alpine

WORKDIR /app

COPY --from=builder /app/build ./build
COPY --from=builder /app/package.json ./
COPY --from=builder /app/node_modules ./node_modules

EXPOSE 3000
ENV PORT=3000
ENV HOST=0.0.0.0
ENV NODE_ENV=production
ENV ORIGIN=https://tourism.vivdio.com

# SvelteKit adapter-node serves on PORT env var
CMD ["node", "build"]
