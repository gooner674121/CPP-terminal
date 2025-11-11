to use this terminal you need to follow the tutorial and open the bat file that istn in the folder follow the tutorial below

Step 1: Download MinGW

Go to the official MinGW-w64 site:
https://www.mingw-w64.org/downloads/

Choose the “SourceForge” link under “Windows” → you’ll be redirected to the download page.

Click Download Latest Version.

Step 2: Install MinGW

Run the installer (.exe) that you downloaded.

Choose installation settings:

Architecture: x86_64 (64-bit)

Threads: posix

Exception: seh

Build revision: leave default

Choose the installation directory (example):

C:\MinGW


⚠️ Avoid spaces in the path to prevent compilation issues.

Click Next → Install. Wait until installation finishes.

Step 3: Add MinGW to Windows PATH

To use gcc from any terminal or Python script, you need to add MinGW’s bin folder to your system PATH.

Press Windows + S → type Environment Variables → select Edit the system environment variables.

Click Environment Variables… at the bottom.

Under System variables, find Path → select it → click Edit.

Click New and add the path to the bin folder of MinGW. Example:

C:\MinGW\bin


Click OK on all windows to save.

Step 4: Verify GCC Installation

Open a new Command Prompt.

Type:

gcc --version


If installed correctly, you should see something like:

gcc (tdm64-1) 10.3.0
Copyright (C) 2020 Free Software Foundation, Inc.

Step 5: Compile Your First C Program

Open a text editor and write a simple C program:

#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    return 0;
}


Save it as hello.c.

Open Command Prompt in the same directory as hello.c.

Compile the program:

gcc hello.c -o hello.exe


Run the executable:

hello.exe


Output:

Hello, world!
