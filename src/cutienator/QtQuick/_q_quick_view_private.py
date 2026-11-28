"""
QQuickViewPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickview_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickViewPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuickWindowPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QRectF, QSize
  from ..QtQml import QQmlEngine
  from . import QQuickGeometryChange, QQuickItem, QQuickView
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlEngine = WAIT['QQmlEngine']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickView = WAIT['QQuickView']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickViewPrivate(QQuickWindowPrivate):
  """
  The cute side of Qt's QQuickViewPrivate: a plain Python object standing in
  front of one C++ QQuickViewPrivate.

  It is built on the cute 'QQuickWindowPrivate', as Qt's QQuickViewPrivate is
  built on Qt's QQuickWindowPrivate, and has everything that class has. Qt's
  QQuickViewPrivate is built on Qt's
  QSafeQuickItemChangeListener<QQuickViewPrivate> as well, which is not
  reflected.

  What exists
  -----------

  Every function of Qt's QQuickViewPrivate that has a ritual and that Python
  can call so far, 10 names in all: 'q_func', 'get', 'executeHelper',
  'execute', 'itemGeometryChanged', 'initResize', 'updateSize',
  'setRootObject', 'init', 'rootObjectSize'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickView *QQuickViewPrivate::q_func() const': takes in
    Python what 'QQuickView *QQuickViewPrivate::q_func()' takes.
  - Qt's 'const QQuickViewPrivate *QQuickViewPrivate::get(const QQuickView
    *view)': takes in Python what 'QQuickViewPrivate
    *QQuickViewPrivate::get(QQuickView *view)' takes.
  - Qt's 'QQuickViewPrivate::~QQuickViewPrivate()': the destructor: Python
    never removes a C++ QQuickViewPrivate.

  What to expect
  --------------

  - The C++ QQuickViewPrivate is created at the first use, not by
    'QQuickViewPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickViewPrivate.
  """

  #  The enums Qt writes inside QQuickViewPrivate, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ExecuteState(CuteNum):
    """
    The enum 'QQuickViewPrivate::ExecuteState' of Qt, with the 2 names Qt
    gives in it.
    """

    Continue = Kee[int](0)
    Stop = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickView)
  @overload(NoneType)
  def get(view: Optional[QQuickView]) -> Optional[QQuickViewPrivate]:
    """
    Calls Qt's 'QQuickViewPrivate *QQuickViewPrivate::get(QQuickView *view)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewprivate.html#get

    Parameters
    ----------

    view : Optional[QQuickView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickViewPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickViewPrivate *QQuickViewPrivate::get(QQuickView *view)
    address = Rituals.call(
        'ritual_ZN17QQuickViewPrivate3getEP10QQuickView',
        CuteMixin._addressOf(view),
    )
    return QQuickViewPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickViewPrivate'

  #  A C++ QQuickViewPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickViewPrivate'

  #  The functions Qt calls itself that QQuickViewPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN17QQuickViewPrivate19itemGeometryChangedEP10QQuickItem20QQui'
           'ckGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
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

  def rootObjectSize(self) -> QSize:
    """
    Calls Qt's 'QSize QQuickViewPrivate::rootObjectSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewprivate.html#rootObjectSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QQuickViewPrivate::rootObjectSize() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickViewPrivate14rootObjectSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setRootObject(self, a0: Optional[QObject]) -> bool:
    """
    Calls Qt's 'bool QQuickViewPrivate::setRootObject(QObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewprivate.html#setRootObject

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickViewPrivate::setRootObject(QObject *a0)
    return self.uglySide.call(
        'ritual_ZN17QQuickViewPrivate13setRootObjectEP7QObject',
        self._addressOf(a0, 'QObject'),
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
    Notes what was given, for Qt's 'QQuickViewPrivate::QQuickViewPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewprivate.html#QQuickViewPrivate
    """
    #  QQuickViewPrivate::QQuickViewPrivate()
    self._noteCreation(QQuickViewPrivate, lambda: Rituals.call(
        'ritual_ZN17QQuickViewPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickView]:
    """
    Calls Qt's 'QQuickView *QQuickViewPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewprivate.html#q_func

    Returns
    -------

    Optional[QQuickView]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickView *QQuickViewPrivate::q_func()
    address = self.uglySide.call('ritual_ZN17QQuickViewPrivate6q_funcEv')
    from . import QQuickView
    return QQuickView._cuteAt(address)

  def executeHelper(self) -> ExecuteState:
    """
    Calls Qt's 'ExecuteState QQuickViewPrivate::executeHelper()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewprivate.html#executeHelper

    Returns
    -------

    ExecuteState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ExecuteState(number)'
      gives.
    """
    #  ExecuteState QQuickViewPrivate::executeHelper()
    return QQuickViewPrivate.ExecuteState(self.uglySide.call(
        'ritual_ZN17QQuickViewPrivate13executeHelperEv',
    ))

  @overload()
  def execute(self) -> None:
    """
    Calls Qt's 'void QQuickViewPrivate::execute()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewprivate.html#execute
    """
    #  void QQuickViewPrivate::execute()
    self.uglySide.call('ritual_ZN17QQuickViewPrivate7executeEv')

  @overload(str, str)
  def execute(self, uri: str, typeName: str) -> None:
    """
    Calls Qt's 'void QQuickViewPrivate::execute(QAnyStringView uri,
    QAnyStringView typeName)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewprivate.html#execute

    Parameters
    ----------

    uri : str
      Passed on as it is: a QString is made of it for the call.

    typeName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickViewPrivate::execute(QAnyStringView uri, QAnyStringView
    #      typeName)
    self.uglySide.call(
        'ritual_ZN17QQuickViewPrivate7executeE14QAnyStringViewS0_',
        uri, typeName,
    )

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickViewPrivate::itemGeometryChanged(QQuickItem *item,
    QQuickGeometryChange change, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickviewprivate.html#itemGeometryChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickViewPrivate::itemGeometryChanged(QQuickItem *item,
    #      QQuickGeometryChange change, const QRectF &a2)
    ritual = (
        'ritual_ZN17QQuickViewPrivate19itemGeometryChangedEP10QQuickItem20Q'
        'QuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickViewPrivate19itemGeometryChangedEP10QQuickI'
          'tem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(a2),
    )

  def initResize(self) -> None:
    """
    Calls Qt's 'void QQuickViewPrivate::initResize()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewprivate.html#initResize
    """
    #  void QQuickViewPrivate::initResize()
    self.uglySide.call('ritual_ZN17QQuickViewPrivate10initResizeEv')

  def updateSize(self) -> None:
    """
    Calls Qt's 'void QQuickViewPrivate::updateSize()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewprivate.html#updateSize
    """
    #  void QQuickViewPrivate::updateSize()
    self.uglySide.call('ritual_ZN17QQuickViewPrivate10updateSizeEv')

  @overload()
  @overload(QQmlEngine)
  @overload(NoneType)
  def init(self, e: Optional[QQmlEngine] = None) -> None:
    """
    Calls Qt's 'void QQuickViewPrivate::init(QQmlEngine *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickviewprivate.html#init

    Parameters
    ----------

    e : Optional[QQmlEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickViewPrivate::init(QQmlEngine *e)
    self.uglySide.call(
        'ritual_ZN17QQuickViewPrivate4initEP10QQmlEngine',
        self._addressOf(e),
    )
