"""
Spacer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/spacer_widget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Spacer to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QSizePolicy, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QPaintEvent, QResizeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Spacer(QWidget):
  """
  The cute side of Qt's Spacer: a plain Python object standing in front of
  one C++ Spacer.

  It is built on the cute 'QWidget', as Qt's Spacer is built on Qt's QWidget,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Spacer that has a ritual and that Python can call so
  far, 17 names in all: 'metaObject', 'tr', 'sizeHint', 'sizeHintProperty',
  'setSizeHintProperty', 'sizeType', 'setSizeType', 'alignment',
  'orientation', 'setOrientation', 'setInteractiveMode', 'event',
  'paintEvent', 'resizeEvent', 'updateMask', 'isInLayout', 'updateToolTip'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Spacer::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int Spacer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Spacer is created at the first use, not by 'Spacer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Spacer.
  - Qt tells when it has removed the C++ Spacer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString Spacer::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#tr

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
    #  QString Spacer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN6Spacer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Spacer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Spacer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Spacer::metaObject() const
    address = self.uglySide.call('ritual_ZNK6Spacer10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize Spacer::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Spacer::sizeHint() const
    ritual = 'ritual_ZNK6Spacer8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK6Spacer8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeHintProperty(self) -> QSize:
    """
    Calls Qt's 'QSize Spacer::sizeHintProperty() const'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#sizeHintProperty

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Spacer::sizeHintProperty() const
    address = self.uglySide.call('ritual_ZNK6Spacer16sizeHintPropertyEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def sizeType(self) -> QSizePolicy.Policy:
    """
    Calls Qt's 'QSizePolicy::Policy Spacer::sizeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#sizeType

    Returns
    -------

    QSizePolicy.Policy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSizePolicy.Policy(number)' gives.
    """
    #  QSizePolicy::Policy Spacer::sizeType() const
    return QSizePolicy.Policy(self.uglySide.call(
        'ritual_ZNK6Spacer8sizeTypeEv',
    ))

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment Spacer::alignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment Spacer::alignment() const
    return Qt.Alignment(self.uglySide.call('ritual_ZNK6Spacer9alignmentEv'))

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation Spacer::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation Spacer::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK6Spacer11orientationEv',
    ))

  def isInLayout(self) -> bool:
    """
    Calls Qt's 'bool Spacer::isInLayout() const'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#isInLayout
    """
    #  bool Spacer::isInLayout() const
    return self.uglySide.call('ritual_ZNK6Spacer10isInLayoutEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSize)
  def setSizeHintProperty(self, s: QSize) -> None:
    """
    Calls Qt's 'void Spacer::setSizeHintProperty(const QSize &s)'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#setSizeHintProperty

    Parameters
    ----------

    s : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Spacer::setSizeHintProperty(const QSize &s)
    self.uglySide.call(
        'ritual_ZN6Spacer19setSizeHintPropertyERK5QSize', self._valueOf(s),
    )

  @overload(QSizePolicy.Policy)
  def setSizeType(self, t: QSizePolicy.Policy) -> None:
    """
    Calls Qt's 'void Spacer::setSizeType(QSizePolicy::Policy t)'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#setSizeType

    Parameters
    ----------

    t : QSizePolicy.Policy
      Passed on as its number.
    """
    #  void Spacer::setSizeType(QSizePolicy::Policy t)
    self.uglySide.call(
        'ritual_ZN6Spacer11setSizeTypeEN11QSizePolicy6PolicyE', t.value,
    )

  @overload(Qt.Orientation)
  def setOrientation(self, o: Qt.Orientation) -> None:
    """
    Calls Qt's 'void Spacer::setOrientation(Qt::Orientation o)'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#setOrientation

    Parameters
    ----------

    o : Qt.Orientation
      Passed on as its number.
    """
    #  void Spacer::setOrientation(Qt::Orientation o)
    self.uglySide.call(
        'ritual_ZN6Spacer14setOrientationEN2Qt11OrientationE', o.value,
    )

  @overload(bool)
  def setInteractiveMode(self, b: bool) -> None:
    """
    Calls Qt's 'void Spacer::setInteractiveMode(bool b)'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#setInteractiveMode

    Parameters
    ----------

    b : bool
      Passed on as it is.
    """
    #  void Spacer::setInteractiveMode(bool b)
    self.uglySide.call('ritual_ZN6Spacer18setInteractiveModeEb', b)

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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'Spacer::Spacer(QWidget *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#Spacer

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Spacer::Spacer(QWidget *parent)
    self._noteCreation(Spacer, lambda: Rituals.call(
        'ritual_ZN6SpacerC1EP7QWidget', self._addressOf(parent),
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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool Spacer::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Spacer::event(QEvent *e)
    ritual = 'ritual_ZN6Spacer5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6Spacer5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, e: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void Spacer::paintEvent(QPaintEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#paintEvent

    Parameters
    ----------

    e : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Spacer::paintEvent(QPaintEvent *e)
    ritual = 'ritual_ZN6Spacer10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6Spacer10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, e: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void Spacer::resizeEvent(QResizeEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#resizeEvent

    Parameters
    ----------

    e : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Spacer::resizeEvent(QResizeEvent *e)
    ritual = 'ritual_ZN6Spacer11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6Spacer11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  def updateMask(self) -> None:
    """
    Calls Qt's 'void Spacer::updateMask()'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#updateMask
    """
    #  void Spacer::updateMask()
    self.uglySide.call('ritual_ZN6Spacer10updateMaskEv')

  def updateToolTip(self) -> None:
    """
    Calls Qt's 'void Spacer::updateToolTip()'.

    Qt's own words: https://doc.qt.io/qt-6/spacer.html#updateToolTip
    """
    #  void Spacer::updateToolTip()
    self.uglySide.call('ritual_ZN6Spacer13updateToolTipEv')
