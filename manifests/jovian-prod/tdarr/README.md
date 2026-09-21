#### Use Case
Tdarr started out as a solution to a few problems. 

1. Plex was having issues properly importing media files. While I created a dashboard in Grafana to track those issues via logs, the problem was too frequent to support spot fixes
2. Storage is expensive in 2026, as in 2x+ more expensive than when I built the Silo pair
3. Using handbrake with automatic conversion doesn't scale in an automated way

#### Architecture
Tdarr is set up in two separate layers, the server portion which is managed here via ArgoCD, and the individual LXC containers running the workers that live on the nodes and are managed with Proxmox. The latter does not have GPU access in the current iteration of my homelab.

Due to handbrakes memory usage causing it to be OOM killed both in K8s and on a docker host, I didn't want the Tdarr workers running within Kubernetes. More importantly, while the GPU access could be helpful, and the memory can be gated, LXC's were usable on all 5 nodes. The Jovian cluster is only on 3.

Shared Media storage is handled via the same UNAS-Pro servers that Plex and other media apps pull from.
#### Diagram
![Tdarr](app.png)
#### LXC Config / Setup process
Set up on one, duplicate LXC to other nodes, change config as needed
Install process: https://docs.tdarr.io/docs/installation/windows-linux-macos/

###### Tdarr Node Config
/root/Tdarr_Node/configs/Tdarr_Node_Config.json
```
{
  "nodeName": "EDIT_ME",
  "serverURL": "http://192.168.6.230:8266",
  "serverIP": "192.168.6.230",
  "serverPort": "8266",
  "handbrakePath": "",
  "ffmpegPath": "",
  "mkvpropeditPath": "",
  "pathTranslators": [
    {
      "server": "/media",
      "node": "/media"
    }
  ],
  "nodeType": "mapped",
  "unmappedNodeCache": "/root/Tdarr_Node/unmappedNodeCache",
  "logLevel": "INFO",
  "priority": -1,
  "cronPluginUpdate": "",
  "apiKey": "",
  "maxLogSizeMB": 10,
  "pollInterval": 2000,
  "startPaused": false
}
```

###### Fstab Entry
```
//IP_HERE/media /media cifs credentials=/etc/.smbcredentials,vers=3.0,iocharset=utf8 0 0
```

###### Service Entry
```
nano /etc/systemd/system/tdarr.service
```

###### tdarr.service file
```
[Unit]
Description=TDarr_Node
After=network.target

[Service]
Type=simple
ExecStart=/root/Tdarr_Node/Tdarr_Node/Tdarr_Node
User=root
Restart=always

[Install]
WantedBy=multi-user.target
```

###### Service Start
```
systemctl daemon-reload && systemctl enable tdarr.service && systemctl start tdarr.service
```

#### Flows
I make use of 3 flows
1. [AV1 Import](https://github.com/aegis-fate-gh/homelab-argocd/blob/main/manifests/jovian-prod/tdarr/flows/AV1%20Import.md) - The primary flow, this handles all downloaded media files, converting them to AV1 as needed. It then moves it to the needed directories for Sonarr and Radarr to pick them up, move them to their final destination, and notify Plex / Jellyfin to trigger library updates
2. [AV1 Replacer Radarr](https://github.com/aegis-fate-gh/homelab-argocd/blob/main/manifests/jovian-prod/tdarr/flows/AV1%20Replacer%20Radarr.md) - Goes through the already existing movie files and looks for files to convert. It replaces them only if the converted file is smaller than the starting file.
3. [AV1 Replacer Sonarr](https://github.com/aegis-fate-gh/homelab-argocd/blob/main/manifests/jovian-prod/tdarr/flows/AV1%20Replacer%20Sonarr.md) - Same process as the Radarr replacer, but for Sonarr sourced TV shows.

#### Source
https://github.com/haveagitgat/tdarr