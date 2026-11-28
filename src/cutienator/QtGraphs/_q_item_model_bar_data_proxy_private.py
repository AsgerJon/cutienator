"""
QItemModelBarDataProxyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qitemmodelbardataproxy_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QItemModelBarDataProxyPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QBarDataProxyPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QItemModelBarDataProxy


class QItemModelBarDataProxyPrivate(QBarDataProxyPrivate):
  """
  The cute side of Qt's QItemModelBarDataProxyPrivate: a plain Python object
  standing in front of one C++ QItemModelBarDataProxyPrivate.

  It is built on the cute 'QBarDataProxyPrivate', as Qt's
  QItemModelBarDataProxyPrivate is built on Qt's QBarDataProxyPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QItemModelBarDataProxyPrivate that has a ritual and
  that Python can call so far, 1 name in all: 'q_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QItemModelBarDataProxy
    *QItemModelBarDataProxyPrivate::q_func() const': takes in Python what
    'QItemModelBarDataProxy *QItemModelBarDataProxyPrivate::q_func()' takes.
  - Qt's 'QItemModelBarDataProxyPrivate::~QItemModelBarDataProxyPrivate()':
    the destructor: Python never removes a C++ QItemModelBarDataProxyPrivate.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 leans on 'AbstractItemModelHandler; 1
  leans on 'vtable for BarItemModelHandler', which Qt's source does not mark
  for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QItemModelBarDataProxyPrivate is created at the first use, not by
    'QItemModelBarDataProxyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QItemModelBarDataProxyPrivate.
  - Each name of Qt's QItemModelBarDataProxyPrivate that has no cute function
    yet, '__init__', 'connectItemModelHandler', holds a function that raises
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
  __qt_class__ = 'QItemModelBarDataProxyPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QItemModelBarDataProxyPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QItemModelBarDataProxyPrivate'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QItemModelBarDataProxyPrivate::QItemModelBarDataProxyPrivate(
    QItemModelBarDataProxy *q)': leans on 'vtable for BarItemModelHandler',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QItemModelBarDataProxyPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QItemModelBarDataProxyPrivate::QItemModelBarDataProxyPrivate(QItem"
        "ModelBarDataProxy *q)': leans on 'vtable for BarItemModelHandler', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def q_func(self) -> Optional[QItemModelBarDataProxy]:
    """
    Calls Qt's 'QItemModelBarDataProxy
    *QItemModelBarDataProxyPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelbardataproxyprivate.html#q_func

    Returns
    -------

    Optional[QItemModelBarDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemModelBarDataProxy *QItemModelBarDataProxyPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN29QItemModelBarDataProxyPrivate6q_funcEv',
    )
    from . import QItemModelBarDataProxy
    return QItemModelBarDataProxy._cuteAt(address)

  @staticmethod
  def connectItemModelHandler(*__, **_) -> Never:
    """
    Qt's 'void QItemModelBarDataProxyPrivate::connectItemModelHandler()':
    leans on 'AbstractItemModelHandler::itemModelChanged(QAbstractItemModel
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QItemModelBarDataProxyPrivate.connectItemModelHandler' has no "
        "cute function yet. Qt's 'void "
        "QItemModelBarDataProxyPrivate::connectItemModelHandler()': leans "
        "on 'AbstractItemModelHandler::itemModelChanged(QAbstractItemModel "
        "const*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
