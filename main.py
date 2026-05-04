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

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response, HTMLResponse, FileResponse, RedirectResponse
import os
from random import randint

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    common_elements = open("site/html/common-elements.html").read()
    website_template = open("site/html/index.html").read()
    image_template = open("site/html/image-template.html").read()

    image_list = ""
    for image in os.listdir("site/images"):
        if image == "logo.png": continue
        if image == "logo.ico": continue
        image_list += image_template.format(image=image)

    return common_elements.format(content=website_template.format(images=image_list))


@app.get("/image/{image}", response_class=HTMLResponse)
def read_image(image: str):
    common_elements = open("site/html/common-elements.html").read()
    viewer = open("site/html/viewer.html").read()
    return common_elements.format(content=viewer.format(image=image))

@app.get("/about", response_class=HTMLResponse)
def read_about():
    common_elements = open("site/html/common-elements.html").read()
    about = open("site/html/about.html").read()
    return common_elements.format(content=about)

@app.get("/fortnite", response_class=HTMLResponse)
def read_about():
    common_elements = open("site/html/common-elements.html").read()
    fortnite = open("site/html/fortnite.html").read()
    return common_elements.format(content=fortnite)


@app.get("/contact", response_class=HTMLResponse)
def read_contact():
    common_elements = open("site/html/common-elements.html").read()
    contact = open("site/html/contact.html").read()
    return common_elements.format(content=contact)


@app.get("/submission", response_class=HTMLResponse)
def read_submission():
    common_elements = open("site/html/common-elements.html").read()
    submission = open("site/html/submission.html").read()
    return common_elements.format(content=submission)


@app.post("/submit", response_class=RedirectResponse)
async def post_image(image: UploadFile = File(...)):
    contents = await image.read()
    try:
        if contents.__sizeof__() < 10000000:
            with open("site/submissions/" + image.filename, "xb") as buffer:
                buffer.write(contents)
    except:
        if contents.__sizeof__() < 10000000:
            with open("site/submissions/" + image.filename + str(randint(0, 999999999)), "xb") as buffer:
                buffer.write(contents)
    return RedirectResponse(url="/", status_code=303)


@app.get("/images/{image}", response_class=FileResponse)
def get_image(image: str):
    return FileResponse("site/images/" + image)

@app.get("/music/{music}", response_class=FileResponse)
def music(music: str):
    return FileResponse("site/music/" + music)


@app.get("/css/{file}", response_class=Response)
def get_css(file:str):
    return Response(open("site/css/" + file).read(), )