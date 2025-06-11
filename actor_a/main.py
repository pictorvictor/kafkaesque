from kafka import KafkaProducer
import time

for i in range(10):
    try:
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        break
    except Exception as e:
        print(f"Kafka not ready, retrying... ({i+1}/10)")
        time.sleep(3)
else:
    raise Exception("Could not connect to Kafka after 10 attempts")

with open("input.xml", "r") as file:
    xml_data = file.read()

try:
    future = producer.send("xml-topic", xml_data.encode('utf-8'))
    record_metadata = future.get(timeout=10)
    print(f"Actor A: XML sent to {record_metadata.topic} [partition {record_metadata.partition}] at offset {record_metadata.offset}")
except Exception as e:
    print(f"Actor A: Failed to send XML: {e}")
finally:
    producer.close()