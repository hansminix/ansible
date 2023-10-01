import requests
from requests.auth import HTTPBasicAuth
from infoblox_client import objects


if __name__=="__main__":
    ibhost='192.168.178.105'
    ibuser='admin'
    ibpassword='infoblox'
    ibwapi_version='2.12'
    auth=HTTPBasicAuth(ibuser,ibpassword)
    nwfilter={"_object": "network","network": "10.0.0.0/24","network_view": "default"}
    url=f"https://{ibhost}/wapi/v{ibwapi_version}/fileop?_function=csv_export"
    r = requests.post(url, json=nwfilter, verify=False, auth=auth)
    print(r.status_code)
    print(r.json())
    headers = {"content-type":"application/force-download"}
    rget=requests.get(r.json()['url'],auth=auth,verify=False, allow_redirects=True,headers=headers)
    print(rget.status_code)
    open('networks.csv', 'wb').write(rget.content)
