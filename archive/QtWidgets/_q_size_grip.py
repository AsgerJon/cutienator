"""
QSizeGrip binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qsizegrip.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QHideEvent, QMouseEvent, QMoveEvent, QPaintEvent
  from ..QtGui import QShowEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QHideEvent = WAIT['QHideEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QMoveEvent = WAIT['QMoveEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QShowEvent = WAIT['QShowEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSizeGrip(QWidget):
  """
  The cute side of Qt's QSizeGrip: a plain Python object standing in front of
  one C++ QSizeGrip.

  It is built on the cute 'QWidget', as Qt's QSizeGrip is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSizeGrip that has a ritual and that Python can call
  so far, 13 names in all: 'metaObject', 'tr', 'sizeHint', 'setVisible',
  'paintEvent', 'mousePressEvent', 'mouseMoveEvent', 'mouseReleaseEvent',
  'moveEvent', 'showEvent', 'hideEvent', 'eventFilter', 'event'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSizeGrip::~QSizeGrip()': the destructor: Python never removes a
    C++ QSizeGrip.

  What has no ritual
  ------------------

  8 of the 23 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QSizeGrip is created at the first use, not by 'QSizeGrip(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSizeGrip.
  - Qt tells when it has removed the C++ QSizeGrip. Every call on the cute
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
    Calls Qt's 'QString QSizeGrip::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#tr

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
    #  QString QSizeGrip::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QSizeGrip2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSizeGrip'

  #  A C++ QSizeGrip Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSizeGrip'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSizeGrip::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSizeGrip::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QSizeGrip10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QSizeGrip::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSizeGrip::sizeHint() const
    ritual = 'ritual_ZNK9QSizeGrip8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK9QSizeGrip8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setVisible(self, a0: bool) -> None:
    """
    Calls Qt's 'void QSizeGrip::setVisible(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#setVisible

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QSizeGrip::setVisible(bool a0)
    ritual = 'ritual_ZN9QSizeGrip10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSizeGrip10setVisibleEb'
    self.uglySide.call(ritual, a0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's 'QSizeGrip::QSizeGrip(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#QSizeGrip

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSizeGrip::QSizeGrip(QWidget *parent)
    self._noteCreation(QSizeGrip, lambda: Rituals.call(
        'ritual_ZN9QSizeGripC1EP7QWidget', self._addressOf(parent),
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

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QSizeGrip::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSizeGrip::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN9QSizeGrip10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSizeGrip10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QSizeGrip::mousePressEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#mousePressEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSizeGrip::mousePressEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN9QSizeGrip15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSizeGrip15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QSizeGrip::mouseMoveEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#mouseMoveEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSizeGrip::mouseMoveEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN9QSizeGrip14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSizeGrip14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, mouseEvent: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QSizeGrip::mouseReleaseEvent(QMouseEvent *mouseEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#mouseReleaseEvent

    Parameters
    ----------

    mouseEvent : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSizeGrip::mouseReleaseEvent(QMouseEvent *mouseEvent)
    ritual = 'ritual_ZN9QSizeGrip17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSizeGrip17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(mouseEvent))

  @overload(QMoveEvent)
  @overload(NoneType)
  def moveEvent(self, moveEvent: Optional[QMoveEvent]) -> None:
    """
    Calls Qt's 'void QSizeGrip::moveEvent(QMoveEvent *moveEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#moveEvent

    Parameters
    ----------

    moveEvent : Optional[QMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSizeGrip::moveEvent(QMoveEvent *moveEvent)
    ritual = 'ritual_ZN9QSizeGrip9moveEventEP10QMoveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSizeGrip9moveEventEP10QMoveEvent'
    self.uglySide.call(ritual, self._addressOf(moveEvent))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, showEvent: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QSizeGrip::showEvent(QShowEvent *showEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#showEvent

    Parameters
    ----------

    showEvent : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSizeGrip::showEvent(QShowEvent *showEvent)
    ritual = 'ritual_ZN9QSizeGrip9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSizeGrip9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(showEvent))

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, hideEvent: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QSizeGrip::hideEvent(QHideEvent *hideEvent)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#hideEvent

    Parameters
    ----------

    hideEvent : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSizeGrip::hideEvent(QHideEvent *hideEvent)
    ritual = 'ritual_ZN9QSizeGrip9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSizeGrip9hideEventEP10QHideEvent'
    self.uglySide.call(ritual, self._addressOf(hideEvent))

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSizeGrip::eventFilter(QObject *a0, QEvent *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#eventFilter

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSizeGrip::eventFilter(QObject *a0, QEvent *a1)
    ritual = 'ritual_ZN9QSizeGrip11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSizeGrip11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(a0, 'QObject'), self._addressOf(a1),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSizeGrip::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsizegrip.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSizeGrip::event(QEvent *a0)
    ritual = 'ritual_ZN9QSizeGrip5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN9QSizeGrip5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))
