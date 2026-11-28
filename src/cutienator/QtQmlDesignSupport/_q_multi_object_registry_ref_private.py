"""
QMultiObjectRegistryRefPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlDesignSupport/6.12.0/QtQmlDesignSupport/private/qmultiobjectregistryref_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QMultiObjectRegistryRefPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractObjectRegistryRefPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from ..QtQml import QQmlEngine
  from . import QMultiObjectRegistryRef
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlEngine = WAIT['QQmlEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMultiObjectRegistryRefPrivate(QAbstractObjectRegistryRefPrivate):
  """
  The cute side of Qt's QMultiObjectRegistryRefPrivate: a plain Python object
  standing in front of one C++ QMultiObjectRegistryRefPrivate.

  It is built on the cute 'QAbstractObjectRegistryRefPrivate', as Qt's
  QMultiObjectRegistryRefPrivate is built on Qt's
  QAbstractObjectRegistryRefPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMultiObjectRegistryRefPrivate that has a ritual and
  that Python can call so far, 4 names in all: 'q_func', 'handleObjectAdded',
  'handleObjectRemoved', 'handleInitialObjects'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMultiObjectRegistryRef
    *QMultiObjectRegistryRefPrivate::q_func() const': takes in Python what
    'QMultiObjectRegistryRef *QMultiObjectRegistryRefPrivate::q_func()'
    takes.
  - Qt's 'qsizetype
    QMultiObjectRegistryRefPrivate::objectsCount(QQmlListProperty<QObject>
    *l)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject
    *QMultiObjectRegistryRefPrivate::objectsAt(QQmlListProperty<QObject> *l,
    qsizetype i)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.

  What to expect
  --------------

  - The C++ QMultiObjectRegistryRefPrivate is created at the first use, not
    by 'QMultiObjectRegistryRefPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMultiObjectRegistryRefPrivate.
  - Each name of Qt's QMultiObjectRegistryRefPrivate that has no cute
    function yet, 'objectsAt', 'objectsCount', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMultiObjectRegistryRefPrivate'

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
    'QMultiObjectRegistryRefPrivate::QMultiObjectRegistryRefPrivate(
    QQmlEngine *engine)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmultiobjectregistryrefprivate.html

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMultiObjectRegistryRefPrivate::QMultiObjectRegistryRefPrivate(
    #      QQmlEngine *engine)
    self._noteCreation(QMultiObjectRegistryRefPrivate, lambda: Rituals.call(
        'ritual_ZN30QMultiObjectRegistryRefPrivateC1EP10QQmlEngine',
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

  def q_func(self) -> Optional[QMultiObjectRegistryRef]:
    """
    Calls Qt's 'QMultiObjectRegistryRef
    *QMultiObjectRegistryRefPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmultiobjectregistryrefprivate.html#q_func

    Returns
    -------

    Optional[QMultiObjectRegistryRef]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMultiObjectRegistryRef *QMultiObjectRegistryRefPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN30QMultiObjectRegistryRefPrivate6q_funcEv',
    )
    from . import QMultiObjectRegistryRef
    return QMultiObjectRegistryRef._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def handleObjectAdded(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QMultiObjectRegistryRefPrivate::handleObjectAdded(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmultiobjectregistryrefprivate.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMultiObjectRegistryRefPrivate::handleObjectAdded(QObject *obj)
    ritual = (
        'ritual_ZN30QMultiObjectRegistryRefPrivate17handleObjectAddedEP7QOb'
        'ject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QMultiObjectRegistryRefPrivate17handleObjectAdded'
          'EP7QObject')
    self.uglySide.call(ritual, self._addressOf(obj, 'QObject'))

  @overload(QObject)
  @overload(NoneType)
  def handleObjectRemoved(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QMultiObjectRegistryRefPrivate::handleObjectRemoved(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmultiobjectregistryrefprivate.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMultiObjectRegistryRefPrivate::handleObjectRemoved(QObject *obj)
    ritual = (
        'ritual_ZN30QMultiObjectRegistryRefPrivate19handleObjectRemovedEP7Q'
        'Object')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QMultiObjectRegistryRefPrivate19handleObjectRemov'
          'edEP7QObject')
    self.uglySide.call(ritual, self._addressOf(obj, 'QObject'))

  def handleInitialObjects(self) -> None:
    """
    Calls Qt's 'void QMultiObjectRegistryRefPrivate::handleInitialObjects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmultiobjectregistryrefprivate.html
    """
    #  void QMultiObjectRegistryRefPrivate::handleInitialObjects()
    ritual = (
        'ritual_ZN30QMultiObjectRegistryRefPrivate20handleInitialObjectsEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QMultiObjectRegistryRefPrivate20handleInitialObje'
          'ctsEv')
    self.uglySide.call(ritual)

  @staticmethod
  def objectsAt(*__, **_) -> Never:
    """
    Qt's 'QObject
    *QMultiObjectRegistryRefPrivate::objectsAt(QQmlListProperty<QObject> *l,
    qsizetype i)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QMultiObjectRegistryRefPrivate.objectsAt' has no cute function "
        "yet. Qt's 'QObject "
        "*QMultiObjectRegistryRefPrivate::objectsAt(QQmlListProperty<QObject"
        "> *l, qsizetype i)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def objectsCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QMultiObjectRegistryRefPrivate::objectsCount(QQmlListProperty<QObject>
    *l)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMultiObjectRegistryRefPrivate.objectsCount' has no cute function "
        "yet. Qt's 'qsizetype "
        "QMultiObjectRegistryRefPrivate::objectsCount(QQmlListProperty<QObje"
        "ct> *l)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")
