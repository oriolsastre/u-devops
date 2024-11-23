# Linux

## Alguns directoris importants

- Home: `/root, /home/username`
- User Executable: `/bin, /usr/bin, /usr/local/bin`
- System executables: `/sbin, /usr/sbin, /usr/local/sbin`
- Other mountpoints: `/media, /mnt`
- Configuration: `/etc`
- Temporary files: `/tmp`
- Kernels and Bootloader: `/boot`
- Server Data: `/var, /srv`
  - Logs: `/var/log`
- System information: `/proc, /sys`
- Shared libraries: `/lib, /usr/lib, /usr/local/lib`

## Terminal

- `[vagrant@localhost ~]$`
  - usuari@hostname.
  - `~`: Home directory (`/home/vagrant`).
  - `$`: Normal user shell.
- `[root@localhost ~]#`
  - root@hostname
  - `~`: Home directory (`/root`).
  - `#`: Root shell.

Puc canviar el hostname canviant el fitxer `/etc/hostname`. I `hostname <new_hostname>`

## Algunes ordres

- `pwd` Present working directory.
- `cat` Imprimeix el contingut d'un fitxer.
- `sudo -i` Canviem a usuari root.
- `file` Per veure quin tipus de fitxer és. Tot són fitxers a Linux.
- `ln -s {destination} {new}` Creem un enllaç (link) a la destinació que diem.
  - `unlink {file}` Per defer l'enllaç.
- `free` Mostra la memòria.

### File system

- `mkdir` Crea una carpeta.
- `touch` Crea un fitxer buit o actualitzar el timestamp del fitxer.
  - `touch textfile.txt` Crea 1 fitxer.
  - `touch textfile{1..10}.txt` Crea 10 fitxer en aquest rang.
- `cp {origin} {destination}` Copia un fitxer.
  - `cp -r` Per moure una carpeta. Recursiu.
- `mv {origin} {destination}` Mou un fitxer. També puc reanomenar el fitxer.
- `rm {file}` Eliminar.

**Archiving**

`tar -czvf [file].tar.gz [origin]`

- `-c` Create
- `-x` Extreure (faríem `-xzvf`)
- `-z` Comprimir (zip)
- `-v` Verbose
- `-f` File

### Filtering

- `grep [PATTERNS] FILE` Busca cadena de text en fixer (`-i` ignore-case). Global Regular Expression Print.
- `less FILE` Llegeix un fitxer. Més interactiu que `cat` ja que `cat` només l'imprimeix.
- `more FILE` Relativament similar a `less`.
- `head [-##] FILE` Veure les primeres línies d'un fitxer.
- `tail [-##] FILE` El contrari.
  - `tail -f FILE` T'ensenya el final de forma dinàmica, per si es van afegint línies, per exemple en un fitxer de logs.
- `cut [OPTIONS] FILE`. Quan tenim delimitadors ben definits. Per exemple "," en un .csv.
  - `-d` indica el delimitador: `-d:` o `-d,`
  - `-f=LIST` field o columna: `-f1`, o `-f1,4`
- `sed -i 's/BUSCA/REEMPLAÇA[/g]' FILE`. `/g` per a fer-ho global i no només 1 vegada per línia. (Amb vim la ordre és similar `%s/STRING/STRING[/g]`). Amb `-i` apliques els canvis, sinó només els veus. Stream EDitor.
- `wc FILE` Word Count. `-c` caràcters, `-w` paraules, `-l` línies.
- `find PATH -name FILE`.

### Input/Output Redirecting

En general l'output és a la pantalla. Es mostra imprès.

- `>` Redirigim l'output. Exemple: `uptime > uptime.txt`. Si el fitxer no existeix, el creem; sinó, reescrivim.
- `>>` Append. No reescriu sinó que afageix. `1>>` default, `2>>` errors, `&>>` tot.

### Usuaris

| Tipus   | Exemple        | User ID (ID) | Group ID (GID) | Home dir       | Login Shell   |
| :------ | :------------- | :----------- | :------------- | :------------- | :------------ |
| ROOT    | root           | 0            | 0              | /root          | /bin/bash     |
| REGULAR | vagrant        | 1000-60000   | 1000-60000     | /home/username | /bin/bash     |
| SERVICE | ftp,ssh,apache | 1-999        | 1-999          | /var/username  | /sbin/nologin |

- `/etc/passwd` Conté informació d'usuaris.
- `/etc/shadow` Conté informació de les contrassenyes.
- `/etc/group` Conté informació dels grups d'usuaris.

Si fem `head -1 /etc/passwd` veiem la informació sobre el 1er usuari.

```
root:x:0:0:root:/root:/bin/bash
```

- `root` Nom d'usuari.
- `x` Referència al fitxer shadow on hi ha la contrassenya encriptada.
- `0` User ID.
- `0` Group ID.
- `root` Un comentari que es pot posar.
- `/root` El home directory.
- `/bin/bash` La login shell.

### Ordres

- `useradd USER` Afegim un usuari.
- `userdel USER` Elimina un usuari. `-r` Per eliminar-ne també el home directory.
- `groupadd GROUP` Afegim un grup.
- `id USER` Mostra informació d'un usuari.
- `passwd USER` Per (re)setejar la contrassenya.
- `last` Els últims usuaris que s'han loguejat.
- `whoami`
- `lsof -u USER` Fitxers oberts per aquest usuari.

### Permissions

`-rwxr-xr-x` Es separa en 1, 3, 3, 3. Els grups de tres són, en ordre, `rwx`: `r` read, `w` write, `x` execute.

- `-` Tipus de fitxer. `-` o `l`o `d`.
- 1er grup de tres. Permisos del usuari propietari.
- 2n grup de tres. Permisos del grup propietari.
- 3er grup de tres. Permisos per als altres usuaris.

- `chown USER:GROUP FILE` CHange OWNership.
- `chmod MODE FILE` CHange MODe. El mode inclou 3 parts.
  - `u, g, o` Per si modifiquem els permisos de User, Group o Other.
  - `+, -` Per si afegim o traiem permisos.
  - `r, w, x` El permís que modifiquem. També poden tenir un valor numèric: `r=4`, `w=2`, `x=1` de tal manera que podem definir els permisos numèricament.
    - Per posició definim `u,g,o` i podem dir: `chmod 640 FILE`. El usuari tindrà `rw- = 4+2`, el grup tindrà `r-- = 4` i els altres tindran `--- = 0`.

### Sudo

Amb `visudo` podem modificar l'arxiu qeu defineix quins usuaris tenen permís de `sudo`. Aquest fitxer es troba a `/etc/sudoers`.

```
USERNAME    ALL=(ALL)   NOPASSWD:   ALL
```

Amb `%GROUP` puc afegir un grup enlloc d'un usuari.

Amb `NOPASSWD:` no ens demana el propi password de l'usuari quan executem `sudo`.

Puc crear el meu propi fitxer de sudoers a `/etc/sudoers.d/`.

## Software management

Hi ha `rpm` i `dpkg` en funció de l'OS que fem servir. En els nostres casos, en funció del `centos`o del `ubuntu` que és debian.

Podem buscar paquets a: http://rpmfind.net/.

- `arch` per veure l'arquitectura del nostre ordinador.
  - `uname -m` també podria servir.

Ens podem baixar el paquet amb un `curl` i l'enllaç al paquet. `curl URL -o FILENAME`. O també amb `wget URL`.

Instal·lem amb `rpm -ivh PACKAGE`

- `i` Install.
- `v` Verbose
- `h` Human readable format.

Desinstal·lem amb `rpm -e PACKAGE` Erase.

---

Problema. Així manualment pot ser que volguem descarregar-nos un paquet i ens trobem que ens diu que necessita d'altres per a poder-se instal·lar. Dependències.

### yum/dnf

`yum search PACKAGE` i busquem el packet via yum.

`yum install PACKAGE`. Ens mostrarà i informarà de les dependències.

`dnf remove PACKAGE`. Ens desinstal·larà dependències que NO S'ESTAN USANT.

## Processes

Amb `top` veiem els processos que s'estan executant.
