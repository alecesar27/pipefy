FROM python:3.9

WORKDIR D:/Projeto_ Accenture/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

#CMD ["fastapi", "dev", "main.py", "--port=80"]
CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "80"]