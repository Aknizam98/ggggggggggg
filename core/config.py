from os import getenv
from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv('TOKEN')
ADMIN_USERID = getenv('ADMIN_USERID')

PGHOST = getenv('PGHOST')
PGDATABASE = getenv('PGDATABASE')
PGUSER = getenv('PGUSER')
PGPASSWORD = getenv('PGPASSWORD')
PGPORT = getenv('PGPORT')

URL = getenv("URL")
DOMAIN = getenv("DOMAIN")
HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
}