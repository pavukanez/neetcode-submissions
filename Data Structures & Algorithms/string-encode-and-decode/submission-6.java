class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for (String s:strs){
            res.append(s.length()).append("#").append(s);
        }
        return res.toString();
        
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int pos = 0;
        while (pos < str.length()){
            StringBuilder strLen = new StringBuilder();
            while (!str[pos].equals("#")){
                strLen.append(str[pos++]);
            }
            String curStr = str.substring(pos + 1, pos + 1 + Integer.valueOf(strLen.toString()));
            res.add(curStr);

            pos += 1 + Integer.valueOf(strLen.toString());
        }

        return res;
    }
}
