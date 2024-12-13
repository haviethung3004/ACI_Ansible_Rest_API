#Import json module
import json
import yaml


def Networking_BD(filepath, output_file):
  with open(f'{filepath}', mode='r') as f:
    reader = json.load(f)
    BDs = []
    for item in reader['imdata'][0]['fvTenant']['children']:
      if 'fvBD' in item:
        bd_name =  item['fvBD']['attributes']['name']
        unicast =  item['fvBD']['attributes']['unicastRoute']
        desc = item['fvBD']['attributes']['descr']
        for item in item['fvBD']['children']:
          if 'fvSubnet' in item:
            ip = item['fvSubnet']['attributes']['ip']
          if 'dhcpLbl' in item:
            dhcp_name = item['dhcpLbl']['attributes']['ip']

            BDs.append({
              'name': f"{bd_name}",
              'unicast': f"{unicast}",
              'ip': f"{ip}",
              'description': f"{desc}",
              'status': "created,modified"
            })
    # Prepare the inventory format for Jinja template
    inventory = {
        'tenant_name': "PLease input your correct tenant name",
        'vrf_name': "PLease input your correct vrf name",
        'bds': BDs
        
    }
    #Output the inventory format for Jina template
    with open(output_file, 'w') as out_file:
      yaml.dump(inventory, out_file, default_flow_style=False,sort_keys=False)


def AAEP(filepath, output_file):
  with open(filepath, mode='r') as f:
    reader = json.load(f)
    AAEPs = []
    for item in reader['imdata'][0]['fvTenant']['children']:
      if 'fvAp' in item:
        for item in item['fvAp']['children']:
          if 'fvAEPg' in item:
            EPG_name = item['fvAEPg']['attributes']['name']
            EPG_des = item['fvAEPg']['attributes']['descr']
            EPG_alias = item['fvAEPg']['attributes']['nameAlias']
            for item in item['fvAEPg']['children']:
              # if 'fvRsPathAtt' in item:
              #     # Extract encap and tDn from fvRsPathAtt
              #     encap = item['fvRsPathAtt']['attributes'].get('encap', None)
              #     tDn = item['fvRsPathAtt']['attributes'].get('tDn', None)
                                
              #     # Append to Encap and Port lists
              #     Encap.append({'vlan': encap})
              #     Port.append({'Port': tDn})

                # mode = item['fvRsPathAtt']['attributes']['mode']
              # if 'fvRsDomAtt' in item:
              #   Phys_Dom= item['fvRsDomAtt']['attributes']['tDn']

              if 'fvRsBd' in item:
                BD_name = item['fvRsBd']['attributes']['tnFvBDName']

                AAEPs.append({
                  'name': EPG_name,
                  'description': EPG_des,
                  'alias': EPG_alias,
                  'mode': "regular",
                  # 'Physical_Dom': Phys_Dom,
                  'BD_name': BD_name,
                  'status': "created,modified"
                })
    # Prepare the inventory format for Jinja template
    inventory = {
        'ap_name': "PLease input your Application Profile",
        'epgs': AAEPs,
        }

    #Output the inventory format for Jina template
    with open(output_file, 'w') as out_file:
      yaml.dump(inventory, out_file, default_flow_style=False,sort_keys=False)
    


if __name__ == "__main__":
  filepath = "/home/dsu979/Downloads/tn-Migrate1.json"
  output = "/home/dsu979/Desktop/PROJECT/ACI_Migration/Ansible_ACI/AAEP_config/inventory.yaml"
  AAEP(filepath,output)


    