import logging, random, inspect, csv 
from typing import List, Dict

def read_csv(file_path: str) -> List[Dict[str, str]]:
    data = []

    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)

        next(reader)  # Skip the first row (header)

        # Read the remaining rows
        for row in reader:
            data.append(row)

    return data

# Boundary based correlation function
def extract_and_check_param(response_text, left_boundary, right_boundary, param_name):
    param_value = None
    caller_function = inspect.currentframe().f_back.f_code.co_name  # Caller function name

    # Finding position of the left boundary
    start_idx = response_text.find(left_boundary)
    if start_idx != -1:
        # Move index to the end of the left boundary
        start_idx += len(left_boundary)

        # Finding position of the right boundary
        end_idx = response_text.find(right_boundary, start_idx)
        if end_idx != -1:
            # Getting value in between the boundaries
            param_value = response_text[start_idx:end_idx]
            logging.info(f"{caller_function}: Extracted {param_name}: {param_value}")
        else:
            logging.error(f"{caller_function}: Right boundary '{right_boundary}' for {param_name} not found in the response")
    else:
        logging.error(f"{caller_function}: Left boundary '{left_boundary}' for {param_name} not found in the response")

    return param_value

# Function for status code and response text validation
def assert_response(response, valid_status_codes, expected_text):
    caller_function = inspect.currentframe().f_back.f_code.co_name  # Caller function name
    if response.status_code in valid_status_codes:
        logging.info(f"{caller_function}: Response code is valid, status code: {response.status_code}")
        if expected_text in response.text:
            logging.info(f"{caller_function}: Response text is valid, contains: {expected_text}")
            response.success()
        else:
            logging.error(f"{caller_function}: Response failed, response doesn't have such text: {expected_text}")
            response.failure(f"{caller_function}: Invalid response text, doesn't contain: {expected_text}") 
    else:
        logging.error(f"{caller_function}: Response failed, status code: {response.status_code}")
        response.failure(f"{caller_function}: Invalid response code: {response.status_code}")

# Logging and debug options function
def log_response(response_text, debug_mode):
    caller_function = inspect.currentframe().f_back.f_code.co_name  # Caller function name
    if debug_mode:
        logging.info(f"{caller_function}: Response: {response_text}")
        logging.info("")  # Adding empty string for readability
