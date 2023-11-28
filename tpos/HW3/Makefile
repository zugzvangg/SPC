build_ubuntu:
	docker build -f Dockerfile_ubuntu -t ubuntu_custom .

build_centos:
	docker build -f Dockerfile_centos -t centos_custom .

d_centos:
	docker exec -d -it --privileged 3e7e6bc64394 /usr/sbin/init