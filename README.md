## Test Instructions

# Stage 1: Easy (Foundational Skills)
Duration: ~20 minutes

Objective: Verify core skills with small, isolated, test-driven tasks.

Part A: React Component
Task: The frontend/ directory contains a component UserCard.js and mock data in src/mockData.js. The App.js file is currently empty.

Implement the UserCard.js component to correctly display the name, email, and company of a user passed in via props.

In App.js, import the mock data and render a UserCard for each user.

Tests (UserCard.test.js, App.test.js):

A unit test will render UserCard with a sample prop and assert that the text content is correct.

An integration test will render App.js and assert that the correct number of user cards are present in the document.

Part B: Python Logic
Task: In the backend/ directory, complete the function transform_products in the logic.py file as per the instructions in the docstring.

Tests (test_logic.py):

Unit tests will call the function with different lists, categories, and discounts to verify the output format and correctness of the calculation. Includes edge cases like an empty product list or a category with no products.

Part C: SQL Queries
Task: In the sql/ directory, write two queries in the queries.sql file based on the schema provided in schema.sql.

Tests: The platform will execute each query against a pre-populated database and compare the result set against the expected output.

# Stage 2: Medium (API Integration)
Duration: ~40 minutes

Objective: Build and connect a simple API. The focus is on making the client and server communicate correctly.

Setup:
A docker-compose.yml file is provided to run the frontend, backend (Python FastAPI/Flask), and a database. The candidate simply needs to run docker-compose up. The backend already has a database connection configured.

Tasks:
(Backend) Implement API Endpoints: In backend/main.py:

Task 2.1: Complete the GET /tasks endpoint. It must query the pre-defined tasks table in the database and return all tasks as a JSON list.

Task 2.2: Complete the POST /tasks endpoint. It must read the {"title": "..."} from the request body, create a new record in the tasks table, and return the newly created task object with its id.

Tests (test_api.py): These are integration tests that use a library like requests to make live HTTP calls to the running backend service. They will test the status codes, response bodies, and check the database state before and after the API calls.

(Frontend) Consume the API: In frontend/src/App.js:

Task 2.3: When the component mounts, fetch data from the GET /tasks endpoint and display the titles in an unordered list (<ul>).

Task 2.4: Implement the form submission logic. When the "Add Task" button is clicked, it should make a POST request to /tasks with the input field's value. After a successful response, it should re-fetch the task list to display the new task.

Tests (App.integration.test.js): These tests use Mock Service Worker (MSW) to intercept the API calls.

One test asserts that a GET request is made on component mount.

Another test simulates filling out the form and clicking the button, then asserts that a POST request was made with the correct body.

# Stage 3: Hard (Refactoring & Business Logic)
Duration: ~30 minutes

Objective: Assess the candidate's ability to modify existing code to add a new business requirement in a clean and secure way.

Task: Implement Multi-User Support
"The application needs to be updated to support multiple users. We will identify users via a simple x-user-id header. You do not need to build a login system."

(Database): An automated migration script is provided. The candidate is instructed to inspect it. The script adds a user_id column to the tasks table.

(Backend) Refactor Endpoints: In backend/main.py:

Modify the POST /tasks endpoint. It must now extract the user ID from the x-user-id request header and save it in the new user_id column when creating a task. If the header is missing, it should return a 401 Unauthorized error.

Modify the GET /tasks endpoint. It must now only return tasks that belong to the user_id specified in the x-user-id header.

(Frontend) Update API Calls:

Modify the API service in the frontend to send a hardcoded x-user-id: "user-123" header with all requests to /tasks.