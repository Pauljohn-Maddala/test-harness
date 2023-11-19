import subprocess
import os
import unittest

class TestProgram(unittest.TestCase):
    test_dir = './test'
    prog_dir = './prog'

    def run_test(self, program, test_name, use_args):
        input_file = f'{self.test_dir}/{program}.{test_name}.in'
        expected_file = f'{self.test_dir}/{program}.{test_name}' + ('.arg.out' if use_args else '.out')
        cmd = ['python3', os.path.join(self.prog_dir, f'{program}.py')]
    
        if program == 'gron':
            # If 'gron', expect a JSON file as an argument
            cmd.append(input_file)
            process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        elif program == 'wc':
            # For 'wc', when use_args is False, the content should be passed through STDIN
            if not use_args:
                with open(input_file, 'r') as f:
                    input_content = f.read()
                process = subprocess.run(cmd, input=input_content.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                # If use_args is True, 'wc' expects a file path
                cmd.append(input_file)
                process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            # For other programs, read the .in file and pass arguments
            with open(input_file, 'r') as f:
                args = f.read().strip().split()
            cmd.extend(args)
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
                # Determine if command line arguments should be used based on the program
                use_args = True if program == 'file_finder' else False
                self.run_test(program, test_name, use_args)

if __name__ == '__main__':
    unittest.main()
