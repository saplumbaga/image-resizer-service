# Image Resizer Service

This is a simple image resizing docker container service with python 2

## 🛡️ Authentication

This service requires an `Authorization` header using a bearer token:

````
Authorization: Bearer YOUR_SECRET_TOKEN
````

The token is injected via an environment variable called `AUTH_TOKEN`.

---

## Parameters

| Name  | Type | Desc |
| ------------ | ------------  |------------ |
| url  |    Optional* | Image URL.  |
| url64  |    Optional* | Base 64 encoded Image URL.  |
| bg  |    Optional*  | Background color Hex code  |
| w  |    Optional  | Width (Default 960px)  |
| h  |    Optional  | Height (Default 960px)  |

\* One of the URL options (`url` or `url64`) or `bg` is required. All other parameters are optional.

------------

## Installing

```
git clone https://github.com/saplumbaga/image-resizer-service.git
cd image-resizer-service
```

## Pull the latest changes:

````
git pull origin main
````

## Building container manually

```
docker build . --tag image-resizer
docker run --rm -i -t -p 8000:18080 \
  -e AUTH_TOKEN=e34f91b209a24c77b321ca7cb1dc0a83 \
  image-resizer
```


## With Docker Compose

```
version: '3.8'

services:
  image-resizer:
    container_name: image-resizer
    build: .
    restart: always
    ports:
      - "8081:18080"
    environment:
      - AUTH_TOKEN=e34f91b209a24c77b321ca7cb1dc0a83

```
Run it with:

````
docker-compose up --build -d
````

## Examples

- [Resize image from URL](https://img.algoritmik.net/?url=https://www.algoritmik.net/images/algoritmik-ofis.jpg&w=250) 
- [Resize image from base64 encoded URL](https://img.algoritmik.net/?url64=aHR0cHM6Ly93d3cuYWxnb3JpdG1pay5uZXQvaW1hZ2VzL2FsZ29yaXRtaWstb2Zpcy5qcGc=&w=250) 
- [New image with spesified hex color and dimentions ](https://img.algoritmik.net/?bg=27bdbe&w=250&h=150) 