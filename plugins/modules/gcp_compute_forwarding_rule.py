#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    AUTO GENERATED CODE     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_forwarding_rule
description:
- A ForwardingRule resource. A ForwardingRule resource specifies which pool of target
  virtual machines to forward a packet to if it matches the given [IPAddress, IPProtocol,
  portRange] tuple.
short_description: Creates a GCP ForwardingRule
version_added: 2.6
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
  description:
    description:
    - An optional description of this resource. Provide this property when you create
      the resource.
    required: false
  ip_address:
    description:
    - The IP address that this forwarding rule is serving on behalf of.
    - Addresses are restricted based on the forwarding rule's load balancing scheme
      (EXTERNAL or INTERNAL) and scope (global or regional).
    - When the load balancing scheme is EXTERNAL, for global forwarding rules, the
      address must be a global IP, and for regional forwarding rules, the address
      must live in the same region as the forwarding rule. If this field is empty,
      an ephemeral IPv4 address from the same scope (global or regional) will be assigned.
      A regional forwarding rule supports IPv4 only. A global forwarding rule supports
      either IPv4 or IPv6.
    - When the load balancing scheme is INTERNAL, this can only be an RFC 1918 IP
      address belonging to the network/subnet configured for the forwarding rule.
      By default, if this field is empty, an ephemeral internal IP address will be
      automatically allocated from the IP range of the subnet or network configured
      for this forwarding rule.
    - 'An address can be specified either by a literal IP address or a URL reference
      to an existing Address resource. The following examples are all valid: * 100.1.2.3
      * U(https://www.googleapis.com/compute/v1/projects/project/regions/region/addresses/address)
      * projects/project/regions/region/addresses/address * regions/region/addresses/address
      * global/addresses/address * address .'
    required: false
  ip_protocol:
    description:
    - The IP protocol to which this rule applies. Valid options are TCP, UDP, ESP,
      AH, SCTP or ICMP.
    - When the load balancing scheme is INTERNAL, only TCP and UDP are valid.
    required: false
    choices:
    - TCP
    - UDP
    - ESP
    - AH
    - SCTP
    - ICMP
  backend_service:
    description:
    - A reference to a BackendService to receive the matched traffic.
    - This is used for internal load balancing.
    - "(not used for external load balancing) ."
    - 'This field represents a link to a BackendService resource in GCP. It can be
      specified in two ways. First, you can place in the selfLink of the resource
      here as a string Alternatively, you can add `register: name-of-resource` to
      a gcp_compute_backend_service task and then set this backend_service field to
      "{{ name-of-resource }}"'
    required: false
  ip_version:
    description:
    - The IP Version that will be used by this forwarding rule. Valid options are
      IPV4 or IPV6. This can only be specified for a global forwarding rule.
    required: false
    choices:
    - IPV4
    - IPV6
  load_balancing_scheme:
    description:
    - 'This signifies what the ForwardingRule will be used for and can only take the
      following values: INTERNAL, EXTERNAL The value of INTERNAL means that this will
      be used for Internal Network Load Balancing (TCP, UDP). The value of EXTERNAL
      means that this will be used for External Load Balancing (HTTP(S) LB, External
      TCP/UDP LB, SSL Proxy) .'
    required: false
    choices:
    - INTERNAL
    - EXTERNAL
  name:
    description:
    - Name of the resource; provided by the client when the resource is created. The
      name must be 1-63 characters long, and comply with RFC1035. Specifically, the
      name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
      which means the first character must be a lowercase letter, and all following
      characters must be a dash, lowercase letter, or digit, except the last character,
      which cannot be a dash.
    required: true
  network:
    description:
    - For internal load balancing, this field identifies the network that the load
      balanced IP should belong to for this Forwarding Rule. If this field is not
      specified, the default network will be used.
    - This field is not used for external load balancing.
    - 'This field represents a link to a Network resource in GCP. It can be specified
      in two ways. First, you can place in the selfLink of the resource here as a
      string Alternatively, you can add `register: name-of-resource` to a gcp_compute_network
      task and then set this network field to "{{ name-of-resource }}"'
    required: false
  port_range:
    description:
    - This field is used along with the target field for TargetHttpProxy, TargetHttpsProxy,
      TargetSslProxy, TargetTcpProxy, TargetVpnGateway, TargetPool, TargetInstance.
    - Applicable only when IPProtocol is TCP, UDP, or SCTP, only packets addressed
      to ports in the specified range will be forwarded to target.
    - Forwarding rules with the same [IPAddress, IPProtocol] pair must have disjoint
      port ranges.
    - 'Some types of forwarding target have constraints on the acceptable ports: *
      TargetHttpProxy: 80, 8080 * TargetHttpsProxy: 443 * TargetTcpProxy: 25, 43,
      110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222 * TargetSslProxy: 25,
      43, 110, 143, 195, 443, 465, 587, 700, 993, 995, 1883, 5222 * TargetVpnGateway:
      500, 4500 .'
    required: false
  ports:
    description:
    - This field is used along with the backend_service field for internal load balancing.
    - When the load balancing scheme is INTERNAL, a single port or a comma separated
      list of ports can be configured. Only packets addressed to these ports will
      be forwarded to the backends configured with this forwarding rule.
    - You may specify a maximum of up to 5 ports.
    required: false
  subnetwork:
    description:
    - A reference to a subnetwork.
    - For internal load balancing, this field identifies the subnetwork that the load
      balanced IP should belong to for this Forwarding Rule.
    - If the network specified is in auto subnet mode, this field is optional. However,
      if the network is in custom subnet mode, a subnetwork must be specified.
    - This field is not used for external load balancing.
    - 'This field represents a link to a Subnetwork resource in GCP. It can be specified
      in two ways. First, you can place in the selfLink of the resource here as a
      string Alternatively, you can add `register: name-of-resource` to a gcp_compute_subnetwork
      task and then set this subnetwork field to "{{ name-of-resource }}"'
    required: false
  target:
    description:
    - A reference to a TargetPool resource to receive the matched traffic.
    - For regional forwarding rules, this target must live in the same region as the
      forwarding rule. For global forwarding rules, this target must be a global load
      balancing resource. The forwarded traffic must be of a type appropriate to the
      target object.
    - This field is not used for internal load balancing.
    - 'This field represents a link to a TargetPool resource in GCP. It can be specified
      in two ways. First, you can place in the selfLink of the resource here as a
      string Alternatively, you can add `register: name-of-resource` to a gcp_compute_target_pool
      task and then set this target field to "{{ name-of-resource }}"'
    required: false
    version_added: 2.7
  network_tier:
    description:
    - 'The networking tier used for configuring this address. This field can take
      the following values: PREMIUM or STANDARD. If this field is not specified, it
      is assumed to be PREMIUM.'
    required: false
    version_added: 2.8
    choices:
    - PREMIUM
    - STANDARD
  region:
    description:
    - A reference to the region where the regional forwarding rule resides.
    - This field is not applicable to global forwarding rules.
    required: true
extends_documentation_fragment: gcp
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/latest/forwardingRule)'
- 'Official Documentation: U(https://cloud.google.com/compute/docs/load-balancing/network/forwarding-rules)'
'''

EXAMPLES = '''
- name: create a address
  gcp_compute_address:
    name: address-forwardingrule
    region: us-west1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: address

- name: create a target pool
  gcp_compute_target_pool:
    name: targetpool-forwardingrule
    region: us-west1
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: targetpool

- name: create a forwarding rule
  gcp_compute_forwarding_rule:
      name: "test_object"
      region: us-west1
      target: "{{ targetpool }}"
      ip_protocol: TCP
      port_range: 80-80
      ip_address: "{{ address.address }}"
      project: "test_project"
      auth_kind: "serviceaccount"
      service_account_file: "/tmp/auth.pem"
      state: present
'''

RETURN = '''
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
description:
  description:
  - An optional description of this resource. Provide this property when you create
    the resource.
  returned: success
  type: str
id:
  description:
  - The unique identifier for the resource.
  returned: success
  type: int
IPAddress:
  description:
  - The IP address that this forwarding rule is serving on behalf of.
  - Addresses are restricted based on the forwarding rule's load balancing scheme
    (EXTERNAL or INTERNAL) and scope (global or regional).
  - When the load balancing scheme is EXTERNAL, for global forwarding rules, the address
    must be a global IP, and for regional forwarding rules, the address must live
    in the same region as the forwarding rule. If this field is empty, an ephemeral
    IPv4 address from the same scope (global or regional) will be assigned. A regional
    forwarding rule supports IPv4 only. A global forwarding rule supports either IPv4
    or IPv6.
  - When the load balancing scheme is INTERNAL, this can only be an RFC 1918 IP address
    belonging to the network/subnet configured for the forwarding rule. By default,
    if this field is empty, an ephemeral internal IP address will be automatically
    allocated from the IP range of the subnet or network configured for this forwarding
    rule.
  - 'An address can be specified either by a literal IP address or a URL reference
    to an existing Address resource. The following examples are all valid: * 100.1.2.3
    * U(https://www.googleapis.com/compute/v1/projects/project/regions/region/addresses/address)
    * projects/project/regions/region/addresses/address * regions/region/addresses/address
    * global/addresses/address * address .'
  returned: success
  type: str
IPProtocol:
  description:
  - The IP protocol to which this rule applies. Valid options are TCP, UDP, ESP, AH,
    SCTP or ICMP.
  - When the load balancing scheme is INTERNAL, only TCP and UDP are valid.
  returned: success
  type: str
backendService:
  description:
  - A reference to a BackendService to receive the matched traffic.
  - This is used for internal load balancing.
  - "(not used for external load balancing) ."
  returned: success
  type: str
ipVersion:
  description:
  - The IP Version that will be used by this forwarding rule. Valid options are IPV4
    or IPV6. This can only be specified for a global forwarding rule.
  returned: success
  type: str
loadBalancingScheme:
  description:
  - 'This signifies what the ForwardingRule will be used for and can only take the
    following values: INTERNAL, EXTERNAL The value of INTERNAL means that this will
    be used for Internal Network Load Balancing (TCP, UDP). The value of EXTERNAL
    means that this will be used for External Load Balancing (HTTP(S) LB, External
    TCP/UDP LB, SSL Proxy) .'
  returned: success
  type: str
name:
  description:
  - Name of the resource; provided by the client when the resource is created. The
    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
    name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
    which means the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last character,
    which cannot be a dash.
  returned: success
  type: str
network:
  description:
  - For internal load balancing, this field identifies the network that the load balanced
    IP should belong to for this Forwarding Rule. If this field is not specified,
    the default network will be used.
  - This field is not used for external load balancing.
  returned: success
  type: str
portRange:
  description:
  - This field is used along with the target field for TargetHttpProxy, TargetHttpsProxy,
    TargetSslProxy, TargetTcpProxy, TargetVpnGateway, TargetPool, TargetInstance.
  - Applicable only when IPProtocol is TCP, UDP, or SCTP, only packets addressed to
    ports in the specified range will be forwarded to target.
  - Forwarding rules with the same [IPAddress, IPProtocol] pair must have disjoint
    port ranges.
  - 'Some types of forwarding target have constraints on the acceptable ports: * TargetHttpProxy:
    80, 8080 * TargetHttpsProxy: 443 * TargetTcpProxy: 25, 43, 110, 143, 195, 443,
    465, 587, 700, 993, 995, 1883, 5222 * TargetSslProxy: 25, 43, 110, 143, 195, 443,
    465, 587, 700, 993, 995, 1883, 5222 * TargetVpnGateway: 500, 4500 .'
  returned: success
  type: str
ports:
  description:
  - This field is used along with the backend_service field for internal load balancing.
  - When the load balancing scheme is INTERNAL, a single port or a comma separated
    list of ports can be configured. Only packets addressed to these ports will be
    forwarded to the backends configured with this forwarding rule.
  - You may specify a maximum of up to 5 ports.
  returned: success
  type: list
subnetwork:
  description:
  - A reference to a subnetwork.
  - For internal load balancing, this field identifies the subnetwork that the load
    balanced IP should belong to for this Forwarding Rule.
  - If the network specified is in auto subnet mode, this field is optional. However,
    if the network is in custom subnet mode, a subnetwork must be specified.
  - This field is not used for external load balancing.
  returned: success
  type: str
target:
  description:
  - A reference to a TargetPool resource to receive the matched traffic.
  - For regional forwarding rules, this target must live in the same region as the
    forwarding rule. For global forwarding rules, this target must be a global load
    balancing resource. The forwarded traffic must be of a type appropriate to the
    target object.
  - This field is not used for internal load balancing.
  returned: success
  type: str
networkTier:
  description:
  - 'The networking tier used for configuring this address. This field can take the
    following values: PREMIUM or STANDARD. If this field is not specified, it is assumed
    to be PREMIUM.'
  returned: success
  type: str
region:
  description:
  - A reference to the region where the regional forwarding rule resides.
  - This field is not applicable to global forwarding rules.
  returned: success
  type: str
'''

################################################################################
# Imports
################################################################################

from ansible.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest, replace_resource_dict
import json
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            description=dict(type='str'),
            ip_address=dict(type='str'),
            ip_protocol=dict(type='str', choices=['TCP', 'UDP', 'ESP', 'AH', 'SCTP', 'ICMP']),
            backend_service=dict(),
            ip_version=dict(type='str', choices=['IPV4', 'IPV6']),
            load_balancing_scheme=dict(type='str', choices=['INTERNAL', 'EXTERNAL']),
            name=dict(required=True, type='str'),
            network=dict(),
            port_range=dict(type='str'),
            ports=dict(type='list', elements='str'),
            subnetwork=dict(),
            target=dict(),
            network_tier=dict(type='str', choices=['PREMIUM', 'STANDARD']),
            region=dict(required=True, type='str'),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#forwardingRule'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind, fetch)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, collection(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind, fetch):
    update_fields(module, resource_to_request(module), response_to_hash(module, fetch))
    return fetch_resource(module, self_link(module), kind)


def update_fields(module, request, response):
    if response.get('target') != request.get('target'):
        target_update(module, request, response)


def target_update(module, request, response):
    auth = GcpSession(module, 'compute')
    auth.post(
        ''.join(["https://www.googleapis.com/compute/v1/", "projects/{project}/regions/{region}/forwardingRules/{name}/setTarget"]).format(**module.params),
        {u'target': replace_resource_dict(module.params.get(u'target', {}), 'selfLink')},
    )


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#forwardingRule',
        u'description': module.params.get('description'),
        u'IPAddress': module.params.get('ip_address'),
        u'IPProtocol': module.params.get('ip_protocol'),
        u'backendService': replace_resource_dict(module.params.get(u'backend_service', {}), 'selfLink'),
        u'ipVersion': module.params.get('ip_version'),
        u'loadBalancingScheme': module.params.get('load_balancing_scheme'),
        u'name': module.params.get('name'),
        u'network': replace_resource_dict(module.params.get(u'network', {}), 'selfLink'),
        u'portRange': module.params.get('port_range'),
        u'ports': module.params.get('ports'),
        u'subnetwork': replace_resource_dict(module.params.get(u'subnetwork', {}), 'selfLink'),
        u'target': replace_resource_dict(module.params.get(u'target', {}), 'selfLink'),
        u'networkTier': module.params.get('network_tier'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/forwardingRules/{name}".format(**module.params)


def collection(module):
    return "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/forwardingRules".format(**module.params)


def return_if_object(module, response, kind, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'description': response.get(u'description'),
        u'id': response.get(u'id'),
        u'IPAddress': response.get(u'IPAddress'),
        u'IPProtocol': response.get(u'IPProtocol'),
        u'backendService': response.get(u'backendService'),
        u'ipVersion': response.get(u'ipVersion'),
        u'loadBalancingScheme': response.get(u'loadBalancingScheme'),
        u'name': response.get(u'name'),
        u'network': response.get(u'network'),
        u'portRange': response.get(u'portRange'),
        u'ports': response.get(u'ports'),
        u'subnetwork': response.get(u'subnetwork'),
        u'target': response.get(u'target'),
        u'networkTier': module.params.get('network_tier'),
    }


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/operations/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#forwardingRule')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = async_op_url(module, {'op_id': op_id})
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation')
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


if __name__ == '__main__':
    main()
