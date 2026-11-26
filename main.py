"""
Main Tester Script
"""
#  Apache-2.0 license
#  Copyright (c) 2025-2026 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING, TypeVar
from types import FunctionType, MethodType, BuiltinFunctionType
from types import ModuleType, MemberDescriptorType
from types import WrapperDescriptorType, MethodWrapperType
from types import MethodDescriptorType, ClassMethodDescriptorType
from types import LambdaType, BuiltinMethodType

from cutienator.QtCore import QObject, QTimer
from cutienator.QtWidgets import (QApplication, QLabel, QLineEdit,
                                  QMainWindow, QPushButton, QVBoxLayout,
                                  QWidget)

try:
  from pyperclip import copy
except ImportError:
  def copy(*_) -> None:
    pass

from worktoy.desc import Field
from bin.dev_tooling.yolo_dev import runTests, runTest, yolo

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import TypeAlias, Union, Optional, Callable

  MaybeStr: TypeAlias = Optional[str]
  StrField: TypeAlias = Union[str, Field]
  Tester: TypeAlias = Callable[[], int]
  MaybeType: TypeAlias = Optional[type]

NotImplementedType = type(NotImplemented)

Func = (
    FunctionType,
    MethodType,
    BuiltinFunctionType,
    ModuleType,
    MemberDescriptorType,
    WrapperDescriptorType,
    MethodWrapperType,
    MethodDescriptorType,
    ClassMethodDescriptorType,
    LambdaType,
    BuiltinMethodType,
)

Names = (
    'FunctionType',
    'MethodType',
    'BuiltinFunctionType',
    'ModuleType',
    'MemberDescriptorType',
    'WrapperDescriptorType',
    'MethodWrapperType',
    'MethodDescriptorType',
    'ClassMethodDescriptorType',
    'LambdaType',
    'BuiltinMethodType',
)

T = TypeVar('T')


def tester00() -> int:
  """
  Hello World!
  """
  stuff = [os, sys, 'Hello world!', runTest, runTests, copy]
  list.extend(stuff, (yolo,))
  for item in stuff:
    itemStr = object.__str__(item)
    clsName = str(type(item).__name__, )
    lineSpec = """%s::%s"""
    if len(itemStr) > 48:
      itemStr = """%s...""" % (itemStr[:45],)
    else:
      itemStr = str.rjust(itemStr, 48, ' ')
    if len(clsName) > 16:
      clsName = """%s...""" % (clsName[:13])
    else:
      clsName = str.ljust(clsName, 16, ' ')
    line = lineSpec % (itemStr, clsName)
    print("""|  %64s  |""" % line)
  else:
    return 0


def tester01() -> int:
  """
  Launches a cutienator application: a main window with a label, a text
  field and a button in a layout. What is typed shows in the label, by
  Qt's own connection of 'textChanged(QString)' to 'setText(QString)';
  the button quits. A timer clicks it, so the run ends by itself.
  """
  app = QApplication(sys.argv)
  window = QMainWindow()
  window.setWindowTitle('cutienator')
  window.resize(320, 160)
  central = QWidget()
  layout = QVBoxLayout(central)
  label = QLabel('Type something')
  edit = QLineEdit()
  button = QPushButton('Quit')
  layout.addWidget(label)
  layout.addWidget(edit)
  layout.addWidget(button)
  window.setCentralWidget(central)
  QObject.connect(edit, '2textChanged(QString)', label, '1setText(QString)')
  QObject.connect(button, '2clicked()', app, '1quit()')
  window.show()
  edit.setText('Hello, cutienator')
  print('label:', label.text())
  QTimer.singleShot(10000, button, '1click()')
  return QApplication.exec()


if __name__ == '__main__':
  yolo(tester01)
