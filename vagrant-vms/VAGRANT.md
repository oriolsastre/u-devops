# Vagrant

Per automatitzar el procés de creació o configuració de màquines virtuals (VM).

Buscar boxes a: `https://portal.cloud.hashicorp.com/vagrant/discover`.

- Centos: eurolinux-vagrant/centos-stream-9
- Ubuntu: ubuntu/jammy64

## Ordres

- `vagrant init eurolinux-vagrant/centos-stream-9` Per crer el fitxer vagrant.
- `vagrant up` Per crear la VM.
- `vagrant box list` Per llistar les boxes descarregades.
- `vagrant status` Estatus de les VM en _aquesta_ carpeta.
- `vagrant global-status` Estatus de totes les VM. (`--prune` per a eliminar registres). Aquí hi puc veure, a més, la id de cada VM i interactuar amb ella directament sense haver d'estar al seu directori. Ordres com `ssh, halt, destroy, reload ${id}`.
- `vagrant ssh` Per fer login a la VM creada.
- `vagrant halt` Per aturar la VM.
- `vagrant reload` Per fer un reboot de la VM per si canviem coses al fitxer vagrant.
- `vagrant destroy` Per destruir la VM. Si obrim VirtualBox ja no la veurem. La Box que ens hem descarregat amb `vagrant init` la seguim tenint. Hem destruit la VM.
- `vagrant provision` Per tornar a forçar l'execusió de les ordres de provisioning.

## Sync folders

`config.vm.synced_folder "<host_route>" "<guest_route>"`

En windows la ruta del host posaríem: `"C:\\Users\\Oriol\\IT\\..."`.

En MacOS seria: `"/Users/Oriol/IT/..."`.

## Provisioning

Per executar scripts i order quan s'obre la VM per **1a** vegada. També se'n diu "_bootstraping_". A AWS pot ser que es digui "_user data_"

Al Vagrant file hi trobem, al final, la secció:

```
config.vm.provision "shell", inline: <<-SHELL
  <ordres>
SHELL
```

Aquí posem les ordres que volem que s'executin quan creem la VM. Per exemple: `yum install httpd wget unzip git -y` per instal·lar allò que volem que hi sigui a la VM. **Notar** el `-y`. Volem que les ordres que hi executem **NO** siguin interactives, sinó fallaria.

Per a tornar a provisionar, podríem fer servir les ordres `vagrant provision` o fer servir la flag `--provision` per forçar tornar a excutar les ordres.

#### Apunts

IAC: Infrastructure As Code
