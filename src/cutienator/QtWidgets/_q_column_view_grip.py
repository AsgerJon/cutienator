"""
QColumnViewGrip binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qcolumnviewgrip_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QColumnViewGrip to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QMouseEvent, QPaintEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QColumnViewGrip(QWidget):
  """
  The cute side of Qt's QColumnViewGrip: a plain Python object standing in
  front of one C++ QColumnViewGrip.

  It is built on the cute 'QWidget', as Qt's QColumnViewGrip is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QColumnViewGrip that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'paintEvent',
  'mouseDoubleClickEvent', 'mouseMoveEvent', 'mouseReleaseEvent',
  'mousePressEvent'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColumnViewGrip::~QColumnViewGrip()': the destructor: Python never
    removes a C++ QColumnViewGrip.

  What has no ritual
  ------------------

  17 of the 24 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 5 leans on 'QColumnViewGrip; 4 forbidden; 1 a template; 1
  declared and nowhere to be found; 1 a signal.

  What to expect
  --------------

  - The C++ QColumnViewGrip is created at the first use, not by
    'QColumnViewGrip(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QColumnViewGrip.
  - Qt tells when it has removed the C++ QColumnViewGrip. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColumnViewGrip'

  #  A C++ QColumnViewGrip Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QColumnViewGrip'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QColumnViewGrip::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnviewgrip.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QColumnViewGrip::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QColumnViewGrip10metaObjectEv')
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
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QColumnViewGrip::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolumnviewgrip.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnViewGrip::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN15QColumnViewGrip10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QColumnViewGrip10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseDoubleClickEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QColumnViewGrip::mouseDoubleClickEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewgrip.html#mouseDoubleClickEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnViewGrip::mouseDoubleClickEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN15QColumnViewGrip21mouseDoubleClickEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QColumnViewGrip::mouseMoveEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewgrip.html#mouseMoveEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnViewGrip::mouseMoveEvent(QMouseEvent *event)
    self.uglySide.call(
        'ritual_ZN15QColumnViewGrip14mouseMoveEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QColumnViewGrip::mouseReleaseEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewgrip.html#mouseReleaseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnViewGrip::mouseReleaseEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QColumnViewGrip17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QColumnViewGrip17mouseReleaseEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, event: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QColumnViewGrip::mousePressEvent(QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolumnviewgrip.html#mousePressEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QColumnViewGrip::mousePressEvent(QMouseEvent *event)
    ritual = 'ritual_ZN15QColumnViewGrip15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QColumnViewGrip15mousePressEventEP11QMouseEvent')
    self.uglySide.call(ritual, self._addressOf(event))
