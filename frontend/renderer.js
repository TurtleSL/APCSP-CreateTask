window.addEventListener('DOMContentLoaded', () => {
    document.getElementById("start-form").addEventListener("submit", function(event)
    {
        event.preventDefault();

        const number = parseInt(document.getElementById("number-field").value)

        if (number <= 0)
        {
            console.warn("Values less than or equal to 0 aren't allowed")
            return
        }
        createValuesLines(number)
        
    })
  })

function createValuesLines(numOfLines)
{
    var root = document.getElementById("bar-frame-1")
    if (root.hasChildNodes())
    {
        root.innerHTML = '' // Clear child nodes
    }
    for (var i=1; i<numOfLines+1; i++)
    {
        var node = document.createElement("div");
        node.className = "bar"
        node.style.height = `${i/numOfLines*100}%`
        node.style.width = `${1.02/(numOfLines)*100}%` // Use 1.02 as buffer to make sure there is no empty space between lines
        node.style.top = "0px"
        node.style.left = `${(i-1)/(numOfLines)*100}%` // use -1 to make sure that the lines start at the beginning since i starts at 1
        root.appendChild(node)
    }
}
