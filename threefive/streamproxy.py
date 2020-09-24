from .splice import Splice
from .streamplus import StreamPlus
from functools import partial
import sys
import json

class StreamProxy(StreamPlus):
    '''
    Class threefive.StreamProxy
    writes scte35 data to sys.stderr
    Writes all packets to sys.stdout
    so you can parse the scte35
    and pipe the packets elsewhere.
    

    example: proxy.py
    ---------------------------------
    import threefive

    with open('vid.ts','rb') as tsdata:
        threefive.StreamProxy(tsdata).decode()
    ---------------------------------

    python3 proxy.py | mplayer -

    '''
    def decode(self,func = None):
        '''
        StreamProxy.decode() reads MPEG-TS
        writes all packets to sys.stdout
        writes scte35 data to sys.stderr
        '''
        for packet in iter( partial(self.tsdata.read, self.packet_size), b''):
            # Write every packet to stdout
            sys.stdout.buffer.write(packet)
            self.parse_header(packet) 
            if self.chk_magic(packet):
                cuep = Splice(packet,self.packet_data)
                if not func:
                    cuep.show()
                else:
                    func(cuep)
                    
             
                # Write SCTE-35 data to stderr (in green).

