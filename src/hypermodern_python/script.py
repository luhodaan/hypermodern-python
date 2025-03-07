from re import L
import requests
import pydantic
from typing import Any, Dict

class LodgingBusiness(pydantic.BaseModel):
    hasNextPage: bool
    nextPageToken: str
    data: Any

def calldiscoverswiss(continuationToken: str ) -> LodgingBusiness:
    url = 'https://api.discover.swiss/info/v2/lodgingbusinesses'
    headers = {'Ocp-Apim-Subscription-Key': 'e69f18d7cf93452c9334f8e3387debfd'}
    if continuationToken != '':
        headers['continuationToken'] = continuationToken

    r = requests.get(url, headers=headers)
    data = r.json()
    return LodgingBusiness(**data)

def main():
    continuationToken = ''
    while True:
        response = calldiscoverswiss(continuationToken)
        if response.hasNextPage:
            continuationToken = response.nextPageToken
        else:
            break
        print(response.data)
    print('Finished')


if __name__ == '__main__':
    main()    