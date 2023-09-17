import requests

def get_uv_sun_info(lat, lng, alt, dt, token):
    print("[INFO] Preparing to send GET request to OpenUV API...")

    url = f"https://api.openuv.io/api/v1/uv?lat={lat}&lng={lng}&alt={alt}&dt={dt}"

    headers = {
        'x-access-token': token,
    }

    response = requests.request("GET", url, headers=headers)

    if response.status_code != 200:
        print("[ERROR] Request failed.")
        print(f"Status code: {response.status_code}")
        print(f"Response content: {response.content}")
        return None

    print("[INFO] Request succeeded, processing data...")

    data = response.json()

    info = {
        "uv": data['result']['uv'],
        "sunrise": data['result']['sun_info']['sun_times']['sunrise'],
        "sunset": data['result']['sun_info']['sun_times']['sunset']
    }

    print("[INFO] Data processed successfully, returning result...")
    return info

# remember to pass lat, lng, alt, dt and your token
info = get_uv_sun_info(25.80, -80.13, 100, '', 'openuv-p1f4orlmnbkmr2-io')
print(info)
