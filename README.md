# DevOps

## Vagrant

Per automatitzar el procés de creació o configuració de màquines virtuals (VM).

Buscar boxes a: `https://portal.cloud.hashicorp.com/vagrant/discover`.

- Centos: eurolinux-vagrant/centos-stream-9
- Ubuntu: ubuntu/jammy64

### Ordres

- `vagrant init eurolinux-vagrant/centos-stream-9` Per crer el fitxer vagrant.
- `vagrant up` Per crear la VM.
- `vagrant box list` Per llistar les boxes descarregades.
- `vagrant status` Estatus de les VM en _aquesta_ carpeta.
- `vagrant global-status` Estatus de totes les VM. (`--prune`). Aquí hi puc veure, a més, la id de cada VM i interactuar amb ella directament sense haver d'estar al seu directori. Ordres com `ssh, halt, destroy, reload ${id}`.
- `vagrant ssh` Per fer login a la VM creada.
- `vagrant halt` Per aturar la VM.
- `vagrant reload` Per fer un reboot de la VM per si canviem coses al fitxer vagrant.
- `vagrant destroy` Per destruir la VM. Si obrim VirtualBox ja no la veurem. La Box que ens hem descarregat amb `vagrant init` la seguim tenint. Hem destruit la VM.
