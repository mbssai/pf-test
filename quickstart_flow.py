from prefect import flow, task
import requests

@task(name="Calculate")
def my_task(num):
	num = num + 2
	print(num)

@task(name="API Get")
def call_api(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()

@task(name="API Parse")
def parse_fact(response):
    fact = response["fact"]
    print(fact)
    return fact

@flow(name="Example Flow")
def my_flow():
    my_task(2)
    my_task(4)
    fact_json = call_api("https://catfact.ninja/fact")
    fact_text = parse_fact(fact_json)
    return fact_text

if __name__ == "__main__":
    my_flow()
    

