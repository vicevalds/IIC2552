#include<bits/stdc++.h>

using namespace std;

vector<vector<int> > edges;
vector<int> visitado;
vector<int> d;

void dfs(int nodo){
    //hago cosas al entrar al nodo
    visitado[nodo] = 1;
    d[nodo] = 1;
    for(auto u: edges[nodo]){
        if(visitado[u] == 0){
            //recursion sobre los hijos
            dfs(u);
            //agrupar info
            d[nodo] = max(d[nodo], 1 + d[u]);
        }
    }
    visitado[nodo] = 2;    
}

int main() {
    int n; 
    cin >> n; //tamaño del arbol
    
    edges.resize(n);
    visitado.resize(n, 0);
    d.resize(n);

    for(int i = 0; i < n-1; i++){
        int u, v;
        cin>>u>>v;
        u--; v--;
        edges[u].push_back(v);
        edges[v].push_back(u);
    }

    dfs(0) // dfs desde la raiz

    //respuesta
    int maxi = 0;
    for(int i = 0; i < n-1; i++){
        maxi = max(maxi, d[i]);
    }
    cout<<maxi<<endl;
}