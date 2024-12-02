FROM python:3.9

WORKDIR D:/Projeto_ Accenture/pipefy

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

#CMD ["fastapi", "dev", "main.py", "--port=80"]
CMD ["python", "manage.py", "runserver",  "0.0.0.0:8000"]