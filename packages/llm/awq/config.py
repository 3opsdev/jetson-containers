
from jetson_containers import L4T_VERSION

if L4T_VERSION.major <= 32:
    print('-- disabling AWQ package on JetPack 4')
    package = None