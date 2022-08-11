include <bits/stdc++.h>
#define int long long
#define ll __int128

using namespace std;
vector<ll> NCR[200000], v;

ll ncr(ll n, ll r){
    if (r==0) return 1;
    if (r==1) return n;
    if (r==2) return n*(n-1)/2;
    if (r==3) return n*(n-1)*(n-2)/6;
    if (r==4) return n*(n-1)*(n-2)*(n-3)/24;
    if ((int)NCR[n].size()<=r-5) return 1e24;
    return NCR[n][r-5];
}

ll calc(int sz, int x, int y){
    ll ret = 0;
    for (int i=0;i<sz;i++){
        for (int j=0;j<=i;j++){
            ret += ncr(x+i, y+j);
            if (ret>1e24 || ret<0) return 1e24;
        }
    }
    return ret;
}

ll mxval[101] = {0, (ll)1e24, 1414213562374, 181712061, 2213366, 164378, 29941, 9071, 3768, 1929, 1143, 752, 535, 404, 320, 263, 223, 194, 172, 155, 142, 131, 123, 116, 110, 106, 102, 98, 96, 93, 91, 90,
89, 87, 86, 86, 85, 85, 84, 84, 84, 84, 84, 84, 84, 84, 84, 85, 85, 85, 86, 86, 86, 87, 87, 88, 89, 89, 90, 90, 91,
91, 92, 93, 93, 94, 95, 96, 96, 97, 98, 98, 99, 100, 101, 102, 102, 103, 104, 105, 106, 106, 107, 108, 109, 110, 110, 111, 112, 113, 114, 115, 116, 116, 117, 118, 119, 120, 121, 122};
void solve(int n){
    scanf("%lld", &n);
    if (n==1) {printf("-1\n"); return;}
    int ans = upper_bound(v.begin(), v.end(), n) - lower_bound(v.begin(), v.end(), n);
    //printf("%lld\n", ans);
    if (n==2) ans++;
    else if (n==3) ans += 3;
    else ans += 4;
    //printf("%lld\n", ans);
    //for (int i=0;i<70;i++) printf("%lld ", mxval[i]);
    for (int i=2;i<=100;i++){
        if (mxval[i]<=i*2) break;
        int l = i*2, r = mxval[i];
        while(l<r){ ///size 1
            int m = (l+r)/2;
            ll tmp = ncr(m, i);
            if (tmp<n) l = m+1;
            else if (tmp>n) r = m;
            else{
                if (m==i*2) ans++;
                else ans += 2;
                break;
            }
        }
        //printf("%lld %lld\n", i, ans);

        l = i*2, r = mxval[i];
        while(l<r){ ///size 2
            int m = (l+r)/2;
            ll tmp = ncr(m, i) + ncr(m-2, i-1);
            if (tmp<n) l = m+1;
            else if (tmp>n) r = m;
            else{
                if (m==i*2) ans++;
                else ans += 2;
                break;
            }
        }
        //printf("%lld %lld\n", i, ans);

        l = i*2, r = mxval[i];
        while(l<r){ ///size 3
            int m = (l+r)/2;
            ll tmp = ncr(m, i) + ncr(m-4, i-2);
            if (tmp<n) l = m+1;
            else if (tmp>n) r = m;
            else{
                if (m==i*2) ans++;
                else ans += 2;
                break;
            }
        }
        //printf("%lld %lld\n", i, ans);
        if (i==2) continue;

        l = i*2, r = mxval[i];
        while(l<r){ ///size 4
            int m = (l+r)/2;
            ll tmp = ncr(m, i) + ncr(m-6, i-3) - ncr(m-2, i-1);
            if (tmp<0) tmp = 1e24;
            if (tmp<n) l = m+1;
            else if (tmp>n) r = m;
            else{
                if (m==i*2) ans++;
                else ans += 2;
                break;
            }
        }
        //printf("%lld %lld\n", i, ans);
    }
    printf("%lld\n", ans);
}

signed main(){
    //freopen("output.txt", "w", stdout);
    for (int i=5;i<=101;i++){
        NCR[i].push_back(1);
        for (int j=i+1;j<200000;j++){
            ll tmp = NCR[j-1].back()*j/(j-i);
            if (tmp>1e24) break;
            NCR[j].push_back(tmp);
        }
    }
    for (int z=5;z<=100;z++){
        bool flag = 0;
        for (int i=0;i<200000;i++){
            bool flag2 = 0;
            for (int j=0;j<=i/2;j++){
                ll tmp = calc(z, i, j);
                if (tmp>1e18) break;
                flag = 1, flag2 = 1;
                v.push_back(tmp);
                if (i!=j*2) v.push_back(tmp);
            }
            if (!flag2) break;
        }
        if (!flag) break;
    }
    sort(v.begin(), v.end());

    int t;
    scanf("%lld", &t);
    for (int i=1;i<=t;i++) solve(i);
    return 0;
}