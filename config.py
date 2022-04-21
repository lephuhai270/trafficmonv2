PREFIX_CHECKER_DEBUG = True
AS_EXPLORER_DEBUG = False
TRAFFMON_DEBUG = False

NFSEN_URL = "https://nfsen.apac.iptp.net"
NFSEN_USERNAME = "traffmon"
NFSEN_PASSWORD = "nI^3!4JE1Pxi$FHj2Qpp&lOQ"

AS_EXPLORER_CACHE_EXPIRATION_INTERVAL = 60 * 60 * 24 # In seconds, 24h by default

# For some reason now most of suspicious traffic in r0.f1k12 moved from
# as 0 to as 3549. Bolivia still only shows AS 0. We are adding this
# to also check for results in AS 3549
# We could also fix this by simply adding 3549 to the as 0 fix filer
# (or src as 3549). But we will keep this in order to monitor its behaviour.
# IMPORTANT: this increased taken time from 54/80 seconds to 150/140 seconds
# for the traffmon.py script.
# Maybe we could also add the 'bad traffic' to the DB. Not doing it for now.

# Use AS 0 only by default
BAD_AS_LIST = []


GOOGLE = {"name": "Google", 'match':"15169"}
FACEBOOK = {"name": "Facebok", 'match':"32934"}
AKAMAI = {"name": "Akamai", 'match':"20940"}
NETFLIX = {"name": "Netflix", 'match':"2906"}
AMAZON = {"name": "Amazon", 'match':"16509"}
LEVEL3 = {"name": "Level 3", 'match':"3356", "priority": 1}
ORACLE = {"name": "ORACLE", 'match':"31898"}
CLOUDFLARE = {"name": "Cloudflare", 'match':"13335"}
ROBLOX = {"name": "Roblox", 'match':"22697"}
HIGHWINDS = {"name": "Highwinds", 'match':"20446"}
MEDIAFIRE = {"name": "Mediafire", 'match':"46179"}
LLNW = {"name": "Limelight", 'match':"22822"}
ZNET = {"name": "Zenlayer", 'match':"21859"}
CACHENETWORKS = {"name": "Cache Networks", 'match':"30081"}
GCORE = {"name": "GCORE", 'match':"199524"}
CDS = {"name": "Capitalonline", 'match':"63199"}
CMC = {"name": "CMCTelecom", 'match':"45903"}
READYSERVER = {"name": "ReadyServer", 'match':"63930"}
ASIAWEB = {"name": "AsiaWeb", 'match':"55639"}
NETSEC = {"name": "Netsec", 'match':"45753"}
CHINANET = {"name": "CHINANET-SH-AP", 'match':"4812"}
ZOOM1 = {"name": "ZOOM-1", 'match':"30103"}
NOINFOAS = {"name": "NO_INFO-AS", 'match':"0"}
APPLE = {"name": "APPLE-ENGINEERING", 'match':"714"}
IANAASTRANS = {"name": "IANA-ASTRANS", 'match':"23456"}
CMNET = {"name": "CMNET-GD", 'match':"9808"}
HYUNDAIKR = {"name": "HYUNDAI-KR", 'match':"4670"}
AKAMAIAS = {"name": "AKAMAI-AS", 'match':"16625"}
HKTLimited = {"name": "HKTIMS-AP", 'match':"4760"}
SINGTEL = {"name": "SINGTEL-AS-AP", 'match':"7473"}
SINGNET = {"name": "SINGNET", 'match':"3758"}
CLOUDFLARENET = {"name": "CLOUDFLARENET", 'match':"13335"}
TaiwanMobile = {"name": "taiwanmobile-as", 'match':"24158"}
HKCOLO = {"name": "GLOBAL-TRANSIT-AS-HKCOLO-AP", 'match':"23749"}
SUPERCLOUDS = {"name": "SUPERCLOUDSLIMITED-AS-AP", 'match':"138571"}
MS8068 = {"name": "MICROSOFT-CORP-MSN-AS-BLOCK", 'match':"8068"}
SHINJIRU = {"name": "SHINJIRU-MY-AS-AP", 'match':"45839"}
HTC= {"name": "HTCHCMC-AS-VN", 'match':"24088"}
LayerStack= {"name": "XIM-HK", 'match':"133322"}
LayerStackLimited= {"name": "LAYER-AS", 'match':"133380"}
PTMulkan= {"name": "MULKAN-AS-ID", 'match':"141062"}
Netnam= {"name": "NETNAM-AS-AP", 'match':"24173"}
VIB= {"name": "VIB-AS-VN", 'match':"131343"}
TMA= {"name": "TMASOLUTIONS-AS-VN", 'match':"56155"}
NITECO= {"name": "NITECO-AS-VN", 'match':"131380"}
UK2Limited= {"name": "UK2NET-AS", 'match':"13213"}
###############CHINA###########
CU1 = {"name": "ChinaUnicomBackbone", 'match':"4837"}
CU2 = {"name": "ChinaUnicomShanghai", 'match':"17621"}
CT = {"name": "CHINANET-BACKBONE", 'match':"4134"}
GRANSY= {"name": "Gransy", 'match':"60592"}
ASCN2 = {"name": "CHINATELECOM-CORE-WAN-CN2", 'match':"4809"}
Alibaba= {"name": "ALIBABA-CN-NET", 'match':"45102"}
AARNet= {"name": "AARNET-AS-AP", 'match':"7575"}
SMARTBRO= {"name": "SMARTBRO-PH-AP", 'match':"10139"}
CONVERGE= {"name": "CONVERGE-AS", 'match':"17639"}

#######################UPLINK_INTERFACE########################

###HONG KONG###
PCCWCU = {"name": "PCCW EQ CU", "match": "123"}
PCCWCT1 = {"name": "PCCW EQ CT1", "match": "137"}
PCCWCT2 =  {"name": "PCCW EQ CT2", "match": "138"}

CHINA_UPLINKS_EQ = [PCCWCU, PCCWCT1, PCCWCT2]

PCCWCU = {"name": "PCCW MEGAI CU", "match": "63"}
PCCWCT1 = {"name": "PCCW MEGAI CT1", "match": "62"}
PCCWCT2 =  {"name": "PCCW MEGAI CT2", "match": "59"}
CU10099 =  {"name": "CU10099 MEGAI", "match": "406"}

CHINA_UPLINKS_MEGAI = [PCCWCU, PCCWCT1, PCCWCT2, CU10099]
###############

###############################################################
AS_LIST = [GOOGLE, FACEBOOK, AKAMAI, NETFLIX, SHINJIRU, AMAZON, LEVEL3, ORACLE, CLOUDFLARE, ROBLOX, HIGHWINDS, MEDIAFIRE, LLNW, ZNET, CACHENETWORKS, GCORE, CDS, CMC, CU1, CU2, CT, GRANSY, READYSERVER, ASIAWEB, NETSEC, CHINANET, ZOOM1, NOINFOAS, APPLE, IANAASTRANS, CMNET, HYUNDAIKR, AKAMAIAS, HKTLimited, SINGTEL, SINGNET, CLOUDFLARENET, TaiwanMobile, HKCOLO, SUPERCLOUDS, ASCN2, MS8068, HTC, LayerStack, PTMulkan, Netnam, LayerStackLimited, UK2Limited, VIB, TMA, NITECO, Alibaba, AARNet, SMARTBRO, CONVERGE]

#####################HONG KONG DOWN ############################
HSIP_DOWN_FILTER = {"name": "EEHK", "interface": "255", "resources": {"as_down_src": {"query":{"filter": "in if 255", "stattype": 11}}}}
HK_IX_FILTER = {"name": "HKIX", "interface": "253", "resources": {"as_down_src": {"query":{"filter": "in if 253", "stattype": 11}}}}
PCCW_HK_EQ = {"name": "PCCW_HK1", "interface": "122", "resources": {"as_down_src": {"query":{"filter": "in if 122", "stattype": 11}}}}
CDSEquinixICT2 = {"name": "CDSEquinixICT2", "interface": "138", "resources": {"as_down_src": {"query":{"filter": "out if 138", "stattype": 11}}}}
CDSEquinixICU = {"name": "CDSEquinixICU", "interface": "123", "resources": {"as_down_src": {"query":{"filter": "out if 123", "stattype": 11}}}}
CDSEquinixICT1 = {"name": "CDSEquinixICT1", "interface": "137", "resources": {"as_down_src": {"query":{"filter": "out if 137", "stattype": 11}}}}

PERU_DOWN_INTERFACES = [HSIP_DOWN_FILTER, HK_IX_FILTER, PCCW_HK_EQ, CDSEquinixICT2, CDSEquinixICU, CDSEquinixICT1]
PERU_DOWN_RESOURCES = {"as_down_src": AS_LIST}

#########################CHINA EQUINIX USAGE##############################

Cataleya_SGP_GSW = {"name": "Cataleya_SGP_GSW_HK101", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 103.242.75.184/29 or src net 103.242.75.176/29 or src net 103.242.75.144/28 or src net 103.242.75.37/31", "stattype": 9}}}}

Cataleya_SGP_EQ_HK101 = {"name": "Cataleya_SGP_EQ_HK101", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.242.74.7 or src net 103.242.74.8/29 or src net 103.242.74.16/30 or src net 103.242.74.20/31 or src ip 103.242.74.22 or src net 103.242.74.88/29 or src net 103.242.74.96/30 or src net 103.242.74.176/29 or src net 103.242.74.224/28 or src net 103.242.74.248/29", "stattype": 9}}}}

##### UMBRA Technologies(HK) Limited #####

UMBRA_HK_101 = {"name": "UMBRA_HK_101", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.242.72.67 or src net 103.242.72.68/30 or src ip 103.242.72.72 or src net 103.6.130.238/31", "stattype": 9}}}}

SOF_150462_HK01 = {"name": "SOF_150462_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 103.6.130.238/31 or src net 103.6.130.240/30 or src net 103.6.130.244/31 or src ip 103.6.130.246", "stattype": 9}}}}

SOF_183127_HK01 = {"name": "SOF_183127_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.242.72.67 or src net 103.242.72.68/30 or src ip 103.242.72.72", "stattype": 9}}}}

SOF_190800_HK01 = {"name": "SOF_190800_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 103.242.72.139/31 or src net 103.242.72.140/30 or src net 103.242.72.144/29 or src net 103.242.72.152/31 or src ip 103.242.72.154", "stattype": 9}}}}

SOF_353882_1_HK01 = {"name": "SOF_353882-1_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.128.3 or src ip 103.6.128.15 or src ip 103.6.128.17 or src net 103.6.128.30/31 or src ip 103.6.128.32 or src net 103.6.128.102/31 or src net 103.6.128.104/30 or src net 103.6.128.108/31 or src ip 103.6.128.113 or src ip 103.6.128.114", "stattype": 9}}}}

SOF_353882_2_HK01 = {"name": "SOF_353882_2_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.128.135 or src ip 103.6.128.141 or src ip 103.6.128.159 or src ip 103.6.128.160 or src ip 103.6.128.199 or src ip 103.6.128.202 or src ip 103.6.128.218 or src net 103.6.128.136/31 or src net 103.6.128.142/31 or src net 103.6.128.194/31 or src net 103.6.128.204/30", "stattype": 9}}}}

ICM_HK101 = {"name": "ICM_HK101", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.128.138 or src ip 103.145.2.77 or src ip 103.145.2.79 or src ip 103.6.128.228 or src ip 103.242.75.47 or src ip 103.145.3.5 or src ip 91.194.117.74", "stattype": 9}}}}

FXDirect_HK101 = {"name": "FXDirect_HK101", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.130.85 or src net 103.6.130.86/31 or src net 103.6.130.88/31 or src ip 103.6.130.90 or src net 103.6.130.134/31 or src net 103.6.130.136/31  or src ip 103.6.130.138", "stattype": 9}}}}

Rational_HK101 = {"name": "Rational_HK101", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.130.145 or src ip 103.6.130.146 or src ip 103.6.130.148", "stattype": 9}}}}

SIMS_HK01 = {"name": "SIMS_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 27.123.0.0/21 or src net 27.124.81.0/24 or src net 27.124.82.0/24 or src net 27.124.83.0/24 or src net 27.124.85.0/24 or src net 27.124.90.0/24 or src net 27.124.92.0/24 or src net 42.62.176.0/22 or src net 43.229.254.0/23 or src net 43.254.124.0/22 or src net 45.251.72.0/22 or src net 49.128.184.0/24 or src net 49.128.186.0/24 or src net 103.3.58.0/23 or src net 103.9.124.0/22 or src net 103.11.106.0/23 or src net 103.18.28.0/22 or src net 103.24.72.0/22 or src net 103.25.110.0/24 or src net 103.28.224.0/22 or src net 103.29.184.0/24 or src net 103.29.184.0/23 or src net 103.29.185.0/24 or src net 103.30.244.0/22 or src net 103.31.204.0/23 or src net 103.31.206.0/24 or src net 103.37.168.0/22 or src net 103.39.52.0/24 or src net 103.40.120.0/23 or src net 103.40.122.0/24 or src net 103.44.100.0/24 or src net 103.49.28.0/23 or src net 103.49.228.0/22 or src net 103.51.44.0/22 or src net 103.65.236.0/23 or src net 103.71.190.0/23 or src net 103.71.255.0/24 or src net 103.76.148.0/22 or src net 103.77.76.0/22 or src net 103.77.106.0/23 or src net 103.80.80.0/22 or src net 103.80.236.0/22 or src net 103.83.176.0/23 or src net 103.84.208.0/22 or src net 103.94.132.0/23 or src net 103.98.121.0/24 or src net 103.100.180.0/22 or src net 103.103.175.0/24 or src net 103.103.192.0/23 or src net 103.105.98.0/23 or src net 103.105.217.0/24 or src net 103.107.71.0/24 or src net 103.107.84.0/23 or src net 103.108.187.0/24 or src net 103.111.217.0/24 or src net 103.111.220.0/22 or src net 103.112.244.0/23 or src net 103.119.228.0/23 or src net 103.120.64.0/23 or src net 103.121.238.0/23 or src net 103.124.244.0/23 or src net 103.125.13.0/24 or src net 103.125.16.0/22 or src net 103.129.205.0/24 or src net 103.131.104.0/23 or src net 103.132.19.0/24 or src net 103.133.20.0/23 or src net 103.134.18.0/23 or src net 103.135.227.0/24 or src net 103.136.182.0/24 or src net 103.137.37.0/24 or src net 103.138.68.0/23 or src net 103.139.120.0/24 or src net 103.141.20.0/23 or src net 103.141.40.0/23 or src net 103.142.224.0/24 or src net 103.143.4.0/23 or src net 103.143.194.0/24 or src net 103.145.68.0/23 or src net 103.146.30.0/24 or src net 103.147.6.0/24 or src net 103.147.53.0/24 or src net 103.147.72.0/23 or src net 103.147.82.0/23 or src net 103.147.84.0/23 or src net 103.147.246.0/23 or src net 103.148.18.0/23 or src net 103.148.24.0/24 or src net 103.148.28.0/23 or src net 103.149.238.0/23 or src net 103.151.22.0/23 or src net 103.151.34.0/23 or src net 103.152.63.0/24 or src net 103.152.118.0/23 or src net 103.152.238.0/23 or src net 103.153.134.0/23 or src net 103.153.136.0/23 or src net 103.153.148.0/23 or src net 103.153.229.0/24 or src net 103.153.248.0/23 or src net 103.155.106.0/23 or src net 103.155.156.0/24 or src net 103.155.167.0/24 or src net 103.155.191.0/24 or src net 103.155.196.0/23 or src net 103.156.128.0/24 or src net 103.156.132.0/23 or src net 103.156.232.0/23 or src net 103.156.233.0/24 or src net 103.157.78.0/23 or src net 103.157.102.0/24 or src net 103.158.130.0/24 or src net 103.158.252.0/23 or src net 103.159.222.0/23 or src net 103.160.18.0/23 or src net 103.160.62.0/23 or src net 103.160.178.0/23 or src net 103.160.201.0/24 or src net 103.160.202.0/23 or src net 103.160.205.0/24 or src net 103.161.62.0/23 or src net 103.161.130.0/23 or src net 103.162.54.0/24 or src net 103.162.63.0/24 or src net 103.162.106.0/24 or src net 103.162.144.0/23 or src net 103.163.13.0/24 or src net 103.163.228.0/23 or src net 103.164.186.0/23 or src net 103.164.235.0/24 or src net 103.167.11.0/24 or src net 103.167.170.0/23 or src net 103.168.28.0/24 or src net 103.168.146.0/23 or src net 103.168.150.0/23 or src net 103.168.186.0/23 or src net 103.169.132.0/22 or src net 103.169.138.0/23 or src net 103.169.220.0/23 or src net 103.172.96.0/24 or src net 103.172.118.0/23 or src net 103.173.74.0/23 or src net 103.175.48.0/24 or src net 103.175.238.0/23 or src net 103.176.26.0/23 or src net 103.176.177.0/24 or src net 103.176.180.0/23 or src net 103.178.41.0/24 or src net 103.198.93.0/24 or src net 103.203.162.0/24 or src net 103.210.35.0/24 or src net 103.210.116.0/22 or src net 103.214.184.0/22 or src net 103.219.72.0/22 or src net 103.233.102.0/23 or src net 103.241.179.0/24 or src net 103.244.204.0/22 or src net 103.254.104.0/22 or src net 103.255.15.0/24 or src net 111.92.162.0/23 or src net 111.92.166.0/24 or src net 111.92.169.0/24 or src net 111.92.170.0/24 or src net 114.199.80.0/20 or src net 116.206.4.0/22 or src net 117.103.64.0/23 or src net 117.103.66.0/24 or src net 118.91.137.0/24 or src net 119.47.88.0/23 or src net 120.89.88.0/23 or src net 150.107.248.0/22 or src net 202.43.64.0/24 or src net 202.43.114.0/23 or src net 202.47.64.0/20 or src net 202.51.19.0/24 or src net 202.51.30.0/24 or src net 202.52.140.0/23 or src net 202.57.16.0/23 or src net 202.57.16.0/21 or src net 202.57.16.0/20 or src net 202.57.18.0/23 or src net 202.57.20.0/23 or src net 202.57.22.0/23 or src net 202.57.24.0/23 or src net 202.57.26.0/23 or src net 202.57.28.0/23 or src net 202.57.30.0/23 or src net 202.58.216.0/23 or src net 202.58.220.0/22 or src net 202.83.120.0/23 or src net 202.83.123.0/24 or src net 202.162.39.0/24 or src net 202.162.40.0/23 or src net 202.169.224.0/20 or src net 203.29.26.0/23 or src net 203.148.84.0/23 or src net 203.190.112.0/21 or src net 206.84.96.0/22 or src net 206.84.96.0/19 or src net 206.84.101.0/24 or src net 206.84.102.0/23 or src net 206.84.105.0/24 or src net 206.84.106.0/24 or src net 210.247.244.0/24", "stattype": 9}}}}

Forextime_HK01 = {"name": "Forextime_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 103.6.130.1/30 or src ip 103.6.130.4 or src ip 103.242.72.3 or src ip 103.242.72.4 or src ip 103.242.72.8 or src ip 103.242.72.10 or src ip 103.242.72.64 or src net 103.242.72.80/30 or src ip 103.242.72.87 or src ip 103.242.72.104 or src ip 103.242.72.155 or src net 103.242.72.164/30 or src net 103.242.72.168/31 or src net 103.242.72.184/30 or src ip 103.242.72.205 or src net 103.242.72.206/31 or src net 103.242.72.208/31 or src ip 103.242.72.211 or src net 103.242.72.212/30 or src ip 103.242.72.234 or src ip 103.6.128.63 or src ip 103.6.128.64 or src net 103.6.128.122/31 or src net 103.6.128.124/30 or src net 103.6.128.128/30 or src net 103.6.128.132/31 or src ip 103.6.128.134 or src net 103.6.128.152/30 or src net 103.6.128.156/31 or src ip 103.6.128.158 or src net 103.6.128.162/31 or src net 103.6.128.164/31 or src ip 103.6.128.180 or src net 103.6.128.196/31 or src ip 103.6.128.198 or src net 103.6.128.200/31 or src ip 103.6.128.203 or src ip 103.6.128.223 or src ip 103.6.128.225 or src ip 103.242.72.216 or src net 103.242.72.244/31 or src ip 103.242.72.246 or src ip 103.242.72.160", "stattype": 9}}}}

SwissQuote_HK01 = {"name": "SwissQuote_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 103.6.130.210/31 or src net 103.6.130.212/30 or src net 103.6.130.216/29 or src net 103.6.130.224/31", "stattype": 9}}}}

FxPro_HK01 = {"name": "FxPro_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 103.6.131.10/31 or src ip 103.6.131.12 or src net 103.6.130.140/31 or src ip 103.6.130.142 or src ip 103.6.130.147 or src ip 103.6.130.153 or src net 103.6.130.154/31 or src net 103.6.130.156/31 or src ip 103.6.128.79 or src ip 103.6.128.80 or src ip 103.6.128.90", "stattype": 9}}}}

###ZEAL CUSTOMER###

Zeal_HK01 = {"name": "Zeal_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.242.72.103 or src ip 103.242.75.122 or src ip 103.242.75.49 or src ip 103.217.163.129 or src ip 103.217.163.130 or src ip 176.56.180.147 or src ip 176.56.180.203 or src ip 103.6.130.91 or src ip 103.6.130.130 or src ip 103.6.130.131 or src ip 103.6.130.149 or src ip 103.6.130.227 or src ip 103.6.130.228 or src ip 103.6.130.229 or src ip 103.6.130.233 or src ip 103.6.130.248 or src ip 103.6.130.249 or src ip 176.56.160.177 or src ip 176.56.160.233 or src ip 176.56.160.236 or src ip 176.56.160.243 or src ip 103.6.129.37 or src ip 103.6.129.38 or src ip 103.145.2.39 or src net 103.145.2.40/29 or src net 103.145.2.48/29 or src ip 103.145.2.52 or src ip 103.145.2.53 or src ip 103.6.128.18 or src net 103.6.128.52/30 or src ip 103.6.128.77 or src ip 103.6.128.78 or src ip 103.6.128.97 or src ip 103.6.128.99 or src ip 103.6.128.151 or src ip 103.6.128.249", "stattype": 9}}}}

SOF_677078_HK01 = {"name": "SOF#677078_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.128.151 or src ip 103.6.128.18 or src ip 103.6.128.249 or src ip 103.6.128.77 or src ip 103.6.128.78", "stattype": 9}}}}

Exness_HK01 = {"name": "Exness_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.242.72.100 or src ip 103.242.72.11 or src net 103.242.72.12/30 or src net 103.242.72.16/29 or src net 103.242.72.24/30 or src ip 103.242.72.28 or src ip 103.242.72.29 or src ip 103.242.72.30 or src net 103.242.72.52/30 or src ip 103.242.72.56 or src ip 103.242.72.63 or src ip 103.6.128.110 or src ip 103.6.128.111 or src ip 103.6.128.112 or src ip 103.6.128.117 or src ip 103.6.128.118 or src ip 103.6.128.119 or src ip 103.6.128.120 or src ip 103.6.128.12 or src ip 103.6.128.229 or src ip 103.6.128.68 or src ip 103.6.128.76 or src ip 103.6.128.82 or src ip 103.6.128.83 or src net 103.6.128.84/30 or src ip 103.6.128.88 or src ip 103.6.128.91 or src net 103.6.128.92/30 or src ip 103.6.128.33 or src ip 103.6.128.34 or src ip 103.6.128.35 or src ip 103.6.128.36 or src ip 103.6.128.37 or src net 103.6.128.40/30 or src ip 103.6.128.49 or src ip 103.145.2.39 or src net 103.145.2.40/29 or src net 103.145.2.48/30 or src ip 103.145.2.52 or src ip 103.145.2.53 or src net 103.242.75.12/30 or src net 103.242.75.16/29 or src ip 103.242.75.24 or src ip 103.242.75.26 or src ip 103.242.75.27 or src net 103.242.75.28/30 or src ip 103.242.75.32 or src ip 103.242.75.33 or src ip 103.242.75.34 or src ip 103.242.75.42 or src ip 103.242.75.43 or src ip 103.242.75.49", "stattype": 9}}}}

Overonix_HK01 = {"name": "Overonix_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138)  and src ip 103.242.74.27 or src ip 103.242.74.57 or src ip 103.6.128.190 or src net 103.6.128.192/31 or src ip 103.6.128.47 or src ip 103.23.168.23 or src ip 103.23.168.24", "stattype": 9}}}}

Greenmile_HK01 = {"name": "Greenmile_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.242.72.75 or src ip 103.6.130.129 or src ip 103.6.130.64 or src ip 103.6.130.150 or src ip 220.158.132.213 or src ip 103.6.130.139 or src ip 103.242.75.61", "stattype": 9}}}}

Notesco_HK01 = {"name": "Notesco_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.242.72.216 or src ip 103.6.128.63 or src ip 103.6.128.64 or src ip 103.6.128.71 or src net 103.6.128.72/30 or src net 103.6.128.162/31 or src net 103.6.128.164/31 or src ip 103.6.128.180 or src net 103.6.128.196/31 or src ip 103.6.128.198 or src net 103.6.128.200/31 or src ip 103.6.128.203 or src ip 103.6.128.223 or src ip 103.6.128.225 or src ip 103.6.128.227 or src ip 103.6.130.69 or src ip 103.6.130.70 or src ip 103.6.130.82 or src ip 103.6.130.95 or src ip 103.6.130.96 or src ip 103.6.130.99 or src net 103.6.130.100/31 or src ip 103.6.130.105 or src net 103.6.130.106/31 or src net 103.6.130.108/30 or src ip 103.6.130.112 or src ip 103.6.130.121 or src net 103.6.130.122/31 or src net 103.6.130.124/30 or src ip 103.6.130.128 or src ip 103.6.130.144 or src ip 103.6.130.172 or src ip 103.6.130.182 or src ip 103.6.130.184 or src ip 103.6.130.198 or src ip 103.6.130.199 or src ip 103.6.130.200 or src ip 103.6.130.204 or src ip 103.6.130.205 or src ip 103.6.130.206 or src ip 103.6.130.208 or src ip 103.23.170.3 or src net 103.23.170.4/30 or src net 103.23.170.8/30 or src net 103.23.170.12/31 or src ip 103.23.170.14", "stattype": 9}}}}

Cheersum_HK01 = {"name": "Cheersum_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 103.6.130.74/31 or src ip 103.6.130.76", "stattype": 9}}}}

MakeCapital_HK01 = {"name": "MakeCapital_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.242.72.74", "stattype": 9}}}}

Algolia_HK01 = {"name": "Algolia_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.130.168", "stattype": 9}}}}

Muganbank_HK01 = {"name": "Muganbank_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.242.72.204", "stattype": 9}}}}

ForexClub_HK01 = {"name": "ForexClub_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.128.10 or src ip 103.6.128.20 or src ip 103.6.128.65 or src ip 103.6.128.66 or src ip 103.6.128.89 or src ip 103.6.128.115 or src ip 103.6.128.116 or src net 103.6.128.170/31 or src net 103.6.128.172/30 or src net 103.6.128.176/30 or src net 103.6.128.210/31 or src net 103.6.128.212/31 or src ip 103.6.128.241 or src net 103.6.128.242/31 or src net 103.6.128.244/31 or src ip 103.6.128.246", "stattype": 9}}}}

GameUAB_HK01 = {"name": "GameUAB_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.130.65 or src ip 103.6.128.39", "stattype": 9}}}}

GrandCapital_HK01 = {"name": "GrandCapital_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.130.93 or src ip 103.6.130.94 or src ip 103.6.130.226", "stattype": 9}}}}

Guruhosting_HK01 = {"name": "Guruhosting_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.242.72.79 or src ip 103.242.72.102 or src ip 103.242.72.162 or src ip 103.242.72.163 or src ip 103.242.72.217 or src ip 103.242.72.222 or src ip 103.242.72.223 or src ip 103.242.72.235 or src net 103.242.72.236/30 or src ip 103.242.72.240 or src ip 103.242.72.241 or src ip 103.242.72.242", "stattype": 9}}}}

Netsentia_HK01 = {"name": "Netsentia_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 220.158.132.0/29", "stattype": 9}}}}

WeTrade_HK01 = {"name": "WeTrade_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.130.79 or src ip 103.6.130.92 or src ip 103.217.160.67  or src ip 103.6.128.45", "stattype": 9}}}}

Gransy_HK01 = {"name": "Gransy_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.128.121 or src ip 103.145.3.2 or src ip 103.242.75.41 or src ip 103.217.160.63 or src ip 103.145.2.95 or src net 185.28.194.0/24 or src net 185.38.108.0/24", "stattype": 9}}}}

JINOM_HK01 = {"name": "JINOM_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 103.122.64.0/24 or src net 103.122.66.0/24 or src net 103.122.67.0/24", "stattype": 9}}}}

LINTAS_HK01 = {"name": "JINOM_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 27.54.116.0/22 or src net 27.121.86.0/24 or src net 43.230.28.0/22 or src net 43.230.155.0/24 or src net 43.241.148.0/22 or src net 43.247.20.0/23 or src net 43.247.20.0/22 or src net 43.247.22.0/23 or src net 43.252.104.0/24 or src net 43.252.106.0/23 or src net 43.252.236.0/22 or src net 43.254.124.0/22 or src net 49.0.0.0/22 or src net 103.4.174.0/23 or src net 103.4.243.0/24 or src net 103.11.21.0/24 or src net 103.11.222.0/24 or src net 103.18.76.0/22 or src net 103.20.188.0/22 or src net 103.20.196.0/23 or src net 103.22.240.0/22 or src net 103.23.234.0/23 or src net 103.25.208.0/22 or src net 103.28.112.0/22 or src net 103.28.224.0/23 or src net 103.28.224.0/22 or src net 103.28.226.0/23 or src net 103.30.180.0/22 or src net 103.31.232.0/22 or src net 103.60.180.0/22 or src net 103.66.69.0/23 or src net 103.76.200.0/22 or src net 103.78.106.0/24 or src net 103.79.91.0/24 or src net 103.80.88.0/23 or src net 103.81.246.0/24 or src net 103.81.248.0/23 or src net 103.97.4.0/22 or src net 103.100.27.0/24 or src net 103.100.96.0/24 or src net 103.100.246.0/24 or src net 103.105.190.0/24 or src net 103.105.216.0/24 or src net 103.107.144.0/22 or src net 103.108.128.0/22 or src net 103.115.36.0/22 or src net 103.124.8.0/24 or src net 103.126.28.0/24 or src net 103.126.30.0/24 or src net 103.132.236.0/24 or src net 103.138.76.0/24 or src net 103.139.76.0/23 or src net 103.140.130.0/23 or src net 103.141.156.0/23 or src net 103.144.126.0/24 or src net 103.144.146.0/24 or src net 103.145.14.0/23 or src net 103.148.24.0/23 or src net 103.148.79.0/24 or src net 103.213.128.0/22 or src net 103.225.172.0/24 or src net 103.225.175.0/24 or src net 103.245.136.0/23 or src net 110.5.96.0/23 or src net 110.5.96.0/22 or src net 110.5.96.0/21 or src net 110.5.96.0/20 or src net 110.5.98.0/23 or src net 110.5.100.0/22 or src net 110.5.104.0/21 or src net 110.50.83.0/24 or src net 110.50.84.0/22 or src net 112.78.40.0/21 or src net 114.141.48.0/21 or src net 117.121.205.0/23 or src net 119.18.152.0/21 or src net 123.253.232.0/22 or src net 124.40.248.0/21 or src net 124.158.176.0/20 or src net 150.107.140.0/22 or src net 180.211.88.0/21 or src net 182.54.140.0/23 or src net 202.46.80.0/22 or src net 202.46.144.0/22 or src net 202.46.152.0/21 or src net 202.51.198.0/24 or src net 202.51.214.0/24 or src net 202.56.164.0/22 or src net 202.62.12.0/22 or src net 202.73.24.0/24 or src net 202.73.26.0/23 or src net 202.75.96.0/24 or src net 202.75.99.0/24 or src net 202.75.101.0/24 or src net 202.75.104.0/22 or src net 202.75.109.0/24 or src net 202.75.111.0/24 or src net 202.80.208.0/21 or src net 202.80.216.0/22 or src net 202.91.24.0/21 or src net 202.93.128.0/20 or src net 202.145.8.0/21 or src net 202.147.192.0/20 or src net 202.149.128.0/21 or src net 202.149.148.0/22 or src net 202.150.160.0/20 or src net 203.57.24.0/23 or src net 203.84.152.0/21 or src net 203.161.16.0/24 or src net 203.161.18.0/23 or src net 203.161.20.0/23 or src net 203.174.8.0/21", "stattype": 9}}}}

MicroFox_HK01 = {"name": "MicroFox_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 103.6.128.56/31 or src ip 103.6.128.58 or src ip 103.6.128.230", "stattype": 9}}}}

JIANGMEN_HK01 = {"name": "JIANGMEN_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.130.207", "stattype": 9}}}}

INFONETWORK_HK01 = {"name": "INFONETWORK_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.130.235", "stattype": 9}}}}

ONEDIRECTION_HK01 = {"name": "ONEDIRECTION_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src ip 103.6.128.50 or src ip 103.6.128.59 or src net 220.158.132.84/30", "stattype": 9}}}}

MSKIX_HK01 = {"name": "MSKIX_HK01", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 123 or out if 137 or out if 138) and src net 193.232.82.0/23 or src net 193.232.127.0/24 or src net 193.232.156.0/23", "stattype": 9}}}}

CHINA_UPLINK_INTERFACE = [Cataleya_SGP_GSW, Cataleya_SGP_EQ_HK101, ICM_HK101, FXDirect_HK101, Rational_HK101, SIMS_HK01, UMBRA_HK_101, Forextime_HK01, SwissQuote_HK01, FxPro_HK01, Zeal_HK01, SOF_677078_HK01, Exness_HK01, Overonix_HK01, Greenmile_HK01, Notesco_HK01, Cheersum_HK01, MakeCapital_HK01, Algolia_HK01, Muganbank_HK01, ForexClub_HK01, GameUAB_HK01, GrandCapital_HK01, Guruhosting_HK01, Netsentia_HK01, WeTrade_HK01, Gransy_HK01, JINOM_HK01, LINTAS_HK01, MicroFox_HK01, JIANGMEN_HK01, INFONETWORK_HK01, ONEDIRECTION_HK01, MSKIX_HK01, SOF_150462_HK01, SOF_183127_HK01, SOF_190800_HK01, SOF_353882_1_HK01, SOF_353882_2_HK01]

CHINA_RESOURCES = {"uplinks": CHINA_UPLINKS_EQ}

#########################CHINA MEGAI USAGE##############################

Cataleya_SGP_GSW_409 = {"name": "Cataleya_SGP_GSW_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 103.242.75.184/29 or src net 103.242.75.176/29 or src net 103.242.75.144/28 or src net 103.242.75.37/31", "stattype": 9}}}}

Cataleya_SGP_EQ_409 = {"name": "Cataleya_SGP_EQ_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.242.74.7 or src net 103.242.74.8/29 or src net 103.242.74.16/30 or src net 103.242.74.20/31 or src ip 103.242.74.22 or src net 103.242.74.88/29 or src net 103.242.74.96/30 or src net 103.242.74.176/29 or src net 103.242.74.224/28 or src net 103.242.74.248/29", "stattype": 9}}}}

##### UMBRA Technologies(HK) Limited #####

UMBRA_HK_409 = {"name": "UMBRA_HK", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.242.72.67 or src net 103.242.72.68/30 or src ip 103.242.72.72 or src net 103.6.130.238/31", "stattype": 9}}}}

SOF_150462_HK409 = {"name": "SOF_150462_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 103.6.130.238/31 or src net 103.6.130.240/30 or src net 103.6.130.244/31 or src ip 103.6.130.246", "stattype": 9}}}}

SOF_183127_HK409 = {"name": "SOF_183127_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.242.72.67 or src net 103.242.72.68/30 or src ip 103.242.72.72", "stattype": 9}}}}

SOF_190800_HK409 = {"name": "SOF_190800_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 103.242.72.139/31 or src net 103.242.72.140/30 or src net 103.242.72.144/29 or src net 103.242.72.152/31 or src ip 103.242.72.154", "stattype": 9}}}}

SOF_353882_1_HK409 = {"name": "SOF_353882-1_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.128.3 or src ip 103.6.128.15 or src ip 103.6.128.17 or src net 103.6.128.30/31 or src ip 103.6.128.32 or src net 103.6.128.102/31 or src net 103.6.128.104/30 or src net 103.6.128.108/31 or src ip 103.6.128.113 or src ip 103.6.128.114", "stattype": 9}}}}


SOF_353882_2_HK409 = {"name": "SOF_353882_2_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.128.3 or src ip 103.6.128.15 or src ip 103.6.128.17 or src net 103.6.128.30/31 or src ip 103.6.128.32 or src net 103.6.128.102/31 or src net 103.6.128.104/30 or src net 103.6.128.108/31 or src ip 103.6.128.113 or src ip 103.6.128.114", "stattype": 9}}}}

ICM_HK409 = {"name": "ICM_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.128.138 or src ip 103.145.2.77 or src ip 103.145.2.79 or src ip 103.6.128.228 or src ip 103.242.75.47 or src ip 103.145.3.5 or src ip 91.194.117.74", "stattype": 9}}}}

FXDirect_HK409 = {"name": "FXDirect_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.130.85 or src net 103.6.130.86/31 or src net 103.6.130.88/31 or src ip 103.6.130.90 or src net 103.6.130.134/31 or src net 103.6.130.136/31  or src ip 103.6.130.138", "stattype": 9}}}}

Rational_HK409 = {"name": "Rational_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.130.145 or src ip 103.6.130.146 or src ip 103.6.130.148", "stattype": 9}}}}

Forextime_HK409 = {"name": "Forextime_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 103.6.130.1/30 or src ip 103.6.130.4 or src ip 103.242.72.3 or src ip 103.242.72.4 or src ip 103.242.72.8 or src ip 103.242.72.10 or src ip 103.242.72.64 or src net 103.242.72.80/30 or src ip 103.242.72.87 or src ip 103.242.72.104 or src ip 103.242.72.155 or src net 103.242.72.164/30 or src net 103.242.72.168/31 or src net 103.242.72.184/30 or src ip 103.242.72.205 or src net 103.242.72.206/31 or src net 103.242.72.208/31 or src ip 103.242.72.211 or src net 103.242.72.212/30 or src ip 103.242.72.234 or src ip 103.6.128.63 or src ip 103.6.128.64 or src net 103.6.128.122/31 or src net 103.6.128.124/30 or src net 103.6.128.128/30 or src net 103.6.128.132/31 or src ip 103.6.128.134 or src net 103.6.128.152/30 or src net 103.6.128.156/31 or src ip 103.6.128.158 or src net 103.6.128.162/31 or src net 103.6.128.164/31 or src ip 103.6.128.180 or src net 103.6.128.196/31 or src ip 103.6.128.198 or src net 103.6.128.200/31 or src ip 103.6.128.203 or src ip 103.6.128.223 or src ip 103.6.128.225 or src ip 103.242.72.216 or src net 103.242.72.244/31 or src ip 103.242.72.246 or src ip 103.242.72.160", "stattype": 9}}}}

SwissQuote_HK409 = {"name": "SwissQuote_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 103.6.130.210/31 or src net 103.6.130.212/30 or src net 103.6.130.216/29 or src net 103.6.130.224/31", "stattype": 9}}}}

FxPro_HK409 = {"name": "FxPro_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 103.6.131.10/31 or src ip 103.6.131.12 or src net 103.6.130.140/31 or src ip 103.6.130.142 or src ip 103.6.130.147 or src ip 103.6.130.153 or src net 103.6.130.154/31 or src net 103.6.130.156/31 or src ip 103.6.128.79 or src ip 103.6.128.80 or src ip 103.6.128.90", "stattype": 9}}}}

###ZEAL CUSTOMER###

Zeal_HK409 = {"name": "Zeal_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.242.72.103 or src ip 103.242.75.122 or src ip 103.242.75.49 or src ip 103.217.163.129 or src ip 103.217.163.130 or src ip 176.56.180.147 or src ip 176.56.180.203 or src ip 103.6.130.91 or src ip 103.6.130.130 or src ip 103.6.130.131 or src ip 103.6.130.149 or src ip 103.6.130.227 or src ip 103.6.130.228 or src ip 103.6.130.229 or src ip 103.6.130.233 or src ip 103.6.130.248 or src ip 103.6.130.249 or src ip 176.56.160.177 or src ip 176.56.160.233 or src ip 176.56.160.236 or src ip 176.56.160.243 or src ip 103.6.129.37 or src ip 103.6.129.38 or src ip 103.145.2.39 or src net 103.145.2.40/29 or src net 103.145.2.48/29 or src ip 103.145.2.52 or src ip 103.145.2.53 or src ip 103.6.128.18 or src net 103.6.128.52/30 or src ip 103.6.128.77 or src ip 103.6.128.78 or src ip 103.6.128.97 or src ip 103.6.128.99 or src ip 103.6.128.151 or src ip 103.6.128.249", "stattype": 9}}}}

SOF_677078_HK409 = {"name": "SOF_677078_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.128.151 or src ip 103.6.128.18 or src ip 103.6.128.249 or src ip 103.6.128.77 or src ip 103.6.128.78", "stattype": 9}}}}

Exness_HK409 = {"name": "Exness_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.242.72.100 or src ip 103.242.72.11 or src net 103.242.72.12/30 or src net 103.242.72.16/29 or src net 103.242.72.24/30 or src ip 103.242.72.28 or src ip 103.242.72.29 or src ip 103.242.72.30 or src net 103.242.72.52/30 or src ip 103.242.72.56 or src ip 103.242.72.63 or src ip 103.6.128.110 or src ip 103.6.128.111 or src ip 103.6.128.112 or src ip 103.6.128.117 or src ip 103.6.128.118 or src ip 103.6.128.119 or src ip 103.6.128.120 or src ip 103.6.128.12 or src ip 103.6.128.229 or src ip 103.6.128.68 or src ip 103.6.128.76 or src ip 103.6.128.82 or src ip 103.6.128.83 or src net 103.6.128.84/30 or src ip 103.6.128.88 or src ip 103.6.128.91 or src net 103.6.128.92/30 or src ip 103.6.128.33 or src ip 103.6.128.34 or src ip 103.6.128.35 or src ip 103.6.128.36 or src ip 103.6.128.37 or src net 103.6.128.40/30 or src ip 103.6.128.49 or src ip 103.145.2.39 or src net 103.145.2.40/29 or src net 103.145.2.48/30 or src ip 103.145.2.52 or src ip 103.145.2.53 or src net 103.242.75.12/30 or src net 103.242.75.16/29 or src ip 103.242.75.24 or src ip 103.242.75.26 or src ip 103.242.75.27 or src net 103.242.75.28/30 or src ip 103.242.75.32 or src ip 103.242.75.33 or src ip 103.242.75.34 or src ip 103.242.75.42 or src ip 103.242.75.43 or src ip 103.242.75.49", "stattype": 9}}}}

Overonix_HK409 = {"name": "Overonix_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.242.74.27 or src ip 103.242.74.57 or src ip 103.6.128.190 or src net 103.6.128.192/31 or src ip 103.6.128.47 or src ip 103.23.168.23 or src ip 103.23.168.24", "stattype": 9}}}}

Greenmile_HK409 = {"name": "Greenmile_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.242.72.75 or src ip 103.6.130.129 or src ip 103.6.130.64 or src ip 103.6.130.150 or src ip 220.158.132.213 or src ip 103.6.130.139 or src ip 103.242.75.61", "stattype": 9}}}}

Notesco_HK409 = {"name": "Notesco_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.242.72.216 or src ip 103.6.128.63 or src ip 103.6.128.64 or src ip 103.6.128.71 or src net 103.6.128.72/30 or src net 103.6.128.162/31 or src net 103.6.128.164/31 or src ip 103.6.128.180 or src net 103.6.128.196/31 or src ip 103.6.128.198 or src net 103.6.128.200/31 or src ip 103.6.128.203 or src ip 103.6.128.223 or src ip 103.6.128.225 or src ip 103.6.128.227 or src ip 103.6.130.69 or src ip 103.6.130.70 or src ip 103.6.130.82 or src ip 103.6.130.95 or src ip 103.6.130.96 or src ip 103.6.130.99 or src net 103.6.130.100/31 or src ip 103.6.130.105 or src net 103.6.130.106/31 or src net 103.6.130.108/30 or src ip 103.6.130.112 or src ip 103.6.130.121 or src net 103.6.130.122/31 or src net 103.6.130.124/30 or src ip 103.6.130.128 or src ip 103.6.130.144 or src ip 103.6.130.172 or src ip 103.6.130.182 or src ip 103.6.130.184 or src ip 103.6.130.198 or src ip 103.6.130.199 or src ip 103.6.130.200 or src ip 103.6.130.204 or src ip 103.6.130.205 or src ip 103.6.130.206 or src ip 103.6.130.208 or src ip 103.23.170.3 or src net 103.23.170.4/30 or src net 103.23.170.8/30 or src net 103.23.170.12/31 or src ip 103.23.170.14", "stattype": 9}}}}

Cheersum_HK409 = {"name": "Cheersum_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 103.6.130.74/31 or src ip 103.6.130.76", "stattype": 9}}}}

MakeCapital_HK409 = {"name": "MakeCapital_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.242.72.74", "stattype": 9}}}}

Algolia_HK409 = {"name": "Algolia_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.130.168", "stattype": 9}}}}

Muganbank_HK409 = {"name": "Muganbank_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.242.72.204", "stattype": 9}}}}

ForexClub_HK409 = {"name": "ForexClub_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.128.10 or src ip 103.6.128.20 or src ip 103.6.128.65 or src ip 103.6.128.66 or src ip 103.6.128.89 or src ip 103.6.128.115 or src ip 103.6.128.116 or src net 103.6.128.170/31 or src net 103.6.128.172/30 or src net 103.6.128.176/30 or src net 103.6.128.210/31 or src net 103.6.128.212/31 or src ip 103.6.128.241 or src net 103.6.128.242/31 or src net 103.6.128.244/31 or src ip 103.6.128.246", "stattype": 9}}}}

GameUAB_HK409 = {"name": "GameUAB_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.130.65 or src ip 103.6.128.39", "stattype": 9}}}}

GrandCapital_HK409 = {"name": "GrandCapital_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.130.93 or src ip 103.6.130.94 or src ip 103.6.130.226", "stattype": 9}}}}

Guruhosting_HK409 = {"name": "Guruhosting_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.242.72.79 or src ip 103.242.72.102 or src ip 103.242.72.162 or src ip 103.242.72.163 or src ip 103.242.72.217 or src ip 103.242.72.222 or src ip 103.242.72.223 or src ip 103.242.72.235 or src net 103.242.72.236/30 or src ip 103.242.72.240 or src ip 103.242.72.241 or src ip 103.242.72.242", "stattype": 9}}}}

Netsentia_HK409 = {"name": "Netsentia_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 220.158.132.0/29", "stattype": 9}}}}

WeTrade_HK409 = {"name": "WeTrade_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.130.79 or src ip 103.6.130.92 or src ip 103.217.160.67 or src ip 103.6.128.45", "stattype": 9}}}}

Gransy_HK409 = {"name": "Gransy_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.128.121 or src ip 103.145.3.2 or src ip 103.242.75.41 or src ip 103.217.160.63 or src ip 103.145.2.95 or src net 185.28.194.0/24 or src net 185.38.108.0/24", "stattype": 9}}}}

SIMS_HK409 = {"name": "SIMS_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 27.123.0.0/21 or src net 27.124.81.0/24 or src net 27.124.82.0/24 or src net 27.124.83.0/24 or src net 27.124.85.0/24 or src net 27.124.90.0/24 or src net 27.124.92.0/24 or src net 42.62.176.0/22 or src net 43.229.254.0/23 or src net 43.254.124.0/22 or src net 45.251.72.0/22 or src net 49.128.184.0/24 or src net 49.128.186.0/24 or src net 103.3.58.0/23 or src net 103.9.124.0/22 or src net 103.11.106.0/23 or src net 103.18.28.0/22 or src net 103.24.72.0/22 or src net 103.25.110.0/24 or src net 103.28.224.0/22 or src net 103.29.184.0/24 or src net 103.29.184.0/23 or src net 103.29.185.0/24 or src net 103.30.244.0/22 or src net 103.31.204.0/23 or src net 103.31.206.0/24 or src net 103.37.168.0/22 or src net 103.39.52.0/24 or src net 103.40.120.0/23 or src net 103.40.122.0/24 or src net 103.44.100.0/24 or src net 103.49.28.0/23 or src net 103.49.228.0/22 or src net 103.51.44.0/22 or src net 103.65.236.0/23 or src net 103.71.190.0/23 or src net 103.71.255.0/24 or src net 103.76.148.0/22 or src net 103.77.76.0/22 or src net 103.77.106.0/23 or src net 103.80.80.0/22 or src net 103.80.236.0/22 or src net 103.83.176.0/23 or src net 103.84.208.0/22 or src net 103.94.132.0/23 or src net 103.98.121.0/24 or src net 103.100.180.0/22 or src net 103.103.175.0/24 or src net 103.103.192.0/23 or src net 103.105.98.0/23 or src net 103.105.217.0/24 or src net 103.107.71.0/24 or src net 103.107.84.0/23 or src net 103.108.187.0/24 or src net 103.111.217.0/24 or src net 103.111.220.0/22 or src net 103.112.244.0/23 or src net 103.119.228.0/23 or src net 103.120.64.0/23 or src net 103.121.238.0/23 or src net 103.124.244.0/23 or src net 103.125.13.0/24 or src net 103.125.16.0/22 or src net 103.129.205.0/24 or src net 103.131.104.0/23 or src net 103.132.19.0/24 or src net 103.133.20.0/23 or src net 103.134.18.0/23 or src net 103.135.227.0/24 or src net 103.136.182.0/24 or src net 103.137.37.0/24 or src net 103.138.68.0/23 or src net 103.139.120.0/24 or src net 103.141.20.0/23 or src net 103.141.40.0/23 or src net 103.142.224.0/24 or src net 103.143.4.0/23 or src net 103.143.194.0/24 or src net 103.145.68.0/23 or src net 103.146.30.0/24 or src net 103.147.6.0/24 or src net 103.147.53.0/24 or src net 103.147.72.0/23 or src net 103.147.82.0/23 or src net 103.147.84.0/23 or src net 103.147.246.0/23 or src net 103.148.18.0/23 or src net 103.148.24.0/24 or src net 103.148.28.0/23 or src net 103.149.238.0/23 or src net 103.151.22.0/23 or src net 103.151.34.0/23 or src net 103.152.63.0/24 or src net 103.152.118.0/23 or src net 103.152.238.0/23 or src net 103.153.134.0/23 or src net 103.153.136.0/23 or src net 103.153.148.0/23 or src net 103.153.229.0/24 or src net 103.153.248.0/23 or src net 103.155.106.0/23 or src net 103.155.156.0/24 or src net 103.155.167.0/24 or src net 103.155.191.0/24 or src net 103.155.196.0/23 or src net 103.156.128.0/24 or src net 103.156.132.0/23 or src net 103.156.232.0/23 or src net 103.156.233.0/24 or src net 103.157.78.0/23 or src net 103.157.102.0/24 or src net 103.158.130.0/24 or src net 103.158.252.0/23 or src net 103.159.222.0/23 or src net 103.160.18.0/23 or src net 103.160.62.0/23 or src net 103.160.178.0/23 or src net 103.160.201.0/24 or src net 103.160.202.0/23 or src net 103.160.205.0/24 or src net 103.161.62.0/23 or src net 103.161.130.0/23 or src net 103.162.54.0/24 or src net 103.162.63.0/24 or src net 103.162.106.0/24 or src net 103.162.144.0/23 or src net 103.163.13.0/24 or src net 103.163.228.0/23 or src net 103.164.186.0/23 or src net 103.164.235.0/24 or src net 103.167.11.0/24 or src net 103.167.170.0/23 or src net 103.168.28.0/24 or src net 103.168.146.0/23 or src net 103.168.150.0/23 or src net 103.168.186.0/23 or src net 103.169.132.0/22 or src net 103.169.138.0/23 or src net 103.169.220.0/23 or src net 103.172.96.0/24 or src net 103.172.118.0/23 or src net 103.173.74.0/23 or src net 103.175.48.0/24 or src net 103.175.238.0/23 or src net 103.176.26.0/23 or src net 103.176.177.0/24 or src net 103.176.180.0/23 or src net 103.178.41.0/24 or src net 103.198.93.0/24 or src net 103.203.162.0/24 or src net 103.210.35.0/24 or src net 103.210.116.0/22 or src net 103.214.184.0/22 or src net 103.219.72.0/22 or src net 103.233.102.0/23 or src net 103.241.179.0/24 or src net 103.244.204.0/22 or src net 103.254.104.0/22 or src net 103.255.15.0/24 or src net 111.92.162.0/23 or src net 111.92.166.0/24 or src net 111.92.169.0/24 or src net 111.92.170.0/24 or src net 114.199.80.0/20 or src net 116.206.4.0/22 or src net 117.103.64.0/23 or src net 117.103.66.0/24 or src net 118.91.137.0/24 or src net 119.47.88.0/23 or src net 120.89.88.0/23 or src net 150.107.248.0/22 or src net 202.43.64.0/24 or src net 202.43.114.0/23 or src net 202.47.64.0/20 or src net 202.51.19.0/24 or src net 202.51.30.0/24 or src net 202.52.140.0/23 or src net 202.57.16.0/23 or src net 202.57.16.0/21 or src net 202.57.16.0/20 or src net 202.57.18.0/23 or src net 202.57.20.0/23 or src net 202.57.22.0/23 or src net 202.57.24.0/23 or src net 202.57.26.0/23 or src net 202.57.28.0/23 or src net 202.57.30.0/23 or src net 202.58.216.0/23 or src net 202.58.220.0/22 or src net 202.83.120.0/23 or src net 202.83.123.0/24 or src net 202.162.39.0/24 or src net 202.162.40.0/23 or src net 202.169.224.0/20 or src net 203.29.26.0/23 or src net 203.148.84.0/23 or src net 203.190.112.0/21 or src net 206.84.96.0/22 or src net 206.84.96.0/19 or src net 206.84.101.0/24 or src net 206.84.102.0/23 or src net 206.84.105.0/24 or src net 206.84.106.0/24 or src net 210.247.244.0/24", "stattype": 9}}}}

JINOM_HK409 = {"name": "JINOM_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 103.122.64.0/24 or src net 103.122.66.0/24 or src net 103.122.67.0/24", "stattype": 9}}}}

LINTAS_HK409 = {"name": "LINTAS_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 27.54.116.0/22 or src net 27.121.86.0/24 or src net 43.230.28.0/22 or src net 43.230.155.0/24 or src net 43.241.148.0/22 or src net 43.247.20.0/23 or src net 43.247.20.0/22 or src net 43.247.22.0/23 or src net 43.252.104.0/24 or src net 43.252.106.0/23 or src net 43.252.236.0/22 or src net 43.254.124.0/22 or src net 49.0.0.0/22 or src net 103.4.174.0/23 or src net 103.4.243.0/24 or src net 103.11.21.0/24 or src net 103.11.222.0/24 or src net 103.18.76.0/22 or src net 103.20.188.0/22 or src net 103.20.196.0/23 or src net 103.22.240.0/22 or src net 103.23.234.0/23 or src net 103.25.208.0/22 or src net 103.28.112.0/22 or src net 103.28.224.0/23 or src net 103.28.224.0/22 or src net 103.28.226.0/23 or src net 103.30.180.0/22 or src net 103.31.232.0/22 or src net 103.60.180.0/22 or src net 103.66.69.0/23 or src net 103.76.200.0/22 or src net 103.78.106.0/24 or src net 103.79.91.0/24 or src net 103.80.88.0/23 or src net 103.81.246.0/24 or src net 103.81.248.0/23 or src net 103.97.4.0/22 or src net 103.100.27.0/24 or src net 103.100.96.0/24 or src net 103.100.246.0/24 or src net 103.105.190.0/24 or src net 103.105.216.0/24 or src net 103.107.144.0/22 or src net 103.108.128.0/22 or src net 103.115.36.0/22 or src net 103.124.8.0/24 or src net 103.126.28.0/24 or src net 103.126.30.0/24 or src net 103.132.236.0/24 or src net 103.138.76.0/24 or src net 103.139.76.0/23 or src net 103.140.130.0/23 or src net 103.141.156.0/23 or src net 103.144.126.0/24 or src net 103.144.146.0/24 or src net 103.145.14.0/23 or src net 103.148.24.0/23 or src net 103.148.79.0/24 or src net 103.213.128.0/22 or src net 103.225.172.0/24 or src net 103.225.175.0/24 or src net 103.245.136.0/23 or src net 110.5.96.0/23 or src net 110.5.96.0/22 or src net 110.5.96.0/21 or src net 110.5.96.0/20 or src net 110.5.98.0/23 or src net 110.5.100.0/22 or src net 110.5.104.0/21 or src net 110.50.83.0/24 or src net 110.50.84.0/22 or src net 112.78.40.0/21 or src net 114.141.48.0/21 or src net 117.121.205.0/23 or src net 119.18.152.0/21 or src net 123.253.232.0/22 or src net 124.40.248.0/21 or src net 124.158.176.0/20 or src net 150.107.140.0/22 or src net 180.211.88.0/21 or src net 182.54.140.0/23 or src net 202.46.80.0/22 or src net 202.46.144.0/22 or src net 202.46.152.0/21 or src net 202.51.198.0/24 or src net 202.51.214.0/24 or src net 202.56.164.0/22 or src net 202.62.12.0/22 or src net 202.73.24.0/24 or src net 202.73.26.0/23 or src net 202.75.96.0/24 or src net 202.75.99.0/24 or src net 202.75.101.0/24 or src net 202.75.104.0/22 or src net 202.75.109.0/24 or src net 202.75.111.0/24 or src net 202.80.208.0/21 or src net 202.80.216.0/22 or src net 202.91.24.0/21 or src net 202.93.128.0/20 or src net 202.145.8.0/21 or src net 202.147.192.0/20 or src net 202.149.128.0/21 or src net 202.149.148.0/22 or src net 202.150.160.0/20 or src net 203.57.24.0/23 or src net 203.84.152.0/21 or src net 203.161.16.0/24 or src net 203.161.18.0/23 or src net 203.161.20.0/23 or src net 203.174.8.0/21", "stattype": 9}}}}

MicroFox_HK409 = {"name": "MicroFox_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 103.6.128.56/31 or src ip 103.6.128.58 or src ip 103.6.128.230", "stattype": 9}}}}

JIANGMEN_HK409 = {"name": "JIANGMEN_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.130.207", "stattype": 9}}}}

INFONETWORK_HK409 = {"name": "INFONETWORK_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.130.235", "stattype": 9}}}}

UMBRA_HK409_TEST = {"name": "UMBRA_409TEST", "interface": "166", "resources": {"uplinks": {"query":{"filter": "out if 62 and src ip 103.242.72.67 or src net 103.242.72.68/30 or src ip 103.242.72.72 or src net 103.6.130.238/31", "stattype": 9}}}}

ONEDIRECTION_HK409 = {"name": "ONEDIRECTION_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src ip 103.6.128.50 or src ip 103.6.128.59 or src net 220.158.132.84/30", "stattype": 9}}}}

MSKIX_HK409 = {"name": "MSKIX_HK409", "interface": "166", "resources": {"uplinks": {"query":{"filter": "(out if 63 or out if 62 or out if 59 or out if 406) and src net 193.232.82.0/23 or src net 193.232.127.0/24 or src net 193.232.156.0/23", "stattype": 9}}}}

CHINA_UPLINK_MEGAI_INTERFACE = [Cataleya_SGP_GSW_409, Cataleya_SGP_EQ_409, UMBRA_HK_409, ICM_HK409, FXDirect_HK409, Rational_HK409, Forextime_HK409, SwissQuote_HK409, FxPro_HK409, Zeal_HK409, SOF_677078_HK409, Exness_HK409, Overonix_HK409, Greenmile_HK409, Notesco_HK409, Cheersum_HK409, MakeCapital_HK409, Algolia_HK409, Muganbank_HK409, ForexClub_HK409, GameUAB_HK409, GrandCapital_HK409, Guruhosting_HK409, Netsentia_HK409, WeTrade_HK409, Gransy_HK409, SIMS_HK409, JINOM_HK409, LINTAS_HK409, MicroFox_HK409, UMBRA_HK409_TEST, JIANGMEN_HK409, INFONETWORK_HK409, ONEDIRECTION_HK409, MSKIX_HK409, SOF_150462_HK409, SOF_183127_HK409, SOF_190800_HK409, SOF_353882_1_HK409, SOF_353882_2_HK409]

CHINA_MEGAI_RESOURCES = {"uplinks": CHINA_UPLINKS_MEGAI}
#####################KOREA############################

CDSONLINE = {"name": "CDS", "interface": "53", "resources": {"as_down_src": {"query":{"filter": "in if 53 and src as 63199", "stattype": 11}}}}
CDSONLINE_CHINA = {"name": "CDS_CHINA", "interface": "53", "resources": {"as_down_src": {"query":{"filter": "in if 53 and src as 63199", "stattype": 12}}}}
PCCW_KR_OUT = {"name": "PCCW_KR_OUT", "interface": "117", "resources": {"as_down_src": {"query":{"filter": "out if 117", "stattype": 11}}}}
KINXLOCAL = {"name": "KINXLOCAL_OUT", "interface": "36", "resources": {"as_down_src": {"query":{"filter": "out if 36", "stattype": 11}}}}

KOREA_DOWN_INTERFACES = [CDSONLINE, CDSONLINE_CHINA, PCCW_KR_OUT, KINXLOCAL]

KOREA_DOWN_RESOURCES = {"as_down_src": AS_LIST}

#####################VIETNAM############################

CMCTELCOM = {"name": "CMC", "interface": "151", "resources": {"as_down_src": {"query":{"filter": "out if 151", "stattype": 11}}}}

HCM_DOWN_INTERFACES = [CMCTELCOM]

HCM_DOWN_RESOURCES = {"as_down_src": AS_LIST}

#####################HONG KONG MEGA-I############################
CU10099 = {"name": "CU10099", "interface": "406", "resources": {"as_down_src": {"query":{"filter": "out if 406", "stattype": 11}}}}
CDSMegaICT1 = {"name": "PCCWMegaICT1", "interface": "62", "resources": {"as_down_src": {"query":{"filter": "out if 62", "stattype": 11}}}}
CDSMegaICT2 = {"name": "PCCWMegaICT2", "interface": "59", "resources": {"as_down_src": {"query":{"filter": "out if 59", "stattype": 11}}}}
PCCW_MegaI = {"name": "PCCW_MegaI", "interface": "66", "resources": {"as_down_src": {"query":{"filter": "in if 66", "stattype": 11}}}}
CDSMegaICU = {"name": "PCCWMegaICU", "interface": "63", "resources": {"as_down_src": {"query":{"filter": "out if 63", "stattype": 11}}}}

CataleyaGSCU10099 = {"name": "CataleyaGSCU1009", "interface": "406", "resources": {"as_down_src": {"query":{"filter": "out if 406 and src net 103.242.75.184/29 or src net 103.242.75.176/29 or src net 103.242.75.144/28 or src net 103.242.75.37/31", "stattype": 12}}}}

CataleyaGSPCCW1 = {"name": "CataleyaGSPCCW1", "interface": "62", "resources": {"as_down_src": {"query":{"filter": "out if 62 and src net 103.242.75.184/29 or src net 103.242.75.176/29 or src net 103.242.75.144/28 or src net 103.242.75.37/31", "stattype": 12}}}}

CataleyaGSPCCW2 = {"name": "CataleyaGSPCCW2", "interface": "59", "resources": {"as_down_src": {"query":{"filter": "out if 59 and src net 103.242.75.184/29 or src net 103.242.75.176/29 or src net 103.242.75.144/28 or src net 103.242.75.37/31", "stattype": 12}}}}

CataleyaGSPCCW3 = {"name": "CataleyaGSPCCWTS", "interface": "66", "resources": {"as_down_src": {"query":{"filter": "out if 66 and src net 103.242.75.184/29 or src net 103.242.75.176/29 or src net 103.242.75.144/28 or src net 103.242.75.37/31", "stattype": 12}}}}

CataleyaGSPCCW4 = {"name": "CataleyaGWPCCW4", "interface": "63", "resources": {"as_down_src": {"query":{"filter": "out if 63 and src net 103.242.75.184/29 or src net 103.242.75.176/29 or src net 103.242.75.144/28 or src net 103.242.75.37/31", "stattype": 12}}}}

HK409_UP_INTERFACES = [CU10099, CDSMegaICT1, CDSMegaICT2, PCCW_MegaI, CDSMegaICU, CataleyaGSCU10099, CataleyaGSPCCW1, CataleyaGSPCCW2, CataleyaGSPCCW3, CataleyaGSPCCW4]
HK409_UP_RESOURCES = {"as_down_src": AS_LIST}

#####################SINGAPORE############################
PCCW_DOWN_EQ = {"name": "PCCW_SGP_EQ", "interface": "171", "resources": {"as_down_src": {"query":{"filter": "in if 171", "stattype": 11}}}}
PCCW_DOWN_GSW = {"name": "PCCW_SGP_GSW", "interface": "320", "resources": {"as_down_src": {"query":{"filter": "in if 320", "stattype": 11}}}}
PCCW_UP_EQ = {"name": "PCCW_UP_EQ", "interface": "171", "resources": {"as_down_src": {"query":{"filter": "out if 171", "stattype": 11}}}}
JBIX_UP_EQ = {"name": "JBIX_UP_EQ", "interface": "556", "resources": {"as_down_src": {"query":{"filter": "in if 556", "stattype": 11}}}}
CataleyaEQ = {"name": "CataleyaEQVl740", "interface": "340", "resources": {"as_down_src": {"query":{"filter": "in if 340", "stattype": 12}}}}

SGP_UP_INTERFACES = [PCCW_DOWN_EQ, PCCW_DOWN_GSW, PCCW_UP_EQ, JBIX_UP_EQ, CataleyaEQ]
SGP_UP_RESOURCES = {"as_down_src": AS_LIST}

#####################TOKYO############################
PCCW_TY2 = {"name": "PCCW_TY2_IN", "interface": "93", "resources": {"as_down_src": {"query":{"filter": "in if 93", "stattype": 11}}}}

JPN_INTERFACES = [PCCW_TY2]
JPN_RESOURCES = {"as_down_src": AS_LIST}

#####################TAIWAN############################
PCCW_TW = {"name": "PCCW_TW_IN", "interface": "46", "resources": {"as_down_src": {"query":{"filter": "in if 46", "stattype": 11}}}}

TW_INTERFACES = [PCCW_TW]
TW_RESOURCES = {"as_down_src": AS_LIST}

#####################SINGAPORE GLOBAL SWITCH IB25############################
#CataleyaG0009AB = {"name": "CataleyaGWVl750", "interface": "83", "resources": {"as_down_src": {"query":{"filter": "in if 83 and src net 103.242.75.184/29 or src net 103.242.75.176/29 or src net 103.242.75.144/28 or src net 103.242.75.37/31", "stattype": 12}}}}

#SGPGW_DOWN_INTERFACES = [CataleyaG0009AB]

#SGPGW_DOWN_RESOURCES = {"as_down_src": AS_LIST}

#############################################################################

COUNTRIES = [
             #{"name": "EE HK DOWN", "router": "r1-102-eq-hk", "customers": PERU_DOWN_INTERFACES, "resources": PERU_DOWN_RESOURCES},
              {"name": "Hong Kong Equinix1", "router": "r0-101-eq-hk", "customers": PERU_DOWN_INTERFACES, "resources": PERU_DOWN_RESOURCES},
              {"name": "HKEQ China Usage", "router": "r0-101-eq-hk", "customers": CHINA_UPLINK_INTERFACE, "resources": CHINA_RESOURCES},
              {"name": "Korea", "router": "r0-a30-kx-sel", "customers": KOREA_DOWN_INTERFACES, "resources": KOREA_DOWN_RESOURCES},
             {"name": "HCM_CMC", "router": "r0-f8-cmc-hcm", "customers": HCM_DOWN_INTERFACES, "resources": HCM_DOWN_RESOURCES},
             {"name": "HK409_CHINA", "router": "r0-409-mi-hk", "customers": HK409_UP_INTERFACES, "resources": HK409_UP_RESOURCES},
              {"name": "HKMEGAI China Usage", "router": "r0-409-mi-hk", "customers": CHINA_UPLINK_MEGAI_INTERFACE, "resources": CHINA_MEGAI_RESOURCES},
              {"name": "SGP_PCCW", "router": "r0-616-eq-sg", "customers": SGP_UP_INTERFACES, "resources": SGP_UP_RESOURCES},
              {"name": "JPN_PCCW", "router": "r0-204-ty2", "customers": JPN_INTERFACES, "resources": JPN_RESOURCES},
              {"name": "TW_PCCW", "router": "r0-4l09-easpn-tp-tw", "customers": TW_INTERFACES, "resources": TW_RESOURCES},
              {"name": "SGP_GSW_PCCW", "router": "r0-ib26-gs-sg", "customers": SGP_UP_INTERFACES, "resources": SGP_UP_RESOURCES}
             ]


for country in COUNTRIES:
    for customer in country["customers"]:
       #del customer["resources"]["as"]
        for resource, resource_data in customer["resources"].items():
            if resource == "as":
                resource_data["query"]["topN"] = 2





