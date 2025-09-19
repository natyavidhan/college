#include <iostream>
#include <string>
using namespace std;

class GameEntry
{
    string name;
    int score;

public:
    GameEntry(string n = "", int s = 0)
    {
        name = n;
        score = s;
    }

    string get_name() const { return name; }
    int get_score() const { return score; }
};

class Scores
{
    GameEntry *entries;
    int maxEntries;
    int numEntries;

public:
    Scores(int n = 10)
    {
        maxEntries = n;
        numEntries = 0;
        entries = new GameEntry[maxEntries];
    }

    ~Scores()
    {
        delete[] entries;
    }

    void add_score(const GameEntry &e)
    {
        int s = e.get_score();

        if (numEntries == maxEntries && s <= entries[numEntries - 1].get_score())
        {
            cout << "?? Score not high enough to enter the leaderboard.\n";
            return;
        }

        if (numEntries < maxEntries)
            numEntries++;

        int i = numEntries - 2;
        while (i >= 0 && entries[i].get_score() < s)
        {
            entries[i + 1] = entries[i];
            i--;
        }
        entries[i + 1] = e;
    }

    void delete_by_name(const string &name)
    {
        int idx = -1;
        for (int i = 0; i < numEntries; i++)
        {
            if (entries[i].get_name() == name)
            {
                idx = i;
                break;
            }
        }

        if (idx == -1)
        {
            cout << "Player not found!\n";
            return;
        }

        for (int i = idx; i < numEntries - 1; i++)
        {
            entries[i] = entries[i + 1];
        }
        numEntries--;
        cout << "Entry for " << name << " deleted.\n";
    }

    void delete_last()
    {
        if (numEntries == 0)
        {
            cout << "No entries to delete!\n";
            return;
        }
        numEntries--;
        cout << "Last entry deleted.\n";
    }

    void display()
    {
        cout << "\n--- Leaderboard ---\n";
        for (int i = 0; i < numEntries; i++)
        {
            cout << i + 1 << ". " << entries[i].get_name()
                 << " : " << entries[i].get_score() << endl;
        }
        if (numEntries == 0)
            cout << "No entries yet.\n";
    }
};

int main()
{
    int capacity;
    cout << "Enter leaderboard size (max entries): ";
    cin >> capacity;

    Scores obj(capacity);

    int choice;
    while (true)
    {
        cout << "\nGame Entry Menu\n";
        cout << "1. Add new entry\n";
        cout << "2. Display leaderboard\n";
        cout << "3. Delete entry by name\n";
        cout << "4. Delete last entry\n";
        cout << "5. Exit\n";
        cout << "Enter choice: ";
        cin >> choice;

        if (choice == 1)
        {
            string name;
            int score;
            cout << "Enter player name: ";
            cin >> name;
            cout << "Enter player score: ";
            cin >> score;
            GameEntry e(name, score);
            obj.add_score(e);
        }
        else if (choice == 2)
        {
            obj.display();
        }
        else if (choice == 3)
        {
            string name;
            cout << "Enter player name to delete: ";
            cin >> name;
            obj.delete_by_name(name);
        }
        else if (choice == 4)
        {
            obj.delete_last();
        }
        else if (choice == 5)
        {
            cout << "Exiting program...\n";
            break;
        }
        else
        {
            cout << "Invalid choice\n";
        }
    }

    return 0;
}