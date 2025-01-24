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
import numpy as np

NAME_NOTEBOOK = 'fpgrowth_e1'

# Create a SparkSession
spark = SparkSession.builder.appName("MarketBasketAnalysis").getOrCreate()


# +
# Sample transaction data
dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

dataset
# -

# Some transfomations, parsing the data.
# note for fpgrowh basket can only have unique elements.
dataset = list(map(lambda x: (np.unique(x).tolist(),), dataset))
dataset

# # Create a Spark DataFrame
df = spark.createDataFrame(dataset, ["items"])


df.show()

# Apply the FPGrowth algorithm
fpGrowth = FPGrowth(itemsCol="items", 
                    minSupport=0.1, 
                    minConfidence=0.1)
model = fpGrowth.fit(df)


# Display frequent itemsets
model.freqItemsets.show()

output = model.freqItemsets
output.show()

output = output.toPandas()
output

output.to_csv('freqItemasFPgrowth.csv')

# Display generated association rules
output2 = model.associationRules.toPandas()
output2


output2.to_csv('associaton_rules_FPgrowth.csv')

# Saving
orden_to_give = f'jupytext --output {NAME_NOTEBOOK}.py {NAME_NOTEBOOK}.ipynb'
print(orden_to_give)
subprocess.call(orden_to_give, shell=True)

# Stop the SparkSession
spark.stop()



