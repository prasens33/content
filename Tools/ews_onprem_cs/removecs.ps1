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


# open remote PS session to Office 365 Security & Compliance Center
$url = "https://" + $server + "/PowerShell"
$session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri $url -Credential $UserCredential -Authentication Kerberos
if (!$session)
{
    "Failed to create remote PS session"
    return
}


Import-PSSession $session -CommandName *Compliance* -AllowClobber -DisableNameChecking -Verbose:$false | Out-Null

# Remove the search
Remove-ComplianceSearch $searchName -Confirm:$false

# Close the session
Remove-PSSession $session
