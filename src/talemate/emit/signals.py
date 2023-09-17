from blinker import signal

SystemMessage = signal("system")
NarratorMessage = signal("narrator")
CharacterMessage = signal("character")
PlayerMessage = signal("player")
DirectorMessage = signal("director")

ClearScreen = signal("clear_screen")

RequestInput = signal("request_input")
ReceiveInput = signal("receive_input")

ClientStatus = signal("client_status")
AgentStatus = signal("agent_status")
ClientBootstraps = signal("client_bootstraps") 

RemoveMessage = signal("remove_message")

SceneStatus = signal("scene_status")
CommandStatus = signal("command_status")
WorldState = signal("world_state")
ArchivedHistory = signal("archived_history")

MessageEdited = signal("message_edited")

handlers = {
    "system": SystemMessage,
    "narrator": NarratorMessage,
    "character": CharacterMessage,
    "player": PlayerMessage,
    "director": DirectorMessage,
    "request_input": RequestInput,
    "receive_input": ReceiveInput,
    "client_status": ClientStatus,
    "agent_status": AgentStatus,
    "client_bootstraps": ClientBootstraps,
    "clear_screen": ClearScreen,
    "remove_message": RemoveMessage,
    "scene_status": SceneStatus,
    "command_status": CommandStatus,
    "world_state": WorldState,
    "archived_history": ArchivedHistory,
    "message_edited": MessageEdited,
}