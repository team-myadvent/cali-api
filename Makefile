RUNFILE ?= docker-compose-dev.yml

restart:
	@echo "Restarting services using ${RUNFILE}..."
	docker compose -f $(RUNFILE) restart

build:
	@echo "Building and starting services using ${RUNFILE}..."
	docker compose -f $(RUNFILE) up --build -d --remove-orphans

up:
	@echo "Starting services using ${RUNFILE}..."
	docker compose -f $(RUNFILE) up

down:
	@echo "Stopping services using ${RUNFILE}..."
	docker compose -f $(RUNFILE) down

down-v:
	@echo "Stopping and removing volumes for services using ${RUNFILE}..."
	docker compose -f $(RUNFILE) down -v

show-logs:
	@echo "Displaying logs for all services using ${RUNFILE}..."
	docker compose -f $(RUNFILE) logs

logs-api:
	@echo "Displaying logs for the API service using ${RUNFILE}..."
	docker compose -f $(RUNFILE) logs api

makemigrations:
	@echo "Creating migrations for the API service using ${RUNFILE}..."
	docker compose -f $(RUNFILE) run --rm api python src/manage.py makemigrations

migrate:
	@echo "Applying migrations for the API service using ${RUNFILE}..."
	docker compose -f $(RUNFILE) run --rm api python src/manage.py migrate
