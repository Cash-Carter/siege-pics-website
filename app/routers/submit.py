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

from random import randint
from fastapi import APIRouter, File, UploadFile
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.post("/submit", response_class=RedirectResponse)
async def post_image(image: UploadFile = File(...)):
    response = RedirectResponse(url="/", status_code=303)
    contents = await image.read()
    if contents.__sizeof__() > 10000000 or contents.__sizeof__() < 100:
        return response
    if image.filename == None:
        return response
    
    try:
        with open("app/submissions/" + image.filename, "xb") as buffer:
            buffer.write(contents)
    except:
        with open("app/submissions/" + image.filename + str(randint(0, 999999999)), "xb") as buffer:
            buffer.write(contents)
    
    return response
