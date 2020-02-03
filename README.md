# spiegel-api [![Docker Hub](https://img.shields.io/badge/docker-hub-blue)](https://hub.docker.com/r/ietz/spiegel-api)

REST API for [DER SPIEGEL](https://www.spiegel.de/) written in python.
Wrapper for the [spiegel-scraper](https://pypi.org/project/spiegel-scraper/) module.

## Usage
Run the [ietz/spiegel-api](https://hub.docker.com/r/ietz/spiegel-api) Docker image:
```bash
docker run -it --rm -p 8080:8080 ietz/spiegel-api
```

The REST API is now running at `http://localhost:8080/`.

## Example requests

- **List all articles published on a given date**
  ```http
  GET /archive/2020/01/20
  ```
	add an `include-html` query parameter if you want the service to return the HTML which the results are scraped from

- **Scrape an article given its url**
  ```http
  GET /articles?url=https%3A%2F%2Fwww.spiegel.de%2Fkultur%2Ftv%2Fanne-will-zu-libyen-mit-heiko-maas-schluessel-ins-schloss-a-67fe47b7-fdbf-4533-a7ea-7b58f95b0b7b
  ```
	add an `include-html` query parameter if you want the service to return the HTML which the results are scraped from

- **Retrieve comments for an article by its id** (which is provided by the article-by-url method)
  ```http
  GET /articles/67fe47b7-fdbf-4533-a7ea-7b58f95b0b7b/comments
  ```

## Build the docker image locally
```bash
docker build -t ietz/spiegel-api:latest .
```
