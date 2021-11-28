#include <bits/stdc++.h>
using namespace std;
struct timeframe {
  int enter, exit;
};
bool sortin(timeframe x, timeframe y){
  return x.exit > y.exit;
}
int main() {
  int n,k;
  cin >> n >> k;
  k--;
  timeframe years[n+1];
  for (int i = 0; i < n; i++){
    int x;
    cin >> x;
    years[i].enter = ((x / 12)+1) * 12;
    years[i].exit = (x/12) * 12;
  }
  years[n].enter = 0;
  years[n].exit = 0;
  sort(years,years+(n+1),sortin);
  int differences[n];
  int total = years[0].enter;
  for (int i = 1; i < n+1; i++){
    differences[i-1] = years[i-1].exit - years[i].enter;
  }
  sort(differences,differences + n, greater<int>());
  for (int i = 0; i < k; i++){
    if (differences[i] > 0){
      total -= differences[i];
    }
  }
  cout << total << endl;


} 
