# market_basket_analysis_experiments

This is to make some experiments / tutorial about market basket analysis and how to quickly set up and experimental sandbox.

**Set up your docker container with spark and Python:**

```
docker run -it -p 8888:8888  -v /Users/rafaelvalerofernandez/Desktop/repositories/pyspark_works:/home/jovyan/work  quay.io/jupyter/all-spark-notebook
```

This is a Docker command that runs a Jupyter notebook image. Here's a breakdown of the options:

* `-it`: Runs the container in interactive mode with a terminal.
* `-p 8888:8888`: Maps port 8888 inside the container to port 8888 on your host machine. This allows you to access the Jupyter notebook interface through a web browser on your local machine.
* `-v /Users/rafaelvalerofernandez/Desktop/repositories/pyspark_works:/home/jovyan/work`: Mounts your local folder `/Users/rafaelvalerofernandez/Desktop/repositories/pyspark_works` to the `/home/jovyan/work` folder inside the container. This allows you to access your files and work on them inside the Jupyter notebook.
* `quay.io/jupyter/all-spark-notebook`: Specifies the Docker image to use. In this case, it's the Jupyter notebook image from Quay.io.

To install jupytext and mlxtend library: `conda install jupytext mlxtend  -y`

I hope this helps! Let me know if you have any other questions.