"""
QSidebar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qsidebar_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QSidebar to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import QListView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize, QUrl
  from ..QtGui import QDragEnterEvent, QFocusEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDragEnterEvent = WAIT['QDragEnterEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSidebar(QListView):
  """
  The cute side of Qt's QSidebar: a plain Python object standing in front of
  one C++ QSidebar.

  It is built on the cute 'QListView', as Qt's QSidebar is built on Qt's
  QListView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSidebar that has a ritual and that Python can call
  so far, 7 names in all: 'metaObject', 'sizeHint', 'urls', 'event',
  'focusInEvent', 'dragEnterEvent', 'removeEntry'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSidebar::~QSidebar()': the destructor: Python never removes a C++
    QSidebar.

  What has no ritual
  ------------------

  14 of the 22 functions Qt declares: 6 leans on 'QSidebar; 3 leans on
  'QUrlModel; 2 takes or gives a type that cannot be passed yet; 1 a
  template; 1 declared and nowhere to be found; 1 a signal.

  What to expect
  --------------

  - The C++ QSidebar is created at the first use, not by 'QSidebar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSidebar.
  - Qt tells when it has removed the C++ QSidebar. Every call on the cute
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
  __qt_class__ = 'QSidebar'

  #  A C++ QSidebar Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSidebar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSidebar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSidebar::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QSidebar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QSidebar::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSidebar::sizeHint() const
    ritual = 'ritual_ZNK8QSidebar8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QSidebar8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def urls(self) -> QList[QUrl]:
    """
    Calls Qt's 'QList<QUrl> QSidebar::urls() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#urls

    Returns
    -------

    QList[QUrl]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QUrl> QSidebar::urls() const
    address = self.uglySide.call('ritual_ZNK8QSidebar4urlsEv')
    from ..QtCore import QUrl
    return QList[QUrl]._cuteOwning(address)

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

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QSidebar::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QSidebar::event(QEvent *e)
    ritual = 'ritual_ZN8QSidebar5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QSidebar5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, event: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QSidebar::focusInEvent(QFocusEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#focusInEvent

    Parameters
    ----------

    event : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSidebar::focusInEvent(QFocusEvent *event)
    ritual = 'ritual_ZN8QSidebar12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QSidebar12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QDragEnterEvent)
  @overload(NoneType)
  def dragEnterEvent(self, event: Optional[QDragEnterEvent]) -> None:
    """
    Calls Qt's 'void QSidebar::dragEnterEvent(QDragEnterEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#dragEnterEvent

    Parameters
    ----------

    event : Optional[QDragEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSidebar::dragEnterEvent(QDragEnterEvent *event)
    self.uglySide.call(
        'ritual_ZN8QSidebar14dragEnterEventEP15QDragEnterEvent',
        self._addressOf(event),
    )

  def removeEntry(self) -> None:
    """
    Calls Qt's 'void QSidebar::removeEntry()'.

    Qt's own words: https://doc.qt.io/qt-6/qsidebar.html#removeEntry
    """
    #  void QSidebar::removeEntry()
    self.uglySide.call('ritual_ZN8QSidebar11removeEntryEv')
