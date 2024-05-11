class Solution {

    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        $in = (string)$x;
        return $in==strrev($in)?  true: false;
    }
}