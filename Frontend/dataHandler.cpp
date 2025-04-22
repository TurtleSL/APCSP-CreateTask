#include "dataHandler.h"

static std::vector<std::vector<std::string>> temp;

int generateData(int length, std::string Type) {
    std::vector<std::string> headerStr; // Vector of headers
	std::vector<std::string> dataStr;	// Vector of data

	std::stringstream lengthStr;
	lengthStr << length;

    headerStr.push_back("Length"); // Add "Length" as a string
	dataStr.push_back(lengthStr.str());

    for (int i = 0; i < length; i++) {
        std::stringstream arrayIdx;
		std::stringstream arrayInt;
        arrayIdx << "A" << i;
		arrayInt << i + 1;
        headerStr.push_back(arrayIdx.str()); // Add the string from stringstream
		dataStr.push_back(arrayInt.str());	 // Add the int from stringstream
    }

    headerStr.push_back("Type"); // Add "Type" as a string
	dataStr.push_back(Type);

    temp.push_back(headerStr);
	temp.push_back(dataStr);

	// open file to write to 
	std::ofstream outputFile("Data/inputData.csv");

	if (!outputFile.is_open()) 
	{
        std::cerr << "Error: Could not open file for writing." << std::endl;
        return 1; // Indicate an error
    }

	// Check for first index of array (length)
	std::string secondRowFirstColumn = temp[0][1];
	std::cout << "0, 1: " << secondRowFirstColumn << std::endl;

	// write the temp vector to the file
	for (const auto& row : temp) 
	{ // Iterate through each row in temp
        for (size_t i = 0; i < row.size(); ++i) 
		{ // Iterate through each element in the row
            outputFile << row[i];
            if (i < row.size() - 1) 
			{
                outputFile << ","; // Add comma separator
            }
        }
        outputFile << std::endl; // Add newline for the next row
    }

    outputFile.close();
	return 0;
}