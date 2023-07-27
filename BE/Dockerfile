FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
RUN apt-get update && apt-get install git -y && pip3 install --upgrade pip && \
pip3 install pillow apscheduler diffusers==0.14.0 requests xmltodict sqlalchemy gunicorn && \
pip3 install git+https://github.com/cloneofsimo/lora.git

WORKDIR /usr/src/app
COPY . .

CMD ["gunicorn", "--bind", "0:8000", "main:app", "--worker-class", "uvicorn.workers.UvicornWorker"]