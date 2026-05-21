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
            // find first occurence of delimiter # starting from current pos
            int delimiter_pos = str.indexOf("#", pos);

            // extract current string length
            int strLen = Integer.valueOf(str.substring(pos, delimiter_pos));

            res.add(str.substring(delimiter_pos + 1, delimiter_pos + 1 + strLen));

            pos = delimiter_pos + 1 + strLen;
        }

        return res;
    }
}
