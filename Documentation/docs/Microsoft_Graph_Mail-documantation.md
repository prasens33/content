## Overview
---
Use the Microsoft Graph integration to connect to and interact with mail data on Microsoft Platforms. This integration was integrated and tested with Microsoft Graph v1.0.

## Microsoft Graph Mail Playbook
---

## Use cases
---

## Configure Microsoft Graph Mail on Demisto
---

1. Navigate to __Settings__ > __Integrations__ > __Servers & Services__.
2. Search for Microsoft Graph Mail.
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
1. msg-list-messages
2. msg-create-message
3. msg-get-message
4. msg-list-drafts
5. msg-del-message
6. msg-send-message
7. msg-move-message
8. msg-forward-message
9. msg-list-folders
10. msg-create-folder
11. msg-del-folder
12. msg-get-attachments
13. msg-del-attachment
14. msg-list-rules
15. msg-create-rule
16. msg-get-rule
17. msg-del-rule
18. msg-update-rule
### msg-list-messages
---
List messages of the user.
##### Base Command
`msg-list-messages`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | UserID of retrieved user, can be GUID or user's email address. | True |
| top | Number of top messages to retrieve. | False |
| filterQuery | Filter query rule. | False |
| timeFrom | Start receivedDate(inclusive) of message. | False |
| timeTo | End receivedDate(inclusive) of message. | False |
| folderId | FolderID of the folder to list messages, can be GUID or folder name. | False |
| searchString | Search for an email that contains the following String. e.g : searchString="Hello World" | False |
| fromAnEmailAddress | List messages from an email address. | False |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Message.Subject | string | Subject of message. |
| MsGraph.User.Mail.Message.Sender | string | Sender email of message. |
| MsGraph.User.Mail.Message.ReceivedDateTime | date | Received time of message. |
| MsGraph.User.Mail.Message.HasAttachments | boolean |  If the message has attachments. |
| MsGraph.User.Mail.Message.Importance | string | The importance of the message: Low, Normal, High. |
| MsGraph.User.Mail.Message.IsDraft | boolean | Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet. |
| MsGraph.User.Mail.Message.IsRead | boolean | Indicates whether the message has been read. |
| MsGraph.User.Mail.Message.ParentFolderId | string | The unique identifier for the message's parent mailFolder. |
| MsGraph.User.Mail.Message.Id | string | Unique identifier for the message (note that this value may change if a message is moved or altered) |
##### Command Example
```
!msg-list-messages userId=donaldt@demistodev.onmicrosoft.com searchString=test
```
##### Context Example
```json
{
    "MsGraph": {
        "User": {
            "Mail": {
                "Message": [
                    {
                        "HasAttachments": false,
                        "Id": "AAMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwBGAAAAAABtNAiM1FO7Q5wMnDvE_mt5BwB1Dw4l9S-ERr8zEwFketPtAAAAAAEMAAB1Dw4l9S-ERr8zEwFketPtAAChw6LCAAA=",
                        "Importance": "low",
                        "IsDraft": false,
                        "IsRead": false,
                        "ParentFolderId": "AQMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwAuAAADbTQIjNRTu0OcDJw7xPpreQEAdQ8OJfUvxEa-MxMBZHrT7QAAAgEMAAAA",
                        "ReceivedDateTime": "2018-12-03T21:13:59Z",
                        "Sender": "donaldt@demistodev.onmicrosoft.com(donald trump)",
                        "Subject": "FW: testsubject",
                        "UserId": "dev@demisto.works"
                    },
                    {
                        "HasAttachments": false,
                        "Id": "AAMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwBGAAAAAABtNAiM1FO7Q5wMnDvE_mt5BwB1Dw4l9S-ERr8zEwFketPtAAAAAAEJAAB1Dw4l9S-ERr8zEwFketPtAACfej7-AAA=",
                        "Importance": "low",
                        "IsDraft": false,
                        "IsRead": true,
                        "ParentFolderId": "AQMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwAuAAADbTQIjNRTu0OcDJw7xPpreQEAdQ8OJfUvxEa-MxMBZHrT7QAAAgEJAAAA",
                        "ReceivedDateTime": "2018-11-30T23:13:26Z",
                        "Sender": "dev@demisto.works(demisto dev)",
                        "Subject": "testsubject",
                        "UserId": "dev@demisto.works"
                    }
                ]
            }
        }
    }
}
```
##### Human Readable Output
![HRO - msg-list-messages](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-list-messages.png "msg-list-messages")

### msg-create-message
---
Create draft of a new message.
##### Base Command
`msg-create-message`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | User_ID of user sending message. | True |
| subject | Subject of new message. | True |
| body | Body of message. | True |
| recipientEmail | Email of recipient of message. | True |
| importance | Importance level of message. | False |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Message.UserId | string | The user ID assigned to the message. |
| MsGraph.User.Mail.Message.Id | string | The message ID that was supposed to be created. |
| MsGraph.User.Mail.Message.IsDraft | boolean | Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet. The value should be true. |
##### Command Example
```
!msg-create-message userId=dev@demisto.works body=testbody recipientEmail=donaldt@demistodev.onmicrosoft.com subject=testsubject importance=low
```
##### Context Example
```json
{
    "MsGraph": {
        "User": {
            "Mail": {
                "Message": {
                    "Id": "AAMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwBGAAAAAABtNAiM1FO7Q5wMnDvE_mt5BwB1Dw4l9S-ERr8zEwFketPtAAAAAAEPAAB1Dw4l9S-ERr8zEwFketPtAAChw4dbAAA=",
                    "IsDraft": true,
                    "UserId": "dev@demisto.works"
                }
            }
        }
    }
}
```
##### Human Readable Output

![HRO - msg-create-message](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-create-message.png "msg-create-message")

### msg-get-message
---
Retrieve detail information of a message.
##### Base Command
`msg-get-message`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | UserID of a user who can access this message. | True |
| messageId | MessageID of the message. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Message.Subject | string | Subject of message. |
| MsGraph.User.Mail.Message.Sender | string | Sender of message |
| MsGraph.User.Mail.Message.ReceivedDateTime | string | Received time of message. |
| MsGraph.User.Mail.Message.HasAttachments | boolean | If has attachment. |
| MsGraph.User.Mail.Message.Content | string | Content of message body. |
| MsGraph.User.Mail.Message.Recipients | string | Recipients of message. |
| MsGraph.User.Mail.Message.CcRecipients | string | CcRecpients of message. |
| MsGraph.User.Mail.Message.BccRecipients | string | BccRecpients of message. |
| MsGraph.User.Mail.Message.Importance | string | The importance of the message: Low, Normal, High. |
| MsGraph.User.Mail.Message.IsDraft | boolean | Indicates whether the message is a draft. A message is a draft if it hasn't been sent yet. |
| MsGraph.User.Mail.Message.IsRead | boolean | Indicates whether the message has been read. |
| MsGraph.User.Mail.Message.ParentFolderId | string | The unique identifier for the message's parent mailFolder. |
| MsGraph.User.Mail.Message.Id | string | Unique identifier for the message (note that this value may change if a message is moved or altered) |
##### Command Example
```
!msg-get-message messageId=AAMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAAAAACyUnP8WIW4TqRDvWY39bJNBwCJPYS7Jus9Q4GxlTpuoikwAAAAg00pAACJPYS7Jus9Q4GxlTpuoikwAAIHoKSlAAA= userId=donaldt@demistodev.onmicrosoft.com
```
##### Context Example
```json
{
    "MsGraph": {
        "User": {
            "Mail": {
                "Message": {
                    "BccRecipients": "",
                    "CcRecipients": "",
                    "Content": "Hello,\r\nThis is a test.\r\n\r\n-Zhao\r\n",
                    "HasAttachments": true,
                    "Id": "AAMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAAAAACyUnP8WIW4TqRDvWY39bJNBwCJPYS7Jus9Q4GxlTpuoikwAAAAg00pAACJPYS7Jus9Q4GxlTpuoikwAAIHoKSlAAA=",
                    "Importance": "normal",
                    "IsDraft": false,
                    "IsRead": true,
                    "ParentFolderId": "AQMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgAuAAADslJz-FiFuE6kQ71mN-WyTQEAiT2EuybrPUOBsZU6bqIpMAAAAYNNKQAAAA==",
                    "ReceivedDateTime": "2018-11-16T01:45:23Z",
                    "Recipients": "donaldt@demistodev.onmicrosoft.com(donald trump)",
                    "Sender": "test@outlook.com(Test)",
                    "Subject": "Test for attachment"
                }
            }
        }
    }
}
```
##### Human Readable Output

![HRO - msg-get-message](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-get-message.png "msg-get-message")

### msg-list-drafts
---
List drafts of message of a user.
##### Base Command
`msg-list-drafts`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | UserID of the user to show. | True |
| top | Number of top messages to retrieve. | False |
| filterQuery | Filter query rule. | False |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Message.Subject | string | Subject of draft. |
| MsGraph.User.Mail.Message.Recipients | string | Recipients of draft. |
| MsGraph.User.Mail.Message.ModifiedTime | date | Last modified time of draft. |
| MsGraph.User.Mail.Message.CcRecipients | string | The Cc: recipients for the message. |
| MsGraph.User.Mail.Message.BccRecipients | string | The Bcc: recipients for the message. |
| MsGraph.User.Mail.Message.HasAttachments | boolean | Indicates whether the message has attachments.  |
| MsGraph.User.Mail.Message.Importance | string | The importance of the message: Low, Normal, High. |
| MsGraph.User.Mail.Message.Content | string | The body of the message. |
| MsGraph.User.Mail.Message.Id | string | Unique identifier for the message (note that this value may change if a message is moved or altered) |
##### Command Example
```
!msg-list-drafts userId=dev@demisto.works
```
##### Context Example
```json
{
    "MsGraph": {
        "User": {
            "Mail": {
                "Message": {
                    "BccRecipients": "",
                    "CcRecipients": "",
                    "Content": "testbody\r\n",
                    "HasAttachments": false,
                    "Id": "AAMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwBGAAAAAABtNAiM1FO7Q5wMnDvE_mt5BwB1Dw4l9S-ERr8zEwFketPtAAAAAAEPAAB1Dw4l9S-ERr8zEwFketPtAAChw4dbAAA=",
                    "Importance": "low",
                    "ModifiedTime": "2018-12-03T19:04:38Z",
                    "Recipients": "donaldt@demistodev.onmicrosoft.com(donald trump)",
                    "Subject": "testsubject"
                }
            }
        }
    }
}
```
##### Human Readable Output

![HRO - msg-list-drafts](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-list-drafts.png "msg-list-drafts")

### msg-del-message
---
Delete a message.
##### Base Command
`msg-del-message`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | User ID of the user who has this message. | True |
| messageId | Message ID of the message to delete. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Message.Action | string | The value will be 'deleted'. |
| MsGraph.User.Mail.Message.Id | string | The message ID that was supposed to be deleted. |
##### Command Example
```
!msg-del-message userId=dev@demisto.works messageId=AAMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwBGAAAAAABtNAiM1FO7Q5wMnDvE_mt5BwB1Dw4l9S-ERr8zEwFketPtAAAAAAEPAAB1Dw4l9S-ERr8zEwFketPtAACfeieBAAA=
```
##### Context Example
```json
{
    "MsGraph": {
        "User": {
            "Mail": {
                "Message": {
                    "Action": "deleted",
                    "Id": "AAMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwBGAAAAAABtNAiM1FO7Q5wMnDvE_mt5BwB1Dw4l9S-ERr8zEwFketPtAAAAAAEPAAB1Dw4l9S-ERr8zEwFketPtAAChw4dbAAA="
                }
            }
        }
    }
}
```
##### Human Readable Output

![HRO - msg-del-message](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-del-message.png "msg-del-message")

### msg-send-message
---
Send a message in the draft folder. 
##### Base Command
`msg-send-message`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | User_ ID of user sending the draft. | True |
| messageId | Message_ID of the draft. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Message.Action | string | The action of message, should be 'sent'. |
| MsGraph.User.Mail.Message.Id | string | The message ID that was supposed to be deleted. |
##### Command Example
```
!msg-send-message userId=dev@demisto.works messageId=AAMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwBGAAAAAABtNAiM1FO7Q5wMnDvE_mt5BwB1Dw4l9S-ERr8zEwFketPtAAAAAAEPAAB1Dw4l9S-ERr8zEwFketPtAACfeieAAAA=
```
##### Context Example
```json
{
    "MsGraph": {
        "User": {
            "Mail": {
                "Message": {
                    "Action": "sent",
                    "Id": "AAMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwBGAAAAAABtNAiM1FO7Q5wMnDvE_mt5BwB1Dw4l9S-ERr8zEwFketPtAAAAAAEPAAB1Dw4l9S-ERr8zEwFketPtAACfeieAAAA="
                }
            }
        }
    }
}
```
##### Human Readable Output

![HRO - msg-send-message](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-send-message.png "msg-send-message")

### msg-move-message
---
Move a message to another folder.
##### Base Command
`msg-move-message`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | The user identifier, can be User ID or User Email Address. | True |
| messageId | The Message ID, GUID. | True |
| folderName | The destination folder ID, or a well-known folder name, such as junkemail, inbox. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Message.UserId | string | The user identifier of the user who has the moved message. |
| MsGraph.User.Mail.Message.Id | string | The Message ID of message to be moved. |
| MsGraph.User.Mail.Message.ParentFolderId | string | The Folder Id of message. |
##### Command Example
```
!msg-move-message folderName=junkemail
 messageId=AQMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAADslJz-FiFuE6kQ71mN-WyTQcAiT2EuybrPUOBsZU6bqIpMAAAAgEMAAAAiT2EuybrPUOBsZU6bqIpMAACEFEWJgAAAA== userId=donaldt@demistodev.onmicrosoft.com
```
##### Context Example
```json
{
    "MsGraph": {
        "User": {
            "Mail": {
                "Message": {
                    "Id": "AQMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAADslJz-FiFuE6kQ71mN-WyTQcAiT2EuybrPUOBsZU6bqIpMAAAAgEMAAAAiT2EuybrPUOBsZU6bqIpMAACEFEWJgAAAA==",
                    "ParentFolderId": "junkemail",
                    "UserId": "donaldt@demistodev.onmicrosoft.com"
                }
            }
        }
    }
}
```
##### Human Readable Output

![HRO - msg-move-message](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-move-message.png "msg-move-message")

### msg-forward-message
---
Forward a message.
##### Base Command
`msg-forward-message`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | The user identifier, can be User ID or User Email Address. | True |
| messageId | The Message ID, GUID. | True |
| recipientEmail | Email of recipient of the forwared message. | True |
| comment | A comment to include. | False |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Message.UserId | string | The user identifier of the user who has forwared message. |
| MsGraph.User.Mail.Message.Id | string | The Message ID of the forwarded message. |
| MsGraph.User.Mail.Message.ForwardedTo | string | The Email of forwarded message receiver. |
##### Command Example

```
!msg-forward-message  messageId=AAMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAAAAACyUnP8WIW4TqRDvWY39bJNBwCJPYS7Jus9Q4GxlTpuoikwAAAAg00pAACJPYS7Jus9Q4GxlTpuoikwAAISZzgmAAA=
 recipientEmail=dev@demisto.works userId=donaldt@demistodev.onmicrosoft.com comment=testForForwarding
```

##### Context Example
```json
{
    "MsGraph": {
        "User": {
            "Mail": {
                "Message": {
                    "ForwardedTo": "dev@demisto.works",
                    "Id": "AAMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAAAAACyUnP8WIW4TqRDvWY39bJNBwCJPYS7Jus9Q4GxlTpuoikwAAAAg00pAACJPYS7Jus9Q4GxlTpuoikwAAISZzgmAAA=",
                    "UserId": "donaldt@demistodev.onmicrosoft.com"
                }
            }
        }
    }
}
```
##### Human Readable Output

![HRO - msg-forward-message](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-forward-message.png "msg-forward-message")

### msg-list-folders
---
Get folders information for a mailbox. Only folders with read permissions will be return as a result. Notice that your visual folders on the mailbox (like Inbox, etc) is under the folder "Top of Information Store".
##### Base Command
`msg-list-folders`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | User_ID of user to get folders. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Folder.Name | string | Folder name. |
| MsGraph.User.Mail.Folder.UnreadCount | number | Number of unread messages in folder. |
| MsGraph.User.Mail.Folder.TotalCount | number | Number of total messages in folder. |
| MsGraph.User.Mail.Folder.Id | string | ID of folder |
| MsGraph.User.Mail.Folder.UserId | string | The User ID of user who has the deleted folder. |
##### Command Example
```
!msg-list-folders userId=dev@demisto.works 
```
##### Context Example
```json
{
    "MsGraph": {
        "User": {
            "Mail": {
                "Folder": [
                    {
                        "Id": "AQMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwAuAAADbTQIjNRTu0OcDJw7xPpreQEAdQ8OJfUvxEa-MxMBZHrT7QAAAgEMAAAA",
                        "Name": "Inbox",
                        "TotalCount": 4,
                        "UnreadCount": 4,
                        "UserId": "dev@demisto.works"
                    },
                    {
                        "Id": "AQMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwAuAAADbTQIjNRTu0OcDJw7xPpreQEAdQ8OJfUvxEa-MxMBZHrT7QAAAgEJAAAA",
                        "Name": "Sent Items",
                        "TotalCount": 2,
                        "UnreadCount": 0,
                        "UserId": "dev@demisto.works"
                    }
                ]
            }
        }
    }
}
```
##### Human Readable Output

![HRO - msg-list-folders](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-list-folders.png "msg-list-folders")

### msg-create-folder
---
Create a new mail folder in the root folder of the user's mailbox.
##### Base Command
`msg-create-folder`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | The user identifier, can be User ID or User Email Address. | True |
| folderName | The created Folder Name. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Folder.FolderName | string | The Folder Name of created folder. |
| MsGraph.User.Mail.Folder.Id | string | The Folder ID of created folder. |
| MsGraph.User.Mail.Folder.UserId | string | The User ID of user who has the deleted folder. |
##### Command Example
```
!msg-create-folder userId=dev@demisto.works folderName=test
```
##### Context Example
```json
{
    "MsGraph": {
        "User": {
            "Mail": {
                "Folder": {
                    "Id": "AAMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwAuAAAAAABtNAiM1FO7Q5wMnDvE_mt5AQB1Dw4l9S-ERr8zEwFketPtAAChw5rqAAA=",
                    "Name": "test",
                    "UserId": "dev@demisto.works"
                }
            }
        }
    }
}
```
##### Human Readable Output

![HRO - msg-create-folder](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-create-folder.png "msg-create-folder")

### msg-del-folder
---
Delete a folder.
##### Base Command
`msg-del-folder`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | User ID of user who has this folder. | True |
| folderId | The Folder ID of folder to be deleted. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Folder.Action | string | The value will be 'deleted'. |
| MsGraph.User.Mail.Folder.Id | string | The Folder ID of deleted folder. |
| MsGraph.User.Mail.Folder.UserId | string | The User ID of user who has the deleted folder. |
##### Command Example
```
!msg-del-folder folderId=AAMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwAuAAAAAABtNAiM1FO7Q5wMnDvE_mt5AQB1Dw4l9S-ERr8zEwFketPtAAChw5rrAAA= userId=dev@demisto.works
```
##### Context Example
```json
{
    "MsGraph": {
        "User": {
            "Mail": {
                "Folder": {
                    "Action": "deleted",
                    "Id": "AAMkADY0ZjMxZmMyLWU3MjgtNDNiOS04ZDZmLTYxZDVkYzk1MTg5MwAuAAAAAABtNAiM1FO7Q5wMnDvE_mt5AQB1Dw4l9S-ERr8zEwFketPtAAChw5rrAAA=",
                    "UserId": "dev@demisto.works"
                }
            }
        }
    }
}
```
##### Human Readable Output

![HRO - msg-delete-folder](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-del-folder.png "msg-del-folder")

### msg-get-attachments
---
Get attachements of a message. If you don't provide attachment id, all the attachments will be listed here.
##### Base Command
`msg-get-attachments`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | The user identifier of user who has the attachment(s), can be User ID or User Email Address. | True |
| messageId | The Message ID of message which has the attachment(s). | True |
| attachmentIds | The Attachments' IDs to get. If none - all attachments will be retrieve from the message. Support multiple attachments with comma-separated value or array. | False |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Attachment.UserId | string | The User ID of the user who has the attachment. |
| MsGraph.User.Mail.Attachment.MessageId | string | The Message ID of the message which has the attachment. |
| MsGraph.User.Mail.Attachment.AttachmentId | string | The attachment id. |
| MsGraph.User.Mail.Attachment.Name | string | The name of attachment. |
| MsGraph.User.Mail.Attachment.Size | number | The size in bytes of the attachment. |
| MsGraph.User.Mail.Attachment.LastModifiedTime | date | The date and time when the attachment was last modified.. |
| MsGraph.User.Mail.Attachment.Path | string | The path of file on Demisto platform, the file's EntryID. |
| MsGraph.User.Mail.Attachment.Type | string | The file type of attachment. |
##### Command Example
```
!msg-get-attachments userId=donaldt@demistodev.onmicrosoft.com messageId=AAMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAAAAACyUnP8WIW4TqRDvWY39bJNBwCJPYS7Jus9Q4GxlTpuoikwAAAAg00pAACJPYS7Jus9Q4GxlTpuoikwAAIHoKSlAAA=
```
##### Context Example
```json
{
    "File": {
        "EntryID": "1604@481d38bb-51f4-45c1-8978-24a823048bde",
        "Extension": "txt",
        "Info": "txt",
        "MD5": "3f9ea81c5a03d088590866580e121c95",
        "Name": "entry_artifact_6@19033.txt",
        "SHA1": "ebd256f9adcebd88a14678f0757797059d9d9f6a",
        "SHA256": "bae5ca38c7a6166a882c3ecbdc7211c84cf10ed11cf42c3e0a3b1a214055a6a9",
        "SSDeep": "48:YTA7+1ngrgfhESrG2jwJaWy29jtNII6TB8CgaV78/jv1yta2Scx9+a+N++SYo2j+:VCdhJCJaWBHII6TGbAYkJxbYxcXB",
        "Size": 2606,
        "Type": "ASCII text, with very long lines, with no line terminators\n"
    },
    "MsGraph": {
        "User": {
            "Mail": {
                "Attachment": {
                    "AttachmentId": "AAMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAAAAACyUnP8WIW4TqRDvWY39bJNBwCJPYS7Jus9Q4GxlTpuoikwAAAAg00pAACJPYS7Jus9Q4GxlTpuoikwAAISZzgoAAABEgAQAPyOBrOEIC9JkJZSemTOo5w=",
                    "Type": "text/plain",
                    "LastModifiedTime": "2018-12-04T21:02:13Z",
                    "MessageId": "AAMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAAAAACyUnP8WIW4TqRDvWY39bJNBwCJPYS7Jus9Q4GxlTpuoikwAAAAg00pAACJPYS7Jus9Q4GxlTpuoikwAAISZzgoAAA=",
                    "Name": "entry_artifact_6@19033.txt",
                    "Path": "701a4270-df3e-48cf-b2a5-131f1cafdf69",
                    "Size": 2959,
                    "UserId": "donaldt@demistodev.onmicrosoft.com"
                }
            }
        }
    }
}
```
##### Human Readable Output

![HRO - msg-get-attachments](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-get-attachments.png "msg-get-attachments")

### msg-del-attachment
---
Delete an attachment on a message.
##### Base Command
`msg-del-attachment`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | The user identifier of the user who has the attachment, can be User ID or User Email Address. | True |
| messageId | The Message ID of the message which has the attachment. | True |
| attachmentId | The Attachment ID of the attachment to be deleted. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Attachment.UserId | string | The User ID of the user who has the attachment. |
| MsGraph.User.Mail.Attachment.MessageId | string | The Message ID of the message which has the attachment. |
| MsGraph.User.Mail.Attachment.AttachmentId | string | The attachment id. |
| MsGraph.User.Mail.Attachment.Action | string | The action of attachment, should be 'deleted'. |
##### Command Example
```
!msg-del-attachment attachmentId=AAMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAAAAACyUnP8WIW4TqRDvWY39bJNBwCJPYS7Jus9Q4GxlTpuoikwAAAAg00pAACJPYS7Jus9Q4GxlTpuoikwAAIHoKSlAAABEgAQACuQWcv_71VCoyFgWPPWN5c= messageId=AAMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAAAAACyUnP8WIW4TqRDvWY39bJNBwCJPYS7Jus9Q4GxlTpuoikwAAAAg00pAACJPYS7Jus9Q4GxlTpuoikwAAIHoKSlAAA= userId=donaldt@demistodev.onmicrosoft.com
```
##### Context Example
```json
{
    "MsGraph": {
        "User": {
            "Mail": {
                "Attachment": {
                    "Action": "deleted",
                    "AttachmentId": "AAMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAAAAACyUnP8WIW4TqRDvWY39bJNBwCJPYS7Jus9Q4GxlTpuoikwAAAAg00pAACJPYS7Jus9Q4GxlTpuoikwAAIHoKSlAAABEgAQACuQWcv_71VCoyFgWPPWN5c=",
                    "MessageId": "AAMkAGJkZWM4NTA0LTZmNGYtNGJkYi05NzhjLWE0MTZkYTYxOWJjNgBGAAAAAACyUnP8WIW4TqRDvWY39bJNBwCJPYS7Jus9Q4GxlTpuoikwAAAAg00pAACJPYS7Jus9Q4GxlTpuoikwAAIHoKSlAAA=",
                    "UserId": "donaldt@demistodev.onmicrosoft.com"
                }
            }
        }
    }
}
```
##### Human Readable Output

![HRO - msg-del-attachment](https://raw.githubusercontent.com/Pekdz/content/joe_doc/Documentation/docs/hrd/msg-del-attachment.png "msg-del-attachment")

### msg-list-rules
---
List all mail rules for a specific user inbox.
##### Base Command
`msg-list-rules`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | UserID of retrieved user, can be GUID or user's email address. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Rule.Name | string | The display name of the rule. |
| MsGraph.User.Mail.Rule.Id | string | The Rule ID. |
| MsGraph.User.Mail.Rule.Enabled | boolean | Indicates whether the rule is enabled to be applied to messages, default is true. |
##### Command Example

```
!msg-list-rules userId=dev@demisto.works
```

##### Context Example

```json
//TODO: permission error, can't test
```

##### Human Readable Output

### msg-create-rule
---
Create a mail rule for user inbox by specifying a set of conditions and actions.
##### Base Command
`msg-create-rule`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | The user identifier of the user who has the new rule, can be User ID or User Email Address. | True |
| ruleName | The display name of the rule. | True |
| enabled | Indicates whether the rule is enabled to be applied to messages, default is true. | False |
| filterContainsString | Condition - Represents the strings that should appear in the body or subject of an incoming message. | False |
| filterFromEmail | Condition - Represents the specific sender email addresses of an incoming message in order for the condition or exception to apply. | False |
| filterHasAttachment | Condition - Indicates whether an incoming message must have attachment. | False |
| filterImportance | Condition - The importance that is stamped on an incoming message in order for the condition or exception to apply: low, normal, high. | False |
| toDelete | Action - Indicates whether a message should be moved to the Deleted Items folder. | False |
| toForwardTo | Action - The email addresses of the recipients to which a message should be forwarded. | False |
| toMarkAsRead | Action - Indicates whether a message should be marked as read. | False |
| toMarkImportance | Action - Sets the importance of the message, which can be: low, normal, high. | False |
| toMoveToFolder | Action - The ID of the folder that a message will be moved to, which can be folder id or folder name. | False |
| toCopyToFolder | Action - The ID of a folder that a message is to be copied to, which can be folder id or folder name. | False |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.Rule.Name | string | The display name of the rule. |
| MsGraph.Rule.Id | string | The Rule ID. |
| MsGraph.Rule.Enabled | boolean | Indicates whether the rule is enabled to be applied to messages, default is true. |
##### Command Example

```
!msg-create-rule userId=dev@demisto.works ruleName=test filterContainsString=keyword toMoveToFolder=junkemail
```

##### Context Example

```json
//TODO: permission error, can't test
```

##### Human Readable Output

### msg-get-rule
---
Get detail information of a mail rule for a specific user inbox.
##### Base Command
`msg-get-rule`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | UserID of retrieved user, can be GUID or user's email address. | True |
| ruleId | The Rule ID, can be get by msg-list-rules. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Rule.Name | string | The display name of the rule. |
| MsGraph.User.Mail.Rule.Id | string | The Rule ID. |
| MsGraph.User.Mail.Rule.Enabled | boolean | Indicates whether the rule is enabled to be applied to messages, default is true. |
##### Command Example
```
!msg-get-rule userId=dev@demisto.works ruleId=xxxx
```
##### Context Example
##### Human Readable Output

### msg-del-rule
---
Delete a mail rule for user inbox.
##### Base Command
`msg-del-rule`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | UserID of retrieved user, can be GUID or user's email address. | True |
| ruleId | The Rule ID, can be get by msg-list-rules. | True |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Rule.Id | string | The Rule ID. |
| MsGraph.User.Mail.Rule.Action | string | Action on the rule, should be 'deleted'. |
##### Command Example
```
!msg-del-rule userId=dev@demisto.works ruleId=xxx
```
##### Context Example

```json
//TODO: permission error, can't test
```

##### Human Readable Output

### msg-update-rule
---
Update a mail rule for user inbox by specifying a set of conditions and actions.
##### Base Command
`msg-update-rule`
##### Input
| **Argument Name** | **Description** | **Required** |
| --- | --- | --- |
| userId | The user identifier of the user who has the new rule, can be User ID or User Email Address. | True |
| ruleId | The Rule ID, can be get by msg-list-rules. | True |
| ruleName | The display name of the rule. | False |
| enabled | Indicates whether the rule is enabled to be applied to messages, default is true. | False |
| filterContainsString | Condition - Represents the strings that should appear in the body or subject of an incoming message. | False |
| filterFromEmail | Condition - Represents the specific sender email addresses of an incoming message in order for the condition or exception to apply. | False |
| filterHasAttachment | Condition - Indicates whether an incoming message must have attachment. | False |
| filterImportance | Condition - The importance that is stamped on an incoming message in order for the condition or exception to apply: low, normal, high. | False |
| toDelete | Action - Indicates whether a message should be moved to the Deleted Items folder. | False |
| toForwardTo | Action - The email addresses of the recipients to which a message should be forwarded. | False |
| toMarkAsRead | Action - Indicates whether a message should be marked as read. | False |
| toMarkImportance | Action - Sets the importance of the message, which can be: low, normal, high. | False |
| toMoveToFolder | Action - The ID of the folder that a message will be moved to, which can be folder id or folder name. | False |
| toCopyToFolder | Action - The ID of a folder that a message is to be copied to, which can be folder id or folder name. | False |
##### Context Output
| **Path** | **Type** | **Description** |
| --- | --- | --- |
| MsGraph.User.Mail.Rule.Name | string | The display name of the rule. |
| MsGraph.User.Mail.Rule.Id | string | The Rule ID. |
| MsGraph.User.Mail.Rule.Enabled | boolean | Indicates whether the rule is enabled to be applied to messages, default is true. |
##### Command Example
```
!msg-update-rule userId=dev@demisto.works ruleId=xxxx enabled=false
```
##### Context Example

```json
//TODO: permission error, can't test
```

##### Human Readable Output
