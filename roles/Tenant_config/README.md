# Tenant Role - Inventory

This role is responsible for generating the inventory file for the Tenant configuration, based on data processed from the input JSON.

## Inventory File
The generated inventory file is in YAML format and focuses on providing details about the tenant, VRF, and BD (Bridge Domain) configuration.

### Key Inventory Fields
- **tenant_name**: The name of the tenant. The default value is `"Please input your correct tenant name"` if not found in the input data.
- **vrf_name**: The name of the VRF (Virtual Routing and Forwarding). The default value is `"Please input your correct vrf name"` if not found in the input data.
- **bds**: A list of Bridge Domains (BDs) under the tenant. Each BD contains:
  - `name`: The name of the BD.
  - `unicast`: The unicast route configuration for the BD.
  - `ip`: The subnet IP address of the BD.
  - `description`: A description of the BD.
  - `status`: The current status, which is set to `"created,modified"` by default.

### Default Status
- The default `status` for each BD is `"created,modified"`.
- If an object is intended for deletion, the `status` can be changed to `"deleted"` in the Jinja template.

### Customizing the Output
- You can modify the `tenant_name`, `vrf_name`, and `bds` directly in the generated inventory file, or adjust the Jinja template to apply changes as necessary.

### Example Inventory
```yaml
tenant_name: "Tenant1"
vrf_name: "VRF1"
bds:
  - name: "BD1"
    unicast: "enabled"
    ip: "192.168.1.1"
    description: "Bridge Domain 1"
    status: "created,modified"
  - name: "BD2"
    unicast: "enabled"
    ip: "192.168.2.1"
    description: "Bridge Domain 2"
    status: "created,modified"
```

### Usage
To use this role:
1. Provide the input JSON file containing the tenant and BD information.
2. The output will be a YAML file that can be processed by Jinja templates for further configuration.

### Notes
- The template uses the default values for `tenant_name` and `vrf_name` if they are missing from the JSON input data.
- Ensure that the input file follows the expected format for successful parsing.


