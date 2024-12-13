# ACI Update and Configuration Automation using REST API

## Prerequisites

Before using this playbook, make sure you have the following:

- **Ansible** installed. If not, you can install it using pip:
    pip install ansible

- **Python 3.x** installed on your machine.
- Access to the **ACI APIC (Application Policy Infrastructure Controller)** where you want to apply the configurations.

---

## How to Use

### 1. Clone the Repository

Clone this repository to your local machine:

    git clone https://git.dision.office/dsu979/Ansible_ACI.git
    cd ACI_Migration/Ansible_ACI

---

### 2. Update Inventory Files

You will find the inventory files in the `roles` directory:

- `roles/AAEP_config/tests/inventory`: For AAEP configuration.
- `roles/Tenant_config/inventory.yaml`: For Tenant configuration.

Make sure these files contain the correct APIC details and inventory information.

---

### 3. Customize Variables

You can customize your variables inside each role's `vars/main.yml`. For example, for the **Tenant Configuration**, the file is located at `roles/Tenant_config/vars/main.yml`. Update the following variables:

- `tenant_name`: The name of your tenant.
- `aci_host`: The APIC IP address or hostname.
- `aci_user` & `aci_password`: Credentials for your APIC.

---

### 4. Run the Playbook

To run the playbook, use the following command:

    ansible-playbook playbook.yaml

This will execute the playbook and apply the configurations defined in the roles (such as Tenant and AAEP).

---

### 5. Test Configurations

There are test inventory files available in the `tests` directories within each role. You can use these for testing the playbooks locally.

