class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function myAtoi($s) {
        $i = intval(str_replace('e','.',$s));

        if($i< -2147483648) return -2147483648;
        elseif($i> 2147483647) return 2147483647;
        return $i;
    }
}