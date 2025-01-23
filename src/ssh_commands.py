import subprocess

def run_terraform_over_ssh(host, private_key_path, terraform_dir, username):
    # Build the SSH command
    ssh_command = [
        "ssh",
        "-i", private_key_path,
        f"{username}@{host}",
        f"cd {terraform_dir} && terraform apply --auto-approve" 
    ]

    # Execute the command using subprocess
    result = subprocess.run(
        ssh_command,
        text=True,
        capture_output=True
    )
