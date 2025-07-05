# prompts.py

def get_parsing_prompt(user_input: str) -> str:
    return f"""你是一个文字理解助手，我将给你一段关于军训的描述，请帮我提取以下信息：
1. 发生了哪些具体事件？
2. 主要人物有哪些？
3. 存在哪些情绪和感受？
4. 请用一句话总结这段经历的主题。

输入内容如下：
{user_input}
"""

def get_reflection_prompt(parsed: str) -> str:
    return f"""你是一位善于思考和引导的导师，请根据下面的军训事件内容，进行深入反思，并用自然的语言写出一段内心感悟。

请包括以下几点：
- 这段经历给了我什么启发？
- 我从中学到了哪些关于人与人、自我或社会的东西？
- 如果这是一堂人生课程，它教会了我什么？

事件描述：
{parsed}
"""

def get_rewriting_prompt(ai_thinking: str, word_limit: str = "500") -> str:
    return f"""你是一位高中生，请将下面这段文字改写成真实、有情感、自然的军训心得。

请注意：
- 文字应具有学生的语气，避免官方或AI口吻；
- 可以加入一些个人感受、转折和生活化表达；
- 要真诚自然，不要做作或假装成熟；
- 请将整段控制在接近 {word_limit} 字左右，太长或太短都会被老师扣分。

AI原文如下：
{ai_thinking}
"""
