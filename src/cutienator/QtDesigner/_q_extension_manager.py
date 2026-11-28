"""
QExtensionManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/qextensionmanager.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractExtensionManager

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAbstractExtensionFactory
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractExtensionFactory = WAIT['QAbstractExtensionFactory']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QExtensionManager(QObject, QAbstractExtensionManager):
  """
  The cute side of Qt's QExtensionManager: a plain Python object standing in
  front of one C++ QExtensionManager.

  It is built on the cute 'QObject', as Qt's QExtensionManager is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QAbstractExtensionManager' as well, as Qt's QExtensionManager is built on
  Qt's QAbstractExtensionManager too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QExtensionManager that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'tr', 'registerExtensions',
  'unregisterExtensions', 'extension'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QExtensionManager::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QExtensionManager::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QExtensionManager::~QExtensionManager()': the destructor: Python
    never removes a C++ QExtensionManager.

  What has no ritual
  ------------------

  2 of the 11 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QExtensionManager is created at the first use, not by
    'QExtensionManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QExtensionManager.
  - Qt tells when it has removed the C++ QExtensionManager. Every call on the
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
    Calls Qt's 'QString QExtensionManager::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qextensionmanager.html#tr

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
    #  QString QExtensionManager::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QExtensionManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QExtensionManager'

  #  Qt's QExtensionManager is built on more than one class. The part of a
  #  C++ QExtensionManager that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAbstractExtensionManager':
          'ritual_cast_QExtensionManager_QAbstractExtensionManager',
  }

  #  A C++ QExtensionManager Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QExtensionManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QExtensionManager::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qextensionmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QExtensionManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QExtensionManager10metaObjectEv',
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
    Calls Qt's 'QObject *QExtensionManager::extension(QObject *object, const
    QString &iid) const'.

    Qt's own words: https://doc.qt.io/qt-6/qextensionmanager.html#extension

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
    #  QObject *QExtensionManager::extension(QObject *object, const QString
    #      &iid) const
    ritual = 'ritual_ZNK17QExtensionManager9extensionEP7QObjectRK7QString'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK17QExtensionManager9extensionEP7QObjectRK7QString')
    address = self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), iid,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QExtensionManager::QExtensionManager(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qextensionmanager.html#QExtensionManager

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QExtensionManager::QExtensionManager(QObject *parent)
    self._noteCreation(QExtensionManager, lambda: Rituals.call(
        'ritual_ZN17QExtensionManagerC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QAbstractExtensionFactory)
  @overload(NoneType)
  @overload(QAbstractExtensionFactory, str)
  @overload(NoneType, str)
  def registerExtensions(
      self,
      factory: Optional[QAbstractExtensionFactory],
      iid: str = '',
  ) -> None:
    """
    Calls Qt's 'void
    QExtensionManager::registerExtensions(QAbstractExtensionFactory *factory,
    const QString &iid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qextensionmanager.html#registerExtensions

    Parameters
    ----------

    factory : Optional[QAbstractExtensionFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iid : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QExtensionManager::registerExtensions(QAbstractExtensionFactory
    #      *factory, const QString &iid)
    ritual = (
        'ritual_ZN17QExtensionManager18registerExtensionsEP25QAbstractExten'
        'sionFactoryRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QExtensionManager18registerExtensionsEP25QAbstrac'
          'tExtensionFactoryRK7QString')
    self.uglySide.call(
        ritual, self._addressOf(factory, 'QAbstractExtensionFactory'), iid,
    )

  @overload(QAbstractExtensionFactory)
  @overload(NoneType)
  @overload(QAbstractExtensionFactory, str)
  @overload(NoneType, str)
  def unregisterExtensions(
      self,
      factory: Optional[QAbstractExtensionFactory],
      iid: str = '',
  ) -> None:
    """
    Calls Qt's 'void
    QExtensionManager::unregisterExtensions(QAbstractExtensionFactory
    *factory, const QString &iid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qextensionmanager.html#unregisterExtensions

    Parameters
    ----------

    factory : Optional[QAbstractExtensionFactory]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    iid : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QExtensionManager::unregisterExtensions(QAbstractExtensionFactory
    #      *factory, const QString &iid)
    ritual = (
        'ritual_ZN17QExtensionManager20unregisterExtensionsEP25QAbstractExt'
        'ensionFactoryRK7QString')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QExtensionManager20unregisterExtensionsEP25QAbstr'
          'actExtensionFactoryRK7QString')
    self.uglySide.call(
        ritual, self._addressOf(factory, 'QAbstractExtensionFactory'), iid,
    )
