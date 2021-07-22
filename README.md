# Image Resizer Service

This is a simple image resizing docker container service with python 2

## Parameters

| Name  | Type | Desc |
| ------------ | ------------  |------------ |
| url  |    Optional* | Image URL.  |
| url64  |    Optional* | Base 64 encoded Image URL.  |
| bg  |    Optional*  | Background color Hex code  |
| w  |    Optional  | Width (Default 960px)  |
| h  |    Optional  | Height (Default 960px)  |

###### One of the URL options or bg color is required, all other parameters are optional.

------------

## Buillding and running as a docker container

```
docker build . --tag image-resizer
docker run --rm -i -t -p 8000:18080 image-resizer
```

## Examples

- [Resize image from URL](https://img.algoritmik.net/?url=https://www.algoritmik.net/images/algoritmik-logo.png&w=250) 
- [Resize image from base64 encoded URL](https://img.algoritmik.net/?url64=aHR0cHM6Ly93d3cuYWxnb3JpdG1pay5uZXQvaW1hZ2VzL2FsZ29yaXRtaWstbG9nby5wbmc=&w=250) 
- [New image with spesified hex color and dimentions ](https://img.algoritmik.net/?bg=27bdbe&w=250&h=150) 