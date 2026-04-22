FROM python:3.11-slim

WORKDIR /expt-20

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5020

CMD ["python", "app.py"]