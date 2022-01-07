FROM python:3.9-slim-buster
RUN apt update && apt install -y build-essential python3-dev ssh git apt-transport-https lsb-release ca-certificates && apt update
COPY . /integration
WORKDIR /integration
RUN pip install -r requirements.txt
ARG PORT=8000
ENV PORT_NUMBER=$PORT
EXPOSE $PORT_NUMBER
ARG DEBUG=False
ENV DEBUG_MODE=$DEBUG
CMD uvicorn app:fast --reload