# 从任意一个字符串开始，扫描该字符串，依次检查其他字符串的同一位置是否是一样的字符，当遇到不一样时则返回当前得到的前缀。
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        res = ''
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res