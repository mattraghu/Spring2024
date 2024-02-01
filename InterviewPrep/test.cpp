#include <iostream>
#include <map>
using namespace std;

map<string, string> tagValueMap; // Map to hold tag-attribute and its value

// Function to create the map of tags and their attributes
void createTagAttributeMap(int &linesRemaining, string currentPath)
{
    if (linesRemaining == 0)
        return; // Base case for recursion

    string line, currentTag, attribute, value;
    getline(cin, line); // Read the current line

    int i = 1; // Index to parse the line
    if (line[i] == '/')
    { // Found a closing tag
        while (line[i] != '>')
            i++;
        if (currentPath.size() > (i - 2)) // Remove the last tag from the path
            currentTag = currentPath.substr(0, currentPath.size() - i + 1);
        else
            currentTag = "";
    }
    else
    { // Found an opening tag
        while (line[i] != ' ' && line[i] != '>')
            i++;
        currentTag = line.substr(1, i - 1); // Extract the tag name
        if (currentPath != "")
            currentTag = currentPath + "." + currentTag; // Build the tag path

        int j;
        while (line[i] != '>')
        { // Parse attributes
            j = ++i;
            while (line[i] != ' ')
                i++;
            attribute = line.substr(j, i - j); // Extract attribute name

            while (line[i] != '\"')
                i++;
            j = ++i;
            while (line[i] != '\"')
                i++;
            value = line.substr(j, i - j); // Extract attribute value
            i += 1;

            tagValueMap[currentTag + "~" + attribute] = value; // Map tag-attribute to its value
        }
    }
    createTagAttributeMap(--linesRemaining, currentTag); // Recursive call with decreased line count
}

int main()
{
    int numberOfLines, queries;
    cin >> numberOfLines >> queries; // Input number of lines and queries
    cin.ignore();                    // Ignore trailing newline character

    createTagAttributeMap(numberOfLines, ""); // Create the tag-attribute map

    string attributeQuery, valueResult;
    while (queries--)
    {
        getline(cin, attributeQuery);              // Read the query
        valueResult = tagValueMap[attributeQuery]; // Get the value from the map
        if (valueResult == "")
            valueResult = "Not Found!"; // Handle not found case
        cout << valueResult << endl;    // Output the result
    }
    return 0;
}