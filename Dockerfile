FROM python:3.10.2-alpine

WORKDIR /unijobs-api
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000
COPY . .
CMD ["python3", "-m", "uvicorn", "--app-dir=./src", "app:app", "--host=0.0.0.0", "--reload"]