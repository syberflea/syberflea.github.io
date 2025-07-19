def what_to_do(instructions):
    simon_says = "Simon says"
    cmd = instructions.strip()
    if simon_says in cmd:
        if cmd.startswith(simon_says):
            answer = cmd[len(simon_says):].strip()
            return "I " + answer
        elif cmd.endswith(simon_says):
            ind = cmd.find(simon_says)
            answer = cmd[:ind].strip()
            return "I " + answer
    else:
        return "I won't do it!"