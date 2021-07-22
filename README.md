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