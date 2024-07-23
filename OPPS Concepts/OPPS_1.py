# define the mobile object
# class is nothing but blue print
# instance is nothing but object which means actions and attributes like model,camera,make call is the actions

class Mobile:
    def __init__(self,model,cameras,face_locaks):
        self.model = model
        self.cameras = cameras
        self.face_locaks = face_locaks

    # Actions methods
    def make_call(self,number):
        print('Calling... {}'.format(number))
        return
    def play_game(self,game):
        print('Playing... {}'.format(game))
        return
    def capture_photo(self,photo):
        print('Capturing... {}'.format(photo))
        return
    

# instance methods

mobile_object=Mobile('Apple 14','64 MP',True)
print(mobile_object.make_call(29384989199))
print(mobile_object.play_game('freefire'))