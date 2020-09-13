""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core.typesystem import schema, fields


class RouteRuleInfoSchema(schema.ResponseSchema):
    """ RouteRuleInfo - 路由规则信息
    """

    fields = {
        "DstAddr": fields.Str(required=False, load_from="DstAddr"),
        "NexthopId": fields.Str(required=False, load_from="NexthopId"),
        "NexthopType": fields.Str(required=False, load_from="NexthopType"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RouteRuleId": fields.Str(required=False, load_from="RouteRuleId"),
        "RuleType": fields.Int(required=False, load_from="RuleType"),
    }


class RouteTableInfoSchema(schema.ResponseSchema):
    """ RouteTableInfo - 路由表信息
    """

    fields = {
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RouteRules": fields.List(RouteRuleInfoSchema()),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
        "RouteTableType": fields.Int(
            required=False, load_from="RouteTableType"
        ),
        "SubnetCount": fields.Str(required=False, load_from="SubnetCount"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
    }


class SubnetInfoSchema(schema.ResponseSchema):
    """ SubnetInfo - 子网信息
    """

    fields = {
        "AvailableIPs": fields.Int(required=False, load_from="AvailableIPs"),
        "CreateTime": fields.Int(required=False, load_from="CreateTime"),
        "Gateway": fields.Str(required=False, load_from="Gateway"),
        "HasNATGW": fields.Bool(required=False, load_from="HasNATGW"),
        "IPv6Network": fields.Str(required=False, load_from="IPv6Network"),
        "Netmask": fields.Str(required=False, load_from="Netmask"),
        "Remark": fields.Str(required=False, load_from="Remark"),
        "RouteTableId": fields.Str(required=False, load_from="RouteTableId"),
        "Subnet": fields.Str(required=False, load_from="Subnet"),
        "SubnetId": fields.Str(required=False, load_from="SubnetId"),
        "SubnetName": fields.Str(required=False, load_from="SubnetName"),
        "SubnetType": fields.Int(required=False, load_from="SubnetType"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
        "VPCName": fields.Str(required=False, load_from="VPCName"),
        "Zone": fields.Str(required=False, load_from="Zone"),
    }


class SubnetResourceSchema(schema.ResponseSchema):
    """ SubnetResource - 子网下资源
    """

    fields = {
        "IP": fields.Str(required=False, load_from="IP"),
        "IPv6Address": fields.Str(required=False, load_from="IPv6Address"),
        "Name": fields.Str(required=False, load_from="Name"),
        "ResourceId": fields.Str(required=False, load_from="ResourceId"),
        "ResourceType": fields.Str(required=False, load_from="ResourceType"),
        "SubResourceId": fields.Str(required=False, load_from="SubResourceId"),
        "SubResourceName": fields.Str(
            required=False, load_from="SubResourceName"
        ),
        "SubResourceType": fields.Str(
            required=False, load_from="SubResourceType"
        ),
    }


class VPCNetworkInfoSchema(schema.ResponseSchema):
    """ VPCNetworkInfo - vpc地址空间信息
    """

    fields = {
        "Network": fields.Str(required=False, load_from="Network"),
        "SubnetCount": fields.Int(required=False, load_from="SubnetCount"),
    }


class VPCInfoSchema(schema.ResponseSchema):
    """ VPCInfo - VPC信息
    """

    fields = {
        "CreateTime": fields.Int(required=True, load_from="CreateTime"),
        "IPv6Network": fields.Str(required=False, load_from="IPv6Network"),
        "Name": fields.Str(required=True, load_from="Name"),
        "Network": fields.List(fields.Str()),
        "NetworkInfo": fields.List(VPCNetworkInfoSchema()),
        "OperatorName": fields.Str(required=False, load_from="OperatorName"),
        "SubnetCount": fields.Int(required=True, load_from="SubnetCount"),
        "Tag": fields.Str(required=True, load_from="Tag"),
        "UpdateTime": fields.Int(required=True, load_from="UpdateTime"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class VPCIntercomInfoSchema(schema.ResponseSchema):
    """ VPCIntercomInfo -
    """

    fields = {
        "DstRegion": fields.Str(required=False, load_from="DstRegion"),
        "Name": fields.Str(required=False, load_from="Name"),
        "Network": fields.List(fields.Str()),
        "ProjectId": fields.Str(required=False, load_from="ProjectId"),
        "Tag": fields.Str(required=False, load_from="Tag"),
        "VPCId": fields.Str(required=False, load_from="VPCId"),
    }


class VINCInfoSchema(schema.ResponseSchema):
    fields = {
        "AttachInstanceId": fields.Str(required=True, load_from="AttachInstanceId"),
        "Default"         : fields.Bool(required=True, load_from="Default"),
        "FirewallIdSet"   : fields.List(fields.Str()),
        "Gateway"         : fields.Str(required=True, load_from="Gateway"),
        "InterfaceId"     : fields.Str(required=True, load_from="InterfaceId"),
        "MacAddress"      : fields.Str(required=True, load_from="MacAddress"),
        "Name"            : fields.Str(required=True, load_from="Name"),
        "Netmask"         : fields.Str(required=True, load_from="Netmask"),
        "PrivateIpSet"    : fields.List(fields.Str()),
        "Remark"          : fields.Str(required=True, load_from="Remark"),
        "Status"          : fields.Int(required=True, load_from="Status"),
        "SubnetId"        : fields.Str(required=True, load_from="SubnetId"),
        "Tag"             : fields.Str(required=True, load_from="Tag"),
        "VPCId"           : fields.Str(required=False, load_from="VPCId"),
    }
