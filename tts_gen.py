from openai import OpenAI
from pathlib import Path

# 设置你的 OpenAI API 密钥
client = OpenAI(api_key="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")

# 要转换为语音的文本
text = """
Struggling with productivity? Meet Max AI – your ultimate AI assistant for everyday tasks!Click the Max AI icon to open the sidebar and access the world's best AI models - all in one place. With the Max AI sidebar, you can ask anything without leaving the page. Get contextual answers directly from any website, always with reliable, cited sources.
Summarize any YouTube video in seconds - no more skipping around.
 From tutorials to interviews, get the key points instantly.
 And screenshots? They're now interactive.
 Chat with anything you capture - translate, extract text, or get answers instantly.
 No typing. No lost context. Just snap and ask.Reply to emails, posts, and messages with AI - right in your browser.
Write complete, thoughtful responses in seconds, without leaving the sidebar.
Analyze the sender's intent, get smart suggestions, and insert polished drafts instantly.
 Select any text and use "Improve Writing" for clearer, more polished language.
 Make content sharper, more concise, or more professional—instantly.
 For multilingual work, translating is just as easy.
 Select the text and click "Translate" - it works seamlessly across dozens of languages.
 Whether you're writing, editing, or translating, MaxAI helps you move faster,
 with intelligent tools that appear exactly when and where you need them.Work smarter, not harder. Get Max AI for free at Max AI.co and stay ahead.
"""

# 使用 OpenAI TTS 生成语音文件
speech_file_path = Path("maxai_american_accent.mp3")
response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input=text
)
response.stream_to_file(speech_file_path)

print("✅ MP3 语音文件已生成：", speech_file_path)
