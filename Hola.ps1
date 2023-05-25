#America Fernanda Martinez Barron
#Matricula: 1901395

$tarea = New-ScheduledTaskAction -Execute "powershell \Documents\Practica15_1901395\send_sysinfo.ps1"
$trigger = New-ScheduledTasktrigger -Once -At 12:42pm

Register-ScheduledTask -Action $tarea -Trigger $trigger -TaskPath “MyHomework” -TaskName “Enviar sysinfo” -Description “Envio de informacion del sistema”