#!/usr/bin/python3
"""
Unit test for BaseModel class
"""
from datetime import datetime
import inspect
from models.base_model import BaseModel
import unittest



class TestBaseModelDocs(unittest.TestCase):
	"""Test BaseModel docs"""
	
	all_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

	def test_doc_file(self):
		"""... documentation for the file"""
		expected = '\nBaseModel Class of Models Module\n'
		actual = models.base_model.__doc__
		self.assertEqual(expected, actual)
	
	def test_doc_class(self):
		"""... documentation for the class"""
		expected = ('\n        attributes and functions for BaseModel class\n'
                    '    ')
		actual = BaseModel.__doc__
		self.assertEqual(expected, actual)

	def test_all_function_docs(self):
		"""... tests for ALL DOCS for all functions in db_storage file"""
		all_functions = TestBaseModelDocs.all_funcs
		for function in all_functions:
			self.assertIsNotNone(function[1].__doc__)

	def test_file_is_executable(self):
		"""... tests if file has correct permissions so user can execute"""
		file_stat = stat('models/base_model.py')
		permissions = str(oct(file_stat[0]))
		actual = int(permissions[5:-2]) >= 5
		self.assertTrue(actual)


if __name__ == '__main__':
    """
    MAIN TESTS
    """
    unittest.main