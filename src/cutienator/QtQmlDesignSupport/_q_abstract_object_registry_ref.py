"""
QAbstractObjectRegistryRef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlDesignSupport/qabstractobjectregistryref.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QAbstractObjectRegistryRefPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractObjectRegistryRef(QObject):
  """
  The cute side of Qt's QAbstractObjectRegistryRef: a plain Python object
  standing in front of one C++ QAbstractObjectRegistryRef.

  It is built on the cute 'QObject', as Qt's QAbstractObjectRegistryRef is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractObjectRegistryRef that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'tr', 'd_func',
  'key', 'setKey', 'event', 'keyChanged', 'dataChanged'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractObjectRegistryRef::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QAbstractObjectRegistryRef::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QAbstractObjectRegistryRefPrivate
    *QAbstractObjectRegistryRef::d_func() const': takes in Python what
    'QAbstractObjectRegistryRefPrivate *QAbstractObjectRegistryRef::d_func()'
    takes.
  - Qt's 'void QAbstractObjectRegistryRef::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.
  - Qt's 'QAbstractObjectRegistryRef::~QAbstractObjectRegistryRef()': the
    destructor: Python never removes a C++ QAbstractObjectRegistryRef.
  - Qt's 'QQmlListProperty<QObject> QAbstractObjectRegistryRef::data()':
    gives a type Python has no way to take yet.
  - Qt's 'QAbstractObjectRegistryRef::QAbstractObjectRegistryRef(
    QAbstractObjectRegistryRefPrivate &dd, QObject *parent)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QAbstractObjectRegistryRef is created at the first use, not by
    'QAbstractObjectRegistryRef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractObjectRegistryRef.
  - Qt tells when it has removed the C++ QAbstractObjectRegistryRef. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QAbstractObjectRegistryRef that has no cute function
    yet, '__init__', 'data', holds a function that raises
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
    Calls Qt's 'QString QAbstractObjectRegistryRef::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractobjectregistryref.html#tr

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
    #  QString QAbstractObjectRegistryRef::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN26QAbstractObjectRegistryRef2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractObjectRegistryRef'

  #  A C++ QAbstractObjectRegistryRef Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractObjectRegistryRef'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractObjectRegistryRef::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryref.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractObjectRegistryRef::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK26QAbstractObjectRegistryRef10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def key(self) -> str:
    """
    Calls Qt's 'QString QAbstractObjectRegistryRef::key() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryref.html#key

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QAbstractObjectRegistryRef::key() const
    return self.uglySide.call('ritual_ZNK26QAbstractObjectRegistryRef3keyEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setKey(self, key: str) -> None:
    """
    Calls Qt's 'void QAbstractObjectRegistryRef::setKey(const QString &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryref.html#setKey

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractObjectRegistryRef::setKey(const QString &key)
    self.uglySide.call(
        'ritual_ZN26QAbstractObjectRegistryRef6setKeyERK7QString', key,
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
    Qt's 'QAbstractObjectRegistryRef::QAbstractObjectRegistryRef(
    QAbstractObjectRegistryRefPrivate &dd, QObject *parent)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QAbstractObjectRegistryRef.__init__' has no cute function yet. "
        "Qt's "
        "'QAbstractObjectRegistryRef::QAbstractObjectRegistryRef(QAbstractOb"
        "jectRegistryRefPrivate &dd, QObject *parent)': takes a type Python "
        "has no way to hand over yet.")

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

  def d_func(self) -> Optional[QAbstractObjectRegistryRefPrivate]:
    """
    Calls Qt's 'QAbstractObjectRegistryRefPrivate
    *QAbstractObjectRegistryRef::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryref.html#d_func

    Returns
    -------

    Optional[QAbstractObjectRegistryRefPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractObjectRegistryRefPrivate
    #      *QAbstractObjectRegistryRef::d_func()
    address = self.uglySide.call(
        'ritual_ZN26QAbstractObjectRegistryRef6d_funcEv',
    )
    from . import QAbstractObjectRegistryRefPrivate
    return QAbstractObjectRegistryRefPrivate._cuteAt(address)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QAbstractObjectRegistryRef::event(QEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryref.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QAbstractObjectRegistryRef::event(QEvent *a0)
    ritual = 'ritual_ZN26QAbstractObjectRegistryRef5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN26QAbstractObjectRegistryRef5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(str)
  def keyChanged(self, key: str) -> None:
    """
    Calls Qt's 'void QAbstractObjectRegistryRef::keyChanged(const QString
    &key)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryref.html#keyChanged

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QAbstractObjectRegistryRef::keyChanged(const QString &key)
    self.uglySide.call(
        'ritual_ZN26QAbstractObjectRegistryRef10keyChangedERK7QString', key,
    )

  def dataChanged(self) -> None:
    """
    Calls Qt's 'void QAbstractObjectRegistryRef::dataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractobjectregistryref.html#dataChanged
    """
    #  void QAbstractObjectRegistryRef::dataChanged()
    self.uglySide.call(
        'ritual_ZN26QAbstractObjectRegistryRef11dataChangedEv',
    )

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QAbstractObjectRegistryRef::data()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QAbstractObjectRegistryRef.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QAbstractObjectRegistryRef::data()': "
        "gives a type Python has no way to take yet.")
