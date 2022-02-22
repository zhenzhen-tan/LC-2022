class Solution(object):
    def longestCommonPrefix(self, strs: list[str]):

        if strs is None or len(strs) == 0:
            return ''

        def is_common(prefix, strs):
            return all(str.startswith(prefix) for str in strs)

        ans = ''
        for i in range(len(strs[0])):
            pre = strs[0][:i + 1]
            print(pre)
            if is_common(pre, strs):
                ans = pre
            else:
                break
        print(ans)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["flower","flow","flight"]))
