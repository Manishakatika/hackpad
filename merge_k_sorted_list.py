class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
     # Dummy node to start the merged list
        head = point = ListNode(0)
        
        while True:
            min_index = -1
            min_value = float('inf')
            
            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_value:
                    min_value = lists[i].val
                    min_index = i
        
            if min_index == -1:
                break
           
            point.next = lists[min_index]
            point = point.next
           
            lists[min_index] = lists[min_index].next
        
        return head.next 
