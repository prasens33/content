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


Import-PSSession $session -CommandName Get-ComplianceSearch -AllowClobber -DisableNameChecking -Verbose:$false | Out-Null



$searchStatus = Get-ComplianceSearch $searchName
#"Search status: " + $searchStatus.Status
$searchStatus.Status
if ($searchStatus.Status -eq "Completed")
{
    $searchStatus.SuccessResults | ConvertTo-Json
}

# Close the session
Remove-PSSession $session
