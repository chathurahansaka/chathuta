#MIT License

#Copyright (c) 2021 slgeekshow

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
SUDO_USERS = os.getenv("SUDO_USERS")
BOT_USERNAME = os.getenv("BOT_USERNAME")
BOT_OWNER = os.getenv("BOT_OWNER")
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO")
U_BRANCH = os.getenv("U_BRANCH")
HEROKU_URL = os.getenv("HEROKU_URL")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
DATABASE_URL = os.getenv("DATABASE_URL")
LOG_CHANNEL = os.getenv("LOG_CHANNEL")
BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY")
ARQ_API_KEY = os.getenv("ARQ_API_KEY")
FSUB_CHANNEL = os.environ.get("FSUB_CHANNEL")
