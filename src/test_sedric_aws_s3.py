from services.sedric_aws_s3 import SedricAwsS3
from utils.collection_utils import get_first


sedric_aws_s3 = SedricAwsS3()

transcription = sedric_aws_s3.get_transcription(
    request_id="18ff38cb-7f9d-46a9-b43e-da06676934bd"
)
transcription_results = transcription.results
transcription_text = get_first(transcription_results.transcripts)

print(transcription_text)