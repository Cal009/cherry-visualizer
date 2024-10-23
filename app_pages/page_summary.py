import streamlit as st

def page_summary():
    st.write("### Project Summary")

    st.info(
        f"** General Information**\n"
        f"* The powdery mildew that can be found on cherry tree's is caused by the fungus Podosphaera clandestina.\n"
        f"* This fungus can easily be spread by insects or wind pushing the fungus spores airborn\n"
        f"* The process for manually identifying these trees can be very tedious and time consuming for the business\n"
        f"* Multiple samples are collected via hand from the trees, assessed and then if"
        f" necessary a compound is applied to the diseased tree, aiming to kill the fungus."
    )

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf"
        f" that is healthy from one that contains powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry tree is healthy or contains powdery mildew. "
        )