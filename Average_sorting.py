# coding: utf-8
'''======import_list========
    
    Text_handle'''
import Text_handle

class Average_sorting(object):
    """docstring for Average_sorting"""
    def __init__(self, widenum, textdir):
        super(Average_sorting, self).__init__()
        self.widenum = int(widenum)
        self.textdir = textdir
        self.success_list=[] #Meet the requirements of the combined group
        self.b_split=[]
        self.max_min=[]  #Max ad min volue save var;[function_name : max_min_mark]
    
    def max_min_mark(self):
        self.max_min=[]
        for i in self.b_split:
            length=len(i)
            self.max_min.append(length)

    def del_list_value(self,list1,list2,n):
        del list1[n]
        del list2[n]
        #Each time run get max_min
        self.max_min_mark()

    def merger_group(self):
        result = ''
        textlines = open(self.textdir,'r').readlines()
        textlines = Text_handle.del_BL(textlines)
        textlines = Text_handle.judge_key(textlines)
        for i in xrange(0,len(textlines)):
            if len(textlines[i])>self.widenum:
                    self.b_split.append(textlines[i])
            else:
                if len('%s%s ' % (result, textlines[i].replace('\n','')))>self.widenum:
                    self.success_list.append('%s\n' % result)
                    result = '' # Empty result
                    result = '%s ' % textlines[i].replace('\n','') # The remaining save to results
                else:
                    result = '%s%s ' % (result, textlines[i].replace('\n',''))

    def best_value(self):
        self.merger_group()
        self.max_min_mark()
        if len(self.max_min) != 0:
            min_value=self.max_min.index(min(self.max_min))
            while len(self.max_min) != 1:
                print 'Every line widenum_list: %s' % self.max_min
                max_value=self.max_min.index(max(self.max_min))
                print 'list max_seat:  %s min_seat:  %s' % (max_value,min_value)
                if len(self.b_split[max_value])+len(self.b_split[min_value])>self.widenum:
                    self.success_list.append(self.b_split[max_value])
                    self.del_list_value(self.max_min,self.b_split,max_value)
                    print "Single"
                else:
                    textlines = self.b_split[max_value].replace('\n','')+' '+self.b_split[min_value]
                    self.del_list_value(self.max_min,self.b_split,max_value)
                    min_value=self.max_min.index(min(self.max_min))
                    self.del_list_value(self.max_min,self.b_split,min_value)
                    min_value=self.max_min.index(min(self.max_min))
                    print "Double"
                    while len(textlines)<self.widenum:
                        print "textlines ++"
                        if len(textlines)+len(self.b_split[min_value])>self.widenum:
                            print 'textlines is "%d" near %d, break' % (len(textlines),self.widenum)
                            break
                        else:
                            textlines = textlines+self.b_split[min_value]
                            self.del_list_value(self.max_min,self.b_split,min_value)
                            min_value=self.max_min.index(min(self.max_min))
                    self.success_list.append(textlines+'\n')
                min_value=self.max_min.index(min(self.max_min))
            
            print 'list end:  %d ' % len(self.b_split[0])
            self.success_list.append(self.b_split[0])
        return self.success_list



def wide_line(widenum, textdir):
    '''You want lines width.

        widenum = lines width(Word-wide)
        textdir = read files path'''
    if widenum == '': widenum = 35
    asg = Average_sorting(widenum, textdir)
    success_list = asg.best_value()
    return success_list

def group_line(linesum,files):
    '''You want to merge several lines

            linesum = several lines?
            files = a list'''
    n=0
    group_list = []
    files = Text_handle.del_BL(files)
    files = Text_handle.judge_key(files)
    file_lines = len(files)
    while file_lines>linesum:
        line = ''
        for x in xrange(0,linesum):
            line = '%s%s ' % (line,files[n].replace('\n',''))
            n+=1
        group_list.append('%s\n' % line)
        file_lines -= linesum
    group_list.append(files[n])
    return group_list,linesum


if __name__ == '__main__':
    textdir = 'd:/name.txt'
    success_list = wide_line(35, textdir)
    path = raw_input('save_filename:')
    Text_handle.wlist(success_list,path)
