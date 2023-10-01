#!/usr/bin/python3
"""This is a script that fetches https://alx-intranet.hbtn.io/status.
making use of the requests package.
"""
import requests


if __name__ == "__main__":
    with (
        requests.get('https://alx-intranet.hbtn.io/status')
    ) as response:
        content = response.text
        formatted_output = (
            "Body response:\n"
            "\t- type: {}\n"
            "\t- content: {}"
        ).format(type(content), content)
        print(formatted_output)
