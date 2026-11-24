import requests

class APIClient:
    def __init__(self,base_url,session,timeout=10):
        self.base_url = base_url
        self.timeout = timeout
        self.session = session

    def get(self,endpoint):
        url = f"{self.base_url}/{endpoint.lstrip("/")}"

        response = self.session.get(url,
        timeout=self.timeout)

        return response

    def post(self,endpoint,payload):
        url  = f"{self.base_url}/{endpoint.lstrip("/")}"

        response = self.session.post(
            url,
            data=  payload
        )
        return response


    def put(self,endpoint,payload):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        return self.session.put(
            url,
            json=payload,
            timeout=self.timeout
            )

    def patch(self,endpoint,payload):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        return self.session.patch(
            url,
            json = payload,
            timeout = self.timeout
        )

    def delete(self,endpoint):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        return self.session.delete(
            url,
            timeout= self.timeout
        )


    def close(self):
        self.session.close()