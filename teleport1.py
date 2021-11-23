from pynput import keyboard
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
def on_press(key):
    try:
        print('Alphanumeric key pressed: {0} '.format(
            key.char))
        entities=mc.getPlayerEntityIds()
        if(key.char=="Z"):
            tpentity=entities[0]
            print(tpentity)
            for i in range(100):
                mc.player.setPos(mc.player.getPos())
            #mc.postToChat("BOO!")
        elif(key.char=="X"):
            tpentity=entities[1]
            print(tpentity)
            mc.player.setPos(mc.entity.getPos(tpentity))
            #mc.postToChat("BOO!")
        elif(key.char=="C"):
            tpentity=entities[2]
            print(tpentity)
            mc.player.setPos(mc.entity.getPos(tpentity))
            #mc.postToChat("BOO!")
        elif(key.char=="V"):
            tpentity=entities[3]
            print(tpentity)
            mc.player.setPos(mc.entity.getPos(tpentity))
            #mc.postToChat("BOO!")
        elif(key.char=="B"):
            tpentity=entities[4]
            print(tpentity)
            mc.player.setPos(mc.entity.getPos(tpentity))
            #mc.postToChat("BOO!")
        elif(key.char=="N"):
            tpentity=entities[5]
            print(tpentity)
            mc.player.setPos(mc.entity.getPos(tpentity))
            #mc.postToChat("BOO!")
        elif(key.char=="M"):
            #tpentity=entities[5]
            #print(tpentity)
            px, py, pz = mc.player.getPos()
            mc.player.setPos.Y(py+2)

    except AttributeError:
        print('special key pressed: {0}'.format(
            key))

def on_release(key):
    #print('Key released: {0}'.format(
    #    key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
