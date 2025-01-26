# market_basket_analysis_experiments

This is to make some experiments / tutorial about market basket analysis and how to quickly set up and experimental sandbox.

Here [youtube video tutorial](https://youtu.be/LR8k86NL1MA)

# FPgrowth alternatives

Choose Python (mlxtend) if:


* You're working with a smaller dataset.
* You're comfortable with Pandas DataFrames.
* You need more flexibility and control over the analysis.
* You prefer a simpler learning curve.

Choose PySpark (pyspark.ml.fpm) if:

* You have a large dataset that requires distributed computing.
* You need high performance and efficiency.
* You're familiar with Spark and its ecosystem.
* You prioritize scalability for future growth.


Remember that these are general guidelines. The best choice depends on your specific needs, dataset size, available resources, and familiarity with the tools.



 Feature | Python (mlxtend) | PySpark (pyspark.ml.fpm) |
|---|---|---|
| Scalability | Suitable for small to medium datasets | Designed for large datasets with distributed computing |
| Performance | Can be slower for very large datasets | Generally faster and more efficient for large datasets |
| Algorithm | Apriori (default), FP-growth also available | FP-growth |
| Data Structure | Pandas DataFrame | Spark DataFrame |
| Implementation | Relatively straightforward | Requires understanding of Spark concepts (like SparkSession, DataFrames) |
| Flexibility | Offers more flexibility for data manipulation and customization | More structured approach with predefined functions |
| Learning Curve | Easier to learn for beginners | Steeper learning curve due to Spark concepts |
| Environment | Single machine | Distributed computing cluster |
| Memory Usage | Can become memory-intensive for large datasets | Distributes memory usage across the cluster |
| Libraries | mlxtend | pyspark.ml.fpm |


# Set up your docker container with spark and Python:**

```
docker run -it -p 8888:8888  -v /Users/rafaelvalerofernandez/Desktop/repositories/pyspark_works:/home/jovyan/work  quay.io/jupyter/all-spark-notebook
```

This is a Docker command that runs a Jupyter notebook image. Here's a breakdown of the options:

* `-it`: Runs the container in interactive mode with a terminal.
* `-p 8888:8888`: Maps port 8888 inside the container to port 8888 on your host machine. This allows you to access the Jupyter notebook interface through a web browser on your local machine.
* `-v /Users/rafaelvalerofernandez/Desktop/repositories/pyspark_works:/home/jovyan/work`: Mounts your local folder `/Users/rafaelvalerofernandez/Desktop/repositories/pyspark_works` to the `/home/jovyan/work` folder inside the container. This allows you to access your files and work on them inside the Jupyter notebook.
* `quay.io/jupyter/all-spark-notebook`: Specifies the Docker image to use. In this case, it's the Jupyter notebook image from Quay.io.

Pick up the address and open it in your browser.

To install jupytext and mlxtend library: `conda install jupytext mlxtend  -y` in a terminal in your browser.

I hope this helps! Let me know if you have any other questions.

## Donwload the repository

```
git clone https://github.com/rafaelvalero/market_basket_analysis_experiments.git
```

## Run the notebooks
You may need first to create the notebooks from the .py files:
```
jupytext --output mlxtend_e1.ipynb mlxtend_e1.py
jupytext --output fpgrowth_e1.ipynb fpgrowth_e1.py
```




