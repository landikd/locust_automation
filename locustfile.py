# Use locust -f locustfile.py --loglevel ERROR to start a test with ERROR log level
# Use locust -f locustfile.py to start a test with loggin type "INFO"

from locust import User, task, constant_pacing, LoadTestShape, run_single_user, events, TaskSet, FastHttpUser, SequentialTaskSet
from utils import extract_and_check_param, assert_response, log_response, read_csv

import logging, inspect, time



# Debug flag
DEBUG_MODE = False  # Change to False to disable response printing to log/console

class TestScenario_1(SequentialTaskSet): # This is your user scenario
    pacing = 30 # Pacing
    tasks_count = 3 # Tasks count to set desired pauses

    def on_start(self): # This is your init function to prepare something before the scenario run
        self.host = self.client.base_url
        self.credentials = read_csv(r"C:\path_to_your_file\credentials.csv") # How to load parameters from CSV file (header should be present in CSV)
        self.username, self.password = self.credentials[0]  # Tip: use .pop() for unique credentials
	
    wait_time = constant_pacing(pacing / tasks_count)  # Constant wait time between tasks (1 task = 1 user transaction / wait time should be applied to every user transaction)
    @task
    def T01_Open_Home_Page(self): # User transaction name

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        }

        body = None
        with self.client.request("GET", "/", headers=headers, body=None, allow_redirects=True, catch_response=True) as response:
            log_response(response.text, DEBUG_MODE)
            assert_response(response, valid_status_codes=[200, 302], expected_text="") # Put here your valid status codes and expected text to be found in response
    
    wait_time = constant_pacing(pacing / tasks_count)  # Constant wait time between tasks
    @task
    def T02_Go_To_Login_Form(self):
        headers = {
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "referer": f"{self.host}/"
        }

        body = None
        with self.client.request("GET", f"/login_and_go?returnUrl={self.host}/", headers=headers, body=body, allow_redirects=True, catch_response=True) as response:
            log_response(response.text, DEBUG_MODE)
            assert_response(response, valid_status_codes=[200, 302], expected_text="")
            self.csrf_token = extract_and_check_param(response.text, left_boundary='id="_token" name="_token" form-error-clear="" value="', right_boundary='" /></form>', param_name='csrf_token') # Correlation for csrf_token
    
    wait_time = constant_pacing(pacing / tasks_count)  # Constant wait time between tasks
    @task
    def T03_Login_With_Credentials(self):
        headers = {
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "content-type": "application/x-www-form-urlencoded",
            "origin": f"{self.host}",
            "referer": f"{self.host}/login_and_go?returnUrl={self.host}/",
        }

        data = f"_username={self.username}&_password={self.password}&login=&_target_path={self.host}&_token={self.csrf_token}"

        body = None
        with self.client.request("POST", "/login_check", headers=headers, body=body, data=data, allow_redirects=True, catch_response=True) as response:
            log_response(response.text, DEBUG_MODE)
            assert_response(response, valid_status_codes=[200, 302], expected_text="")

class TestScenario_2(SequentialTaskSet): # This is your user scenario
    pacing = 30 # Pacing
    tasks_count = 3 # Tasks count to set desired pauses
   
    def on_start(self): # This is your init function to prepare something before the scenario run
        self.host = self.client.base_url
        self.credentials = read_csv(r"C:\Users\DmytroLandik\Desktop\credentials.csv") # How to load parameters from CSV file (header should be present in CSV)
        self.username, self.password = self.credentials[0]  
	
    wait_time = constant_pacing(pacing / tasks_count)  # Constant wait time between tasks (1 task = 1 user transaction / wait time should be applied to every user transaction)
    @task
    def T01_2_Open_Home_Page(self): # User transaction name

        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "sec-ch-ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        }

        body = None
        with self.client.request("GET", "/", headers=headers, body=None, allow_redirects=True, catch_response=True) as response:
            log_response(response.text, DEBUG_MODE)
            assert_response(response, valid_status_codes=[200, 302], expected_text="")
    
    wait_time = constant_pacing(pacing / tasks_count)  # Constant wait time between tasks
    @task
    def T02_2_Go_To_Login_Form(self):
        headers = {
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "referer": f"{self.host}/"
        }

        body = None
        with self.client.request("GET", f"/login_and_go?returnUrl={self.host}/", headers=headers, body=body, allow_redirects=True, catch_response=True) as response:
            log_response(response.text, DEBUG_MODE)
            assert_response(response, valid_status_codes=[200, 302], expected_text="")
            self.csrf_token = extract_and_check_param(response.text, left_boundary='id="_token" name="_token" form-error-clear="" value="', right_boundary='" /></form>', param_name='csrf_token') # Correlation for csrf_token
    
    wait_time = constant_pacing(pacing / tasks_count)  # Constant wait time between tasks
    @task
    def T03_2_Login_With_Credentials(self):
        headers = {
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "content-type": "application/x-www-form-urlencoded",
            "origin": f"{self.host}",
            "referer": f"{self.host}/login_and_go?returnUrl={self.host}/",
        }

        data = f"_username={self.username}&_password={self.password}&login=&_target_path={self.host}&_token={self.csrf_token}"

        body = None
        with self.client.request("POST", "/login_check", headers=headers, body=body, data=data, allow_redirects=True, catch_response=True) as response:
            log_response(response.text, DEBUG_MODE)
            assert_response(response, valid_status_codes=[200, 302], expected_text="")


class StagesShape(LoadTestShape):
    stages = [
        {"duration": 60, "users": 3, "spawn_rate": 1}, # Adjust stages to perform different types of load
        #{"duration": 50, "users": 2, "spawn_rate": 1}
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                # This will return the number of users and spawn rate for the current stage
                return (stage["users"], stage["spawn_rate"])

        return None

class WebsiteUser(FastHttpUser): # Main class to run all user scenarios
    host = "https://www.chess.com" # Passing target testing host is a must
    tasks = {TestScenario_1: 2, TestScenario_2: 1} # Add your test scenarios here to run them simultaneously / number of users will be split
