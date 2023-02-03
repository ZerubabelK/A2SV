class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split('/')
        print(directories)
        for directory in directories:
            if directory == '.' or directory == '':
                continue
            elif directory == '..':
                stack.pop() if stack else None
            else:
                stack.append('/' + directory)
        if not stack:
            return '/'
        return ''.join(stack)