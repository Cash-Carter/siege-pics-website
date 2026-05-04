# Copyright 2026 Cash Carter
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>.

from fastapi import FastAPI
from .routers import about, contact, css, fortnite, image, images, music, root, submission, submit

app = FastAPI()


app.include_router(about.router)
app.include_router(contact.router)
app.include_router(css.router)
app.include_router(fortnite.router)
app.include_router(image.router)
app.include_router(images.router)
app.include_router(music.router)
app.include_router(root.router)
app.include_router(submission.router)
app.include_router(submit.router)
