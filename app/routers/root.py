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
from fastapi import APIRouter, Query
from fastapi.responses import HTMLResponse
from typing import Annotated

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def read_root(operators: Annotated[list[str] | None, Query()] = None):
    common_elements = open("app/html/common-elements.html").read()
    website_template = open("app/html/gallery.html").read()
    image_template = open("app/html/image-template.html").read()

    images = os.listdir("app/images")

    if operators:
        images = filter(lambda image: not set(image.split("-")[0].split("_")).isdisjoint(set(operators)), images)

    image_list = ""
    for image in images:
        if image == "logo.png": continue
        if image == "logo.ico": continue
        image_list += image_template.format(image=image)

    return common_elements.format(content=website_template.format(images=image_list)) # TODO: add different page if no images found
