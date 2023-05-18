from handlers.aws_lambda.recognize_complete import handle


event = {
    "Records": [
        {
            "EventSource": "aws:sns",
            "EventVersion": "1.0",
            "EventSubscriptionArn": "arn:aws:sns:eu-west-3:093767042774:sedric-ai-stack-RecognizeCompletionTopic-6Z48dl4kw67L:af2a38f5-a5c3-4750-8f70-01cc38c095d2",
            "Sns": {
                "Type": "Notification",
                "MessageId": "abb37517-9c72-5252-94a0-29f738c8ceba",
                "TopicArn": "arn:aws:sns:eu-west-3:093767042774:sedric-ai-stack-RecognizeCompletionTopic-6Z48dl4kw67L",
                "Subject": "Amazon S3 Notification",
                "Message": '{"Records":[{"eventVersion":"2.1","eventSource":"aws:s3","awsRegion":"eu-west-3","eventTime":"2023-05-18T22:11:05.486Z","eventName":"ObjectCreated:Put","userIdentity":{"principalId":"AWS:AROARLVHTQ3LMLIOAFX23:sedric-ai-stack-RecognizeFunction-cIznGz6DqxaL"},"requestParameters":{"sourceIPAddress":"10.0.183.30"},"responseElements":{"x-amz-request-id":"S1JTHTYXZ6QEWGXM","x-amz-id-2":"G+k506124Nsj38Y2WA4reW0OkKDmYaTL6KIBZYe+rKDn/5iKVYo42XWgmygzVl9AXK+40A8mv/9/N3g1XOUc7FT0q0xgG8BO"},"s3":{"s3SchemaVersion":"1.0","configurationId":"ae13b5f0-7b0f-48f9-9831-0c55f4c0d8bc","bucket":{"name":"sedric-transcription-results","ownerIdentity":{"principalId":"A3AKQ9XL0YYTEW"},"arn":"arn:aws:s3:::sedric-transcription-results"},"object":{"key":"3facb9d5-0afd-4a68-bf52-4fefe8fccf93.json","size":2,"eTag":"d751713988987e9331980363e24189ce","sequencer":"006466A27971321ACE"}}}]}',
                "Timestamp": "2023-05-18T22:11:06.873Z",
                "SignatureVersion": "1",
                "Signature": "mX0mhOD4XjwrvLBx5tGiFWwU9Ipv05CWz7dnBAcrca1+v1QxN/yM1AhoHouIIm6ERnvHDlRWVyaDD71ZoKDywIYVJG/W3H08Gm+4ZnqS2q60j6aFpE0CzKq1pjS/1IuWfvYX/qeB0JVGH0bQpDD8dutnkOLjEWpai0Mf3zwsY4AnsoClXPdvJcb3rkMqghkw0HHB32HDud5+n/RDJwowk2TFBNqi9JBon5wgBozxj/tbo0G4xUPiLL5jhhs9JCmwAHn4afVXiFSgH0MJnLou2qWJBOUdwJjw4TDnw7AVUC+zFhUXLTNw+44jMp3U7SSMXHguWqE3xc7CHRDI8GsyZg==",
                "SigningCertUrl": "https://sns.eu-west-3.amazonaws.com/SimpleNotificationService-01d088a6f77103d0fe307c0069e40ed6.pem",
                "UnsubscribeUrl": "https://sns.eu-west-3.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:eu-west-3:093767042774:sedric-ai-stack-RecognizeCompletionTopic-6Z48dl4kw67L:af2a38f5-a5c3-4750-8f70-01cc38c095d2",
                "MessageAttributes": {},
            },
        }
    ]
}

handle(event, None)
