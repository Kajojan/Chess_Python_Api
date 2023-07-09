FROM python:3.8
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

HEALTHCHECK --interval=5s --timeout=3s \
    CMD curl --fail http://localhost:8000/healthcheck || exit 1

EXPOSE 8000

