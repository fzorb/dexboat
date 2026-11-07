FROM astral/uv:latest

WORKDIR /app
COPY . .

RUN uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:$PATH"
ENV PORT=8080

CMD ["sh", "-c", "uv run --no-sync functions-framework --source src/dexboat/main.py --target bot --host 0.0.0.0 --port ${PORT}"]
