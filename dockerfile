FROM python:3.11.0rc2-bullseye
WORKDIR /
COPY . .
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD [ "python", "app.py" ]