import subprocess
import os
import unittest

class TestProgram(unittest.TestCase):
    test_dir = './test'
    prog_dir = './prog'

    def run_test(self, program, test_name, use_args):
        input_file = os.path.join(self.test_dir, f'{program}.{test_name}.in')
        expected_file = os.path.join(self.test_dir, f'{program}.{test_name}{'.arg.out' if use_args else '.out'}')
        status_file = os.path.join(self.test_dir, f'{program}.{test_name}.status')
        cmd = ['python3', os.path.join(self.prog_dir, f'{program}.py')]

        # Read arguments from the .in file and pass them to the command
        if program != 'wc' or use_args:
            with open(input_file, 'r') as f:
                args = f.read().strip().split()
            cmd.extend(args)
            process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            # For 'wc', when use_args is False, pass the content through STDIN
            with open(input_file, 'r') as f:
                input_content = f.read()
            process = subprocess.run(cmd, input=input_content.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Get the expected exit status
        expected_status = 0  # Default expected status is 0
        if os.path.exists(status_file):
            with open(status_file, 'r') as f:
                expected_status = int(f.read().strip())

        # Check the exit status against the expected status
        self.assertEqual(process.returncode, expected_status, f"Program exited with {process.returncode}, expected {expected_status}. Error: {process.stderr.decode('utf-8')}")

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
                # Determine if command line arguments should be used based on the program
                use_args = True if program == 'file_finder' or program == 'gron' else False
                self.run_test(program, test_name, use_args)

if __name__ == '__main__':
    unittest.main()
