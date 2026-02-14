from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import random

@register("astrbot_plugin_valentine", "Tweet-META", "情人节抽奖", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("咱俩试试")
    async def valentine(self, event: AstrMessageEvent):
        try:
            prob = random.random()
            if 0 <= prob <= 0.1:
                yield event.plain_result("滚你🐎的喵！")
                return
            
            if 0.1 < prob <= 0.2:
                yield event.plain_result("去你🐎的喵！")
                return
            
            if 0.2 < prob <= 0.3:
                yield event.plain_result("你也配喵？")
                return

            if 0.3 < prob <= 0.4:
                yield event.plain_result("啥b二次元喵！")
                return
            
            if 0.4 < prob <= 0.5:
                yield event.plain_result("癔症又犯了喵？")
                return

            if 0.5 < prob <= 0.6:
                yield event.plain_result("现在是幻想时刻喵！")
                return
            
            if 0.6 < prob <= 0.65:
                yield event.plain_result("柚子厨滚出去喵！")
                return

            if 0.65 < prob <= 0.7:
                yield event.plain_result("这是最后通牒喵！")
                return
            
            if 0.7 < prob <= 0.75:
                yield event.plain_result("以后不要再和我扯上关系喵！")
                return

            if 0.75 < prob <= 0.8:
                yield event.plain_result("（被拉黑+屏蔽）")
                return
            
            if 0.8 < prob <= 0.85:
                yield event.plain_result("小男娘喵！")
                return
            
            if 0.85 < prob <= 0.875:
                yield event.plain_result("（随机的网图）")
                return
            
            if 0.875 < prob <= 0.9:
                yield event.plain_result("我一直把你当好朋友喵！")
                return
            
            if 0.9 < prob <= 0.925:
                yield event.plain_result("（随机的贴吧圣经）")
                return

            if 0.925 < prob <= 0.95:
                yield event.plain_result("下次再说吧喵！")
                return
            
            if 0.95 < prob <= 0.975:
                yield event.plain_result("你是个好人喵！")
                return

            if 0.975 < prob <= 0.999:
                yield event.plain_result("滚出去喵！")
                return
            
            if 0.999 < prob <= 0.9999:
                yield event.plain_result("好呀宝宝喵！")
                return
            
            if 0.9999 < prob <= 1:
                yield event.plain_result("其实我也喜欢你好久了喵...")
                yield event.plain_result("居然真的有人能抽到这条的喵？！！")
                return

        except Exception as e:
            logger.error("draw error: " + str(e))
            yield event.plain_result("喵？发生错误了喵！")
            return
        
    @filter.command("valentine")
    async def help_valentine(self, event: AstrMessageEvent):
        try:
            help_text = {
                "情人节限定卡池开催 \n"
                "编辑发送“/咱俩试试？”\n"
                "即有机会获得限定ssr“好呀宝宝”\n"
    
                "抽取日期:2026年02月14日之前\n"
    
                "抽奖概率公示：\n"
                "滚你吗的喵 10%\n"
                "去你吗的喵 10%\n"
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
            }
            yield event.plain_result(help_text)
            return
        except Exception as e:
            logger.error("draw error: " + str(e))
            yield event.plain_result("喵？发生错误了喵！")
            return
