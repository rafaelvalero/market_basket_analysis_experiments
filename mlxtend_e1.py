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
jupytext --output mlxtend_e1.py mlxtend_e1.ipynb
jupytext --output mlxtend_e1.ipynb mlxtend_e1.py
"""
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd
import subprocess

NAME_NOTEBOOK = 'mlxtend_e1'

# +

# Sample transaction data
dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

dataset

# +
# Encode the transaction data
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

df

# +
# Apply the Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

frequent_itemsets
# -



# +
# Generate association rules
rules = association_rules(frequent_itemsets,
                            metric="lift",
                            min_threshold=1,
                            num_itemsets = dataset.__len__())

rules
# -

# Print the rules
print(rules)

#


orden_to_give = f'jupytext --output {NAME_NOTEBOOK}.py {NAME_NOTEBOOK}.ipynb'
# orden_to_give = f'pwd'
print(orden_to_give)
subprocess.call(orden_to_give, shell=True)


