import json
import yaml


def dump_to_yaml(inventory, output_file):
    """Helper function to write inventory data to a YAML file."""
    with open(output_file, 'w') as out_file:
        yaml.dump(inventory, out_file, default_flow_style=False, sort_keys=False)


def Networking_BD(filepath, output_file):
    """Process Networking BD inventory and output to YAML."""
    with open(filepath, mode='r') as f:
        reader = json.load(f)
        BDs = []

        # Initialize default values for tenant and vrf
        tenant_name = "Please input your correct tenant name"
        vrf_name = "Please input your correct vrf name"

        # Try to extract tenant_name from the data
        try:
            tenant_name = reader['imdata'][0]['fvTenant']['attributes']['name']
        except KeyError:
            pass  # If tenant_name is missing, it will remain the default value

        # Loop through 'fvTenant' children to find 'vrf_name'
        for child in reader['imdata'][0]['fvTenant']['children']:
            if 'fvCtx' in child:
                try:
                    vrf_name = child['fvCtx']['attributes']['name']
                    break  # Exit loop once vrf_name is found
                except KeyError:
                    pass  # Continue searching if the 'vrf_name' is missing

        # Iterate through the JSON data to extract BD information
        for item in reader['imdata'][0]['fvTenant']['children']:
            if 'fvBD' in item:
                bd_name = item['fvBD']['attributes']['name']
                unicast = item['fvBD']['attributes']['unicastRoute']
                desc = item['fvBD']['attributes']['descr']

                for child in item['fvBD']['children']:
                    if 'fvSubnet' in child:
                        ip = child['fvSubnet']['attributes']['ip']

                        BDs.append({
                            'name': bd_name,
                            'unicast': unicast,
                            'ip': ip,
                            'description': desc,
                            'status': "created,modified"
                        })

    # Prepare the inventory format for Jinja template
    inventory = {
        'tenant_name': tenant_name,
        'vrf_name': vrf_name,
        'bds': BDs
    }

    # Output the inventory format for Jinja template
    dump_to_yaml(inventory, output_file)


def AAEP(filepath, output_file):
    """Process AAEP inventory and output to YAML."""
    with open(filepath, mode='r') as f:
        reader = json.load(f)
        AAEPs = []
        # Initialize default values for tenant and vrf
        tenant_name = "Please input your correct tenant name"
        Ap_name = "Please input your correct AP name"
        # Try to extract tenant_name from the data
        try:
            tenant_name = reader['imdata'][0]['fvTenant']['attributes']['name']
        except KeyError:
            pass

        # Extract AAEP information from the JSON data
        for item in reader['imdata'][0]['fvTenant']['children']:
            if 'fvAp' in item:
                try:
                    Ap_name = item['fvAp']['attributes']['name']
                except KeyError:
                    pass
                for child in item['fvAp']['children']:
                    if 'fvAEPg' in child:
                        epg = child['fvAEPg']['attributes']
                        epg_name = epg['name']
                        epg_des = epg['descr']
                        epg_alias = epg['nameAlias']

                        for sub_child in child['fvAEPg']['children']:
                            if 'fvRsBd' in sub_child:
                                bd_name = sub_child['fvRsBd']['attributes']['tnFvBDName']

                                AAEPs.append({
                                    'name': epg_name,
                                    'description': epg_des,
                                    'alias': epg_alias,
                                    'mode': "regular",
                                    'BD_name': bd_name,
                                    'status': "created,modified"
                                })

    # Prepare the inventory format for Jinja template
    inventory = {
        'tenant_name': tenant_name,
        'ap_name': Ap_name,
        'epgs': AAEPs
    }

    # Output the inventory format for Jinja template
    dump_to_yaml(inventory, output_file)


def Static_Port_Binding(filepath, output_file):
    """Process Static Port Binding inventory and output to YAML."""
    with open(filepath, mode='r') as f:
        reader = json.load(f)
        epgs = []
        
        # Initialize default values for tenant and vrf
        tenant_name = "Please input your correct tenant name"
        Ap_name = "Please input your correct AP name"
        # Try to extract tenant_name from the data
        try:
            tenant_name = reader['imdata'][0]['fvTenant']['attributes']['name']
        except KeyError:
            pass

        # Extract Static Port Binding details from the JSON data
        for item in reader['imdata'][0]['fvTenant']['children']:
            if 'fvAp' in item:
                try:
                    Ap_name = item['fvAp']['attributes']['name']
                except KeyError:
                    pass

                for child in item['fvAp']['children']:
                    if 'fvAEPg' in child:
                        epg = child['fvAEPg']
                        epg_name = epg['attributes']['name']

                        vlans = {}
                        for sub_child in epg.get('children', []):
                            if 'fvRsPathAtt' in sub_child:
                                port_info = sub_child['fvRsPathAtt']['attributes']['tDn']
                                vlan_id = sub_child['fvRsPathAtt']['attributes']['encap']

                                # Group ports by VLAN
                                if vlan_id not in vlans:
                                    vlans[vlan_id] = []
                                vlans[vlan_id].append(port_info)

                        # Add EPG to the list with VLANs and ports
                        epgs.append({
                            'name': epg_name,
                            'vlans': [{'vlan': vlan_id, 'ports': port_info} for vlan_id, port_info in vlans.items()]
                        })

    # Prepare the inventory format for Jinja template
    inventory = {
        'tenant_name': tenant_name,
        'ap_name': Ap_name,
        'epgs': epgs
    }

    # Output the inventory format for Jinja template
    dump_to_yaml(inventory, output_file)


def L3Out(filepath, output_file):
    """Process L3Out OSPF inventory and output to YAML."""
    with open(filepath, mode='r') as f:
        reader = json.load(f)
        l3out_info = []
        router_info  = []

        # Initialize default values for L3Out and VRF
        tenant_name = "Please input your correct tenant name"
        vrf_name = "Please input your correct vrf name"
        # Extract OSPF details from 'ospfExtP'
        ospf_info = {}
        # Extract L3Out details from the 'fvTenant' → 'children' → 'l3extOut' section
        for item in reader['imdata'][0].get('fvTenant', {}).get('children', []):
            if 'l3extOut' in item:
                l3out = item['l3extOut']['attributes']
                l3out_name = l3out.get('name', 'Unknown')
                description = l3out.get('descr', 'No description')

                # Extract VRF from 'l3extRsEctx' (tnFvCtxName)
                for child in item.get('l3extOut', {}).get('children', []):
                    if 'l3extRsEctx' in child:
                        vrf_name = child['l3extRsEctx']['attributes'].get('tnFvCtxName', 'Unknown VRF')
                    if 'ospfExtP' in child:
                        ospf_info = {
                            'area_id': child['ospfExtP']['attributes'].get('areaId', 'Unknown'),
                            'area_type': child['ospfExtP']['attributes'].get('areaType', 'Unknown'),
                            'area_cost': child['ospfExtP']['attributes'].get('areaCost', 'Unknown'),
                            'area_ctrl': child['ospfExtP']['attributes'].get('areaCtrl', 'Unknown'),
                            'description': child['ospfExtP']['attributes'].get('descr', 'No description')
                        }
                    if 'l3extLNodeP' in child:
                        for sub_child in child.get('l3extLNodeP', {}).get('children', []):
                            if 'l3extRsNodeL3OutAtt' in sub_child:
                                # Extract rtrId, rtrIdLoopBack, tDn
                                router_info.append({
                                    'rtrId': sub_child['l3extRsNodeL3OutAtt']['attributes'].get('rtrId', 'Unknown'),
                                    'rtrIdLoopBack': sub_child['l3extRsNodeL3OutAtt']['attributes'].get('rtrIdLoopBack', 'Unknown'),
                                    'tDn': sub_child['l3extRsNodeL3OutAtt']['attributes'].get('tDn', 'Unknown')
                                })


                # Add extracted data to the list
                l3out_info.append({
                    'l3out_name': l3out_name,
                    'description': description,
                    'vrf_name': vrf_name,
                    'ospf_info': ospf_info,
                    'router_info': router_info,
                })

    # Prepare the inventory format for Jinja template or other uses
    inventory = {
        'l3out_info': l3out_info
    }

    # Output the inventory format to YAML file
    dump_to_yaml(inventory, output_file)

# Example usage of the function:
# L3Out_ospf_Config('/mnt/data/tn-Datacenter1.json', '/mnt/data/l3out_ospf_inventory.yaml')





def main(input_file_path):
    """Main function to process and generate inventory files."""
    # Export Inventory of Networking_BD
    Networking_BD_output = 'roles/Tenant_config/tests/inventory.yaml'
    Networking_BD(input_file_path, Networking_BD_output)

    # Export Inventory of AAEP
    AAEP_output = 'roles/AAEP_config/tests/inventory.yaml'
    AAEP(input_file_path, AAEP_output)

    # Export Inventory of Static Port Binding
    Static_Port_Binding_output = 'roles/Port_Binding_config/tests/inventory.yaml'
    Static_Port_Binding(input_file_path, Static_Port_Binding_output)

    # Export Iventory of L3Out
    L3Outs_output = 'roles/L3Out/tests/inventory.yaml'
    L3Out(input_file_path, L3Outs_output)

if __name__ == "__main__":
    main('/home/dsu979/Downloads/tn-Datacenter1.json')
