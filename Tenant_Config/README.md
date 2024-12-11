# ACI Tenant, VRF, and BD Configuration via REST API

This Ansible playbook is designed to **configure and update ACI Tenant, VRF, and Bridge Domain (BD)** using **REST API**. The solution avoids using the native ACI Ansible modules, instead leveraging direct REST API calls for more flexibility and control.

## Features

- **Tenant Management**: Create and update ACI tenants.
- **VRF Management**: Configure and manage Virtual Routing and Forwarding (VRF) instances.
- **Bridge Domain (BD) Management**: Create and manage Bridge Domains (BD) at Layer 3 with Unicast as the default configuration.
- **REST API Integration**: Uses REST API calls to interact with the ACI fabric, bypassing the need for ACI-specific Ansible modules.

## Prerequisites

Before running this playbook, ensure the following:

1. **Ansible**: Make sure you have Ansible installed on your system.
   - Install Ansible: `pip install ansible`
2. **Python dependencies**: The playbook uses the `requests` library to interact with the ACI REST API. Ensure it's installed:
   - Install dependencies: `pip install requests`
3. **APIC Authentication**: You will need a valid **APIC IP** and **authentication token** (Bearer token) to interact with the ACI REST API.

## File Structure


### Templates

- **Tenant_Rendered.j2**: Template used for rendering the full Tenant configuration.
- **Tenant_Template.j2**: Template used to render Bridge Domain configuration (default uses Unicast at Layer 3).
- **tenant_vars.yaml**: Variables file where you define all parameters related to Tenant, VRF, and BD.
- **Tenant.yaml**: Main playbook that performs the configurations by calling REST API endpoints.

## Configuration

### Template Modifications

By default, this playbook configures Bridge Domain (BD) at **Layer 3** with **Unicast** as the default. If you require a different configuration, please modify the `Tenant_Template.j2` to reflect your desired BD configuration.

For example, you can change the BD configuration by editing the following section:

```yaml
# Example of default configuration in Tenant_Template.j2
fvBD:
  attributes:
    name: "{{ bd_name }}"
    descr: "Created by Ansible"
    vnid: "{{ vnid }}"
    status: "created"
    l3Out: true  # Change this based on your requirement, e.g., for Layer 3 setup
    multicastMode: "unicast"  # Modify if necessary


