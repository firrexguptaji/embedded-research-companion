[Setup]
AppName=Embedded Research Companion
AppVersion=1.0
DefaultDirName={pf}\EmbeddedResearchCompanion
DefaultGroupName=Embedded Research Companion
OutputDir=.
OutputBaseFilename=EmbeddedResearchInstaller
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
DisableDirPage=no
PrivilegesRequired=admin

[Files]
Source: "*"; DestDir: "{app}"; Flags: recursesubdirs createallsubdirs; \
Excludes: "venv\*;.git\*;__pycache__\*;*.pyc;*.pyo;*.log"

[Icons]
Name: "{group}\Embedded Research Companion"; \
Filename: "powershell.exe"; \
Parameters: "-ExecutionPolicy Bypass -File ""{app}\run.ps1"""

[Run]
Filename: "powershell.exe"; \
Parameters: "-NoExit -ExecutionPolicy Bypass -File ""{app}\setup.ps1"""; \
Flags: postinstall
