import platform
import shutil
import subprocess
import sys


def check_linux_service(service_name: str) -> str:
  if shutil.which("systemctl"):
    result = subprocess.run(
        ["systemctl", "is-active", service_name], capture_output=True, text=True
    )
    status = result.stdout.strip()

    if status == "active":
      return f"Service '{service_name}' is running."
    elif status == "unknown":
      return f"Service '{service_name}' was not found."
    return f"Service '{service_name}' is not running (Status: {status or 'inactive'})."

  if shutil.which("service"):
    result = subprocess.run(
        ["service", service_name, "status"], capture_output=True, text=True
    )
    return (
        f"Service '{service_name}' is running."
        if result.returncode == 0
        else f"Service '{service_name}' is not running or not found."
    )

  return "Error: Neither 'systemctl' nor 'service' command was found."


def check_macos_service(service_name: str) -> str:
  if not shutil.which("launchctl"):
    return "Error: 'launchctl' command not found."

  result = subprocess.run(
      ["launchctl", "list", service_name], capture_output=True, text=True
  )

  if result.returncode != 0:
    return f"Service '{service_name}' is not loaded or not found."

  # If loaded and running, launchctl output includes a active PID
  if '"PID"' in result.stdout or "PID" in result.stdout:
    return f"Service '{service_name}' is running."
  return f"Service '{service_name}' is loaded but stopped."


def check_windows_service(service_name: str) -> str:
  result = subprocess.run(
      ["sc", "query", service_name], capture_output=True, text=True
  )
  output = result.stdout

  if "1060" in output or "does not exist" in output.lower():
    return f"Service '{service_name}' does not exist."
  if "RUNNING" in output:
    return f"Service '{service_name}' is running."
  if "STOPPED" in output:
    return f"Service '{service_name}' is stopped."
  if "PAUSED" in output:
    return f"Service '{service_name}' is paused."

  return (
      f"Service '{service_name}' status could not be determined:\n{output.strip()}"
  )


def check_service(service_name: str) -> None:
  current_os = platform.system()

  os_handlers = {
      "Linux": check_linux_service,
      "Darwin": check_macos_service,
      "Windows": check_windows_service,
  }

  handler = os_handlers.get(current_os)
  if not handler:
    print(f"Unsupported operating system: {current_os}")
    return

  try:
    print(handler(service_name))
  except Exception as e:
    print(f"An error occurred while querying the service: {e}")


if __name__ == "__main__":
  service = (
      sys.argv[1] if len(sys.argv) > 1 else input("Enter service name: ").strip()
  )
  if service:
    check_service(service)
  else:
    print("Error: No service name provided.")