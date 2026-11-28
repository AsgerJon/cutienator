"""
Q3DScene binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/q3dscene.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect
  from . import Q3DScenePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DScene(QObject):
  """
  The cute side of Qt's Q3DScene: a plain Python object standing in front of
  one C++ Q3DScene.

  It is built on the cute 'QObject', as Qt's Q3DScene is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DScene that has a ritual and that Python can call
  so far, 30 names in all: 'metaObject', 'tr', 'd_func', 'viewport',
  'primarySubViewport', 'setPrimarySubViewport', 'isPointInPrimarySubView',
  'secondarySubViewport', 'setSecondarySubViewport',
  'isPointInSecondarySubView', 'setSelectionQueryPosition',
  'selectionQueryPosition', 'setGraphPositionQuery', 'graphPositionQuery',
  'setSlicingActive', 'isSlicingActive', 'setSecondarySubviewOnTop',
  'isSecondarySubviewOnTop', 'devicePixelRatio', 'setDevicePixelRatio',
  'invalidSelectionPoint', 'viewportChanged', 'primarySubViewportChanged',
  'secondarySubViewportChanged', 'secondarySubviewOnTopChanged',
  'slicingActiveChanged', 'devicePixelRatioChanged',
  'selectionQueryPositionChanged', 'graphPositionQueryChanged', 'needRender'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DScene::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int Q3DScene::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const Q3DScenePrivate *Q3DScene::d_func() const': takes in Python
    what 'Q3DScenePrivate *Q3DScene::d_func()' takes.
  - Qt's 'void Q3DScene::qt_qmlMarker_uncreatable()': one of Qt's own inner
    workings.
  - Qt's 'Q3DScene::~Q3DScene()': the destructor: Python never removes a C++
    Q3DScene.

  What has no ritual
  ------------------

  4 of the 40 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ Q3DScene is created at the first use, not by 'Q3DScene(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DScene.
  - Qt tells when it has removed the C++ Q3DScene. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

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
    Calls Qt's 'QString Q3DScene::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#tr

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
    #  QString Q3DScene::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8Q3DScene2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DScene'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ Q3DScene Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DScene'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DScene::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DScene::metaObject() const
    address = self.uglySide.call('ritual_ZNK8Q3DScene10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def viewport(self) -> QRect:
    """
    Calls Qt's 'QRect Q3DScene::viewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#viewport

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect Q3DScene::viewport() const
    address = self.uglySide.call('ritual_ZNK8Q3DScene8viewportEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def primarySubViewport(self) -> QRect:
    """
    Calls Qt's 'QRect Q3DScene::primarySubViewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#primarySubViewport

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect Q3DScene::primarySubViewport() const
    address = self.uglySide.call('ritual_ZNK8Q3DScene18primarySubViewportEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def secondarySubViewport(self) -> QRect:
    """
    Calls Qt's 'QRect Q3DScene::secondarySubViewport() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#secondarySubViewport

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect Q3DScene::secondarySubViewport() const
    address = self.uglySide.call(
        'ritual_ZNK8Q3DScene20secondarySubViewportEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def selectionQueryPosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint Q3DScene::selectionQueryPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#selectionQueryPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Q3DScene::selectionQueryPosition() const
    address = self.uglySide.call(
        'ritual_ZNK8Q3DScene22selectionQueryPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def graphPositionQuery(self) -> QPoint:
    """
    Calls Qt's 'QPoint Q3DScene::graphPositionQuery() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#graphPositionQuery

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Q3DScene::graphPositionQuery() const
    address = self.uglySide.call('ritual_ZNK8Q3DScene18graphPositionQueryEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def isSlicingActive(self) -> bool:
    """
    Calls Qt's 'bool Q3DScene::isSlicingActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#isSlicingActive
    """
    #  bool Q3DScene::isSlicingActive() const
    return self.uglySide.call('ritual_ZNK8Q3DScene15isSlicingActiveEv')

  def isSecondarySubviewOnTop(self) -> bool:
    """
    Calls Qt's 'bool Q3DScene::isSecondarySubviewOnTop() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#isSecondarySubviewOnTop
    """
    #  bool Q3DScene::isSecondarySubviewOnTop() const
    return self.uglySide.call(
        'ritual_ZNK8Q3DScene23isSecondarySubviewOnTopEv',
    )

  def devicePixelRatio(self) -> float:
    """
    Calls Qt's 'qreal Q3DScene::devicePixelRatio() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#devicePixelRatio
    """
    #  qreal Q3DScene::devicePixelRatio() const
    return self.uglySide.call('ritual_ZNK8Q3DScene16devicePixelRatioEv')

  def invalidSelectionPoint(self) -> QPoint:
    """
    Calls Qt's 'QPoint Q3DScene::invalidSelectionPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#invalidSelectionPoint

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint Q3DScene::invalidSelectionPoint() const
    address = self.uglySide.call(
        'ritual_ZNK8Q3DScene21invalidSelectionPointEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setPrimarySubViewport(self, primarySubViewport: QRect) -> None:
    """
    Calls Qt's 'void Q3DScene::setPrimarySubViewport(QRect
    primarySubViewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#setPrimarySubViewport

    Parameters
    ----------

    primarySubViewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void Q3DScene::setPrimarySubViewport(QRect primarySubViewport)
    self.uglySide.call(
        'ritual_ZN8Q3DScene21setPrimarySubViewportE5QRect',
        self._valueOf(primarySubViewport),
    )

  @overload(QRect)
  def setSecondarySubViewport(self, secondarySubViewport: QRect) -> None:
    """
    Calls Qt's 'void Q3DScene::setSecondarySubViewport(QRect
    secondarySubViewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#setSecondarySubViewport

    Parameters
    ----------

    secondarySubViewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void Q3DScene::setSecondarySubViewport(QRect secondarySubViewport)
    self.uglySide.call(
        'ritual_ZN8Q3DScene23setSecondarySubViewportE5QRect',
        self._valueOf(secondarySubViewport),
    )

  @overload(QPoint)
  def setSelectionQueryPosition(self, point: QPoint) -> None:
    """
    Calls Qt's 'void Q3DScene::setSelectionQueryPosition(QPoint point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#setSelectionQueryPosition

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Q3DScene::setSelectionQueryPosition(QPoint point)
    self.uglySide.call(
        'ritual_ZN8Q3DScene25setSelectionQueryPositionE6QPoint',
        self._valueOf(point),
    )

  @overload(QPoint)
  def setGraphPositionQuery(self, point: QPoint) -> None:
    """
    Calls Qt's 'void Q3DScene::setGraphPositionQuery(QPoint point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#setGraphPositionQuery

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Q3DScene::setGraphPositionQuery(QPoint point)
    self.uglySide.call(
        'ritual_ZN8Q3DScene21setGraphPositionQueryE6QPoint',
        self._valueOf(point),
    )

  @overload(bool)
  def setSlicingActive(self, isSlicing: bool) -> None:
    """
    Calls Qt's 'void Q3DScene::setSlicingActive(bool isSlicing)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#setSlicingActive

    Parameters
    ----------

    isSlicing : bool
      Passed on as it is.
    """
    #  void Q3DScene::setSlicingActive(bool isSlicing)
    self.uglySide.call('ritual_ZN8Q3DScene16setSlicingActiveEb', isSlicing)

  @overload(bool)
  def setSecondarySubviewOnTop(self, isSecondaryOnTop: bool) -> None:
    """
    Calls Qt's 'void Q3DScene::setSecondarySubviewOnTop(bool
    isSecondaryOnTop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#setSecondarySubviewOnTop

    Parameters
    ----------

    isSecondaryOnTop : bool
      Passed on as it is.
    """
    #  void Q3DScene::setSecondarySubviewOnTop(bool isSecondaryOnTop)
    self.uglySide.call(
        'ritual_ZN8Q3DScene24setSecondarySubviewOnTopEb', isSecondaryOnTop,
    )

  @overload(float)
  def setDevicePixelRatio(self, pixelRatio: float) -> None:
    """
    Calls Qt's 'void Q3DScene::setDevicePixelRatio(qreal pixelRatio)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#setDevicePixelRatio

    Parameters
    ----------

    pixelRatio : float
      Passed on as it is.
    """
    #  void Q3DScene::setDevicePixelRatio(qreal pixelRatio)
    self.uglySide.call(
        'ritual_ZN8Q3DScene19setDevicePixelRatioEd', pixelRatio,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'Q3DScene::Q3DScene(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#Q3DScene

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Q3DScene::Q3DScene(QObject *parent)
    self._noteCreation(Q3DScene, lambda: Rituals.call(
        'ritual_ZN8Q3DSceneC1EP7QObject', self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[Q3DScenePrivate]:
    """
    Calls Qt's 'Q3DScenePrivate *Q3DScene::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#d_func

    Returns
    -------

    Optional[Q3DScenePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Q3DScenePrivate *Q3DScene::d_func()
    address = self.uglySide.call('ritual_ZN8Q3DScene6d_funcEv')
    from . import Q3DScenePrivate
    return Q3DScenePrivate._cuteAt(address)

  @overload(QPoint)
  def isPointInPrimarySubView(self, point: QPoint) -> bool:
    """
    Calls Qt's 'bool Q3DScene::isPointInPrimarySubView(QPoint point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#isPointInPrimarySubView

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool Q3DScene::isPointInPrimarySubView(QPoint point)
    return self.uglySide.call(
        'ritual_ZN8Q3DScene23isPointInPrimarySubViewE6QPoint',
        self._valueOf(point),
    )

  @overload(QPoint)
  def isPointInSecondarySubView(self, point: QPoint) -> bool:
    """
    Calls Qt's 'bool Q3DScene::isPointInSecondarySubView(QPoint point)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#isPointInSecondarySubView

    Parameters
    ----------

    point : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool Q3DScene::isPointInSecondarySubView(QPoint point)
    return self.uglySide.call(
        'ritual_ZN8Q3DScene25isPointInSecondarySubViewE6QPoint',
        self._valueOf(point),
    )

  @overload(QRect)
  def viewportChanged(self, viewport: QRect) -> None:
    """
    Calls Qt's 'void Q3DScene::viewportChanged(QRect viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#viewportChanged

    Parameters
    ----------

    viewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void Q3DScene::viewportChanged(QRect viewport)
    self.uglySide.call(
        'ritual_ZN8Q3DScene15viewportChangedE5QRect',
        self._valueOf(viewport),
    )

  @overload(QRect)
  def primarySubViewportChanged(self, subViewport: QRect) -> None:
    """
    Calls Qt's 'void Q3DScene::primarySubViewportChanged(QRect subViewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#primarySubViewportChanged

    Parameters
    ----------

    subViewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void Q3DScene::primarySubViewportChanged(QRect subViewport)
    self.uglySide.call(
        'ritual_ZN8Q3DScene25primarySubViewportChangedE5QRect',
        self._valueOf(subViewport),
    )

  @overload(QRect)
  def secondarySubViewportChanged(self, subViewport: QRect) -> None:
    """
    Calls Qt's 'void Q3DScene::secondarySubViewportChanged(QRect
    subViewport)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#secondarySubViewportChanged

    Parameters
    ----------

    subViewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void Q3DScene::secondarySubViewportChanged(QRect subViewport)
    self.uglySide.call(
        'ritual_ZN8Q3DScene27secondarySubViewportChangedE5QRect',
        self._valueOf(subViewport),
    )

  @overload(bool)
  def secondarySubviewOnTopChanged(self, isSecondaryOnTop: bool) -> None:
    """
    Calls Qt's 'void Q3DScene::secondarySubviewOnTopChanged(bool
    isSecondaryOnTop)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#secondarySubviewOnTopChanged

    Parameters
    ----------

    isSecondaryOnTop : bool
      Passed on as it is.
    """
    #  void Q3DScene::secondarySubviewOnTopChanged(bool isSecondaryOnTop)
    self.uglySide.call(
        'ritual_ZN8Q3DScene28secondarySubviewOnTopChangedEb',
        isSecondaryOnTop,
    )

  @overload(bool)
  def slicingActiveChanged(self, isSlicingActive: bool) -> None:
    """
    Calls Qt's 'void Q3DScene::slicingActiveChanged(bool isSlicingActive)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#slicingActiveChanged

    Parameters
    ----------

    isSlicingActive : bool
      Passed on as it is.
    """
    #  void Q3DScene::slicingActiveChanged(bool isSlicingActive)
    self.uglySide.call(
        'ritual_ZN8Q3DScene20slicingActiveChangedEb', isSlicingActive,
    )

  @overload(float)
  def devicePixelRatioChanged(self, pixelRatio: float) -> None:
    """
    Calls Qt's 'void Q3DScene::devicePixelRatioChanged(qreal pixelRatio)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#devicePixelRatioChanged

    Parameters
    ----------

    pixelRatio : float
      Passed on as it is.
    """
    #  void Q3DScene::devicePixelRatioChanged(qreal pixelRatio)
    self.uglySide.call(
        'ritual_ZN8Q3DScene23devicePixelRatioChangedEd', pixelRatio,
    )

  @overload(QPoint)
  def selectionQueryPositionChanged(self, position: QPoint) -> None:
    """
    Calls Qt's 'void Q3DScene::selectionQueryPositionChanged(QPoint
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#selectionQueryPositionChanged

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Q3DScene::selectionQueryPositionChanged(QPoint position)
    self.uglySide.call(
        'ritual_ZN8Q3DScene29selectionQueryPositionChangedE6QPoint',
        self._valueOf(position),
    )

  @overload(QPoint)
  def graphPositionQueryChanged(self, position: QPoint) -> None:
    """
    Calls Qt's 'void Q3DScene::graphPositionQueryChanged(QPoint position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dscene.html#graphPositionQueryChanged

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void Q3DScene::graphPositionQueryChanged(QPoint position)
    self.uglySide.call(
        'ritual_ZN8Q3DScene25graphPositionQueryChangedE6QPoint',
        self._valueOf(position),
    )

  def needRender(self) -> None:
    """
    Calls Qt's 'void Q3DScene::needRender()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dscene.html#needRender
    """
    #  void Q3DScene::needRender()
    self.uglySide.call('ritual_ZN8Q3DScene10needRenderEv')
