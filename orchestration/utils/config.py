# Copyright 2019 The OpenSDS Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# flask server configuration
HOST = "127.0.0.1"
PORT = "5000"

# logging configuration
LOGGING_FILE = "/var/log/opensds/orchestration.log"
LOGGIGN_FORMAT = "format = [%(asctime)s] [%(levelname)s] [%(name)s] " \
    "[%(funcName)s():%(lineno)s] [PID:%(process)d TID:%(thread)d] %(message)s"
LOGGING_LEVEL = "INFO"


# database configuration
DATABASE = {
    'sqlalchemy.url': 'sqlite://'
}
