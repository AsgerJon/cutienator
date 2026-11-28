"""
QScxmlInternal::ScxmlEventRouter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlstatemachine_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QScxmlInternal::ScxmlEventRouter to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaMethod, QMetaObject
  from . import QScxmlEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaMethod = WAIT['QMetaMethod']
  QScxmlEvent = WAIT['QScxmlEvent']


class ScxmlEventRouter(QObject):
  """
  The cute side of Qt's QScxmlInternal::ScxmlEventRouter: a plain Python
  object standing in front of one C++ QScxmlInternal::ScxmlEventRouter.

  It is built on the cute 'QObject', as Qt's QScxmlInternal::ScxmlEventRouter
  is built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QScxmlInternal::ScxmlEventRouter that has a ritual
  and that Python can call so far, 3 names in all: 'metaObject',
  'eventOccurred', 'disconnectNotify'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScxmlInternal::ScxmlEventRouter::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QScxmlInternal::ScxmlEventRouter::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  8 of the 13 functions Qt declares: 3 leans on 'vtable for QScxmlInternal; 2
  not a gap; 2 leans on 'QScxmlInternal; 1 Qt's library has no name for it,
  and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QScxmlInternal::ScxmlEventRouter is created at the first use, not
    by 'QScxmlInternal::ScxmlEventRouter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlInternal::ScxmlEventRouter.
  - Qt tells when it has removed the C++ QScxmlInternal::ScxmlEventRouter.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScxmlInternal::ScxmlEventRouter that has no cute
    function yet, '__init__', 'child', 'connectToEvent', 'route', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlInternal::ScxmlEventRouter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QScxmlInternal::ScxmlEventRouter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-scxmleventrouter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScxmlInternal::ScxmlEventRouter::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK14QScxmlInternal16ScxmlEventRouter10metaObjectEv',
    )
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QScxmlInternal::ScxmlEventRouter::ScxmlEventRouter(QObject
    *parent)': leans on 'vtable for QScxmlInternal::ScxmlEventRouter', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QScxmlInternal.ScxmlEventRouter.__init__' has no cute function "
        "yet. Qt's "
        "'QScxmlInternal::ScxmlEventRouter::ScxmlEventRouter(QObject "
        "*parent)': leans on 'vtable for QScxmlInternal::ScxmlEventRouter', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QScxmlEvent)
  def eventOccurred(self, event: QScxmlEvent) -> None:
    """
    Calls Qt's 'void QScxmlInternal::ScxmlEventRouter::eventOccurred(const
    QScxmlEvent &event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-scxmleventrouter.html#eventOccurred

    Parameters
    ----------

    event : QScxmlEvent
      Passed on as a value: Qt reads the C++ QScxmlEvent, which stays
      Python's own.
    """
    #  void QScxmlInternal::ScxmlEventRouter::eventOccurred(const QScxmlEvent
    #      &event)
    self.uglySide.call(
        'ritual_ZN14QScxmlInternal16ScxmlEventRouter13eventOccurredERK11QSc'
        'xmlEvent',
        self._valueOf(event),
    )

  @overload(QMetaMethod)
  def disconnectNotify(self, signal: QMetaMethod) -> None:
    """
    Calls Qt's 'void QScxmlInternal::ScxmlEventRouter::disconnectNotify(const
    QMetaMethod &signal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlinternal-scxmleventrouter.html

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QScxmlInternal::ScxmlEventRouter::disconnectNotify(const
    #      QMetaMethod &signal)
    self.uglySide.call(
        'ritual_ZN14QScxmlInternal16ScxmlEventRouter16disconnectNotifyERK11'
        'QMetaMethod',
        self._valueOf(signal),
    )

  @staticmethod
  def child(*__, **_) -> Never:
    """
    Qt's 'ScxmlEventRouter *QScxmlInternal::ScxmlEventRouter::child(const
    QString &segment)': leans on 'vtable for
    QScxmlInternal::ScxmlEventRouter', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QScxmlInternal.ScxmlEventRouter.child' has no cute function yet. "
        "Qt's 'ScxmlEventRouter "
        "*QScxmlInternal::ScxmlEventRouter::child(const QString &segment)': "
        "leans on 'vtable for QScxmlInternal::ScxmlEventRouter', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def connectToEvent(*__, **_) -> Never:
    """
    - Qt's 'QMetaObject::Connection
      QScxmlInternal::ScxmlEventRouter::connectToEvent(const QStringList
      &segments, const QObject *receiver, void **slot,
      QtPrivate::QSlotObjectBase *method, Qt::ConnectionType type)': Qt's
      library has no name for it, and its code in Qt's source does not
      compile apart from its file: use of undeclared identifier
      'nextSegment'.
    - Qt's 'QMetaObject::Connection
      QScxmlInternal::ScxmlEventRouter::connectToEvent(const QStringList
      &segments, const QObject *receiver, const char *method,
      Qt::ConnectionType type)': leans on 'vtable for
      QScxmlInternal::ScxmlEventRouter', which Qt's source does not mark for
      use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QScxmlInternal.ScxmlEventRouter.connectToEvent' has no cute "
        "function yet. Qt's 'QMetaObject::Connection "
        "QScxmlInternal::ScxmlEventRouter::connectToEvent(const QStringList "
        "&segments, const QObject *receiver, void **slot, "
        "QtPrivate::QSlotObjectBase *method, Qt::ConnectionType type)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'nextSegment'. Qt's 'QMetaObject::Connection "
        "QScxmlInternal::ScxmlEventRouter::connectToEvent(const QStringList "
        "&segments, const QObject *receiver, const char *method, "
        "Qt::ConnectionType type)': leans on 'vtable for "
        "QScxmlInternal::ScxmlEventRouter', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def route(*__, **_) -> Never:
    """
    Qt's 'void QScxmlInternal::ScxmlEventRouter::route(const QStringList
    &segments, QScxmlEvent *event)': leans on
    'QScxmlInternal::ScxmlEventRouter::eventOccurred(QScxmlEvent const&)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QScxmlInternal.ScxmlEventRouter.route' has no cute function yet. "
        "Qt's 'void QScxmlInternal::ScxmlEventRouter::route(const "
        "QStringList &segments, QScxmlEvent *event)': leans on "
        "'QScxmlInternal::ScxmlEventRouter::eventOccurred(QScxmlEvent "
        "const&)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
