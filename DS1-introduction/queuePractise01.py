# class Queue:
#     def __init__(self):
#         self.items = []
    
#     def isEmpty(self):
#         return self.items == []
    
#     def enqueue(self,item):
#         self.items.insert(0,item)

#     def dequeue(self):
#         return self.items.pop()

#     def size(self):
#         return len(self.items)


'''
平均每天10名学生在任何给定时间在实验室工作，每个学生通常在此期间打印2次
打印一次的范围1-20页   20  400     2 40     4 80
每分钟打印机可以处理10页，但打印的质量比较差
如果需要打印的质量比较好，那么打印机每分钟只能处理5页
'''
'''
    1. 创建打印任务的队列。每个任务都有个时间戳，队列启动的时候为空
    2. 是否创建新的打印任务？如果是，创建时间戳添加到队列 090101
    3. 打印机不忙并且有任务在等待：
       从打印机队列中删除一个任务并将其分配给打印机  090301
       当前时间减去创建任务的时间戳，计算该任务的等待时间  2
       将该任务的等待时间附件到列表中稍后处理
       根据打印任务的页数，确定需要多少时间
    4. 打印机需要1s打印，所以得从2分钟内-1s = 等待时间
    5. 任务完成，所需要的时间是0，打印机空闲
    模拟完成后，从生成的等待时间列表中计算平均等待时间
'''
