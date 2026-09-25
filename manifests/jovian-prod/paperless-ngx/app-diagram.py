from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom
from diagrams.onprem import network, storage, database, inmemory
from diagrams.k8s.storage import PVC

with Diagram("APP", show=False, direction="TB"):
    with Cluster("Backblaze"):
        backblaze = Custom("Backups", "/app/icons/backblaze.png")
    with Cluster("Homelab"):
        with Cluster("Eos"):
            with Cluster("k3s"):
                with Cluster("Namespace: jovian-prod"):
                    with Cluster("Pod: paperless"):
                        paperless = Custom("Paperless-ngx", "/app/icons/paperless-ngx.png")
                        redis = inmemory.Redis("Redis")
                        db = database.Postgresql("Postgres")
                        gotenberg = Custom("Gotenberg", "/app/icons/gotenberg.png")
                        tika = Custom("Apache Tika", "/app/icons/apache-tika.png")

                    backup = Custom("Backups", "/app/icons/restic.png")
                    paperless_pvc = storage.Ceph("n8n PVC")
                with Cluster("Namespace: kube-system"):
                    traefik = network.Traefik("Traefik\nInternal Proxy")

    traefik >> Edge(color="blue", style="dotted") >> paperless
    backblaze << Edge(color="black", style="solid") << backup << Edge(color="black", style="solid") << paperless_pvc

    paperless >> paperless_pvc
    redis >> paperless_pvc
    db >> paperless_pvc
    paperless >> redis
    paperless >> db
    paperless >> gotenberg
    paperless >> tika


                