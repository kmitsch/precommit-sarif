import subprocess

# Command injection vulnerability (Insecure: Avoid using shell=True)
def dangerous_command(user_input):
    command = f"ls {user_input}"
    subprocess.run(command, shell=True)  # Potential command injection

if __name__ == "__main__":
    dangerous_command("; echo Hacked!")
