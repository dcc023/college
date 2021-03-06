#include <stdio.h>

int main()
{
  FILE *ifp, *ofp;
  char *mode = "r";
  char outputFilename[] = "out.list";
  char username[9];
  int score;
  ifp = fopen("in.list", mode);
  if (ifp == NULL) {
    fprintf(stderr, "Can't open input file in.list!\n");
    exit(1);
  }
  ofp = fopen(outputFilename, "w");
  if (ofp == NULL) {
    fprintf(stderr, "Can't open output file %s!\n", outputFilename);
    exit(1);
  }
  while (fscanf(ifp, "%s %d", username, &score) == 2) {
    fprintf(ofp, "%s %d\n", username, score+10);
  }
  fclose(ifp);
  fclose(ofp);
  return 0;
}
