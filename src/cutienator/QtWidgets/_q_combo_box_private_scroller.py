"""
QComboBoxPrivateScroller binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcombobox_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QComboBoxPrivateScroller to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QSize, QTimerEvent
  from ..QtGui import QEnterEvent, QHideEvent, QMouseEvent, QPaintEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEnterEvent = WAIT['QEnterEvent']
  QEvent = WAIT['QEvent']
  QHideEvent = WAIT['QHideEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QComboBoxPrivateScroller(QWidget):
  """
  The cute side of Qt's QComboBoxPrivateScroller: a plain Python object
  standing in front of one C++ QComboBoxPrivateScroller.

  It is built on the cute 'QWidget', as Qt's QComboBoxPrivateScroller is
  built on Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QComboBoxPrivateScroller that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'sizeHint',
  'stopTimer', 'enterEvent', 'leaveEvent', 'timerEvent', 'hideEvent',
  'mouseMoveEvent', 'paintEvent', 'doScroll'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QComboBoxPrivateScroller::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QComboBoxPrivateScroller::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QComboBoxPrivateScroller::~QComboBoxPrivateScroller()': the
    destructor: Python never removes a C++ QComboBoxPrivateScroller.

  What has no ritual
  ------------------

  5 of the 18 functions Qt declares: 2 not a gap; 2 leans on
  'QComboBoxPrivateScroller; 1 Qt's library has no name for it, and its code
  in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QComboBoxPrivateScroller is created at the first use, not by
    'QComboBoxPrivateScroller(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QComboBoxPrivateScroller.
  - Qt tells when it has removed the C++ QComboBoxPrivateScroller. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QComboBoxPrivateScroller that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QComboBoxPrivateScroller'

  #  A C++ QComboBoxPrivateScroller Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QComboBoxPrivateScroller'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QComboBoxPrivateScroller::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatescroller.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QComboBoxPrivateScroller::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QComboBoxPrivateScroller10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QComboBoxPrivateScroller::sizeHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatescroller.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QComboBoxPrivateScroller::sizeHint() const
    ritual = 'ritual_ZNK24QComboBoxPrivateScroller8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QComboBoxPrivateScroller8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QComboBoxPrivateScroller::QComboBoxPrivateScroller(QAbstractSlider::
    SliderAction action, QWidget *parent)': leans on
    'QComboBoxPrivateScroller::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QComboBoxPrivateScroller.__init__' has no cute function yet. Qt's "
        "'QComboBoxPrivateScroller::QComboBoxPrivateScroller(QAbstractSlider"
        "::SliderAction action, QWidget *parent)': leans on "
        "'QComboBoxPrivateScroller::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def stopTimer(self) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateScroller::stopTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatescroller.html#stopTimer
    """
    #  void QComboBoxPrivateScroller::stopTimer()
    self.uglySide.call('ritual_ZN24QComboBoxPrivateScroller9stopTimerEv')

  @overload(QEnterEvent)
  @overload(NoneType)
  def enterEvent(self, a0: Optional[QEnterEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateScroller::enterEvent(QEnterEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatescroller.html#enterEvent

    Parameters
    ----------

    a0 : Optional[QEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateScroller::enterEvent(QEnterEvent *a0)
    self.uglySide.call(
        'ritual_ZN24QComboBoxPrivateScroller10enterEventEP11QEnterEvent',
        self._addressOf(a0),
    )

  @overload(QEvent)
  @overload(NoneType)
  def leaveEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateScroller::leaveEvent(QEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatescroller.html#leaveEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateScroller::leaveEvent(QEvent *a0)
    ritual = 'ritual_ZN24QComboBoxPrivateScroller10leaveEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QComboBoxPrivateScroller10leaveEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateScroller::timerEvent(QTimerEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatescroller.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateScroller::timerEvent(QTimerEvent *e)
    self.uglySide.call(
        'ritual_ZN24QComboBoxPrivateScroller10timerEventEP11QTimerEvent',
        self._addressOf(e),
    )

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, a0: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateScroller::hideEvent(QHideEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatescroller.html#hideEvent

    Parameters
    ----------

    a0 : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateScroller::hideEvent(QHideEvent *a0)
    ritual = 'ritual_ZN24QComboBoxPrivateScroller9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QComboBoxPrivateScroller9hideEventEP10QHideEvent')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateScroller::mouseMoveEvent(QMouseEvent
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatescroller.html#mouseMoveEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateScroller::mouseMoveEvent(QMouseEvent *e)
    ritual = (
        'ritual_ZN24QComboBoxPrivateScroller14mouseMoveEventEP11QMouseEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QComboBoxPrivateScroller14mouseMoveEventEP11QMous'
          'eEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateScroller::paintEvent(QPaintEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatescroller.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QComboBoxPrivateScroller::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN24QComboBoxPrivateScroller10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QComboBoxPrivateScroller10paintEventEP11QPaintEve'
          'nt')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(int)
  def doScroll(self, action: int) -> None:
    """
    Calls Qt's 'void QComboBoxPrivateScroller::doScroll(int action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcomboboxprivatescroller.html#doScroll

    Parameters
    ----------

    action : int
      Passed on as it is.
    """
    #  void QComboBoxPrivateScroller::doScroll(int action)
    self.uglySide.call(
        'ritual_ZN24QComboBoxPrivateScroller8doScrollEi', action,
    )
