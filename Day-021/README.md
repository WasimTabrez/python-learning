# 📅 Day 21 – Backend Development Fundamentals (HTTP, REST APIs & JSON)

## 🎯 Objective

Begin the Backend Engineering phase by learning how web applications communicate over the Internet. Understand HTTP, REST APIs, JSON, URL parsing, API requests, and API design. Build your first REST API simulators before moving to FastAPI.

---

# 📚 Concepts Learned

- Introduction to Backend Development
- Client-Server Architecture
- Frontend vs Backend
- HTTP Protocol
- HTTPS
- URL Structure
- REST API Fundamentals
- HTTP Request
- HTTP Response
- HTTP Headers
- HTTP Methods
- HTTP Status Codes
- Query Parameters
- URL Parsing
- JSON Encoding
- JSON Decoding
- JSON Files
- API Requests using `requests`
- API Error Handling
- Request Logging
- Configuration Files
- REST API Design
- Routing
- Modular Backend Architecture

---

# 💻 Programs Implemented

| File | Description |
|------|-------------|
| `json_encode.py` | Convert Python objects to JSON |
| `json_decode.py` | Convert JSON to Python objects |
| `json_file.py` | Read and write JSON files |
| `http_methods.py` | Demonstrate common HTTP methods |
| `status_codes.py` | Demonstrate HTTP status codes |
| `url_parser.py` | Parse URLs using `urllib.parse` |
| `request_logger.py` | Log HTTP requests |
| `config_loader.py` | Load configuration from a JSON file |
| `requests_get.py` | Send an HTTP GET request |
| `requests_post.py` | Send an HTTP POST request |
| `requests_headers.py` | Send custom HTTP headers |
| `requests_params.py` | Send query parameters |
| `requests_timeout.py` | Demonstrate request timeout handling |
| `requests_error.py` | Handle HTTP and network exceptions |
| `api_response.py` | Process JSON API responses |
| `rest_demo.py` | Demonstrate REST operations |
| `api_client.py` | Build a reusable API client |
| `weather_api.py` | Consume a Weather REST API |
| `github_api.py` | Consume the GitHub REST API |
| `news_api.py` | Consume a News REST API |

---

# 🏆 Mini Project

## Student REST API Simulator

### Features

- Home Endpoint
- Get All Students
- Get Student by ID
- Add Student
- Update Student
- Delete Student
- JSON Responses
- HTTP Status Codes
- Modular Routing
- In-Memory Database

### Concepts Used

- HTTP
- REST APIs
- Routing
- JSON
- CRUD Operations
- Dictionaries
- Functions
- Classes
- Error Handling

---

# ⭐ Bonus Project

## Employee REST API Simulator

### Features

- Employee CRUD Operations
- Department Endpoint
- Salary Update Endpoint
- Employee Search
- JSON Responses
- HTTP Status Codes
- Modular Routing
- In-Memory Database

### Concepts Used

- REST API Design
- HTTP Methods
- Routing
- JSON
- Dictionaries
- OOP
- Modular Programming

---

# 📂 Folder Structure

```text
Day-021/
│
├── README.md
│
├── json_encode.py
├── json_decode.py
├── json_file.py
├── http_methods.py
├── status_codes.py
├── url_parser.py
├── request_logger.py
├── config_loader.py
├── requests_get.py
├── requests_post.py
├── requests_headers.py
├── requests_params.py
├── requests_timeout.py
├── requests_error.py
├── api_response.py
├── rest_demo.py
├── api_client.py
├── weather_api.py
├── github_api.py
├── news_api.py
│
├── StudentRESTAPI/
│   ├── student.py
│   ├── database.py
│   ├── response.py
│   ├── router.py
│   └── api.py
│
└── EmployeeRESTAPI/
    ├── employee.py
    ├── database.py
    ├── response.py
    ├── router.py
    └── api.py
```

---

# 🧠 Key Concepts Summary

## HTTP Methods

| Method | Purpose |
|---------|---------|
| GET | Retrieve data |
| POST | Create a new resource |
| PUT | Replace an existing resource |
| PATCH | Partially update a resource |
| DELETE | Remove a resource |

---

## Common HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

## JSON Functions

| Function | Description |
|----------|-------------|
| `json.dumps()` | Python object → JSON string |
| `json.loads()` | JSON string → Python object |
| `json.dump()` | Write JSON to file |
| `json.load()` | Read JSON from file |

---

## REST API Flow

```text
Client
   │
   │ HTTP Request
   ▼
Server
   │
Business Logic
   │
Database
   │
JSON Response
   ▼
Client
```

---

# 🌍 Real-World Applications

- Backend Web Development
- RESTful Web Services
- Mobile App Backends
- AI Application APIs
- Payment Gateways
- Cloud Services
- GitHub APIs
- Weather APIs
- OpenAI APIs
- Microservices

---

# 🎯 Learning Outcomes

By the end of Day 21, you can:

- Explain how the web works.
- Understand the client-server architecture.
- Understand HTTP and HTTPS.
- Use HTTP methods correctly.
- Interpret HTTP status codes.
- Read and write JSON data.
- Parse URLs.
- Send GET and POST requests.
- Handle API errors and timeouts.
- Build reusable API clients.
- Design RESTful APIs.
- Build modular backend applications.

---

# 💡 Interview Questions

1. What is Backend Development?
2. Explain the Client-Server Architecture.
3. What is HTTP?
4. What is HTTPS?
5. What is the difference between HTTP and HTTPS?
6. What is a REST API?
7. What are the commonly used HTTP methods?
8. What is the difference between PUT and PATCH?
9. What are HTTP status codes?
10. What is JSON?
11. What is the difference between `json.dump()` and `json.dumps()`?
12. What is the difference between `json.load()` and `json.loads()`?
13. Why are HTTP headers used?
14. What are query parameters?
15. What is URL parsing?
16. Why should every API request use a timeout?
17. What is `response.raise_for_status()`?
18. Why should API calls use exception handling?
19. Why is modular programming important in backend development?
20. How will these concepts help when learning FastAPI?

---

# 🏆 Skills Acquired

- HTTP Fundamentals
- REST API Design
- JSON Processing
- URL Parsing
- API Consumption
- Request Handling
- Error Handling
- Logging
- Routing
- Modular Programming
- Backend Architecture

---

# 📈 Progress Tracker

```text
Python Basics                  ██████████ 100%
Functions                      ██████████ 100%
Object-Oriented Programming    ██████████ 100%
Exception Handling             ██████████ 100%
File Handling                  ██████████ 100%
Regular Expressions            ██████████ 100%
Iterators & Generators         ██████████ 100%
Decorators                     ██████████ 100%
Multithreading                 ██████████ 100%
SQLite                         ██████████ 100%

Backend Fundamentals           ███░░░░░░░ 30%

Overall Roadmap                ██████░░░░ 60%
```

---

# 🚀 Next Step

**Day 22 – FastAPI Fundamentals**

Topics:

- Installing FastAPI
- Creating Your First API
- Running Uvicorn
- Path Operations
- Query Parameters
- Path Parameters
- Request Body
- Response Models
- Automatic API Documentation
- Interactive Swagger UI

---

## ✅ Day 21 Completed Successfully

You have successfully entered the **Backend Engineering** phase of your roadmap. The concepts learned today provide the foundation for building real-world APIs with **FastAPI**, which will be used extensively in modern backend development and AI applications.
