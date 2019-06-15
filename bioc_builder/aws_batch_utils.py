import boto3
from typing import List

JOB_STATUS=("SUBMITTED",
           "PENDING",
           "RUNNABLE",
           "STARTING",
           "RUNNING",
           "SUCCEEDED",
           "FAILED")

class BatchClient(object):
    def __init__(self, jobQueue):
        self.client = boto3.client('batch')
        self.jobQueue = jobQueue

    def get_client(self):
        return self.client

    def list_jobs(self, job_status=JOB_STATUS, **kwargs):
        jobs = []
        for s in job_status:
            res = self.client.list_jobs(jobStatus=s, **kwargs)
            if('jobSummaryList' in res):
                jobs = jobs + res['jobSummaryList']
        return jobs

    def describe_job_queues(self, **kwargs):
        return self.client.describe_job_queues(**kwargs)


    def describe_jobs(self, jobs):
        if(len(jobs)>99):
            raise Exception('not good')
        return self.client.describe_jobs(jobs=jobs)
    

    def describe_job(self, job):
        return self.describe_jobs([job])


    def submit_job(self, jobName: str,
                   jobDefinition: str, **kwargs):
        
        return self.client.submit_job(
            jobName=jobName,
            jobQueue=self.jobQueue,
            jobDefinition=jobDefinition,
            **kwargs)['jobId']

    def describe_job_definitions(self, **kwargs):
        return self.client.describe_job_definitions(**kwargs)

