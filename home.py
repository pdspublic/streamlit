import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "Statistics", "ML"]

def login():

    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()


def logout():
    st.session_state.role = None
    st.rerun()


role = st.session_state.role

logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")
stats_types = st.Page("statistics/stats_types.py", title="Stattistics Types", icon=":material/info:", default=(role == "Statistics"))
multiple_regression = st.Page("statistics/multiple_regression.py", title="Multiple Regression", icon=":material/info:")
logistic_regression = st.Page("statistics/logistic_regression.py", title="Logistic Regression", icon=":material/info:")
non_parametric_test = st.Page("statistics/non_parametric_test.py", title="Non Parametric Test", icon=":material/info:")
parametric_test = st.Page("statistics/parametric_test.py", title="Parametric Test", icon=":material/info:")
simple_regression = st.Page("statistics/simple_regression.py", title="Simple Regression", icon=":material/info:")
outlier_detection = st.Page("ml/outlier_detection.py", title="Outlier Detection", icon=":material/info:", default=(role == "ML"))
ml_1 = st.Page("ml/ml_1.py", title="ml 1", icon=":material/info:")
ml_2 = st.Page("ml/ml_2.py", title="ml 2", icon=":material/info:")

account_pages = [logout_page, settings]
statistics_pages = [stats_types, logistic_regression, multiple_regression, non_parametric_test, parametric_test, simple_regression]
ml_pages = [outlier_detection, ml_1, ml_2]

# st.title("Select Project")
st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

page_dict = {}
if st.session_state.role in ["Statistics"]:
    page_dict["statistics"] = statistics_pages
if st.session_state.role == "ML":
    page_dict["ml"] = ml_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()