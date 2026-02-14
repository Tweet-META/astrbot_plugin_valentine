from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import random

@register("astrbot_plugin_valentine", "Tweet-META", "情人节抽奖", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    def draw(self):
        prob = random.random()
        if 0 <= prob <= 0.1:
            return "滚你🐎的喵！"
        elif 0.1 < prob <= 0.2:
            return "去你🐎的喵！"
        elif 0.2 < prob <= 0.3:
            return "你也配喵？"
        elif 0.3 < prob <= 0.4:
            return "啥b二次元喵！"
        elif 0.4 < prob <= 0.5:
            return "癔症又犯了喵？"
        elif 0.5 < prob <= 0.6:
            return "现在是幻想时刻喵！"
        elif 0.6 < prob <= 0.65:
            return "柚子厨滚出去喵！"
        elif 0.65 < prob <= 0.7:
            return "这是最后通牒喵！"
        elif 0.7 < prob <= 0.75:
            return "以后不要再和我扯上关系喵！"
        elif 0.75 < prob <= 0.8:
            return "（被拉黑+屏蔽）"
        elif 0.8 < prob <= 0.85:
            return "小男娘喵！"
        elif 0.85 < prob <= 0.875:
            return "（随机的网图）"
        elif 0.875 < prob <= 0.9:
            return "我一直把你当好朋友喵！"
        elif 0.9 < prob <= 0.925:
            return "（随机的贴吧圣经）"
        elif 0.925 < prob <= 0.95:
            return "下次再说吧喵！"
        elif 0.95 < prob <= 0.975:
            return "你是个好人喵！"
        elif 0.975 < prob <= 0.999:
            return "滚出去喵！"
        elif 0.999 < prob <= 0.9999:
            return "好呀宝宝喵！"
        elif 0.9999 < prob <= 1:
            return "其实我也喜欢你好久了喵...\n居然真的有人能抽到这条的喵？！！"


    @filter.command("咱俩试试")
    async def valentine(self, event: AstrMessageEvent):
        try:
            message_parts = event.message_str.split()
            if len(message_parts) >= 2 and message_parts[1].isdigit():
                num = max(1, min(int(message_parts[1]),10))
                result = ""
                for _ in range(num):
                    result += f"{self.draw()}\n"

                result = result.rstrip()
                yield event.plain_result(result)
            else:
                yield event.plain_result(self.draw())
        except Exception as e:
            logger.error("draw error: " + str(e))
            yield event.plain_result("喵？发生错误了喵！")
            return
        
    @filter.command("valentine")
    async def help_valentine(self, event: AstrMessageEvent):
        try:
            help_text = (
                "情人节限定卡池开催 \n"
                "编辑发送“/咱俩试试？”\n"
                "即有机会获得限定ssr“好呀宝宝”\n"
                "抽取日期:2026年02月14日之前\n"
                "抽奖概率公示：\n"
                "滚你🐎的喵 10%\n"
                "去你🐎的喵 10%\n"
                "你也配喵？ 10%\n"
                "啥b二次元喵！ 10%\n"
                "癔症又犯了喵？ 10%\n"
                "现在是幻想时刻喵！ 10%\n"
                "柚子厨滚出去喵！ 5%\n"
                "这是最后通牒喵！ 5%\n"
                "以后不要再和我扯上关系喵！ 5%\n"
                "（被拉黑+屏蔽） 5%\n"
                "小男娘喵！ 5%\n"
                "（随机的网图） 2.5%\n"
                "（随机的贴吧圣经） 2.5%\n"
                "下次再说吧喵！ 2.5%\n"
                "你是个好人喵！ 2.5%\n"
                "我一直把你当好朋友喵！ 2.5%\n"
                "滚出去喵！ 2.49%\n"
                "好呀宝宝喵！ 0.009%\n"
                "其实我也喜欢你好久了（隐藏款）0.001％\n"
                "*抽取概率为综合概率。\n"
            )
            yield event.plain_result(help_text)
            return
        except Exception as e:
            logger.error("draw error: " + str(e))
            yield event.plain_result("喵？发生错误了喵！")
            return