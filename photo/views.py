from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
import boto3
from botocore.client import Config
from photo.models import Photo

@login_required
def fetch(request, photoid):
    s3 = boto3.resource('s3')
    
    try:
        photo = Photo.objects.get(owner=request.user, pk=photoid)
        key = photo.name
        filetype = photo.filetype
    except Exception as e:
        return HttpResponse('No photo')
    
    try:    
        obj = s3.Object(settings.AWS_STORAGE_BUCKET_NAME, key)
        file_byte_string = obj.get()['Body'].read()
        return HttpResponse(file_byte_string, content_type='image/'+filetype)
    except Exception as e:
        return HttpResponse('No photo on cloud')

@login_required
def upload(request):
    s3_client = boto3.client(
        's3',
        aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
        config = Config(signature_version='s3v4'),
        region_name = settings.AWS_DEFAULT_REGION
    )
    with open("my_local_image.jpg", "rb") as f:
        response = s3_client.upload_fileobj(f, settings.AWS_STORAGE_BUCKET_NAME, 'mypicture.png')