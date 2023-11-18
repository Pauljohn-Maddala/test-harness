import subprocess
import os
import unittest

class TestHarness(unittest.TestCase):

    def run_test_case(self, program, input_file, expected_output_file, arg=False):
        # If arg is True, pass input_file as a command-line argument, else use STDIN
        if arg:
            proc = subprocess.run([f'./{program}', input_file], capture_output=True, text=True)
        else:
            with open(input_file, 'r') as f:
                proc = subprocess.run([f'./{program}'], stdin=f, capture_output=True, text=True)
        
        # Check if the process exited with a non-zero status
        self.assertEqual(proc.returncode, 0)
        
        # Compare the actual output to the expected output
        with open(expected_output_file, 'r') as f:
            expected_output = f.read()
        self.assertEqual(proc.stdout, expected_output)

    def test_programs(self):
        test_dir = './test/'
        for filename in os.listdir(test_dir):
            if filename.endswith('.in'):
                basename = filename[:-3]  # Strip off '.in' to get the base filename
                program, test_case = basename.split('.', 1)

                # Test using STDIN
                input_file = os.path.join(test_dir, f'{program}.{test_case}.in')
                expected_output_file = os.path.join(test_dir, f'{program}.{test_case}.out')
                if os.path.exists(expected_output_file):
                    self.run_test_case(program, input_file, expected_output_file)

                # Test using command-line argument
                arg_output_file = os.path.join(test_dir, f'{program}.{test_case}.arg.out')
                if os.path.exists(arg_output_file):
                    self.run_test_case(program, input_file, arg_output_file, arg=True)

if __name__ == '__main__':
    unittest.main()
