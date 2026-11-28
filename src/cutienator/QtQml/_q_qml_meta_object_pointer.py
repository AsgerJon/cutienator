"""
QQmlMetaObjectPointer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlpropertycache_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlMetaObjectPointer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaObject = WAIT['QMetaObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlMetaObjectPointer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlMetaObjectPointer: a plain Python object standing
  in front of one C++ QQmlMetaObjectPointer.

  What exists
  -----------

  Every function of Qt's QQmlMetaObjectPointer that has a ritual and that
  Python can call so far, 4 names in all: 'setSharedOnce', 'metaObject',
  'isShared', 'isNull'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlMetaObjectPointer::~QQmlMetaObjectPointer()': the destructor:
    Python never removes a C++ QQmlMetaObjectPointer.
  - Qt's 'QQmlMetaObjectPointer::QQmlMetaObjectPointer(const
    QQmlMetaObjectPointer &other)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  3 of the 11 functions Qt declares: 3 forbidden.

  What to expect
  --------------

  - The C++ QQmlMetaObjectPointer is created at the first use, not by
    'QQmlMetaObjectPointer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlMetaObjectPointer.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlMetaObjectPointer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlMetaObjectPointer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetaobjectpointer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlMetaObjectPointer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQmlMetaObjectPointer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isShared(self) -> bool:
    """
    Calls Qt's 'bool QQmlMetaObjectPointer::isShared() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetaobjectpointer.html#isShared
    """
    #  bool QQmlMetaObjectPointer::isShared() const
    return self.uglySide.call('ritual_ZNK21QQmlMetaObjectPointer8isSharedEv')

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQmlMetaObjectPointer::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlmetaobjectpointer.html#isNull
    """
    #  bool QQmlMetaObjectPointer::isNull() const
    return self.uglySide.call('ritual_ZNK21QQmlMetaObjectPointer6isNullEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMetaObject)
  @overload(NoneType)
  def setSharedOnce(self, shared: Optional[QMetaObject]) -> None:
    """
    Calls Qt's 'void QQmlMetaObjectPointer::setSharedOnce(QMetaObject
    *shared) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetaobjectpointer.html#setSharedOnce

    Parameters
    ----------

    shared : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlMetaObjectPointer::setSharedOnce(QMetaObject *shared) const
    self.uglySide.call(
        'ritual_ZNK21QQmlMetaObjectPointer13setSharedOnceEP11QMetaObject',
        self._addressOf(shared, 'QMetaObject'),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlMetaObjectPointer::QQmlMetaObjectPointer()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetaobjectpointer.html#QQmlMetaObjectPointer
    """
    #  QQmlMetaObjectPointer::QQmlMetaObjectPointer()
    self._noteCreation(QQmlMetaObjectPointer, lambda: Rituals.call(
        'ritual_ZN21QQmlMetaObjectPointerC1Ev',
    ))

  @overload(QMetaObject)
  @overload(NoneType)
  def __init__(self, staticMetaObject: Optional[QMetaObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQmlMetaObjectPointer::QQmlMetaObjectPointer(const QMetaObject
    *staticMetaObject)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlmetaobjectpointer.html#QQmlMetaObjectPointer

    Parameters
    ----------

    staticMetaObject : Optional[QMetaObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlMetaObjectPointer::QQmlMetaObjectPointer(const QMetaObject
    #      *staticMetaObject)
    self._noteCreation(QQmlMetaObjectPointer, lambda: Rituals.call(
        'ritual_ZN21QQmlMetaObjectPointerC1EPK11QMetaObject',
        self._addressOf(staticMetaObject, 'QMetaObject'),
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
