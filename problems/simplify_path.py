def simplifyPath(path: str) -> str:
    #split the give string by slashes
    #initiate a stack to store the elements as by the rules
    #iterate through the split items checking appending to the stack items if rules
    #at the end join elements in stack with a slash
    path = path.split("/")
    stack = []
    
    #iterate through split elements 
    for item in path:
        if item == "" or item == ".":
            continue
        elif item == "..":
            if stack:
                stack.pop()
        else:
            stack.append(item)
    
    if stack:
        return "/" + "/".join(stack)
    else:
        return "/"
    
if __name__ == "__main__":
    path = "/home/user/Documents/../Pictures"
    print(simplifyPath(path))