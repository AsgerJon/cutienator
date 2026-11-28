"""
Q3DScenePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/q3dscene_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Q3DScenePrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRect, QSize
  from ..QtGui import QVector3D
  from . import Q3DScene
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  Q3DScene = WAIT['QtDataVisualization:Q3DScene']
  QRect = WAIT['QRect']
  QSize = WAIT['QSize']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Q3DScenePrivate(QObject):
  """
  The cute side of Qt's Q3DScenePrivate: a plain Python object standing in
  front of one C++ Q3DScenePrivate.

  It is built on the cute 'QObject', as Qt's Q3DScenePrivate is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Q3DScenePrivate that has a ritual and that Python
  can call so far, 16 names in all: 'metaObject', 'tr', 'setViewport',
  'setViewportSize', 'setWindowSize', 'windowSize', 'calculateSubViewports',
  'updateGLViewport', 'updateGLSubViewports', 'glViewport',
  'glPrimarySubViewport', 'glSecondarySubViewport',
  'setLightPositionRelativeToCamera', 'markDirty', 'isInArea', 'needRender'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Q3DScenePrivate::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int Q3DScenePrivate::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'Q3DScenePrivate::~Q3DScenePrivate()': the destructor: Python never
    removes a C++ Q3DScenePrivate.
  - Qt's 'void Q3DScenePrivate::sync(Q3DScenePrivate &other)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Q3DScenePrivate is created at the first use, not by
    'Q3DScenePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Q3DScenePrivate.
  - Qt tells when it has removed the C++ Q3DScenePrivate. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Q3DScenePrivate that has no cute function yet, 'sync',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString Q3DScenePrivate::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#tr

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
    #  QString Q3DScenePrivate::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15Q3DScenePrivate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Q3DScenePrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ Q3DScenePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Q3DScenePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Q3DScenePrivate::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Q3DScenePrivate::metaObject() const
    address = self.uglySide.call('ritual_ZNK15Q3DScenePrivate10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def windowSize(self) -> QSize:
    """
    Calls Qt's 'QSize Q3DScenePrivate::windowSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#windowSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize Q3DScenePrivate::windowSize() const
    address = self.uglySide.call('ritual_ZNK15Q3DScenePrivate10windowSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(QRect, int, int)
  def isInArea(self, area: QRect, x: int, y: int) -> bool:
    """
    Calls Qt's 'bool Q3DScenePrivate::isInArea(const QRect &area, int x, int
    y) const'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#isInArea

    Parameters
    ----------

    area : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.
    """
    #  bool Q3DScenePrivate::isInArea(const QRect &area, int x, int y) const
    return self.uglySide.call(
        'ritual_ZNK15Q3DScenePrivate8isInAreaERK5QRectii',
        self._valueOf(area), x, y,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRect)
  def setViewport(self, viewport: QRect) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::setViewport(const QRect &viewport)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#setViewport

    Parameters
    ----------

    viewport : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
    """
    #  void Q3DScenePrivate::setViewport(const QRect &viewport)
    self.uglySide.call(
        'ritual_ZN15Q3DScenePrivate11setViewportERK5QRect',
        self._valueOf(viewport),
    )

  @overload(int, int)
  def setViewportSize(self, width: int, height: int) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::setViewportSize(int width, int
    height)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsceneprivate.html#setViewportSize

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.
    """
    #  void Q3DScenePrivate::setViewportSize(int width, int height)
    self.uglySide.call(
        'ritual_ZN15Q3DScenePrivate15setViewportSizeEii', width, height,
    )

  @overload(QSize)
  def setWindowSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::setWindowSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#setWindowSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void Q3DScenePrivate::setWindowSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN15Q3DScenePrivate13setWindowSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(QVector3D)
  @overload(QVector3D, float)
  @overload(QVector3D, float, float)
  def setLightPositionRelativeToCamera(
      self,
      relativePosition: QVector3D,
      fixedRotation: float = 0.0,
      distanceModifier: float = 0.0,
  ) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::setLightPositionRelativeToCamera(const
    QVector3D &relativePosition, float fixedRotation, float
    distanceModifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsceneprivate.html

    Parameters
    ----------

    relativePosition : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    fixedRotation : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.

    distanceModifier : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void Q3DScenePrivate::setLightPositionRelativeToCamera(const QVector3D
    #      &relativePosition, float fixedRotation, float distanceModifier)
    self.uglySide.call(
        'ritual_ZN15Q3DScenePrivate32setLightPositionRelativeToCameraERK9QV'
        'ector3Dff',
        self._valueOf(relativePosition), fixedRotation, distanceModifier,
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

  @overload(Q3DScene)
  @overload(NoneType)
  def __init__(self, q: Optional[Q3DScene]) -> None:
    """
    Notes what was given, for Qt's 'Q3DScenePrivate::Q3DScenePrivate(Q3DScene
    *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsceneprivate.html#Q3DScenePrivate

    Parameters
    ----------

    q : Optional[Q3DScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Q3DScenePrivate::Q3DScenePrivate(Q3DScene *q)
    self._noteCreation(Q3DScenePrivate, lambda: Rituals.call(
        'ritual_ZN15Q3DScenePrivateC1EP8Q3DScene', self._addressOf(q),
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

  def calculateSubViewports(self) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::calculateSubViewports()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsceneprivate.html#calculateSubViewports
    """
    #  void Q3DScenePrivate::calculateSubViewports()
    self.uglySide.call('ritual_ZN15Q3DScenePrivate21calculateSubViewportsEv')

  def updateGLViewport(self) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::updateGLViewport()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsceneprivate.html#updateGLViewport
    """
    #  void Q3DScenePrivate::updateGLViewport()
    self.uglySide.call('ritual_ZN15Q3DScenePrivate16updateGLViewportEv')

  def updateGLSubViewports(self) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::updateGLSubViewports()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsceneprivate.html#updateGLSubViewports
    """
    #  void Q3DScenePrivate::updateGLSubViewports()
    self.uglySide.call('ritual_ZN15Q3DScenePrivate20updateGLSubViewportsEv')

  def glViewport(self) -> QRect:
    """
    Calls Qt's 'QRect Q3DScenePrivate::glViewport()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#glViewport

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect Q3DScenePrivate::glViewport()
    address = self.uglySide.call('ritual_ZN15Q3DScenePrivate10glViewportEv')
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def glPrimarySubViewport(self) -> QRect:
    """
    Calls Qt's 'QRect Q3DScenePrivate::glPrimarySubViewport()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsceneprivate.html#glPrimarySubViewport

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect Q3DScenePrivate::glPrimarySubViewport()
    address = self.uglySide.call(
        'ritual_ZN15Q3DScenePrivate20glPrimarySubViewportEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def glSecondarySubViewport(self) -> QRect:
    """
    Calls Qt's 'QRect Q3DScenePrivate::glSecondarySubViewport()'.

    Qt's own words:
    https://doc.qt.io/qt-6/q3dsceneprivate.html#glSecondarySubViewport

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect Q3DScenePrivate::glSecondarySubViewport()
    address = self.uglySide.call(
        'ritual_ZN15Q3DScenePrivate22glSecondarySubViewportEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  def markDirty(self) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::markDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#markDirty
    """
    #  void Q3DScenePrivate::markDirty()
    self.uglySide.call('ritual_ZN15Q3DScenePrivate9markDirtyEv')

  def needRender(self) -> None:
    """
    Calls Qt's 'void Q3DScenePrivate::needRender()'.

    Qt's own words: https://doc.qt.io/qt-6/q3dsceneprivate.html#needRender
    """
    #  void Q3DScenePrivate::needRender()
    self.uglySide.call('ritual_ZN15Q3DScenePrivate10needRenderEv')

  @staticmethod
  def sync(*__, **_) -> Never:
    """
    Qt's 'void Q3DScenePrivate::sync(Q3DScenePrivate &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Q3DScenePrivate.sync' has no cute function yet. Qt's 'void "
        "Q3DScenePrivate::sync(Q3DScenePrivate &other)': takes a type "
        "Python has no way to hand over yet.")
