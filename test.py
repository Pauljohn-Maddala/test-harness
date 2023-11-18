import subprocess
import os
import unittest

class TestProgram(unittest.TestCase):
    test_dir = './test'
    prog_dir = './prog'

    def run_test(self, program, test_name, use_args=False):
        input_file = f'{self.test_dir}/{program}.{test_name}.in'
        expected_file = f'{self.test_dir}/{program}.{test_name}' + ('.arg.out' if use_args else '.out')
        
        cmd = ['python3', os.path.join(self.prog_dir, f'{program}.py')]
    
        if use_args:
            with open(input_file, 'r') as f:
                # Assuming the arguments are newline-separated
                args = f.read().strip().splitlines()
            cmd.extend(args)
            process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            with open(input_file, 'rb') as f:
                process = subprocess.run(cmd, stdin=f, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
        self.assertEqual(process.returncode, 0, f"Program exited with {process.returncode}. Error: {process.stderr.decode('utf-8')}")
    
        actual_output = process.stdout.decode('utf-8').strip()
    
        with open(expected_file, 'r') as f:
            expected_output = f.read().strip()
    
        self.assertEqual(actual_output, expected_output, f'Failed test: {program}.{test_name} with {"arguments" if use_args else "stdin"}')

    def test_programs(self):
        for filename in os.listdir(self.test_dir):
            if filename.endswith('.in'):
                program, test_name = filename[:-3].split('.', 1)
                self.run_test(program, test_name, use_args=False)
                arg_file = f'{program}.{test_name}.arg.out'
                if arg_file in os.listdir(self.test_dir):
                    self.run_test(program, test_name, use_args=True)

if __name__ == '__main__':
    unittest.main()
