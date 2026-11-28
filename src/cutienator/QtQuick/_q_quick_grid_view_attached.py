"""
QQuickGridViewAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickgridview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickGridViewAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickItemViewAttached

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickGridView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickGridView = WAIT['QQuickGridView']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickGridViewAttached(QQuickItemViewAttached):
  """
  The cute side of Qt's QQuickGridViewAttached: a plain Python object
  standing in front of one C++ QQuickGridViewAttached.

  It is built on the cute 'QQuickItemViewAttached', as Qt's
  QQuickGridViewAttached is built on Qt's QQuickItemViewAttached, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickGridViewAttached that has a ritual and that
  Python can call so far, 3 names in all: 'metaObject', 'view', 'setView'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickGridViewAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickGridViewAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickGridViewAttached::~QQuickGridViewAttached()': the destructor:
    Python never removes a C++ QQuickGridViewAttached.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 2 not a gap; 2 leans on
  'QQuickGridViewAttached.

  What to expect
  --------------

  - The C++ QQuickGridViewAttached is created at the first use, not by
    'QQuickGridViewAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickGridViewAttached.
  - Qt tells when it has removed the C++ QQuickGridViewAttached. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickGridViewAttached that has no cute function yet,
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
  __qt_class__ = 'QQuickGridViewAttached'

  #  A C++ QQuickGridViewAttached Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickGridViewAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickGridViewAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridviewattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickGridViewAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickGridViewAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def view(self) -> Optional[QQuickGridView]:
    """
    Calls Qt's 'QQuickGridView *QQuickGridViewAttached::view() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickgridviewattached.html#view

    Returns
    -------

    Optional[QQuickGridView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickGridView *QQuickGridViewAttached::view() const
    address = self.uglySide.call('ritual_ZNK22QQuickGridViewAttached4viewEv')
    from . import QQuickGridView
    return QQuickGridView._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickGridView)
  @overload(NoneType)
  def setView(self, view: Optional[QQuickGridView]) -> None:
    """
    Calls Qt's 'void QQuickGridViewAttached::setView(QQuickGridView *view)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickgridviewattached.html#setView

    Parameters
    ----------

    view : Optional[QQuickGridView]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickGridViewAttached::setView(QQuickGridView *view)
    self.uglySide.call(
        'ritual_ZN22QQuickGridViewAttached7setViewEP14QQuickGridView',
        self._addressOf(view),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickGridViewAttached::QQuickGridViewAttached(QObject *parent)':
    leans on 'QQuickGridViewAttached::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickGridViewAttached.__init__' has no cute function yet. Qt's "
        "'QQuickGridViewAttached::QQuickGridViewAttached(QObject *parent)': "
        "leans on 'QQuickGridViewAttached::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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
