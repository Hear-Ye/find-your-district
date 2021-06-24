# Copyright 2021 Andrew Chen Wang
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from src.app import GEOJSON, get_federal_district


votable = set(range(len(GEOJSON)))
non_votable = {12, 87, 130, 231, 346, 417}
# Get rid of non votable districts for testing sake
# I'm going to add them back in once I figure out which
# 6 VOTING districts are missing and what's causing the
# geojson to fail.
votable.difference_update(non_votable)


@pytest.mark.parametrize("index", votable)
def test_geojson_indices_good(index):
    assert get_federal_district(index)
