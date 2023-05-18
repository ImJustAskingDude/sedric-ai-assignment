import jsons
from data_transfer.aws_event_sns import AwsEventSns


aws_event_sns = {
    "Records": [
        {
            "EventSource": "aws:sns",
            "EventVersion": "1.0",
            "EventSubscriptionArn": "arn:aws:sns:eu-west-3:093767042774:sedric-ai-stack-RecognizeCompletionTopic-6Z48dl4kw67L:af2a38f5-a5c3-4750-8f70-01cc38c095d2",
            "Sns": {
                "Type": "Notification",
                "MessageId": "b0427a21-d53e-5c75-bbf7-26c14af11a38",
                "TopicArn": "arn:aws:sns:eu-west-3:093767042774:sedric-ai-stack-RecognizeCompletionTopic-6Z48dl4kw67L",
                "Subject": "Amazon S3 Notification",
                "Message": '{"Records":[{"eventVersion":"2.1","eventSource":"aws:s3","awsRegion":"eu-west-3","eventTime":"2023-05-18T21:50:06.159Z","eventName":"ObjectCreated:Put","userIdentity":{"principalId":"A3AKQ9XL0YYTEW"},"requestParameters":{"sourceIPAddress":"10.0.112.34"},"responseElements":{"x-amz-request-id":"BNZCC79RD2WX9JQ9","x-amz-id-2":"vDNGqvc6kxdrIsImvs02GDCXbcTVnmKXSm5yDTeNbGlhfeQEpl/xLT0WRqJCv1Dx5I2lOamhzgJZYYuf0Whw6aiSf/ysj7ud"},"s3":{"s3SchemaVersion":"1.0","configurationId":"ae13b5f0-7b0f-48f9-9831-0c55f4c0d8bc","bucket":{"name":"sedric-transcription-results","ownerIdentity":{"principalId":"A3AKQ9XL0YYTEW"},"arn":"arn:aws:s3:::sedric-transcription-results"},"object":{"key":".write_access_check_file.temp","size":2,"eTag":"d751713988987e9331980363e24189ce","sequencer":"0064669D8E227930B6"}}}]}',
                "Timestamp": "2023-05-18T21:50:07.467Z",
                "SignatureVersion": "1",
                "Signature": "GaJ45eJ3nD3fMlq2Bpx6VoOeo3/DU1tagwn6zyis7/QYLQswROXdLQyn+YQispLcOfgZshVEDXDfY3mdVLMPuGExrsYAKRpwSgcDJo9hafDP/lBJTEbgBcpP7JTSDXTveQpyZAea4siapLKwc9Cv0O+WAS0a4o7Oah0iUWrPIpmxG99B+eHPH2bA4q7UQS2nUIwW/cytIii+4c20hlcrXdOW1csp3ALe3laL94ioz+hGzEvykEQf86EqUnNcPeEVzJZWNd8TLMhZ3ug/pZfPDtFxt9G+J5rsS6Qo9qhrgyV/Oeo7PKAx6O90j9JkLzRbiM1w2IKa+4s1IJecPGM9cg==",
                "SigningCertUrl": "https://sns.eu-west-3.amazonaws.com/SimpleNotificationService-01d088a6f77103d0fe307c0069e40ed6.pem",
                "UnsubscribeUrl": "https://sns.eu-west-3.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-west-3:093767042774:sedric-ai-stack-RecognizeCompletionTopic-6Z48dl4kw67L:af2a38f5-a5c3-4750-8f70-01cc38c095d2",
                "MessageAttributes": {},
            },
        }
    ]
}

aws_event = jsons.load(aws_event_sns, AwsEventSns)
print(aws_event)