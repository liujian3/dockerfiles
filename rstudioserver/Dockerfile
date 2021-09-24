ROM rstudio/r-base:4.1-centos8

RUN yum install wget initscripts compat-openssl10 -y

RUN wget https://download2.rstudio.org/rstudio-server-rhel-1.1.463-x86_64.rpm

RUN yum install rstudio-server-rhel-1.1.463-x86_64.rpm -y

RUN yum clean

RUN rm -f rstudio-server-rhel-1.1.463-x86_64.rpm

EXPOSE 8787
  
ENTRYPOINT ["/usr/lib/rstudio-server/bin/rserver"]
CMD ["--server-daemonize=0", "--server-app-armor-enabled=0"]
