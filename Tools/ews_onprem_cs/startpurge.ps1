[CmdletBinding()]
Param(
[Parameter(Mandatory=$True)]
[string]$username,

[Parameter(Mandatory=$True)]
[string]$password,

[Parameter(Mandatory=$True)]
[string]$searchName,

[Parameter(Mandatory=$True)]
[string]$server
)

$WarningPreference = "silentlyContinue"
# Create Credential object
$secpasswd = ConvertTo-SecureString $password -AsPlainText -Force
$UserCredential = New-Object System.Management.Automation.PSCredential ($username, $secpasswd)

# open remote PS session to Exchange 2016 on-prem server
$url = "https://" + $server + "/PowerShell"
$session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri $url -Credential $UserCredential -Authentication Kerberos
if (!$session)
{
    "Failed to create remote PS session"
    return
}


Import-PSSession $session -CommandName *Compliance* -AllowClobber -DisableNameChecking -Verbose:$false | Out-Null

# Delete mails based on an existing search criteria
$newActionResult = New-ComplianceSearchAction -SearchName $searchName -Purge -PurgeType SoftDelete -Confirm:$false
if (!$newActionResult)
{
    # Happens when there are no results from the search
    "No action was created"
}

# Close the session
Remove-PSSession $session
return
