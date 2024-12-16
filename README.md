# APIC Automation with Ansible

This repository contains Ansible playbooks and roles for automating Cisco APIC (Application Policy Infrastructure Controller) configurations using the REST API and Bulk ACI. The code provides a structured approach to configure ACI policies, manage tenants, bridge domains, application profiles, and more. The repository is designed to streamline the process of managing ACI infrastructure with the power of automation.

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Directory Structure](#directory-structure)
4. [Installation and Setup](#installation-and-setup)
5. [Usage](#usage)
6. [Roles Overview](#roles-overview)
7. [Testing](#testing)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction

This project leverages Ansible to automate configuration tasks in Cisco's APIC using the ACI REST API and Bulk operations. The aim is to simplify the deployment and management of ACI policies, including the configuration of application profiles, tenants, and port bindings.

## Prerequisites

Before using this Ansible automation, ensure you have the following prerequisites:
- **Ansible** version 2.9 or higher installed.
- **Cisco ACI APIC** credentials (username and password).
- **Python 3.x** and necessary libraries (e.g., `requests`, `pyyaml`).
- **Cisco ACI REST API** access configured in your environment.
- **Ansible collections for Cisco ACI**, which can be installed via:

  ```bash
  ansible-galaxy collection install cisco.aci
  ```

## Directory Structure

The directory structure is as follows:

```
.
├── Export_inventory.py      # Python script for exporting inventory data
├── host_vars                # Directory containing host variable files
│   └── localhost.yml        # Host variable file for localhost
├── playbook.yaml            # Main Ansible playbook for orchestrating tasks
├── README.md                # Project documentation
└── roles                    # Ansible roles for different ACI configurations
    ├── AAEP_config          # Role for configuring AAEP settings
    ├── Port_Binding_config  # Role for configuring port bindings
    └── Tenant_config        # Role for configuring tenant settings
```

- **Export_inventory.py**: A Python script to export the APIC inventory into a format compatible with Ansible.
- **host_vars/**: Directory containing variable files for different hosts, with `localhost.yml` being the configuration file for localhost.
- **playbook.yaml**: Main playbook that includes all the tasks to be automated.
- **roles/**: Contains reusable roles for different ACI configuration tasks:
    - **AAEP_config**: Configures AAEP (Attachable Access Entity Profile) settings.
    - **Port_Binding_config**: Configures port bindings in the ACI fabric.
    - **Tenant_config**: Manages tenant configurations and policies.

## Installation and Setup

1. **Clone the Repository**:

   Clone this repository to your local machine using Git:

   ```bash
   git clone https://github.com/yourusername/aci-automation.git
   cd aci-automation
   ```

2. **Install Dependencies**:

   Install Ansible and the required collections:

   ```bash
   pip install ansible
   ansible-galaxy collection install cisco.aci
   ```

3. **Configure Inventory**:

   Edit the `host_vars/localhost.yml` file to include your APIC credentials and any additional configuration required for your environment.

4. **Configure Variables**:

   Each role in the `roles` directory may have its own set of variables defined in `defaults/main.yml` or `vars/main.yml`. Ensure these are configured according to your ACI environment.

## Usage

Once the setup is complete, you can use the following command to run the playbook:

```bash
ansible-playbook playbook.yaml -i host_vars/localhost.yml
```

This will execute the playbook, applying the configurations defined in the respective roles.

### Example: Apply Tenant Configuration

To apply tenant configurations, you can run the playbook with a specific tag:

```bash
ansible-playbook playbook.yaml -i host_vars/localhost.yml --tags "tenant"
```

## Roles Overview

### 1. AAEP_config
The `AAEP_config` role is responsible for configuring the **Attachable Access Entity Profile** (AAEP) in the ACI fabric. AAEPs define the configuration for how devices (like switches) are connected to the ACI fabric.

#### Variables:
- `aci_aaep_name`: Name of the AAEP.
- `aci_aaep_ports`: List of ports to be included in the AAEP.

### 2. Port_Binding_config
The `Port_Binding_config` role configures port bindings within the ACI fabric, ensuring that physical or virtual ports are properly associated with the correct profiles.

#### Variables:
- `aci_binding_name`: The name for the port binding.
- `aci_binding_ports`: List of ports for binding.

### 3. Tenant_config
The `Tenant_config` role manages the configuration of tenants, application profiles, bridge domains, and subnets within ACI.

#### Variables:
- `aci_tenant_name`: Name of the tenant.
- `aci_application_profiles`: List of application profiles to be configured for the tenant.
- `aci_bridge_domains`: List of bridge domains to be configured.

## Testing

Unit tests are located in the `roles` directories under the `tests` folder. You can run the tests using the following command:

```bash
ansible-playbook roles/AAEP_config/tests/test.yml
```

You can extend these tests to match your own environment.

## License

This project is licensed under the MIT License.


