import os
import numpy as np
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
from googleapiclient.discovery import build


def main():

    load_dotenv()

    api_key = os.getenv("API_KEY")

    print(api_key != None)


if __name__ == "__main__":
    main()