"""
QtParseCommon::ParsedText binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qtparsecommon_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QtParseCommon::ParsedText to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute


class ParsedText(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtParseCommon::ParsedText: a plain Python object
  standing in front of one C++ QtParseCommon::ParsedText.

  C++ hands a QtParseCommon::ParsedText around as a copy, so every C++
  QtParseCommon::ParsedText behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtParseCommon::ParsedText that has a ritual and that
  Python can call so far, 4 names in all: '__bool__', 'isEmpty', 'size',
  'used'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtParseCommon::ParsedText::~ParsedText()': the destructor: Python
    removes its C++ QtParseCommon::ParsedText by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ QtParseCommon::ParsedText is created at the first use, not by
    'QtParseCommon::ParsedText(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtParseCommon::ParsedText back gives a copy the
    ritual made for Python, in a new cute QtParseCommon::ParsedText.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtParseCommon::ParsedText'

  #  Qt's '~QtParseCommon::ParsedText()'. Naming it makes this a value class:
  #  Python owns every C++ QtParseCommon::ParsedText behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN13QtParseCommon10ParsedTextD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QtParseCommon::ParsedText::isEmpty() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtparsecommon-parsedtext.html#isEmpty
    """
    #  bool QtParseCommon::ParsedText::isEmpty() const
    return self.uglySide.call(
        'ritual_ZNK13QtParseCommon10ParsedText7isEmptyEv',
    )

  def size(self) -> int:
    """
    Calls Qt's 'qsizetype QtParseCommon::ParsedText::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtparsecommon-parsedtext.html#size
    """
    #  qsizetype QtParseCommon::ParsedText::size() const
    return self.uglySide.call('ritual_ZNK13QtParseCommon10ParsedText4sizeEv')

  @overload(str)
  def used(self, text: str) -> str:
    """
    Calls Qt's 'QStringView QtParseCommon::ParsedText::used(QStringView text)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtparsecommon-parsedtext.html#used

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QtParseCommon::ParsedText::used(QStringView text) const
    return self.uglySide.call(
        'ritual_ZNK13QtParseCommon10ParsedText4usedE11QStringView', text,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __bool__(self) -> bool:
    """
    Calls Qt's 'bool QtParseCommon::ParsedText::operator bool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtparsecommon-parsedtext.html#operator bool
    """
    #  bool QtParseCommon::ParsedText::operator bool() const
    return self.uglySide.call('ritual_ZNK13QtParseCommon10ParsedTextcvbEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
