"""
QTextListFormat binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QTextFormat


class QTextListFormat(QTextFormat):
  """
  The cute side of Qt's QTextListFormat: a plain Python object standing in
  front of one C++ QTextListFormat.

  It is built on the cute 'QTextFormat', as Qt's QTextListFormat is built on
  Qt's QTextFormat, and has everything that class has.

  C++ hands a QTextListFormat around as a copy, so every C++ QTextListFormat
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextListFormat that has a ritual and that Python
  can call so far, 11 names in all: 'isValid', 'setStyle', 'style',
  'setIndent', 'indent', 'setNumberPrefix', 'numberPrefix',
  'setNumberSuffix', 'numberSuffix', 'setStart', 'start'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextListFormat::~QTextListFormat()': the destructor: Python
    removes its C++ QTextListFormat by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QTextListFormat is created at the first use, not by
    'QTextListFormat(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextListFormat back gives a copy the ritual made for
    Python, in a new cute QTextListFormat.
  """

  #  The enums Qt writes inside QTextListFormat, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Style(CuteNum):
    """
    The enum 'QTextListFormat::Style' of Qt, with the 9 names Qt gives in it.
    """

    ListDisc = Kee[int](-1)
    ListCircle = Kee[int](-2)
    ListSquare = Kee[int](-3)
    ListDecimal = Kee[int](-4)
    ListLowerAlpha = Kee[int](-5)
    ListUpperAlpha = Kee[int](-6)
    ListLowerRoman = Kee[int](-7)
    ListUpperRoman = Kee[int](-8)
    ListStyleUndefined = Kee[int](0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextListFormat'

  #  Qt's '~QTextListFormat()'. Naming it makes this a value class: Python
  #  owns every C++ QTextListFormat behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QTextListFormatD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextListFormat::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlistformat.html#isValid
    """
    #  bool QTextListFormat::isValid() const
    return self.uglySide.call('ritual_ZNK15QTextListFormat7isValidEv')

  def style(self) -> Style:
    """
    Calls Qt's 'Style QTextListFormat::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlistformat.html#style

    Returns
    -------

    Style
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Style(number)' gives.
    """
    #  Style QTextListFormat::style() const
    return QTextListFormat.Style(self.uglySide.call(
        'ritual_ZNK15QTextListFormat5styleEv',
    ))

  def indent(self) -> int:
    """
    Calls Qt's 'int QTextListFormat::indent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlistformat.html#indent
    """
    #  int QTextListFormat::indent() const
    return self.uglySide.call('ritual_ZNK15QTextListFormat6indentEv')

  def numberPrefix(self) -> str:
    """
    Calls Qt's 'QString QTextListFormat::numberPrefix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlistformat.html#numberPrefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextListFormat::numberPrefix() const
    return self.uglySide.call('ritual_ZNK15QTextListFormat12numberPrefixEv')

  def numberSuffix(self) -> str:
    """
    Calls Qt's 'QString QTextListFormat::numberSuffix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlistformat.html#numberSuffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextListFormat::numberSuffix() const
    return self.uglySide.call('ritual_ZNK15QTextListFormat12numberSuffixEv')

  def start(self) -> int:
    """
    Calls Qt's 'int QTextListFormat::start() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlistformat.html#start
    """
    #  int QTextListFormat::start() const
    return self.uglySide.call('ritual_ZNK15QTextListFormat5startEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Style)
  def setStyle(self, style: Style) -> None:
    """
    Calls Qt's 'void QTextListFormat::setStyle(Style style)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlistformat.html#setStyle

    Parameters
    ----------

    style : Style
      Passed on as its number.
    """
    #  void QTextListFormat::setStyle(Style style)
    self.uglySide.call(
        'ritual_ZN15QTextListFormat8setStyleENS_5StyleE', style.value,
    )

  @overload(int)
  def setIndent(self, indent: int) -> None:
    """
    Calls Qt's 'void QTextListFormat::setIndent(int indent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlistformat.html#setIndent

    Parameters
    ----------

    indent : int
      Passed on as it is.
    """
    #  void QTextListFormat::setIndent(int indent)
    self.uglySide.call('ritual_ZN15QTextListFormat9setIndentEi', indent)

  @overload(str)
  def setNumberPrefix(self, numberPrefix: str) -> None:
    """
    Calls Qt's 'void QTextListFormat::setNumberPrefix(const QString
    &numberPrefix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlistformat.html#setNumberPrefix

    Parameters
    ----------

    numberPrefix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextListFormat::setNumberPrefix(const QString &numberPrefix)
    self.uglySide.call(
        'ritual_ZN15QTextListFormat15setNumberPrefixERK7QString',
        numberPrefix,
    )

  @overload(str)
  def setNumberSuffix(self, numberSuffix: str) -> None:
    """
    Calls Qt's 'void QTextListFormat::setNumberSuffix(const QString
    &numberSuffix)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlistformat.html#setNumberSuffix

    Parameters
    ----------

    numberSuffix : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextListFormat::setNumberSuffix(const QString &numberSuffix)
    self.uglySide.call(
        'ritual_ZN15QTextListFormat15setNumberSuffixERK7QString',
        numberSuffix,
    )

  @overload(int)
  def setStart(self, indent: int) -> None:
    """
    Calls Qt's 'void QTextListFormat::setStart(int indent)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextlistformat.html#setStart

    Parameters
    ----------

    indent : int
      Passed on as it is.
    """
    #  void QTextListFormat::setStart(int indent)
    self.uglySide.call('ritual_ZN15QTextListFormat8setStartEi', indent)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QTextListFormat::QTextListFormat()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlistformat.html#QTextListFormat
    """
    #  QTextListFormat::QTextListFormat()
    self._noteCreation(QTextListFormat, lambda: Rituals.call(
        'ritual_ZN15QTextListFormatC1Ev',
    ))

  @overload(QTextFormat)
  def __init__(self, fmt: QTextFormat) -> None:
    """
    Notes what was given, for Qt's 'QTextListFormat::QTextListFormat(const
    QTextFormat &fmt)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextlistformat.html#QTextListFormat

    Parameters
    ----------

    fmt : QTextFormat
      Passed on as a value: Qt reads the C++ QTextFormat, which stays
      Python's own.
    """
    #  QTextListFormat::QTextListFormat(const QTextFormat &fmt)
    self._noteCreation(QTextListFormat, lambda: Rituals.call(
        'ritual_ZN15QTextListFormatC1ERK11QTextFormat', self._valueOf(fmt),
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
