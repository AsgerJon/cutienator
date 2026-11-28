"""
QAbstractObjectRegistryRefPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlDesignSupport/6.12.0/QtQmlDesignSupport/private/qabstractobjectregistryref_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAbstractObjectRegistryRefPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QAbstractObjectRegistryRef, QObjectRegistrySingleton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractObjectRegistryRefPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAbstractObjectRegistryRefPrivate: a plain Python
  object standing in front of one C++ QAbstractObjectRegistryRefPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QAbstractObjectRegistryRefPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractObjectRegistryRefPrivate that has a ritual
  and that Python can call so far, 6 names in all: 'q_func',
  'handleObjectAdded', 'handleObjectRemoved', 'key', 'handleInitialObjects',
  'registry'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractObjectRegistryRef
    *QAbstractObjectRegistryRefPrivate::q_func() const': takes in Python what
    'QAbstractObjectRegistryRef *QAbstractObjectRegistryRefPrivate::q_func()'
    takes.
  - Qt's 'void
    QAbstractObjectRegistryRefPrivate::dataAppend(QQmlListProperty<QObject>
    *l, QObject *o)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'qsizetype
    QAbstractObjectRegistryRefPrivate::dataCount(QQmlListProperty<QObject>
    *l)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject
    *QAbstractObjectRegistryRefPrivate::dataAt(QQmlListProperty<QObject> *l,
    qsizetype i)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
  - Qt's 'void
    QAbstractObjectRegistryRefPrivate::dataClear(QQmlListProperty<QObject>
    *l)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void
    QAbstractObjectRegistryRefPrivate::dataReplace(QQmlListProperty<QObject>
    *l, qsizetype i, QObject *o)': names 'QQmlListProperty<QObject>', which
    has no cute class yet.
  - Qt's 'void QAbstractObjectRegistryRefPrivate::dataRemoveLast(
    QQmlListProperty<QObject> *l)': names 'QQmlListProperty<QObject>', which
    has no cute class yet.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QAbstractObjectRegistryRefPrivate is created at the first use,
    not by 'QAbstractObjectRegistryRefPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractObjectRegistryRefPrivate.
  - Each name of Qt's QAbstractObjectRegistryRefPrivate that has no cute
    function yet, '__init__', 'dataAppend', 'dataAt', 'dataClear',
    'dataCount', 'dataRemoveLast', 'dataReplace', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractObjectRegistryRefPrivate'

  #  The functions Qt calls itself that QAbstractObjectRegistryRefPrivate is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'handleObjectAdded': (
          ('_ZN33QAbstractObjectRegistryRefPrivate17handleObjectAddedEP7QOb'
           'ject',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleObjectRemoved': (
          ('_ZN33QAbstractObjectRegistryRefPrivate19handleObjectRemovedEP7Q'
           'Object',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'handleInitialObjects': (
          ('_ZN33QAbstractObjectRegistryRefPrivate20handleInitialObjectsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def key(self) -> str:
    """
    Calls Qt's 'QString QAbstractObjectRegistryRefPrivate::key() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryrefprivate.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractObjectRegistryRefPrivate::key() const
    return self.uglySide.call(
        'ritual_ZNK33QAbstractObjectRegistryRefPrivate3keyEv',
    )

  def registry(self) -> Optional[QObjectRegistrySingleton]:
    """
    Calls Qt's 'QObjectRegistrySingleton
    *QAbstractObjectRegistryRefPrivate::registry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryrefprivate.html#registry

    Returns
    -------

    Optional[QObjectRegistrySingleton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObjectRegistrySingleton
    #      *QAbstractObjectRegistryRefPrivate::registry() const
    address = self.uglySide.call(
        'ritual_ZNK33QAbstractObjectRegistryRefPrivate8registryEv',
    )
    from . import QObjectRegistrySingleton
    return QObjectRegistrySingleton._cuteAt(address)

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
    'QAbstractObjectRegistryRefPrivate::QAbstractObjectRegistryRefPrivate(
    QQmlEngine *engine)': the class is abstract, so C++ cannot make one, and
    the C++ class of ours does not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QAbstractObjectRegistryRefPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QAbstractObjectRegistryRefPrivate::QAbstractObjectRegistryRefPriva"
        "te(QQmlEngine *engine)': the class is abstract, so C++ cannot make "
        "one, and the C++ class of ours does not fill in every function it "
        "leaves open.")

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

  def q_func(self) -> Optional[QAbstractObjectRegistryRef]:
    """
    Calls Qt's 'QAbstractObjectRegistryRef
    *QAbstractObjectRegistryRefPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryrefprivate.html#q_func

    Returns
    -------

    Optional[QAbstractObjectRegistryRef]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractObjectRegistryRef
    #      *QAbstractObjectRegistryRefPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN33QAbstractObjectRegistryRefPrivate6q_funcEv',
    )
    from . import QAbstractObjectRegistryRef
    return QAbstractObjectRegistryRef._cuteAt(address)

  @overload(QObject)
  @overload(NoneType)
  def handleObjectAdded(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QAbstractObjectRegistryRefPrivate::handleObjectAdded(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryrefprivate.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractObjectRegistryRefPrivate::handleObjectAdded(QObject
    #      *obj)
    self.uglySide.call(
        'ritual_ZN33QAbstractObjectRegistryRefPrivate17handleObjectAddedEP7'
        'QObject',
        self._addressOf(obj, 'QObject'),
    )

  @overload(QObject)
  @overload(NoneType)
  def handleObjectRemoved(self, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void
    QAbstractObjectRegistryRefPrivate::handleObjectRemoved(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryrefprivate.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractObjectRegistryRefPrivate::handleObjectRemoved(QObject
    #      *obj)
    self.uglySide.call(
        'ritual_ZN33QAbstractObjectRegistryRefPrivate19handleObjectRemovedE'
        'P7QObject',
        self._addressOf(obj, 'QObject'),
    )

  def handleInitialObjects(self) -> None:
    """
    Calls Qt's 'void
    QAbstractObjectRegistryRefPrivate::handleInitialObjects()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryrefprivate.html
    """
    #  void QAbstractObjectRegistryRefPrivate::handleInitialObjects()
    self.uglySide.call(
        'ritual_ZN33QAbstractObjectRegistryRefPrivate20handleInitialObjects'
        'Ev',
    )

  @staticmethod
  def dataAppend(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractObjectRegistryRefPrivate::dataAppend(QQmlListProperty<QObject>
    *l, QObject *o)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QAbstractObjectRegistryRefPrivate.dataAppend' has no cute "
        "function yet. Qt's 'void "
        "QAbstractObjectRegistryRefPrivate::dataAppend(QQmlListProperty<QObj"
        "ect> *l, QObject *o)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def dataAt(*__, **_) -> Never:
    """
    Qt's 'QObject
    *QAbstractObjectRegistryRefPrivate::dataAt(QQmlListProperty<QObject> *l,
    qsizetype i)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QAbstractObjectRegistryRefPrivate.dataAt' has no cute function "
        "yet. Qt's 'QObject "
        "*QAbstractObjectRegistryRefPrivate::dataAt(QQmlListProperty<QObject"
        "> *l, qsizetype i)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def dataClear(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractObjectRegistryRefPrivate::dataClear(QQmlListProperty<QObject>
    *l)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractObjectRegistryRefPrivate.dataClear' has no cute function "
        "yet. Qt's 'void "
        "QAbstractObjectRegistryRefPrivate::dataClear(QQmlListProperty<QObje"
        "ct> *l)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def dataCount(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QAbstractObjectRegistryRefPrivate::dataCount(QQmlListProperty<QObject>
    *l)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractObjectRegistryRefPrivate.dataCount' has no cute function "
        "yet. Qt's 'qsizetype "
        "QAbstractObjectRegistryRefPrivate::dataCount(QQmlListProperty<QObje"
        "ct> *l)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def dataRemoveLast(*__, **_) -> Never:
    """
    Qt's 'void QAbstractObjectRegistryRefPrivate::dataRemoveLast(
    QQmlListProperty<QObject> *l)': names 'QQmlListProperty<QObject>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractObjectRegistryRefPrivate.dataRemoveLast' has no cute "
        "function yet. Qt's 'void "
        "QAbstractObjectRegistryRefPrivate::dataRemoveLast(QQmlListProperty<"
        "QObject> *l)': names 'QQmlListProperty<QObject>', which has no "
        "cute class yet.")

  @staticmethod
  def dataReplace(*__, **_) -> Never:
    """
    Qt's 'void
    QAbstractObjectRegistryRefPrivate::dataReplace(QQmlListProperty<QObject>
    *l, qsizetype i, QObject *o)': names 'QQmlListProperty<QObject>', which
    has no cute class yet.
    """
    raise NotImplementedError(
        "'QAbstractObjectRegistryRefPrivate.dataReplace' has no cute "
        "function yet. Qt's 'void "
        "QAbstractObjectRegistryRefPrivate::dataReplace(QQmlListProperty<QOb"
        "ject> *l, qsizetype i, QObject *o)': names "
        "'QQmlListProperty<QObject>', which has no cute class yet.")
