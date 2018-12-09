## Overview
---
Use the Microsoft Graph integration to connect to and interact with user objects on Microsoft Platforms. This integration was integrated and tested with Microsoft Graph v1.0.

## Microsoft Graph User Playbook
---
## Use cases
---

## Configure Microsoft Graph User on Demisto
---

1. Navigate to __Settings__ > __Integrations__ > __Servers & Services__.
2. Search for Microsoft Graph User.
3. Click __Add instance__ to create and configure a new integration instance.
You should configure the following settings:
  * __Name__: a textual name for the integration instance.
  * __Host URL (e.g. https://graph.microsoft.com)__
  * __The tenant ID as received from the admin consent - see detailed instructions (?)__
  * __The token received from Demisto support to allow access to generate MS tokens__
  * __Trust any certificate (unsecure)__
  * __Use system proxy settings__
4. Click __Test__ to validate the URLs, token, and connection.

## Commands
---
You can execute these commands from the Demisto CLI, as part of an automation, or in a playbook.
After you successfully execute a command, a DBot message appears in the War Room with the command details.
1. msg-get-users
2. msg-get-user
3. msg-create-user
4. msg-delete-user
5. msg-update-user
### msg-get-users
---
Retrieve all users.
##### Base Command
`msg-get-users`
##### Input
N/A
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Email | string | User email address |
| MsGraph.User.Id | string | User ID |
| MsGraph.User.Title | string | User job title |
| MsGraph.User.Name | string | User name |
| MsGraph.User.MailIsEnabled | boolean | Indicate whether mail service of the account is enabled or disabled. |
##### Command Example

```
!msg-get-users
```

##### Context Example

```json
{
    "MsGraph": {
        "User": [
            {
                "Email": "dev@demisto.works",
                "Id": "2827c1e7-edb6-4529-b50d-25984e968637",
                "MailIsEnabled": true,
                "Name": "demisto dev",
                "Title": null
            },
            {
                "Email": "serviceaccount1@demistodev.onmicrosoft.com",
                "Id": "70585180-517a-43ea-9403-2d80b97ab19d",
                "MailIsEnabled": false,
                "Name": "ServiceAccount1",
                "Title": null
            }
        ]
    }
}
```

##### Human Readable Output

![HRO - msg-get-users](/Users/pekdz/Workspace/demisto/integration/documentation/msg-get-users.png "msg-get-users")

### msg-get-user
---
Retrieve detailed information of a user.
##### Base Command
`msg-get-user`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | The User Id or User Email of the existing user to retrieve. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Email | string | User email address |
| MsGraph.User.Id | string | User ID |
| MsGraph.User.Title | string | User job title |
| MsGraph.User.Name | string | User name |
| MsGraph.User.MailIsEnabled | boolean | Indicate whether mail service of the account is enabled or disabled |
##### Command Example

```
!msg-get-user userId=dev@demisto.works
```

##### Context Example

```json
{
    "MsGraph": {
        "User": {
            "Department": null,
            "Email": "dev@demisto.works",
            "Id": "2827c1e7-edb6-4529-b50d-25984e968637",
            "MailIsEnabled": true,
            "Name": "demisto dev",
            "Phone": null,
            "Title": null
        }
    }
}
```

##### Human Readable Output

![HRO - msg-get-user](/Users/pekdz/Workspace/demisto/integration/documentation/msg-get-user.png "msg-get-user")

### msg-create-user
---
Create a new user.
##### Base Command
`msg-create-user`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| displayName | The name to display in the address book for the user. | True |
| userPrincipalName | The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant’s collection of verified domains. | True |
| mailNickname | The mail alias for the user. | True |
| password | The password for the user. | True |
| onPremisesImmutableId | Only needs to be specified when creating a new user account if you are using a federated domain for the user's userPrincipalName (UPN) property. | False |
| accountEnabled | Indicate whether the account is enabled or disabled, the default value is true. | False |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Email | string | User email address |
| MsGraph.User.Id | string | User ID |
| MsGraph.User.MailIsEnabled | boolean | Indicate whether mail service of the account is enabled or disabled |
##### Command Example

```
!msg-create-user displayName="Test Name" mailNickname=testnick password=Demisto@test userPrincipalName=testmail@demisto.works
```

##### Context Example

```json
{
    "MsGraph": {
        "User": {
            "Email": "testmail@demisto.works",
            "Id": "c6aa6944-c94b-4611-b34c-ab97f5555001",
            "MailIsEnabled": false
        }
    }
}
```

##### Human Readable Output

![HRO - msg-create-user](/Users/pekdz/Workspace/demisto/integration/documentation/msg-create-user.png "msg-create-user")

### msg-delete-user
---
Delete an existing user.
##### Base Command
`msg-delete-user`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | The User Id or User Email of the existing user to delete. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Id | string | User ID |
| MsGraph.User.Action | string | Action on the user, should be 'deleted' |
##### Command Example

```
!msg-delete-user userId=testmail@demisto.works
```

##### Context Example

```json
{
    "MsGraph": {
        "User": {
            "Action": "deleted",
            "Id": "testmail@demisto.works"
        }
    }
}
```

##### Human Readable Output

![HRO - msg-delete-user](/Users/pekdz/Workspace/demisto/integration/documentation/msg-delete-user.png "msg-delete-user")

### msg-update-user
---
Update an existing user.
##### Base Command
`msg-update-user`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | The User Id or User Email of the existing user to update. | True |
| displayName | The name to display in the address book for the user. | False |
| userPrincipalName | The user principal name (UPN) of the user. The UPN is an Internet-style login name for the user based on the Internet standard RFC 822. By convention, this should map to the user's email name. The general format is alias@domain, where domain must be present in the tenant’s collection of verified domains. | False |
| mailNickname | The mail alias for the user. | False |
| password | The password for the user. | False |
| jobTitle | The user’s job title. | False |
| department | The name for the department in which the user works. | False |
| city | The city in which the user is located. | False |
| accountEnabled | Indicate whether the account is enabled or disabled. | False |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Email | string | User email address |
| MsGraph.User.Id | string | User ID |
| MsGraph.User.MailIsEnabled | boolean | Indicate whether mail service of the account is enabled or disabled |
##### Command Example

```
!msg-update-user userId=testmail@demisto.works password=Test@pwd department=QA
```

##### Context Example

```json
//TODO: permission error, can't test
```

##### Human Readable Output

```json
//TODO: permission error, can't test
```