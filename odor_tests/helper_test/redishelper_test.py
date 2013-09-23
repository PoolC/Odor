'''
Created on 2013. 9. 17.

@author: tintypemolly
'''
import sys
sys.path.append("../..")

from odor_helper.redishelper import RedisHelper
import unittest


class RedisHelperTest(unittest.TestCase):
    
    def test_get_set(self):
        RedisHelper.connection.set("foo", "bar")
        self.assertEqual(RedisHelper.connection.get("foo"), "bar")
    
    def tearDown(self):
        RedisHelper.connection.delete("foo")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()