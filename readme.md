---

# **SSL Management API**

A RESTful API for managing SSL certificates, including selecting certificate authorities (CAs), verifying domains, generating Certificate Signing Requests (CSRs), submitting CSRs, installing certificates, enabling HTTPS redirection, and checking SSL status.

---

## **Features**

- Select available Certificate Authorities (CAs).
- Verify domain ownership.
- Generate a Certificate Signing Request (CSR).
- Submit the CSR to a Certificate Authority (CA) and obtain a certificate.
- Install the SSL certificate on the server.
- Enable HTTPS redirection.
- Check the validity of an existing SSL certificate.

---

## **API Endpoints**

| **Method** | **Endpoint**           | **Description**                            |
|------------|------------------------|--------------------------------------------|
| `GET`      | `/v2/api/sslmanager/choose_ca/`      | Retrieve a list of available CAs.          |
| `POST`     | `/v2/api/sslmanager/verify_website/` | Verify the ownership of a domain.          |
| `POST`     | `/v2/api/sslmanager/generate_csr/`   | Generate a Certificate Signing Request.    |
| `POST`     | `/v2/api/sslmanager/submit_csr/`     | Submit CSR to CA and obtain the certificate.|
| `POST`     | `/v2/api/sslmanager/install_certificate/` | Install the certificate on the server.    |
| `POST`     | `/v2/api/sslmanager/redirect_to_https/` | Enable HTTPS redirection.                 |
| `GET`      | `/v2/api/sslmanager/check_ssl/`      | Check SSL certificate validity.            |

---

## **Request/Response Details**

### **1. Choose Certificate Authority**
**Endpoint**: `GET /v2/api/sslmanager/choose_ca/`

**Response**:
```json
{
  "available_cas": ["Let's Encrypt", "DigiCert", "Comodo", "GlobalSign"]
}
```

---

### **2. Verify Website**
**Endpoint**: `POST /v2/api/sslmanager/verify_website/`

**Request**:
```json
{
  "domain": "example.com"
}
```

**Response**:
- **Success**:
  ```json
  {
    "message": "Domain verified"
  }
  ```
- **Error**:
  ```json
  {
    "error": "Domain verification failed"
  }
  ```

---

### **3. Generate CSR**
**Endpoint**: `POST /v2/api/sslmanager/generate_csr/`

**Request**:
```json
{
  "country": "US",
  "state": "California",
  "locality": "Los Angeles",
  "organization": "Example Inc",
  "common_name": "example.com"
}
```

**Response**:
```json
{
  "csr": "-----BEGIN CERTIFICATE REQUEST-----\n...\n-----END CERTIFICATE REQUEST-----",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----"
}
```

---

### **4. Submit CSR**
**Endpoint**: `POST /v2/api/sslmanager/submit_csr/`

**Request**:
```json
{
  "csr": "-----BEGIN CERTIFICATE REQUEST-----\n...\n-----END CERTIFICATE REQUEST-----",
  "ca": "Let's Encrypt"
}
```

**Response**:
```json
{
  "certificate": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----"
}
```

---

### **5. Install Certificate**
**Endpoint**: `POST /v2/api/sslmanager/install_certificate/`

**Request**:
```json
{
  "certificate": "-----BEGIN CERTIFICATE-----\n...\n-----END CERTIFICATE-----",
  "domain": "example.com"
}
```

**Response**:
```json
{
  "message": "Certificate installed successfully"
}
```

---

### **6. Redirect to HTTPS**
**Endpoint**: `POST /v2/api/sslmanager/redirect_to_https/`

**Response**:
```json
{
  "message": "Redirect to HTTPS enabled"
}
```

---

### **7. Check SSL**
**Endpoint**: `GET /v2/api/sslmanager/check_ssl/`

**Request**:
```http
GET /v2/api/sslmanager/check_ssl/?domain=example.com
```

**Response**:
```json
{
  "domain": "example.com",
  "ssl_valid": true
}
```

---

## **Deployment Instructions**

### **1. Kubernetes Deployment File**
The `deployment.yaml` file contains the configuration for deploying the API to an EKS cluster.

**Example**:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ssl-management-api
  labels:
    app: ssl-management-api
spec:
  replicas: 2
  selector:
    matchLabels:
      app: ssl-management-api
  template:
    metadata:
      labels:
        app: ssl-management-api
    spec:
      containers:
        - name: ssl-management-api
          image: <image-repo>:<tag>
          ports:
            - containerPort: 8000
          env:
            - name: DJANGO_SETTINGS_MODULE
              value: "ssl_management.settings"
---
apiVersion: v1
kind: Service
metadata:
  name: ssl-management-api
  labels:
    app: ssl-management-api
spec:
  selector:
    app: ssl-management-api  # Must match the labels in your Deployment
  ports:
    - protocol: TCP
      port: 8001             # Port exposed by the Service
      targetPort: 8001       # Container port in the Deployment
  type: ClusterIP            # Default service type, accessible within the cluster
---
```

---

### **2. Ingress Configuration**
The `ingress.yaml` file (stored in certping-web repository) will route traffic to the API.

**Example**:
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ssl-management-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /v2/api/sslmanager/
            pathType: Prefix
            backend:
              service:
                name: ssl-management-api
                port:
                  number: 8001
```

---

## **Running Locally**
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd ssl-management-api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```bash
   python manage.py runserver
   ```

4. Access the API at `http://127.0.0.1:8000/v2/api/sslmanager`.

---

## **Testing**
Run unit tests to ensure the API is functioning correctly:
```bash
python manage.py test
```

---
