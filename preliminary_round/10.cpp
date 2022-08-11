#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

vector<ll> tree[800010];
vector<ll> sutree[800010];
vector<ll>arr(200002);
ll asd=0;
void update(ll bucket, ll node, ll start, ll end, ll x){
	if(node<start || end<node) return;
	tree[bucket].push_back(x);
	if(start != end){
		update(bucket*2, node, start, (start+end)/2, x);
		update(bucket*2+1, node, (start+end)/2+1, end, x);
	}
}

ll get(ll node,ll start, ll end, ll left,ll right,ll x){
	if(left>end || right<start) return 0;
	if(left<=start && end<=right){
        ll jk=tree[node].end()-upper_bound(tree[node].begin(),tree[node].end(),x);
        //printf("%lld %lld %lld %lld\n",start,end,jk,sutree[node][end-start+1]);
        ll kp=end-start+1;
        ll pit=((sutree[node][kp]-sutree[node][kp-jk])-(x*jk))+((x*(kp-jk))-sutree[node][kp-jk]);
        return pit;
        //return jk;
    }
	ll mid = (start+end)/2;
	return get(node*2, start, mid, left, right, x) + get(node*2+1, mid+1, end, left, right, x);
}
void srt(ll node,ll start,ll end){
    sort(tree[node].begin(),tree[node].end());
    sutree[node].push_back(0);
    for(int io=0;io<end-start+1;io++)sutree[node].push_back(sutree[node][io]+tree[node][io]);
    if(start!=end){
        srt(node*2,start,(start+end)/2);
        srt(node*2+1,(start+end)/2+1,end);
    }
}
int main(){
	ll n, m,a,b,c,mi,cnt;
    ll ans=0;
    scanf("%lld %lld",&n,&m);
	for(int i=1; i<=n; i++){
        scanf("%lld ",&arr[i]);
		update(1, i, 1, n, arr[i]);
	}
    srt(1,1,n);
    for(int i=2;i<=m;i++)ans+=get(1,1,n,1,i,arr[i]);
    ll ma=ans;
    //printf("%lld\n",ans);
    for(int i=m+1;i<=n;i++){
        ll A=get(1,1,n,i-m+1,i-1,arr[i]);
        ll B=get(1,1,n,i-m,i-1,arr[i-m]);
        ans+=A;
        ans-=B;
        ma=max(ma,ans);
        //printf("%lld %lld %lld\n",ans,A,B);
    }
    printf("%lld\n",ma);
        
        
}