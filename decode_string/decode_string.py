class Solution:
    def decodeString(self, s: str) -> str:
        print(s.split("\d"))

        return ""


print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("2[abc]3[cd]ef"))
