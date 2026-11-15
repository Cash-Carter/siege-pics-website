# Copyright 2026 Cash Carter
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import ssl
import uvicorn
import sys

reload: bool = "--reload" in sys.argv
if reload: print("Reload enabled")
development_mode: bool = "--dev" in sys.argv
if development_mode: print("Development mode enabled")

if development_mode:
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=reload)
else:
    uvicorn.run("main:app", host="0.0.0.0", port=443, reload=reload,
                ssl_version=ssl.PROTOCOL_TLS_SERVER,
                ssl_keyfile="private_key",
                ssl_certfile="origin_certificate")