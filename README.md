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

### install conda for python
download conda from - https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
sudo bash Anaconda3-2023.09-0-Linux-x86_64.sh
install path - /opt/anaconda3
sudo groupadd anaconda
sudo chgrp -R anaconda /opt/anaconda3
sudo adduser scorpion anaconda
source /opt/anaconda3/bin/activate
conda init
### install juypter lab
pip install jupyterlab
jupyter lab
cd .jupyter
jupyter notebook --generate-config
vi jupyter_notebook_config.py
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.token = ''


