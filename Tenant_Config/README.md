# ACI Tenant, VRF, and BD Configuration via REST API

This Ansible playbook is designed to **configure and update ACI Tenant, VRF, and Bridge Domain (BD)** using **REST API**. The solution leverage direct REST API calls for more flexibility and control.

## Features

- **Tenant Management**: Create and update ACI tenants.
- **VRF Management**: Configure and manage Virtual Routing and Forwarding (VRF) instances.
- **Bridge Domain (BD) Management**: Create and manage Bridge Domains (BD) at Layer 3 with Unicast as the default configuration.
- **REST API Integration**: Uses REST API calls to interact with the ACI fabric, bypassing the need for ACI-specific Ansible modules.

## File Structure

The project folder is organized as follows:

├── inventory.yaml # Inventory file with the configuration for the ACI environment. 
├── README.md # This README file. 
├── Tenant_BD_VRF.yaml # Main playbook to configure ACI Tenant, VRF, and BD via REST API. 
├── Tenant_Rendered.j2 # Template used to render the full Tenant configuration. 
├── Tenant_Template.j2 # Template for rendering Bridge Domain configuration (default uses Unicast at Layer 3). 
└── tenant_vars.yaml # Variables file where you define all parameters related to Tenant, VRF, and BD


## Configuration

### Template Modifications

By default, this playbook configures Bridge Domain (BD) at **Layer 3** with **Unicast** as the default. If you require a different configuration, please modify the `Tenant_Template.j2` to reflect your desired BD configuration.




