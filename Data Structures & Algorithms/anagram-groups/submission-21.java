class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();

        for (String s:strs){
            String sortedStr = Arrays.sort(s.toCharArray()).toString();
            map.computeIfAbsent(sortedStr, k -> new ArrayList<>()).append(s);
        }

        return new ArrayList<>(map.keys());
    }
}
