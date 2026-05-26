class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String s:strs){
            sb.append(s.length()).append("#").append(s);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int pos = 0;

        while (pos < str.length()){
            int dividerPos = str.indexOf("#", pos);
            int strLen = Integer.valueOf(str.substring(pos, dividerPos));
            String s = str.substring(dividerPos + 1, dividerPos + 1 + strLen);
            
            res.add(s);

            pos = dividerPos + 1 + strLen;
        }
        return res;
    }
}
