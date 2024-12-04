from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from OpenSSL import crypto
import subprocess

class ChooseCA(APIView):
    def get(self, request):
        # Example CA selection logic
        ca_list = ["Let's Encrypt", "DigiCert", "Comodo", "GlobalSign"]
        return Response({"available_cas": ca_list})

class VerifyWebsite(APIView):
    def post(self, request):
        domain = request.data.get('domain')
        if not domain:
            return Response({"error": "Domain is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Use ICANN Lookup or a mock validation for now
        is_valid = True  # Replace with actual ICANN Lookup integration
        if is_valid:
            return Response({"message": "Domain verified"})
        return Response({"error": "Domain verification failed"}, status=status.HTTP_400_BAD_REQUEST)

class GenerateCSR(APIView):
    def post(self, request):
        data = request.data
        required_fields = ["country", "state", "locality", "organization", "common_name"]
        
        # Validate required fields
        for field in required_fields:
            if field not in data:
                return Response({"error": f"{field} is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Generate a CSR
        key = crypto.PKey()
        key.generate_key(crypto.TYPE_RSA, 2048)

        csr = crypto.X509Req()
        csr.get_subject().C = data['country']
        csr.get_subject().ST = data['state']
        csr.get_subject().L = data['locality']
        csr.get_subject().O = data['organization']
        csr.get_subject().CN = data['common_name']
        csr.set_pubkey(key)
        csr.sign(key, 'sha256')

        csr_pem = crypto.dump_certificate_request(crypto.FILETYPE_PEM, csr).decode('utf-8')
        return Response({"csr": csr_pem, "private_key": crypto.dump_privatekey(crypto.FILETYPE_PEM, key).decode('utf-8')})

class SubmitCSR(APIView):
    def post(self, request):
        csr = request.data.get('csr')
        ca = request.data.get('ca')
        
        # Simulate CA signing
        if not csr or not ca:
            return Response({"error": "CSR and CA are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Simulate certificate issuance
        cert = "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"  # Replace with actual CA integration
        return Response({"certificate": cert})

class InstallCertificate(APIView):
    def post(self, request):
        certificate = request.data.get('certificate')
        domain = request.data.get('domain')

        if not certificate or not domain:
            return Response({"error": "Certificate and domain are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Example: Save certificate and restart server (pseudo-code)
        cert_path = f"/etc/ssl/certs/{domain}.crt"
        with open(cert_path, "w") as f:
            f.write(certificate)

        subprocess.run(["sudo", "service", "nginx", "reload"])
        return Response({"message": "Certificate installed successfully"})

class RedirectToHTTPS(APIView):
    def post(self, request):
        # Example: Add redirect rules to NGINX config (pseudo-code)
        subprocess.run(["sudo", "service", "nginx", "reload"])
        return Response({"message": "Redirect to HTTPS enabled"})

class CheckSSL(APIView):
    def get(self, request):
        domain = request.query_params.get('domain')
        if not domain:
            return Response({"error": "Domain is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if SSL is valid (mock example)
        ssl_valid = True  # Replace with actual SSL check
        return Response({"domain": domain, "ssl_valid": ssl_valid})
