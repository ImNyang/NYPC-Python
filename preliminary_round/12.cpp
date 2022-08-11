#include<bits/stdc++.h>
using namespace std;
#define X first
#define Y second
typedef pair<int,int> pii;
int n,m,k;
char a[15][25];
vector<pii> tmp,st;
vector<int> t;
int mx=-1;
void update(pii p,int s) {
	mx=s;
	cout << '\n' << mx << '\n';
	cout << (p.Y==0?0:p.Y==m+1?2*m:2*p.Y-1) << ' '
		<< (p.X==0?0:p.X==n+1?2*n:2*p.X-1) << '\n';
	for(int i=1;i<=n;i++){
		for(int j=1;j<=m;j++) cout << a[i][j];
		cout << '\n';
	}
}
void go(pii p,int x,int y,int d,int s) {
	if(a[x][y]=='@') return;
	if(a[x][y]=='.'){
		int dx=(d==0?-1:d==2?1:0);
		int dy=(d==1?1:d==3?-1:0);
		x+=dx,y+=dy,s+=2;
		while(1<=x&&x<=n&&1<=y&&y<=m){
			if(a[x][y]!='.') { go(p,x,y,d,s); return; }
			x+=dx,y+=dy,s+=2;
		}
		if(a[x][y]=='o'&&mx<s) update(p,s);
		return;
	}
	if(a[x][y]=='|'){
		if((d&1)&&mx<=s) update(p,s+1);
		return;
	}
	if(a[x][y]=='-'){
		if(!(d&1)&&mx<=s) update(p,s+1);
		return;
	}
	if(a[x][y]=='/'){
		int dx=(d==1?-1:d==3?1:0);
		int dy=(d==0?1:d==2?-1:0);
		int dd=(d<1?1:d<2?0:d<3?3:2);
		x+=dx,y+=dy,s+=2;
		while(1<=x&&x<=n&&1<=y&&y<=m){
			if(a[x][y]!='.') { go(p,x,y,dd,s); return; }
			x+=dx,y+=dy,s+=2;
		}
		if(a[x][y]=='o'&&mx<s) update(p,s);
		return;
	}
	if(a[x][y]=='\\'){
		int dx=(d==1?1:d==3?-1:0);
		int dy=(d==0?-1:d==2?1:0);
		int dd=(d<1?3:d<2?2:d<3?1:0);
		x+=dx,y+=dy,s+=2;
		while(1<=x&&x<=n&&1<=y&&y<=m){
			if(a[x][y]!='.') { go(p,x,y,dd,s); return; }
			x+=dx,y+=dy,s+=2;
		}
		if(a[x][y]=='o'&&mx<s) update(p,s);
		return;
	}
}
void bt(int idx) {
	if(idx==t.size()){
		for(int i=0;i<idx;i++)
			a[tmp[i].X][tmp[i].Y]=(t[i]?t[i]<2?'/':'\\':'.');
		for(int i=0;i<k;i++){
			int x=st[i].X,y=st[i].Y,d=0;
			if(x==0) x=1,d=2; if(x==n+1) x=n,d=0;
			if(y==0) y=1,d=1; if(y==m+1) y=m,d=3;
			go(st[i],x,y,d,0);
		}
		return;
	}
	for(int i=0;i<3;i++) t[idx]=i, bt(idx+1);
}
int main()
{
	ios::sync_with_stdio(0),cin.tie(0);
	cin >> n >> m;
	for(int i=0;i<=n+1;i++) for(int j=0;j<=m+1;j++){
		if(1<=i&&i<=n&&1<=j&&j<=m){
			char c; cin >> c; a[i][j]=c;
			if(c=='?') tmp.push_back({i,j});
		}
		else a[i][j]='x';
	}
	cin >> k;
	for(int i=0;i<k;i++){
		int x,y; cin >> y >> x;
		x=x?x/2+1:0, y=y?y/2+1:0;
		st.push_back({x,y}); a[x][y]='o';
	}
	t.resize(tmp.size());
	bt(0);
}