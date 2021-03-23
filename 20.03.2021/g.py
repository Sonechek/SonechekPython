T,K = map(int,input().split(' '))

def check_servers(T,K,servers):
    servers = [0 for i in range(servers)]
    task = 1
    servers[servers.index(0)] = T
    while 0 in servers:
        if task % K != 0:
            servers[servers.index(0)] = T
        if task % K == 0:
            servers[servers.index(0)] = T * 2
        task += 1 
        for i in range(len(servers)):
            if servers[i] != 0:
                servers[i] -= 1
        if task > T + 100:
            if 0 in servers:
                return True
            else:
                return None


servers_c = T 
output = None
while output == None:
    servers_c += 1
    output = check_servers(T,K,servers_c)
print(servers_c)