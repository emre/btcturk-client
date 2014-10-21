
def authenticated_method(func):
    def _decorated(self, *args, **kwargs):
        if not self.api_key:
            raise ValueError("you need to set your API KEY for this method.")

        response = func(self, *args, **kwargs)

        if response.status_code == 401:
            raise ValueError("invalid private/public key for API.")

        return response.json()

    return _decorated