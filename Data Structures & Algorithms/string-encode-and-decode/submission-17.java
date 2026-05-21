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

            // extract substring length
            int strLen = Integer.valueOf(str.substring(pos, delimiter_pos));

            // extract the substring and add to res
            res.add(str.substring(delimiter_pos + 1, delimiter_pos + 1 + strLen));

            // move pos to first index of next "string length"
            pos = delimiter_pos + 1 + strLen;
        }

        return res;
    }
}
