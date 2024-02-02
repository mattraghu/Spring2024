// Attribute Parser

#include <iostream>
#include <map>
using namespace std;

int numOfLines;
map<string, string> tagMap;
// map to store tag and its attributes
// format: map <key type, value type> name;
// tagMap[tag] = value

void BuildMap(string currentPath, int currentLineNum)
{
    currentLineNum++;
    // End of Recursion
    if (currentLineNum > numOfLines)
    {
        return;
    }

    int i = 1;

    string line;
    getline(cin, line);

    // End of tag
    if (line[i] == '/')
    {
        // Remove tag from currentPath
        while (line[i] != '>')
            i++;

        // may error if out of bounds check later
        currentPath = currentPath.substr(0, currentPath.size() - i + 1);

        BuildMap(currentPath, currentLineNum);
        return;
    }
    // Beggining of tag

    while (line[i] != ' ' && line[i] != '>')
        i++;

    string tag = line.substr(1, i - 1);

    if (currentPath.size() == 0)
    {
        currentPath = tag;
    }
    else
    {
        currentPath = currentPath + "." + tag;
    }

    while (line[i] != '>')
    {
        i++;
        int start = i;
        // Get attribute name
        while (line[i] != ' ')
        {
            i++;
        }

        string attributeName = line.substr(start, (i - 1) - start + 1);

        // Get attribute value
        i += 4;
        start = i;
        while (line[i] != '"')
            i++;

        string attributeValue = line.substr(start, (i - 1) - start + 1);

        tagMap[currentPath + "~" + attributeName] = attributeValue;

        i++;
    }

    BuildMap(currentPath, currentLineNum);
    return;
}

int main()
{

    string test = "testing123";
    cout << test.substr(100, test.size() + 10) << endl;

    // Recieve Number of Lines and Queries
    int Q;

    string numLinesAndQueries;
    getline(cin, numLinesAndQueries);
    numOfLines = stoi(numLinesAndQueries.substr(0, numLinesAndQueries.find(" ")));
    Q = stoi(numLinesAndQueries.substr(numLinesAndQueries.find(" ") + 1));

    // Build Map
    BuildMap("", 0);

    // // For now lets just print the map
    // for (auto i = tagMap.begin(); i != tagMap.end(); i++)
    // {
    //     cout << i->first << " : " << i->second << endl;
    // }

    // Queries
    string query;
    while (Q--)
    {
        getline(cin, query);

        cout << "Trying to process " << query << endl;

        auto result = tagMap.find(query);

        if (result == tagMap.end())
        {
            cout << "Not found!" << endl;
        }
        else
        {
            cout << result->second << endl;
        }
    }
}
