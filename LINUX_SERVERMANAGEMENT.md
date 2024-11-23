# Tomcat

1. Creem un usuari per a que gestioni el tomcat

   `useradd --home-dir /opt/tomcat --shell /sbin/nologin tomcat`

   És un usuari que es diu "tomcat" on li hem definit un home directori i no té accés a shell per seguretat, ja que no li cal.

2. Movem el que ens hem descarregat de tomcat (un tar que hem descomprimit) i li donem permisos.

   `cp -r apache-tomcat-[]/* /opt/tomcat/`

   `chown -R tomcat.tomcat /opt/tomcat/`

3. Creem el fitxer del nom del servei (ruta: `/etc/systemd/system/{servei}.service`)

   `vim /etc/systemd/system/tomcat.service`

```
[Unit]
Description=Tomcat
After=network.target // Dependència

[Service]
Type=forking // Pot iniciar child processes

User=tomcat // L'usuari que hem creat
Group=tomcat

WorkingDirectory=/opt/tomcat

Environment=JAVA_HOME=/usr/lib/jvm/jre

Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat

ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

[Install]
WantedBy=multi-user.target // Mode no GUI
```

    Aquest exemple de fitxer es pot buscar.

4. `systemctl daemon-reload` quan hem fet canvis al systemd file.
