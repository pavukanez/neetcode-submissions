class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num:nums){
            map.put(nums, map.getOrDefault(num, 0) + 1);
        }

        List<Integer>[] buckets = new ArrayList[nums.length + 1];
        for(int num:map.keys()){
            int count = map.get(num);

            if (buckets[count] == null) buckets[count] = new ArrayList<>();
            buckets[count].add(num);

        }

        int[] res = new int[k];
        int pos = 0;

        for (int i=buckets.length;i>=0;i--){
            for (int num:buckets[i]){
                res[index++] = num;
                if (index == k) return res;
            }
        }
        return res;
    }
}
