"""
QColorOutput binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qcoloroutput_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QColorOutput to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QColorOutput(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorOutput: a plain Python object standing in front
  of one C++ QColorOutput.

  What exists
  -----------

  Every function of Qt's QColorOutput that has a ritual and that Python can
  call so far, 8 names in all: 'isSilent', 'setSilent', 'insertMapping',
  'writeUncolored', 'write', 'colorify', 'flushBuffer', 'discardBuffer'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorOutput::~QColorOutput()': the destructor: Python never
    removes a C++ QColorOutput.
  - Qt's 'void QColorOutput::writePrefixedMessage(const QString &message,
    QtMsgType type, const QString &prefix)': names the enum 'QtMsgType',
    whose class cannot be named here.

  What has no ritual
  ------------------

  5 of the 16 functions Qt declares: 4 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QColorOutput is created at the first use, not by
    'QColorOutput(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QColorOutput.
  - Each name of Qt's QColorOutput that has no cute function yet,
    'writePrefixedMessage', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QColorOutput, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ColorCodeComponent(CuteFlags):
    """
    The flags enum 'QColorOutput::ColorCodeComponent' of Qt, with the 24
    names Qt gives in it. Qt names the type of its combinations
    'QColorOutput::ColorCode'.
    """

    BlackForeground = 0x400
    BlueForeground = 0x800
    GreenForeground = 0xc00
    CyanForeground = 0x1000
    RedForeground = 0x1400
    PurpleForeground = 0x1800
    BrownForeground = 0x1c00
    LightGrayForeground = 0x2000
    DarkGrayForeground = 0x2400
    LightBlueForeground = 0x2800
    LightGreenForeground = 0x2c00
    LightCyanForeground = 0x3000
    LightRedForeground = 0x3400
    LightPurpleForeground = 0x3800
    YellowForeground = 0x3c00
    WhiteForeground = 0x4000
    BlackBackground = 0x100000
    BlueBackground = 0x200000
    GreenBackground = 0x300000
    CyanBackground = 0x400000
    RedBackground = 0x500000
    PurpleBackground = 0x600000
    BrownBackground = 0x700000
    DefaultColor = 0x100000

  ColorCode = ColorCodeComponent

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorOutput'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isSilent(self) -> bool:
    """
    Calls Qt's 'bool QColorOutput::isSilent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloroutput.html#isSilent
    """
    #  bool QColorOutput::isSilent() const
    return self.uglySide.call('ritual_ZNK12QColorOutput8isSilentEv')

  @overload(str)
  @overload(str, int)
  def colorify(self, message: str, color: int = -1) -> str:
    """
    Calls Qt's 'QString QColorOutput::colorify(QStringView message, int
    color) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloroutput.html#colorify

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    color : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QColorOutput::colorify(QStringView message, int color) const
    return self.uglySide.call(
        'ritual_ZNK12QColorOutput8colorifyE11QStringViewi', message, color,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setSilent(self, silent: bool) -> None:
    """
    Calls Qt's 'void QColorOutput::setSilent(bool silent)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloroutput.html#setSilent

    Parameters
    ----------

    silent : bool
      Passed on as it is.
    """
    #  void QColorOutput::setSilent(bool silent)
    self.uglySide.call('ritual_ZN12QColorOutput9setSilentEb', silent)

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
    Notes what was given, for Qt's 'QColorOutput::QColorOutput()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcoloroutput.html#QColorOutput
    """
    #  QColorOutput::QColorOutput()
    self._noteCreation(QColorOutput, lambda: Rituals.call(
        'ritual_ZN12QColorOutputC1Ev',
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

  @overload(int, ColorCode)
  def insertMapping(self, colorID: int, colorCode: ColorCode) -> None:
    """
    Calls Qt's 'void QColorOutput::insertMapping(int colorID, ColorCode
    colorCode)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloroutput.html#insertMapping

    Parameters
    ----------

    colorID : int
      Passed on as it is.

    colorCode : ColorCode
      Passed on as its number.
    """
    #  void QColorOutput::insertMapping(int colorID, ColorCode colorCode)
    self.uglySide.call(
        'ritual_ZN12QColorOutput13insertMappingEi6QFlagsINS_18ColorCodeComp'
        'onentEE',
        colorID, colorCode.value,
    )

  @overload(str)
  def writeUncolored(self, message: str) -> None:
    """
    Calls Qt's 'void QColorOutput::writeUncolored(const QString &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloroutput.html#writeUncolored

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QColorOutput::writeUncolored(const QString &message)
    self.uglySide.call(
        'ritual_ZN12QColorOutput14writeUncoloredERK7QString', message,
    )

  @overload(str)
  @overload(str, int)
  def write(self, message: str, color: int = -1) -> None:
    """
    Calls Qt's 'void QColorOutput::write(const QStringView message, int
    color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloroutput.html#write

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    color : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QColorOutput::write(const QStringView message, int color)
    self.uglySide.call(
        'ritual_ZN12QColorOutput5writeE11QStringViewi', message, color,
    )

  def flushBuffer(self) -> None:
    """
    Calls Qt's 'void QColorOutput::flushBuffer()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloroutput.html#flushBuffer
    """
    #  void QColorOutput::flushBuffer()
    self.uglySide.call('ritual_ZN12QColorOutput11flushBufferEv')

  def discardBuffer(self) -> None:
    """
    Calls Qt's 'void QColorOutput::discardBuffer()'.

    Qt's own words: https://doc.qt.io/qt-6/qcoloroutput.html#discardBuffer
    """
    #  void QColorOutput::discardBuffer()
    self.uglySide.call('ritual_ZN12QColorOutput13discardBufferEv')

  @staticmethod
  def writePrefixedMessage(*__, **_) -> Never:
    """
    Qt's 'void QColorOutput::writePrefixedMessage(const QString &message,
    QtMsgType type, const QString &prefix)': names the enum 'QtMsgType',
    whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QColorOutput.writePrefixedMessage' has no cute function yet. Qt's "
        "'void QColorOutput::writePrefixedMessage(const QString &message, "
        "QtMsgType type, const QString &prefix)': names the enum "
        "'QtMsgType', whose class cannot be named here.")
