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

import os
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def read_root():
    common_elements = open("app/html/common-elements.html").read()
    website_template = open("app/html/index.html").read()
    image_template = open("app/html/image-template.html").read()

    image_list = ""
    for image in os.listdir("app/images"):
        if image == "logo.png": continue
        if image == "logo.ico": continue
        image_list += image_template.format(image=image)

    return common_elements.format(content=website_template.format(images=image_list))
