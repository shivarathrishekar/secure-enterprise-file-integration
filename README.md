\# Secure Enterprise File Integration \& DevOps Automation



\## Project Overview



This project demonstrates a containerized enterprise file integration workflow using Docker, SFTP, Python, Ansible, Jenkins and Nginx.



The objective is to simulate secure business data exchange between organisations, automate transaction validation, detect invalid records, and process incoming business files through a CI/CD pipeline.



\## Architecture



Company A → SFTP Server → Incoming CSV File → Python Validation → Jenkins Pipeline → Transaction Processing → Processed CSV



Nginx provides an HTTPS endpoint for secure communication testing.



Ansible automates integration environment configuration.



\## Technologies Used



| Technology | Purpose |

|---|---|

| Docker \& Docker Compose | Containerisation and service management |

| SFTP | Secure business file transfer |

| Python | Transaction validation and processing |

| Ansible | Configuration automation |

| Jenkins | CI/CD pipeline automation |

| Nginx | HTTPS endpoint |

| OpenSSL | TLS certificate generation |

| PowerShell | Windows environment management |



\## Project Features



\### 1. Secure File Transfer

\- Configured an SFTP server using Docker.

\- Created a sample business transaction CSV file.

\- Uploaded files using an SFTP client.

\- Verified uploaded files on the server.



\### 2. Python Transaction Validation

\- Reads incoming CSV files.

\- Validates transaction amounts.

\- Identifies invalid transactions.

\- Generates timestamped error logs.

\- Implements a quality gate that returns a non-zero exit code when invalid records are found.



\### 3. Transaction Processing

\- Processes incoming business records.

\- Marks valid transactions as PROCESSED.

\- Marks invalid transactions as REJECTED.

\- Generates a separate processed CSV file.



\### 4. Ansible Automation

\- Created an Ansible inventory.

\- Developed a playbook to configure the integration environment.

\- Automates directory and status-file creation.



\### 5. Jenkins CI/CD

\- Installed Jenkins using Docker.

\- Created a Pipeline job.

\- Integrated Python validation and transaction processing.

\- Added a quality gate for invalid transactions.

\- Verified both successful and failed pipeline executions.



\### 6. HTTPS and TLS

\- Generated a self-signed TLS certificate using OpenSSL.

\- Configured Nginx with HTTPS.

\- Created an HTTPS health endpoint.

\- Verified secure endpoint communication.



\### 7. Shared Storage

\- Created a persistent Docker named volume.

\- Verified that separate containers can write and read shared data.



\## Sample Validation Results



| Transaction | Amount | Result |

|---|---:|---|

| TXN001 | 5000 | VALID |

| TXN002 | 7500 | VALID |

| TXN003 | -3200 | INVALID |



Jenkins rejects the build when invalid transactions are detected.



\## Service Endpoints



| Service | Local endpoint |

|---|---|

| Jenkins | http://localhost:8081 |

| HTTPS health check | https://localhost:8444/health |

| SFTP | localhost:2223 |



The HTTPS endpoint uses a self-signed certificate for this lab environment.



\## Run the Project



Start the services:



```powershell

docker compose up -d --build

```



Check running containers:



```powershell

docker compose ps

```



Test HTTPS:



```powershell

curl.exe -k https://localhost:8444/health

```



Run Python validation:



```powershell

docker run --rm -v "${PWD}:/app" python:3.14-slim python /app/monitor.py

```



Run Ansible automation:



```powershell

docker run --rm -v "${PWD}:/project" -w /project cytopia/ansible:latest ansible-playbook -i ansible/inventory.ini ansible/setup.yml

```



\## Project Limitations



\- Docker shared storage is demonstrated using a named volume; a dedicated NFS server has not been implemented.

\- TLS is demonstrated using a self-signed certificate, not a production CA-issued certificate.

\- Axway B2Bi and Seeburger BIS are not implemented; their integration concepts are represented through this simulated workflow.

\- This is a learning and demonstration project, not a production deployment.



\## Learning Outcomes



\- Practical Docker container management.

\- Secure file transfer using SFTP.

\- Python automation and error handling.

\- Jenkins CI/CD pipeline development.

\- Ansible configuration automation.

\- TLS certificate management.

\- Container networking and troubleshooting.

\- End-to-end integration testing.



\---



\*\*Project Type:\*\* DevOps / Enterprise Integration  

\*\*Environment:\*\* Windows + Docker Desktop  

\*\*Status:\*\* Core demonstration implemented; documentation and repository publication in progress.



