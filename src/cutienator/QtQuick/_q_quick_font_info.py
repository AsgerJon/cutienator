"""
QQuickFontInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickfontinfo_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickFontInfo to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQuickFontEnums

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont, QFontVariableAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFontInfo(QObject):
  """
  The cute side of Qt's QQuickFontInfo: a plain Python object standing in
  front of one C++ QQuickFontInfo.

  It is built on the cute 'QObject', as Qt's QQuickFontInfo is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFontInfo that has a ritual and that Python can
  call so far, 15 names in all: 'metaObject', 'tr', 'font', 'setFont',
  'family', 'styleName', 'pixelSize', 'pointSize', 'italic', 'weight',
  'bold', 'fixedPitch', 'style', 'variableAxes', 'fontChanged'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFontInfo::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickFontInfo::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickFontInfo::~QQuickFontInfo()': the destructor: Python never
    removes a C++ QQuickFontInfo.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFontInfo is created at the first use, not by
    'QQuickFontInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFontInfo.
  - Qt tells when it has removed the C++ QQuickFontInfo. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickFontInfo::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFontInfo::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickFontInfo2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFontInfo'

  #  A C++ QQuickFontInfo Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickFontInfo'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFontInfo::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFontInfo::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickFontInfo10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickFontInfo::font() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickFontInfo::font() const
    address = self.uglySide.call('ritual_ZNK14QQuickFontInfo4fontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def family(self) -> str:
    """
    Calls Qt's 'QString QQuickFontInfo::family() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#family

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFontInfo::family() const
    return self.uglySide.call('ritual_ZNK14QQuickFontInfo6familyEv')

  def styleName(self) -> str:
    """
    Calls Qt's 'QString QQuickFontInfo::styleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#styleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFontInfo::styleName() const
    return self.uglySide.call('ritual_ZNK14QQuickFontInfo9styleNameEv')

  def pixelSize(self) -> int:
    """
    Calls Qt's 'int QQuickFontInfo::pixelSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#pixelSize
    """
    #  int QQuickFontInfo::pixelSize() const
    return self.uglySide.call('ritual_ZNK14QQuickFontInfo9pixelSizeEv')

  def pointSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickFontInfo::pointSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#pointSize
    """
    #  qreal QQuickFontInfo::pointSize() const
    return self.uglySide.call('ritual_ZNK14QQuickFontInfo9pointSizeEv')

  def italic(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontInfo::italic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#italic
    """
    #  bool QQuickFontInfo::italic() const
    return self.uglySide.call('ritual_ZNK14QQuickFontInfo6italicEv')

  def weight(self) -> int:
    """
    Calls Qt's 'int QQuickFontInfo::weight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#weight
    """
    #  int QQuickFontInfo::weight() const
    return self.uglySide.call('ritual_ZNK14QQuickFontInfo6weightEv')

  def bold(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontInfo::bold() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#bold
    """
    #  bool QQuickFontInfo::bold() const
    return self.uglySide.call('ritual_ZNK14QQuickFontInfo4boldEv')

  def fixedPitch(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontInfo::fixedPitch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#fixedPitch
    """
    #  bool QQuickFontInfo::fixedPitch() const
    return self.uglySide.call('ritual_ZNK14QQuickFontInfo10fixedPitchEv')

  def style(self) -> QQuickFontEnums.Style:
    """
    Calls Qt's 'QQuickFontEnums::Style QQuickFontInfo::style() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#style

    Returns
    -------

    QQuickFontEnums.Style
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickFontEnums.Style(number)' gives.
    """
    #  QQuickFontEnums::Style QQuickFontInfo::style() const
    return QQuickFontEnums.Style(self.uglySide.call(
        'ritual_ZNK14QQuickFontInfo5styleEv',
    ))

  def variableAxes(self) -> QList[QFontVariableAxis]:
    """
    Calls Qt's 'QList<QFontVariableAxis> QQuickFontInfo::variableAxes()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#variableAxes

    Returns
    -------

    QList[QFontVariableAxis]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QFontVariableAxis> QQuickFontInfo::variableAxes() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickFontInfo12variableAxesEv',
    )
    from ..QtGui import QFontVariableAxis
    return QList[QFontVariableAxis]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickFontInfo::setFont(QFont font)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#setFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickFontInfo::setFont(QFont font)
    self.uglySide.call(
        'ritual_ZN14QQuickFontInfo7setFontE5QFont', self._valueOf(font),
    )

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickFontInfo::QQuickFontInfo(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#QQuickFontInfo

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFontInfo::QQuickFontInfo(QObject *parent)
    self._noteCreation(QQuickFontInfo, lambda: Rituals.call(
        'ritual_ZN14QQuickFontInfoC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontInfo::fontChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontinfo.html#fontChanged
    """
    #  void QQuickFontInfo::fontChanged()
    self.uglySide.call('ritual_ZN14QQuickFontInfo11fontChangedEv')
