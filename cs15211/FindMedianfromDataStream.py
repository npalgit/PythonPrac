__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/find-median-from-data-stream.py
# Time:  O(nlogn) for total n addNums, O(logn) per addNum, O(1) per findMedian.
# Space: O(n), total space

# Median is the middle value in an ordered integer list.
# If the size of the list is even, there is no middle value.
# So the median is the mean of the two middle value.
#
# Examples:
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# For example:
#
# add(1)
# add(2)
# findMedian() -> 1.5
# add(3)
# findMedian() -> 2
# Google
#Heap design

# Heap solution.
from heapq import heappush, heappop

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__max_heap = []
        self.__min_heap = []


    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        # Balance smaller half and larger half.
        if not self.__max_heap or num > -self.__max_heap[0]:
            heappush(self.__min_heap, num)
            if len(self.__min_heap) > len(self.__max_heap) + 1:
                heappush(self.__max_heap, -heappop(self.__min_heap))
        else:
            heappush(self.__max_heap, -num)
            if len(self.__max_heap) > len(self.__min_heap):
                heappush(self.__min_heap, -heappop(self.__max_heap))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        return (-self.__max_heap[0] + self.__min_heap[0]) / 2.0 \
                if len(self.__max_heap) == len(self.__min_heap) \
                else self.__min_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

from heapq import heappush, heappop, heapify
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
        self.median = 0.0
        self.ttl = 0

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.minHeap) == 0:
            self.minHeap.append(num)
        else:
            if num > self.median:
                heappush(self.minHeap, num)
            else:
                heappush(self.maxHeap, -num)
        self.ttl += 1
        self.shuffle()
        self.setMedian()

    def shuffle(self):
        while abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            if len(self.minHeap) > len(self.maxHeap):
                heappush(self.maxHeap, -heappop(self.minHeap))
            else:
                heappush(self.minHeap, -heappop(self.maxHeap))

    def setMedian(self):
        if self.ttl % 2 == 1:
            self.median = self.minHeap[0] if len(self.minHeap) > len(self.maxHeap) else -self.maxHeap[0]
        else:
            fir = self.minHeap[0]
            sec = -self.maxHeap[0]
            self.median = (fir + sec) / 2.0

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        return float(self.median)

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()

#java
js = '''
class MedianFinder {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

    // Adds a number into the data structure.
    public void addNum(int num) {
        if(maxHeap.size() == 0 || num < maxHeap.peek()){
            maxHeap.offer(num);
        }else{
            minHeap.offer(num);
        }
        shuffle();
    }
    private void shuffle(){
        if(Math.abs(maxHeap.size() - minHeap.size()) <= 1) {
            return;
        }else if(maxHeap.size() > minHeap.size()){
            minHeap.offer(maxHeap.poll());
        }else{
            maxHeap.offer(minHeap.poll());
        }
    }

    // Returns the median of current data stream
    public double findMedian() {
        if(maxHeap.size() == minHeap.size()){
            return (double)(maxHeap.peek() + minHeap.peek()) / 2;
        }else if(maxHeap.size() > minHeap.size()){
            return (double) maxHeap.peek();
        }else{
            return (double) minHeap.peek();
        }
    }
};

// Your MedianFinder object will be instantiated and called as such:
// MedianFinder mf = new MedianFinder();
// mf.addNum(1);
// mf.findMedian();


class MedianFinder {
    private PriorityQueue<Integer> minHeap;
    private PriorityQueue<Integer> maxHeap;
    private double median;

    public MedianFinder() {
        minHeap = new PriorityQueue<>();
        maxHeap = new PriorityQueue<>(10, Collections.reverseOrder());
    }

    // Adds a number into the data structure.
    public void addNum(int num) {
        if (minHeap.isEmpty()) {
            minHeap.add(num);
            median = num;
            return;
        }
        if (num > median) {
            minHeap.add(num);
            if (minHeap.size() - maxHeap.size() > 1) {
                maxHeap.add(minHeap.poll());
            }
        } else {
            maxHeap.add(num);
            if (maxHeap.size() - minHeap.size() > 1) {
                minHeap.add(maxHeap.poll());
            }
        }
        if (((maxHeap.size() + minHeap.size()) & 1) == 1) {
            median = maxHeap.size() > minHeap.size() ? maxHeap.peek() : minHeap.peek();
        } else {
            median = ((double) maxHeap.peek() + minHeap.peek()) / 2;
        }
    }

    // Returns the median of current data stream
    public double findMedian() {
        return median;
    }
};

// Your MedianFinder object will be instantiated and called as such:
// MedianFinder mf = new MedianFinder();
// mf.addNum(1);
// mf.findMedian();

class MedianFinder {
    private PriorityQueue<Integer> minHeap;
    private PriorityQueue<Integer> maxHeap;
    private int ttl;
    private double median;

    public MedianFinder(){
        minHeap = new PriorityQueue<Integer>();
        maxHeap = new PriorityQueue<Integer>();
        //maxHeap = new PriorityQueue<Integer>(Collections.reverseORder());
        ttl = 0;
        median = -1;
    }

    // Adds a number into the data structure.
    public void addNum(int num) {
        if(ttl == 0){
            minHeap.offer(num);
        }else{
            if(num < median){
                maxHeap.offer(-num);
            }else{
                minHeap.offer(num);
            }
        }

        while(Math.abs(minHeap.size() - maxHeap.size()) > 1){
            if(minHeap.size() > maxHeap.size()){
                maxHeap.offer(-minHeap.poll());
            }else{
                minHeap.offer(-maxHeap.poll());
            }
        }
        ttl++;
        setMedian();
    }

    private void setMedian(){
        if(ttl % 2 == 1){
            if(minHeap.size() > maxHeap.size()){
                median = minHeap.peek();
            }else{
                median = -maxHeap.peek();
            }
        }else{
            int fir = minHeap.peek();
            int sec = -maxHeap.peek();
            median = (double) (fir + sec) / 2;
        }
    }

    // Returns the median of current data stream
    public double findMedian() {
        return median;
    }
};
'''