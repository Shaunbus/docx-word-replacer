from docx import Document


document = Document('ShaunB_CV_Template.docx')

# Dictionary of keys
dic = {'JOBNAME': 'Test', 'COMPNAME': 'zain'}


for p in document.paragraphs:
    inline = p.runs
    for i in range(len(inline)):
        text = inline[i].text
        if text in dic.keys():
            text = text.replace(text, dic[text])
            inline[i].text = text

document.save('new.docx')
