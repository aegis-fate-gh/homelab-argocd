# homelab-argocd
This contains configs and files for the argocd managed portion of my homelab.

It works via an app of apps model. With the big apps being in the applications folder, and the apps they manage being located in apps. Manifests is as the name implies, where the manifests are stored. They're split based on what app manages them, along with a templates folder.