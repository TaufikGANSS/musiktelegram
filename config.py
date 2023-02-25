from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("1BVtsOLABuzhXHd3R3C2E-2tblAkS5JyU0LRHhWhSyTZKtINGe0xLs4YyBiSSBvY0xmdX7pjsjCeMa1Ph6vixYQFJCkkiBC92FfUl3Ls0q97PqKtbkj4uzcLkj_4sByYYbCdoJFWHfwnP4Rbl4V503lPH8EYxFF1eJpliWzGmb5Wrz50wQ6JQ3VGK-pJdfGgGTXqC_FqarH9QqIbKpqy_10BW3Z0sqsXwdSCXUDVJtRCdHAHcfSzZswIKBHRKjEPgpjinQ6zrWWYV5jqp_IjWmRPSytX4Le5CBmNLzuNoknneBokuE0sq5G2mT9ttC2ldlKBNl5ied0ihsuu47uL3Wti1ndQktI0=", "session")
BOT_TOKEN = getenv("6038053134:AAF70JiVG5iFbMgLlMfXBlS5IJw5kUez_9Q")

API_ID = int(getenv("29717887"))
API_HASH = getenv("dbceb604465fabeb200f43b2fd32770d")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))

