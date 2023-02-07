# Social Card API

This application is an API built with Django REST Framework (DRF) that lets users track social cards that they want to create, display, or follow other users doing the same! Cards are listed with important information like title, user, font, or border options.

# Link to Production Application

https://social-cards-wg2j.onrender.com

**All requests, except registration and log in, require authentication**.

Documentation starts here:

### API ENDPOINTS

| HTTP Verbs | Endpoints           | Action                                 |
| ---------- | ------------------- | -------------------------------------- |
| GET        | /auth/token/login   | To login to an existing account        |
| GET        | /auth/token/logout  | Logout from account                    |
| POST       | /auth/users/        | Register new user                      |
| GET        | /cards/             | Gets list of all cards created         |
| GET        | /cards/me/          | List all of the logged in user's cards |
| POST       | /cards/me/          | Create a card for the logged in user   |
| GET        | /cards/<card_id>/   | Get a specific card's details          |
| PATCH      | /cards/<card_id>/   | Updates a specific card's details.     |
| DELETE     | /cards/<card_id>/   | Delete's a specific card.              |
| GET        | /cards/<username>/  | View a specific user's cards.          |
| GET        | /cards/followed/    | Gets a list of followed user's cards.  |
| POST       | /follower/<username>| Follow the given user.                 |
| DELETE     | /unfollow/<username>| Unfollow the given user.               |
| GET        | /like/<int:card_id> | Will like/unlike given card.           |
| GET        | /search             | Search for a card's tag(s).            |
| GET        | /comment/           | Get a list of all comments             |
| POST       | /comment/           | Create a new comment                   |
| GET        | /comments/<int:pk>/ | View a Specific comment                |
| PUT        | /comments/<int:pk>/ | Updates the comment with specified id  |
| DELETE     | /comments/<int:pk>/ | Deletes comment with specific id       |

## Register a new user

### request

Username and password are required.

```
POST auth/users/

{
	"username": "coding11",
	"password": "keyboard10"
}
```

### response

```
201 Created

{
	"email": "",
	"username": "coding11",
	"id": 3
}

```

## Log In

### request

```
POST auth/token/login

{
  "username": "coding11",
  "password": "keyboard10"
}
```

### response

```json
{
  "auth_token": "70a36d6046970a5d2cb25fe450a6c16c16b44df2"
}
```

## List all Cards

Requires authentication.

### request

```txt
GET /cards/me/
```

### response

```json
[
  {
    "id": 11,
    "owner": "coding11",
    "title": "Example",
    "front_message": "I love examples",
    "back_message": "Just kidding",
    "front_image": null,
    "back_image": null,
    "font": "Arial",
    "text_color": "Red",
    "border_color": "Dark blue",
    "tags": ["EXAMPLE"]
  },
  {
    "id": 12,
    "owner": "coding11",
    "title": "Coding",
    "front_message": "Coding is too easy",
    "back_message": "For me anyways",
    "front_image": null,
    "back_image": null,
    "font": "Times New Roman",
    "text_color": "Orange",
    "border_color": "Black",
    "tags": ["CODING"]
  }
]
```

## Add a Card

Requires authentication.

### request

```txt
POST /cards/me/
```

```json
{
  "title": "Coding",
  "front_message": "Coding is too easy",
  "back_message": "For me anyways",
  "front_image": null,
  "back_image": null,
  "font": "Times New Roman",
  "text_color": "Orange",
  "border_color": "Black",
  "tags": ["CODING"]
}
```

### response

```json
{
  "id": 12,
  "owner": "coding11",
  "title": "Coding",
  "front_message": "Coding is too easy",
  "back_message": "For me anyways",
  "front_image": null,
  "back_image": null,
  "font": "Times New Roman",
  "text_color": "Orange",
  "border_color": "Black",
  "tags": ["CODING"]
}
```

\*\*\* Please note that default values are null for certain parameters, may institute defaults in the future.

## Look at cards details

Requires authentication.

### request

```txt
GET /cards/<int:card_id>/
```

### response

```json
{
  "id": 3,
  "owner": "admin",
  "title": null,
  "front_message": null,
  "back_message": null,
  "front_image": null,
  "back_image": null,
  "font": null,
  "text_color": null,
  "border_color": null,
  "tags": []
}
```

## List all comments

### request

Authorization is required.

```
GET <BASE_URL>/comment/

```

### response

```json
200 OK

[
	{
		"id": 1,
		"social_card": 3,
		"comment": "TESTING!",
		"user": "coding11"
	},
	{
		"id": 2,
		"social_card": 4,
		"comment": "I really like coding!",
		"user": "coding11"
	}
]

```

## Comment detail

### request

Authorization is required.

```
GET <BASE_URL>/comment/1/

```

### response

```json
200 OK

{
	"id": 1,
	"social_card": 3,
	"comment": "TESTING!",
	"user": "coding11"
}

```


## Follow a user

### request

Authorization is required.

```
GET /follower/<username>/

```

### response




## Unfollow a user

### request

Authorization is required.

```
GET /unfollow/<username>/

```

### response

```json