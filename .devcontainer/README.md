Codespaces notes

- After the container builds, use Run Task > "dev: all" to start both Django (port 8000) and React (port 3000).
- The React app (port 3000) will be auto-forwarded. To call the Django API through Codespaces forwarding, configure the environment variable REACT_APP_API_BASE_URL to the forwarded URL for the Django port, e.g.:

  REACT_APP_API_BASE_URL=https://<your-codespace>-8000.app.github.dev

- For local development (outside Codespaces), the CRA proxy remains set to http://localhost:8000 so no env var is needed.
