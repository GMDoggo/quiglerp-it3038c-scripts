#Set IP variable (I have multiple interfaces so I use interface aliast to filter)
$IP = Get-NetIPAddress -InterfaceAlias "Ethernet" | Select-Object IPAddress
#Declare user variable and set to user
$User = $env:USERNAME
#Declare Hostname
$HostName = $env:COMPUTERNAME
#Declare Version
$Version = $HOST.Version.Major
#Declare Date (Will have to use a format to remove the time)
$CurrentDate = Get-Date -Format "dddd, MMMM dd, yyyy"

#Declaring what email to use and send to
Send-MailMessage -To "quiglerp@gmail.com" -From "murphy.quigs@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential) 

#Body built with variables from above
$BODY = "

This machine's IP is $IP
User is $User
Hostname is $HostName
Powershell Version $Version
Today's Date is $CurrentDate
"

