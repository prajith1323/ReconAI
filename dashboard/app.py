import streamlit as st

from modules.whois_lookup import perform_whois_lookup
from modules.subdomain_enum import enumerate_subdomains
from modules.social_scraper import scrape_social_media
from modules.shodan_lookup import perform_shodan_lookup
from modules.ai_analyzer import analyze_with_ai

from utils.report_generator import generate_report
from utils.config_loader import load_config
from utils.logger import setup_logger

# Setup logger
logger = setup_logger()

def main():
    st.set_page_config(page_title="ReconAI - AI-Enhanced OSINT Recon Tool", layout="wide")
    st.title("🔍 ReconAI - AI-Enhanced OSINT Recon Tool")

    config = load_config()

    with st.sidebar:
        st.header("Configuration")
        target = st.text_input("Target Domain/Organization", "example.com")
        
        st.subheader("Modules")
        run_whois = st.checkbox("WHOIS Lookup", value=True)
        run_subdomain = st.checkbox("Subdomain Enumeration", value=True)
        run_social = st.checkbox("Social Media Scraper", value=True)
        run_shodan = st.checkbox("Shodan Lookup", value=True)
        run_ai = st.checkbox("AI Analysis", value=True)

        st.subheader("Reporting")
        report_format = st.selectbox("Report Format", [None, "pdf", "markdown"])
        output_dir = st.text_input("Output Directory", "./reports")

        if st.button("Run Recon"): 
            st.session_state.run_recon = True
            st.session_state.target = target
            st.session_state.modules_to_run = {
                "whois": run_whois,
                "subdomain": run_subdomain,
                "social": run_social,
                "shodan": run_shodan,
                "ai": run_ai
            }
            st.session_state.report_format = report_format
            st.session_state.output_dir = output_dir

    if st.session_state.get("run_recon", False):
        st.subheader(f"Running Recon for: {st.session_state.target}")
        results = {}
        
        if st.session_state.modules_to_run["whois"]:
            with st.spinner("Performing WHOIS lookup..."):
                results["whois"] = perform_whois_lookup(st.session_state.target)
            st.success("WHOIS Lookup Complete!")
            st.json(results["whois"])

        if st.session_state.modules_to_run["subdomain"]:
            with st.spinner("Enumerating subdomains..."):
                results["subdomain"] = enumerate_subdomains(st.session_state.target)
            st.success("Subdomain Enumeration Complete!")
            st.json(results["subdomain"])

        if st.session_state.modules_to_run["social"]:
            with st.spinner("Scraping social media..."):
                results["social"] = scrape_social_media(st.session_state.target)
            st.success("Social Media Scraping Complete!")
            st.json(results["social"])

        if st.session_state.modules_to_run["shodan"]:
            with st.spinner("Performing Shodan lookup..."):
                results["shodan"] = perform_shodan_lookup(st.session_state.target, config.get("SHODAN_API_KEY"))
            st.success("Shodan Lookup Complete!")
            st.json(results["shodan"])

        if st.session_state.modules_to_run["ai"]:
            with st.spinner("Analyzing with AI..."):
                results["ai"] = analyze_with_ai(results, config.get("OPENAI_API_KEY"))
            st.success("AI Analysis Complete!")
            st.json(results["ai"])

        if st.session_state.report_format:
            with st.spinner(f"Generating {st.session_state.report_format} report..."):
                generate_report(st.session_state.target, results, st.session_state.report_format, st.session_state.output_dir)
            st.success(f"{st.session_state.report_format.upper()} Report Generated!")
            st.download_button(
                label=f"Download {st.session_state.report_format.upper()} Report",
                data=open(os.path.join(st.session_state.output_dir, f"{st.session_state.target}_report.{st.session_state.report_format}"), "rb").read(),
                file_name=f"{st.session_state.target}_report.{st.session_state.report_format}",
                mime=f"application/{st.session_state.report_format}"
            )

        st.session_state.run_recon = False # Reset the flag

if __name__ == "__main__":
    main()


