from typing import Optional

#importing classes
import tcod.event

#import sublclasses from actions
from actions import Action, EscapeAction, MovementAction

#Creating a subclass of tcods EventDispatch class
class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

        #method recieves key presses and will return either an action sublass or none
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key ==tcod.event.K_UP:
                action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
                action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
                action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
                action = MovementAction(dx=1, dy=0)

        elif key ==tcod.event.K_ESCAPE:
            action = EscapeAction()

            # No valid key was pressed
        return action