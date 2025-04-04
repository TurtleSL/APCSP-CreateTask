#pragma once

#include <vector>

// Simple abstraction for data that will be outputted to Cpp_data.csv
struct SortData
{
    int size; // Size of the list to be created
    std::vector<int> data; //Actual data list
    unsigned char type; // Type of sort
    double sort_time; // How much time it takes to sort the entire list
};