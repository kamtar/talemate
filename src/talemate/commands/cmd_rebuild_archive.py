import asyncio

from talemate.commands.base import TalemateCommand
from talemate.commands.manager import register


@register
class CmdRebuildArchive(TalemateCommand):
    """
    Command class for the 'rebuild_archive' command
    """

    name = "rebuild_archive"
    description = "Rebuilds the archive of the scene"
    aliases = ["rebuild"]

    async def run(self):
        summarizer = self.scene.get_helper("summarizer")

        if not summarizer:
            self.system_message("No summarizer found")
            return True

        self.scene.archived_history = []

        while True:
            more = await summarizer.agent.build_archive(self.scene)

            if not more:
                break

        await asyncio.sleep(0)