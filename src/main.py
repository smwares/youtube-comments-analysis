import os
from dotenv import load_dotenv

def main():

    load_dotenv()

    api_key = os.getenv("API_KEY")

    print(api_key != None)


if __name__ == "__main__":
    main()