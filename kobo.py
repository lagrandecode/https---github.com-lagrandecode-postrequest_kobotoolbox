import io
import requests
import uuid
from datetime import datetime

BASE_URL = 'https://kc.kobotoolbox.org'
SUMISSION_URL = f'{BASE_URL}/api/v1/submissions'
TOKEN = '6fb29d8015dc136cba3558590282ddab7f2b24a5'

def format_openrosa_datetime():
    return datetime.now().isoformat('T', 'milliseconds')

def create_xml_submission(data, _uuid):
    return f'''
    <aK9ANfTMCGAQHNiunmQyki id="aK9ANfTMCGAQHNiunmQyki" version="1 (2023-09-02 18:06:48)">
        <formhub>
            <uuid>43e93d84ef2341a89b562d41db6bd829</uuid>
        </formhub>
        <start>{format_openrosa_datetime()}</start>
        <end>{format_openrosa_datetime()}</end>
        <name>{data}</name>
        <__version__>vKMXGsXb7sEw42x2hnDqcf</__version__>
        <meta>
            <instanceID>uuid:{_uuid}</instanceID>
        </meta>
    </aK9ANfTMCGAQHNiunmQyki>
    '''.encode()

def submit_data(data):
    _uuid = str(uuid.uuid4())
    file_tuple = (_uuid, io.BytesIO(create_xml_submission(data, _uuid)))
    files = {'xml_submission_file': file_tuple}
    headers = {'Authorization': f'Token {TOKEN}'}
    res = requests.Request(
        method='POST', url=SUMISSION_URL, files=files, headers=headers
    )
    session = requests.Session()
    res = session.send(res.prepare())

    if res.status_code == 201:
        return 'Success 🎉'
    return 'Something went wrong 😢'

if __name__ == '__main__':
    res = submit_data('working')
    print(res)



# def submit_data(data, file_name):
#     ...
#     another_file_tuple = (file_name, open(file_name, 'rb'))
#     files = {'xml_submission_file': file_tuple, file_name: another_file_tuple}