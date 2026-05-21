class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        
        for (String s:strs){
            // sort current string
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);

            // if key not in map yet -> map key: new List -> add current string to list
            map.computeIfAbsent(sortedStr, k -> new ArrayList<String>()).add(s);
        }

        return new ArrayList<>(map.values());
    }
}
