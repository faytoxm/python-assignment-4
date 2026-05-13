# Test results:
# test_analyse_twice (tests.test_analyser.TestAnalyser) ... ok
# test_result_has_required_keys (tests.test_analyser.TestAnalyser) ... ok
# test_result_is_not_empty (tests.test_analyser.TestAnalyser) ... ok
# test_total_students (tests.test_analyser.TestAnalyser) ... ok
# ----------------------------------------------------------------------
# Ran 4 tests in 0.001s
# OK

import unittest
# Importing your GpaAnalyser from the analytics package
from analytics.analyser import GpaAnalyser

class TestAnalyser(unittest.TestCase):
    
    def setUp(self):
        """
        Task 3: Setting up a small sample data for testing.
        This replaces the need for students.csv during tests.
        """
        self.sample = [
            {"student_id": "1", "GPA": "4.0", "age": "20", "country": "USA"},
            {"student_id": "2", "GPA": "3.0", "age": "21", "country": "India"},
            {"student_id": "3", "GPA": "3.8", "age": "22", "country": "UK"},
            {"student_id": "4", "GPA": "2.5", "age": "20", "country": "Canada"},
            {"student_id": "5", "GPA": "3.6", "age": "23", "country": "USA"}
        ]

    def test_result_is_not_empty(self):
        """Test 1: Verify that the result dictionary is not empty after analysis"""
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertTrue(len(analyser.result) > 0)

    def test_total_students(self):
        """Test 2: Verify that the total_students count is exactly 5"""
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        self.assertEqual(analyser.result["total_students"], 5)

    def test_result_has_required_keys(self):
        """Test 3: Check if all required keys for Variant A are present in the result"""
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        expected_keys = ["total_students", "average_gpa", "max_gpa", "min_gpa", "high_performers"]
        for key in expected_keys:
            self.assertIn(key, analyser.result)

    def test_analyse_twice(self):
        """Test 4: Ensure that running analyse() multiple times produces the same result"""
        analyser = GpaAnalyser(self.sample)
        analyser.analyse()
        first_result = analyser.result.copy()
        analyser.analyse()
        self.assertEqual(analyser.result, first_result)

if __name__ == '__main__':
    unittest.main()