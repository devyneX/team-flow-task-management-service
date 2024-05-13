FROM python:3.12.3-alpine3.19
 
WORKDIR /app
 
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
 
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
 
COPY requirements.txt /app/
 
RUN pip install -r requirements.txt
 
COPY . /app/
 
RUN chmod +x /app/start.sh
 
CMD ["sh", "/app/start.sh"]