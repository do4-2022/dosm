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

        # Parse name and pid

        name = "unknown"
        pid = "unknown"
        if (con.pid is not None):
            try:
                pid = con.pid
                name = psutil.Process(con.pid).name()
            except:
                pass

        # Parse local address and port

        local_addr = ""
        local_port = ""
        if (con.laddr != ()):
            local_addr = con.laddr.ip
            local_port = str(con.laddr.port)

        # Parse remote address and port

        remote_addr = ""
        remote_port = ""
        if (con.raddr != ()):
            remote_addr = con.raddr.ip
            remote_port = str(con.raddr.port)

        # Parse connexion type

        con_type = "unknown"

        if (con.type.name == "SOCK_STREAM"):
            con_type = "TCP"
        elif (con.type.name == "SOCK_DGRAM"):
            con_type = "UDP"
        elif (con.type.name == "SOCK_SEQPACKET"):
            con_type = "SCTP"

        # Parse status

        status = con.status

        out.append({
            'pid': pid,
            'name': name,
            'local_addr': local_addr,
            'local_port': local_port,
            'remote_addr': remote_addr,
            'remote_port': remote_port,
            'status': status,
            'type': con_type
        })
    return out
