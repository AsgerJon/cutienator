"""
QObjectRegistrySingleton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlDesignSupport/6.12.0/QtQmlDesignSupport/private/qobjectregistrysingleton_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QObjectRegistrySingleton to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QQmlEngine
  from . import QAbstractObjectRegistryRefPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractObjectRegistryRefPrivate = WAIT['QAbstractObjectRegistryRefPrivate']
  QQmlEngine = WAIT['QQmlEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObjectRegistrySingleton(QObject):
  """
  The cute side of Qt's QObjectRegistrySingleton: a plain Python object
  standing in front of one C++ QObjectRegistrySingleton.

  It is built on the cute 'QObject', as Qt's QObjectRegistrySingleton is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QObjectRegistrySingleton that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'registerRef',
  'deregisterRef', 'add', 'remove', 'registryForObject', 'registryForEngine'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QObjectRegistrySingleton::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QObjectRegistrySingleton::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QObjectRegistrySingleton::qt_qmlMarker_singleton()': one of
    Qt's own inner workings.
  - Qt's 'QObjectRegistrySingleton::~QObjectRegistrySingleton()': the
    destructor: Python never removes a C++ QObjectRegistrySingleton.
  - Qt's 'QSet<QObject *> QObjectRegistrySingleton::objects(const QString
    &key) const': gives a type Python has no way to take yet.
  - Qt's 'void QObjectRegistrySingleton::notifyRefs(const QString &key,
    QObject *obj, Notification notification)': names the enum
    'QObjectRegistrySingleton::Notification', whose class cannot be named
    here.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QObjectRegistrySingleton is created at the first use, not by
    'QObjectRegistrySingleton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QObjectRegistrySingleton.
  - Qt tells when it has removed the C++ QObjectRegistrySingleton. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QObjectRegistrySingleton that has no cute function yet,
    'notifyRefs', 'objects', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QObjectRegistrySingleton::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectregistrysingleton.html#tr

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
    #  QString QObjectRegistrySingleton::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QObjectRegistrySingleton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def registryForObject(
      obj: Optional[QObject],
  ) -> Optional[QObjectRegistrySingleton]:
    """
    Calls Qt's 'QObjectRegistrySingleton
    *QObjectRegistrySingleton::registryForObject(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistrysingleton.html#registryForObject

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObjectRegistrySingleton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObjectRegistrySingleton
    #      *QObjectRegistrySingleton::registryForObject(QObject *obj)
    address = Rituals.call(
        'ritual_ZN24QObjectRegistrySingleton17registryForObjectEP7QObject',
        CuteMixin._addressOf(obj, 'QObject'),
    )
    return QObjectRegistrySingleton._cuteAt(address)

  @staticmethod
  @overload(QQmlEngine)
  @overload(NoneType)
  def registryForEngine(
      engine: Optional[QQmlEngine],
  ) -> Optional[QObjectRegistrySingleton]:
    """
    Calls Qt's 'QObjectRegistrySingleton
    *QObjectRegistrySingleton::registryForEngine(QQmlEngine *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistrysingleton.html#registryForEngine

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObjectRegistrySingleton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObjectRegistrySingleton
    #      *QObjectRegistrySingleton::registryForEngine(QQmlEngine *engine)
    address = Rituals.call(
        'ritual_ZN24QObjectRegistrySingleton17registryForEngineEP10QQmlEngi'
        'ne',
        CuteMixin._addressOf(engine),
    )
    return QObjectRegistrySingleton._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QObjectRegistrySingleton'

  #  A C++ QObjectRegistrySingleton Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QObjectRegistrySingleton'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QObjectRegistrySingleton::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistrysingleton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QObjectRegistrySingleton::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QObjectRegistrySingleton10metaObjectEv',
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QObjectRegistrySingleton::QObjectRegistrySingleton(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistrysingleton.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QObjectRegistrySingleton::QObjectRegistrySingleton(QObject *parent)
    self._noteCreation(QObjectRegistrySingleton, lambda: Rituals.call(
        'ritual_ZN24QObjectRegistrySingletonC1EP7QObject',
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

  @overload(QAbstractObjectRegistryRefPrivate)
  @overload(NoneType)
  def registerRef(
      self,
      ref: Optional[QAbstractObjectRegistryRefPrivate],
  ) -> None:
    """
    Calls Qt's 'void
    QObjectRegistrySingleton::registerRef(QAbstractObjectRegistryRefPrivate
    *ref)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistrysingleton.html#registerRef

    Parameters
    ----------

    ref : Optional[QAbstractObjectRegistryRefPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectRegistrySingleton::registerRef(
    #      QAbstractObjectRegistryRefPrivate *ref)
    self.uglySide.call(
        'ritual_ZN24QObjectRegistrySingleton11registerRefEP33QAbstractObjec'
        'tRegistryRefPrivate',
        self._addressOf(ref),
    )

  @overload(QAbstractObjectRegistryRefPrivate)
  @overload(NoneType)
  def deregisterRef(
      self,
      ref: Optional[QAbstractObjectRegistryRefPrivate],
  ) -> None:
    """
    Calls Qt's 'void
    QObjectRegistrySingleton::deregisterRef(QAbstractObjectRegistryRefPrivate
    *ref)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistrysingleton.html#deregisterRef

    Parameters
    ----------

    ref : Optional[QAbstractObjectRegistryRefPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectRegistrySingleton::deregisterRef(
    #      QAbstractObjectRegistryRefPrivate *ref)
    self.uglySide.call(
        'ritual_ZN24QObjectRegistrySingleton13deregisterRefEP33QAbstractObj'
        'ectRegistryRefPrivate',
        self._addressOf(ref),
    )

  @overload(str, QObject)
  @overload(str, NoneType)
  def add(self, key: str, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObjectRegistrySingleton::add(const QString &key,
    QObject *obj)'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectregistrysingleton.html#add

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectRegistrySingleton::add(const QString &key, QObject *obj)
    self.uglySide.call(
        'ritual_ZN24QObjectRegistrySingleton3addERK7QStringP7QObject',
        key, self._addressOf(obj, 'QObject'),
    )

  @overload(str, QObject)
  @overload(str, NoneType)
  def remove(self, key: str, obj: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObjectRegistrySingleton::remove(const QString &key,
    QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistrysingleton.html#remove

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectRegistrySingleton::remove(const QString &key, QObject
    #      *obj)
    self.uglySide.call(
        'ritual_ZN24QObjectRegistrySingleton6removeERK7QStringP7QObject',
        key, self._addressOf(obj, 'QObject'),
    )

  @staticmethod
  def notifyRefs(*__, **_) -> Never:
    """
    Qt's 'void QObjectRegistrySingleton::notifyRefs(const QString &key,
    QObject *obj, Notification notification)': names the enum
    'QObjectRegistrySingleton::Notification', whose class cannot be named
    here.
    """
    raise NotImplementedError(
        "'QObjectRegistrySingleton.notifyRefs' has no cute function yet. "
        "Qt's 'void QObjectRegistrySingleton::notifyRefs(const QString "
        "&key, QObject *obj, Notification notification)': names the enum "
        "'QObjectRegistrySingleton::Notification', whose class cannot be "
        "named here.")

  @staticmethod
  def objects(*__, **_) -> Never:
    """
    Qt's 'QSet<QObject *> QObjectRegistrySingleton::objects(const QString
    &key) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QObjectRegistrySingleton.objects' has no cute function yet. Qt's "
        "'QSet<QObject *> QObjectRegistrySingleton::objects(const QString "
        "&key) const': gives a type Python has no way to take yet.")
