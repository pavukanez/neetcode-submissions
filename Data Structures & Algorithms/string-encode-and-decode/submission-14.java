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
            int delimiter_pos = str.indexOf("#", pos);
            int strLen = Integer.valueOf(str.substring(pos, delimiter_pos));

            pos = delimiter_pos + 1;
            res.add(str.substring(pos, pos + strLen));
        }

        return res;
    }
}
