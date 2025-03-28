new:
	docker compose up --build -d

db:
	docker exec -it mongo /bin/bash

be:
	docker exec -it backend /bin/bash

logs:
	docker logs -f --tail 50 backend