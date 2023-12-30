# kube-install-ubuntu
Installing Kubernetes on ubuntu 22.04
# configuration
Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 10.0.0.48:6443 --token q5ntqk.05kj33m40gas8l6e \
	--discovery-token-ca-cert-hash sha256:8fafe327bb8908f4b9f42ca760eeca4c97dc5351fb3972f07971c9526c71afeb 
