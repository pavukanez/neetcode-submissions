class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num:nums){
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        // 1: 1
        // 2: 2
        // 3: 3
        List<Integer>[] buckets = new ArrayList<>()[nums.length];
        for (Map.Entry<Integer, Integer> entry: map.entrySet()){
            int count = entry.value();
            int num = entry.key();
            buckets[count].add(num);
        }
        
        int[] res = new int[k];
        int pos = 0;

        for (int i=buckets.length-1;i>=0;i--){
            for (int num:buckets[i]){
                res[pos++] = num;
                k--;
                if (k == 0){
                    return res;
                }
            }
        }
        return res;
        
    }
}
