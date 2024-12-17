import json
import os
import time
import requests
import unidecode
import browser_cookie3
import urllib
from alive_progress import alive_bar
from typing import List, Dict, Any

# Configuration
OVERWRITE = False
BROWSER = "chrome"  # Change if using a different browser

# Constants for script categories
SCRIPT_CATEGORIES = ["library", "strategy", "study"]

# Base URL for API endpoints
API_BASE_URL = "https://pine-facade.tradingview.com/pine-facade/"

# -- Data Acquisition and Processing --

def fetch_script_data(filter_type: str, cj: Any) -> List[Dict[str, Any]]:
    """Fetches script metadata from the TradingView API."""
    url = f"{API_BASE_URL}list?filter={filter_type}"
    if filter_type != "published":
        url += "&last?no_4xx=true"
    response = requests.get(url, cookies=cj)
    return json.loads(response.text)

def categorize_scripts(data: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Categorizes scripts based on their 'kind' attribute."""
    categorized_scripts: Dict[str, List[Dict[str, Any]]] = {
        category: [] for category in SCRIPT_CATEGORIES
    }
    categorized_scripts["rest"] = []

    for script_sector in data:
        for script in script_sector:
            kind = script["extra"].get("kind")
            if kind in SCRIPT_CATEGORIES:
                categorized_scripts[kind].append(script)
            else:
                categorized_scripts["rest"].append(script)
    return categorized_scripts

# -- Script Download and Storage --

def sanitize_filename(filename: str) -> str:
    """Removes invalid characters from a filename."""
    invalid_chars = '<>:"/\\|?* '
    return "".join(char for char in filename if char not in invalid_chars)

def download_script(
    script_id_part: str, version: str, script_name: str, sector_name: str, kind: str, cj: Any
) -> bool:
    """Downloads a script and its metadata, returning True if successful."""
    url = f"{API_BASE_URL}get/{script_id_part}/{version}"
    url2 = f"{API_BASE_URL}translate/{script_id_part}/{version}"

    script_name = sanitize_filename(script_name)

    r = requests.get(url, cookies=cj)
    r2 = requests.get(url2, cookies=cj)

    if r.status_code != 200:
        return False

    script_data = json.loads(r.text)
    metadata = r2.text.encode("utf-8").decode()

    if "source" not in script_data:
        return False

    script_source = script_data["source"].encode("utf-8").decode()

    directory = f"scripts/{sector_name}/{kind}/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    script_filepath = f"{directory}{script_name}.pine"
    metadata_filepath = f"{directory}{script_name}.json"

    if os.path.isfile(script_filepath) and not OVERWRITE:
        return True

    with open(script_filepath, "w", encoding="utf-8") as f:
        f.write(script_source)
    with open(metadata_filepath, "w", encoding="utf-8") as f:
        f.write(metadata)

    return True

# -- Main Execution Logic --

def main():
    """Main function to orchestrate script download."""
    cj = getattr(browser_cookie3, BROWSER)()
    
    # -- Data Fetching and Categorization --

    filters = ["published", "saved", "standard"]
    
    script_metadata = [
        fetch_script_data(filter_type, cj)
        for filter_type in filters
        if "Error: cannot compile script"
        not in fetch_script_data(filter_type, cj)
    ]

    categorized_scripts = categorize_scripts(script_metadata)

    # -- Script Downloading with Progress Tracking --
    
    for category, scripts in categorized_scripts.items():
        with alive_bar(
            len(scripts), calibrate=5, dual_line=True, theme="smooth"
        ) as bar:
            bar.title(f"\n\nChecking {category} scripts")
            for script in scripts:
                time.sleep(0.01)
                script_id_part = script["scriptIdPart"]
                version = script["version"]
                sector_name = script_id_part.split(";")[0]
                
                # -- Filter Script Types --
                
                is_valid_sector = sector_name in ["STD", "USER", "PUB"]
                if not is_valid_sector:
                    bar()
                    continue

                bar.text(f"Checking {script['scriptName']}")
                success = download_script(
                    script_id_part,
                    version,
                    script["scriptName"],
                    sector_name,
                    category,
                    cj,
                )
                
                # -- Conditional Logging for Errors --
                
                if not success:
                    bar.text(f"Error downloading {script['scriptName']}")
                bar()

if __name__ == "__main__":
    main()
