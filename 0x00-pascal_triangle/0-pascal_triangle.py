#!/usr/bin/python3
'''Module to return pascal triangle'''

def pascal_triangle(num):
{
    '''
    Pascal's triangle
    Args: num(int): The number of rows of the triangle
    Returns:
        List of lists of integers representing the Pascal’s triangle
    '''
    lists = []
    if (num == 0):
    {
        return lists;
    }
    for(i in range(num)):
    {
        lists.append([]);
        lists[i].append(1);
        if (i > 0):
        {
            for (j in range(1, i)):
            {
                lists[i].append(lists[i - 1][j - 1] + lists[i - 1][j]);
            }
            lists[i].append(1);
        }
    }
    return lists;
}
