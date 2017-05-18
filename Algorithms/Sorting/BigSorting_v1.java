import java.math.BigInteger;
import java.util.*;

public class BigSorting_v1
{
	static class Node
	{
		BigInteger data = new BigInteger("0");
		Node left;
		Node right;

		public Node(BigInteger b1)
		{
			data = b1;
			left = right = null;
		}
	}

	public static void main(String args[])
	{
		List<BigInteger> list = new ArrayList<BigInteger>();
		list.add(new BigInteger("31415926535897932384626433832795"));
		list.add(new BigInteger("1"));
		list.add(new BigInteger("3"));
		list.add(new BigInteger("10"));
		list.add(new BigInteger("3"));
		list.add(new BigInteger("5"));

		Node root = new Node(list.get(0));

		for (int i=1; i<list.size(); i++)
		{
			insertNode(list.get(i), root);
		}

		doInorderTraversal(root);
	}

	public static void insertNode(BigInteger item, Node root)
	{
		while(root != null)
		{
			if (item.compareTo(root.data) == 1)
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