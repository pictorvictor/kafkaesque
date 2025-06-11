from kafka import KafkaConsumer, KafkaProducer
from lxml import etree
import os
from datetime import datetime
import time

for i in range(10):
    try:
        consumer = KafkaConsumer("xml-topic", bootstrap_servers='kafka:9092', auto_offset_reset='earliest')
        producer = KafkaProducer(bootstrap_servers='kafka:9092')        
        break
    except Exception as e:
        print(f"Kafka not ready, retrying... ({i+1}/10)")
        time.sleep(3)
else:
    raise Exception("Could not connect to Kafka after 10 attempts")

xslt_doc = etree.parse("transform.xslt")
transform = etree.XSLT(xslt_doc)

if consumer is None:
    raise Exception("Kafka consumer not initialized")

for message in consumer:
    xml_doc = etree.fromstring(message.value)
    result_tree = transform(xml_doc)
    transformed_xml = etree.tostring(result_tree, pretty_print=True)

    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{output_dir}/response_{timestamp}.xml"
    with open(output_file, "wb") as f:
        f.write(transformed_xml)
    print(f"Actor B: Transformed XML written to {output_file}")

    try:
        future = producer.send("response-topic", transformed_xml)
        record_metadata = future.get(timeout=10)
        print(f"Actor B: Kafka message sent to {record_metadata.topic} at offset {record_metadata.offset}")
    except Exception as e:
        print(f"Actor B: Kafka send failed: {e}")
    
    producer.close()
    break
