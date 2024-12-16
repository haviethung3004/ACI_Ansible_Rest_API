# AAEP Role - Inventory

## Purpose:
This role processes and generates an inventory YAML file for the **AAEP** configuration. It reads the input JSON data, extracts relevant information, and outputs a structured inventory suitable for use in Jinja templates.

## Inventory Structure:
The inventory file contains the following fields:

- `tenant_name`: Name of the tenant.
- `ap_name`: Name of the AP (Access Point).
- `epgs`: A list of EPG (Endpoint Groups) objects, each with the following details:
  - `name`: EPG name.
  - `description`: EPG description.
  - `alias`: EPG alias.
  - `mode`: Mode of the EPG (always "regular").
  - `BD_name`: The associated BD (Bridge Domain) name.
  - `status`: The status of the object, which can be:
    - `"created,modified"`: Default value for newly created/modified objects.
    - `"deleted"`: Change this status in the Jinja template when you want to mark an object as deleted.

## Default Status:
The default status for each object is set to `"created,modified"`. You can change this to `"deleted"` in the **Jinja template** when you want to delete an object.

### Example:
```yaml
tenant_name: your-tenant-name
ap_name: your-ap-name
epgs:
  - name: your-epg-name
    description: your-epg-description
    alias: your-epg-alias
    mode: regular
    BD_name: your-bd-name
    status: created,modified  # Change to "deleted" if you want to delete the EPG
```

## Customization:
- You can easily adjust the default values by modifying the Jinja template where the inventory data is used.
- The status field can be dynamically altered based on your template logic.

## Requirements:
Ensure the input JSON follows the expected structure for proper extraction of information.


