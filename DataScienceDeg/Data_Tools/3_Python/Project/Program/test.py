import json
import click
  
with open('generated.json', 'r') as f: 
    data_dict = json.load(f)
print(data_dict)

@click.option('--name', 'user_name', prompt='User name',help='Name to add.')
@click.option('--gender', 'gender', prompt='Gender',help='Gender to add.')
@click.option('--company', 'user_company', prompt='User company',help='Company to add.')
@click.option('--email', 'user_email', prompt='Email',help='Email to add.')
@click.option('--env',type=click.Choice(['dev', 'prod']),help='your environment')
def finalise(user_name, gender, user_company, user_email, env):
    if env == "prod":
        print("this is production")

if __name__ == '__main__':
    finalise()

with open('generated.txt', 'w') as json_file:
  json.dump(data_dict, json_file)