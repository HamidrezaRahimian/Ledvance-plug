import http.client, urllib.request, urllib.parse, urllib.error, base64
import json

headers = {
}

params = urllib.parse.urlencode({
})


try:
    conn = http.client.HTTPSConnection('api.update.ledvance.com')
    conn.request("GET", "/v1/zigbee/products?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
    json_data = json.loads(data.decode('utf-8'))
    print(json.dumps(json_data, indent=2))


except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))