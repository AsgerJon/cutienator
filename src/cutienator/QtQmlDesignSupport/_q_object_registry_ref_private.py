"""
QObjectRegistryRefPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlDesignSupport/6.12.0/QtQmlDesignSupport/private/qobjectregistryref_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QObjectRegistryRefPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractObjectRegistryRefPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject
  from ..QtQml import QQmlEngine
  from . import QObjectRegistryRef
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlEngine = WAIT['QQmlEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObjectRegistryRefPrivate(QAbstractObjectRegistryRefPrivate):
  """
  The cute side of Qt's QObjectRegistryRefPrivate: a plain Python object
  standing in front of one C++ QObjectRegistryRefPrivate.

  It is built on the cute 'QAbstractObjectRegistryRefPrivate', as Qt's
  QObjectRegistryRefPrivate is built on Qt's
  QAbstractObjectRegistryRefPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QObjectRegistryRefPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'q_func', 'setObject',
  'printMultiWarning', 'handleObjectAdded', 'handleObjectRemoved',
  'handleInitialObjects'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QObjectRegistryRef *QObjectRegistryRefPrivate::q_func()
    const': takes in Python what 'QObjectRegistryRef
    *QObjectRegistryRefPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QObjectRegistryRefPrivate is created at the first use, not by
    'QObjectRegistryRefPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QObjectRegistryRefPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QObjectRegistryRefPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setObject(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObjectRegistryRefPrivate::setObject(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistryrefprivate.html#setObject

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectRegistryRefPrivate::setObject(QObject *obj)
    self.uglySide.call(
        'ritual_ZN25QObjectRegistryRefPrivate9setObjectEP7QObject',
        self._addressOf(obj, 'QObject'),
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
  @overload(QQmlEngine)
  @overload(NoneType)
  def __init__(self, engine: Optional[QQmlEngine] = None) -> None:
    """
    Notes what was given, for Qt's
    'QObjectRegistryRefPrivate::QObjectRegistryRefPrivate(QQmlEngine
    *engine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistryrefprivate.html

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QObjectRegistryRefPrivate::QObjectRegistryRefPrivate(QQmlEngine
    #      *engine)
    self._noteCreation(QObjectRegistryRefPrivate, lambda: Rituals.call(
        'ritual_ZN25QObjectRegistryRefPrivateC1EP10QQmlEngine',
        self._addressOf(engine),
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

  def q_func(self) -> Optional[QObjectRegistryRef]:
    """
    Calls Qt's 'QObjectRegistryRef *QObjectRegistryRefPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistryrefprivate.html#q_func

    Returns
    -------

    Optional[QObjectRegistryRef]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObjectRegistryRef *QObjectRegistryRefPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QObjectRegistryRefPrivate6q_funcEv',
    )
    from . import QObjectRegistryRef
    return QObjectRegistryRef._cuteAt(address)

  def printMultiWarning(self) -> None:
    """
    Calls Qt's 'void QObjectRegistryRefPrivate::printMultiWarning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistryrefprivate.html#printMultiWarning
    """
    #  void QObjectRegistryRefPrivate::printMultiWarning() const
    self.uglySide.call(
        'ritual_ZNK25QObjectRegistryRefPrivate17printMultiWarningEv',
    )

  @overload(QObject)
  @overload(NoneType)
  def handleObjectAdded(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObjectRegistryRefPrivate::handleObjectAdded(QObject
    *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistryrefprivate.html#handleObjectAdded

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectRegistryRefPrivate::handleObjectAdded(QObject *obj)
    ritual = (
        'ritual_ZN25QObjectRegistryRefPrivate17handleObjectAddedEP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QObjectRegistryRefPrivate17handleObjectAddedEP7QO'
          'bject')
    self.uglySide.call(ritual, self._addressOf(obj, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleObjectRemoved(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObjectRegistryRefPrivate::handleObjectRemoved(QObject
    *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistryrefprivate.html#handleObjectRemoved

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectRegistryRefPrivate::handleObjectRemoved(QObject *obj)
    ritual = (
        'ritual_ZN25QObjectRegistryRefPrivate19handleObjectRemovedEP7QObjec'
        't')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QObjectRegistryRefPrivate19handleObjectRemovedEP7'
          'QObject')
    self.uglySide.call(ritual, self._addressOf(obj, 'QObject'))

  def handleInitialObjects(self) -> None:
    """
    Calls Qt's 'void QObjectRegistryRefPrivate::handleInitialObjects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistryrefprivate.html
    """
    #  void QObjectRegistryRefPrivate::handleInitialObjects()
    ritual = 'ritual_ZN25QObjectRegistryRefPrivate20handleInitialObjectsEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QObjectRegistryRefPrivate20handleInitialObjectsEv')
    self.uglySide.call(ritual)
