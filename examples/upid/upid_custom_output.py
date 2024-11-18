"""
Segmentation Upid Examples
"""

import threefive


ADID = "/DA4AAAAAAAA///wBQb+AKpFLgAiAiBDVUVJAAAAA3//AAApPWwDDEFCQ0QwMTIzNDU2SBAAABZE5vg="
UMID = "/DBDAAAAAAAA///wBQb+AA2QOQAtAitDVUVJAAAAA3+/BCAwNjBhMmIzNC4wMTAxMDEwNS4wMTAxMGQyMC4xEAEBRKI3vg=="
ISAN = "/DA4AAAAAAAA///wBQb+Lom5UgAiAiBDVUVJAAAABn//AAApPWwGDAAAAAA6jQAAAAAAABAAAHGXrpg="
TID2 = "/DAzAAAAAAAA///wBQb+AAQesAAdAhtDVUVJAAAAA3+/BwxNVjAwMDQxNDY0MDARAAAf8lPm"
AIRID = "/DBhAAAAAAAA///wBQb+qM1E7QBLAhdDVUVJSAAArX+fCAgAAAAALLLXnTUCAAIXQ1VFSUgAACZ/nwgIAAAAACyy150RAAACF0NVRUlIAAAnf58ICAAAAAAsstezEAAAihiGnw=="
ADI = "/DBEAAAAAAAA///wBQb+AFJlwAAuAixDVUVJYgAFin+/CR1TSUdOQUw6My1zUTROZ0ZUME9qUHNHNFdxVVFvdzUAAEukzlg="
EIDR = "/DA4AAAAAAAA///wBQb+AKpFLgAiAiBDVUVJAAAAA3//AAApPWwKDDB4MTQ3OGY4NWFlMRAAAGXOtak="
ATSC = "/DA4AAAAAAAA///wBQb+QjoOtgAiAiBDVUVJAAAAA3//AAApPWwLDADx7/9odW1hbjAxMhAAABdHvhE="
MPU = "/DCSAAAAAAAAAP/wBQb/RgeVUgB8AhdDVUVJbs6+VX+/CAgAAAAABy0IxzELGQIXQ1VFSW7MmIh/vwgIAAABGDayFhE3AQECHENVRUluzw0If/8AABvLoAgIAAAAAActVhIwDBkCKkNVRUluzw02f78MG1JUTE4xSAEAAAAAMTM3NjkyMDI1NDQ5NUgxAAEAAGnbuXg="
MID = "/DA9AAAAAAAAAACABQb+0fha8wAnAiVDVUVJSAAAv3/PAAD4+mMNEQ4FTEEzMDkICAAAAAAuU4SBNAAAPIaCPw=="
ADS2 = "/DBUAAAAAAAA///wBQb+Lom5UgA+AjxDVUVJAAAAC3+/Di1BRFMtVVBJRDphYTg1YmJiNi01YzQzLTRiNmEtYmViYi1lZTNiMTNlYjc5OTkRAAAO7LCw"



dmesg = [
    ADID,
    UMID,
    ISAN,
    TID2,
    AIRID,
    ADI,
    EIDR,
    ATSC,
    MPU,
    MID,
    ADS2,
]

ids = []


def stuff(t, upid, uname):
    if t not in ids:
        ids.append(t)
        print(f"\033[92m{hex(t)}\033[0m : {upid} {uname}")


for m in dmesg:
    tf = threefive.Cue(m)
    tf.decode()
    print(tf.xml(binary=True))
    _ = [stuff(d.segmentation_upid_type, d.segmentation_upid, d.segmentation_upid_type_name) for d in tf.descriptors]
