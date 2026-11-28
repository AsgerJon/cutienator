"""
QExtensionFactory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/default_extensionfactory.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractExtensionFactory

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QExtensionManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QExtensionManager = WAIT['QExtensionManager']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QExtensionFactory(QObject, QAbstractExtensionFactory):
  """
  The cute side of Qt's QExtensionFactory: a plain Python object standing in
  front of one C++ QExtensionFactory.

  It is built on the cute 'QObject', as Qt's QExtensionFactory is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QAbstractExtensionFactory' as well, as Qt's QExtensionFactory is built on
  Qt's QAbstractExtensionFactory too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QExtensionFactory that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'extension',
  'extensionManager', 'objectDestroyed', 'createExtension'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QExtensionFactory::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QExtensionFactory::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QExtensionFactory is created at the first use, not by
    'QExtensionFactory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QExtensionFactory.
  - Qt tells when it has removed the C++ QExtensionFactory. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QExtensionFactory::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qextensionfactory.html#tr

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
    #  QString QExtensionFactory::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QExtensionFactory2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QExtensionFactory'

  #  Qt's QExtensionFactory is built on more than one class. The part of a
  #  C++ QExtensionFactory that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAbstractExtensionFactory':
          'ritual_cast_QExtensionFactory_QAbstractExtensionFactory',
  }

  #  The functions Qt calls itself that QExtensionFactory is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createExtension': (
          ('_ZNK17QExtensionFactory15createExtensionEP7QObjectRK7QStringS1_',
           ('address', 'address', 'QtCore:QObject'),
           (
               ('address', 'address', 'QtCore:QObject'),
               ('address', 'text', ''),
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QExtensionFactory::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qextensionfactory.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QExtensionFactory::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QExtensionFactory10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QObject, str)
  @overload(NoneType, str)
  def extension(
      self,
      object: Optional[QObject],
      iid: str,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QExtensionFactory::extension(QObject *object, const
    QString &iid) const'.

    Qt's own words: https://doc.qt.io/qt-6/qextensionfactory.html#extension

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iid : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QExtensionFactory::extension(QObject *object, const QString
    #      &iid) const
    ritual = 'ritual_ZNK17QExtensionFactory9extensionEP7QObjectRK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QExtensionFactory9extensionEP7QObjectRK7QString')
    address = self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), iid,
    )
    return QObject._cuteAt(address)

  def extensionManager(self) -> Optional[QExtensionManager]:
    """
    Calls Qt's 'QExtensionManager *QExtensionFactory::extensionManager()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qextensionfactory.html#extensionManager

    Returns
    -------

    Optional[QExtensionManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QExtensionManager *QExtensionFactory::extensionManager() const
    address = self.uglySide.call(
        'ritual_ZNK17QExtensionFactory16extensionManagerEv',
    )
    from . import QExtensionManager
    return QExtensionManager._cuteAt(address)

  @overload(QObject, str, QObject)
  @overload(QObject, str, NoneType)
  @overload(NoneType, str, QObject)
  @overload(NoneType, str, NoneType)
  def createExtension(
      self,
      object: Optional[QObject],
      iid: str,
      parent: Optional[QObject],
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QExtensionFactory::createExtension(QObject *object,
    const QString &iid, QObject *parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qextensionfactory.html#createExtension

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iid : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QExtensionFactory::createExtension(QObject *object, const
    #      QString &iid, QObject *parent) const
    ritual = (
        'ritual_ZNK17QExtensionFactory15createExtensionEP7QObjectRK7QString'
        'S1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QExtensionFactory15createExtensionEP7QObjectRK7Q'
          'StringS1_')
    address = self.uglySide.call(
        ritual,
        self._addressOf(object, 'QObject'), iid, self._addressOf(parent,
        'QObject'),
    )
    return QObject._cuteAt(address)

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
  @overload(QExtensionManager)
  @overload(NoneType)
  def __init__(self, parent: Optional[QExtensionManager] = None) -> None:
    """
    Notes what was given, for Qt's
    'QExtensionFactory::QExtensionFactory(QExtensionManager *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qextensionfactory.html#QExtensionFactory

    Parameters
    ----------

    parent : Optional[QExtensionManager]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QExtensionFactory::QExtensionFactory(QExtensionManager *parent)
    self._noteCreation(QExtensionFactory, lambda: Rituals.call(
        'ritual_ZN17QExtensionFactoryC1EP17QExtensionManager',
        self._addressOf(parent),
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

  @overload(QObject)
  @overload(NoneType)
  def objectDestroyed(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QExtensionFactory::objectDestroyed(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qextensionfactory.html#objectDestroyed

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QExtensionFactory::objectDestroyed(QObject *object)
    self.uglySide.call(
        'ritual_ZN17QExtensionFactory15objectDestroyedEP7QObject',
        self._addressOf(object, 'QObject'),
    )
