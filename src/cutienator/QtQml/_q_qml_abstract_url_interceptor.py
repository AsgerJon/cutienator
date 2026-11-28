"""
QQmlAbstractUrlInterceptor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/qqmlabstracturlinterceptor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']


class QQmlAbstractUrlInterceptor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlAbstractUrlInterceptor: a plain Python object
  standing in front of one C++ QQmlAbstractUrlInterceptor.

  What exists
  -----------

  Every function of Qt's QQmlAbstractUrlInterceptor that has a ritual and
  that Python can call so far, 1 name in all: 'intercept'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlAbstractUrlInterceptor::~QQmlAbstractUrlInterceptor()': the
    destructor: Python never removes a C++ QQmlAbstractUrlInterceptor.

  What to expect
  --------------

  - The C++ QQmlAbstractUrlInterceptor is created at the first use, not by
    'QQmlAbstractUrlInterceptor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlAbstractUrlInterceptor.
  """

  #  The enums Qt writes inside QQmlAbstractUrlInterceptor, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class DataType(CuteNum):
    """
    The enum 'QQmlAbstractUrlInterceptor::DataType' of Qt, with the 4 names
    Qt gives in it.
    """

    QmlFile = Kee[int](0)
    JavaScriptFile = Kee[int](1)
    QmldirFile = Kee[int](2)
    UrlString = Kee[int](4096)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlAbstractUrlInterceptor'

  #  A C++ QQmlAbstractUrlInterceptor Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlAbstractUrlInterceptor'

  #  The functions Qt calls itself that QQmlAbstractUrlInterceptor is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'intercept': (
          ('_ZN26QQmlAbstractUrlInterceptor9interceptERK4QUrlNS_8DataTypeE',
           ('address', 'value', 'QtCore:QUrl'),
           (
               ('address', 'value', 'QtCore:QUrl'),
               ('int', 'enum', 'QtQml:QQmlAbstractUrlInterceptor.DataType'),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQmlAbstractUrlInterceptor::QQmlAbstractUrlInterceptor()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstracturlinterceptor.html
    """
    #  QQmlAbstractUrlInterceptor::QQmlAbstractUrlInterceptor()
    self._noteCreation(QQmlAbstractUrlInterceptor, lambda: Rituals.call(
        'ritual_ZN26QQmlAbstractUrlInterceptorC1Ev',
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

  @overload(QUrl, DataType)
  def intercept(self, path: QUrl, type: DataType) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlAbstractUrlInterceptor::intercept(const QUrl &path,
    DataType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstracturlinterceptor.html#intercept

    Parameters
    ----------

    path : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    type : DataType
      Passed on as its number.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlAbstractUrlInterceptor::intercept(const QUrl &path, DataType
    #      type)
    address = self.uglySide.call(
        'ritual_ZN26QQmlAbstractUrlInterceptor9interceptERK4QUrlNS_8DataTyp'
        'eE',
        self._valueOf(path), type.value,
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)


#  Qt's 'QList<QQmlAbstractUrlInterceptor *>': the list of
#  QQmlAbstractUrlInterceptor, which 'QList[QQmlAbstractUrlInterceptor]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QQmlAbstractUrlInterceptor.
QList.createKind(
    QQmlAbstractUrlInterceptor, 'address',
    make='ritual_list_make_QQmlAbstractUrlInterceptor_ptr',
    add='ritual_list_add_QQmlAbstractUrlInterceptor_ptr',
    size='ritual_list_size_QQmlAbstractUrlInterceptor_ptr',
    at='ritual_list_at_QQmlAbstractUrlInterceptor_ptr',
    drop='ritual_list_drop_QQmlAbstractUrlInterceptor_ptr',
)
