let fs = require("fs");
const path = require("path");

var content = {}

function createInputData(amount, type)
{
    // create dictionary with length, A0 -> An, and type
    content[`Length`] = amount;
    for (i = 0; i < amount; i++)
    {
        content[`A${i}`] = i + 1;
    }
    content[`Type`] = type;

    // randomize A0 -> An
    for (i = 0; i < amount; i++)
    {
        let randomIndex = Math.floor(Math.random() * amount);
        let temp = content[`A${i}`];
        content[`A${i}`] = content[`A${randomIndex}`];
        content[`A${randomIndex}`] = temp;
    }
}

function createInputFile() {
    // Explicitly define the order of keys
    const orderedKeys = ["Length", ...Object.keys(content).filter(key => key.startsWith("A")), "Type"];
    const csvString = orderedKeys.join(",") + "\n" + orderedKeys.map(key => content[key]).join(",");

    const csvFilePath = path.join(__dirname + '../../', "inputData.csv");

    fs.writeFile(csvFilePath, csvString, (err) => {
        if (err) {
            console.error("Failed to write CSV file:", err);
        } else {
            console.log("CSV file created:", csvFilePath);
        }
    });
}

function readArrays(inFile)
{
    fs.readFile(inFile,processCSV);
}

function processCSV(err, data)
{
    if (err)
    {
        console.error("error reading file");
    }

    var csv = Buffer.toString()
}

// Example: Create input data
createInputData(10, "bubble");
console.log(content);

// Example: Create a text file
createInputFile();