"""
QGlyphRun binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qglyphrun.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QRectF
  from . import QRawFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRawFont = WAIT['QRawFont']
  QRectF = WAIT['QRectF']


class QGlyphRun(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGlyphRun: a plain Python object standing in front of
  one C++ QGlyphRun.

  C++ hands a QGlyphRun around as a copy, so every C++ QGlyphRun behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGlyphRun that has a ritual and that Python can call
  so far, 21 names in all: 'rawFont', 'setRawFont', 'clear', '__eq__',
  '__ne__', 'setOverline', 'overline', 'setUnderline', 'underline',
  'setStrikeOut', 'strikeOut', 'setRightToLeft', 'isRightToLeft', 'setFlag',
  'setFlags', 'flags', 'setBoundingRect', 'boundingRect', 'setSourceString',
  'sourceString', 'isEmpty'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGlyphRun::~QGlyphRun()': the destructor: Python removes its C++
    QGlyphRun by it, and has no other use for it.

  What has no ritual
  ------------------

  13 of the 37 functions Qt declares: 10 takes or gives a type that cannot be
  passed yet; 3 private.

  What to expect
  --------------

  - The C++ QGlyphRun is created at the first use, not by 'QGlyphRun(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGlyphRun back gives a copy the ritual made for
    Python, in a new cute QGlyphRun.
  """

  #  The enums Qt writes inside QGlyphRun, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class GlyphRunFlag(CuteFlags):
    """
    The flags enum 'QGlyphRun::GlyphRunFlag' of Qt, with the 5 names Qt gives
    in it. Qt names the type of its combinations 'QGlyphRun::GlyphRunFlags'.
    """

    Overline = 0x1
    Underline = 0x2
    StrikeOut = 0x4
    RightToLeft = 0x8
    SplitLigature = 0x10

  GlyphRunFlags = GlyphRunFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGlyphRun'

  #  Qt's '~QGlyphRun()'. Naming it makes this a value class: Python owns
  #  every C++ QGlyphRun behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QGlyphRunD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def rawFont(self) -> QRawFont:
    """
    Calls Qt's 'QRawFont QGlyphRun::rawFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#rawFont

    Returns
    -------

    QRawFont
      A new cute QRawFont around the copy Qt gave back. Python owns it.
    """
    #  QRawFont QGlyphRun::rawFont() const
    address = self.uglySide.call('ritual_ZNK9QGlyphRun7rawFontEv')
    from . import QRawFont
    return QRawFont._cuteOwning(address)

  def overline(self) -> bool:
    """
    Calls Qt's 'bool QGlyphRun::overline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#overline
    """
    #  bool QGlyphRun::overline() const
    return self.uglySide.call('ritual_ZNK9QGlyphRun8overlineEv')

  def underline(self) -> bool:
    """
    Calls Qt's 'bool QGlyphRun::underline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#underline
    """
    #  bool QGlyphRun::underline() const
    return self.uglySide.call('ritual_ZNK9QGlyphRun9underlineEv')

  def strikeOut(self) -> bool:
    """
    Calls Qt's 'bool QGlyphRun::strikeOut() const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#strikeOut
    """
    #  bool QGlyphRun::strikeOut() const
    return self.uglySide.call('ritual_ZNK9QGlyphRun9strikeOutEv')

  def isRightToLeft(self) -> bool:
    """
    Calls Qt's 'bool QGlyphRun::isRightToLeft() const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#isRightToLeft
    """
    #  bool QGlyphRun::isRightToLeft() const
    return self.uglySide.call('ritual_ZNK9QGlyphRun13isRightToLeftEv')

  def flags(self) -> GlyphRunFlags:
    """
    Calls Qt's 'GlyphRunFlags QGlyphRun::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#flags

    Returns
    -------

    GlyphRunFlags
      The value standing for the combination Qt gave back.
    """
    #  GlyphRunFlags QGlyphRun::flags() const
    return QGlyphRun.GlyphRunFlags(self.uglySide.call(
        'ritual_ZNK9QGlyphRun5flagsEv',
    ))

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGlyphRun::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGlyphRun::boundingRect() const
    address = self.uglySide.call('ritual_ZNK9QGlyphRun12boundingRectEv')
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def sourceString(self) -> str:
    """
    Calls Qt's 'QString QGlyphRun::sourceString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#sourceString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGlyphRun::sourceString() const
    return self.uglySide.call('ritual_ZNK9QGlyphRun12sourceStringEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QGlyphRun::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#isEmpty
    """
    #  bool QGlyphRun::isEmpty() const
    return self.uglySide.call('ritual_ZNK9QGlyphRun7isEmptyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRawFont)
  def setRawFont(self, rawFont: QRawFont) -> None:
    """
    Calls Qt's 'void QGlyphRun::setRawFont(const QRawFont &rawFont)'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#setRawFont

    Parameters
    ----------

    rawFont : QRawFont
      Passed on as a value: Qt reads the C++ QRawFont, which stays Python's
      own.
    """
    #  void QGlyphRun::setRawFont(const QRawFont &rawFont)
    self.uglySide.call(
        'ritual_ZN9QGlyphRun10setRawFontERK8QRawFont',
        self._valueOf(rawFont),
    )

  @overload(bool)
  def setOverline(self, overline: bool) -> None:
    """
    Calls Qt's 'void QGlyphRun::setOverline(bool overline)'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#setOverline

    Parameters
    ----------

    overline : bool
      Passed on as it is.
    """
    #  void QGlyphRun::setOverline(bool overline)
    self.uglySide.call('ritual_ZN9QGlyphRun11setOverlineEb', overline)

  @overload(bool)
  def setUnderline(self, underline: bool) -> None:
    """
    Calls Qt's 'void QGlyphRun::setUnderline(bool underline)'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#setUnderline

    Parameters
    ----------

    underline : bool
      Passed on as it is.
    """
    #  void QGlyphRun::setUnderline(bool underline)
    self.uglySide.call('ritual_ZN9QGlyphRun12setUnderlineEb', underline)

  @overload(bool)
  def setStrikeOut(self, strikeOut: bool) -> None:
    """
    Calls Qt's 'void QGlyphRun::setStrikeOut(bool strikeOut)'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#setStrikeOut

    Parameters
    ----------

    strikeOut : bool
      Passed on as it is.
    """
    #  void QGlyphRun::setStrikeOut(bool strikeOut)
    self.uglySide.call('ritual_ZN9QGlyphRun12setStrikeOutEb', strikeOut)

  @overload(bool)
  def setRightToLeft(self, on: bool) -> None:
    """
    Calls Qt's 'void QGlyphRun::setRightToLeft(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#setRightToLeft

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QGlyphRun::setRightToLeft(bool on)
    self.uglySide.call('ritual_ZN9QGlyphRun14setRightToLeftEb', on)

  @overload(GlyphRunFlag)
  @overload(GlyphRunFlag, bool)
  def setFlag(self, flag: GlyphRunFlag, enabled: bool = True) -> None:
    """
    Calls Qt's 'void QGlyphRun::setFlag(GlyphRunFlag flag, bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#setFlag

    Parameters
    ----------

    flag : GlyphRunFlag
      Passed on as its number.

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QGlyphRun::setFlag(GlyphRunFlag flag, bool enabled)
    self.uglySide.call(
        'ritual_ZN9QGlyphRun7setFlagENS_12GlyphRunFlagEb',
        flag.value, enabled,
    )

  @overload(GlyphRunFlags)
  def setFlags(self, flags: GlyphRunFlags) -> None:
    """
    Calls Qt's 'void QGlyphRun::setFlags(GlyphRunFlags flags)'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#setFlags

    Parameters
    ----------

    flags : GlyphRunFlags
      Passed on as its number.
    """
    #  void QGlyphRun::setFlags(GlyphRunFlags flags)
    self.uglySide.call(
        'ritual_ZN9QGlyphRun8setFlagsE6QFlagsINS_12GlyphRunFlagEE',
        flags.value,
    )

  @overload(QRectF)
  def setBoundingRect(self, boundingRect: QRectF) -> None:
    """
    Calls Qt's 'void QGlyphRun::setBoundingRect(const QRectF &boundingRect)'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#setBoundingRect

    Parameters
    ----------

    boundingRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QGlyphRun::setBoundingRect(const QRectF &boundingRect)
    self.uglySide.call(
        'ritual_ZN9QGlyphRun15setBoundingRectERK6QRectF',
        self._valueOf(boundingRect),
    )

  @overload(str)
  def setSourceString(self, sourceString: str) -> None:
    """
    Calls Qt's 'void QGlyphRun::setSourceString(const QString
    &sourceString)'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#setSourceString

    Parameters
    ----------

    sourceString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QGlyphRun::setSourceString(const QString &sourceString)
    self.uglySide.call(
        'ritual_ZN9QGlyphRun15setSourceStringERK7QString', sourceString,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QGlyphRun) -> bool:
    """
    Calls Qt's 'bool QGlyphRun::operator==(const QGlyphRun &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#operator==

    Parameters
    ----------

    other : QGlyphRun
      Passed on as a value: Qt reads the C++ QGlyphRun, which stays Python's
      own.
    """
    #  bool QGlyphRun::operator==(const QGlyphRun &other) const
    return self.uglySide.call(
        'ritual_ZNK9QGlyphRuneqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QGlyphRun) -> bool:
    """
    Calls Qt's 'bool QGlyphRun::operator!=(const QGlyphRun &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#operator!=

    Parameters
    ----------

    other : QGlyphRun
      Passed on as a value: Qt reads the C++ QGlyphRun, which stays Python's
      own.
    """
    #  bool QGlyphRun::operator!=(const QGlyphRun &other) const
    return self.uglySide.call(
        'ritual_ZNK9QGlyphRunneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QGlyphRun::QGlyphRun()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#QGlyphRun
    """
    #  QGlyphRun::QGlyphRun()
    self._noteCreation(QGlyphRun, lambda: Rituals.call(
        'ritual_ZN9QGlyphRunC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QGlyphRun) -> None:
    """
    Notes what was given, for Qt's 'QGlyphRun::QGlyphRun(const QGlyphRun
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#QGlyphRun

    Parameters
    ----------

    other : QGlyphRun
      Passed on as a value: Qt reads the C++ QGlyphRun, which stays Python's
      own.
    """
    #  QGlyphRun::QGlyphRun(const QGlyphRun &other)
    self._noteCreation(QGlyphRun, lambda: Rituals.call(
        'ritual_ZN9QGlyphRunC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QGlyphRun::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qglyphrun.html#clear
    """
    #  void QGlyphRun::clear()
    self.uglySide.call('ritual_ZN9QGlyphRun5clearEv')
