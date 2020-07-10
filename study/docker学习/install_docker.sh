#!/bin/bash
# 设置下载源
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak
#curl -o /etc/yum.repos.d/CentOS-Base-Ali.repo http://mirrors.aliyun.com/repo/Centos-7.repo
#curl -o /etc/yum.repos.d/CentOS-Base-163.repo https://mirrors.163.com/.help/CentOS7-Base-163.repo
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
curl -o /etc/yum.repos.d/Docker-ce-Ali.repo https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

yum makecache

# 安装Docker
yum -y install --setopt=obsoletes=0 docker-ce-18.09.1-3.el7 
# 启动 Docker 并设置开机启动
systemctl start docker && systemctl enable docker
##安装docker-compose
yum install -y docker-compose
