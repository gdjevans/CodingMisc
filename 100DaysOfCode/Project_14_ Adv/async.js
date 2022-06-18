const fs = require('fs/promises');

async function readFile() {

    let fileData;
    // fs.readFile('data.txt', function(error, fileData) {
    //     console.log('File parsing done!');
    //     console.log(fileData.toString());
    //     // start another async task that sends the data to a database
    // });

try{
    fileData = await fs.readFile('data.txt');
} catch {
    console.log('File Reading Error');
}
    

    console.log('File parsing done!');
    console.log(fileData.toString());
    //return anotherASyncOperation();
    console.log('Hi There!');
}

readFile();