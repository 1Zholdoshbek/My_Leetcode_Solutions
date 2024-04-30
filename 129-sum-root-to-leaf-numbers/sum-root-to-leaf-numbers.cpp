class Solution {
public:

    void inorder(TreeNode* root, long  num, long & sum){
        if(!root) return;

        num+=root->val;
        if(!root->left && !root->right)sum+=num;

        inorder(root->left,num*10,sum);
        inorder(root->right,num*10,sum);
    }
    int sumNumbers(TreeNode* root) {
        ios_base::sync_with_stdio(false), cin.tie(NULL), cout.tie(NULL);

        long num=0,sum=0;
        inorder(root,num,sum);
        return sum;
    }
};