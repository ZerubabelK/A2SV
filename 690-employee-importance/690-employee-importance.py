"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        def dfs(node, imp):

            if not node.subordinates:    
                return node.importance
            
            for sub in node.subordinates:
                for emp in employees:
                    if emp.id == sub:
                        
                        imp += dfs(emp, emp.importance)
                        
            return imp
        
        for emp in employees:
            if emp.id == id:
                return dfs(emp, emp.importance)