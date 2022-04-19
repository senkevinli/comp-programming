#include <bits/stdc++.h>

using namespace std;

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }
#ifdef LOCAL
#define dbg(...) cerr << "(" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

#define ar array
#define ll long long
#define ld long double
#define sza(x) ((int)x.size())
#define all(a) (a).begin(), (a).end()

const int MAX_N = 1e5 + 5;
const ll MOD = 1e9 + 7;
const ll INF = 1e18;
const ld EPS = 1e-9;


ll determine_zeroes(int index, vector<ll> &a) {
    ll prev = 0;
    ll total = 0;

    for (ll i = index + 1; i < sza(a); ++i) {
        ll moves = (prev / a[i]) + 1;
        total += moves;
        prev = a[i] * moves;
    }

    prev = 0;

    for (ll i = index - 1; i >= 0; --i) {
        ll moves = (prev / a[i]) + 1;
        total += moves;
        prev = a[i] * moves;
    }

    return total;
}

void solve() {
    ll n;
    cin >> n;

    vector<ll> a(n);
    for (ll i = 0; i < n; ++i) {
        cin >> a[i];
    }

    ll minimum = INF;
    for (ll i = 0; i < n; ++i) {
        ll moves = determine_zeroes(i, a);
        minimum = min(minimum, moves);
    }

    cout << minimum << endl;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    int tc = 1;
    // cin >> tc;
    for (int t = 1; t <= tc; t++) {
        // cout << "Case #" << t << ": ";
        solve();
    }
}