
# ============================================================
# SMART MANUFACTURING PLATFORM
# Group 8 - MCA Project
# ============================================================

import streamlit as st
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="Smart Manufacturing Platform",
    page_icon="🏭",
    layout="wide"
)

# ------------------------------------------------------------
# DEMO DATA
# ------------------------------------------------------------

MACHINES = [
    "Machine 1",
    "Machine 2",
    "Machine 3",
    "Machine 4",
    "Machine 5"
]

TEMPERATURES = [45, 55, 70, 90, 60]

# Demo operating limits
TEMP_MIN, TEMP_MAX = 20, 80
VIB_MIN, VIB_MAX = 0, 7
PRESS_MIN, PRESS_MAX = 30, 120

# ------------------------------------------------------------
# FAULT DETECTION FUNCTION
# ------------------------------------------------------------

def detect_fault(temperature, vibration, pressure):

    faults = []

    if temperature < TEMP_MIN or temperature > TEMP_MAX:
        faults.append("Abnormal Temperature")

    if vibration < VIB_MIN or vibration > VIB_MAX:
        faults.append("Abnormal Vibration")

    if pressure < PRESS_MIN or pressure > PRESS_MAX:
        faults.append("Abnormal Pressure")

    risk_score = (len(faults) / 3) * 100

    if len(faults) >= 2:
        status = "Critical"
    elif len(faults) == 1:
        status = "Warning"
    else:
        status = "Normal"

    return {
        "status": status,
        "faults": faults,
        "risk_score": round(risk_score, 2)
    }


# ============================================================
# HEADER
# ============================================================

st.title("🏭 Smart Manufacturing Platform")

st.write(
    "An integrated manufacturing monitoring system "
    "for machine health, maintenance and product quality."
)

st.divider()

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🏭 Group 8")
st.sidebar.subheader("Main Menu")

choice = st.sidebar.selectbox(
    "Select Project Module",
    [
        "Dashboard",
        "Machine Fault Detection",
        "Predictive Maintenance",
        "Product Defect Detection",
        "Machine Performance"
    ]
)

st.sidebar.divider()
st.sidebar.info("MCA Project | Group 8")
st.sidebar.caption("Smart Manufacturing Platform")


# ============================================================
# MODULE 1: DASHBOARD
# ============================================================

if choice == "Dashboard":

    st.header("📊 Factory Dashboard")

    st.write("Welcome to the Smart Manufacturing System.")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Machines", "20")
    col2.metric("Working Machines", "16")
    col3.metric("Faulty Machines", "4")
    col4.metric("Efficiency", "85%")

    st.divider()

    st.subheader("Machine Temperature Report")

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.bar(
        MACHINES,
        TEMPERATURES
    )

    ax.set_title("Machine Temperature Monitoring")
    ax.set_xlabel("Machines")
    ax.set_ylabel("Temperature (°C)")
    ax.set_ylim(0, 150)

    ax.axhline(
        y=TEMP_MAX,
        linestyle="--",
        label="Maximum Temperature Limit"
    )

    ax.legend()

    st.pyplot(fig)
    plt.close(fig)

    st.subheader("Machine Status")

    status_col1, status_col2 = st.columns(2)

    with status_col1:
        st.success("16 Machines Working")

    with status_col2:
        st.error("4 Machines Need Attention")

    st.info(
        "Dashboard displays demonstration data "
        "for the academic project."
    )


# ============================================================
# MODULE 2: MACHINE FAULT DETECTION
# ============================================================

elif choice == "Machine Fault Detection":

    st.header("⚙️ Machine Fault Detection")

    st.write(
        "Enter sensor readings to check machine health."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        temperature = st.number_input(
            "Temperature (°C)",
            min_value=0.0,
            max_value=200.0,
            value=45.0
        )

    with col2:
        vibration = st.number_input(
            "Vibration",
            min_value=0.0,
            max_value=20.0,
            value=3.0
        )

    with col3:
        pressure = st.number_input(
            "Pressure",
            min_value=0.0,
            max_value=200.0,
            value=80.0
        )

    if st.button("🔍 Detect Machine Fault", type="primary"):

        result = detect_fault(
            temperature,
            vibration,
            pressure
        )

        st.divider()
        st.subheader("Detection Results")

        c1, c2 = st.columns(2)

        c1.metric(
            "Machine Status",
            result["status"]
        )

        c2.metric(
            "Rule-Based Risk Score",
            str(result["risk_score"]) + "%"
        )

        if result["status"] == "Critical":

            st.error("🚨 Critical Fault Detected!")

        elif result["status"] == "Warning":

            st.warning("⚠️ Warning: Check Machine Condition!")

        else:

            st.success("✅ Machine Operating Normally")

        if result["faults"]:

            st.subheader("Detected Issues")

            for fault in result["faults"]:
                st.write("❌", fault)

        else:

            st.success("No abnormal sensor readings detected.")

        st.caption(
            "Detection uses predefined sensor thresholds, "
            "not a trained machine learning model."
        )


# ============================================================
# MODULE 3: PREDICTIVE MAINTENANCE
# ============================================================

elif choice == "Predictive Maintenance":

    st.header("🔧 Predictive Maintenance")

    st.write(
        "Monitor machine working hours and maintenance schedule."
    )

    machine = st.selectbox(
        "Select Machine",
        MACHINES
    )

    working_hours = st.number_input(
        "Total Working Hours",
        min_value=0,
        max_value=100000,
        value=500,
        step=50
    )

    maintenance_limit = 1000

    remaining = maintenance_limit - working_hours

    col1, col2, col3 = st.columns(3)

    col1.metric("Selected Machine", machine)

    col2.metric(
        "Working Hours",
        str(working_hours)
    )

    col3.metric(
        "Maintenance Interval",
        str(maintenance_limit) + " Hours"
    )

    st.divider()

    progress = min(
        working_hours / maintenance_limit,
        1.0
    )

    st.subheader("Maintenance Progress")

    st.progress(progress)

    if remaining <= 0:

        st.error("🚨 Maintenance Required!")

        st.write(
            "Machine has crossed its maintenance interval."
        )

        st.warning(
            "Please schedule machine servicing immediately."
        )

    elif remaining <= 200:

        st.warning("⚠️ Maintenance Approaching")

        st.write(
            f"{remaining} working hours remaining."
        )

    else:

        st.success("✅ Machine Condition is Normal")

        st.write(
            f"{remaining} working hours remaining "
            "before scheduled maintenance."
        )

    st.caption(
        "This module uses a predefined maintenance interval "
        "for demonstration. It is not a trained predictive model."
    )


# ============================================================
# MODULE 4: PRODUCT DEFECT DETECTION
# ============================================================

elif choice == "Product Defect Detection":

    st.header("🔍 Product Defect Detection")

    st.write(
        "Upload a product image for visual quality inspection."
    )

    uploaded_image = st.file_uploader(
        "Upload Product Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_image is not None:

        st.subheader("Uploaded Product")

        st.image(
            uploaded_image,
            caption="Product Image",
            use_container_width=True
        )

        st.divider()

        st.subheader("Quality Inspection")

        st.write(
            "Inspect the uploaded image and mark any visible defects."
        )

        scratch = st.checkbox("Scratch detected")

        crack = st.checkbox("Crack detected")

        shape_defect = st.checkbox("Shape defect detected")

        color_defect = st.checkbox("Color defect detected")

        if st.button("Submit Quality Inspection", type="primary"):

            defects = []

            if scratch:
                defects.append("Scratch")

            if crack:
                defects.append("Crack")

            if shape_defect:
                defects.append("Shape Defect")

            if color_defect:
                defects.append("Color Defect")

            if defects:

                st.error("❌ Product Rejected")

                st.write("Detected Defects:")

                for defect in defects:
                    st.write("- " + defect)

            else:

                st.success("✅ Product Passed Manual Inspection")

        st.caption(
            "This is manual image inspection. "
            "An automated computer vision model is not yet trained."
        )

    else:

        st.info("Please upload a product image to begin inspection.")


# ============================================================
# MODULE 5: MACHINE PERFORMANCE
# ============================================================

elif choice == "Machine Performance":

    st.header("📈 Machine Performance")

    st.write(
        "Monitor machine efficiency and performance status."
    )

    machine = st.selectbox(
        "Select Machine",
        MACHINES,
        key="performance_machine"
    )

    efficiency = st.slider(
        "Machine Efficiency (%)",
        min_value=0,
        max_value=100,
        value=85
    )

    st.divider()

    col1, col2 = st.columns(2)

    col1.metric(
        "Selected Machine",
        machine
    )

    col2.metric(
        "Machine Efficiency",
        str(efficiency) + "%"
    )

    st.subheader("Performance Analysis")

    fig, ax = plt.subplots(figsize=(8, 3))

    ax.barh(
        ["Efficiency"],
        [efficiency]
    )

    ax.set_xlim(0, 100)

    ax.set_xlabel("Efficiency (%)")

    ax.set_title("Machine Efficiency Report")

    st.pyplot(fig)
    plt.close(fig)

    if efficiency >= 80:

        st.success("✅ Machine Performance is Good.")

    elif efficiency >= 50:

        st.warning("⚠️ Machine Performance is Average.")

    else:

        st.error("❌ Machine Performance is Poor.")


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Smart Manufacturing Platform | Group 8 | MCA Project"
)

st.caption(
    "Developed using Python, Streamlit, NumPy concepts "
    "and Matplotlib."
)
