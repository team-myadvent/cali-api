import json
import boto3

from django.conf import settings


def get_youtube_search_results(query):
    client = boto3.client("lambda", region_name=settings.AWS_S3_REGION_NAME)
    payload = {"query": query}

    response = client.invoke(
        FunctionName=settings.AWS_LAMBDA_FUNCTION_NAME,
        InvocationType="RequestResponse",
        Payload=json.dumps(payload),
    )
    videos = json.loads(response["Payload"].read())

    results = []
    for video in videos:
        title = video.get("title", "")
        link = video.get("link", "")
        video_id = link.split("v=")[-1].split("&")[0]
        results.append({"title": title, "link": link, "youtube_video_id": video_id})

    return results
