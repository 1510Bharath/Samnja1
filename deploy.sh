#!/bin/bash
# =============================================================================
# deploy.sh — One-command deployment on AWS EC2 / Google Cloud / Azure VM
# Run this ONCE on a fresh Ubuntu 22.04 server:
#   chmod +x deploy.sh && ./deploy.sh
# =============================================================================

echo "=== Samjna Web Deployment ==="

# 1. Install Docker
echo "Installing Docker..."
sudo apt-get update -q
sudo apt-get install -y docker.io docker-compose nginx certbot python3-certbot-nginx

# 2. Start Docker
sudo systemctl enable docker
sudo systemctl start docker

# 3. Add current user to docker group
sudo usermod -aG docker $USER

# 4. Build and start the app
echo "Building container..."
sudo docker-compose up -d --build

echo ""
echo "=== Done! ==="
echo "App running at: http://$(curl -s ifconfig.me)"
echo ""
echo "Next steps for HTTPS:"
echo "  1. Point your domain DNS to: $(curl -s ifconfig.me)"
echo "  2. Edit nginx.conf — replace 'your-domain.com' with your domain"
echo "  3. sudo cp nginx.conf /etc/nginx/sites-available/samjna"
echo "  4. sudo ln -s /etc/nginx/sites-available/samjna /etc/nginx/sites-enabled/"
echo "  5. sudo certbot --nginx -d your-domain.com"
echo "  6. sudo systemctl reload nginx"
echo ""
echo "Recordings are saved to: $(pwd)/recordings/"
