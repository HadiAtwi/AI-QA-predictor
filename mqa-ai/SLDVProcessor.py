import subprocess

class SLDVProcessor:
    def __init__(self, exe_path, slx_path, findings_list):
        self.exe_path = exe_path
        self.slx_path = slx_path
        self.findings_list = findings_list

    def run(self):
        cmd = [self.exe_path, self.findings_list, self.slx_path]
        print(f"Executing: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)

        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
