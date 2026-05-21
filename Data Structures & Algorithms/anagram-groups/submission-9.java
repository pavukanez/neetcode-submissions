class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<int[], List<String>> map = new HashMap<>();
        for (String s:strs){
            int[] count = new int[26];
            for (char c:s.toCharArray()){
                count[c - 'a']++;
            }
            map.computeIfAbsent(count, k -> new ArrayList<String>()).add(s);
        }
        List<List<String>> res = new ArrayList<>();
        for (Map.Entry<int[], List<String>> entry:map.entrySet()){
            res.add(entry.getValue());

        }

        return res;
    }
}
