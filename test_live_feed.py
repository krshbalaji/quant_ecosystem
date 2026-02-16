from core.live_feed_engine import LiveFeedEngine
from core.paper_engine import PaperEngine
import time

feed = LiveFeedEngine()
paper = PaperEngine()

feed.subscribe(paper.on_tick)

feed.connect()

time.sleep(30)

feed.stop()
