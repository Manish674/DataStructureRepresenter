screen_helper = """
ScreenManager:
    DsSelecter:
    Stack:
    Queue:
    LinkedList:
    DoublyLinkedList:

<DsSelecter>:
    name: 'ds'
    MDRectangleFlatButton:
        text: 'Stack'
        pos_hint: {'center_x': 0.5, 'center_y':0.5} 
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'stack'
    MDRectangleFlatButton:
        text: 'Queue'
        pos_hint: {'center_x': 0.5, 'center_y':0.4} 
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'q'
    MDRectangleFlatButton:
        text: 'Doubly Linked LIst'
        pos_hint: {'center_x': 0.5, 'center_y':0.3}
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'dll' 
    MDRectangleFlatButton:
        text: 'Linked List'
        pos_hint: {'center_x': 0.5, 'center_y':0.2} 
        on_press: 
            root.manager.transition.direction = 'up'
            root.manager.current = 'll'
<Stack>:
    name: 'stack'
    MDRectangleFlatButton: 
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: 
            root.manager.transition.direction = 'down'
            root.manager.current = 'ds'
    
<DoublyLinkedList>:
    name: 'dll'
    MDRectangleFlatButton: 
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press:
            root.manager.transition.direction = 'down'
            root.manager.current = 'ds'

<Queue>:
    name: 'q'
    MDRectangleFlatButton: 
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press:
            root.manager.transition.direction = 'down'
            root.manager.current = 'ds'

<LinkedList>:
    name: 'll'
    MDRectangleFlatButton: 
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press:
            root.manager.transition.direction = 'down'
            root.manager.current = 'ds'

"""