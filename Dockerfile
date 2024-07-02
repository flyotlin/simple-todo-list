FROM python:3.9-alpine3.19

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# CMD ["uvicorn", "main:app", "--reload"]
CMD ["fastapi", "run", "main.py", "--port", "80"]
