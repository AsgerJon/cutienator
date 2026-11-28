"""
QBar3DSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qbar3dseries_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QBar3DSeriesPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import QAbstract3DSeriesPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QColor, QQuaternion
  from . import Abstract3DController, QAbstractDataProxy, QBar3DSeries
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Abstract3DController = WAIT['Abstract3DController']
  QAbstractDataProxy = WAIT['QtDataVisualization:QAbstractDataProxy']
  QColor = WAIT['QColor']
  QPoint = WAIT['QPoint']
  QQuaternion = WAIT['QQuaternion']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBar3DSeriesPrivate(QAbstract3DSeriesPrivate):
  """
  The cute side of Qt's QBar3DSeriesPrivate: a plain Python object standing
  in front of one C++ QBar3DSeriesPrivate.

  It is built on the cute 'QAbstract3DSeriesPrivate', as Qt's
  QBar3DSeriesPrivate is built on Qt's QAbstract3DSeriesPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QBar3DSeriesPrivate that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'setDataProxy',
  'connectControllerAndProxy', 'createItemLabel',
  'handleMeshRotationChanged', 'setSelectedBar', 'setRowColors', 'qptr'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QBar3DSeriesPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QBar3DSeriesPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QBar3DSeriesPrivate::~QBar3DSeriesPrivate()': the destructor:
    Python never removes a C++ QBar3DSeriesPrivate.

  What has no ritual
  ------------------

  5 of the 16 functions Qt declares: 3 leans on 'QBar3DSeriesPrivate; 2 not a
  gap.

  What to expect
  --------------

  - The C++ QBar3DSeriesPrivate is created at the first use, not by
    'QBar3DSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBar3DSeriesPrivate.
  - Qt tells when it has removed the C++ QBar3DSeriesPrivate. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QBar3DSeriesPrivate that has no cute function yet,
    '__init__', 'connectSignals', holds a function that raises
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
  __qt_class__ = 'QBar3DSeriesPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QBar3DSeriesPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBar3DSeriesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QBar3DSeriesPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QBar3DSeriesPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QBar3DSeriesPrivate10metaObjectEv',
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
    Calls Qt's 'void QBar3DSeriesPrivate::setDataProxy(QAbstractDataProxy
    *proxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setDataProxy

    Parameters
    ----------

    proxy : Optional[QAbstractDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
    ritual = (
        'ritual_ZN19QBar3DSeriesPrivate12setDataProxyEP18QAbstractDataProxy')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBar3DSeriesPrivate12setDataProxyEP18QAbstractDat'
          'aProxy')
    self.uglySide.call(ritual, self._addressOf(proxy))

  @overload(QPoint)
  def setSelectedBar(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setSelectedBar(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setSelectedBar

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QBar3DSeriesPrivate::setSelectedBar(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate14setSelectedBarERK6QPoint',
        self._valueOf(position),
    )

  @overload(QList[QColor])
  def setRowColors(self, colors: QList[QColor]) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::setRowColors(const QList<QColor>
    &colors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#setRowColors

    Parameters
    ----------

    colors : QList[QColor]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QBar3DSeriesPrivate::setRowColors(const QList<QColor> &colors)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate12setRowColorsERK5QListI6QColorE',
        self._valueOf(colors),
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
    Qt's 'QBar3DSeriesPrivate::QBar3DSeriesPrivate(QBar3DSeries *q)': leans
    on 'QBar3DSeriesPrivate::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QBar3DSeriesPrivate.__init__' has no cute function yet. Qt's "
        "'QBar3DSeriesPrivate::QBar3DSeriesPrivate(QBar3DSeries *q)': leans "
        "on 'QBar3DSeriesPrivate::qt_metacall(QMetaObject::Call, int, "
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
    QBar3DSeriesPrivate::connectControllerAndProxy(Abstract3DController
    *newController)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#connectControllerAndProxy

    Parameters
    ----------

    newController : Optional[Abstract3DController]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBar3DSeriesPrivate::connectControllerAndProxy(
    #      Abstract3DController *newController)
    ritual = (
        'ritual_ZN19QBar3DSeriesPrivate25connectControllerAndProxyEP20Abstr'
        'act3DController')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QBar3DSeriesPrivate25connectControllerAndProxyEP2'
          '0Abstract3DController')
    self.uglySide.call(ritual, self._addressOf(newController))

  def createItemLabel(self) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::createItemLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#createItemLabel
    """
    #  void QBar3DSeriesPrivate::createItemLabel()
    ritual = 'ritual_ZN19QBar3DSeriesPrivate15createItemLabelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QBar3DSeriesPrivate15createItemLabelEv'
    self.uglySide.call(ritual)

  @overload(QQuaternion)
  def handleMeshRotationChanged(self, rotation: QQuaternion) -> None:
    """
    Calls Qt's 'void QBar3DSeriesPrivate::handleMeshRotationChanged(const
    QQuaternion &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbar3dseriesprivate.html#handleMeshRotationChanged

    Parameters
    ----------

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QBar3DSeriesPrivate::handleMeshRotationChanged(const QQuaternion
    #      &rotation)
    self.uglySide.call(
        'ritual_ZN19QBar3DSeriesPrivate25handleMeshRotationChangedERK11QQua'
        'ternion',
        self._valueOf(rotation),
    )

  def qptr(self) -> Optional[QBar3DSeries]:
    """
    Calls Qt's 'QBar3DSeries *QBar3DSeriesPrivate::qptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qbar3dseriesprivate.html#qptr

    Returns
    -------

    Optional[QBar3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBar3DSeries *QBar3DSeriesPrivate::qptr()
    address = self.uglySide.call('ritual_ZN19QBar3DSeriesPrivate4qptrEv')
    from . import QBar3DSeries
    return QBar3DSeries._cuteAt(address)

  @staticmethod
  def connectSignals(*__, **_) -> Never:
    """
    Qt's 'void QBar3DSeriesPrivate::connectSignals()': leans on
    'QBar3DSeriesPrivate::staticMetaObject', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QBar3DSeriesPrivate.connectSignals' has no cute function yet. "
        "Qt's 'void QBar3DSeriesPrivate::connectSignals()': leans on "
        "'QBar3DSeriesPrivate::staticMetaObject', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
