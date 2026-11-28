"""
QAbstractDataProxy binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qabstractdataproxy.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QAbstractDataProxyPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractDataProxyPrivate = WAIT['QtDataVisualization:QAbstractDataProxyPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractDataProxy(QObject):
  """
  The cute side of Qt's QAbstractDataProxy: a plain Python object standing in
  front of one C++ QAbstractDataProxy.

  It is built on the cute 'QObject', as Qt's QAbstractDataProxy is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractDataProxy that has a ritual and that Python
  can call so far, 3 names in all: 'metaObject', 'tr', 'type'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QAbstractDataProxy::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QAbstractDataProxy::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QAbstractDataProxy::~QAbstractDataProxy()': the destructor: Python
    never removes a C++ QAbstractDataProxy.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QAbstractDataProxy is created at the first use, not by
    'QAbstractDataProxy(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractDataProxy.
  - Qt tells when it has removed the C++ QAbstractDataProxy. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QAbstractDataProxy, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DataType(CuteNum):
    """
    The enum 'QAbstractDataProxy::DataType' of Qt, with the 4 names Qt gives
    in it.
    """

    DataTypeNone = Kee[int](0)
    DataTypeBar = Kee[int](1)
    DataTypeScatter = Kee[int](2)
    DataTypeSurface = Kee[int](4)

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
    Calls Qt's 'QString QAbstractDataProxy::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractdataproxy.html#tr

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
    #  QString QAbstractDataProxy::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QAbstractDataProxy2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractDataProxy'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QAbstractDataProxy Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractDataProxy'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAbstractDataProxy::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractdataproxy.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAbstractDataProxy::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QAbstractDataProxy10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def type(self) -> DataType:
    """
    Calls Qt's 'DataType QAbstractDataProxy::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qabstractdataproxy.html#type

    Returns
    -------

    DataType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DataType(number)' gives.
    """
    #  DataType QAbstractDataProxy::type() const
    return QAbstractDataProxy.DataType(self.uglySide.call(
        'ritual_ZNK18QAbstractDataProxy4typeEv',
    ))

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

  @overload(QAbstractDataProxyPrivate)
  @overload(NoneType)
  @overload(QAbstractDataProxyPrivate, QObject)
  @overload(QAbstractDataProxyPrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      d: Optional[QAbstractDataProxyPrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractDataProxy::QAbstractDataProxy(QAbstractDataProxyPrivate *d,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractdataproxy.html#QAbstractDataProxy

    Parameters
    ----------

    d : Optional[QAbstractDataProxyPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QAbstractDataProxy::QAbstractDataProxy(QAbstractDataProxyPrivate *d,
    #      QObject *parent)
    self._noteCreation(QAbstractDataProxy, lambda: Rituals.call(
        'ritual_ZN18QAbstractDataProxyC1EP25QAbstractDataProxyPrivateP7QObj'
        'ect',
        self._addressOf(d), self._addressOf(parent, 'QObject'),
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
