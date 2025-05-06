# network-transfer

**Two Linode API endpoints are involved:**

[https://techdocs.akamai.com/linode-api/reference/get-tagged-objects](https://techdocs.akamai.com/linode-api/reference/get-tagged-objects)
[https://techdocs.akamai.com/linode-api/reference/get-linode-transfer](https://techdocs.akamai.com/linode-api/reference/get-linode-transfer)

**1. Obtain Instance IDs under a Tag:**

  * Invoke the `get_tagged_instance_ids` function to retrieve all instance IDs associated with the "ZX-TEST" tag.
  * Construct the API URL, initiate a request, and verify the response status code.
  * On successful request, parse the response data, extract each instance's ID, store them in a list, and return this list.

**2. Retrieve Instance Traffic and Calculate Total:**

  * Call the `get_total_used_gb` function with the list of instance IDs as an argument.
  * Iterate over each instance ID, construct the corresponding API URL, and send a request.
  * If the request succeeds, convert the traffic usage from bytes to GB, display the usage for the instance, and accumulate it into the total traffic.
  * If the request fails, output the corresponding error message.

**3. Main Function:**

  * Call `get_tagged_instance_ids` to obtain the list of instance IDs.
  * If the list is obtained successfully, invoke `get_total_used_gb` to get the total traffic usage and print it.

