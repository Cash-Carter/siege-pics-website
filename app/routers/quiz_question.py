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
from random import randint
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.templates import templates

router = APIRouter()


@router.get("/quiz-question", response_class=JSONResponse)
def read_quiz():
    while True:
        images = os.listdir("app/images")
        image = images[randint(0, len(images) - 1)]

        return f"{{imageSrc = images/{image}, answers = [1, 2, 3, 4]}}"