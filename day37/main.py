import requests
import datetime
USERNAME="altaye21"
TOKEN="iouyeriterrhre53432f2"
urlw="https://pixe.la/v1/users"

user_params ={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=urlw, json=user_params)

# graph_ap=f"{urlw}/{USERNAME}/graphs"

# graph_config={
#     "id":"code",
#     "name":"Coding Graph",
#     "unit":"time",
#     "type":"float",
#     "color":"ajisai"
# }

# headers={
#     "X-USER-TOKEN":TOKEN
# }

# response_graph=requests.post(url=graph_ap, json=graph_config, headers=headers)
# print(response_graph.text)


add_issue=f"{urlw}/{USERNAME}/graphs/code"
today=datetime.datetime.now()
print(today)

task_param={
    "date":today.strftime('%Y%m%d'),
    "quantity":input("how many time you code today"),
}

header={
    "X-USER-TOKEN":TOKEN,
}

add_issue=requests.post(url=add_issue, json=task_param, headers=header)

print(add_issue.text)

update_issue=f"{add_issue}/{today.strftime('%Y%m%d')}"
task_updated={
    "quantity":"589.2",
}

updated=requests.put(url=update_issue, json=task_updated, headers=header)
print(updated.text)

delete_issue=f"{add_issue}/{today.strftime('%Y%m%d')}"

deleted=requests.delete(url=delete_issue, headers=header)
print(deleted.text)