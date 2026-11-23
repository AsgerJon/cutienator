"""
QBalloonTip binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qsystemtrayicon_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QBalloonTip to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QTimerEvent
  from ..QtGui import QMouseEvent, QPaintEvent, QResizeEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBalloonTip(QWidget):
  """
  The cute side of Qt's QBalloonTip: a plain Python object standing in front
  of one C++ QBalloonTip.

  It is built on the cute 'QWidget', as Qt's QBalloonTip is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QBalloonTip that has a ritual and that Python can
  call so far, 5 names in all: 'metaObject', 'paintEvent', 'resizeEvent',
  'mousePressEvent', 'timerEvent'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has no ritual
  ------------------

  12 of the 17 functions Qt declares: 6 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 takes or
  gives a type that cannot be passed yet; 1 a template; 1 declared and
  nowhere to be found; 1 leans on 'QBalloonTip; 1 leans on 'vtable for
  QBalloonTip', which Qt's library does not offer and Qt's source has no code
  for that could be taken.

  What to expect
  --------------

  - The C++ QBalloonTip is created at the first use, not by
    'QBalloonTip(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBalloonTip.
  - Qt tells when it has removed the C++ QBalloonTip. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBalloonTip'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBalloonTip::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qballoontip.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBalloonTip::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QBalloonTip10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Calls Qt's 'void QBalloonTip::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qballoontip.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBalloonTip::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN11QBalloonTip10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QBalloonTip10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QBalloonTip::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qballoontip.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBalloonTip::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN11QBalloonTip11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QBalloonTip11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, e: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QBalloonTip::mousePressEvent(QMouseEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qballoontip.html#mousePressEvent

    Parameters
    ----------

    e : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBalloonTip::mousePressEvent(QMouseEvent *e)
    ritual = 'ritual_ZN11QBalloonTip15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QBalloonTip15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, e: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QBalloonTip::timerEvent(QTimerEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qballoontip.html#timerEvent

    Parameters
    ----------

    e : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBalloonTip::timerEvent(QTimerEvent *e)
    ritual = 'ritual_ZN11QBalloonTip10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QBalloonTip10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(e))
