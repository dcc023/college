/***************************************************************
* <Dylan Campbell>
* <10/11/2015>
*
* <Game of Life>
***************************************************************/

#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

#define MAX_WIDTH 40

// function prototypes
void ParseCmdLine(int, char**);
void ShowUsage(char*);
int ReadGen0(bool[MAX_WIDTH][MAX_WIDTH]);
void DisplayBoard(bool[MAX_WIDTH][MAX_WIDTH], int, int);
void NextTick(bool [MAX_WIDTH][MAX_WIDTH], int len);


// default command line parameters
int numGens = 10;
int genInt = 1;

/*******
* MAIN
*******/
int main(int argc, char **argv)
{
    // "*" => true, " " => false
    bool board[MAX_WIDTH][MAX_WIDTH];
    bool copyboard[MAX_WIDTH][MAX_WIDTH];
    int len;

    // command line, read gen0, and display
    ParseCmdLine(argc, argv);
    len = ReadGen0(board);
    DisplayBoard(board, 0, len);

    // new generations
    NextTick(board, len);
}

// parses the command line for parameters
void ParseCmdLine(int argc, char **argv)
{
    if(argc == 1)
    {
        ShowUsage(argv[0]);
        exit(0);
    }

    for(int i = 1; i < argc; i++)
    {
        // default values
        if(!strcmp(argv[i], "-D"))
            break;
        // help/usage
        if(!strcmp(argv[i], "-h"))
        {
            ShowUsage(argv[0]);
            exit(0);
        }
        // number of generations to produce
        else if(strcmp(argv[i], "-n") > 0)
        {
            argv[i] += 2;
            numGens = atoi(argv[i]);
        }
        // display generation interval
        else if(strcmp(argv[i], "-i") > 0)
        {
            argv[i] += 2;
            genInt = atoi(argv[i]);
        }
    }
}

// displays help/usage
void ShowUsage(char* app)
{
    cout << "Usage: " << app << " [-(Dhd)] [-(nia)<val>]\n";
    cout << " -D\t\tUse default values for parameters\n";
    cout << " -h\t\tShow this usage\n";
    cout << " -d\t\tDisplay debugging output\n";
    cout << " -n<val>\tSet the number of generations to <val>\n";
    cout << " -i<val>\tSet the generation interval to <val>\n";
    cout << " -a<val>\tSet animation delay to <val>\n";
}

// reads the initial generation
int ReadGen0(bool board[MAX_WIDTH][MAX_WIDTH])
{
    char line[MAX_WIDTH];
    int i = 0;
    int len = 0;

    // we assume that the input contains a blank border
    while(cin.getline(line, MAX_WIDTH))
    {
        // grab each character of each line
        for(int j = 0; j < strlen(line); j++)
            board[i][j] = (line[j] == '*');
        i++;
        // note the board size
        len = strlen(line);
    }

    return len;
}

void NextTick(bool board[MAX_WIDTH][MAX_WIDTH], int len)
{
    bool copyboard[MAX_WIDTH][MAX_WIDTH];
    int neighbors;

    for(int i = 1; i <= numGens; i++)
    {
        //set the boards to be the same
        for(int row = 0; row < len; row++)
        {
            for(int col = 0; col < len; col++)
            {
                copyboard[row][col] = board[row][col];
            }
        }
        //change board according to number of neighbors
        for(int row = 1; row < len - 1; row++)
        {
            for(int col = 1; col < len - 1; col++)
            {

                //Add neighbors
                neighbors = 0;

                if(copyboard[row-1][col])//On the low low
                {
                    neighbors++;
                }
                if(copyboard[row+1][col])//Neighbors up top
                {
                    neighbors++;
                }
                if(copyboard[row][col-1])//To the left, to the left
                {
                    neighbors++;
                }
                if(copyboard[row][col+1])//To the roight, m8
                {
                    neighbors++;
                }
                if(copyboard[row-1][col-1])//lower left diagonal
                {
                    neighbors++;
                }
                if(copyboard[row-1][col+1])//lower right diagonal
                {
                    neighbors++;
                }
                if(copyboard[row+1][col-1])//upper left diagonal
                {
                    neighbors++;
                }
                if(copyboard[row+1][col+1])//upper right diagonal
                {
                    neighbors++;
                }


                //Set board conditions regarding neighbors.
                if(neighbors > 3 or neighbors < 2)
                    board[row][col] = false;
                if(neighbors == 2 && board[row][col])
                    board[row][col] = true;
                if(neighbors == 3)
                    board[row][col] = true;

            }
        }


        //Display the board
        if(i % numGens)
        {
            DisplayBoard(board, i, len);
        }
    }
}

void DisplayBoard(bool board[MAX_WIDTH][MAX_WIDTH], int gen, int len)
{
    cout << "Gen" << gen << ":/n";

    for(int r=1; r<len-1; r++)
    {
        // for reference, display a top numerical legend
        if( r ==1)
        {
            cout << " ";
            for (int c=1; c<len-1; c++)
                cout << (c % 10) << " ";
            cout << endl;
        }

        // for reference, also display a left numerical legend
        cout << (r % 10) << " ";

        for (int c=1; c<len-1; c++)
            cout << ((board[r][c]) ? "*" : " ") << " "; //turnary, ? separates true and false options
        cout << endl;
    }
    cout << endl;
}
