"""
QItemModelSurfaceDataProxyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qitemmodelsurfacedataproxy_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QItemModelSurfaceDataProxyPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QSurfaceDataProxyPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QItemModelSurfaceDataProxy


class QItemModelSurfaceDataProxyPrivate(QSurfaceDataProxyPrivate):
  """
  The cute side of Qt's QItemModelSurfaceDataProxyPrivate: a plain Python
  object standing in front of one C++ QItemModelSurfaceDataProxyPrivate.

  It is built on the cute 'QSurfaceDataProxyPrivate', as Qt's
  QItemModelSurfaceDataProxyPrivate is built on Qt's
  QSurfaceDataProxyPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QItemModelSurfaceDataProxyPrivate that has a ritual
  and that Python can call so far, 1 name in all: 'q_func'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QItemModelSurfaceDataProxy
    *QItemModelSurfaceDataProxyPrivate::q_func() const': takes in Python what
    'QItemModelSurfaceDataProxy *QItemModelSurfaceDataProxyPrivate::q_func()'
    takes.
  - Qt's
    'QItemModelSurfaceDataProxyPrivate::~QItemModelSurfaceDataProxyPrivate(
    )': the destructor: Python never removes a C++
    QItemModelSurfaceDataProxyPrivate.

  What has no ritual
  ------------------

  2 of the 5 functions Qt declares: 1 leans on 'AbstractItemModelHandler; 1
  leans on 'vtable for SurfaceItemModelHandler', which Qt's source does not
  mark for use from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QItemModelSurfaceDataProxyPrivate is created at the first use,
    not by 'QItemModelSurfaceDataProxyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QItemModelSurfaceDataProxyPrivate.
  - Each name of Qt's QItemModelSurfaceDataProxyPrivate that has no cute
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
  __qt_class__ = 'QItemModelSurfaceDataProxyPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QItemModelSurfaceDataProxyPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QItemModelSurfaceDataProxyPrivate'

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
    Qt's
    'QItemModelSurfaceDataProxyPrivate::QItemModelSurfaceDataProxyPrivate(
    QItemModelSurfaceDataProxy *q)': leans on 'vtable for
    SurfaceItemModelHandler', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QItemModelSurfaceDataProxyPrivate.__init__' has no cute function "
        "yet. Qt's "
        "'QItemModelSurfaceDataProxyPrivate::QItemModelSurfaceDataProxyPriva"
        "te(QItemModelSurfaceDataProxy *q)': leans on 'vtable for "
        "SurfaceItemModelHandler', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")

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

  def q_func(self) -> Optional[QItemModelSurfaceDataProxy]:
    """
    Calls Qt's 'QItemModelSurfaceDataProxy
    *QItemModelSurfaceDataProxyPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qitemmodelsurfacedataproxyprivate.html#q_func

    Returns
    -------

    Optional[QItemModelSurfaceDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QItemModelSurfaceDataProxy
    #      *QItemModelSurfaceDataProxyPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN33QItemModelSurfaceDataProxyPrivate6q_funcEv',
    )
    from . import QItemModelSurfaceDataProxy
    return QItemModelSurfaceDataProxy._cuteAt(address)

  @staticmethod
  def connectItemModelHandler(*__, **_) -> Never:
    """
    Qt's 'void QItemModelSurfaceDataProxyPrivate::connectItemModelHandler()':
    leans on 'AbstractItemModelHandler::itemModelChanged(QAbstractItemModel
    const*)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QItemModelSurfaceDataProxyPrivate.connectItemModelHandler' has no "
        "cute function yet. Qt's 'void "
        "QItemModelSurfaceDataProxyPrivate::connectItemModelHandler()': "
        "leans on "
        "'AbstractItemModelHandler::itemModelChanged(QAbstractItemModel "
        "const*)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")
