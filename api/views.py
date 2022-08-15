from xml.dom.pulldom import parseString
from django.shortcuts import render
from django.http import JsonResponse
from cam_viewer.settings import BASE_DIR
import os

# Create your views here.
def list_files(request):
    # Get list of files and directories
    print(f"Current path: {os.getcwd()}")

    sub_path = request.GET["path"] if request.GET.get("path") else "Videos"

    os.chdir(os.path.join(BASE_DIR, sub_path))
    files = filter(os.path.isfile, os.listdir())
    file_sizes = [(f, os.stat(f).st_size) for f in files]
    directories = list(filter(os.path.isdir, os.listdir()))

    answer = {
        "current_dir": os.getcwd(),
        "directories": directories,
        "files": file_sizes,
    }
    return JsonResponse(
        answer,
    )


def schedule_recording(request):
    pass
