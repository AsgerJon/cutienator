"""
QQmlComponentAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlcomponentattached_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlComponentAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlComponentAttached(QObject):
  """
  The cute side of Qt's QQmlComponentAttached: a plain Python object standing
  in front of one C++ QQmlComponentAttached.

  It is built on the cute 'QObject', as Qt's QQmlComponentAttached is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlComponentAttached that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr',
  'removeFromList', 'next', 'completed', 'destruction'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlComponentAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlComponentAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlComponentAttached::~QQmlComponentAttached()': the destructor:
    Python never removes a C++ QQmlComponentAttached.
  - Qt's 'void QQmlComponentAttached::insertIntoList(QQmlComponentAttached
    **listHead)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlComponentAttached is created at the first use, not by
    'QQmlComponentAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlComponentAttached.
  - Qt tells when it has removed the C++ QQmlComponentAttached. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlComponentAttached that has no cute function yet,
    'insertIntoList', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QQmlComponentAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentattached.html#tr

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
    #  QString QQmlComponentAttached::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQmlComponentAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlComponentAttached'

  #  A C++ QQmlComponentAttached Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlComponentAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlComponentAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlComponentAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlComponentAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def next(self) -> Optional[QQmlComponentAttached]:
    """
    Calls Qt's 'QQmlComponentAttached *QQmlComponentAttached::next() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcomponentattached.html#next

    Returns
    -------

    Optional[QQmlComponentAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponentAttached *QQmlComponentAttached::next() const
    address = self.uglySide.call('ritual_ZNK21QQmlComponentAttached4nextEv')
    return QQmlComponentAttached._cuteAt(address)

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
    'QQmlComponentAttached::QQmlComponentAttached(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentattached.html#QQmlComponentAttached

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlComponentAttached::QQmlComponentAttached(QObject *parent)
    self._noteCreation(QQmlComponentAttached, lambda: Rituals.call(
        'ritual_ZN21QQmlComponentAttachedC1EP7QObject',
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

  def removeFromList(self) -> None:
    """
    Calls Qt's 'void QQmlComponentAttached::removeFromList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentattached.html#removeFromList
    """
    #  void QQmlComponentAttached::removeFromList()
    self.uglySide.call('ritual_ZN21QQmlComponentAttached14removeFromListEv')

  def completed(self) -> None:
    """
    Calls Qt's 'void QQmlComponentAttached::completed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentattached.html#completed
    """
    #  void QQmlComponentAttached::completed()
    self.uglySide.call('ritual_ZN21QQmlComponentAttached9completedEv')

  def destruction(self) -> None:
    """
    Calls Qt's 'void QQmlComponentAttached::destruction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlcomponentattached.html#destruction
    """
    #  void QQmlComponentAttached::destruction()
    self.uglySide.call('ritual_ZN21QQmlComponentAttached11destructionEv')

  @staticmethod
  def insertIntoList(*__, **_) -> Never:
    """
    Qt's 'void QQmlComponentAttached::insertIntoList(QQmlComponentAttached
    **listHead)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlComponentAttached.insertIntoList' has no cute function yet. "
        "Qt's 'void "
        "QQmlComponentAttached::insertIntoList(QQmlComponentAttached "
        "**listHead)': takes a type Python has no way to hand over yet.")
