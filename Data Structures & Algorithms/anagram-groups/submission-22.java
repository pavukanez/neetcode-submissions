class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();

        for (String s:strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sortedStr = new String(chars);
            
            map.computeIfAbsent(sortedStr, k -> new ArrayList<>()).add(s);
        }

        return new ArrayList<>(map.values());
    }
}
