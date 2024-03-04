import subprocess

# Function to install a package
def install_package(package):
    try:
        subprocess.check_call(["pip", "install", package])
        return True, None
    except subprocess.CalledProcessError as e:
        return False, e

# Read requirements.txt and install packages
with open("requirements.txt", "r") as file:
    packages = file.read().splitlines()

installed_packages = []
failed_packages = []

for package in packages:
    success, error = install_package(package)
    if success:
        installed_packages.append(package)
        print(f"Installed {package}")
    else:
        failed_packages.append(package)
        print(f"Failed to install {package}: {error}")

# Write failed packages to a file
with open("failed_packages.txt", "w") as file:
    for package in failed_packages:
        file.write(package + "\n")

print("Installation complete.")
