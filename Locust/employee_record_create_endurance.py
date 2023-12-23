from locust import HttpUser, task, between

# Define a Locust user class for HR endurance testing
class OdooHREnduranceUser(HttpUser):
    # Set wait time between tasks
    wait_time = between(2, 5)

    # Task to create an employee record
    @task
    def create_employee_record(self):
        # Log in to Odoo
        login_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'common',
                'method': 'login',
                'args': ['database_name', 'username', 'password']
            }
        }
        response = self.client.post('/web/session/authenticate', json=login_payload)
        session_id = response.json()['result']['session_id']

        # Payload to create an employee record
        create_employee_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'object',
                'method': 'execute',
                'args': ['database_name', session_id, 'password', 'hr.employee', 'create', {
                    'name': 'John Doe',  
                    'job_id': 1,  
                }]
            }
        }

        # Send a POST request to create an employee record
        self.client.post('/web/dataset/call_kw/hr.employee/create', json=create_employee_payload)

        # Log out
        logout_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'common',
                'method': 'logout',
                'args': ['database_name', session_id]
            }
        }
        self.client.post('/web/session/destroy', json=logout_payload)

    # Method executed on the start of the user's task execution
    def on_start(self):
        pass
