import databases
import sqlalchemy
from fastapi import FastAPI
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.config import Config
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from .aws_batch_utils import BatchClient
from .aws_s3_utils import BiocBuildDirectory


templates = Jinja2Templates(directory='templates')

# Config will be read from environment variables and/or ".env" files.
config = Config('.env')
# cast here will wrap username/password in ****** when printed
DATABASE_URL = config('DATABASE_URL', cast=databases.DatabaseURL,
                      default = 'postgresql://localhost:5432/bioc_builder')
JOB_QUEUE = config('JOB_QUEUE', cast=str)
BUCKET = config('BUCKET', default = 'biocbuild.cancerdatasci.org')
PREFIX = config('PREFIX', default = 'jobs')

bioc_build_dir = BiocBuildDirectory(bucket = BUCKET, prefix = PREFIX)

DEBUG = config('DEBUG', cast=bool, default=True)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.debug = DEBUG
app.mount('/static', StaticFiles(directory='static'), name='static')


# Main application code.
database = databases.Database(DATABASE_URL)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.route("/jobs", methods=["GET"])
async def list_jobs(request):
    client=BatchClient(jobQueue=JOB_QUEUE)
    res = client.list_jobs(jobQueue=JOB_QUEUE)
    print(res)
    return templates.TemplateResponse('jobs.html', {'request': request, 'jobs':res})

@app.route('/')
async def homepage(request):
    return templates.TemplateResponse('base.html', {'request': request})

@app.route('/form')
async def submit_job(request):
    if('pkg_repo' not in request.query_params):
        return templates.TemplateResponse('submit.html', {'request': request})
    pkg_repo = request.query_params['pkg_repo']
    wb_repo = "https://github.com/Bioconductor/BiocWorkshops2019"
    wb_local = "bioc_2019"
    client=BatchClient(jobQueue=JOB_QUEUE)
    id = client.submit_job(jobName = 'bioc_build_' + pkg_repo[0:5],
                           jobDefinition = "bioc_builder",
                           parameters = {"book_repo": wb_repo,
                                         "book_path": wb_local,
                                         "pkg_repo":pkg_repo})
    return JSONResponse({"ID":id})

@app.route('/job/{id:str}')
async def show_job(request):
    id = username = request.path_params['id']
    files = bioc_build_dir.get_all_files(id)
    return JSONResponse(files)


@app.route('/job_list')
async def job_list(request):
    client=BatchClient(jobQueue=JOB_QUEUE)
    res = client.list_jobs(jobQueue=JOB_QUEUE)
    return JSONResponse(res)
