from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem.storage import Ceph
from diagrams.k8s.compute import Cronjob
from diagrams.k8s.storage import PVC

with Diagram("app", show=False, direction="TB"):
    with Cluster("Github"):
        github = Custom("Github", "/app/icons/github.png")
    with Cluster("Homelab"):
        unas_pro = Custom("UNAS-Pro", "/app/icons/unifi-drive.png")
        synology = Custom("Syn-Coruscant", "/app/icons/synology.png")
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Jobs"):
                        diagrams_runner = Cronjob("diagrams-repo-runner")
                        metadata = Cronjob("media-metadata-manager")
                        pruner = Custom("media-pruner", "/app/icons/busybox.png")
                        kometa = Custom("Kometa", "/app/icons/kometa.png")
                    plex = Custom("Plex", "/app/icons/plex.png")
                    smb = PVC("Media SMB PVC")
                    syn_smb = PVC("Synology SMB PVC")
                    kometa_pvc = Ceph("Kometa PVC")

    github - diagrams_runner
    unas_pro - Edge(color="black", style="solid") - smb - Edge(color="black", style="solid") - pruner
    synology << Edge(color="black", style="solid") << syn_smb << Edge(color="black", style="solid") << metadata
    kometa >> Edge(color="orange", style="bold", minlen="2") >> plex
    kometa_pvc >> Edge(color="darkorange", style="solid") >> kometa
