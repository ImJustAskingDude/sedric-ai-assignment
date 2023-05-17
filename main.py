from src.handlers.recognize import handle


e = {
    "resource": "/recognize",
    "path": "/recognize",
    "httpMethod": "POST",
    "headers": None,
    "multiValueHeaders": None,
    "queryStringParameters": None,
    "multiValueQueryStringParameters": None,
    "pathParameters": None,
    "stageVariables": None,
    "requestContext": {
        "resourceId": "8ueeg5",
        "resourcePath": "/recognize",
        "httpMethod": "POST",
        "extendedRequestId": "FCHoPF8lCGYF2sQ=",
        "requestTime": "16/May/2023:20:50:34 +0000",
        "path": "/recognize",
        "accountId": "093767042774",
        "protocol": "HTTP/1.1",
        "stage": "test-invoke-stage",
        "domainPrefix": "testPrefix",
        "requestTimeEpoch": 1684270234860,
        "requestId": "7dece30d-8e44-46b5-a8b2-0f91f1b4a666",
        "identity": {
            "cognitoIdentityPoolId": None,
            "cognitoIdentityId": None,
            "apiKey": "test-invoke-api-key",
            "principalOrgId": None,
            "cognitoAuthenticationType": None,
            "userArn": "arn:aws:iam::093767042774:root",
            "apiKeyId": "test-invoke-api-key-id",
            "userAgent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0",
            "accountId": "093767042774",
            "caller": "093767042774",
            "sourceIp": "test-invoke-source-ip",
            "accessKey": "ASIARLVHTQ3LD5A2WIK7",
            "cognitoAuthenticationProvider": None,
            "user": "093767042774",
        },
        "domainName": "testPrefix.testDomainName",
        "apiId": "05mg9f9874",
    },
    "body": """{
        "audio_url": "url/for/file.wav",
        "sentences": ["hi my name is joe", "can you hear me?"]
    }""",
    "isBase64Encoded": False,
}

handle(e, None)