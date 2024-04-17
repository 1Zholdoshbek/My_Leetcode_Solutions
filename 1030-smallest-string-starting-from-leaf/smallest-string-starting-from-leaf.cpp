class Solution {
private:
    string smallest = "~"; 
    string alphabet = "abcdefghijklmnopqrstuvwxyz";

    void helper(TreeNode* root, string path) {
        if (!root) return;

       
        path = alphabet[root->val] + path;

        if (!root->left && !root->right) {
            smallest = min(smallest, path);
        }

        helper(root->left, path);
        helper(root->right, path);
    }

public:
    string smallestFromLeaf(TreeNode* root) {
        helper(root, "");
        return smallest;
    }
};
