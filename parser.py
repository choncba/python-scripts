INPUT_FILE = "telegraf_2.conf"
OUTPUT_FILE = "parsed_" + INPUT_FILE 
START_TAG = "[[outputs.influxdb]]"
END_TAG = "\n\n"

with open(INPUT_FILE) as fd:
    input_text = fd.read()
    fd.close()

output_text =""

while START_TAG in input_text:
    start_index = input_text.find(START_TAG)
    end_index = input_text.find(END_TAG, start_index)
    output_text = output_text + input_text[start_index:end_index] + "\n\n"
    input_text = input_text[end_index:]

with open(OUTPUT_FILE,"w") as output_file:
    output_file.write(output_text)

print(output_text)