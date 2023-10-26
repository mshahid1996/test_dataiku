# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Sept_Task = dataiku.Dataset("Sept_Task")
Sept_Task_df = Sept_Task.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test2_df = Sept_Task_df # For this sample code, simply copy input to output


# Write recipe outputs
test2 = dataiku.Dataset("test2")
test2.write_with_schema(test2_df)
