# main.py

from openrouter_api import call_openrouter
from prompts import (
    get_parsing_prompt,
    get_reflection_prompt,
    get_rewriting_prompt
)

def main():
    print("📌 请输入你在军训中经历了什么：")
    user_input = input("> ")

    print("✏️ 想要生成多少字的心得？（例如：300 / 500 / 800）")
    word_limit = input("> ").strip()

    print("\n🔍 正在分析事件...")
    parsed = call_openrouter(get_parsing_prompt(user_input))
    print(f"\n🧠 AI 分析结果：\n{parsed}")

    print("\n🤔 正在进行深度思考...")
    thinking = call_openrouter(get_reflection_prompt(parsed))
    print(f"\n💬 深度思考结果：\n{thinking}")

    print("\n🎨 正在去AI化重写成自然心得...")
    final_output = call_openrouter(get_rewriting_prompt(thinking, word_limit))
    print("\n✅ 最终军训心得：\n")
    print(final_output)

if __name__ == "__main__":
    main()
