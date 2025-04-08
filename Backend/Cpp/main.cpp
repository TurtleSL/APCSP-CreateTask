#include <iostream>
#include <vector>

// Parse header for the input
#include "Parse.cpp"

// All the sort algorithm functions
#include "bubble.hpp"

// Simple method that prints all items from an array
void printArray(const std::vector<int> data);

int main(int argc, char** argv)
{
    ArrayConfigs data = parseCSV("../../inputData.csv");

    printArray(data.array);
    
    return 0;
}

void printArray(const std::vector<int> data)
{
    for(int i=0;i<data.size();i++)
    {
        std::cout << data.at(i) << ", ";
    }
    std::cout << std::endl;
}