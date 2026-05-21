class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String s:strs){
            // sort current string
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sorted_s = new String(chars);

            map.computeIfAbsent(sorted_s, k -> new ArrayList<String>()).add(s);
        }

        List<List<String>> res = new ArrayList<>();
        for (Map.Entry<int[], List<String>> entry:map.entrySet()){
            res.add(entry.getValue());
        }

        return res;
    }
}
