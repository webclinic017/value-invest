# Stock Valuations using Rule1 Analysis

This repo contains code used for stock valuations. The stock valuation method used is a form of value investing, using Rule 1 calculations and analysis.

The stock price and company fundamental data is sourced from [SimFin](https://simfin.com/) and [Alpha Vantage](https://www.alphavantage.co/). Historical fundamental data (pre-2019) for US companies was downloaded via SimFin. This data was then loaded into a [Postgres](https://www.postgresql.org/) database. The Alpha Vantage data provides current fundamental data, and recent data is added to the Postgres database from this source as it becomes available.



## Table of Contents
1. [Setup](#1-setup)
2. [Configuration](#2-configuration)
3. [Database](#3-database)

## 1. Setup

First, clone the repo using the command:
```shell
git clone https://github.com/h-morgan/value-invest.git
```

Next, intialize a virtual environment to store project dependencies. The following command uses the `venv` Python command to intialize a virtual environment called `venv`:
```shell
python3 -m venv venv
```

Then, install project dependencies in the `venv` using the following command:
```shell
pip install -r requirements.txt
```

## 2. Configuration

This project requies a `.env` file to store environment variables and configuations. Create a `.env` file in the `src/` directory with the following contents:

```json
av-api-token = "your-api-key"
```

In order to use use the project, an API key from [Alpha Vantage](https://www.alphavantage.co/) is needed. as described above. Once a free API key is obtained, the value needs to be stored in the `.env` file as shown above.

## 3. Database

As previously mentioned, the data for this project is sourced and loaded into a Postgres database, which is currently hosted in a [Docker](https://www.docker.com/) container on a [Digital Ocean](https://www.digitalocean.com/) server droplet. 

For future debugging and reference, the command used to run the [Postgres Docker](https://hub.docker.com/_/postgres) container on the server is:
```shell
docker run -d --name invest-pg-docker \
 -e POSTGRES_PASSWORD=password \
 -e POSTGRES_DB=invest-db \
 -e PGDATA=/var/lib/postgresql/data/pgdata \
 -v ~/data:/var/lib/postgresql/data \
 -p 5432:5432 \
 postgres
```
