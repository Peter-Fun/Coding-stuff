#include <bits/stdc++.h>
using namespace std;
int n;
int grid[1100][1100];
int visited[1100][1100];
int area;
int perimeter;
int xdir[4] = {0,0,-1,1};
int ydir[4] = {1,-1,0,0};
void look(int x,int y){
  area++;
  visited[x][y] = 1;
  for (int i = 0; i < 4; i++){
    int nx = x + xdir[i];
    int ny = y + ydir[i];
    if (grid[nx][ny] == 0){
      perimeter++;
    }
    else{
      if (visited[nx][ny] == 0) look(nx,ny);
    }
  }
}
int main() {
  freopen("perimeter.in","r",stdin);
  freopen("perimeter.out","w",stdout);
  cin >> n;
  for (int i = 0; i < 1100; i++){
    for (int j = 0; j < 1100; j++){
      visited[i][j] = 0;
    }
  }
  for (int i = 0; i < n; i++){
    for (int j = 0; j < n; j++){
      char input;
      cin >> input;
      if (input == '.'){
        grid[i+50][j+50] = 0;
      }
      else{
        grid[i+50][j+50] = 1;
      }
    }
  }
  int maxarea = 0;
  int maxareaperi = 0;
  for (int i = 0; i < n; i++){
    for (int j = 0; j < n; j++){
      area = 0;
      perimeter = 0;
      if (grid[i+50][j+50] == 1 && visited[i+50][j+50] == 0){
        look(i+50,j+50);
      }
      if (area > maxarea){
        maxarea = area;
        maxareaperi = perimeter;
      }
      else if (area == maxarea && perimeter < maxareaperi){
        maxareaperi = perimeter;
      }
    }
  }
  cout << maxarea << " " << maxareaperi;

} 
