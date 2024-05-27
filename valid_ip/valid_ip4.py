def is_valid_ipv4_address(address):
  """
  Check if the given IP address is a valid IPv4 address.

  Args:
    address (str): The IP address to check.

  Returns:
    bool: True if the address is valid, False otherwise.
  """

  try:
    octets = address.split(".")
    if len(octets) != 4:
      return False
    for octet in octets:
      octet_int = int(octet)
      if not (0 <= octet_int <= 255):
        return False
  except ValueError:
    return False

  return True

print(is_valid_ipv4_address("24.78.0.0"))
print(is_valid_ipv4_address("300.10.20.30"))