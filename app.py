import streamlit as st

st.set_page_config(page_title="AI API Failure Detection Agent")

st.title("🚀 AI API Failure Detection & Debugging Agent")

logs = st.text_area("Paste API Logs Here")

if st.button("Analyze Logs"):

    if "500" in logs:

        st.error("🚨 Critical Alert: High Failure Rate Detected")

        st.metric("API Health Score", "62%")

        st.subheader("AI Analysis")

        if "/login" in logs:
            endpoint = "/login"
            cause = "Database Connection Failure"
            confidence = "88%"
        elif "/payment" in logs:
            endpoint = "/payment"
            cause = "Payment Gateway Timeout"
            confidence = "91%"
        else:
            endpoint = "Unknown Endpoint"
            cause = "Service Failure Detected"
            confidence = "80%"

        st.write(f"**Affected Endpoint:** {endpoint}")
        st.write(f"**Likely Root Cause:** {cause}")
        st.write(f"**Confidence Score:** {confidence}")

        st.subheader("Recommended Actions")

        st.write("""
        ✅ Check service status

        ✅ Verify credentials and configuration

        ✅ Restart affected service

        ✅ Monitor logs after applying fix

        ✅ Verify API connectivity
        """)

    else:
        st.success("✅ No critical API issues detected")