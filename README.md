# EXEfromCER
This is a proof of concept to deliver a binary payload via an X.509 TLS certificate.
It embeds a full Windows executable inside a custom extension of an X.509 certificate and serves it via HTTPS. The client extracts the payload from the certificate and executes it.

1. Generate a certificate with a custom OID extension containing your binary. (openssl req -new -x509 -days 365 -config cert.ini -keyout srkey.pem -out srcert.pem -nodes)
2. Serve it over TLS (e.g., with OpenSSL).
3. Python client connects to the SSL server, extracts the binary, writes it to disk, and runs it.

<img width="719" height="714" alt="image" src="https://github.com/user-attachments/assets/74b04e6a-ea05-4847-960c-31a8e9a59e2e" />
