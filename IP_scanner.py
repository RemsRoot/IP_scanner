# Script qui scan toutes  les interfaces réseaux

from socket import AF_INET, AF_INET6
from psutil import net_if_addrs, AF_LINK

stock_interface = []

def type_IPv6(adresse) :
  if adresse.startswith("fe80") :
    return "link-local"
  elif adresse.startswith("fd") :
    return "Unique locale"
  elif adresse.startswith("2") :
    return "Globale"
  else :
    return "Spéciale"


def lister_interface() :

  var_interface = []
  interfaces = net_if_addrs()

  for interface, adresses in interfaces.items() :
    print(f"Interface : {interface}")
    dico_interface = {}
    dico_interface["interface"] = interface 
    for adresse in adresses :
      if adresse.family == AF_INET :
        print(f"\tAdresse IPv4 : {adresse.address}")
        print(f"\tMasque IPv4  : {adresse.netmask}")
        dico_interface["ipv4"] = adresse.address
        dico_interface["masque-ipv4"] = adresse.netmask
      elif adresse.family == AF_INET6 :
        type = type_IPv6(adresse.address)
        print(f"\tAdresse IPv6 : {adresse.address.split('%')[0]}\t[{type}]")
        print(f"\tMasque IPv6  : {adresse.netmask}")
      if type == "Globale" :
        dico_interface["ipv6"] = adresse.address.split('%')[0]
        dico_interface["masque_ipv6"] = adresse.netmask
      elif adresse.family == AF_LINK :
        print(f"\tAdresse MAC  : {adresse.address}")
        dico_interface["MAC"] = adresse.address
      else :
        print(f"\terror : {adresse.address}")
    print()
    var_interface.append(dico_interface)
  return var_interface

if name == "main" :
  print("\n\n-- Script interface scanner --\n\n")
  stock_interface = lister_interface()
