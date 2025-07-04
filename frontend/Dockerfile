# --- Build Stage ---
FROM docker.arvancloud.ir/node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
# RUN npm install
ARG VITE_API_BASE_URL
ARG VITE_API_DASHBOARD_URL

ENV VITE_API_BASE_URL=$VITE_API_BASE_URL
ENV VITE_API_DASHBOARD_URL=$VITE_API_DASHBOARD_URL
COPY . .
RUN npm run build


# --- Production Stage ---
FROM docker.arvancloud.ir/nginx:stable-alpine AS production

# Copy built frontend
COPY --from=builder /app/dist /usr/share/nginx/html

# Optional: Replace default nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
