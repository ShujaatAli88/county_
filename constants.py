from enum import Enum
import os

DATA_DIRECTORY = "tmp"
LOGS_FILE_NAME = "logs.log"
RAW_RESPONSES = os.path.join(DATA_DIRECTORY, "raw_responses")
PDF_DIRECTORY = os.path.join(DATA_DIRECTORY, "pdfs")

os.makedirs(DATA_DIRECTORY, exist_ok=True)
os.makedirs(RAW_RESPONSES, exist_ok=True)
os.makedirs(PDF_DIRECTORY, exist_ok=True)

class CClerkCrawlerConstants(Enum):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0'    ,
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.cclerk.hctx.net',
        'Referer': 'https://www.cclerk.hctx.net/Applications/WebSearch/FRCL_R.aspx',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
    }

    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': 'Page%242',
        '__LASTFOCUS': '',
        '__VIEWSTATE': 'OL/zfT0ZhNig5zto//uSAr682TINVJdjI6sLPP3UAqqRrcajBcZXe4nzPrxbJc3vyzlvPG63/qJppV4C6bjkDtkIK/XD5JsHa2sllsppZ3gGtha19DWkEUphjoVzwoc3+8P2HWItW8/Ien3UUQD0rRtJlFk+WV6ygWz+OcrfhnkZjnLg6zmtGth8Z2Dz55vTmtyJNa8DVQ7J3f2uJaJ/bVPJHX8t+7GnbnPm/Tm82uG8HECgH6oifO2j091xtqMEQdXMG9CjbQQw1AINzEFH6RvOpizsw+Oeg2dAVAl/opHqORj8v8FiHr4kIHw3OyK47RUx6/YL4XUMLcrjJmghcE+vPx2P2KTY/cqqYrsimlWaokxldVMviyAipsijd31Rb3FidwhUHZ15FtUm80IHG7DiEc/w6NXjh3OZ4Vhv+BqjXsgOyNWN/RqTAI6whZq/pFWQWARZNRHpqvBdt4B4N98ErvbNJU97+AqGfH+/MlluT5YmB/WKKJTGQw0bG3in/DC7dsbgMMYfynMjQYbzKRP0Mu+w3befBs5FVJssXu4mPMxvF2UYRA34hJzwAQ2B6sUsAiascvytE6L8Jk86dQ6jAe1k2ii04hj1x6/wB5vysgeAGU4ALKpCwjYrbaJOFwzs4E+rkECKh4XBu4wQn8b1fuUyT+y1Nq0PmaBljcbBeNokD2Pl7bVE6koZRSs0L9k5ylF0Pr66Kp62SKXrmOeWzwc1oORbevb14d45tNA+EG6qv24gKzKetx6o8XVz/F4jAJKbKXNBZBkuIGq7grFbsSzYfGo2iY6/6cno8QYbkiLGFl2h/cf5XyV3grXRzA2zcRhCzx33QU8s+94r7mcMSa/s5ocxJIljeyJgvBUXn02rYmRJqZ4qlvjNqzHVN6n1UFPgWuKwD+cVbtfYRXbDSs0P0clwSv4kwmkwN23nxWLnepOb5+trLqdAC+AuZdXRETDncFqzTjI0cmZzMzKYwrnp73u/1nX445SHv/BqK34fka1qOEU6P3enaldTskD0GRiSAwy2BBJjQG7QzYTBN+GNTS9jpHR4+LJddQjRPmIWKU2hD6+B84aGy/FXZr0GJtjjECyY+nnLc3E39NI/oNvSg9Jnna+T67cx4ZFvlUeGhLD5GRUsFIEaYR/HX3T5prvkte22iRS/4+95axxB8aSym8SKX2g+x/9PMtaBJAIIFlU44fP2Ja+PzT8pmtprQ+Y+pb2ttknAJQNIRj9znffSfbWenun3XVNtZPZLprsOd7zmENHYVeZ9NjDBWyJMhBmIDVfUP9YHg0iBeYgistRMo595uwYiJu4hDUIG3OK6YP/kzHsyW26uy4dnALMsnevGc1GSx4cLbhaQFAQar4L+cGPN1IiowL01n7bmUxVlnMEuTQH29/pe7TGGRswQQ+z18JpBXmgN2TN1X5S/NtMcvG/wkAYDlBCC+ON2smYbnBkZsBK+iyGUkqaPFteVgwMgnRWaX7BD3WEoSyZuje8zWDJh1lMTqx152VzXyyC7QzWqdgwjXUCB18yinswxOQjZrgsh+W2GzCOPS2MPRhNkgRLZzls+K8SnYHL5VioEp4zVSpRr5Tw637o1yzRG/d47vFToz0ZXXMJlSmORtXU+uNtmB7WnMic5r/2hhDhENsemqNSCfvKqNaGIFHfyslHv2xApr7RwqNrZoihp24xkVU+6jG8I8Z2/IsRMH8kdjLzpU+1S3Ycyr4if6ZxaVxLtN8iAtwiqeENZ69JmuKm0iiH5zDNsbgpjitjEkqX/KEOBnkjwZCSwORBRUvP17ZRfOktd4eoxj7VdQrGN0mxBCeQvYu1PDgMwrof7wF8Kao041Z3Wm26/8mQbmBjyrZoNbexiwU9Wl6CoURC2oFzoDgSOXWtLKtcVJa4aoZ1s4AH16vJoGrrXEIQpVrbtTHyj72kBbh+77cvsZA==',
        '__VIEWSTATEGENERATOR': '0AF47E56',
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': 'VQ444t/qM6Au+9LuaIdO2+/HXfJdjIk8WPozuEEPyWbUQO+P4OiQL4kaw5k7MJ2aqoRLtd0DdXAbJ2nN5DV1HDtfgf1wmPe6zIJ728NfhH2KanlUjQwowW9bKo2az1ho2bMZ4lzL3Zu9vONb41E9NWmX0/zEA9FmoZmzCHtOvP/kkJy1Iv1gn07n2IPHmVFYjeMt3tNwpLjr4UfucHQmcZzH+aofLyHPDeHlfFzFQS0BFv3PC3znf6Z0I5pgRTXNabXfAXqQxYMWrc/+SeoE8J7gzPyipBXX+9CjHSpW6S8cXCF9LB36I7t4qsLrhMyw4oSUcrdOapzckxGaKeGR8n+NxVu1HvhKNEnqIEYO3esHCfqzYva6q25XZ+aZkXpD3N5evv3vaqQRGOhLWDMKJfcG1t3DGeJeIgshlsicAeh4IGobnP6LwDhHerQ1qh5HYu2pCIB8UC8j73ePZCzuAh0aGlLaZrM81r5k54lC5fhyuYBzdjQGTr8T1+gh2Jnc/T/y07WhZKdhyt9ofmg0d0jE9nqyuhS8+u1FTyDeVLphLJA/hre5ZzigSkPmqQUYMBqBOmmrLcpVIhojEWzM4CaBwVcasayK94deNO6ky1N5fgox9dVYYYTMgnZoqYKqGvd5OmO2CeD/tRzKZZQuw/WQQqfGhVZciqZlBU7IINLIpunZyRPyEQIpQQ57Mb/pYaEsoPQAptlJ5JnBvwZuQHvuBb3/thhunmiHEFbPqB65UK2XzfR+5yg+0y9/VLZEm/iDMhymXEry9L+LcUGDXONwisvVd3e6nEeSh1fAWhEMqBCVaSnSRxXEUzRxOyyXj/Sfh9iY4ryneaJcr3KkXCysnRsYan7YyfBXle1fvaA=',
        'ctl00$ContentPlaceHolder1$hfSearchType': '0',
        'ctl00$ContentPlaceHolder1$hfViewCopyOrders': 'False',
        'ctl00$ContentPlaceHolder1$hfViewECart': 'False',
        'ctl00$ContentPlaceHolder1$txtFileNo': '',
        'ctl00$ContentPlaceHolder1$rbtlDate': 'SaleDate',
        'ctl00$ContentPlaceHolder1$ddlYear': '2025',
        'ctl00$ContentPlaceHolder1$ddlMonth': '4',
        'ctl00$ContentPlaceHolder1$btnSearch': 'Search',
    }

class AirtableConstants(Enum):
    airtable_name = "c_clerk_data_table"