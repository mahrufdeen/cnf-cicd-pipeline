# 🚀 CNF CI/CD Pipeline (Cloud-Native Telecom DevOps Project)
![CI](https://github.com/mahrufdeen/cnf-cicd-pipeline/actions/workflows/cicd.yaml/badge.svg)

## 👤 Author
**Moruf Kelani**
GitHub: https://github.com/mahrufdeen

## 🧠 Overview
This project demonstrates a **cloud-native CI/CD pipeline** for deploying a mock Packet Core Network Function (CNF) in a Kubernetes environment.

It simulates how telecom workloads (e.g., AMF-like services) are built, containerized, and deployed using modern DevOps practices aligned with **Ericsson CNIS/CCD environments**.

## 🏗️ Architecture
GitHub Actions → Docker Hub → Kubernetes (Kind) → Helm Deployment

## ⚙️ Tech Stack
* **Docker** – Containerization
* **Kubernetes (Kind)** – Cluster environment
* **Helm** – Application deployment
* **GitHub Actions** – CI/CD pipeline
* **Python (Flask)** – Mock CNF service

## 🔄 CI/CD Pipeline Flow
1. Code pushed to `main` branch
2. Docker image is built
3. Image is pushed to Docker Hub (`mahrufdeen/cnf-app`)
4. Kubernetes cluster is created using Kind
5. Application is deployed using Helm
6. Deployment is verified using `kubectl`

## 📦 Docker Image
```text
mahrufdeen/cnf-app:latest
```

## 📁 Project Structure
```text
app/                  # Mock CNF application (Flask)
helm/                 # Helm chart for Kubernetes deployment
.github/workflows/    # CI/CD pipeline definition
README.md             # Project documentation
```

## ☸️ Kubernetes Deployment (Manual Test)

```bash
kind create cluster
helm install cnf-app ./helm/cnf-app
kubectl get pods
```

## 🚀 Key Features
* ✅ End-to-end CI/CD pipeline
* ✅ Docker Hub integration
* ✅ Kubernetes-based deployment
* ✅ Helm packaging
* ✅ Telecom CNF simulation

## 📸 Screenshots

<img width="248" height="402" alt="image" src="https://github.com/user-attachments/assets/fbcaac67-f336-411c-97a2-45d2e2c61d1b" />

## 🔮 Future Improvements
* GitOps integration (ArgoCD)
* Prometheus & Grafana monitoring
* CNF log analysis & RCA automation
* Multi-environment deployment (dev/stage/prod)

## 📈 Use Case
This project reflects real-world telecom scenarios where **Packet Core network functions are deployed as cloud-native workloads**, enabling scalability, automation, and reliability.

## 📫 Connect With Me
* LinkedIn: https://www.linkedin.com/in/moruf-kelani-19689882/

## ⚡ Summary
This project demonstrates practical experience in:
* Cloud-native telecom systems
* DevOps automation
* Kubernetes-based deployments
* CI/CD pipeline design

> 🚀 Built as part of my journey into Cloud-Native Telecom & DevOps Engineering
