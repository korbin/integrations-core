# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)
import functools
import ssl

import requests
from pyVim import connect
from pyVmomi import vim, vmodl

from datadog_checks.vsphere.constants import ALL_RESOURCES, MAX_QUERY_METRICS_OPTION, UNLIMITED_HIST_METRICS_PER_QUERY

# Python 3 only
PROTOCOL_TLS_CLIENT = getattr(ssl, 'PROTOCOL_TLS_CLIENT', ssl.PROTOCOL_TLS)


def get_tags():
    pass
    # ## Get token: vmware-api-session-id
    # https://vmware.github.io/vsphere-automation-sdk-rest/6.5/operations/com/vmware/cis/session.create-operation.html

    # ## Get all tags
    # https://vmware.github.io/vsphere-automation-sdk-rest/6.5/operations/com/vmware/cis/tagging/tag.list-operation.html
    # {
    #     "value": [
    #         "urn:vmomi:InventoryServiceTag:9a55f4a6-1290-4a57-a9c9-632a2e774970:GLOBAL",
    #         "urn:vmomi:InventoryServiceTag:370dd9a7-ff82-4a37-beb3-ab6791f3d604:GLOBAL",
    #         "urn:vmomi:InventoryServiceTag:a5d0c1a2-c021-4d82-ada7-9e3815c60e85:GLOBAL",
    #         "urn:vmomi:InventoryServiceTag:b34096e9-91c8-4096-9f88-c31473375508:GLOBAL",
    #         "urn:vmomi:InventoryServiceTag:40d3b19c-59eb-4747-813d-c9482a8e068a:GLOBAL",
    #         "urn:vmomi:InventoryServiceTag:da5e9cde-524c-4971-8d6e-4815ee1e8dda:GLOBAL"
    #     ]
    # }

    # ## Get name for each tag
    # https://vmware.github.io/vsphere-automation-sdk-rest/6.5/operations/com/vmware/cis/tagging/tag.get-operation.html
    # {
    #     "value": {
    #         "category_id": "urn:vmomi:InventoryServiceCategory:41feb681-9ba1-46c0-97ac-c4521e813ca3:GLOBAL",
    #         "name": "MyTagFoo2",
    #         "description": "MyTagFoo2 Description",
    #         "id": "urn:vmomi:InventoryServiceTag:a5d0c1a2-c021-4d82-ada7-9e3815c60e85:GLOBAL",
    #         "used_by": []
    #     }
    # }

    # ## For each tag, get objects
    # https://vmware.github.io/vsphere-automation-sdk-rest/6.5/operations/com/vmware/cis/tagging/tag_association.list_attached_objects_on_tags-operation.html
    # {
    #     "value": [
    #         {
    #             "object_ids": [
    #                 {
    #                     "id": "vm-745",
    #                     "type": "VirtualMachine"
    #                 }
    #             ],
    #             "tag_id": "urn:vmomi:InventoryServiceTag:b34096e9-91c8-4096-9f88-c31473375508:GLOBAL"
    #         }
    #     ]
    # }

