"""
QSurface3DSeriesPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qsurface3dseries_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSurface3DSeriesPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstract3DSeriesPrivate, QSurface3DSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QColor, QImage
  from . import Abstract3DController, QAbstractDataProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Abstract3DController = WAIT['Abstract3DController']
  QAbstractDataProxy = WAIT['QtDataVisualization:QAbstractDataProxy']
  QColor = WAIT['QColor']
  QImage = WAIT['QImage']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSurface3DSeriesPrivate(QAbstract3DSeriesPrivate):
  """
  The cute side of Qt's QSurface3DSeriesPrivate: a plain Python object
  standing in front of one C++ QSurface3DSeriesPrivate.

  It is built on the cute 'QAbstract3DSeriesPrivate', as Qt's
  QSurface3DSeriesPrivate is built on Qt's QAbstract3DSeriesPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSurface3DSeriesPrivate that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'setDataProxy',
  'connectControllerAndProxy', 'createItemLabel', 'setSelectedPoint',
  'setFlatShadingEnabled', 'setDrawMode', 'setTexture', 'setWireframeColor',
  'qptr'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSurface3DSeriesPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QSurface3DSeriesPrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QSurface3DSeriesPrivate::~QSurface3DSeriesPrivate()': the
    destructor: Python never removes a C++ QSurface3DSeriesPrivate.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 2 not a gap; 2 leans on
  'QSurface3DSeriesPrivate.

  What to expect
  --------------

  - The C++ QSurface3DSeriesPrivate is created at the first use, not by
    'QSurface3DSeriesPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSurface3DSeriesPrivate.
  - Qt tells when it has removed the C++ QSurface3DSeriesPrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSurface3DSeriesPrivate that has no cute function yet,
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
  __qt_class__ = 'QSurface3DSeriesPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QSurface3DSeriesPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSurface3DSeriesPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSurface3DSeriesPrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSurface3DSeriesPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QSurface3DSeriesPrivate10metaObjectEv',
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
    Calls Qt's 'void QSurface3DSeriesPrivate::setDataProxy(QAbstractDataProxy
    *proxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setDataProxy

    Parameters
    ----------

    proxy : Optional[QAbstractDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeriesPrivate::setDataProxy(QAbstractDataProxy *proxy)
    ritual = (
        'ritual_ZN23QSurface3DSeriesPrivate12setDataProxyEP18QAbstractDataP'
        'roxy')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSurface3DSeriesPrivate12setDataProxyEP18QAbstrac'
          'tDataProxy')
    self.uglySide.call(ritual, self._addressOf(proxy))

  @overload(QPoint)
  def setSelectedPoint(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::setSelectedPoint(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setSelectedPoint

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSurface3DSeriesPrivate::setSelectedPoint(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate16setSelectedPointERK6QPoint',
        self._valueOf(position),
    )

  @overload(bool)
  def setFlatShadingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::setFlatShadingEnabled(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setFlatShadingEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QSurface3DSeriesPrivate::setFlatShadingEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate21setFlatShadingEnabledEb',
        enabled,
    )

  @overload(QSurface3DSeries.DrawFlags)
  def setDrawMode(self, mode: QSurface3DSeries.DrawFlags) -> None:
    """
    Calls Qt's 'void
    QSurface3DSeriesPrivate::setDrawMode(QSurface3DSeries::DrawFlags mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setDrawMode

    Parameters
    ----------

    mode : QSurface3DSeries.DrawFlags
      Passed on as its number.
    """
    #  void QSurface3DSeriesPrivate::setDrawMode(QSurface3DSeries::DrawFlags
    #      mode)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate11setDrawModeE6QFlagsIN16QSurfac'
        'e3DSeries8DrawFlagEE',
        mode.value,
    )

  @overload(QImage)
  def setTexture(self, texture: QImage) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::setTexture(const QImage
    &texture)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setTexture

    Parameters
    ----------

    texture : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QSurface3DSeriesPrivate::setTexture(const QImage &texture)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate10setTextureERK6QImage',
        self._valueOf(texture),
    )

  @overload(QColor)
  def setWireframeColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::setWireframeColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#setWireframeColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSurface3DSeriesPrivate::setWireframeColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN23QSurface3DSeriesPrivate17setWireframeColorERK6QColor',
        self._valueOf(color),
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
    Qt's 'QSurface3DSeriesPrivate::QSurface3DSeriesPrivate(QSurface3DSeries
    *q)': leans on 'QSurface3DSeriesPrivate::qt_metacall(QMetaObject::Call,
    int, void**)', which Qt's source does not mark for use from outside Qt
    and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QSurface3DSeriesPrivate.__init__' has no cute function yet. Qt's "
        "'QSurface3DSeriesPrivate::QSurface3DSeriesPrivate(QSurface3DSeries "
        "*q)': leans on "
        "'QSurface3DSeriesPrivate::qt_metacall(QMetaObject::Call, int, "
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
    QSurface3DSeriesPrivate::connectControllerAndProxy(Abstract3DController
    *newController)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html

    Parameters
    ----------

    newController : Optional[Abstract3DController]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeriesPrivate::connectControllerAndProxy(
    #      Abstract3DController *newController)
    ritual = (
        'ritual_ZN23QSurface3DSeriesPrivate25connectControllerAndProxyEP20A'
        'bstract3DController')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QSurface3DSeriesPrivate25connectControllerAndProx'
          'yEP20Abstract3DController')
    self.uglySide.call(ritual, self._addressOf(newController))

  def createItemLabel(self) -> None:
    """
    Calls Qt's 'void QSurface3DSeriesPrivate::createItemLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#createItemLabel
    """
    #  void QSurface3DSeriesPrivate::createItemLabel()
    ritual = 'ritual_ZN23QSurface3DSeriesPrivate15createItemLabelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSurface3DSeriesPrivate15createItemLabelEv'
    self.uglySide.call(ritual)

  def qptr(self) -> Optional[QSurface3DSeries]:
    """
    Calls Qt's 'QSurface3DSeries *QSurface3DSeriesPrivate::qptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseriesprivate.html#qptr

    Returns
    -------

    Optional[QSurface3DSeries]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface3DSeries *QSurface3DSeriesPrivate::qptr()
    address = self.uglySide.call('ritual_ZN23QSurface3DSeriesPrivate4qptrEv')
    return QSurface3DSeries._cuteAt(address)
