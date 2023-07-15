class AVLTree<T extends Comparable<T>> {
    private AVLNode<T> root;

    public AVLNode<T> getRoot() {
        return root;
    }

    public void insert(T value) {
        if (root == null) {
            root = new AVLNode<>(value);
        } else {
            root = root.insert(value);
        }
    }

    public void delete(T value) {
        if (root != null) {
            root = root.delete(value);
        }
    }
}

class AVLNode<T extends Comparable<T>> {
    private T value;
    private AVLNode<T> left;
    private AVLNode<T> right;
    private int height;

    public AVLNode(T value) {
        this.value = value;
        this.height = 1;
    }

    public T getValue() {
        return value;
    }

    public AVLNode<T> getLeft() {
        return left;
    }

    public AVLNode<T> getRight() {
        return right;
    }

    public int getHeight() {
        return height;
    }

    public AVLNode<T> insert(T value) {
        if (value.compareTo(this.value) < 0) {
            left = (left == null) ? new AVLNode<>(value) : left.insert(value);
        } else if (value.compareTo(this.value) > 0) {
            right = (right == null) ? new AVLNode<>(value) : right.insert(value);
        } else {
            // Duplicate values are not allowed in AVL tree
            return this;
        }

        updateHeight();
        return balance();
    }

    private void updateHeight() {
        int leftHeight = (left == null) ? 0 : left.getHeight();
        int rightHeight = (right == null) ? 0 : right.getHeight();
        height = 1 + Math.max(leftHeight, rightHeight);
    }

    private AVLNode<T> balance() {
        int balanceFactor = getBalanceFactor();
        if (balanceFactor > 1) {
            if (right != null && right.getBalanceFactor() < 0) {
                right = right.rotateRight();
            }
            return rotateLeft();
        } else if (balanceFactor < -1) {
            if (left != null && left.getBalanceFactor() > 0) {
                left = left.rotateLeft();
            }
            return rotateRight();
        }
        return this;
    }

    private int getBalanceFactor() {
        int leftHeight = (left == null) ? 0 : left.getHeight();
        int rightHeight = (right == null) ? 0 : right.getHeight();
        return rightHeight - leftHeight;
    }

    private AVLNode<T> rotateLeft() {
        AVLNode<T> newRoot = right;
        right = newRoot.left;
        newRoot.left = this;

        updateHeight();
        newRoot.updateHeight();

        return newRoot;
    }

    private AVLNode<T> rotateRight() {
        AVLNode<T> newRoot = left;
        left = newRoot.right;
        newRoot.right = this;

        updateHeight();
        newRoot.updateHeight();

        return newRoot;
    }

    public AVLNode<T> delete(T value) {
        if (value.compareTo(this.value) < 0) {
            if (left != null) {
                left = left.delete(value);
            }
        } else if (value.compareTo(this.value) > 0) {
            if (right != null) {
                right = right.delete(value);
            }
        } else {
            if (left == null && right == null) {
                return null;
            } else if (left == null) {
                return right;
            } else if (right == null) {
                return left;
            } else {
                AVLNode<T> successor = findMinNode(right);
                this.value = successor.value;
                right = right.delete(successor.value);
            }
        }

        updateHeight();
        return balance();
    }

    private AVLNode<T> findMinNode(AVLNode<T> node) {
        while (node.left != null) {
            node = node.left;
        }
        return node;
    }
}
