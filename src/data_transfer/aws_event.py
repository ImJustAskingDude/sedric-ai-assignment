from dataclasses import dataclass
from enum import Enum
from types import NoneType


class HttpMethod(Enum):
    POST = "POST"
    GET = "GET"


@dataclass(frozen=True)
class AwsEventRequestContextIdentity:
    cognitoIdentityPoolId: NoneType
    cognitoIdentityId: NoneType
    apiKey: str
    principalOrgId: NoneType
    cognitoAuthenticationType: NoneType
    userArn: str
    apiKeyId: str
    userAgent: str
    accountId: str
    caller: str
    sourceIp: str
    accessKey: str
    cognitoAuthenticationProvider: NoneType
    user: str


@dataclass(frozen=True)
class AwsEventRequestContext:
    resourceId: str
    resourcePath: HttpMethod
    extendedRequestId: str
    requestTime: str
    path: str
    accountId: str
    protocol: str
    stage: str
    domainPrefix: str
    requestTimeEpoch: int
    requestId: str
    identity: AwsEventRequestContextIdentity
    domainName: str
    apiId: str


@dataclass(frozen=True)
class AwsEvent:
    resource: str
    path: str
    httpMethod: HttpMethod
    headers: NoneType
    multiValueHeaders: NoneType
    queryStringParameters: NoneType
    multiValueQueryStringParameters: NoneType
    pathParameters: NoneType
    stageVariables: NoneType
    body: str
    isBase64Encoded: bool
