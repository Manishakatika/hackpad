
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list1=[]
        curr=head
        while curr:
            list1.append(curr.val)
            curr=curr.next
        for i in range(0,len(list1),k):
            if i+k<=len(list1):
                list1[i:i+k]=reversed(list1[i:i+k])
        dummy=ListNode(0)
        curr=dummy
        for x in list1:
            curr.next=ListNode(x)
            curr=curr.next
        return dummy.next
