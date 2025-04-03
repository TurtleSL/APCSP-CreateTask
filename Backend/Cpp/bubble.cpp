#include "empty.cpp"

void bubble(SortData& data)
{
    for(int i=0;i<data.size-1;i++)
    {
        for(int j=0;j<data.size-i-1;j++)
        {
            if(data.data[j] > data.data[j+1])
            {
                int temp = data.data[j];
                data.data[j] = data.data[j+1];
                data.data[j+1] = temp;
            }
        }
    }
}