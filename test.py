import subprocess
import os
import unittest

class TestProgram(unittest.TestCase):
    test_dir = './test'
    prog_dir = './prog'

    def run_test(self, program, test_name, use_args=False):
        input_file = f'{self.test_dir}/{program}.{test_name}.in'
        expected_file = f'{self.test_dir}/{program}.{test_name}'+ ('.arg.out' if use_args else '.out')

        # Read arguments from the .in file
        with open(input_file, 'r') as f:
            # Split the arguments into a list. Assumes that the input file has the arguments on one line.
            args = f.read().strip().split(' ', 1)

        # Construct the command
        cmd = ['python', os.path.join(self.prog_dir, f'{program}.py')] + args

        # Run the program with the provided arguments
        process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Check if the process exited with a non-zero status
        self.assertEqual(process.returncode, 0, f"Program exited with {process.returncode}. Error: {process.stderr.decode('utf-8')}")

        # Get the actual output from the program
        actual_output = process.stdout.decode('utf-8').strip()

        # Compare the actual output to the expected output
        with open(expected_file, 'r') as f:
            expected_output = f.read().strip()
        
        self.assertEqual(actual_output, expected_output, f'Failed test: {program}.{test_name} with {"arguments" if use_args else "stdin"}')

    def test_programs(self):
        for filename in os.listdir(self.test_dir):
            if filename.endswith('.in'):
                program, test_name = filename[:-3].split('.', 1)
                self.run_test(program, test_name, use_args=True) # Set to True to use command line arguments

if __name__ == '__main__':
    unittest.main()
