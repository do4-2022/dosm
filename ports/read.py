import os
import psutil


def read_connexions():
    """
    Reads all inet connexions on the system.
    Returns a list of connexions with the following structure:
    [
        {
            'pid': 1,
            'name': "",
            'local_addr': "",
            'local_port': "",
            'remote_addr': "",
            'remote_port': "",
            'status': "",
            'type': < SOCK_STREAM | SOCK_DGRAM | SOCK_SEQPACKET >
        },
        ...
    ]
    """
    connexions = psutil.net_connections()

    out = []

    for con in connexions:

        name = "unknown"

        if (con.pid is not None):
            try:
                name = psutil.Process(con.pid).name()
            except:
                pass

        local_addr = "unknown"
        local_port = ""
        if (con.laddr != ()):
            local_addr = con.laddr.ip
            local_port = str(con.laddr.port)

        remote_addr = ""
        remote_port = ""
        if (con.raddr != ()):
            remote_addr = con.raddr.ip
            remote_port = str(con.raddr.port)

        out.append({
            'pid': con.pid,
            'name': name,
            'local_addr': local_addr,
            'local_port': local_port,
            'remote_addr': remote_addr,
            'remote_port': remote_port,
            'status': con.status,
            'type': con.type
        })
    return out


if __name__ == '__main__':

    print(read_connexions())

    # print(psutil.net_connections())
    # print(readProcs())
