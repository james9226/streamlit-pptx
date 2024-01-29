import streamlit as st
import numpy as np

from src.dashboard.pages.dashboard.data import DATE_COLUMN, load_dashboard_data
from src.powerpoint.ppt import ThemedPresentation


def render_dashboard():
    st.title("Uber pickups in NYC")
    data_load_state = st.text("Loading data...")
    data = load_dashboard_data(100_000)
    data_load_state.text("Done! (using st.cache_data)")

    if st.checkbox("Show raw data"):
        st.subheader("Raw data")
        st.write(data)

    st.subheader("Number of pickups by hour")
    hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
    st.bar_chart(hist_values)

    # Some number in the range 0-23
    hour_to_filter = st.slider("hour", 0, 23, 17)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

    st.subheader("Map of all pickups at %s:00" % hour_to_filter)
    st.map(filtered_data)


def generate_slides(ppt: ThemedPresentation) -> ThemedPresentation:
    data = load_dashboard_data(100_000)
    data["Hour"] = data[DATE_COLUMN].dt.hour
    grpd = data.groupby("Hour", as_index=False).count()
    ppt.add_line_chart(
        data=grpd, x_axis="Hour", y_value="base", y_axis_reference_value=400
    )
    return ppt
