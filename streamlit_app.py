import os
os.environ["MPLBACKEND"] = "Agg"

import pandas as pd
import matplotlib
matplotlib.use("Agg", force=True)
import streamlit as st

st.set_page_config(page_title="AI Cockpit Dashboard", layout="wide")
st.title("AI Cockpit for a Manufacturing Line")
st.markdown("Bringing together predictive maintenance and analytics.")
