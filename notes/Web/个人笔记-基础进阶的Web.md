# 脚本库

## 爬虫

### 1. 同步

#### 1.1 requests

```python
import requests
import fake_useragent
from requests import Response

request = requests

"""
Sync Get By Request
:param uri uri
:param params params
:param data data
:param headers headers
:return response | None
"""
def getByRequests(
        uri: str,
        params: dict | None = None,
        data: dict | None = None,
        headers: dict | None = None
) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return request.get(
        url=uri,
        params=params,
        data=data,
        headers = headers
    )

"""
Sync Post By Request
:param uri uri
:param params params
:param data data
:param headers headers
:return response | None
"""
def postByRequests(
        uri: str,
        data: dict | None = None,
        params: dict | None = None,
        headers: dict | None = None
) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return request.post(
        url=uri,
        params=params,
        data=data,
        headers=headers
    )
```

#### 1.2 session

```python
import requests
import fake_useragent
from requests import Response

session = requests.Session()

"""
Sync Get By Session
:param uri uri
:param params params
:param data data
:param headers headers
:return response | None
"""
def getBySession(
        uri: str,
        params: dict | None = None,
        data: dict | None = None,
        headers: dict | None = None
) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return session.get(
        url=uri,
        params=params,
        data=data,
        headers=headers
    )

"""
Sync Post By Session
:param uri uri
:param params params
:param data data
:param headers headers
:return response | None
"""
def postBySession(
        uri: str,
        data: dict | None = None,
        params: dict | None = None,
        headers: dict | None = None
) -> Response:
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}
    return session.post(
        url=uri,
        params=params,
        data=data,
        headers=headers
    )
```

### 2. 异步

```python
import aiohttp
import fake_useragent
from aiohttp import ClientError, ClientResponse, ClientTimeout

"""
Async Get By Session
:param uri uri
:param params params
:param data data
:param headers headers
:param session session
:param timeout timeout
:param attempts attempts
:return: response | None
"""
async def async_get(
        uri: str,
        params: dict | None = None,
        data: dict | None = None,
        headers: dict | None = None,
        session: aiohttp.ClientSession = None,
        timeout: int = 60,
        attempts: int = 10
) -> ClientResponse | None:
    
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}

    if session is not None:
        for attempt in range(attempts):
            try:
                async with session.get(
                        url=uri,
                        params=params,
                        data=data,
                        headers=headers,
                        timeout=ClientTimeout(total=timeout)
                ) as response:
                    response._body = await response.read()
                    response._body_cache = True
                    return response
            except ClientError as clientError:
                if attempt + 1 == attempts:
                    print(f"{clientError}")

    else:
        async with aiohttp.ClientSession() as clientSession:
            for attempt in range(attempts):
                try:
                    async with clientSession.get(
                            url=uri,
                            params=params,
                            data=data,
                            headers=headers,
                            timeout=ClientTimeout(total=timeout)
                    ) as response:
                        response._body = await response.read()
                        response._body_cache = True
                        return response
                except ClientError as clientError:
                    if attempt + 1 == attempts:
                        print(f"{clientError}")

    return None

"""
Async Post By Session
:param uri uri
:param params params
:param data data
:param headers headers
:param session session
:param timeout timeout
:param attempts attempts
:return: response | None
"""
async def async_post(
        uri: str,
        params: dict | None = None,
        data: dict | None = None,
        headers: dict | None = None,
        session: aiohttp.ClientSession = None,
        timeout: int = 60,
        attempts: int = 10
) -> ClientResponse | None:
    
    if headers is None: headers = {"User-Agent": fake_useragent.UserAgent().random}

    if session is not None:
        for attempt in range(attempts):
            try:
                async with session.post(
                        url=uri,
                        params=params,
                        data=data,
                        headers=headers,
                        timeout=ClientTimeout(total=timeout)
                ) as response:
                    response._body = await response.read()
                    response._body_cache = True
                    return response
            except ClientError as clientError:
                if attempt + 1 == attempts:
                    print(f"{clientError}")

    else:
        async with aiohttp.ClientSession() as clientSession:
            for attempt in range(attempts):
                try:
                    async with clientSession.post(
                            url=uri,
                            params=params,
                            data=data,
                            headers=headers,
                            timeout=ClientTimeout(total=timeout)
                    ) as response:
                        response._body = await response.read()
                        response._body_cache = True
                        return response
                except ClientError as clientError:
                    if attempt + 1 == attempts:
                        print(f"{clientError}")

    return None
```

