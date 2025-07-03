# --- Build Stage ---
FROM docker.arvancloud.ir/node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
# RUN npm install

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
