# Ansible Playbooks
![Ansible](https://upload.wikimedia.org/wikipedia/commons/0/05/Ansible_Logo.png)

This directory contains Ansible playbooks for deploying and managing containers platform.
* Setting the Timezone
  * setup_0_timezone.yml - Sets the timezone to America/Arizona
* Accessing Network Attached Storage (NAS)
  * setup_1_smb.yml - Installs cifs-utils and configures Samba server access
* Docker
  * setup_2_docker.yml - Installs Docker and configures Docker daemon and Container Registry access
* Watchtower
  * setup_3_watchtower.yml - Installs Watchtower and configures Watchtower to automatically update containers and email notifications
* Portainer
  * setup_4_portainer.yml - Installs Portainer and configures Portainer to manage containers
* Cloudflare
  * setup_5_cloudflare.yml - Installs Cloudflare and maps hostnames to ports.
* CNames
  * setup_8_cnames.yml - Creates CNames for hostnames
* Containers
  * setup_9_containers.yml - Installs students' containers