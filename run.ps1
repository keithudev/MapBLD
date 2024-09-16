#Setup variables
$engine = "C:\Program Files\Epic Games\UE_5.4\Engine\Binaries\Win64\UnrealEditor-Cmd.exe"
$project = "C:\Users\keithu\Documents\Unreal Projects\demo\demo.uproject"
$script = "C:\Users\keithu\Documents\MapBLD\run.py"

#Start headless editor with specified script. Backtick ` used to preserve quotes in argument list.
Start-Process $engine -ArgumentList "`"$project`" -run=pythonscript -script=`"$script`""