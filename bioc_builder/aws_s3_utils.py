import boto3
import os
from typing import List

class BiocBuildDirectory(object):
    def __init__(self, bucket, prefix):
        self.bucket = bucket
        self.prefix = prefix
        self.resource = boto3.resource('s3')
        self.client = boto3.client('s3')
        
    def _get_bucket(self):
        return self.resource.Bucket(self.bucket)

    def _presign(self, key, **kwargs) -> str:
        return self.client.generate_presigned_url(
            'get_object',
            Params = {"Bucket": self.bucket,
                      "Key": key},
            **kwargs)
                                           
    
    def get_all_files(self, jobId) -> List[dict]:
        files = []
        for f in self._get_bucket().objects.filter(Prefix=self.prefix+"/"+jobId):
            stuff = {'name': os.path.basename(f.key),
                     'url': self._presign(f.key)}
            files.append(stuff)
        return(files)
        
        
