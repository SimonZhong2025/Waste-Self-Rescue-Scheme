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

Node *findmax(Node *root)
{
    if (root->rchild == NULL)
        return root;
    else
        return findmax(root->rchild);
}

Node *findmin(Node *root)
{
    if (root->lchild == NULL)
        return root;
    else
        return findmin(root->lchild);
}

void deleteNode(Node *&root, int v)
{
    if (root == NULL)
        return;  // 不存在
    if (root->v == v)
    {
        if (root->lchild == NULL && root->rchild == NULL)
        {
            root = NULL;
            return;
        }
        else if (root->lchild != NULL)
        {
            Node *pre = findmax(root->lchild);
            root->v = pre->v;
            deleteNode(root->lchild, pre->v);
        }
        else if (root->rchild != NULL)
        {
            Node *post = findmin(root->rchild);
            root->v = post->v;
            deleteNode(root->rchild, post->v);
        }
    }
    else if (root->v > v)
        deleteNode(root->lchild, v);
    else if (root->v < v)
        deleteNode(root->rchild, v);
    else
    {
        cout << "wrong!" << endl;
        exit(1);
    }
}

void preorder(Node *root)
{
    if (root == NULL)
        return;
    printf("%d ", root->v);
    preorder(root->lchild);
    preorder(root->rchild);
}

int main()
{
    int n, t;
    cin >> n;
    Node *root = NULL;
    for (int i = 0; i < n; i++)
    {
        cin >> t;
        insert(root, t);
    }
    deleteNode(root, 8);
    preorder(root);
}
```

