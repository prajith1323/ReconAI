
import argparse

from modules.whois_lookup import perform_whois_lookup
from modules.subdomain_enum import enumerate_subdomains
from modules.social_scraper import scrape_social_media
from modules.shodan_lookup import perform_shodan_lookup
from modules.ai_analyzer import analyze_with_ai

from utils.report_generator import generate_report
from utils.config_loader import load_config
from utils.logger import setup_logger

def main():
    parser = argparse.ArgumentParser(description="ReconAI - AI-Enhanced OSINT Recon Tool")
    parser.add_argument("--target", required=True, help="Target domain or organization")
    parser.add_argument("--modules", nargs="+


, default=["all"], help="Modules to run (e.g., whois, subdomain, social, shodan, ai)")
    parser.add_argument("--report", choices=["pdf", "markdown"], help="Generate report in specified format")
    parser.add_argument("--output", default="./reports", help="Output directory for reports")

    args = parser.parse_args()

    config = load_config()
    logger = setup_logger()

    logger.info(f"Starting ReconAI for target: {args.target}")

    results = {}

    if "all" in args.modules or "whois" in args.modules:
        logger.info("Running WHOIS lookup...")
        results["whois"] = perform_whois_lookup(args.target)

    if "all" in args.modules or "subdomain" in args.modules:
        logger.info("Running Subdomain enumeration...")
        results["subdomain"] = enumerate_subdomains(args.target)

    if "all" in args.modules or "social" in args.modules:
        logger.info("Running Social media scraping...")
        results["social"] = scrape_social_media(args.target)

    if "all" in args.modules or "shodan" in args.modules:
        logger.info("Running Shodan lookup...")
        results["shodan"] = perform_shodan_lookup(args.target, config.get("SHODAN_API_KEY"))

    if "all" in args.modules or "ai" in args.modules:
        logger.info("Running AI analysis...")
        results["ai"] = analyze_with_ai(results, config.get("OPENAI_API_KEY"))

    if args.report:
        logger.info(f"Generating {args.report} report...")
        generate_report(args.target, results, args.report, args.output)

    logger.info("ReconAI finished.")

if __name__ == "__main__":
    main()


