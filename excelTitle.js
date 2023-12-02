 
 /*
    A 3 lettered columnNumber 'n' can be represented as,        
        n = (excel_symbol_value_2) x 26^2 + (excel_symbol_value_1) x 26^1 + (excel_symbol_value_0) x 26^0
        n = (base_26_symbol_value_2 + 1) x 26^2 + (base_26_symbol_value_1 + 1) x 26^1 + (base_26_symbol_value_0 + 1) x 26^0
        Notice how an excel_symbol_value is 1 more than its corresponding base_26_symbol_value, 
        i.e. A's value in excel system = (base_26_symbol_value('A') + 1) 
                                       = (0 + 1)
                                       = 1
 
        In the base 26 system, a symbol_value maps to a symbol as follows:
            0 -> A
            1 -> B
            ...
           25 -> Z
        To extract base_26_symbol_value_0, subtract 1 from both sides:
        n - 1 = (base_26_symbol_value_2 + 1) x 26^2 + (base_26_symbol_value_1 + 1) x 26^1 + (base_26_symbol_value_0 + 1) x 26^0 - 1
        n - 1 = (base_26_symbol_value_2 + 1) x 26^2 + (base_26_symbol_value_1 + 1) x 26^1 + (base_26_symbol_value_0 + 1) x 1 - 1
        n - 1 = (base_26_symbol_value_2 + 1) x 26^2 + (base_26_symbol_value_1 + 1) x 26^1 + (base_26_symbol_value_0 + 1 - 1)
        n - 1 = (base_26_symbol_value_2 + 1) x 26^2 + (base_26_symbol_value_1 + 1) x 26^1 + (base_26_symbol_value_0 + 1)
 
        Now take mod 26 on both sides
        (n - 1) % 26 = base_26_symbol_value_0
 
        To remove base_26_symbol_value_0's contribution, divide by 26 on both sides,
        (n - 1) / 26 = ((base_26_symbol_value_2 + 1) x 26^2 + (base_26_symbol_value_1 + 1) x 26^1 + (base_26_symbol_value_0 + 1)) / 26
                     =  (base_26_symbol_value_2 + 1) x 26^1 + (base_26_symbol_value_1 + 1) x 26^0 + 0
                     =  (base_26_symbol_value_2 + 1) x 26^1 + (base_26_symbol_value_1 + 1)
        Extract base_26_symbol_value_1 similarly to how base_26_symbol_value_0 was calculated and repeat 
        until all base_26_symbol_values have been extracted.
*/

/* neetcode explanation
    notice how AA is 27. If we went from 0-25, then AA would be 0. In this representation there is no way for us to have any leading
    zeroes. If we went from 0-25 then AA would be the same as AAAAA, but in out case it's not. 

    notice that 26*26 = 676. For 0-25, This would be BAA. For 1-26 this would be YZ. The reason 1-26 can get more numbers out of 2 digits
    is that 0-25 has repeat numbers when the leading digit is A.
*/
 
 let base = 'A'.charCodeAt(0);
var convertToTitle = function(columnNumber) {
    // AABZ
    let ans = '';
    let num = columnNumber;
    while(num !== 0 ){
        num--;
        let ones = num % 26;
        // if(ones === 0) {
        //     ones = 26
        //     num--;
        // }
        let char = String.fromCharCode(base + ones);
        ans = char+ans;
        num = Math.floor(num/26);
    }
    return ans;
};