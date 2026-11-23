"""
QFontInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/qfontinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList
from . import QFont

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QFontVariableAxis


class QFontInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFontInfo: a plain Python object standing in front of
  one C++ QFontInfo.

  C++ hands a QFontInfo around as a copy, so every C++ QFontInfo behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFontInfo that has a ritual and that Python can call
  so far, 17 names in all: 'family', 'styleName', 'pixelSize', 'pointSize',
  'pointSizeF', 'italic', 'style', 'weight', 'bold', 'underline', 'overline',
  'strikeOut', 'fixedPitch', 'styleHint', 'variableAxes', 'legacyWeight',
  'exactMatch'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontInfo::~QFontInfo()': the destructor: Python removes its C++
    QFontInfo by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QFontInfo is created at the first use, not by 'QFontInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFontInfo back gives a copy the ritual made for
    Python, in a new cute QFontInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontInfo'

  #  Qt's '~QFontInfo()'. Naming it makes this a value class: Python owns
  #  every C++ QFontInfo behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QFontInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def family(self) -> str:
    """
    Calls Qt's 'QString QFontInfo::family() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#family

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontInfo::family() const
    return self.uglySide.call('ritual_ZNK9QFontInfo6familyEv')

  def styleName(self) -> str:
    """
    Calls Qt's 'QString QFontInfo::styleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#styleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontInfo::styleName() const
    return self.uglySide.call('ritual_ZNK9QFontInfo9styleNameEv')

  def pixelSize(self) -> int:
    """
    Calls Qt's 'int QFontInfo::pixelSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#pixelSize
    """
    #  int QFontInfo::pixelSize() const
    return self.uglySide.call('ritual_ZNK9QFontInfo9pixelSizeEv')

  def pointSize(self) -> int:
    """
    Calls Qt's 'int QFontInfo::pointSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#pointSize
    """
    #  int QFontInfo::pointSize() const
    return self.uglySide.call('ritual_ZNK9QFontInfo9pointSizeEv')

  def pointSizeF(self) -> float:
    """
    Calls Qt's 'qreal QFontInfo::pointSizeF() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#pointSizeF
    """
    #  qreal QFontInfo::pointSizeF() const
    return self.uglySide.call('ritual_ZNK9QFontInfo10pointSizeFEv')

  def italic(self) -> bool:
    """
    Calls Qt's 'bool QFontInfo::italic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#italic
    """
    #  bool QFontInfo::italic() const
    return self.uglySide.call('ritual_ZNK9QFontInfo6italicEv')

  def style(self) -> QFont.Style:
    """
    Calls Qt's 'QFont::Style QFontInfo::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#style

    Returns
    -------

    QFont.Style
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QFont.Style(number)'
      gives.
    """
    #  QFont::Style QFontInfo::style() const
    return QFont.Style(self.uglySide.call('ritual_ZNK9QFontInfo5styleEv'))

  def weight(self) -> int:
    """
    Calls Qt's 'int QFontInfo::weight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#weight
    """
    #  int QFontInfo::weight() const
    return self.uglySide.call('ritual_ZNK9QFontInfo6weightEv')

  def bold(self) -> bool:
    """
    Calls Qt's 'bool QFontInfo::bold() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#bold
    """
    #  bool QFontInfo::bold() const
    return self.uglySide.call('ritual_ZNK9QFontInfo4boldEv')

  def underline(self) -> bool:
    """
    Calls Qt's 'bool QFontInfo::underline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#underline
    """
    #  bool QFontInfo::underline() const
    return self.uglySide.call('ritual_ZNK9QFontInfo9underlineEv')

  def overline(self) -> bool:
    """
    Calls Qt's 'bool QFontInfo::overline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#overline
    """
    #  bool QFontInfo::overline() const
    return self.uglySide.call('ritual_ZNK9QFontInfo8overlineEv')

  def strikeOut(self) -> bool:
    """
    Calls Qt's 'bool QFontInfo::strikeOut() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#strikeOut
    """
    #  bool QFontInfo::strikeOut() const
    return self.uglySide.call('ritual_ZNK9QFontInfo9strikeOutEv')

  def fixedPitch(self) -> bool:
    """
    Calls Qt's 'bool QFontInfo::fixedPitch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#fixedPitch
    """
    #  bool QFontInfo::fixedPitch() const
    return self.uglySide.call('ritual_ZNK9QFontInfo10fixedPitchEv')

  def styleHint(self) -> QFont.StyleHint:
    """
    Calls Qt's 'QFont::StyleHint QFontInfo::styleHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#styleHint

    Returns
    -------

    QFont.StyleHint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QFont.StyleHint(number)'
      gives.
    """
    #  QFont::StyleHint QFontInfo::styleHint() const
    return QFont.StyleHint(self.uglySide.call(
        'ritual_ZNK9QFontInfo9styleHintEv',
    ))

  def variableAxes(self) -> QList[QFontVariableAxis]:
    """
    Calls Qt's 'QList<QFontVariableAxis> QFontInfo::variableAxes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#variableAxes

    Returns
    -------

    QList[QFontVariableAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QFontVariableAxis> QFontInfo::variableAxes() const
    address = self.uglySide.call('ritual_ZNK9QFontInfo12variableAxesEv')
    from . import QFontVariableAxis
    return QList[QFontVariableAxis]._cuteOwning(address)

  def legacyWeight(self) -> int:
    """
    Calls Qt's 'int QFontInfo::legacyWeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#legacyWeight
    """
    #  int QFontInfo::legacyWeight() const
    return self.uglySide.call('ritual_ZNK9QFontInfo12legacyWeightEv')

  def exactMatch(self) -> bool:
    """
    Calls Qt's 'bool QFontInfo::exactMatch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#exactMatch
    """
    #  bool QFontInfo::exactMatch() const
    return self.uglySide.call('ritual_ZNK9QFontInfo10exactMatchEv')

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

  @overload(QFont)
  def __init__(self, a0: QFont) -> None:
    """
    Notes what was given, for Qt's 'QFontInfo::QFontInfo(const QFont &a0)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#QFontInfo

    Parameters
    ----------

    a0 : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  QFontInfo::QFontInfo(const QFont &a0)
    self._noteCreation(QFontInfo, lambda: Rituals.call(
        'ritual_ZN9QFontInfoC1ERK5QFont', self._valueOf(a0),
    ))

  @overload(THIS)
  def __init__(self, a0: QFontInfo) -> None:
    """
    Notes what was given, for Qt's 'QFontInfo::QFontInfo(const QFontInfo
    &a0)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontinfo.html#QFontInfo

    Parameters
    ----------

    a0 : QFontInfo
      Passed on as a value: Qt reads the C++ QFontInfo, which stays Python's
      own.
    """
    #  QFontInfo::QFontInfo(const QFontInfo &a0)
    self._noteCreation(QFontInfo, lambda: Rituals.call(
        'ritual_ZN9QFontInfoC1ERKS_', self._valueOf(a0),
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
