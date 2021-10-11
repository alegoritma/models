# Copyright 2021 The TensorFlow Authors. All Rights Reserved.
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

"""YT8M model training driver."""

from absl import app

from official.common import flags as tfm_flags
from official.vision.beta import train
# pylint: disable=unused-import
from official.vision.beta.projects.yt8m.configs import yt8m
from official.vision.beta.projects.yt8m.tasks import yt8m_task
# pylint: enable=unused-import


if __name__ == '__main__':
  tfm_flags.define_flags()
  app.run(train.main)
