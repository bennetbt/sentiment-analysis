FROM python:3.10.10-bullseye
WORKDIR /sentiment-analysis
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "uvicorn", "sentiment-analysis:app", "--host", "0.0.0.0", "--port", "8000", "--reload"] 