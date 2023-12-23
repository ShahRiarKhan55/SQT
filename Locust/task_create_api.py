from locust import HttpUser, task, between

# Define a Locust user class for project scalability testing
class OdooProjectScalabilityUser(HttpUser):
    # Set wait time between tasks
    wait_time = between(2, 5)

    # Task to create a project task
    @task
    def create_task(self):
        # Payload for logging in
        login_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'common',
                'method': 'login',
                'args': ['database_name', 'username', 'password']
            }
        }

        # Send a POST request to authenticate and get the session ID
        response = self.client.post('/web/session/authenticate', json=login_payload)
        session_id = response.json()['result']['session_id']

        # Payload to create a project task
        create_task_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'object',
                'method': 'execute',
                'args': ['database_name', session_id, 'password', 'project.task', 'create', {
                    'name': 'New Task', 
                    'project_id': 1, 
                }]
            }
        }

        # Send a POST request to create a project task
        self.client.post('/web/dataset/call_kw/project.task/create', json=create_task_payload)

        # Payload for logging out and destroying the session
        logout_payload = {
            'jsonrpc': '2.0',
            'method': 'call',
            'params': {
                'service': 'common',
                'method': 'logout',
                'args': ['database_name', session_id]
            }
        }

        # Send a POST request to logout and destroy the session
        self.client.post('/web/session/destroy', json=logout_payload)

    # Method executed on the start of the user's task execution
    def on_start(self):
        pass
