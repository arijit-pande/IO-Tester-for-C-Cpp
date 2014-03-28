#!/usr/bin/env python
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os,sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_IOTester(object):
    def setupUi(self, IOTester):
        IOTester.setObjectName(_fromUtf8("IOTester"))
        IOTester.resize(726, 641)
        self.CodeWindow = QtGui.QTextEdit(IOTester)
        self.CodeWindow.setGeometry(QtCore.QRect(50, 40, 651, 241))
        self.CodeWindow.setObjectName(_fromUtf8("CodeWindow"))
    #    self.CodeWindow.textChanged.connect(self.function)
	self.highlighter=MyHighlighter(self.CodeWindow,"Classic")
	self.Stdout = QtGui.QTextBrowser(IOTester)
        self.Stdout.setGeometry(QtCore.QRect(50, 520, 651, 71))
        self.Stdout.setObjectName(_fromUtf8("Stdout"))
        self.Stdin = QtGui.QTextEdit(IOTester)
        self.Stdin.setGeometry(QtCore.QRect(50, 410, 651, 71))
        self.Stdin.setObjectName(_fromUtf8("Stdin"))
        self.CompileLog = QtGui.QTextBrowser(IOTester)
        self.CompileLog.setGeometry(QtCore.QRect(50, 310, 651, 71))
        self.CompileLog.setObjectName(_fromUtf8("CompileLog"))
        self.CompileBtn = QtGui.QPushButton(IOTester)
        self.CompileBtn.setGeometry(QtCore.QRect(120, 610, 84, 24))
        self.CompileBtn.setObjectName(_fromUtf8("CompileBtn"))
        self.RunBtn = QtGui.QPushButton(IOTester)
        self.RunBtn.setGeometry(QtCore.QRect(230, 610, 84, 24))
        self.RunBtn.setObjectName(_fromUtf8("RunBtn"))
        self.SaveBtn = QtGui.QPushButton(IOTester)
        self.SaveBtn.setGeometry(QtCore.QRect(340, 610, 84, 24))
        self.SaveBtn.setObjectName(_fromUtf8("SaveBtn"))
        self.OpenBtn = QtGui.QPushButton(IOTester)
        self.OpenBtn.setGeometry(QtCore.QRect(440, 610, 84, 24))
        self.OpenBtn.setObjectName(_fromUtf8("OpenBtn"))
        self.label = QtGui.QLabel(IOTester)
        self.label.setGeometry(QtCore.QRect(50, 20, 111, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(IOTester)
        self.label_2.setGeometry(QtCore.QRect(50, 290, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(IOTester)
        self.label_3.setGeometry(QtCore.QRect(50, 390, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(IOTester)
        self.label_4.setGeometry(QtCore.QRect(50, 490, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
	self.CompileBtn.clicked.connect(self.compile_function)
        self.RunBtn.clicked.connect(self.run_function)
	self.OpenBtn.clicked.connect(self.open_function)
	self.SaveBtn.clicked.connect(self.save_function)
	self.retranslateUi(IOTester)
        QtCore.QMetaObject.connectSlotsByName(IOTester)
     	

    def retranslateUi(self, IOTester):
        IOTester.setWindowTitle(_translate("IOTester", "IO Tester for C/C++", None))
        self.CompileBtn.setText(_translate("IOTester", "Compile", None))
        self.RunBtn.setText(_translate("IOTester", "Run", None))
        self.SaveBtn.setText(_translate("IOTester", "Save", None))
        self.OpenBtn.setText(_translate("IOTester", "Open", None))
        self.label.setText(_translate("IOTester", "Code Window", None))
        self.label_2.setText(_translate("IOTester", "Compile Log", None))
        self.label_3.setText(_translate("IOTester", "Stdin", None))
        self.label_4.setText(_translate("IOTester", "Stdout", None))
    
    def compile_function(self):
    	self.x=str(self.CodeWindow.toPlainText())
	self.text_file=open(".temp.c","w")
	self.text_file.write(self.x);
	self.text_file.close()
	os.system("bash compile_script.sh")
	self.text_file=open(".compile.log","r")
	self.x=self.text_file.read()
	self.text_file.close()
	self.CompileLog.setPlainText(self.x)
	os.system("bash flush_script.sh")
    
    def run_function(self):
    	self.x=str(self.Stdin.toPlainText())
	self.text_file=open(".input","w")
	self.text_file.write(self.x)
	self.text_file.close()
	os.system("bash run_script.sh")
    	self.text_file=open(".output","r")
	self.x=self.text_file.read()
	self.text_file.close()
	self.Stdout.setPlainText(self.x)
	os.system("bash flush_script.sh")
	self.text_file=open("logfile","r")
	self.x=self.text_file.read()
	self.text_file.close()
	QtGui.QMessageBox.about(None,"Message","Submission Report:"+self.x)
	os.system("echo \"\"> logfile")

        
    
    def open_function(self):
        self.fname = QtGui.QFileDialog.getOpenFileName(IOTester, 'Open file', 
                '/home')
	if(self.fname==''):
		return;
        self.f = open(self.fname, 'r')
        self.data = self.f.read()
	self.f.close()
	self.CodeWindow.setText(self.data)
    def save_function(self):
    	self.fname=QtGui.QFileDialog.getSaveFileName(IOTester,'Save File','/home')
	if self.fname=='':
		return #do nothing
	self.data=str(self.CodeWindow.toPlainText())
	self.f=open(self.fname,'w')
	self.f.write(self.data)
	self.f.close()

class MyHighlighter( QSyntaxHighlighter ):

    def __init__( self, parent, theme ):
      QSyntaxHighlighter.__init__( self, parent )
      self.parent = parent
      keyword = QTextCharFormat()
      assignmentOperator = QTextCharFormat()
      delimiter = QTextCharFormat()
      specialConstant = QTextCharFormat()
      number = QTextCharFormat()
      header = QTextCharFormat()
      string = QTextCharFormat()
      singleLineComment=QTextCharFormat()
      multiLineComment=QTextCharFormat() #this would be a rather complicated regex- still working on it :P
      self.highlightingRules = []

      # keyword
      brush = QBrush( Qt.darkBlue, Qt.SolidPattern )
      keyword.setForeground( brush )
      keyword.setFontWeight( QFont.Bold )
      keywords = QStringList( [ "break", "else", "for", "if", "int","float","double","long","short","signed","unsigned","sizeof","typedef" 
                                 "return", "switch","return","case","struct","union" 
                                "try", "while","void","char","volatile","register","auto","true","false","goto","do","static","extern"] )
      for word in keywords:
        pattern = QRegExp("\\b" + word + "\\b")
        rule = HighlightingRule( pattern, keyword )
        self.highlightingRules.append(rule)

      # delimiter
      pattern = QRegExp( "[\)\(]+|[\{\}]+|[][]+" )
      delimiter.setForeground( brush )
      delimiter.setFontWeight( QFont.Bold )
      rule = HighlightingRule( pattern, delimiter )
      self.highlightingRules.append( rule )

      # specialConstant
      brush = QBrush( Qt.yellow, Qt.SolidPattern )
      specialConstant.setForeground( brush )
      keywords = QStringList( [ "NULL" ] )
      for word in keywords:
        pattern = QRegExp("\\b" + word + "\\b")
        rule = HighlightingRule( pattern, specialConstant )
        self.highlightingRules.append( rule )


      # header files
      brush = QBrush( Qt.blue, Qt.SolidPattern )
      pattern = QRegExp( "#[^\n]*" )
      header.setForeground( brush )
      rule = HighlightingRule( pattern, header )
      self.highlightingRules.append( rule )

      
      # string
      brush = QBrush( Qt.red, Qt.SolidPattern )
      pattern = QRegExp( "\".*\"" )
      string.setForeground( brush )
      rule = HighlightingRule( pattern, string )
      self.highlightingRules.append( rule )
      
      #single line comment
      brush=QBrush(Qt.darkGreen,Qt.SolidPattern)
      pattern=QRegExp("//[^\n]*")
      singleLineComment.setForeground(brush)
      rule=HighlightingRule(pattern,singleLineComment)
      self.highlightingRules.append(rule)

      #multi line comment
      brush=QBrush(Qt.darkRed,Qt.SolidPattern)
      pattern=QRegExp("/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/")
      multiLineComment.setForeground(brush)
      rule=HighlightingRule(pattern,multiLineComment)
      self.highlightingRules.append(rule)


    def highlightBlock( self, text ):
      for rule in self.highlightingRules:
        expression = QRegExp( rule.pattern )
        index = expression.indexIn( text )
        while index >= 0:
          length = expression.matchedLength()
          self.setFormat( index, length, rule.format )
          index = text.indexOf( expression, index + length )
      self.setCurrentBlockState( 0 )


class HighlightingRule():
  def __init__( self, pattern, format ):
    self.pattern = pattern
    self.format = format
 

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    IOTester=QtGui.QWidget()
    ui=Ui_IOTester()
    ui.setupUi(IOTester)
    IOTester.show()
    sys.exit(app.exec_())
