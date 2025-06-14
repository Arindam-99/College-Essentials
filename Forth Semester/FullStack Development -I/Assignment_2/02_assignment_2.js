//2.	a) Write a Node.js program to take user input ,add two numbers, and display the result 

const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter the first number: ', (num1) => {
    rl.question('Enter the second number: ', (num2) => {
        const sum = parseFloat(num1) + parseFloat(num2);
        console.log(`The sum is: ${sum}`);
        rl.close();
    });
});

/* OUTPUT
Enter the first number: 10
Enter the second number: 20
The sum is: 30 
*/




// B. Read and display all environment variables
console.log("System Environment Variables:");
console.log(process.env);

// Access specific environment variables
console.log("\nSpecific Environment Variables:");
console.log("HOME:", process.env.HOME);  // For Unix-like systems
console.log("USER:", process.env.USER);  // For Unix-like systems
console.log("PATH:", process.env.PATH);  // Shows system path
console.log("OS:", process.env.OS);  // System's OS name
console.log("Platform:", process.platform); // Platform: 'win32' for Windows, 'darwin' for macOS, 'linux' for Linux

// You can also check for Windows-specific environment variables
if (process.platform === 'win32') {
  console.log("\nWindows Specific Environment Variables:");
  console.log("USERPROFILE:", process.env.USERPROFILE);  // Windows user profile path
  console.log("TEMP:", process.env.TEMP);  // Temporary directory in Windows
  console.log("ProgramData:", process.env.ProgramData);  // Common application data in Windows
}

/* OUTPUT 
program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules',
  PUBLIC: 'C:\\Users\\Public',
  SESSIONNAME: 'Console',
  SystemDrive: 'C:',
  SystemRoot: 'C:\\WINDOWS',
  TEMP: 'C:\\Users\\ARINDA~1\\AppData\\Local\\Temp',
  TMP: 'C:\\Users\\ARINDA~1\\AppData\\Local\\Temp',
  USERDOMAIN: 'DESKTOP-2FCGTFQ',
  USERDOMAIN_ROAMINGPROFILE: 'DESKTOP-2FCGTFQ',
  USERNAME: 'ARINDAM  DAS',
  USERPROFILE: 'C:\\Users\\ARINDAM  DAS',
  windir: 'C:\\WINDOWS',
  TERM_PROGRAM: 'vscode',
  TERM_PROGRAM_VERSION: '1.97.1',
  LANG: 'en_US.UTF-8',
  COLORTERM: 'truecolor',
  VSCODE_INJECTION: '1',
  VSCODE_NONCE: '3174d768-0f2a-4a92-aaf5-83920b9ac951',
  VSCODE_STABLE: '1'
}

 */