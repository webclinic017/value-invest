# Stock Valuations using Rule1 Analysis

This repo contains code used for stock valuations. The stock valuation method used is a form of value investing, using Rule 1 calculations and analysis.

The stock price and company fundamental data is source from [Alpha Vantage](https://www.alphavantage.co/). From the "About" section of their website:
>Backed by the prestigious Y Combinator and composed of a tight-knit community of researchers, engineers, and business professionals, Alpha Vantage Inc. has partnered with major exchanges and institutions around the world to become a leading provider of stock APIs as well as forex (FX) and digital/crypto currency data feeds. Our success is driven by rigorous research, cutting edge technology, and a disciplined focus on democratizing access to data.

They provide free a stock API service for up to 5 requests per minute, or 500 requests per day.


## Table of Contents
1. [Setup](#1-setup)
2. [Configuration](#2-configuration)

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