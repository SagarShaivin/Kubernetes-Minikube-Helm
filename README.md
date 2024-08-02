# Kubernetes-Minikube-Helm
Hosted a 2-Tier Flask application with Mysql using Kubernetes with Minikube and Helm

minikube start
helm install myapp ./myapp
helm template myapp ./myapp/
helm template myapp ./myapp --debug
kubectl get pods
kubectl get services
kubectl logs myapp-myapp-test-connection
minikube service flask-app
