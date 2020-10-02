```cpp
#include <stdio.h>
#include <string.h>

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

const int N = 110;

int n;
vector<int> origin, pre, preM, post, postM;

struct Node
{
    Node *lchild;
    Node *rchild;
    int v;
    Node() { lchild = rchild = NULL; }
    Node(int v)
    {
        lchild = NULL, rchild = NULL;
        this->v = v;
    }
};

void insert(Node *&root, int v)
{
    if (root == NULL)
    {
        root = new Node(v);
        root->v = v;
        return;
    }

    if (v < root->v)
    {
        insert(root->lchild, v);
    }
    else
    {
        insert(root->rchild, v);
    }
}

void preorder(Node *root, vector<int> &vi)
{
    if (root == NULL)
        return;
    vi.push_back(root->v);
    preorder(root->lchild, vi);
    preorder(root->rchild, vi);
}

void preorderM(Node *root, vector<int> &vi)
{
    if (root == NULL)
        return;
    vi.push_back(root->v);
    preorderM(root->rchild, vi);
    preorderM(root->lchild, vi);
}

void postorder(Node *root, vector<int> &vi)
{
    if (root == NULL)
        return;
    postorder(root->lchild, vi);
    postorder(root->rchild, vi);
    vi.push_back(root->v);
}

void postorderM(Node *root, vector<int> &vi)
{
    if (root == NULL)
        return;
    postorderM(root->rchild, vi);
    postorderM(root->lchild, vi);
    vi.push_back(root->v);
}

int main()
{
    cin >> n;
    int t = -1;
    Node *root = NULL;
    for (int i = 0; i < n; i++)
    {
        cin >> t;
        origin.push_back(t);
        insert(root, t);
    }
    preorder(root, pre);
    preorderM(root, preM);
    postorder(root, post);
    postorderM(root, postM);
    if (pre == origin)
    {
        cout << "YES" << endl;
        printf("%d", post[0]);
        for (int i = 1; i < n; i++)
        {
            printf(" %d", post[i]);
        }
        puts("");
    }
    else if (preM == origin)
    {
        cout << "YES" << endl;
        printf("%d", postM[0]);
        for (int i = 1; i < n; i++)
        {
            printf(" %d", postM[i]);
        }
        puts("");
    }
    else
    {
        cout << "NO" << endl;
    }
    return 0;
}
```

