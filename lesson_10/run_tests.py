import subprocess
import sys

def run_tests():
    result = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-v"], cwd=".")
    return result.returncode

if __name__ == "__main__":
    sys.exit(run_tests())
    