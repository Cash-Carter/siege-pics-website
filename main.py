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
from fastapi.responses import Response, HTMLResponse, FileResponse
import os

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    website_template = open("site/html/index.html").read()
    image_template = open("site/html/image-template.html").read()

    image_list = ""
    for image in os.listdir("site/images"):
        image_list += image_template.format(image=image)

    return website_template.format(images=image_list)


@app.get("/images/{image}", response_class=FileResponse)
def get_image(image: str):
    return FileResponse("site/images/" + image)


@app.get("/css/{file}", response_class=Response)
def get_css(file:str):
    return Response(open("site/css/" + file).read(), )