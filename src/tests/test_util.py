# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2014 Midokura Europe SARL, All Rights Reserved.
# All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# @author: Ryu Ishimoto <ryu@midokura.com>, Midokura

from ddt import ddt, data
import unittest

from midonetclient import util


@ddt
class TestUtil(unittest.TestCase):

    @data(
        ("foo", "foo"),
        ("foo_bar", "foo_bar"),
        ("Foo", "foo"),
        ("fooBar", "foo_bar"),
        ("fooBarBaz", "foo_bar_baz")
    )
    def test_convert_camel_to_snake(self, data):
        input, expected = data
        self.assertEquals(expected, util.camel_to_snake(input))

    @data(
        ("foo", "foo"),
        ("fooBar", "fooBar"),
        ("Foo", "Foo"),
        ("foo_bar", "fooBar"),
        ("foo_bar_baz", "fooBarBaz")
    )
    def test_convert_snake_to_camel(self, data):
        input, expected = data
        self.assertEquals(expected, util.snake_to_camel(input))

    @data(
        (None, None),
        ({}, {}),
        ([], []),
        (1, 1),
        ([1, 2], [1, 2]),
        ({"foo": 1, "bar": 2}, {"FOO": 1, "BAR": 2}),
        ({"foo": [1, 2]}, {"FOO": [1, 2]}),
        ([{"foo": 1}, {"bar": 2}], [{"FOO": 1}, {"BAR": 2}]),
        ({"foo": [{"bar": 1}, {"baz": 2}]}, {"FOO": [{"BAR": 1}, {"BAZ": 2}]})
    )
    def test_convert_dict_keys(self, data):
        input, expected = data

        def to_upper(s):
            return s.upper()

        output = util.convert_dict_keys(input, to_upper)
        self.assertTrue(cmp(expected, output) == 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()