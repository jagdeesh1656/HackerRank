import java.io.*;
import java.math.BigInteger;
import java.util.*;

public class Solution {

    static class Node
	{
		String data;
		Node left;
		Node right;

		public Node(String b1)
		{
			data = b1;
			left = right = null;
		}
	}
    public static boolean compare(String s0, String s1){
        if (s0.length() > s1.length()) return true;
        else if (s0.length() < s1.length()) return false;
        else{
            String arr[] = {s0, s1};
            Arrays.sort(arr);
            if (arr[0].equals(s0)) return false;
            else return true;
        }
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        String[] unsorted = new String[n];
        for(int unsorted_i=0; unsorted_i < n; unsorted_i++){
            unsorted[unsorted_i] = in.next();
        }
        Node root = new Node(unsorted[0]);
        for (int i=1; i<unsorted.length; i++)
				{
					insertNode(unsorted[i], root);
				}
			doInorderTraversal(root);
    }
	public static void insertNode(String item, Node root)
	{
		while(root != null)
		{
			if (compare(item, root.data))
			{
				if (root.right == null)
				{
					root.right = new Node(item);
					return;
				}
				else
					root = root.right;
			}
			else
			{
				if (root.left == null)
				{
					root.left = new Node(item);
					return;
				}
				else
					root = root.left;
			}
		}
	}

	public static void doInorderTraversal(Node root)
	{
		if (root == null)
			return;
		doInorderTraversal(root.left);
		System.out.println(root.data + "");
		doInorderTraversal(root.right);
	}
}
