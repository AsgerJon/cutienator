"""
QObjectRegistryRef binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlDesignSupport/qobjectregistryref.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QAbstractObjectRegistryRef

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtQml import QQmlEngine
  from . import QObjectRegistryRefPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QQmlEngine = WAIT['QQmlEngine']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QObjectRegistryRef(QAbstractObjectRegistryRef):
  """
  The cute side of Qt's QObjectRegistryRef: a plain Python object standing in
  front of one C++ QObjectRegistryRef.

  It is built on the cute 'QAbstractObjectRegistryRef', as Qt's
  QObjectRegistryRef is built on Qt's QAbstractObjectRegistryRef, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QObjectRegistryRef that has a ritual and that Python
  can call so far, 6 names in all: 'metaObject', 'tr', 'd_func', 'object',
  'event', 'objectChanged'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QObjectRegistryRef::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QObjectRegistryRef::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QObjectRegistryRefPrivate *QObjectRegistryRef::d_func()
    const': takes in Python what 'QObjectRegistryRefPrivate
    *QObjectRegistryRef::d_func()' takes.
  - Qt's 'QObjectRegistryRef::~QObjectRegistryRef()': the destructor: Python
    never removes a C++ QObjectRegistryRef.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QObjectRegistryRef is created at the first use, not by
    'QObjectRegistryRef(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QObjectRegistryRef.
  - Qt tells when it has removed the C++ QObjectRegistryRef. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QObjectRegistryRef::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectregistryref.html#tr

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
    #  QString QObjectRegistryRef::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QObjectRegistryRef2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QObjectRegistryRef'

  #  A C++ QObjectRegistryRef Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QObjectRegistryRef'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QObjectRegistryRef::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectregistryref.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QObjectRegistryRef::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QObjectRegistryRef10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def object(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QObjectRegistryRef::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectregistryref.html#object

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QObjectRegistryRef::object() const
    address = self.uglySide.call('ritual_ZNK18QObjectRegistryRef6objectEv')
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

  @overload(QQmlEngine)
  @overload(QQmlEngine, QObject)
  @overload(QQmlEngine, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QQmlEngine],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QObjectRegistryRef::QObjectRegistryRef(QQmlEngine *engine, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistryref.html#QObjectRegistryRef

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QObjectRegistryRef::QObjectRegistryRef(QQmlEngine *engine, QObject
    #      *parent)
    self._noteCreation(QObjectRegistryRef, lambda: Rituals.call(
        'ritual_ZN18QObjectRegistryRefC1EP10QQmlEngineP7QObject',
        self._addressOf(engine), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QObjectRegistryRef::QObjectRegistryRef(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistryref.html#QObjectRegistryRef

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QObjectRegistryRef::QObjectRegistryRef(QObject *parent)
    self._noteCreation(QObjectRegistryRef, lambda: Rituals.call(
        'ritual_ZN18QObjectRegistryRefC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(QQmlEngine, str)
  @overload(NoneType, str)
  @overload(QQmlEngine, str, QObject)
  @overload(QQmlEngine, str, NoneType)
  @overload(NoneType, str, QObject)
  @overload(NoneType, str, NoneType)
  def __init__(
      self,
      engine: Optional[QQmlEngine],
      key: str,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QObjectRegistryRef::QObjectRegistryRef(QQmlEngine *engine, const QString
    &key, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistryref.html#QObjectRegistryRef

    Parameters
    ----------

    engine : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    key : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QObjectRegistryRef::QObjectRegistryRef(QQmlEngine *engine, const
    #      QString &key, QObject *parent)
    self._noteCreation(QObjectRegistryRef, lambda: Rituals.call(
        'ritual_ZN18QObjectRegistryRefC1EP10QQmlEngineRK7QStringP7QObject',
        self._addressOf(engine), key, self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QObjectRegistryRefPrivate]:
    """
    Calls Qt's 'QObjectRegistryRefPrivate *QObjectRegistryRef::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectregistryref.html#d_func

    Returns
    -------

    Optional[QObjectRegistryRefPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObjectRegistryRefPrivate *QObjectRegistryRef::d_func()
    address = self.uglySide.call('ritual_ZN18QObjectRegistryRef6d_funcEv')
    from . import QObjectRegistryRefPrivate
    return QObjectRegistryRefPrivate._cuteAt(address)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QObjectRegistryRef::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qobjectregistryref.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QObjectRegistryRef::event(QEvent *a0)
    ritual = 'ritual_ZN18QObjectRegistryRef5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QObjectRegistryRef5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QObject)
  @overload(NoneType)
  def objectChanged(self, object: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QObjectRegistryRef::objectChanged(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qobjectregistryref.html#objectChanged

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QObjectRegistryRef::objectChanged(QObject *object)
    self.uglySide.call(
        'ritual_ZN18QObjectRegistryRef13objectChangedEP7QObject',
        self._addressOf(object, 'QObject'),
    )
