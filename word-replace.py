from docx import Document

#read in Document
document = Document('ShaunB_CV_Template.docx')


def WordReplace(document, dictionary):

    for p in document.paragraphs:
        inline = p.runs
        for i in range(len(inline)):
            text = inline[i].text
            if text in dic.keys():
                text = text.replace(text, dic[text])
                inline[i].text = text


def GetInput():
    job = input("Job Name: ")
    comp = input("Comp Name: ")
    dic = {'JOBNAME': job, 'COMPNAME': comp}
    return dic


# Read in user Input then replace template words
dic = GetInput()
WordReplace(document, dic)

# Saving Document
document.save('ShaunB_CV_' + dic["JOBNAME"] + '.docx')
