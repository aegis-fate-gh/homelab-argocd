# homelab-argocd
This contains configs and files for the argocd managed portion of my homelab.

It works via an app of apps model. With the big apps being in the [applications](https://github.com/aegis-fate-gh/homelab-argocd/tree/main/argocd/applications) folder, and the apps they manage being located in [apps](https://github.com/aegis-fate-gh/homelab-argocd/tree/main/apps). [Manifests](https://github.com/aegis-fate-gh/homelab-argocd/tree/main/manifests) is as the name implies, where the manifests are stored. They're split based on what app manages them, along with a [templates](https://github.com/aegis-fate-gh/homelab-argocd/tree/main/manifests/template/base) folder.

Within each app folder are additional folders, with "base" being where the actual manifests used by Argo CD are stored.

There are a few additional pieces of baseline facts to note
1. MetalLB is used when pods are given static externally accessible IP addresses, that's configured [here](https://github.com/aegis-fate-gh/homelab/blob/main/Ansible/playbooks/jovian-prod/helm-base.yml#L36-L57)
2. Traefik is the ingress controller and reverse proxy, which is configured [here](https://github.com/aegis-fate-gh/homelab/blob/main/Ansible/playbooks/jovian-prod/helm-base.yml#L112-L241)
3. ArgoCD itself is configured [here](https://github.com/aegis-fate-gh/homelab/blob/main/Ansible/playbooks/jovian-prod/helm-base.yml#L377-L434)
4. Backups are handled via snapshots of the cephFS PV's configured [here](https://github.com/aegis-fate-gh/homelab/blob/main/Ansible/playbooks/jovian-prod/helm-base.yml#L266-L306)
5. Backups are then handled by Restic. The secrets used by Restic to connect to Backblaze are configured [here](https://github.com/aegis-fate-gh/homelab/blob/main/Ansible/playbooks/jovian-prod/helm-base.yml#L450-L470).  With the secrets created, a file named backup.yaml creates the replication source
6. Restores are also done via Ansible, which is demonstrated [here](https://github.com/aegis-fate-gh/homelab/blob/main/Ansible/tasks/jovian-prod/restic-restore.yml)
7. Prometheus is used for metrics, which is configured [here](https://github.com/aegis-fate-gh/homelab/blob/main/Ansible/playbooks/jovian-prod/helm-base.yml#L330-L359), and made usable by [Grafana](https://github.com/aegis-fate-gh/homelab-argocd/tree/main/manifests/jovian-prod/grafana)
8. Logging is handled by Grafana Alloy, which replaced Promtail. Alloy is managed by ArgoCD [here](https://github.com/aegis-fate-gh/homelab-argocd/tree/main/manifests/monitoring/grafana-alloy)
9. CephFS is persistent storage, and is configured within the Jovian cluster [here](https://github.com/aegis-fate-gh/homelab/blob/main/Ansible/playbooks/jovian-prod/helm-base.yml#L73-L110)
10. Secrets are currently managed [here](https://github.com/aegis-fate-gh/homelab/blob/main/Ansible/tasks/jovian-prod/env-secrets.yml) via Ansible