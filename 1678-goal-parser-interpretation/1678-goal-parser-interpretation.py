class Solution:
    def interpret(self, command: str) -> str:
        new_String = command.replace('()','o')
        return new_String.replace('(al)','al')