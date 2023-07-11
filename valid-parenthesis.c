bool isValid(char* s) {
    int i = 0, top = -1, length = strlen(s); 
    char curr, stack[length], opening; 

    // Loops each char in string s
    for (i = 0; i < length; i++) {
        curr = s[i];

        // Pushes the stack with the current open bracket
        if (curr == '(' || curr == '{' || curr == '[') {
            stack[++top] = curr;
        }

        else {
            if (top == -1) {
                return false;
            }

            // Pops the opening character from the stack if brackets are valid
            opening = stack[top];
            if ((opening == '(' && curr == ')') 
            || (opening == '{' && curr == '}') 
            || (opening == '[' && curr == ']')) {
                top--; 
            }
            else {
                return false; 
            }
        }
    }

    return top == -1; 
}
