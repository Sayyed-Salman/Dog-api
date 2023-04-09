# 🐶 Dog API

The Dog API is a RESTful API interface for retrieving random images of dogs. The API is completely free to use and does not require an API key. The API is a great way to add some fun to your application or website.

## Schema

```json
{
    id: int,
    name : string,
    image : string,
    description : string,
}
```

## Methods

Base URL: https://localhost:5000/api

### /add_dog

HTTP Method: POST

Request body:

```json
{
  "name": "Labrador Retriever",
  "image": "https://images.dog.ceo/breeds/labrador/n02099712_1003.jpg",
  "description": "The Labrador Retriever is one of the most popular breeds of dog in Canada, the United Kingdom"
}
```

### /dog/int:id

HTTP Method: GET

Request parameters: id - ID of the dog to retrieve

Response body:

```json
{
  "id": 1,
  "name": "Labrador Retriever",
  "image": "https://images.dog.ceo/breeds/labrador/n02099712_1003.jpg",
  "description": "The Labrador Retriever is one of the most popular breeds of dog in Canada, the United Kingdom"
}
```

### /dogs

HTTP Method: GET

Response body:

```json
[
  {
    "id": 1,
    "name": "Labrador Retriever",
    "image": "https://images.dog.ceo/breeds/labrador/n02099712_1003.jpg",
    "description": "The Labrador Retriever is one of the most popular breeds of dog in Canada, the United Kingdom"
  },

  {
    "id": 2,
    "name": "Labrador Retriever",
    "image": "https://images.dog.ceo/breeds/labrador/n02099712_1003.jpg",
    "description": "The Labrador Retriever is one of the most popular breeds of dog in Canada, the United Kingdom"
  }
]
```

## License

The Dog API is free to use and distribute under the MIT license. See LICENSE for more information.
