[CmdletBinding()]
Param(
[Parameter(Mandatory=$True)]
[string]$username,

[Parameter(Mandatory=$True)]
[string]$password,

[Parameter(Mandatory=$True)]
[string]$query,

[Parameter(Mandatory=$True)]
[string]$server
)

$WarningPreference = "silentlyContinue"
# Create Credential object
$secpasswd = ConvertTo-SecureString $password -AsPlainText -Force
$UserCredential = New-Object System.Management.Automation.PSCredential ($username, $secpasswd)

# Generate a unique search name
$searchName = [guid]::NewGuid().ToString() -replace '[-]'
$searchName = "DemistoSearch" + $searchName

# open remote PS session to Exchange 2016 on-prem server
$url = "https://" + $server + "/PowerShell"
$session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri $url -Credential $UserCredential -Authentication Kerberos
if (!$session)
{
    "Failed to create remote PS session"
    return
}


Import-PSSession $session -CommandName *Compliance* -AllowClobber -DisableNameChecking -Verbose:$false | Out-Null

$compliance = New-ComplianceSearch -Name $searchName -ExchangeLocation All -ContentMatchQuery $query -Confirm:$false 

Start-ComplianceSearch -Identity $searchName


$complianceSearchName = "Action status: " + $searchName 

$complianceSearchName | ConvertTo-Json

# Close the session
Remove-PSSession $session
