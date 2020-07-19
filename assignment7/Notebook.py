# title
# page_number 총 몇장인지, 1페이지부터 시작
# 노트 자체를 저장하기 위한 공간 필요

class NoteBook(object):
    def __init__(self,title):
        self.title=title
        self.page_number = 0
        self.notes = {}
        
    def add_note(self,note,page=0):
        if self.page_number <= 300:
            if page == 0:
                # page 입력 없을때는 뒤에 삽입
                self.notes[self.page_number]=note
                self.page_number += 1
            else:
                if page in self.notes.keys():
                    print("해당 페이지에는 이미 노트가 존재합니다.")
                else:
                    # page 입력 직접 했을 때
                    self.notes[page] = note
                    self.page_number += 1
        else:
            print("페이지가 모두 채워졌다.")
            
    def remove_note(self,page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않는다.")
            
    def get_number_of_all_pages(self):
        return len(self.notes.keys())
    def get_number_of_all_characters(self):
        temp = 0
        for v in self.notes.values():
            temp+= len(v.contents.replace(" ",""))
        return temp
    
    
class Note(object):
    def __init__(self,contents=None):
        self.contents=contents
        self.isremoved=0
    def write_contents(self,contents):
        self.isremoved = 0
        self.contents = contents
    def remove_all(self):
        self.contents=""
        self.isremoved=1
    def __str__(self):
        if self.isremoved == 1:
            print("삭제된 노트입니다.")
        return self.contents