class Solution {
    public boolean isOper(String s){
        return (s.equals("*")||s.equals("/")||s.equals("-")||s.equals("+"));
    }
    public Integer solve(Integer a, Integer b, String op){
        switch(op){
            case "+":
                return a+b;
            case "-":
                return a-b;
            case "*":
                return a*b;
            case "/":
                return a/b;
        } return a+b;
    }
    public int evalRPN(String[] tokens) {
        Integer a;
        Integer b;
        Integer s = 1;
        Stack<Integer> stack = new Stack<>();
        stack.push(Integer.parseInt(tokens[0]));
        while (s!=tokens.length){
            while(!isOper(tokens[s])){
                stack.push(Integer.parseInt(tokens[s]));
                s++;
            } 
            if (isOper(tokens[s])){
                b = stack.pop();
                a = stack.pop();
                stack.push(solve(a,b,tokens[s]));
                s++;
            }
        }
        return stack.pop();
    }
}