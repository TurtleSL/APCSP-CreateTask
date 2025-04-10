var root = null
var width = null

var progressBar = null
var progressBarInterval = null

var creating = false

window.addEventListener('DOMContentLoaded', () => {
    root = document.getElementById("bar-frame-1")
    width = root.getBoundingClientRect().width

    progressBar = document.getElementById("create-bar-progress")

    document.getElementById("start-form").addEventListener("submit", function(event)
    {
        event.preventDefault();

        if (creating) // if already creating
        {
            return
        }

        const number = parseInt(document.getElementById("number-field").value)

        if (number <= 0)
        {
            console.warn("Values less than or equal to 0 aren't allowed")
            return
        }
        progressBar.value = number
        progressBar.max = number
        progressBarInterval = Math.ceil(number/100)
        creating = true

    })
})

function createValueLinesFromCSV(file)
{
    const lines = file.split('\n');
    const result = [];
    const headers = lines[0].split(','); // Assuming the first row contains headers

    for (let i = 1; i < lines.length; i++) {
        const obj = {};
        const currentLine = lines[i].split(',');

        if (currentLine.length === headers.length) { //check for matching length to headers.
        for (let j = 0; j < headers.length; j++) {
            obj[headers[j].trim()] = currentLine[j].trim(); // trim whitespace
        }
        result.push(obj);
        }
    }
    return result;
}

// window.addEventListener('DOMContentLoaded', () => {
//     root = document.getElementById("bar-frame-1")
//     width = root.getBoundingClientRect().width

//     progressBar = document.getElementById("create-bar-progress")

//     document.getElementById("start-form").addEventListener("submit", function(event)
//     {
//         event.preventDefault();

//         if (creating) // if already creating
//         {
//             return
//         }

//         const number = parseInt(document.getElementById("number-field").value)

//         if (number <= 0)
//         {
//             console.warn("Values less than or equal to 0 aren't allowed")
//             return
//         }
//         progressBar.value = number
//         progressBar.max = number
//         progressBarInterval = Math.ceil(number/100)
//         creating = true
//         createValuesLines(number, 0)
//     })
//   })

// function createValuesLines(numOfLines, i)
// {
//     if (i > numOfLines)
//     {
//         creating = false
//         return
//     }
    
//     if (i == 0 && root.hasChildNodes())
//     {
//         root.innerHTML = '' // Clear child nodes
//     }

//     var node = document.createElement("div");
//     node.className = "bar"
//     node.style.height = `${i/numOfLines*100}%`
//     node.style.width = `${Math.max(1,width/numOfLines)}px` // Use 1.02 as buffer to make sure there is no empty space between lines
//     node.style.top = "0px"
//     node.style.left = `${(i-1)/(numOfLines)*width}px` // use -1 to make sure that the lines start at the beginning since i starts at 1
//     root.appendChild(node)
    
//     if (i%progressBarInterval == 0)
//     {
//         progressBar.value = i
//         setTimeout(() => {createValuesLines(numOfLines, i+1)}, 10)
//     }
//     else
//     {
//         createValuesLines(numOfLines, i+1)
//     }
// }