"""
QQuickAbstractPathRenderer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickAbstractPathRenderer to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from . import QQuickShapePath

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickShapeGradient
  from ..QtGui import QColor, QPainterPath
  from ..QtQuick import QQuickItem, QQuickPath, QQuickWindow, QSGTransform
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPainterPath = WAIT['QPainterPath']
  QQuickItem = WAIT['QQuickItem']
  QQuickPath = WAIT['QQuickPath']
  QQuickShapeGradient = WAIT['QQuickShapeGradient']
  QQuickWindow = WAIT['QQuickWindow']
  QSGTransform = WAIT['QSGTransform']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAbstractPathRenderer(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickAbstractPathRenderer: a plain Python object
  standing in front of one C++ QQuickAbstractPathRenderer.

  What exists
  -----------

  Every function of Qt's QQuickAbstractPathRenderer that has a ritual and
  that Python can call so far, 17 names in all: 'endSync', 'flags',
  'setPath', 'setStrokeColor', 'setStrokeWidth', 'setCosmeticStroke',
  'setJoinStyle', 'setCapStyle', 'setFillColor', 'setFillRule',
  'setFillGradient', 'setStrokeGradient', 'setFillTextureProvider',
  'setFillTransform', 'setTriangulationScale', 'handleSceneChange',
  'updateNode'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickAbstractPathRenderer::~QQuickAbstractPathRenderer()': the
    destructor: Python never removes a C++ QQuickAbstractPathRenderer.
  - Qt's 'void QQuickAbstractPathRenderer::beginSync(int totalCount, bool
    *countChanged)': takes a number to change where it is.
  - Qt's 'void QQuickAbstractPathRenderer::setAsyncCallback(void (*)(void *)
    a0, void *a1)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuickAbstractPathRenderer::setStrokeStyle(int index,
    QQuickShapePath::StrokeStyle strokeStyle, qreal dashOffset, const
    QList<qreal> &dashPattern)': takes a type Python has no way to hand over
    yet.

  What to expect
  --------------

  - The C++ QQuickAbstractPathRenderer is created at the first use, not by
    'QQuickAbstractPathRenderer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAbstractPathRenderer.
  - Each name of Qt's QQuickAbstractPathRenderer that has no cute function
    yet, 'beginSync', 'setAsyncCallback', 'setStrokeStyle', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickAbstractPathRenderer, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class FillGradientType(CuteNum):
    """
    The enum 'QQuickAbstractPathRenderer::FillGradientType' of Qt, with the 4
    names Qt gives in it.
    """

    NoGradient = Kee[int](0)
    LinearGradient = Kee[int](1)
    RadialGradient = Kee[int](2)
    ConicalGradient = Kee[int](3)

  class Flag(CuteFlags):
    """
    The flags enum 'QQuickAbstractPathRenderer::Flag' of Qt, with the 1 names
    Qt gives in it. Qt names the type of its combinations
    'QQuickAbstractPathRenderer::Flags'.
    """

    SupportsAsync = 0x1

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAbstractPathRenderer'

  #  A C++ QQuickAbstractPathRenderer Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAbstractPathRenderer'

  #  The functions Qt calls itself that QQuickAbstractPathRenderer is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'beginSync': (
          'void QQuickAbstractPathRenderer::beginSync(int, bool *)',
      ),
      'setAsyncCallback': (
          'void QQuickAbstractPathRenderer::setAsyncCallback(void (*)(void '
          '*), void *)',
      ),
      'setStrokeStyle': (
          'void QQuickAbstractPathRenderer::setStrokeStyle(int, '
          'QQuickShapePath::StrokeStyle, qreal, const QList<qreal> &)',
      ),
  }

  #  The functions Qt calls itself that QQuickAbstractPathRenderer is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'endSync': (
          ('_ZN26QQuickAbstractPathRenderer7endSyncEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'flags': (
          ('_ZNK26QQuickAbstractPathRenderer5flagsEv',
           ('int', 'flags', 'QtQuickShapes:QQuickAbstractPathRenderer.Flag'),
           ()),
      ),
      'setPath': (
          ('_ZN26QQuickAbstractPathRenderer7setPathEiPK10QQuickPath',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtQuick:QQuickPath'),
           )),
          ('_ZN26QQuickAbstractPathRenderer7setPathEiRK12QPainterPath6QFlag'
           'sIN15QQuickShapePath8PathHintEE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QPainterPath'),
               ('int', 'flags', 'QtQuickShapes:QQuickShapePath.PathHint'),
           )),
      ),
      'setStrokeColor': (
          ('_ZN26QQuickAbstractPathRenderer14setStrokeColorEiRK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'setStrokeWidth': (
          ('_ZN26QQuickAbstractPathRenderer14setStrokeWidthEid',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'setCosmeticStroke': (
          ('_ZN26QQuickAbstractPathRenderer17setCosmeticStrokeEib',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('bool', 'number', ''),
           )),
      ),
      'setJoinStyle': (
          ('_ZN26QQuickAbstractPathRenderer12setJoinStyleEiN15QQuickShapePa'
           'th9JoinStyleEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'enum', 'QtQuickShapes:QQuickShapePath.JoinStyle'),
               ('int', 'number', ''),
           )),
      ),
      'setCapStyle': (
          ('_ZN26QQuickAbstractPathRenderer11setCapStyleEiN15QQuickShapePat'
           'h8CapStyleE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'enum', 'QtQuickShapes:QQuickShapePath.CapStyle'),
           )),
      ),
      'setFillColor': (
          ('_ZN26QQuickAbstractPathRenderer12setFillColorEiRK6QColor',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtGui:QColor'),
           )),
      ),
      'setFillRule': (
          ('_ZN26QQuickAbstractPathRenderer11setFillRuleEiN15QQuickShapePat'
           'h8FillRuleE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'enum', 'QtQuickShapes:QQuickShapePath.FillRule'),
           )),
      ),
      'setFillGradient': (
          ('_ZN26QQuickAbstractPathRenderer15setFillGradientEiP19QQuickShap'
           'eGradient',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtQuickShapes:QQuickShapeGradient'),
           )),
      ),
      'setStrokeGradient': (
          ('_ZN26QQuickAbstractPathRenderer17setStrokeGradientEiP19QQuickSh'
           'apeGradient',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtQuickShapes:QQuickShapeGradient'),
           )),
      ),
      'setFillTextureProvider': (
          ('_ZN26QQuickAbstractPathRenderer22setFillTextureProviderEiP10QQu'
           'ickItem',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'setFillTransform': (
          ('_ZN26QQuickAbstractPathRenderer16setFillTransformEiRK12QSGTrans'
           'form',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('address', 'value', 'QtQuick:QSGTransform'),
           )),
      ),
      'setTriangulationScale': (
          ('_ZN26QQuickAbstractPathRenderer21setTriangulationScaleEid',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('double', 'number', ''),
           )),
      ),
      'handleSceneChange': (
          ('_ZN26QQuickAbstractPathRenderer17handleSceneChangeEP12QQuickWin'
           'dow',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickWindow'),
           )),
      ),
      'updateNode': (
          ('_ZN26QQuickAbstractPathRenderer10updateNodeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QQuickAbstractPathRenderer::flags() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QQuickAbstractPathRenderer::flags() const
    ritual = 'ritual_ZNK26QQuickAbstractPathRenderer5flagsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QQuickAbstractPathRenderer5flagsEv'
    return QQuickAbstractPathRenderer.Flags(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QQuickPath)
  @overload(int, NoneType)
  def setPath(self, index: int, path: Optional[QQuickPath]) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setPath(int index, const
    QQuickPath *path)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#setPath

    Parameters
    ----------

    index : int
      Passed on as it is.

    path : Optional[QQuickPath]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractPathRenderer::setPath(int index, const QQuickPath
    #      *path)
    ritual = 'ritual_ZN26QQuickAbstractPathRenderer7setPathEiPK10QQuickPath'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickAbstractPathRenderer7setPathEiPK10QQuickPat'
          'h')
    self.uglySide.call(ritual, index, self._addressOf(path))

  @overload(int, QPainterPath)
  @overload(int, QPainterPath, QQuickShapePath.PathHints)
  def setPath(
      self,
      index: int,
      path: QPainterPath,
      pathHints: QQuickShapePath.PathHints = QQuickShapePath.PathHints(),
  ) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setPath(int index, const
    QPainterPath &path, QQuickShapePath::PathHints pathHints)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#setPath

    Parameters
    ----------

    index : int
      Passed on as it is.

    path : QPainterPath
      Passed on as a value: Qt reads the C++ QPainterPath, which stays
      Python's own.

    pathHints : QQuickShapePath.PathHints
      Passed on as its number. May be left out, as in Qt: it is then
      QQuickShapePath.PathHints().
    """
    #  void QQuickAbstractPathRenderer::setPath(int index, const QPainterPath
    #      &path, QQuickShapePath::PathHints pathHints)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer7setPathEiRK12QPainterPath6QF'
        'lagsIN15QQuickShapePath8PathHintEE',
        index, self._valueOf(path), pathHints.value,
    )

  @overload(int, QColor)
  def setStrokeColor(self, index: int, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setStrokeColor(int index,
    const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#setStrokeColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickAbstractPathRenderer::setStrokeColor(int index, const
    #      QColor &color)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer14setStrokeColorEiRK6QColor',
        index, self._valueOf(color),
    )

  @overload(int, float)
  def setStrokeWidth(self, index: int, w: float) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setStrokeWidth(int index,
    qreal w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#setStrokeWidth

    Parameters
    ----------

    index : int
      Passed on as it is.

    w : float
      Passed on as it is.
    """
    #  void QQuickAbstractPathRenderer::setStrokeWidth(int index, qreal w)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer14setStrokeWidthEid', index, w,
    )

  @overload(int, bool)
  def setCosmeticStroke(self, index: int, c: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setCosmeticStroke(int index,
    bool c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#setCosmeticStroke

    Parameters
    ----------

    index : int
      Passed on as it is.

    c : bool
      Passed on as it is.
    """
    #  void QQuickAbstractPathRenderer::setCosmeticStroke(int index, bool c)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer17setCosmeticStrokeEib',
        index, c,
    )

  @overload(int, QQuickShapePath.JoinStyle, int)
  def setJoinStyle(
      self,
      index: int,
      joinStyle: QQuickShapePath.JoinStyle,
      miterLimit: int,
  ) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setJoinStyle(int index,
    QQuickShapePath::JoinStyle joinStyle, int miterLimit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#setJoinStyle

    Parameters
    ----------

    index : int
      Passed on as it is.

    joinStyle : QQuickShapePath.JoinStyle
      Passed on as its number.

    miterLimit : int
      Passed on as it is.
    """
    #  void QQuickAbstractPathRenderer::setJoinStyle(int index,
    #      QQuickShapePath::JoinStyle joinStyle, int miterLimit)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer12setJoinStyleEiN15QQuickShap'
        'ePath9JoinStyleEi',
        index, joinStyle.value, miterLimit,
    )

  @overload(int, QQuickShapePath.CapStyle)
  def setCapStyle(
      self,
      index: int,
      capStyle: QQuickShapePath.CapStyle,
  ) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setCapStyle(int index,
    QQuickShapePath::CapStyle capStyle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#setCapStyle

    Parameters
    ----------

    index : int
      Passed on as it is.

    capStyle : QQuickShapePath.CapStyle
      Passed on as its number.
    """
    #  void QQuickAbstractPathRenderer::setCapStyle(int index,
    #      QQuickShapePath::CapStyle capStyle)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer11setCapStyleEiN15QQuickShape'
        'Path8CapStyleE',
        index, capStyle.value,
    )

  @overload(int, QColor)
  def setFillColor(self, index: int, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setFillColor(int index,
    const QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#setFillColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickAbstractPathRenderer::setFillColor(int index, const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer12setFillColorEiRK6QColor',
        index, self._valueOf(color),
    )

  @overload(int, QQuickShapePath.FillRule)
  def setFillRule(
      self,
      index: int,
      fillRule: QQuickShapePath.FillRule,
  ) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setFillRule(int index,
    QQuickShapePath::FillRule fillRule)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#setFillRule

    Parameters
    ----------

    index : int
      Passed on as it is.

    fillRule : QQuickShapePath.FillRule
      Passed on as its number.
    """
    #  void QQuickAbstractPathRenderer::setFillRule(int index,
    #      QQuickShapePath::FillRule fillRule)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer11setFillRuleEiN15QQuickShape'
        'Path8FillRuleE',
        index, fillRule.value,
    )

  @overload(int, QQuickShapeGradient)
  @overload(int, NoneType)
  def setFillGradient(
      self,
      index: int,
      gradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setFillGradient(int index,
    QQuickShapeGradient *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#setFillGradient

    Parameters
    ----------

    index : int
      Passed on as it is.

    gradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractPathRenderer::setFillGradient(int index,
    #      QQuickShapeGradient *gradient)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer15setFillGradientEiP19QQuickS'
        'hapeGradient',
        index, self._addressOf(gradient),
    )

  @overload(int, QQuickShapeGradient)
  @overload(int, NoneType)
  def setStrokeGradient(
      self,
      index: int,
      gradient: Optional[QQuickShapeGradient],
  ) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setStrokeGradient(int index,
    QQuickShapeGradient *gradient)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#setStrokeGradient

    Parameters
    ----------

    index : int
      Passed on as it is.

    gradient : Optional[QQuickShapeGradient]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractPathRenderer::setStrokeGradient(int index,
    #      QQuickShapeGradient *gradient)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer17setStrokeGradientEiP19QQuic'
        'kShapeGradient',
        index, self._addressOf(gradient),
    )

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def setFillTextureProvider(
      self,
      index: int,
      textureProviderItem: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setFillTextureProvider(int
    index, QQuickItem *textureProviderItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    textureProviderItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractPathRenderer::setFillTextureProvider(int index,
    #      QQuickItem *textureProviderItem)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer22setFillTextureProviderEiP10'
        'QQuickItem',
        index, self._addressOf(textureProviderItem),
    )

  @overload(int, QSGTransform)
  def setFillTransform(self, index: int, transform: QSGTransform) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setFillTransform(int index,
    const QSGTransform &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#setFillTransform

    Parameters
    ----------

    index : int
      Passed on as it is.

    transform : QSGTransform
      Passed on as a value: Qt reads the C++ QSGTransform, which stays
      Python's own.
    """
    #  void QQuickAbstractPathRenderer::setFillTransform(int index, const
    #      QSGTransform &transform)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer16setFillTransformEiRK12QSGTr'
        'ansform',
        index, self._valueOf(transform),
    )

  @overload(int, float)
  def setTriangulationScale(self, a0: int, a1: float) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::setTriangulationScale(int
    a0, qreal a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.

    a1 : float
      Passed on as it is.
    """
    #  void QQuickAbstractPathRenderer::setTriangulationScale(int a0, qreal
    #      a1)
    ritual = (
        'ritual_ZN26QQuickAbstractPathRenderer21setTriangulationScaleEid')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickAbstractPathRenderer21setTriangulationScale'
          'Eid')
    self.uglySide.call(ritual, a0, a1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(bool)
  def endSync(self, async_: bool) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::endSync(bool async)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#endSync

    Parameters
    ----------

    async_ : bool
      Passed on as it is.
    """
    #  void QQuickAbstractPathRenderer::endSync(bool async)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer7endSyncEb', async_,
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def handleSceneChange(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void
    QQuickAbstractPathRenderer::handleSceneChange(QQuickWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#handleSceneChange

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAbstractPathRenderer::handleSceneChange(QQuickWindow
    #      *window)
    self.uglySide.call(
        'ritual_ZN26QQuickAbstractPathRenderer17handleSceneChangeEP12QQuick'
        'Window',
        self._addressOf(window),
    )

  def updateNode(self) -> None:
    """
    Calls Qt's 'void QQuickAbstractPathRenderer::updateNode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickabstractpathrenderer.html#updateNode
    """
    #  void QQuickAbstractPathRenderer::updateNode()
    self.uglySide.call('ritual_ZN26QQuickAbstractPathRenderer10updateNodeEv')

  @staticmethod
  def beginSync(*__, **_) -> Never:
    """
    Qt's 'void QQuickAbstractPathRenderer::beginSync(int totalCount, bool
    *countChanged)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQuickAbstractPathRenderer.beginSync' has no cute function yet. "
        "Qt's 'void QQuickAbstractPathRenderer::beginSync(int totalCount, "
        "bool *countChanged)': takes a number to change where it is.")

  @staticmethod
  def setAsyncCallback(*__, **_) -> Never:
    """
    Qt's 'void QQuickAbstractPathRenderer::setAsyncCallback(void (*)(void *)
    a0, void *a1)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickAbstractPathRenderer.setAsyncCallback' has no cute function "
        "yet. Qt's 'void QQuickAbstractPathRenderer::setAsyncCallback(void "
        "(*)(void *) a0, void *a1)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def setStrokeStyle(*__, **_) -> Never:
    """
    Qt's 'void QQuickAbstractPathRenderer::setStrokeStyle(int index,
    QQuickShapePath::StrokeStyle strokeStyle, qreal dashOffset, const
    QList<qreal> &dashPattern)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuickAbstractPathRenderer.setStrokeStyle' has no cute function "
        "yet. Qt's 'void QQuickAbstractPathRenderer::setStrokeStyle(int "
        "index, QQuickShapePath::StrokeStyle strokeStyle, qreal dashOffset, "
        "const QList<qreal> &dashPattern)': takes a type Python has no way "
        "to hand over yet.")
