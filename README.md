# PetStorePerformanceTest

A Python-based performance testing framework built with [Locust](https://locust.io), designed to evaluate and validate the scalability and reliability of the Swagger Petstore API. It includes modular test suites for Pet, Store, and User resources, simulating realistic load scenarios and monitoring system behavior under stress.

---

## Project Structure

```
PetStorePerformanceTest/
├── locust_tests/              # Contains categorized Locust test scripts
│   ├── pet/
│   │   └── pet_test.py        # Pet API performance tests
│   ├── store/
│   │   └── store_test.py      # Store order performance tests
│   └── user/
│       └── user_test.py       # User API performance tests
└── Main.py                    # CLI-based launcher to select which test to run
```

---

## Features

- Modular design using Locust
- Separate test suites: Pet, Store, User
- Real-time web UI monitoring
- CRUD operations & verification for each entity
- Random ID generation for unique test data (Pet)
- Automatic test startup from Main.py

---

## Technologies Used and Their Purpose

| Technology | Purpose |
|-----------|---------|
| Python    | Programming language |
| Locust    | Performance/load testing framework |
| JSON      | Request body and response parsing |
| Subprocess & CLI | For launching tests dynamically via Main.py |

---

## Test Coverage

| Class | Methods Tested           |
|-------|--------------------------|
| Pet   | POST, PUT, GET, DELETE   |
| Store | POST, GET, DELETE        |
| User  | POST, PUT, GET, DELETE   |
