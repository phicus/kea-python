from typing import Any, Callable, List, Dict, Optional, Tuple, Union, TYPE_CHECKING

Element: Dict[str, Any]

ALL_SOURCES: int
ALTERNATE_SOURCES: int
BOOTREPLY: int
BOOTREQUEST: int
DHCP4_CLIENT_PORT: int
DHCP4_SERVER_PORT: int
DHCPACK: int
DHCPBULKLEASEQUERY: int
DHCPDECLINE: int
DHCPDISCOVER: int
DHCPINFORM: int
DHCPLEASEACTIVE: int
DHCPLEASEQUERY: int
DHCPLEASEQUERYDONE: int
DHCPLEASEQUERYSTATUS: int
DHCPLEASEUNASSIGNED: int
DHCPLEASEUNKNOWN: int
DHCPNAK: int
DHCPOFFER: int
DHCPRELEASE: int
DHCPREQUEST: int
DHCPTLS: int
DHCP_NOTYPE: int
DHCP_OPTIONS_COOKIE: int
DHCP_TYPES_EOF: int
DHO_6RD: int
DHO_ALL_SUBNETS_LOCAL: int
DHO_ARP_CACHE_TIMEOUT: int
DHO_ASSOCIATED_IP: int
DHO_AUTHENTICATE: int
DHO_AUTO_CONFIG: int
DHO_BCMCS_DOMAIN_NAME_LIST: int
DHO_BCMCS_IPV4_ADDR: int
DHO_BOOT_FILE_NAME: int
DHO_BOOT_SIZE: int
DHO_BROADCAST_ADDRESS: int
DHO_CAPWAP_AC_V4: int
DHO_CLIENT_LAST_TRANSACTION_TIME: int
DHO_COOKIE_SERVERS: int
DHO_DEFAULT_IP_TTL: int
DHO_DEFAULT_TCP_TTL: int
DHO_DHCP_AGENT_OPTIONS: int
DHO_DHCP_CLIENT_IDENTIFIER: int
DHO_DHCP_LEASE_TIME: int
DHO_DHCP_MAX_MESSAGE_SIZE: int
DHO_DHCP_MESSAGE: int
DHO_DHCP_MESSAGE_TYPE: int
DHO_DHCP_OPTION_OVERLOAD: int
DHO_DHCP_PARAMETER_REQUEST_LIST: int
DHO_DHCP_REBINDING_TIME: int
DHO_DHCP_RENEWAL_TIME: int
DHO_DHCP_REQUESTED_ADDRESS: int
DHO_DHCP_SERVER_IDENTIFIER: int
DHO_DIRECTORY_AGENT: int
DHO_DOMAIN_NAME: int
DHO_DOMAIN_NAME_SERVERS: int
DHO_DOMAIN_SEARCH: int
DHO_END: int
DHO_EXTENSIONS_PATH: int
DHO_FINGER_SERVER: int
DHO_FONT_SERVERS: int
DHO_FQDN: int
DHO_GEOCONF_CIVIC: int
DHO_HOME_AGENT_ADDRS: int
DHO_HOST_NAME: int
DHO_IEEE802_3_ENCAPSULATION: int
DHO_IMPRESS_SERVERS: int
DHO_INTERFACE_MTU: int
DHO_IP_FORWARDING: int
DHO_IRC_SERVER: int
DHO_LOG_SERVERS: int
DHO_LPR_SERVERS: int
DHO_MASK_SUPPLIER: int
DHO_MAX_DGRAM_REASSEMBLY: int
DHO_MERIT_DUMP: int
DHO_NAME_SERVERS: int
DHO_NAME_SERVICE_SEARCH: int
DHO_NDI: int
DHO_NDS_CONTEXT: int
DHO_NDS_SERVERS: int
DHO_NDS_TREE_NAME: int
DHO_NETBIOS_DD_SERVER: int
DHO_NETBIOS_NAME_SERVERS: int
DHO_NETBIOS_NODE_TYPE: int
DHO_NETBIOS_SCOPE: int
DHO_NETINFO_ADDR: int
DHO_NETINFO_TAG: int
DHO_NISP_DOMAIN_NAME: int
DHO_NISP_SERVER_ADDR: int
DHO_NIS_DOMAIN: int
DHO_NIS_SERVERS: int
DHO_NNTP_SERVER: int
DHO_NON_LOCAL_SOURCE_ROUTING: int
DHO_NTP_SERVERS: int
DHO_NWIP_DOMAIN_NAME: int
DHO_NWIP_SUBOPTIONS: int
DHO_PAD: int
DHO_PANA_AGENT: int
DHO_PATH_MTU_AGING_TIMEOUT: int
DHO_PATH_MTU_PLATEAU_TABLE: int
DHO_PCODE: int
DHO_PERFORM_MASK_DISCOVERY: int
DHO_POLICY_FILTER: int
DHO_POP3_SERVER: int
DHO_RDNSS_SELECT: int
DHO_RESOURCE_LOCATION_SERVERS: int
DHO_ROOT_PATH: int
DHO_ROUTERS: int
DHO_ROUTER_DISCOVERY: int
DHO_ROUTER_SOLICITATION_ADDRESS: int
DHO_SERVICE_SCOPE: int
DHO_SIP_UA_CONF_SERVICE_DOMAINS: int
DHO_SMTP_SERVER: int
DHO_STATIC_ROUTES: int
DHO_STDASERVER: int
DHO_STREETTALK_SERVER: int
DHO_SUBNET_MASK: int
DHO_SUBNET_SELECTION: int
DHO_SWAP_SERVER: int
DHO_SYSTEM: int
DHO_TCODE: int
DHO_TCP_KEEPALIVE_GARBAGE: int
DHO_TCP_KEEPALIVE_INTERVAL: int
DHO_TFTP_SERVER_NAME: int
DHO_TIME_OFFSET: int
DHO_TIME_SERVERS: int
DHO_TRAILER_ENCAPSULATION: int
DHO_USER_AUTH: int
DHO_USER_CLASS: int
DHO_UUID_GUID: int
DHO_V4_ACCESS_DOMAIN: int
DHO_V4_CAPTIVE_PORTAL: int
DHO_V4_LOST: int
DHO_V4_PORTPARAMS: int
DHO_VENDOR_CLASS_IDENTIFIER: int
DHO_VENDOR_ENCAPSULATED_OPTIONS: int
DHO_VIVCO_SUBOPTIONS: int
DHO_VIVSO_SUBOPTIONS: int
DHO_WWW_SERVER: int
DHO_X_DISPLAY_MANAGER: int
IDENT_CIRCUIT_ID: int
IDENT_CLIENT_ID: int
IDENT_DUID: int
IDENT_FLEX: int
IDENT_HWADDR: int
NEXT_STEP_CONTINUE: int
NEXT_STEP_DROP: int
NEXT_STEP_PARK: int
NEXT_STEP_SKIP: int
PRIMARY_SOURCE: int
RAI_OPTION_ACCESS_NETWORK_NAME: int
RAI_OPTION_ACCESS_POINT_BSSID: int
RAI_OPTION_ACCESS_POINT_NAME: int
RAI_OPTION_ACCESS_TECHNO_TYPE: int
RAI_OPTION_AGENT_CIRCUIT_ID: int
RAI_OPTION_AUTH: int
RAI_OPTION_DOCSIS_DEVICE_CLASS: int
RAI_OPTION_LINK_SELECTION: int
RAI_OPTION_OPERATOR_ID: int
RAI_OPTION_OPERATOR_REALM: int
RAI_OPTION_RADIUS: int
RAI_OPTION_RELAY_FLAGS: int
RAI_OPTION_RELAY_ID: int
RAI_OPTION_RELAY_PORT: int
RAI_OPTION_REMOTE_ID: int
RAI_OPTION_SERVER_ID_OVERRIDE: int
RAI_OPTION_SUBSCRIBER_ID: int
RAI_OPTION_VIRTUAL_SUBNET_SELECT: int
RAI_OPTION_VIRTUAL_SUBNET_SELECT_CTRL: int
RAI_OPTION_VSI: int
STATE_DECLINED: int
STATE_DEFAULT: int
STATE_EXPIRED_RECLAIMED: int
UNSPECIFIED_SOURCE: int
__version__: str
logger: None

class CalloutHandle:
    def getArgument(self, name: str) -> Union[Lease4, Pkt4, Element]: ...
    def setArgument(self, name: str, value: Union[Lease4, Pkt4, Element]) -> None: ...
    def setContext(self, name: str, value: Any) -> None: ...
    def getContext(self, name: str) -> Any: ...
    def deleteContext(self, name: str) -> None: ...
    def getStatus(self) -> int: ...
    def setStatus(self, status: int) -> None: ...
    def __init__(self, manager: "CalloutManager") -> None: ...

class CalloutManager:
    @property
    def use_count(self) -> int: ...
    def __init__(self) -> None: ...

class CfgMgr:
    def getCurrentCfg(self) -> SrvConfig:
        """Returns current configuration."""
    def getStagingCfg(self) -> SrvConfig:
        """Returns staging configuration."""

class CfgSubnets4:
    def getAll(self) -> Optional[List[Subnet4]]: ...
    def getSubnet(self, subnet_id: int) -> Optional[Subnet4]: ...
    def selectSubnet(self, addr: str) -> Optional[Subnet4]: ...
    def toElement(self) -> Optional[Element]: ...
    @property
    def use_count(self) -> int: ...

class Host:
    def __init__(self, identifier: str, identifier_type: str, subnet_id: int, ipv4_reservation: str) -> None:
        """Creates a new host object."""

    def getHostId(self) -> int:
        """Returns host identifier."""
    def toElement(self) -> Optional[Element]:
        """Returns host as a dictionary."""

    @property
    def use_count(self) -> int: ...

class HostMgr:
    @staticmethod
    def instance() -> "HostMgr":
        """Returns a sole instance of the HostMgr."""

    def add(self, host: Host, target: int = 0) -> None:
        """Adds a new host to data source."""

    def get(
        self, subnet_id: int, identifier_type: str, identifier: Optional[str] = None, target: int = 0
    ) -> Optional[Host]:
        """Returns a host connected to the IPv4 subnet."""

    def getAll4(self, subnet_id: int) -> List[Host]:
        """Returns all hosts in a DHCPv4 subnet."""

    def getPage4(self, subnet_id: int, source_index: int, lower_host_id: int, page_size: int) -> Tuple[List[Host], int]:
        """Returns range of hosts in a DHCPv4 subnet."""

    def del_(self, subnet_id: int, ip_address: str, target: int = 0) -> bool:
        """Attempts to delete a host by address."""

    def del4(self, subnet_id: int, identifier_type: str, identifier: str, target: int = 0) -> bool:
        """Attempts to delete a host by (subnet4-id, identifier, identifier-type)."""

class HostReservationParser4:
    def __init__(self) -> None: ...
    def parse(self, subnet_id: int, config: Any) -> Host: ...

class Lease4:
    def setContext(self, ctx: Any) -> "Lease4": ...
    def getContext(self) -> Optional[Element]: ...
    def toElement(self) -> Optional[Element]: ...
    @property
    def use_count(self) -> int: ...
    @property
    def addr(self) -> str: ...
    @addr.setter
    def addr(self, value: str) -> None: ...
    @property
    def valid_lft(self) -> int: ...
    @valid_lft.setter
    def valid_lft(self, value: int) -> None: ...
    @property
    def cltt(self) -> int: ...
    @cltt.setter
    def cltt(self, value: int) -> None: ...
    @property
    def subnet_id(self) -> int: ...
    @subnet_id.setter
    def subnet_id(self, value: int) -> None: ...
    @property
    def hostname(self) -> Optional[str]: ...
    @hostname.setter
    def hostname(self, value: Optional[str]) -> None: ...
    @property
    def fqdn_fwd(self) -> bool: ...
    @fqdn_fwd.setter
    def fqdn_fwd(self, value: bool) -> None: ...
    @property
    def fqdn_rev(self) -> bool: ...
    @fqdn_rev.setter
    def fqdn_rev(self, value: bool) -> None: ...
    @property
    def hwaddr(self) -> Optional[str]: ...
    @hwaddr.setter
    def hwaddr(self, value: str) -> None: ...
    @property
    def client_id(self) -> Optional[str]: ...
    @client_id.setter
    def client_id(self, value: Optional[str]) -> None: ...
    @property
    def state(self) -> int: ...
    @state.setter
    def state(self, value: int) -> None: ...

class LeaseMgr:
    def getLease4(
        self,
        addr: Optional[str] = None,
        hwaddr: Optional[str] = None,
        client_id: Optional[str] = None,
        subnet_id: Optional[int] = None,
    ) -> Optional[Union[Lease4, List[Lease4]]]: ...
    def getLeases4(
        self,
        subnet_id: Optional[int] = None,
        hostname: Optional[str] = None,
        lower_bound_address: Optional[str] = None,
        page_size: Optional[int] = None,
    ) -> List[Lease4]: ...
    def addLease(self, lease: Lease4) -> None: ...
    def deleteLease(self, addr: Optional[str] = None, lease: Optional[Lease4] = None) -> bool: ...
    def updateLease4(self, lease: Lease4) -> None: ...
    def wipeLeases4(self, subnet_id: int) -> int: ...
    def __init__(self) -> None: ...

class LibraryHandle:
    def __init__(self, manager: CalloutManager) -> None: ...
    def registerCommandCallout(self, name: str, callout: Callable) -> None: ...

class Option:
    def __init__(self, type: int) -> None: ...
    def getType(self) -> int: ...
    def getBytes(self) -> bytes: ...
    def setBytes(self, data: bytes) -> "Option": ...
    def getString(self) -> str: ...
    def setString(self, data: str) -> "Option": ...
    def getUint8(self) -> int: ...
    def setUint8(self, value: int) -> "Option": ...
    def getUint16(self) -> int: ...
    def setUint16(self, value: int) -> "Option": ...
    def getUint32(self) -> int: ...
    def setUint32(self, value: int) -> "Option": ...
    def addOption(self, option: "Option") -> "Option": ...
    def getOption(self, type: int) -> Optional["Option"]: ...
    def pack(self) -> bytes: ...
    def toText(self) -> str: ...
    @property
    def use_count(self) -> int: ...

class Pkt4:
    def __init__(
        self, data: Union[bytes, None] = None, msg_type: Optional[int] = None, transid: Optional[int] = None
    ) -> None:
        """Initializes an instance of Pkt4."""

    # Accessor and Mutator Methods
    def getType(self) -> int:
        """Gets the message type."""

    def setType(self, type: int) -> "Pkt4":
        """Sets the message type."""

    def getFlags(self) -> int:
        """Gets the message flags."""

    def setFlags(self, flags: int) -> "Pkt4":
        """Sets the message flags."""

    def getLocalAddr(self) -> str:
        """Gets the local address."""

    def setLocalAddr(self, addr: str) -> "Pkt4":
        """Sets the local address."""

    def getRemoteAddr(self) -> str:
        """Gets the remote address."""

    def setRemoteAddr(self, addr: str) -> "Pkt4":
        """Sets the remote address."""

    def getCiaddr(self) -> str:
        """Gets the client address."""

    def setCiaddr(self, addr: str) -> "Pkt4":
        """Sets the client address."""

    def getGiaddr(self) -> str:
        """Gets the gateway address."""

    def setGiaddr(self, addr: str) -> "Pkt4":
        """Sets the gateway address."""

    def getSiaddr(self) -> str:
        """Gets the server address."""

    def setSiaddr(self, addr: str) -> "Pkt4":
        """Sets the server address."""

    def getYiaddr(self) -> str:
        """Gets the 'your' (client) address."""

    def setYiaddr(self, addr: str) -> "Pkt4":
        """Sets the 'your' (client) address."""

    def getHWAddr(self) -> str:
        """Gets the hardware address."""

    def setHWAddr(self, addr: str) -> "Pkt4":
        """Sets the hardware address."""

    # Option Methods
    def delOption(self, type: int) -> bool:
        """Deletes an option by type."""

    def addOption(self, opt: Option) -> "Pkt4":
        """Adds an option."""

    def getOption(self, type: int) -> Optional[Option]:
        """Gets an option by type."""

    def getOptions(self) -> Optional[List[int]]:
        """Gets the list of options."""

    # Processing Methods
    def toText(self) -> str:
        """Converts the packet to text."""

    def pack(self) -> bytes:
        """Packs the message into bytes."""

    def unpack(self) -> None:
        """Unpacks the message from bytes."""

    # Properties
    @property
    def use_count(self) -> int:
        """Gets the use count."""

class SrvConfig:
    def toElement(self) -> Optional[Element]: ...
    def getCfgSubnets4(self) -> Optional[CfgSubnets4]: ...
    @property
    def use_count(self) -> int: ...

class Subnet4:
    def getID(self) -> int: ...
    def getValid(self) -> int: ...
    def inRange(self, addr: str) -> bool: ...
    def toText(self) -> str: ...
    def toElement(self) -> Optional[Element]: ...
    @property
    def use_count(self) -> int: ...
