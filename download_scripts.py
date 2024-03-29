import json
import os
import time
import requests

"""
I only set it to grab cookies from chrome for logging in..
you may choose otherwise..


NEED TO INSTALL THESE modules here:
"""
import unidecode
import browser_cookie3
import urllib
import alive_progress as ap
from  codecs import decode


"""  SET THIS ? """
overwrite = False


# Get logged in and fetched cookies from Chrome, download indexes of scripts.

############
""" change chrome to whatever if ou user a different browser """
cj = browser_cookie3.chrome()
############

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

login_html = opener.open(
    "https://pine-facade.tradingview.com/pine-facade/list?filter=published"
).read()
published = json.loads(
    requests.get(
        "https://pine-facade.tradingview.com/pine-facade/list?filter=published&last?no_4xx=false",
        cookies=cj,
    ).text
)
saved = json.loads(
    requests.get(
        "https://pine-facade.tradingview.com/pine-facade/list?filter=saved&last?no_4xx=false",
        cookies=cj,
    ).text
)

# only load scripts without compile error "Error: cannot compile script"
saved = [sc for sc in saved if "Error" not in sc["scriptTitle"]]
data = [published, saved]

# split the data apart . if "extra": { "kind": "library" }, then it is a library. and strategy as well separate. the remainder in a third group.
libs = []
strats = []
study = []
rest = []

##  rewrite to do this from data:
for script_sector in data:
    ([libs.append(sc) for sc in script_sector if sc["extra"]["kind"] == "library"])
    ([strats.append(sc) for sc in script_sector if sc["extra"]["kind"] == "strategy"])
    ([study.append(sc) for sc in script_sector if sc["extra"]["kind"] == "study"])
    (
        [
            rest.append(sc)
            for sc in script_sector
            if sc["extra"]["kind"] not in ["library", "study", "strategy"]
        ]
    )
# combine for iterating
sections = [libs, strats, study, rest]

# download functional files
for pct, sector in enumerate(sections):
    names = ["libs", "strats", "study", "rest"]
    with ap.alive_bar(len(sector),calibrate = 5, dual_line = True, theme='smooth') as script_group:
        script_group.title(f"\n\nChecking {names[pct]} scripts")
        for scNum, sc in enumerate(sector):

            # put a 100ms delay
            time.sleep(0.5)
            scriptIdPart = sc["scriptIdPart"]
            version = sc["version"]
            urlpart = f"{scriptIdPart}/{version}"
            sectorname = scriptIdPart.split(";")[0]
            url2part = scriptIdPart.split(";")[-1]
            script_name = sc["scriptName"]
            s = sectorname == "STD"
            u = sectorname == "USER"
            p = sectorname == "PUB"
            script_group()
            good = s or p or u
            if not good:
                continue
            script_group.text(f"Checking {script_name}")
            url = f"https://pine-facade.tradingview.com/pine-facade/get/{urlpart}"
            url2 = (
                f"https://pine-facade.tradingview.com/pine-facade/translate/{urlpart}"
            )

            # for formatting purposes
            invalid = '<>:"/\|?* '

            for char in invalid:
	            script_name = script_name.replace(char, '')

            # using requests to download the pine script with cookies
            r = requests.get(url, cookies=cj)
            r2 = requests.get(url2, cookies=cj)
            if r.status_code != 200:
                script_group.text(f"Error: No Script found for {script_name}")
                continue

            # get the tet from the response
            r = r.text
            r = r.replace(r"\n\n+", r"\n")
            r = json.loads(r)

            # get text of additional information
            r2 = r2.text
            r2 = r2.replace(r"\n\n+", r"\n")
            r2 = r2.encode("utf-8").decode()

            # check if response is valid and contains the 'source' field
            if "source" not in r:
                script_group.text(f"Error: No Source field found for {script_name}")
                continue

            # extract the source from the response
            r = r["source"]
            r = r.replace(r"\n\n+", r"\n")
            r = r.encode("utf-8").decode()#unidecode.unidecode(r)

            # fix name
            script_name = script_name.encode("utf-8").decode()

            # if directory nott exist, create
            if not os.path.exists(f'scripts/{sectorname}/{sc["extra"]["kind"]}/'):
                os.makedirs(f'scripts/{sectorname}/{sc["extra"]["kind"]}/')

            # check if file exists, if not, save the script to file
            if os.path.isfile(
                f'scripts/{sectorname}/{sc["extra"]["kind"]}/{script_name}.pine'
            ):
                if not overwrite:
                    script_group.text(f"{script_name}.pine exists" + "\n")
                    continue
                else:
                    script_group.text(f"Overwriting {script_name}.pine " + "\n")

            with open(
                f'scripts/{sectorname}/{sc["extra"]["kind"]}/{script_name}.pine', "w",
            encoding="utf-8") as f:
                script_group.text(f"{script_name}.pine saved" + "\n")
                f.write(r)
            with open(
                f'scripts/{sectorname}/{sc["extra"]["kind"]}/{script_name}.json', "w",
            encoding="utf-8") as f:
                script_group.text(f"{script_name}.json saved" + "\n")
                f.write(r2)
