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
    cin >> line;
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
    {
        cout << line[i];
        i++;
    }
    cout << endl;

    string tag = line.substr(1, i - 1);

    if (currentPath.size() == 0)
    {
        currentPath = tag;
    }
    else
    {
        currentPath = currentPath + "." + tag;
    }

    cout << currentPath << endl;

    cout << i << endl;
    cout << line[i] << endl;

    while (line[i] != '>')
    {
        cout << "GOT HERE" << endl;
        i++;
        int start = i;
        // Get attribute name
        cout << i << endl;
        while (line[i] != ' ')
            i++;
        cout << i << endl;
        cout << "A" << endl;

        string attributeName = line.substr(start, i - 1);
        cout << attributeName << endl;

        // Get attribute value
        i += 4;
        start = i;
        while (line[i] != '"')
            i++;

        cout << "B" << endl;

        string attributeValue = line.substr(start, i - 1);

        tagMap[currentPath + "~" + attributeName] = attributeValue;

        cout << "C" << endl;

        i++;
    }

    BuildMap(currentPath, currentLineNum);
    return;
}

int main()
{
    // Recieve Number of Lines and Queries
    int Q;
    cin >> numOfLines >> Q;

    // Build Map
    BuildMap("", 0);

    // For now lets just print the map
    for (auto i = tagMap.begin(); i != tagMap.end(); i++)
    {
        cout << i->first << " " << i->second << endl;
    }
}
