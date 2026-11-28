"""
QQuickSaturationLightnessPickerCanvas binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquicksaturationlightnesspicker_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickSaturationLightnessPickerCanvas to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QImage
  from ..QtQuick import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSaturationLightnessPickerCanvas(QQuickItem):
  """
  The cute side of Qt's QQuickSaturationLightnessPickerCanvas: a plain Python
  object standing in front of one C++ QQuickSaturationLightnessPickerCanvas.

  It is built on the cute 'QQuickItem', as Qt's
  QQuickSaturationLightnessPickerCanvas is built on Qt's QQuickItem, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSaturationLightnessPickerCanvas that has a
  ritual and that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'hue', 'setHue', 'hueChanged', 'updatePaintNode', 'generateImage'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSaturationLightnessPickerCanvas::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QQuickSaturationLightnessPickerCanvas::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickSaturationLightnessPickerCanvas is created at the first
    use, not by 'QQuickSaturationLightnessPickerCanvas(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSaturationLightnessPickerCanvas.
  - Qt tells when it has removed the C++
    QQuickSaturationLightnessPickerCanvas. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
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
    Calls Qt's 'QString QQuickSaturationLightnessPickerCanvas::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksaturationlightnesspickercanvas.html#tr

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
    #  QString QQuickSaturationLightnessPickerCanvas::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN37QQuickSaturationLightnessPickerCanvas2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSaturationLightnessPickerCanvas'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickSaturationLightnessPickerCanvas::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksaturationlightnesspickercanvas.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSaturationLightnessPickerCanvas::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK37QQuickSaturationLightnessPickerCanvas10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def hue(self) -> float:
    """
    Calls Qt's 'qreal QQuickSaturationLightnessPickerCanvas::hue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksaturationlightnesspickercanvas.html#hue
    """
    #  qreal QQuickSaturationLightnessPickerCanvas::hue() const
    return self.uglySide.call(
        'ritual_ZNK37QQuickSaturationLightnessPickerCanvas3hueEv',
    )

  @overload(int, int, float)
  def generateImage(self, width: int, height: int, hue01: float) -> QImage:
    """
    Calls Qt's 'QImage
    QQuickSaturationLightnessPickerCanvas::generateImage(int width, int
    height, double hue01) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksaturationlightnesspickercanvas.html

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    hue01 : float
      Passed on as it is.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickSaturationLightnessPickerCanvas::generateImage(int width,
    #      int height, double hue01) const
    address = self.uglySide.call(
        'ritual_ZNK37QQuickSaturationLightnessPickerCanvas13generateImageEi'
        'id',
        width, height, hue01,
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setHue(self, h: float) -> None:
    """
    Calls Qt's 'void QQuickSaturationLightnessPickerCanvas::setHue(qreal h)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksaturationlightnesspickercanvas.html#setHue

    Parameters
    ----------

    h : float
      Passed on as it is.
    """
    #  void QQuickSaturationLightnessPickerCanvas::setHue(qreal h)
    self.uglySide.call(
        'ritual_ZN37QQuickSaturationLightnessPickerCanvas6setHueEd', h,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickSaturationLightnessPickerCanvas::
    QQuickSaturationLightnessPickerCanvas(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksaturationlightnesspickercanvas.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSaturationLightnessPickerCanvas::
    #      QQuickSaturationLightnessPickerCanvas(QQuickItem *parent)
    self._noteCreation(
        QQuickSaturationLightnessPickerCanvas, lambda: Rituals.call(
            'ritual_ZN37QQuickSaturationLightnessPickerCanvasC1EP10QQuickIt'
            'em',
            self._addressOf(parent),
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

  def hueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSaturationLightnessPickerCanvas::hueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksaturationlightnesspickercanvas.html
    """
    #  void QQuickSaturationLightnessPickerCanvas::hueChanged()
    self.uglySide.call(
        'ritual_ZN37QQuickSaturationLightnessPickerCanvas10hueChangedEv',
    )

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      oldNode: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode
    *QQuickSaturationLightnessPickerCanvas::updatePaintNode(QSGNode *oldNode,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksaturationlightnesspickercanvas.html

    Parameters
    ----------

    oldNode : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode
    #      *QQuickSaturationLightnessPickerCanvas::updatePaintNode(QSGNode
    #      *oldNode, UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN37QQuickSaturationLightnessPickerCanvas15updatePaintNodeE'
        'P7QSGNodePN10QQuickItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN37QQuickSaturationLightnessPickerCanvas15updatePain'
          'tNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(oldNode, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)
