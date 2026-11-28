"""
QItemModelScatterDataProxyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qitemmodelscatterdataproxy_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QItemModelScatterDataProxyPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QScatterDataProxyPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QItemModelScatterDataProxy


class QItemModelScatterDataProxyPrivate(QScatterDataProxyPrivate):
  """
  The cute side of Qt's QItemModelScatterDataProxyPrivate: a plain Python
  object standing in front of one C++ QItemModelScatterDataProxyPrivate.

  It is built on the cute 'QScatterDataProxyPrivate', as Qt's
  QItemModelScatterDataProxyPrivate is built on Qt's
  QScatterDataProxyPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QItemModelScatterDataProxyPrivate that has a ritual
  and that Python can call so far, 2 names in all: 'metaObject', 'qptr'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QItemModelScatterDataProxyPrivate::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QItemModelScatterDataProxyPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QItemModelScatterDataProxyPrivate::~QItemModelScatterDataProxyPrivate(
    )': the destructor: Python never removes a C++
    QItemModelScatterDataProxyPrivate.

  What has no ritual
  ------------------

  5 of the 10 functions Qt declares: 2 not a gap; 2 leans on
  'QItemModelScatterDataProxyPrivate; 1 leans on 'AbstractItemModelHandler.

  What to expect
  --------------

  - The C++ QItemModelScatterDataProxyPrivate is created at the first use,
    not by 'QItemModelScatterDataProxyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QItemModelScatterDataProxyPrivate.
  - Qt tells when it has removed the C++ QItemModelScatterDataProxyPrivate.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QItemModelScatterDataProxyPrivate that has no cute
    function yet, '__init__', 'connectItemModelHandler', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QItemModelScatterDataProxyPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QItemModelScatterDataProxyPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QItemModelScatterDataProxyPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QItemModelScatterDataProxyPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxyprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QItemModelScatterDataProxyPrivate::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QItemModelScatterDataProxyPrivate10metaObjectEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'QItemModelScatterDataProxyPrivate::QItemModelScatterDataProxyPrivate(
    QItemModelScatterDataProxy *q)': leans on
    'QItemModelScatterDataProxyPrivate::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QItemModelScatterDataProxyPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QItemModelScatterDataProxyPrivate::QItemModelScatterDataProxyPriva"
        "te(QItemModelScatterDataProxy *q)': leans on "
        "'QItemModelScatterDataProxyPrivate::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

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

  def qptr(self) -> Optional[QItemModelScatterDataProxy]:
    """
    Calls Qt's 'QItemModelScatterDataProxy
    *QItemModelScatterDataProxyPrivate::qptr()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelscatterdataproxyprivate.html#qptr

    Returns
    -------

    Optional[QItemModelScatterDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemModelScatterDataProxy *QItemModelScatterDataProxyPrivate::qptr()
    address = self.uglySide.call(
        'ritual_ZN33QItemModelScatterDataProxyPrivate4qptrEv',
    )
    from . import QItemModelScatterDataProxy
    return QItemModelScatterDataProxy._cuteAt(address)

  @staticmethod
  def connectItemModelHandler(*__, **_) -> Never:
    """
    Qt's 'void QItemModelScatterDataProxyPrivate::connectItemModelHandler()':
    leans on 'AbstractItemModelHandler::itemModelChanged(QAbstractItemModel
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QItemModelScatterDataProxyPrivate.connectItemModelHandler' has no "
        "cute function yet. Qt's 'void "
        "QItemModelScatterDataProxyPrivate::connectItemModelHandler()': "
        "leans on "
        "'AbstractItemModelHandler::itemModelChanged(QAbstractItemModel "
        "const*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
