import sys
sys.path.append('../gen-py')

from keyvalue import KeyValueService
from keyvalue.ttypes import GetRequest, GetResponse, SetRequest

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def main():
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)

    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = KeyValueService.Client(protocol)

    # Connect!
    transport.open()

    client.Set(SetRequest(key="shivam", val="mitra"))
    result = client.Get(GetRequest(key="shivam"))
    print(result.val)

    # Close!
    transport.close()


if __name__ == '__main__':
    try:
        main()
    except Thrift.TException as tx:
        print('%s' % tx.message)