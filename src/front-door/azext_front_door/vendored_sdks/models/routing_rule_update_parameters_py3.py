# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RoutingRuleUpdateParameters(Model):
    """Routing rules to apply to an endpoint.

    :param frontend_endpoints: Frontend endpoints associated with this rule
    :type frontend_endpoints: list[~azure.mgmt.frontdoor.models.SubResource]
    :param accepted_protocols: Protocol schemes to match for this rule
    :type accepted_protocols: list[str or
     ~azure.mgmt.frontdoor.models.FrontDoorProtocol]
    :param patterns_to_match: The route patterns of the rule.
    :type patterns_to_match: list[str]
    :param enabled_state: Whether to enable use of this rule. Permitted values
     are 'Enabled' or 'Disabled'. Possible values include: 'Enabled',
     'Disabled'
    :type enabled_state: str or
     ~azure.mgmt.frontdoor.models.RoutingRuleEnabledState
    :param route_configuration: A reference to the routing configuration.
    :type route_configuration: ~azure.mgmt.frontdoor.models.RouteConfiguration
    """

    _attribute_map = {
        'frontend_endpoints': {'key': 'frontendEndpoints', 'type': '[SubResource]'},
        'accepted_protocols': {'key': 'acceptedProtocols', 'type': '[str]'},
        'patterns_to_match': {'key': 'patternsToMatch', 'type': '[str]'},
        'enabled_state': {'key': 'enabledState', 'type': 'str'},
        'route_configuration': {'key': 'routeConfiguration', 'type': 'RouteConfiguration'},
    }

    def __init__(self, *, frontend_endpoints=None, accepted_protocols=None, patterns_to_match=None, enabled_state=None, route_configuration=None, **kwargs) -> None:
        super(RoutingRuleUpdateParameters, self).__init__(**kwargs)
        self.frontend_endpoints = frontend_endpoints
        self.accepted_protocols = accepted_protocols
        self.patterns_to_match = patterns_to_match
        self.enabled_state = enabled_state
        self.route_configuration = route_configuration
