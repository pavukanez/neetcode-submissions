class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] pre = new int[len], post = new int[len], res = new int[len];

        for(int i=0;i<len;i++){
            pre[i] = 1;
            post[i] = 1;
        }

        for (int i=1;i<len;i++){
            pre[i] = pre[i-1] * nums[i-1];
        }

        for (int i=len-2;i>-1;i--){
            post[i] = post[i+1] * nums[i+1];
        }

        for (int i=0;i<len;i++){
            res[i] = pre[i] * post[i];
        }

        return res;
        
    }
}  
