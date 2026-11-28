"""
QXmlParseException binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QXmlParseException(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlParseException: a plain Python object standing in
  front of one C++ QXmlParseException.

  C++ hands a QXmlParseException around as a copy, so every C++
  QXmlParseException behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QXmlParseException that has a ritual and that Python
  can call so far, 5 names in all: 'columnNumber', 'lineNumber', 'publicId',
  'systemId', 'message'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlParseException::~QXmlParseException()': the destructor: Python
    removes its C++ QXmlParseException by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QXmlParseException is created at the first use, not by
    'QXmlParseException(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QXmlParseException back gives a copy the ritual made
    for Python, in a new cute QXmlParseException.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlParseException'

  #  Qt's '~QXmlParseException()'. Naming it makes this a value class: Python
  #  owns every C++ QXmlParseException behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QXmlParseExceptionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def columnNumber(self) -> int:
    """
    Calls Qt's 'int QXmlParseException::columnNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlparseexception.html#columnNumber
    """
    #  int QXmlParseException::columnNumber() const
    return self.uglySide.call(
        'ritual_ZNK18QXmlParseException12columnNumberEv',
    )

  def lineNumber(self) -> int:
    """
    Calls Qt's 'int QXmlParseException::lineNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlparseexception.html#lineNumber
    """
    #  int QXmlParseException::lineNumber() const
    return self.uglySide.call('ritual_ZNK18QXmlParseException10lineNumberEv')

  def publicId(self) -> str:
    """
    Calls Qt's 'QString QXmlParseException::publicId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlparseexception.html#publicId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlParseException::publicId() const
    return self.uglySide.call('ritual_ZNK18QXmlParseException8publicIdEv')

  def systemId(self) -> str:
    """
    Calls Qt's 'QString QXmlParseException::systemId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlparseexception.html#systemId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlParseException::systemId() const
    return self.uglySide.call('ritual_ZNK18QXmlParseException8systemIdEv')

  def message(self) -> str:
    """
    Calls Qt's 'QString QXmlParseException::message() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlparseexception.html#message

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlParseException::message() const
    return self.uglySide.call('ritual_ZNK18QXmlParseException7messageEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(str)
  @overload(str, int)
  @overload(str, int, int)
  @overload(str, int, int, str)
  @overload(str, int, int, str, str)
  def __init__(
      self,
      name: str = '',
      c: int = -1,
      l: int = -1,
      p: str = '',
      s: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's
    'QXmlParseException::QXmlParseException(const QString &name, int c, int
    l, const QString &p, const QString &s)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlparseexception.html#QXmlParseException

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    c : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    l : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    p : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    s : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QXmlParseException::QXmlParseException(const QString &name, int c, int
    #      l, const QString &p, const QString &s)
    self._noteCreation(QXmlParseException, lambda: Rituals.call(
        'ritual_ZN18QXmlParseExceptionC1ERK7QStringiiS2_S2_',
        name, c, l, p, s,
    ))

  @overload(THIS)
  def __init__(self, other: QXmlParseException) -> None:
    """
    Notes what was given, for Qt's
    'QXmlParseException::QXmlParseException(const QXmlParseException
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlparseexception.html#QXmlParseException

    Parameters
    ----------

    other : QXmlParseException
      Passed on as a value: Qt reads the C++ QXmlParseException, which stays
      Python's own.
    """
    #  QXmlParseException::QXmlParseException(const QXmlParseException
    #      &other)
    self._noteCreation(QXmlParseException, lambda: Rituals.call(
        'ritual_ZN18QXmlParseExceptionC1ERKS_', self._valueOf(other),
    ))

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
