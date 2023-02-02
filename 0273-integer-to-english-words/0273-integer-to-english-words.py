class Solution:
    def numberToWords(self, num: int) -> str:
        table_one = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
        table_two = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
        
        ten_more = {10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen',16:'Sixteen',17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
        
        def helper(c, i):
            if i == 0:
                return table_one[int(c)] if c != '0' else ''
            elif i == 1:
                return table_two[int(c)] if c != '0' else ''
            else:
                return table_one[int(c)] + ' ' + 'Hundred' if c != '0' else ''
        
        def convert(s, i):
            res_s = ''
            j=0
            for k in range(len(s)):
                if k == 1 and s[k]=='1':
                    res_s = ten_more[int(s[0:2][::-1])]
                else:
                    sol = helper(s[k],j)
                    if sol != '':
                        res_s = sol if res_s =='' else sol + ' ' + res_s 
                j+=1
        
            if not res_s:
                return ''
                
            if i == 1:
                res_s = res_s + ' ' + 'Thousand'
            elif i == 2:
                res_s = res_s + ' ' + 'Million'
            elif i == 3:
                res_s = res_s + ' ' + 'Billion'
            return res_s
                  
        rs = str(num)[::-1]
        i = step = 0
        final = ''
        while (i<len(rs)):
            j = min(i+3, len(rs))
            sol=convert(rs[i:j], step)
            
            if sol:
                final=sol if final=='' else sol + ' '+ final
            
            step += 1
            i = j
        
        return 'Zero' if not final else final