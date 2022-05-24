import json
import click
  
# Data to be written
dictionary ={
    "name" : "booomake",
    "rollno" : 72,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}
  
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)

@click.option('--env',type=click.Choice(['dev', 'prod']),help='your environment')
def hello(env):
    if env == "prod":
        print("this is production")

if __name__ == '__main__':
    hello()