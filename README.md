# Locust Automation for Web Scripting

This project is an automation framework built using **Locust** to perform load testing and web interaction automation based on user behavior recorded from a real web browser. It leverages the **HAR** (HTTP Archive) file format for capturing and replaying browser interactions, then automates these interactions using Locust.

## Overview

The project enables you to automate web testing using Locust by following these steps:
1. **Record user interactions**: Capture web interactions from a browser using HAR files.
2. **Convert HAR to Locust**: Use `har2locust` to convert the recorded HAR file to a Locust test script.
3. **Enhance the Locust file**: Use custom functions for parameterization, boundary correlation, assertions, and debugging from **utils.py** file.
4. **Run load tests**: Perform load testing on the website by simulating real user behavior.

## Tools and Libraries

- **Locust**: An open-source load testing tool for web applications.
- **har2locust**: A tool to convert HAR files to Locust test scripts.
- **Python**: Programming language used for custom test script enhancements.
- **Browser (Chrome/Firefox)**: For recording user interactions with the website.

## Installation

### Prerequisites

- Python 3.9 or higher.
- `pip` (Python package manager).
- A web browser (Chrome or Firefox) with Developer Tools for recording HAR files.

### Dependencies

To install the required libraries, use the provided **`requirements.txt`** file. This file lists all the dependencies needed to run the project.

1. Clone this repository or navigate to the project directory.

2. Install the dependencies with the following command:

    ```bash
    pip install -r requirements.txt
    ```

This will install all necessary dependencies, including **Locust**, **har2locust**, and other required Python packages.

## How It Works

### Step 1: Record User Interactions

1. Open the desired website in your browser.
2. Open Developer Tools (`F12` or `Ctrl+Shift+I` in most browsers).
3. Go to the **"Network"** tab.
4. Enable **"Preserve log"** and **"Disable cache"** options.
5. Interact with the website as a normal user (click buttons, fill forms, navigate through pages, etc.).
6. Once the interactions are completed, filter the network log, right-click the network log and select **"Save all as HAR with content"** to save the HAR file.

### Step 2: Convert HAR to Locust Script

1. Use the **`har2locust`** tool to convert the saved HAR file into a Locust test script. For example:

    ```bash
    har2locust your_file.har > locustfile.py
    ```

2. This will generate a Locust script based on the recorded requests and responses.

### Step 3: Customize Locust Script

Now, open the generated **`locustfile.py`**, adjust it with my **`locustfile.py`** from the repository and add enhancements, such as:

- **Parameterization**: Use dynamic data (e.g., random values, data from an external file, or API responses) to simulate a more realistic user experience.
- **Boundary Correlation**: Automatically correlate dynamic values (such as session IDs, tokens, etc.) from previous requests to make subsequent requests work correctly.
- **Assertions**: Add assertions to validate that the application behaves as expected under load (e.g., check for HTTP status codes, response times).
- **Debugging**: Add logging for debugging the script, especially useful for tracking down issues in request handling.

### Step 4: Running Locust
Run the Locust load test with the following command:

    ```bash
    Copy code
    locust -f locustfile.py
    ```
Navigate to http://localhost:8089 in your browser to start the test.

### Step 5: Analyze the Results
The Locust UI will show real-time results, including the number of requests per second, response times, and any failures. You can use this information to identify performance bottlenecks or issues with your application.

### Additional Resources
For further improvements or inspiration, check out the Awesome Locust list:

Awesome Locust: A collection of tools, libraries, and resources for building automated frameworks based on Locust.
