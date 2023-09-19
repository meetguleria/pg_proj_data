---

## PostgreSQL Testing Framework

This repository contains a framework designed to interact with and validate the functionality of a PostgreSQL database. It integrates automated testing and CI/CD practices, ensuring that the database operations adhere to expected behaviors.

### Project Structure

- **Python Environment**: Utilizes a virtual environment (`venv`) for dependency management.
- **Automated Tests**: Leverages the `pytest` framework for writing and executing tests against a PostgreSQL instance.
- **CI/CD**: Incorporates Jenkins to automate the test execution process, showcasing a basic Continuous Integration pipeline.

### Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/meetguleria/pg_proj_data.git
   cd pg_proj_data
   ```

2. **Set up the Python Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Start PostgreSQL**:

   Ensure PostgreSQL is active and reachable. If utilizing Homebrew:

   ```bash
   brew services start postgresql
   ```

4. **Execute Tests**:

   ```bash
   pytest
   ```

5. **Jenkins Integration**:

   With Jenkins operational, ensure it can access the project directory. In Jenkins, create a new task, link it to this Git repository, and configure the build steps to navigate to the project directory and invoke `pytest`.

### Key Tests Included

1. **Connection Verification**: Confirms successful connection to the PostgreSQL server.
2. **Database Creation**: Validates the capability to generate and access a new database.
3. **CRUD Operations**: Conducts basic Create, Read, Update, and Delete operations on a database table.

---