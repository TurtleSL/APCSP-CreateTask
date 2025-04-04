#include <iostream>
#include <random>
#include <fstream>

// All the sort algorithm functions
#include "bubble.hpp"

// Simple method that prints all items from an array
void printArray(const std::vector<int> data);

int main(int argc, char** argv)
{
    std::vector<int> data;

    // Initialize random values to the array
    for(int i=0;i<data.size();i++)
    {
        int rv = rand() % 10 + 1;
        data[i] = rv;
    }

    printArray(data);

    bubble(data);

    printArray(data);
    
    return 0;
}

void printArray(const std::vector<int> data)
{
    for(int i=0;i<data.size();i++)
    {
        std::cout << data[i] << ", ";
    }
    std::cout << std::endl;
}