#include <iostream>
#include <random>
#include <fstream>
#include <vector>

// All the sort algorithm functions
#include "bubble.hpp"

// Simple method that prints all items from an array
void printArray(const std::vector<int> data);

int main(int argc, char** argv)
{
    // Overlying data list
    std::vector<int> data;

    printArray(data);

    bubble(data);

    printArray(data);
    
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