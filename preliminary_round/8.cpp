#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
vector<ll>l(1000001),t(4001001);
ll st[1000010]={0,};
ll seg(ll n,ll s,ll e){
    if(s==e){return t[n]=0;}
    return t[n]=seg(n*2,s,(s+e)/2)+seg(n*2+1,(s+e)/2+1,e);
}
ll m(ll n,ll s,ll e,ll left,ll right){
    if(left>e||right<s){return 0;}
    if(left<=s&&e<=right){return t[n];}
    return m(n*2,s,(s+e)/2,left,right)+m(n*2+1,(s+e)/2+1,e,left,right);
}
void h(ll n,ll s,ll e,ll i,ll f){
    if(i<s||i>e){return;}
    t[n]+=f;
    if(s!=e){h(n*2,s,(s+e)/2,i,f);h(n*2+1,(s+e)/2+1,e,i,f);}
}
int main()
{
    ll a,b,c,d,q,k,i,cnt=1;
    scanf("%lld",&a);
    for(i=1;i<=2*a;i++){scanf("%lld\n",&l[i]);}
    seg(1,1,2*a);
    for(i=1;i<=2*a;i++){
        if(st[l[i]]==0){
            st[l[i]]=i;
            h(1,1,2*a,i,1);
        }else{
            ll sm=m(1,1,2*a,st[l[i]]+1,i);
            h(1,1,2*a,st[l[i]],-1);
            st[l[i]]=0;
            cnt+=sm+1;
        }
    }
    printf("%lld\n",cnt);
}