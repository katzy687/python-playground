import keyring

keyring.set_password(service_name="natti-service", username="natti", password="ha")
x = keyring.get_password(service_name="natti-service", username="natti")
y = keyring.get_credential(service_name="natti-service", username=None)
pass