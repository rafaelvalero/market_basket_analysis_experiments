# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

"""_summary_
jupytext --output fpgrowth_e1.py fpgrowth_e1.ipynb
jupytext --output fpgrowth_e1.ipynb fpgrowth_e1.py
"""
from pyspark.sql import SparkSession
from pyspark.ml.fpm import FPGrowth
import pandas as pd
import subprocess

NAME_NOTEBOOK = 'fpgrowth_e1'

# Create a SparkSession
spark = SparkSession.builder.appName("MarketBasketAnalysis").getOrCreate()


# +
# Sample transaction data
dataset = [(['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],),
           (['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],),
           (['Milk', 'Apple', 'Kidney Beans', 'Eggs'],),
           (['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],),
           (['Corn', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs'],)]

dataset

# +
# dataset = [['Milk', 'Onion'],
#            ['Dill']]

# dataset

# +
# df = spark.createDataFrame(dataset)
# df.show()

# +
# from pyspark.sql.types import ArrayType, StringType

# # Sample data with arrays of different lengths
# data = [
#     (["apple", "banana", "cherry"],),
#     (["orange", "grape"],),
#     (["watermelon"],),
#     (["pineapple", "mango", "papaya", "kiwi"],)
# ]

# # Define the schema
# schema = ArrayType(StringType())

# # Create a DataFrame
# df = spark.createDataFrame(data, ["fruits"])

# # Show the DataFrame
# df.show(truncate=False)
# -





# +
# input_spark_df = list(map(lambda x: (', '.join(x),), dataset))
# input_spark_df

# +
# df = spark.createDataFrame(dataset,\
#                            ["items"])
# df.show()

# +
# # Create a Spark DataFrame
# df = spark.createDataFrame([('milk, onion',),\
#                             ('milk, onion',)],\
#                            ["items"])
# df.show()

# +
# # Sample data
# data = [
#     ("Alice", 25),
#     ("Bob", 30),
#     ("Charlie", 35)
# ]

# # Create a DataFrame
# df = spark.createDataFrame(data, ["Name", "Age"])
# df.show()

# +
# # Sample transaction data
# data = [
#     ["Milk", "Onion", "Nutmeg", "Kidney Beans", "Eggs", "Yogurt"],
#     ["Dill", "Onion", "Nutmeg", "Kidney Beans", "Eggs", "Yogurt"],
#     ["Milk", "Apple", "Kidney Beans", "Eggs"],
#     ["Milk", "Unicorn", "Corn", "Kidney Beans", "Yogurt"],
#     ["Corn", "Onion", "Onion", "Kidney Beans", "Ice cream", "Eggs"],
# ]

# # Create a Spark DataFrame
df = spark.createDataFrame(dataset, ["items"])

# -

df.show()

# Apply the FPGrowth algorithm
fpGrowth = FPGrowth(itemsCol="items", minSupport=0.6, minConfidence=0.6)
model = fpGrowth.fit(df)


# Display frequent itemsets
model.freqItemsets.show()

# Display generated association rules
model.associationRules.show()







#


orden_to_give = f'jupytext --output {NAME_NOTEBOOK}.py {NAME_NOTEBOOK}.ipynb'
# orden_to_give = f'pwd'
print(orden_to_give)
subprocess.call(orden_to_give, shell=True)

# Stop the SparkSession
spark.stop()

