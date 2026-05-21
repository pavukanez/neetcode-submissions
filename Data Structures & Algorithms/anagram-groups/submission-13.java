class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for (String s:strs){
            // sort current string
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sorted_s = new String(chars);

            // init new ArrayList if key not found, add current string to list, update map
            map.computeIfAbsent(sorted_s, k -> new ArrayList<String>()).add(s);
        }

        return new ArrayList<>(map.values());
    }
}
