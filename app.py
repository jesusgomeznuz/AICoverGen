import os

os.system("pip install ort-nightly-gpu --index-url=https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ort-cuda-12-nightly/pypi/simple/")
os.system("python src/download_models.py")
os.system("python src/webui.py")