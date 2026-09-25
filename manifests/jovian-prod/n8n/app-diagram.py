from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage, database
from diagrams.saas import automation
from diagrams.k8s.storage import PVC

with Diagram("APP", show=False, direction="TB"):
    with Cluster("Homelab"):
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: n8n"):
                        busybox = Custom("Busybox", "/app/icons/busybox.png")
                        n8n = automation.N8N("n8n")
                        db = database.Postgresql("Postgres")
                        n8n_runner = automation.N8N("n8n-runner")

                    n8n_pvc = storage.Ceph("n8n PVC")
                    db_pvc = storage.Ceph("DB PVC")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> n8n

    n8n >> n8n_pvc
    busybox >> n8n_pvc
    db >> db_pvc

    n8n >> n8n_runner
    n8n >> db
                