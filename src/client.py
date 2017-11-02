#!/usr/bin/env python

import socket

def recv_until(conn, str):
	buf = ''
	while not str in buf:
		buf += conn.recv(1)
	return buf

def getValidSubnet(host):
	return host + '/32'

def countHosts(subnet):
	# get the number of zeros from subnet
	tail = subnet.find('/') + 1
	zeroes = 32 - int(subnet[tail:])
	# make 2^zeroes
	if(zeroes > 0):
		hosts = 1 << zeroes
	else:
		hosts = 1
	# print hosts
	return str(hosts)

def isSubnetValid(subnet, host):
	subnetAddress = subnet[:subnet.find('/')]
	subnetSplitted = subnetAddress.split('.')
	binarySubnet = str('{0:08b}'.format(int(subnetSplitted[0]))) + str('{0:08b}'.format(int(subnetSplitted[1]))) + str('{0:08b}'.format(int(subnetSplitted[2]))) + str('{0:08b}'.format(int(subnetSplitted[3])))
	a = (long(binarySubnet,2))
	
	hosts = int(subnet[subnet.find('/')+1:])
	x = ''
	for i in range(0, hosts):
		x = x + '1'
	for i in range(0, 32-hosts):
		x = x + '0'
	x = (long(x,2))
	
	subnetSplitted = host.split('.')
	binarySubnet = str('{0:08b}'.format(int(subnetSplitted[0]))) + str('{0:08b}'.format(int(subnetSplitted[1]))) + str('{0:08b}'.format(int(subnetSplitted[2]))) + str('{0:08b}'.format(int(subnetSplitted[3])))
	b = (long(binarySubnet,2))
	
	res = ''
	subnetSubtring = (str(bin(b & x)))
	subnetHost = (str(bin(a & x)))

	if(subnetSubtring == subnetHost):
		res = 'T'
	else:
		res = 'F'
	return res
	
TCP_IP = 'hmif.cf'
TCP_PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = recv_until(s, 'NIM: ')
nim = raw_input(data)
s.send(nim + '\n')

data = recv_until(s, 'Verify NIM: ')
nim = raw_input(data)
s.send(nim + '\n')

print recv_until(s, '\n')[:-1]

# Phase 1
for i in range(100):
	recv_until(s, 'Host: ')
	host = recv_until(s, '\n')[:-1]
	recv_until(s, 'Subnet: ')
	s.send(getValidSubnet(host) + '\n')
	#print i
print recv_until(s, '\n')[:-1]

# Phase 2
for i in range(100):
	recv_until(s, 'Subnet: ')
	subnet = recv_until(s, '\n')[:-1]
	recv_until(s, 'Number of Hosts: ')
	s.send(countHosts(subnet) + '\n')
	#print i
print recv_until(s, '\n')[:-1]

# Phase 3
for i in range(100):
	recv_until(s, 'Subnet: ')
	subnet = recv_until(s, '\n')[:-1]
	recv_until(s, 'Host: ')
	host = recv_until(s, '\n')[:-1]
	#print subnet
	#print host
	s.send(isSubnetValid(subnet, host) + '\n')
print recv_until(s, '\n')[:-1]

s.close()
