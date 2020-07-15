screen_helper = """
#: import content stackcode.content
#: import ll_code linkedlistcode.ll_code 
#: import queue_code q_code.queue_code
#: import dll_code doublyLinkedlist.dll_code


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
    MDLabel:    
        text: content
        valign: 'middle'
        text_size: root.width, None
        size: self.texture_size
        
<DoublyLinkedList>:
    name: 'dll'
    MDRectangleFlatButton: 
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press:
            root.manager.transition.direction = 'down'
            root.manager.current = 'ds'
    MDLabel:    
        text: dll_code
        valign: 'middle'
        text_size: root.width, None 
<Queue>:
    name: 'q'
    MDRectangleFlatButton: 
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press:
            root.manager.transition.direction = 'down'
            root.manager.current = 'ds'
        
    MDLabel:    
        text: queue_code
        valign: 'middle'
        text_size: root.width, None
        size: self.texture_size

            

<LinkedList>:
    name: 'll'
    MDRectangleFlatButton: 
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press:
            root.manager.transition.direction = 'down'
            root.manager.current = 'ds'
    MDLabel:    
        text: ll_code
        valign: 'middle'
        text_size: self.size
        
"""