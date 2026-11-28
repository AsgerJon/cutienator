"""
QAbstractDataProxyPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qabstractdataproxy_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QAbstractDataProxyPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from . import QAbstractDataProxy

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstract3DSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstract3DSeries = WAIT['QtGraphs:QAbstract3DSeries']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractDataProxyPrivate(QObjectPrivate):
  """
  The cute side of Qt's QAbstractDataProxyPrivate: a plain Python object
  standing in front of one C++ QAbstractDataProxyPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QAbstractDataProxyPrivate
  is built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractDataProxyPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'q_func', 'series', 'setSeries'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractDataProxy *QAbstractDataProxyPrivate::q_func()
    const': takes in Python what 'QAbstractDataProxy
    *QAbstractDataProxyPrivate::q_func()' takes.
  - Qt's 'QAbstractDataProxyPrivate::~QAbstractDataProxyPrivate()': the
    destructor: Python never removes a C++ QAbstractDataProxyPrivate.

  What to expect
  --------------

  - The C++ QAbstractDataProxyPrivate is created at the first use, not by
    'QAbstractDataProxyPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractDataProxyPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractDataProxyPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QAbstractDataProxyPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractDataProxyPrivate'

  #  The functions Qt calls itself that QAbstractDataProxyPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setSeries': (
          ('_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSeries',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGraphs:QAbstract3DSeries'),
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

  def series(self) -> Optional[QAbstract3DSeries]:
    """
    Calls Qt's 'QAbstract3DSeries *QAbstractDataProxyPrivate::series()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractdataproxyprivate.html#series

    Returns
    -------

    Optional[QAbstract3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstract3DSeries *QAbstractDataProxyPrivate::series() const
    address = self.uglySide.call(
        'ritual_ZNK25QAbstractDataProxyPrivate6seriesEv',
    )
    from . import QAbstract3DSeries
    return QAbstract3DSeries._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstract3DSeries)
  @overload(NoneType)
  def setSeries(self, series: Optional[QAbstract3DSeries]) -> None:
    """
    Calls Qt's 'void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries
    *series)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractdataproxyprivate.html#setSeries

    Parameters
    ----------

    series : Optional[QAbstract3DSeries]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractDataProxyPrivate::setSeries(QAbstract3DSeries *series)
    ritual = (
        'ritual_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3DSerie'
        's')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QAbstractDataProxyPrivate9setSeriesEP17QAbstract3'
          'DSeries')
    self.uglySide.call(ritual, self._addressOf(series))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractDataProxy.DataType)
  def __init__(self, type: QAbstractDataProxy.DataType) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractDataProxyPrivate::QAbstractDataProxyPrivate(
    QAbstractDataProxy::DataType type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractdataproxyprivate.html

    Parameters
    ----------

    type : QAbstractDataProxy.DataType
      Passed on as its number.
    """
    #  QAbstractDataProxyPrivate::QAbstractDataProxyPrivate(
    #      QAbstractDataProxy::DataType type)
    self._noteCreation(QAbstractDataProxyPrivate, lambda: Rituals.call(
        'ritual_ZN25QAbstractDataProxyPrivateC1EN18QAbstractDataProxy8DataT'
        'ypeE',
        type.value,
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

  def q_func(self) -> Optional[QAbstractDataProxy]:
    """
    Calls Qt's 'QAbstractDataProxy *QAbstractDataProxyPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractdataproxyprivate.html#q_func

    Returns
    -------

    Optional[QAbstractDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractDataProxy *QAbstractDataProxyPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN25QAbstractDataProxyPrivate6q_funcEv',
    )
    return QAbstractDataProxy._cuteAt(address)
