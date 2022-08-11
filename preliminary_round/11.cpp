#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
struct nd{
    ll i,k;
};
vector<pair<ll,ll>>l;
vector<pair<ll,ll>>st;
vector<pair<ll,ll>>ch;
deque<ll>bu;
vector<ll>tree(2001000);
vector<ll>tree1(2001000);
ll cse=0,inf=1e12;
ll ans[500001];
ll seg(ll n,ll s,ll e){
    tree1[n]=inf;
    if(s==e){return tree[n]=inf;}
    return tree[n]=min(seg(n*2,s,(s+e)/2),seg(n*2+1,(s+e)/2+1,e));
}
void propagate(ll n,ll s,ll e){
    if(tree1[n]!=inf){
        if(s!=e){
            tree1[n*2]=min(tree1[n*2],tree1[n]);
            tree1[n*2+1]=min(tree1[n*2+1],tree1[n]);
        }
        tree[n]=min(tree[n],tree1[n]);
        tree1[n]=inf;
    }
}
ll max1(ll n,ll s,ll e,ll left,ll right){
    propagate(n,s,e);
    if(left>e||right<s){return inf;}
    if(left<=s&&e<=right){return tree[n];}
    return min(max1(n*2,s,(s+e)/2,left,right),max1(n*2+1,(s+e)/2+1,e,left,right));
}
void change(ll n,ll s,ll e,ll s1,ll e1,ll f){
    propagate(n,s,e);
    if(s1<=s&&e<=e1){tree1[n]=min(tree1[n],f);propagate(n,s,e);return;}
    if(e1<s||s1>e){return;}
    change(n*2,s,(s+e)/2,s1,e1,f);
    change(n*2+1,(s+e)/2+1,e,s1,e1,f);
    tree[n]=min(tree[n*2],tree[n*2+1]);
}
ll lb(ll x,ll s,ll k){
    ll start=s;
    ll end=k;
    while(end-start>0){
        ll mid=(start+end)/2;
        if(st[mid].first<=x)start=mid+1;
        else end=mid;
    }
    return end;//s~end-1
}
ll ld(ll x,ll k){
    ll start=0;
    ll end=k;
    while(end-start>0){
        ll mid=(start+end)/2;
        if(st[mid].first<x)start=mid+1;
        else end=mid;
    }
    return end;//s~end-1
}
int main()
{
    ll a,b,c,d,q,k,i,A,B,C;
    ll bunt=0;
    scanf("%lld %lld %lld",&a,&b,&k);
    for(int i=1;i<=a;i++){
        scanf("%lld %lld\n",&A,&B);
        l.push_back(pair<ll,ll>(A,B));
    }
    for(int i=1;i<=k;i++){
        scanf("%lld\n",&C);
        st.push_back(pair<ll,ll>(C,i));
        l.push_back(pair<ll,ll>(C,0));
    }
    sort(l.begin(),l.end());
    sort(st.begin(),st.end());
    ll left=0,right=0;
    ll cnt=0;
    ll ck[500010]={0,};
    ll inx=0,lnx=0;
    ll rnt=0;
    ll last[2]={-inf,};
    if(l[0].second!=0){ck[l[0].second]+=1;cnt++;}
    while(1){
        if(l[right].second!=0){
            if(cnt<b){
                if(right+1<a+k){
                    if(l[right+1].second!=0){
                        if(ck[l[right+1].second]==0)cnt++;
                        ck[l[right+1].second]++;
                    }
                    right++;
                }else{break;}
            }else{
                if(l[left].second!=0){   
                    ll lt=l[left].first,rt=l[right].first;
                    ch.push_back(pair<ll,ll>(lt,rt));
                    if(bunt!=0){
                        while(bunt!=0){
                            if(bu[0]>lt)break;
                            ch.push_back(pair<ll,ll>(bu[0],rt));
                            bunt--;
                            bu.pop_front();
                        }
                    }
                    last[0]=lt;
                    last[1]=rt;
                    if(inx<k){
                        if(inx-1>=0&&st[inx-1].first==l[right].first)ch.push_back(pair<ll,ll>(lt,rt));
                        else ch.push_back(pair<ll,ll>(lt,st[inx].first));
                    }
                    if(lnx-1>=0&&lnx-1<k)ch.push_back(pair<ll,ll>(st[lnx-1].first,rt));
                    if(ck[l[left].second]!=0)ck[l[left].second]--;
                    if(ck[l[left].second]==0)cnt--;
                    rnt++;
                }
                left++;
            }
        }else{
            bu.push_back(l[right].first);
            bunt++;
            if(inx<k)inx++;
            if(last[0]!=-inf)ch.push_back(pair<ll,ll>(last[0],l[right].first));
            rnt=0;
            if(right+1<a+k){
                if(l[right+1].second!=0){
                    if(ck[l[right+1].second]==0)cnt++;
                    ck[l[right+1].second]++;
                }
                right++;
            }else{break;}
        }
        if(l[left].second==0){
            if(lnx<k)lnx++;
            left++;
        }
    }
    sort(ch.begin(),ch.end());
    ch.erase(unique(ch.begin(),ch.end()),ch.end());
    cse=ch.size();
    seg(1,1,k);
    for(int i=0;i<cse;i++){
        ll jk=ld(ch[i].first,k);
        ll rd=lb(ch[i].second,jk,k);
        if(rd-1>=jk)change(1,1,k,jk+1,rd,ch[i].second-ch[i].first);
    }
    for(int i=1;i<=k;i++)ans[st[i-1].second]=max1(1,1,k,i,i);
    for(int i=1;i<=k;i++)printf("%lld\n",ans[i]);
}