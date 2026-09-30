def call_partner_api():
    api_key = os.environ["API_TOKEN"]
    headers = {"Authorization": f"Bearer {api_key}"}
    return headers
