# Static Port Binding Role - Inventory

## Overview
This role processes Static Port Binding inventory and outputs it in YAML format for use in Jinja templates. The inventory structure provides details about the static port bindings, including VLANs and ports within the tenant and access point.

### Default Values
- **tenant_name**: If no tenant name is found, it will default to "Please input your correct tenant name".
- **ap_name**: If no AP (Access Point) name is found, it will default to "Please input your correct AP name".
- **status**: The default status for all entries is "created,modified". If something is to be deleted, you can manually change the status to "deleted".

### Jinja Template Customization
The default values can be changed in the Jinja template, allowing for more dynamic configurations.

## Structure of the Inventory
The inventory contains the following structure:

```yaml
tenant_name: Please input your correct tenant name
ap_name: Please input your correct AP name
epgs:
  - name: <EPG Name>
    vlans:
      - vlan: <VLAN ID>
        ports:
          - <port1>
          - <port2>
          - <port3>
```

- **tenant_name**: The name of the tenant.
- **ap_name**: The name of the access point.
- **epgs**: A list of EPGs (Endpoint Groups) within the tenant, each containing the following details:
  - **name**: The name of the EPG.
  - **vlans**: A list of VLANs associated with the EPG, including the following details:
    - **vlan**: The VLAN ID.
    - **ports**: A list of ports associated with the VLAN.

## Status Field
The **status** field is essential for indicating the action taken for the inventory item:
- **created,modified**: The default value for newly created or modified entries.
- **deleted**: To be manually updated if an item is to be deleted.

## Usage
To use this role, input a valid JSON file containing the necessary data. The role processes the data and generates a corresponding YAML file for use in Jinja templates.

### Example:

```bash
ansible-playbook -i inventory.yaml static_port_binding.yml
```

In the Jinja template, you can access values like:

```jinja
{{ tenant_name }}
{{ ap_name }}
{% for epg in epgs %}
  {{ epg.name }}
  {% for vlan in epg.vlans %}
    VLAN ID: {{ vlan.vlan }}
    Ports:
    {% for port in vlan.ports %}
      - {{ port }}
    {% endfor %}
  {% endfor %}
{% endfor %}
```

## Conclusion
This role provides a structured approach to managing Static Port Binding inventory in a tenant-based environment. The inventory can be easily customized in Jinja templates to suit specific requirements.


