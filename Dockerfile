FROM python:3.11.4

# install needed packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libcairo2-dev

# clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . .

CMD gunicorn darient_credit.wsgi