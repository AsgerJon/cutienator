"""
QScatter3DSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qscatter3dseries_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QScatter3DSeriesPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstract3DSeriesPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import Abstract3DController, QAbstractDataProxy, QScatter3DSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Abstract3DController = WAIT['Abstract3DController']
  QAbstractDataProxy = WAIT['QtDataVisualization:QAbstractDataProxy']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScatter3DSeriesPrivate(QAbstract3DSeriesPrivate):
  """
  The cute side of Qt's QScatter3DSeriesPrivate: a plain Python object
  standing in front of one C++ QScatter3DSeriesPrivate.

  It is built on the cute 'QAbstract3DSeriesPrivate', as Qt's
  QScatter3DSeriesPrivate is built on Qt's QAbstract3DSeriesPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QScatter3DSeriesPrivate that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'setDataProxy',
  'connectControllerAndProxy', 'createItemLabel', 'setSelectedItem',
  'setItemSize', 'qptr'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QScatter3DSeriesPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QScatter3DSeriesPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QScatter3DSeriesPrivate::~QScatter3DSeriesPrivate()': the
    destructor: Python never removes a C++ QScatter3DSeriesPrivate.

  What has no ritual
  ------------------

  4 of the 14 functions Qt declares: 2 not a gap; 2 leans on
  'QScatter3DSeriesPrivate.

  What to expect
  --------------

  - The C++ QScatter3DSeriesPrivate is created at the first use, not by
    'QScatter3DSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScatter3DSeriesPrivate.
  - Qt tells when it has removed the C++ QScatter3DSeriesPrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QScatter3DSeriesPrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScatter3DSeriesPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QScatter3DSeriesPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QScatter3DSeriesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QScatter3DSeriesPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QScatter3DSeriesPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QScatter3DSeriesPrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractDataProxy)
  @overload(NoneType)
  def setDataProxy(self, proxy: Optional[QAbstractDataProxy]) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy
    *proxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#setDataProxy

    Parameters
    ----------

    proxy : Optional[QAbstractDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
    ritual = (
        'ritual_ZN23QScatter3DSeriesPrivate12setDataProxyEP18QAbstractDataP'
        'roxy')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QScatter3DSeriesPrivate12setDataProxyEP18QAbstrac'
          'tDataProxy')
    self.uglySide.call(ritual, self._addressOf(proxy))

  @overload(int)
  def setSelectedItem(self, index: int) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::setSelectedItem(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#setSelectedItem

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QScatter3DSeriesPrivate::setSelectedItem(int index)
    self.uglySide.call(
        'ritual_ZN23QScatter3DSeriesPrivate15setSelectedItemEi', index,
    )

  @overload(float)
  def setItemSize(self, size: float) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::setItemSize(float size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#setItemSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QScatter3DSeriesPrivate::setItemSize(float size)
    self.uglySide.call(
        'ritual_ZN23QScatter3DSeriesPrivate11setItemSizeEf', size,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QScatter3DSeriesPrivate::QScatter3DSeriesPrivate(QScatter3DSeries
    *q)': leans on 'QScatter3DSeriesPrivate::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QScatter3DSeriesPrivate.__init__' has no cute function yet. Qt's "
        "'QScatter3DSeriesPrivate::QScatter3DSeriesPrivate(QScatter3DSeries "
        "*q)': leans on "
        "'QScatter3DSeriesPrivate::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  @overload(Abstract3DController)
  @overload(NoneType)
  def connectControllerAndProxy(
      self,
      newController: Optional[Abstract3DController],
  ) -> None:
    """
    Calls Qt's 'void
    QScatter3DSeriesPrivate::connectControllerAndProxy(Abstract3DController
    *newController)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html

    Parameters
    ----------

    newController : Optional[Abstract3DController]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScatter3DSeriesPrivate::connectControllerAndProxy(
    #      Abstract3DController *newController)
    ritual = (
        'ritual_ZN23QScatter3DSeriesPrivate25connectControllerAndProxyEP20A'
        'bstract3DController')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QScatter3DSeriesPrivate25connectControllerAndProx'
          'yEP20Abstract3DController')
    self.uglySide.call(ritual, self._addressOf(newController))

  def createItemLabel(self) -> None:
    """
    Calls Qt's 'void QScatter3DSeriesPrivate::createItemLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#createItemLabel
    """
    #  void QScatter3DSeriesPrivate::createItemLabel()
    ritual = 'ritual_ZN23QScatter3DSeriesPrivate15createItemLabelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QScatter3DSeriesPrivate15createItemLabelEv'
    self.uglySide.call(ritual)

  def qptr(self) -> Optional[QScatter3DSeries]:
    """
    Calls Qt's 'QScatter3DSeries *QScatter3DSeriesPrivate::qptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qscatter3dseriesprivate.html#qptr

    Returns
    -------

    Optional[QScatter3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScatter3DSeries *QScatter3DSeriesPrivate::qptr()
    address = self.uglySide.call('ritual_ZN23QScatter3DSeriesPrivate4qptrEv')
    from . import QScatter3DSeries
    return QScatter3DSeries._cuteAt(address)
