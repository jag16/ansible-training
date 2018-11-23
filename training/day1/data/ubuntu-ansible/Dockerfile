FROM ubuntu:16.04

RUN apt-get update && apt-get install -y openssh-server python-minimal
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

COPY authorized_keys /root/.ssh/authorized_keys

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# Open port 22 for ssh and port 80 for any webserver
EXPOSE 22
EXPOSE 80 

# Configure SSH Server as the startup application
CMD ["/usr/sbin/sshd", "-D"]
