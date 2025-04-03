#include <iostream>
#include <random>
#include <fstream>

#include "SortData.hpp"
#include "bubble.hpp"

// Simple method that prints all items from an array
void printArray(const SortData& data);

int main()
{
    SortData data;
    data.size = 10;

    // Initialize random values to the array
    for(int i=0;i<data.size;i++)
    {
        int rv = rand() % 10 + 1;
        data.data[i] = rv;
    }

    printArray(data);

    bubble(data);

    printArray(data);
    
    return 0;
}

void printArray(const SortData& data)
{
    for(int i=0;i<data.size;i++)
    {
        std::cout << data.data[i] << ", ";
    }
    std::cout << std::endl;
}