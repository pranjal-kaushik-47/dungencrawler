# dungencrawler

## Project Description

Dungencrawler is a dungeon crawler game built with a Vue 3 frontend and a FastAPI backend. The game features procedural map generation, item spawning, and various player mechanics.

## Project Structure

- **frontend**: Contains the Vue 3 frontend code.
- **server**: Contains the FastAPI backend code.
- **docker-compose.yml**: Docker Compose configuration for running the frontend and backend services.
- **Dockerfile**: Dockerfile for building the frontend and backend images.

## Setup Instructions

### Prerequisites

- Node.js (version 22 or higher)
- Python (version 3.12 or higher)
- Docker

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/dungencrawler.git
    cd dungencrawler
    ```

2. Install frontend dependencies:
    ```sh
    cd frontend
    npm install
    ```

3. Install backend dependencies:
    ```sh
    cd ../server
    pip install -r requirements.txt
    ```

### Running the Application

#### Using Docker Compose

1. Build and start the services:
    ```sh
    docker-compose up --build
    ```

2. Access the frontend at `http://localhost:5173` and the backend at `http://localhost:8000`.

#### Running Locally

1. Start the frontend:
    ```sh
    cd frontend
    npm run dev
    ```

2. Start the backend:
    ```sh
    cd ../server
    uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
    ```

3. Access the frontend at `http://localhost:5173` and the backend at `http://localhost:8000`.

## Usage

### Frontend

- The frontend is built with Vue 3 and Vite.
- Main entry point: `frontend/src/main.ts`
- Main component: `frontend/src/App.vue`

### Backend

- The backend is built with FastAPI.
- Main entry point: `server/src/main.py`
- API endpoints:
  - `GET /`: Welcome message
  - `GET /ping`: Ping endpoint
  - `GET /items/{item_id}`: Get item details
  - `GET /users/{user_id}`: Get user details

## Development

### Recommended IDE Setup

- [VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

### Type Support for `.vue` Imports in TS

- TypeScript cannot handle type information for `.vue` imports by default, so we replace the `tsc` CLI with `vue-tsc` for type checking.
- In editors, we need [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) to make the TypeScript language service aware of `.vue` types.

### Formatting

- The project uses Prettier for code formatting.
- To format the code, run:
    ```sh
    npm run format
    ```

## License

This project is licensed under the MIT License.