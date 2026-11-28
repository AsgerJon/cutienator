"""
QQuickShape binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickShape to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QRectF
  from . import QQuickShapePrivate
  from ..QtQuick import QSGNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']
  QSGNode = WAIT['QSGNode']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickShape(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickShape: a plain Python object standing in front
  of one C++ QQuickShape.

  What exists
  -----------

  Every function of Qt's QQuickShape that has a ritual and that Python can
  call so far, 36 names in all: 'metaObject', 'tr', 'rendererType',
  'asynchronous', 'setAsynchronous', 'preferredRendererType',
  'setPreferredRendererType', 'boundingRect', 'vendorExtensionsEnabled',
  'setVendorExtensionsEnabled', 'status', 'containsMode', 'setContainsMode',
  'contains', 'fillMode', 'setFillMode', 'horizontalAlignment',
  'setHorizontalAlignment', 'verticalAlignment', 'setVerticalAlignment',
  'updatePaintNode', 'updatePolish', 'itemChange', 'componentComplete',
  'classBegin', 'rendererChanged', 'asynchronousChanged',
  'vendorExtensionsEnabledChanged', 'statusChanged',
  'preferredRendererTypeChanged', 'boundingRectChanged',
  'containsModeChanged', 'fillModeChanged', 'horizontalAlignmentChanged',
  'verticalAlignmentChanged', 'd_func'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickShape::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickShape::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickShape::~QQuickShape()': the destructor: Python never removes
    a C++ QQuickShape.
  - Qt's 'QQmlListProperty<QObject> QQuickShape::data()': gives a type Python
    has no way to take yet.
  - Qt's 'QQuickShape::QQuickShape(QQuickShapePrivate &dd, QQuickItem
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickShapePrivate *QQuickShape::d_func() const': takes in
    Python what 'QQuickShapePrivate *QQuickShape::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 47 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickShape is created at the first use, not by
    'QQuickShape(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickShape.
  - Qt tells when it has removed the C++ QQuickShape. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQuickShape that has no cute function yet, 'data',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QQuickShape, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ContainsMode(CuteNum):
    """
    The enum 'QQuickShape::ContainsMode' of Qt, with the 2 names Qt gives in
    it.
    """

    BoundingRectContains = Kee[int](0)
    FillContains = Kee[int](1)

  class FillMode(CuteNum):
    """
    The enum 'QQuickShape::FillMode' of Qt, with the 4 names Qt gives in it.
    """

    NoResize = Kee[int](0)
    PreserveAspectFit = Kee[int](1)
    PreserveAspectCrop = Kee[int](2)
    Stretch = Kee[int](3)

  class HAlignment(CuteNum):
    """
    The enum 'QQuickShape::HAlignment' of Qt, with the 3 names Qt gives in
    it.
    """

    AlignLeft = Kee[int](1)
    AlignRight = Kee[int](2)
    AlignHCenter = Kee[int](4)

  class RendererType(CuteNum):
    """
    The enum 'QQuickShape::RendererType' of Qt, with the 5 names Qt gives in
    it.
    """

    UnknownRenderer = Kee[int](0)
    GeometryRenderer = Kee[int](1)
    NvprRenderer = Kee[int](2)
    SoftwareRenderer = Kee[int](3)
    CurveRenderer = Kee[int](4)

  class Status(CuteNum):
    """
    The enum 'QQuickShape::Status' of Qt, with the 3 names Qt gives in it.
    """

    Null = Kee[int](0)
    Ready = Kee[int](1)
    Processing = Kee[int](2)

  class VAlignment(CuteNum):
    """
    The enum 'QQuickShape::VAlignment' of Qt, with the 3 names Qt gives in
    it.
    """

    AlignTop = Kee[int](32)
    AlignBottom = Kee[int](64)
    AlignVCenter = Kee[int](128)

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
    Calls Qt's 'QString QQuickShape::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#tr

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
    #  QString QQuickShape::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQuickShape2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickShape'

  #  A C++ QQuickShape Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickShape'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickShape::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickShape::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQuickShape10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rendererType(self) -> RendererType:
    """
    Calls Qt's 'RendererType QQuickShape::rendererType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#rendererType

    Returns
    -------

    RendererType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RendererType(number)'
      gives.
    """
    #  RendererType QQuickShape::rendererType() const
    return QQuickShape.RendererType(self.uglySide.call(
        'ritual_ZNK11QQuickShape12rendererTypeEv',
    ))

  def asynchronous(self) -> bool:
    """
    Calls Qt's 'bool QQuickShape::asynchronous() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#asynchronous
    """
    #  bool QQuickShape::asynchronous() const
    return self.uglySide.call('ritual_ZNK11QQuickShape12asynchronousEv')

  def preferredRendererType(self) -> RendererType:
    """
    Calls Qt's 'RendererType QQuickShape::preferredRendererType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#preferredRendererType

    Returns
    -------

    RendererType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RendererType(number)'
      gives.
    """
    #  RendererType QQuickShape::preferredRendererType() const
    return QQuickShape.RendererType(self.uglySide.call(
        'ritual_ZNK11QQuickShape21preferredRendererTypeEv',
    ))

  def boundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickShape::boundingRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#boundingRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickShape::boundingRect() const
    ritual = 'ritual_ZNK11QQuickShape12boundingRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQuickShape12boundingRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def vendorExtensionsEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickShape::vendorExtensionsEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#vendorExtensionsEnabled
    """
    #  bool QQuickShape::vendorExtensionsEnabled() const
    return self.uglySide.call(
        'ritual_ZNK11QQuickShape23vendorExtensionsEnabledEv',
    )

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQuickShape::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQuickShape::status() const
    return QQuickShape.Status(self.uglySide.call(
        'ritual_ZNK11QQuickShape6statusEv',
    ))

  def containsMode(self) -> ContainsMode:
    """
    Calls Qt's 'ContainsMode QQuickShape::containsMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#containsMode

    Returns
    -------

    ContainsMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ContainsMode(number)'
      gives.
    """
    #  ContainsMode QQuickShape::containsMode() const
    return QQuickShape.ContainsMode(self.uglySide.call(
        'ritual_ZNK11QQuickShape12containsModeEv',
    ))

  @overload(QPointF)
  def contains(self, point: QPointF) -> bool:
    """
    Calls Qt's 'bool QQuickShape::contains(const QPointF &point) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#contains

    Parameters
    ----------

    point : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  bool QQuickShape::contains(const QPointF &point) const
    ritual = 'ritual_ZNK11QQuickShape8containsERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QQuickShape8containsERK7QPointF'
    return self.uglySide.call(ritual, self._valueOf(point, 'QPointF'))

  def fillMode(self) -> FillMode:
    """
    Calls Qt's 'FillMode QQuickShape::fillMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#fillMode

    Returns
    -------

    FillMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FillMode(number)' gives.
    """
    #  FillMode QQuickShape::fillMode() const
    return QQuickShape.FillMode(self.uglySide.call(
        'ritual_ZNK11QQuickShape8fillModeEv',
    ))

  def horizontalAlignment(self) -> HAlignment:
    """
    Calls Qt's 'HAlignment QQuickShape::horizontalAlignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#horizontalAlignment

    Returns
    -------

    HAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'HAlignment(number)'
      gives.
    """
    #  HAlignment QQuickShape::horizontalAlignment() const
    return QQuickShape.HAlignment(self.uglySide.call(
        'ritual_ZNK11QQuickShape19horizontalAlignmentEv',
    ))

  def verticalAlignment(self) -> VAlignment:
    """
    Calls Qt's 'VAlignment QQuickShape::verticalAlignment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#verticalAlignment

    Returns
    -------

    VAlignment
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'VAlignment(number)'
      gives.
    """
    #  VAlignment QQuickShape::verticalAlignment() const
    return QQuickShape.VAlignment(self.uglySide.call(
        'ritual_ZNK11QQuickShape17verticalAlignmentEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAsynchronous(self, async_: bool) -> None:
    """
    Calls Qt's 'void QQuickShape::setAsynchronous(bool async)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#setAsynchronous

    Parameters
    ----------

    async_ : bool
      Passed on as it is.
    """
    #  void QQuickShape::setAsynchronous(bool async)
    self.uglySide.call('ritual_ZN11QQuickShape15setAsynchronousEb', async_)

  @overload(RendererType)
  def setPreferredRendererType(self, preferredType: RendererType) -> None:
    """
    Calls Qt's 'void QQuickShape::setPreferredRendererType(RendererType
    preferredType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#setPreferredRendererType

    Parameters
    ----------

    preferredType : RendererType
      Passed on as its number.
    """
    #  void QQuickShape::setPreferredRendererType(RendererType preferredType)
    self.uglySide.call(
        'ritual_ZN11QQuickShape24setPreferredRendererTypeENS_12RendererType'
        'E',
        preferredType.value,
    )

  @overload(bool)
  def setVendorExtensionsEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QQuickShape::setVendorExtensionsEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#setVendorExtensionsEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QQuickShape::setVendorExtensionsEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN11QQuickShape26setVendorExtensionsEnabledEb', enable,
    )

  @overload(ContainsMode)
  def setContainsMode(self, containsMode: ContainsMode) -> None:
    """
    Calls Qt's 'void QQuickShape::setContainsMode(ContainsMode
    containsMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#setContainsMode

    Parameters
    ----------

    containsMode : ContainsMode
      Passed on as its number.
    """
    #  void QQuickShape::setContainsMode(ContainsMode containsMode)
    self.uglySide.call(
        'ritual_ZN11QQuickShape15setContainsModeENS_12ContainsModeE',
        containsMode.value,
    )

  @overload(FillMode)
  def setFillMode(self, newFillMode: FillMode) -> None:
    """
    Calls Qt's 'void QQuickShape::setFillMode(FillMode newFillMode)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#setFillMode

    Parameters
    ----------

    newFillMode : FillMode
      Passed on as its number.
    """
    #  void QQuickShape::setFillMode(FillMode newFillMode)
    self.uglySide.call(
        'ritual_ZN11QQuickShape11setFillModeENS_8FillModeE',
        newFillMode.value,
    )

  @overload(HAlignment)
  def setHorizontalAlignment(
      self,
      newHorizontalAlignment: HAlignment,
  ) -> None:
    """
    Calls Qt's 'void QQuickShape::setHorizontalAlignment(HAlignment
    newHorizontalAlignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#setHorizontalAlignment

    Parameters
    ----------

    newHorizontalAlignment : HAlignment
      Passed on as its number.
    """
    #  void QQuickShape::setHorizontalAlignment(HAlignment
    #      newHorizontalAlignment)
    self.uglySide.call(
        'ritual_ZN11QQuickShape22setHorizontalAlignmentENS_10HAlignmentE',
        newHorizontalAlignment.value,
    )

  @overload(VAlignment)
  def setVerticalAlignment(self, newVerticalAlignment: VAlignment) -> None:
    """
    Calls Qt's 'void QQuickShape::setVerticalAlignment(VAlignment
    newVerticalAlignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#setVerticalAlignment

    Parameters
    ----------

    newVerticalAlignment : VAlignment
      Passed on as its number.
    """
    #  void QQuickShape::setVerticalAlignment(VAlignment
    #      newVerticalAlignment)
    self.uglySide.call(
        'ritual_ZN11QQuickShape20setVerticalAlignmentENS_10VAlignmentE',
        newVerticalAlignment.value,
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
    Notes what was given, for Qt's 'QQuickShape::QQuickShape(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#QQuickShape

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickShape::QQuickShape(QQuickItem *parent)
    self._noteCreation(QQuickShape, lambda: Rituals.call(
        'ritual_ZN11QQuickShapeC1EP10QQuickItem', self._addressOf(parent),
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

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      node: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickShape::updatePaintNode(QSGNode *node,
    UpdatePaintNodeData *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#updatePaintNode

    Parameters
    ----------

    node : Optional[QSGNode]
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
    #  QSGNode *QQuickShape::updatePaintNode(QSGNode *node,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN11QQuickShape15updatePaintNodeEP7QSGNodePN10QQuickItem19U'
        'pdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQuickShape15updatePaintNodeEP7QSGNodePN10QQuickI'
          'tem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(node, 'QSGNode'), self._addressOf(a1),
    )
    from ..QtQuick import QSGNode
    return QSGNode._cuteAt(address)

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickShape::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#updatePolish
    """
    #  void QQuickShape::updatePolish()
    ritual = 'ritual_ZN11QQuickShape12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickShape12updatePolishEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickShape::itemChange(ItemChange change, const
    ItemChangeData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickShape::itemChange(ItemChange change, const ItemChangeData
    #      &data)
    ritual = (
        'ritual_ZN11QQuickShape10itemChangeEN10QQuickItem10ItemChangeERKNS0'
        '_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QQuickShape10itemChangeEN10QQuickItem10ItemChange'
          'ERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickShape::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#componentComplete
    """
    #  void QQuickShape::componentComplete()
    ritual = 'ritual_ZN11QQuickShape17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickShape17componentCompleteEv'
    self.uglySide.call(ritual)

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickShape::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#classBegin
    """
    #  void QQuickShape::classBegin()
    ritual = 'ritual_ZN11QQuickShape10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QQuickShape10classBeginEv'
    self.uglySide.call(ritual)

  def rendererChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShape::rendererChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#rendererChanged
    """
    #  void QQuickShape::rendererChanged()
    self.uglySide.call('ritual_ZN11QQuickShape15rendererChangedEv')

  def asynchronousChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShape::asynchronousChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#asynchronousChanged
    """
    #  void QQuickShape::asynchronousChanged()
    self.uglySide.call('ritual_ZN11QQuickShape19asynchronousChangedEv')

  def vendorExtensionsEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShape::vendorExtensionsEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#vendorExtensionsEnabledChanged
    """
    #  void QQuickShape::vendorExtensionsEnabledChanged()
    self.uglySide.call(
        'ritual_ZN11QQuickShape30vendorExtensionsEnabledChangedEv',
    )

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShape::statusChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#statusChanged
    """
    #  void QQuickShape::statusChanged()
    self.uglySide.call('ritual_ZN11QQuickShape13statusChangedEv')

  def preferredRendererTypeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShape::preferredRendererTypeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#preferredRendererTypeChanged
    """
    #  void QQuickShape::preferredRendererTypeChanged()
    self.uglySide.call(
        'ritual_ZN11QQuickShape28preferredRendererTypeChangedEv',
    )

  def boundingRectChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShape::boundingRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#boundingRectChanged
    """
    #  void QQuickShape::boundingRectChanged()
    self.uglySide.call('ritual_ZN11QQuickShape19boundingRectChangedEv')

  def containsModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShape::containsModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#containsModeChanged
    """
    #  void QQuickShape::containsModeChanged()
    self.uglySide.call('ritual_ZN11QQuickShape19containsModeChangedEv')

  def fillModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShape::fillModeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#fillModeChanged
    """
    #  void QQuickShape::fillModeChanged()
    self.uglySide.call('ritual_ZN11QQuickShape15fillModeChangedEv')

  def horizontalAlignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShape::horizontalAlignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#horizontalAlignmentChanged
    """
    #  void QQuickShape::horizontalAlignmentChanged()
    self.uglySide.call(
        'ritual_ZN11QQuickShape26horizontalAlignmentChangedEv',
    )

  def verticalAlignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickShape::verticalAlignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickshape.html#verticalAlignmentChanged
    """
    #  void QQuickShape::verticalAlignmentChanged()
    self.uglySide.call('ritual_ZN11QQuickShape24verticalAlignmentChangedEv')

  def d_func(self) -> Optional[QQuickShapePrivate]:
    """
    Calls Qt's 'QQuickShapePrivate *QQuickShape::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickshape.html#d_func

    Returns
    -------

    Optional[QQuickShapePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickShapePrivate *QQuickShape::d_func()
    address = self.uglySide.call('ritual_ZN11QQuickShape6d_funcEv')
    from . import QQuickShapePrivate
    return QQuickShapePrivate._cuteAt(address)

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickShape::data()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickShape.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickShape::data()': gives a type "
        "Python has no way to take yet.")
