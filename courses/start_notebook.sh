#!/bin/sh

rm -rf academy
git clone https://github.com/DatioBD/academy.git
docker run -d -p 8888:8888 -v /root/academy/courses:/home/jovyan/work jupyter/all-spark-notebook start-notebook.sh --NotebookApp.token=''
