import json
import os
import psycopg2

with open("infracost-output.json") as f:
    data = json.load(f)

total_cost = float(data["totalMonthlyCost"])
resources = data["projects"][0]["breakdown"]["resources"]

build_id = os.environ.get("BUILD_NUMBER", "manual-test")

conn = psycopg2.connect(
    host="172.31.1.215",
    dbname="cost_dashboard",
    user="jenkins_writer",
    password="123456",
    port=5432
)
cur = conn.cursor()

cur.execute(
    """
    INSERT INTO build_costs (build_id, service_name, total_monthly_cost, resource_breakdown)
    VALUES (%s, %s, %s, %s)
    """,
    (build_id, "sample-tf", total_cost, json.dumps(resources))
)

conn.commit()
cur.close()
conn.close()

print(f"Inserted cost record: ${total_cost}/month for build {build_id}")