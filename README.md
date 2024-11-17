# Confidential Workload Template

This project provides a framework for processing confidential workloads between multiple data holders and users. It supports secure data quality checks, collaborative analysis, and AI training in a confidential computing environment.

---

## Features

- **Confidential Data Processing**: Handles secure workloads while maintaining privacy.
- **Data Quality Checks**: Triggers data holders' quality checks.
- **Collaborative Analysis**: Enables secure analysis across data owners.

---

## Use case
To make this template closer to a real use case,
The use case implements a basic algorithm that is waiting for an event of type 'CHECK_COMMON_DEMO_CUSTOMERS' and when received does the following:
 1. Read data from 2 data holders
 2. Calculate common customers based on email, name and company
 3. Build a report and send it to data user.

All these steps are defined in the "check_common_customers_demo_event_processor" function of the process.py file.

---

## Project Structure

```
├── .github 
├── ── workflows
├── ── ──release_docker_image.yaml  #  sample code to build and publish the docker image via github actions 
├── data             # datasets examples used in the demo and loaded by the confidential workload from the github repository at execution time
├── data             # example of outputs
├── test             # unit tests
├── .env.example     # env example to run locally
├── Dockerfile       # Docker configuration for containerized deployment
├── index.py         # Entry point for orchestrating events
├── LICENSE.txt      # License information (MIT License)
├── process.py       # Core processing logic for confidential workloads
├── README.md.txt    # Readme file
├── requirements.txt # List of required Python packages
```

---

## Deployment process
What happens when such a repo is pushed on a github repository ?

The dockerfile is being used to build a docker image that is then published on the github container registry.
You can then refer to this docker image via its registry address to make the datavillage platform download and run it in a confidential environment

---

## License

This project is licensed under the MIT License. See `LICENSE.txt` for details.