"""
QGraphicsItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qgraphicsitem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGraphicsItemPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QGraphicsItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QPointF, QRectF, QVariant
  from ..QtGui import QRegion, QTransform
  from . import QGraphicsItemCache, QGraphicsTransform
  from . import QStyleOptionGraphicsItem, QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QGraphicsTransform = WAIT['QGraphicsTransform']
  QPointF = WAIT['QPointF']
  QRectF = WAIT['QRectF']
  QRegion = WAIT['QRegion']
  QStyleOptionGraphicsItem = WAIT['QStyleOptionGraphicsItem']
  QTransform = WAIT['QTransform']
  QVariant = WAIT['QVariant']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGraphicsItemPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGraphicsItemPrivate: a plain Python object standing
  in front of one C++ QGraphicsItemPrivate.

  C++ hands a QGraphicsItemPrivate around as a copy, so every C++
  QGraphicsItemPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGraphicsItemPrivate that has a ritual and that
  Python can call so far, 75 names in all: 'q_func', 'get',
  'updateChildWithGraphicsEffectFlagRecursively', 'updateAncestorFlag',
  'updateAncestorFlags', 'setIsMemberOfGroup', 'remapItemPos',
  'genericMapFromSceneTransform', 'genericMapFromScene',
  'itemIsUntransformable', 'combineTransformToParent',
  'combineTransformFromParent', 'updateSceneTransformFromParent',
  'movableAncestorIsSelected', 'setPosHelper', 'setTransformHelper',
  'prependGraphicsTransform', 'appendGraphicsTransform', 'setVisibleHelper',
  'setEnabledHelper', 'discardUpdateRequest', 'transformChanged', 'depth',
  'invalidateParentGraphicsEffectsRecursively',
  'invalidateChildGraphicsEffectsRecursively', 'invalidateDepthRecursively',
  'resolveDepth', 'addChild', 'removeChild', 'setParentItemHelper',
  'childrenBoundingRectHelper', 'initStyleOption', 'effectiveBoundingRect',
  'sceneEffectiveBoundingRect', 'resolveFont', 'resolvePalette',
  'isProxyWidget', 'extra', 'setExtra', 'unsetExtra', 'maybeExtraItemCache',
  'extraItemCache', 'removeExtraItemCache', 'updatePaintedViewBoundingRects',
  'ensureSceneTransform', 'hasTranslateOnlySceneTransform',
  'invalidateChildrenSceneTransform', 'calcEffectiveOpacity',
  'isOpacityNull', 'isFullyTransparent', 'effectiveOpacity',
  'combineOpacityFromParent', 'childrenCombineOpacity',
  'childrenClippedToShape', 'isInvisible', 'markParentDirty',
  'setFocusHelper', 'clearFocusHelper', 'setSubFocus', 'clearSubFocus',
  'resetFocusProxy', 'subFocusItemChange', 'focusScopeItemChange',
  'transformToParent', 'ensureSortedChildren', 'insertionOrder',
  'ensureSequentialSiblingIndex', 'sendScenePosChange', 'siblingOrderChange',
  'width', 'setWidth', 'resetWidth', 'height', 'setHeight', 'resetHeight'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGraphicsItem *QGraphicsItemPrivate::q_func() const': takes
    in Python what 'QGraphicsItem *QGraphicsItemPrivate::q_func()' takes.
  - Qt's 'QGraphicsItemPrivate::~QGraphicsItemPrivate()': the destructor:
    Python removes its C++ QGraphicsItemPrivate by it, and has no other use
    for it.
  - Qt's 'QGraphicsItemPrivate *QGraphicsItemPrivate::get(QGraphicsItem
    *item)': takes in Python what 'const QGraphicsItemPrivate
    *QGraphicsItemPrivate::get(const QGraphicsItem *item)' takes.
  - Qt's 'void
    QGraphicsItemPrivate::ensureSceneTransformRecursive(QGraphicsItem
    **topMostDirtyItem)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGraphicsItemPrivate is created at the first use, not by
    'QGraphicsItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGraphicsItemPrivate back gives a copy the ritual
    made for Python, in a new cute QGraphicsItemPrivate.
  - Each name of Qt's QGraphicsItemPrivate that has no cute function yet,
    'ensureSceneTransformRecursive', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGraphicsItemPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class AncestorFlag(CuteNum):
    """
    The enum 'QGraphicsItemPrivate::AncestorFlag' of Qt, with the 6 names Qt
    gives in it.
    """

    NoFlag = Kee[int](0)
    AncestorHandlesChildEvents = Kee[int](1)
    AncestorClipsChildren = Kee[int](2)
    AncestorIgnoresTransformations = Kee[int](4)
    AncestorFiltersChildEvents = Kee[int](8)
    AncestorContainsChildren = Kee[int](16)

  class Extra(CuteNum):
    """
    The enum 'QGraphicsItemPrivate::Extra' of Qt, with the 5 names Qt gives
    in it.
    """

    ExtraToolTip = Kee[int](0)
    ExtraCursor = Kee[int](1)
    ExtraCacheData = Kee[int](2)
    ExtraMaxDeviceCoordCacheSize = Kee[int](3)
    ExtraBoundingRegionGranularity = Kee[int](4)

  class InvalidateReason(CuteNum):
    """
    The enum 'QGraphicsItemPrivate::InvalidateReason' of Qt, with the 1 names
    Qt gives in it.
    """

    OpacityChanged = Kee[int](0)

  #  The classes Qt writes inside QGraphicsItemPrivate, each a class in here
  #  as in C++.

  class ExtraStruct(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGraphicsItemPrivate::ExtraStruct: a plain Python
    object standing in front of one C++ QGraphicsItemPrivate::ExtraStruct.

    C++ hands a QGraphicsItemPrivate::ExtraStruct around as a copy, so every
    C++ QGraphicsItemPrivate::ExtraStruct behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QGraphicsItemPrivate::ExtraStruct yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGraphicsItemPrivate::ExtraStruct::ExtraStruct(Extra type, const
      QVariant &value)': names the enum 'QGraphicsItemPrivate::Extra', whose
      class cannot be named here.
    - Qt's 'bool QGraphicsItemPrivate::ExtraStruct::operator<(Extra extra)
      const': names the enum 'QGraphicsItemPrivate::Extra', whose class
      cannot be named here.
    - Qt's 'QGraphicsItemPrivate::ExtraStruct::~ExtraStruct()': the
      destructor: Python removes its C++ QGraphicsItemPrivate::ExtraStruct by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QGraphicsItemPrivate::ExtraStruct is created at the first use,
      not by 'QGraphicsItemPrivate::ExtraStruct(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGraphicsItemPrivate::ExtraStruct back gives a copy
      the ritual made for Python, in a new cute
      QGraphicsItemPrivate::ExtraStruct.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGraphicsItemPrivate::ExtraStruct'

    #  Qt's '~QGraphicsItemPrivate::ExtraStruct()'. Naming it makes this a
    #  value class: Python owns every C++ QGraphicsItemPrivate::ExtraStruct
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN20QGraphicsItemPrivate11ExtraStructD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QGraphicsItemPrivate::ExtraStruct::ExtraStruct()', which is called at
      the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qgraphicsitemprivate-extrastruct.html
      """
      #  QGraphicsItemPrivate::ExtraStruct::ExtraStruct()
      self._noteCreation(
          QGraphicsItemPrivate.ExtraStruct, lambda: Rituals.call(
              'ritual_ZN20QGraphicsItemPrivate11ExtraStructC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class TransformData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QGraphicsItemPrivate::TransformData: a plain Python
    object standing in front of one C++ QGraphicsItemPrivate::TransformData.

    C++ hands a QGraphicsItemPrivate::TransformData around as a copy, so
    every C++ QGraphicsItemPrivate::TransformData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QGraphicsItemPrivate::TransformData that has a
    ritual and that Python can call so far, 1 name in all:
    'computedFullTransform'. It can be made from Python, in 1 way; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QGraphicsItemPrivate::TransformData::~TransformData()': the
      destructor: Python removes its C++ QGraphicsItemPrivate::TransformData
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QGraphicsItemPrivate::TransformData is created at the first
      use, not by 'QGraphicsItemPrivate::TransformData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QGraphicsItemPrivate::TransformData back gives a
      copy the ritual made for Python, in a new cute
      QGraphicsItemPrivate::TransformData.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QTransform = WAIT['QTransform']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QGraphicsItemPrivate::TransformData'

    #  Qt's '~QGraphicsItemPrivate::TransformData()'. Naming it makes this a
    #  value class: Python owns every C++ QGraphicsItemPrivate::TransformData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN20QGraphicsItemPrivate13TransformDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    @overload(QTransform)
    @overload(NoneType)
    def computedFullTransform(
        self,
        postmultiplyTransform: Optional[QTransform] = None,
    ) -> QTransform:
      """
      Calls Qt's 'QTransform
      QGraphicsItemPrivate::TransformData::computedFullTransform(QTransform
      *postmultiplyTransform) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qgraphicsitemprivate-transformdata.html

      Parameters
      ----------

      postmultiplyTransform : Optional[QTransform]
        Passed on as the address of its C++ object. None is passed on as no
        object. May be left out, as in Qt: it is then None.

      Returns
      -------

      QTransform
        A new cute QTransform around the copy Qt gave back. Python owns it.
      """
      #  QTransform
      #      QGraphicsItemPrivate::TransformData::computedFullTransform(
      #      QTransform *postmultiplyTransform) const
      address = self.uglySide.call(
          'ritual_ZNK20QGraphicsItemPrivate13TransformData21computedFullTra'
          'nsformEP10QTransform',
          self._addressOf(postmultiplyTransform),
      )
      from ..QtGui import QTransform
      return QTransform._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QGraphicsItemPrivate::TransformData::TransformData()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qgraphicsitemprivate-transformdata.html
      """
      #  QGraphicsItemPrivate::TransformData::TransformData()
      self._noteCreation(
          QGraphicsItemPrivate.TransformData, lambda: Rituals.call(
              'ritual_ZN20QGraphicsItemPrivate13TransformDataC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGraphicsItem)
  @overload(NoneType)
  def get(item: Optional[QGraphicsItem]) -> Optional[QGraphicsItemPrivate]:
    """
    Calls Qt's 'const QGraphicsItemPrivate *QGraphicsItemPrivate::get(const
    QGraphicsItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemprivate.html#get

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGraphicsItemPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QGraphicsItemPrivate *QGraphicsItemPrivate::get(const
    #      QGraphicsItem *item)
    address = Rituals.call(
        'ritual_ZN20QGraphicsItemPrivate3getEPK13QGraphicsItem',
        CuteMixin._addressOf(item, 'QGraphicsItem'),
    )
    return QGraphicsItemPrivate._cuteAt(address)

  @staticmethod
  @overload(QGraphicsItem)
  @overload(NoneType)
  def movableAncestorIsSelected(item: Optional[QGraphicsItem]) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemPrivate::movableAncestorIsSelected(const
    QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html

    Parameters
    ----------

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsItemPrivate::movableAncestorIsSelected(const
    #      QGraphicsItem *item)
    return Rituals.call(
        'ritual_ZN20QGraphicsItemPrivate25movableAncestorIsSelectedEPK13QGr'
        'aphicsItem',
        CuteMixin._addressOf(item, 'QGraphicsItem'),
    )

  @staticmethod
  @overload(QGraphicsItem, QGraphicsItem)
  @overload(QGraphicsItem, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def insertionOrder(
      a: Optional[QGraphicsItem],
      b: Optional[QGraphicsItem],
  ) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemPrivate::insertionOrder(QGraphicsItem *a,
    QGraphicsItem *b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#insertionOrder

    Parameters
    ----------

    a : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    b : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QGraphicsItemPrivate::insertionOrder(QGraphicsItem *a,
    #      QGraphicsItem *b)
    return Rituals.call(
        'ritual_ZN20QGraphicsItemPrivate14insertionOrderEP13QGraphicsItemS1'
        '_',
        CuteMixin._addressOf(a, 'QGraphicsItem'), CuteMixin._addressOf(b,
        'QGraphicsItem'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGraphicsItemPrivate'

  #  A C++ QGraphicsItemPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGraphicsItemPrivate'

  #  The functions Qt calls itself that QGraphicsItemPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateSceneTransformFromParent': (
          ('_ZN20QGraphicsItemPrivate30updateSceneTransformFromParentEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setPosHelper': (
          ('_ZN20QGraphicsItemPrivate12setPosHelperERK7QPointF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPointF'),
           )),
      ),
      'transformChanged': (
          ('_ZN20QGraphicsItemPrivate16transformChangedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resolveFont': (
          ('_ZN20QGraphicsItemPrivate11resolveFontEj',
           ('nothing', 'nothing', ''),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'resolvePalette': (
          ('_ZN20QGraphicsItemPrivate14resolvePaletteEj',
           ('nothing', 'nothing', ''),
           (
               ('unsigned int', 'number', ''),
           )),
      ),
      'isProxyWidget': (
          ('_ZNK20QGraphicsItemPrivate13isProxyWidgetEv',
           ('bool', 'number', ''),
           ()),
      ),
      'subFocusItemChange': (
          ('_ZN20QGraphicsItemPrivate18subFocusItemChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'focusScopeItemChange': (
          ('_ZN20QGraphicsItemPrivate20focusScopeItemChangeEb',
           ('nothing', 'nothing', ''),
           (
               ('bool', 'number', ''),
           )),
      ),
      'siblingOrderChange': (
          ('_ZN20QGraphicsItemPrivate18siblingOrderChangeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'width': (
          ('_ZNK20QGraphicsItemPrivate5widthEv',
           ('double', 'number', ''),
           ()),
      ),
      'setWidth': (
          ('_ZN20QGraphicsItemPrivate8setWidthEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'resetWidth': (
          ('_ZN20QGraphicsItemPrivate10resetWidthEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'height': (
          ('_ZNK20QGraphicsItemPrivate6heightEv',
           ('double', 'number', ''),
           ()),
      ),
      'setHeight': (
          ('_ZN20QGraphicsItemPrivate9setHeightEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'resetHeight': (
          ('_ZN20QGraphicsItemPrivate11resetHeightEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Qt's '~QGraphicsItemPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QGraphicsItemPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QGraphicsItemPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  def genericMapFromSceneTransform(
      self,
      viewport: Optional[QWidget] = None,
  ) -> QTransform:
    """
    Calls Qt's 'QTransform
    QGraphicsItemPrivate::genericMapFromSceneTransform(const QWidget
    *viewport) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html

    Parameters
    ----------

    viewport : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QGraphicsItemPrivate::genericMapFromSceneTransform(const
    #      QWidget *viewport) const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate28genericMapFromSceneTransformEPK7'
        'QWidget',
        self._addressOf(viewport),
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  @overload(QPointF, QWidget)
  @overload(QPointF, NoneType)
  def genericMapFromScene(
      self,
      pos: QPointF,
      viewport: Optional[QWidget],
  ) -> QPointF:
    """
    Calls Qt's 'QPointF QGraphicsItemPrivate::genericMapFromScene(const
    QPointF &pos, const QWidget *viewport) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#genericMapFromScene

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    viewport : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QGraphicsItemPrivate::genericMapFromScene(const QPointF &pos,
    #      const QWidget *viewport) const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate19genericMapFromSceneERK7QPointFPK'
        '7QWidget',
        self._valueOf(pos, 'QPointF'), self._addressOf(viewport),
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def itemIsUntransformable(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemPrivate::itemIsUntransformable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#itemIsUntransformable
    """
    #  bool QGraphicsItemPrivate::itemIsUntransformable() const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate21itemIsUntransformableEv',
    )

  @overload()
  @overload(bool)
  @overload(bool, bool)
  @overload(bool, bool, bool)
  def discardUpdateRequest(
      self,
      ignoreVisibleBit: bool = False,
      ignoreDirtyBit: bool = False,
      ignoreOpacity: bool = False,
  ) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemPrivate::discardUpdateRequest(bool
    ignoreVisibleBit, bool ignoreDirtyBit, bool ignoreOpacity) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#discardUpdateRequest

    Parameters
    ----------

    ignoreVisibleBit : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    ignoreDirtyBit : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    ignoreOpacity : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  bool QGraphicsItemPrivate::discardUpdateRequest(bool ignoreVisibleBit,
    #      bool ignoreDirtyBit, bool ignoreOpacity) const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate20discardUpdateRequestEbbb',
        ignoreVisibleBit, ignoreDirtyBit, ignoreOpacity,
    )

  def depth(self) -> int:
    """
    Calls Qt's 'int QGraphicsItemPrivate::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemprivate.html#depth
    """
    #  int QGraphicsItemPrivate::depth() const
    return self.uglySide.call('ritual_ZNK20QGraphicsItemPrivate5depthEv')

  @overload()
  @overload(QGraphicsItem)
  @overload(NoneType)
  def effectiveBoundingRect(
      self,
      topMostEffectItem: Optional[QGraphicsItem] = None,
  ) -> QRectF:
    """
    Calls Qt's 'QRectF
    QGraphicsItemPrivate::effectiveBoundingRect(QGraphicsItem
    *topMostEffectItem) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#effectiveBoundingRect

    Parameters
    ----------

    topMostEffectItem : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItemPrivate::effectiveBoundingRect(QGraphicsItem
    #      *topMostEffectItem) const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate21effectiveBoundingRectEP13QGraphi'
        'csItem',
        self._addressOf(topMostEffectItem, 'QGraphicsItem'),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  @overload(QRectF)
  def effectiveBoundingRect(self, rect: QRectF) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItemPrivate::effectiveBoundingRect(const
    QRectF &rect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#effectiveBoundingRect

    Parameters
    ----------

    rect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItemPrivate::effectiveBoundingRect(const QRectF &rect)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate21effectiveBoundingRectERK6QRectF',
        self._valueOf(rect),
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def sceneEffectiveBoundingRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGraphicsItemPrivate::sceneEffectiveBoundingRect()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGraphicsItemPrivate::sceneEffectiveBoundingRect() const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate26sceneEffectiveBoundingRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def isProxyWidget(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemPrivate::isProxyWidget() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#isProxyWidget
    """
    #  bool QGraphicsItemPrivate::isProxyWidget() const
    ritual = 'ritual_ZNK20QGraphicsItemPrivate13isProxyWidgetEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QGraphicsItemPrivate13isProxyWidgetEv'
    return self.uglySide.call(ritual)

  @overload(Extra)
  def extra(self, type: Extra) -> QVariant:
    """
    Calls Qt's 'QVariant QGraphicsItemPrivate::extra(Extra type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemprivate.html#extra

    Parameters
    ----------

    type : Extra
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QGraphicsItemPrivate::extra(Extra type) const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate5extraENS_5ExtraE', type.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def maybeExtraItemCache(self) -> Optional[QGraphicsItemCache]:
    """
    Calls Qt's 'QGraphicsItemCache
    *QGraphicsItemPrivate::maybeExtraItemCache() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#maybeExtraItemCache

    Returns
    -------

    Optional[QGraphicsItemCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItemCache *QGraphicsItemPrivate::maybeExtraItemCache() const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate19maybeExtraItemCacheEv',
    )
    from . import QGraphicsItemCache
    return QGraphicsItemCache._cuteAt(address)

  def extraItemCache(self) -> Optional[QGraphicsItemCache]:
    """
    Calls Qt's 'QGraphicsItemCache *QGraphicsItemPrivate::extraItemCache()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#extraItemCache

    Returns
    -------

    Optional[QGraphicsItemCache]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItemCache *QGraphicsItemPrivate::extraItemCache() const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate14extraItemCacheEv',
    )
    from . import QGraphicsItemCache
    return QGraphicsItemCache._cuteAt(address)

  def calcEffectiveOpacity(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsItemPrivate::calcEffectiveOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#calcEffectiveOpacity
    """
    #  qreal QGraphicsItemPrivate::calcEffectiveOpacity() const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate20calcEffectiveOpacityEv',
    )

  @overload()
  def isOpacityNull(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemPrivate::isOpacityNull() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#isOpacityNull
    """
    #  bool QGraphicsItemPrivate::isOpacityNull() const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate13isOpacityNullEv',
    )

  @staticmethod
  @overload(float)
  def isOpacityNull(opacity: float) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemPrivate::isOpacityNull(qreal opacity)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#isOpacityNull

    Parameters
    ----------

    opacity : float
      Passed on as it is.
    """
    #  bool QGraphicsItemPrivate::isOpacityNull(qreal opacity)
    return Rituals.call(
        'ritual_ZN20QGraphicsItemPrivate13isOpacityNullEd', opacity,
    )

  def isFullyTransparent(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemPrivate::isFullyTransparent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#isFullyTransparent
    """
    #  bool QGraphicsItemPrivate::isFullyTransparent() const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate18isFullyTransparentEv',
    )

  def effectiveOpacity(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsItemPrivate::effectiveOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#effectiveOpacity
    """
    #  qreal QGraphicsItemPrivate::effectiveOpacity() const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate16effectiveOpacityEv',
    )

  @overload(float)
  def combineOpacityFromParent(self, parentOpacity: float) -> float:
    """
    Calls Qt's 'qreal QGraphicsItemPrivate::combineOpacityFromParent(qreal
    parentOpacity) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#combineOpacityFromParent

    Parameters
    ----------

    parentOpacity : float
      Passed on as it is.
    """
    #  qreal QGraphicsItemPrivate::combineOpacityFromParent(qreal
    #      parentOpacity) const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate24combineOpacityFromParentEd',
        parentOpacity,
    )

  def childrenCombineOpacity(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemPrivate::childrenCombineOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#childrenCombineOpacity
    """
    #  bool QGraphicsItemPrivate::childrenCombineOpacity() const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate22childrenCombineOpacityEv',
    )

  def childrenClippedToShape(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemPrivate::childrenClippedToShape() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#childrenClippedToShape
    """
    #  bool QGraphicsItemPrivate::childrenClippedToShape() const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate22childrenClippedToShapeEv',
    )

  def isInvisible(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemPrivate::isInvisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#isInvisible
    """
    #  bool QGraphicsItemPrivate::isInvisible() const
    return self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate11isInvisibleEv',
    )

  def transformToParent(self) -> QTransform:
    """
    Calls Qt's 'QTransform QGraphicsItemPrivate::transformToParent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#transformToParent

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QGraphicsItemPrivate::transformToParent() const
    address = self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate17transformToParentEv',
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  def width(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsItemPrivate::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemprivate.html#width
    """
    #  qreal QGraphicsItemPrivate::width() const
    ritual = 'ritual_ZNK20QGraphicsItemPrivate5widthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QGraphicsItemPrivate5widthEv'
    return self.uglySide.call(ritual)

  def height(self) -> float:
    """
    Calls Qt's 'qreal QGraphicsItemPrivate::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemprivate.html#height
    """
    #  qreal QGraphicsItemPrivate::height() const
    ritual = 'ritual_ZNK20QGraphicsItemPrivate6heightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QGraphicsItemPrivate6heightEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setIsMemberOfGroup(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::setIsMemberOfGroup(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#setIsMemberOfGroup

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QGraphicsItemPrivate::setIsMemberOfGroup(bool enabled)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate18setIsMemberOfGroupEb', enabled,
    )

  @overload(QPointF)
  def setPosHelper(self, pos: QPointF) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::setPosHelper(const QPointF &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#setPosHelper

    Parameters
    ----------

    pos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QGraphicsItemPrivate::setPosHelper(const QPointF &pos)
    ritual = 'ritual_ZN20QGraphicsItemPrivate12setPosHelperERK7QPointF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QGraphicsItemPrivate12setPosHelperERK7QPointF'
    self.uglySide.call(ritual, self._valueOf(pos, 'QPointF'))

  @overload(QTransform)
  def setTransformHelper(self, transform: QTransform) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::setTransformHelper(const
    QTransform &transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#setTransformHelper

    Parameters
    ----------

    transform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.
    """
    #  void QGraphicsItemPrivate::setTransformHelper(const QTransform
    #      &transform)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate18setTransformHelperERK10QTransform',
        self._valueOf(transform),
    )

  @overload(bool, bool)
  @overload(bool, bool, bool)
  @overload(bool, bool, bool, bool)
  def setVisibleHelper(
      self,
      newVisible: bool,
      explicitly: bool,
      update: bool = True,
      hiddenByPanel: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::setVisibleHelper(bool newVisible,
    bool explicitly, bool update, bool hiddenByPanel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#setVisibleHelper

    Parameters
    ----------

    newVisible : bool
      Passed on as it is.

    explicitly : bool
      Passed on as it is.

    update : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    hiddenByPanel : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QGraphicsItemPrivate::setVisibleHelper(bool newVisible, bool
    #      explicitly, bool update, bool hiddenByPanel)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate16setVisibleHelperEbbbb',
        newVisible, explicitly, update, hiddenByPanel,
    )

  @overload(bool, bool)
  @overload(bool, bool, bool)
  def setEnabledHelper(
      self,
      newEnabled: bool,
      explicitly: bool,
      update: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::setEnabledHelper(bool newEnabled,
    bool explicitly, bool update)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#setEnabledHelper

    Parameters
    ----------

    newEnabled : bool
      Passed on as it is.

    explicitly : bool
      Passed on as it is.

    update : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QGraphicsItemPrivate::setEnabledHelper(bool newEnabled, bool
    #      explicitly, bool update)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate16setEnabledHelperEbbb',
        newEnabled, explicitly, update,
    )

  @overload(QGraphicsItem, QVariant, QVariant)
  @overload(QGraphicsItem, QVariant, NoneType)
  @overload(QGraphicsItem, NoneType, QVariant)
  @overload(QGraphicsItem, NoneType, NoneType)
  @overload(NoneType, QVariant, QVariant)
  @overload(NoneType, QVariant, NoneType)
  @overload(NoneType, NoneType, QVariant)
  @overload(NoneType, NoneType, NoneType)
  def setParentItemHelper(
      self,
      parent: Optional[QGraphicsItem],
      newParentVariant: Optional[QVariant],
      thisPointerVariant: Optional[QVariant],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::setParentItemHelper(QGraphicsItem
    *parent, const QVariant *newParentVariant, const QVariant
    *thisPointerVariant)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#setParentItemHelper

    Parameters
    ----------

    parent : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    newParentVariant : Optional[QVariant]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisPointerVariant : Optional[QVariant]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItemPrivate::setParentItemHelper(QGraphicsItem *parent,
    #      const QVariant *newParentVariant, const QVariant
    #      *thisPointerVariant)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate19setParentItemHelperEP13QGraphicsI'
        'temPK8QVariantS4_',
        self._addressOf(parent, 'QGraphicsItem'),
        self._addressOf(newParentVariant),
        self._addressOf(thisPointerVariant),
    )

  @overload(Extra, QVariant)
  def setExtra(self, type: Extra, value: QVariant) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::setExtra(Extra type, const
    QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemprivate.html#setExtra

    Parameters
    ----------

    type : Extra
      Passed on as its number.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QGraphicsItemPrivate::setExtra(Extra type, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate8setExtraENS_5ExtraERK8QVariant',
        type.value, self._valueOf(value),
    )

  @overload(Qt.FocusReason, bool, bool)
  def setFocusHelper(
      self,
      focusReason: Qt.FocusReason,
      climb: bool,
      focusFromHide: bool,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::setFocusHelper(Qt::FocusReason
    focusReason, bool climb, bool focusFromHide)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#setFocusHelper

    Parameters
    ----------

    focusReason : Qt.FocusReason
      Passed on as its number.

    climb : bool
      Passed on as it is.

    focusFromHide : bool
      Passed on as it is.
    """
    #  void QGraphicsItemPrivate::setFocusHelper(Qt::FocusReason focusReason,
    #      bool climb, bool focusFromHide)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate14setFocusHelperEN2Qt11FocusReasonE'
        'bb',
        focusReason.value, climb, focusFromHide,
    )

  @overload()
  @overload(QGraphicsItem)
  @overload(NoneType)
  @overload(QGraphicsItem, QGraphicsItem)
  @overload(QGraphicsItem, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def setSubFocus(
      self,
      rootItem: Optional[QGraphicsItem] = None,
      stopItem: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::setSubFocus(QGraphicsItem
    *rootItem, QGraphicsItem *stopItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#setSubFocus

    Parameters
    ----------

    rootItem : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    stopItem : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QGraphicsItemPrivate::setSubFocus(QGraphicsItem *rootItem,
    #      QGraphicsItem *stopItem)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate11setSubFocusEP13QGraphicsItemS1_',
        self._addressOf(rootItem, 'QGraphicsItem'), self._addressOf(stopItem,
        'QGraphicsItem'),
    )

  @overload(float)
  def setWidth(self, a0: float) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::setWidth(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemprivate.html#setWidth

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QGraphicsItemPrivate::setWidth(qreal a0)
    ritual = 'ritual_ZN20QGraphicsItemPrivate8setWidthEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QGraphicsItemPrivate8setWidthEd'
    self.uglySide.call(ritual, a0)

  @overload(float)
  def setHeight(self, a0: float) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::setHeight(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#setHeight

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QGraphicsItemPrivate::setHeight(qreal a0)
    ritual = 'ritual_ZN20QGraphicsItemPrivate9setHeightEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QGraphicsItemPrivate9setHeightEd'
    self.uglySide.call(ritual, a0)

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
    'QGraphicsItemPrivate::QGraphicsItemPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#QGraphicsItemPrivate
    """
    #  QGraphicsItemPrivate::QGraphicsItemPrivate()
    self._noteCreation(QGraphicsItemPrivate, lambda: Rituals.call(
        'ritual_ZN20QGraphicsItemPrivateC1Ev',
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

  def q_func(self) -> Optional[QGraphicsItem]:
    """
    Calls Qt's 'QGraphicsItem *QGraphicsItemPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemprivate.html#q_func

    Returns
    -------

    Optional[QGraphicsItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGraphicsItem *QGraphicsItemPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QGraphicsItemPrivate6q_funcEv')
    return QGraphicsItem._cuteAt(address)

  def updateChildWithGraphicsEffectFlagRecursively(self) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemPrivate::updateChildWithGraphicsEffectFlagRecursively()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html
    """
    #  void QGraphicsItemPrivate::
    #      updateChildWithGraphicsEffectFlagRecursively()
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate44updateChildWithGraphicsEffectFlag'
        'RecursivelyEv',
    )

  @overload(QGraphicsItem.GraphicsItemFlag)
  @overload(QGraphicsItem.GraphicsItemFlag, AncestorFlag)
  @overload(QGraphicsItem.GraphicsItemFlag, AncestorFlag, bool)
  @overload(QGraphicsItem.GraphicsItemFlag, AncestorFlag, bool, bool)
  def updateAncestorFlag(
      self,
      childFlag: QGraphicsItem.GraphicsItemFlag,
      flag: AncestorFlag = AncestorFlag.NoFlag,
      enabled: bool = False,
      root: bool = True,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemPrivate::updateAncestorFlag(QGraphicsItem::GraphicsItemFlag
    childFlag, AncestorFlag flag, bool enabled, bool root)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#updateAncestorFlag

    Parameters
    ----------

    childFlag : QGraphicsItem.GraphicsItemFlag
      Passed on as its number.

    flag : AncestorFlag
      Passed on as its number. May be left out, as in Qt: it is then
      AncestorFlag.NoFlag.

    enabled : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    root : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QGraphicsItemPrivate::updateAncestorFlag(QGraphicsItem::
    #      GraphicsItemFlag childFlag, AncestorFlag flag, bool enabled, bool
    #      root)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate18updateAncestorFlagEN13QGraphicsIt'
        'em16GraphicsItemFlagENS_12AncestorFlagEbb',
        childFlag.value, flag.value, enabled, root,
    )

  def updateAncestorFlags(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::updateAncestorFlags()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#updateAncestorFlags
    """
    #  void QGraphicsItemPrivate::updateAncestorFlags()
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate19updateAncestorFlagsEv',
    )

  @overload(QEvent, QGraphicsItem)
  @overload(QEvent, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def remapItemPos(
      self,
      event: Optional[QEvent],
      item: Optional[QGraphicsItem],
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::remapItemPos(QEvent *event,
    QGraphicsItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#remapItemPos

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItemPrivate::remapItemPos(QEvent *event, QGraphicsItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate12remapItemPosEP6QEventP13QGraphics'
        'Item',
        self._addressOf(event), self._addressOf(item, 'QGraphicsItem'),
    )

  @overload(QTransform)
  @overload(NoneType)
  @overload(QTransform, QTransform)
  @overload(QTransform, NoneType)
  @overload(NoneType, QTransform)
  @overload(NoneType, NoneType)
  def combineTransformToParent(
      self,
      x: Optional[QTransform],
      viewTransform: Optional[QTransform] = None,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemPrivate::combineTransformToParent(QTransform *x, const
    QTransform *viewTransform) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#combineTransformToParent

    Parameters
    ----------

    x : Optional[QTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewTransform : Optional[QTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QGraphicsItemPrivate::combineTransformToParent(QTransform *x,
    #      const QTransform *viewTransform) const
    self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate24combineTransformToParentEP10QTra'
        'nsformPKS0_',
        self._addressOf(x), self._addressOf(viewTransform),
    )

  @overload(QTransform)
  @overload(NoneType)
  @overload(QTransform, QTransform)
  @overload(QTransform, NoneType)
  @overload(NoneType, QTransform)
  @overload(NoneType, NoneType)
  def combineTransformFromParent(
      self,
      x: Optional[QTransform],
      viewTransform: Optional[QTransform] = None,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemPrivate::combineTransformFromParent(QTransform *x, const
    QTransform *viewTransform) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html

    Parameters
    ----------

    x : Optional[QTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    viewTransform : Optional[QTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QGraphicsItemPrivate::combineTransformFromParent(QTransform *x,
    #      const QTransform *viewTransform) const
    self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate26combineTransformFromParentEP10QT'
        'ransformPKS0_',
        self._addressOf(x), self._addressOf(viewTransform),
    )

  def updateSceneTransformFromParent(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::updateSceneTransformFromParent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html
    """
    #  void QGraphicsItemPrivate::updateSceneTransformFromParent()
    ritual = (
        'ritual_ZN20QGraphicsItemPrivate30updateSceneTransformFromParentEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QGraphicsItemPrivate30updateSceneTransformFromPar'
          'entEv')
    self.uglySide.call(ritual)

  @overload(QGraphicsTransform)
  @overload(NoneType)
  def prependGraphicsTransform(
      self,
      t: Optional[QGraphicsTransform],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemPrivate::prependGraphicsTransform(QGraphicsTransform *t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#prependGraphicsTransform

    Parameters
    ----------

    t : Optional[QGraphicsTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItemPrivate::prependGraphicsTransform(QGraphicsTransform
    #      *t)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate24prependGraphicsTransformEP18QGrap'
        'hicsTransform',
        self._addressOf(t),
    )

  @overload(QGraphicsTransform)
  @overload(NoneType)
  def appendGraphicsTransform(self, t: Optional[QGraphicsTransform]) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemPrivate::appendGraphicsTransform(QGraphicsTransform *t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#appendGraphicsTransform

    Parameters
    ----------

    t : Optional[QGraphicsTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItemPrivate::appendGraphicsTransform(QGraphicsTransform
    #      *t)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate23appendGraphicsTransformEP18QGraph'
        'icsTransform',
        self._addressOf(t),
    )

  def transformChanged(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::transformChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#transformChanged
    """
    #  void QGraphicsItemPrivate::transformChanged()
    ritual = 'ritual_ZN20QGraphicsItemPrivate16transformChangedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QGraphicsItemPrivate16transformChangedEv'
    self.uglySide.call(ritual)

  def invalidateParentGraphicsEffectsRecursively(self) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemPrivate::invalidateParentGraphicsEffectsRecursively()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html
    """
    #  void
    #      QGraphicsItemPrivate::invalidateParentGraphicsEffectsRecursively()
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate42invalidateParentGraphicsEffectsRe'
        'cursivelyEv',
    )

  @overload(InvalidateReason)
  def invalidateChildGraphicsEffectsRecursively(
      self,
      reason: InvalidateReason,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemPrivate::invalidateChildGraphicsEffectsRecursively(
    InvalidateReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html

    Parameters
    ----------

    reason : InvalidateReason
      Passed on as its number.
    """
    #  void QGraphicsItemPrivate::invalidateChildGraphicsEffectsRecursively(
    #      InvalidateReason reason)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate41invalidateChildGraphicsEffectsRec'
        'ursivelyENS_16InvalidateReasonE',
        reason.value,
    )

  def invalidateDepthRecursively(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::invalidateDepthRecursively()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html
    """
    #  void QGraphicsItemPrivate::invalidateDepthRecursively()
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate26invalidateDepthRecursivelyEv',
    )

  def resolveDepth(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::resolveDepth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#resolveDepth
    """
    #  void QGraphicsItemPrivate::resolveDepth()
    self.uglySide.call('ritual_ZN20QGraphicsItemPrivate12resolveDepthEv')

  @overload(QGraphicsItem)
  @overload(NoneType)
  def addChild(self, child: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::addChild(QGraphicsItem *child)'.

    Qt's own words: https://doc.qt.io/qt-6/qgraphicsitemprivate.html#addChild

    Parameters
    ----------

    child : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItemPrivate::addChild(QGraphicsItem *child)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate8addChildEP13QGraphicsItem',
        self._addressOf(child, 'QGraphicsItem'),
    )

  @overload(QGraphicsItem)
  @overload(NoneType)
  def removeChild(self, child: Optional[QGraphicsItem]) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::removeChild(QGraphicsItem
    *child)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#removeChild

    Parameters
    ----------

    child : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItemPrivate::removeChild(QGraphicsItem *child)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate11removeChildEP13QGraphicsItem',
        self._addressOf(child, 'QGraphicsItem'),
    )

  @overload(QTransform, QRectF, QGraphicsItem)
  @overload(QTransform, QRectF, NoneType)
  @overload(QTransform, NoneType, QGraphicsItem)
  @overload(QTransform, NoneType, NoneType)
  @overload(NoneType, QRectF, QGraphicsItem)
  @overload(NoneType, QRectF, NoneType)
  @overload(NoneType, NoneType, QGraphicsItem)
  @overload(NoneType, NoneType, NoneType)
  def childrenBoundingRectHelper(
      self,
      x: Optional[QTransform],
      rect: Optional[QRectF],
      topMostEffectItem: Optional[QGraphicsItem],
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemPrivate::childrenBoundingRectHelper(QTransform *x, QRectF
    *rect, QGraphicsItem *topMostEffectItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html

    Parameters
    ----------

    x : Optional[QTransform]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rect : Optional[QRectF]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    topMostEffectItem : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QGraphicsItemPrivate::childrenBoundingRectHelper(QTransform *x,
    #      QRectF *rect, QGraphicsItem *topMostEffectItem)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate26childrenBoundingRectHelperEP10QTr'
        'ansformP6QRectFP13QGraphicsItem',
        self._addressOf(x), self._addressOf(rect),
        self._addressOf(topMostEffectItem, 'QGraphicsItem'),
    )

  @overload(QStyleOptionGraphicsItem, QTransform, QRegion)
  @overload(NoneType, QTransform, QRegion)
  @overload(QStyleOptionGraphicsItem, QTransform, QRegion, bool)
  @overload(NoneType, QTransform, QRegion, bool)
  def initStyleOption(
      self,
      option: Optional[QStyleOptionGraphicsItem],
      worldTransform: QTransform,
      exposedRegion: QRegion,
      allItems: bool = False,
  ) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemPrivate::initStyleOption(QStyleOptionGraphicsItem *option,
    const QTransform &worldTransform, const QRegion &exposedRegion, bool
    allItems) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    worldTransform : QTransform
      Passed on as a value: Qt reads the C++ QTransform, which stays Python's
      own.

    exposedRegion : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    allItems : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QGraphicsItemPrivate::initStyleOption(QStyleOptionGraphicsItem
    #      *option, const QTransform &worldTransform, const QRegion
    #      &exposedRegion, bool allItems) const
    self.uglySide.call(
        'ritual_ZNK20QGraphicsItemPrivate15initStyleOptionEP24QStyleOptionG'
        'raphicsItemRK10QTransformRK7QRegionb',
        self._addressOf(option), self._valueOf(worldTransform),
        self._valueOf(exposedRegion), allItems,
    )

  @overload(int)
  def resolveFont(self, inheritedMask: int) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::resolveFont(uint inheritedMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#resolveFont

    Parameters
    ----------

    inheritedMask : int
      Passed on as it is.
    """
    #  void QGraphicsItemPrivate::resolveFont(uint inheritedMask)
    ritual = 'ritual_ZN20QGraphicsItemPrivate11resolveFontEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QGraphicsItemPrivate11resolveFontEj'
    self.uglySide.call(ritual, inheritedMask)

  @overload(int)
  def resolvePalette(self, inheritedMask: int) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::resolvePalette(uint
    inheritedMask)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#resolvePalette

    Parameters
    ----------

    inheritedMask : int
      Passed on as it is.
    """
    #  void QGraphicsItemPrivate::resolvePalette(uint inheritedMask)
    ritual = 'ritual_ZN20QGraphicsItemPrivate14resolvePaletteEj'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QGraphicsItemPrivate14resolvePaletteEj'
    self.uglySide.call(ritual, inheritedMask)

  @overload(Extra)
  def unsetExtra(self, type: Extra) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::unsetExtra(Extra type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#unsetExtra

    Parameters
    ----------

    type : Extra
      Passed on as its number.
    """
    #  void QGraphicsItemPrivate::unsetExtra(Extra type)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate10unsetExtraENS_5ExtraE', type.value,
    )

  def removeExtraItemCache(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::removeExtraItemCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#removeExtraItemCache
    """
    #  void QGraphicsItemPrivate::removeExtraItemCache()
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate20removeExtraItemCacheEv',
    )

  @overload(bool)
  def updatePaintedViewBoundingRects(self, updateChildren: bool) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemPrivate::updatePaintedViewBoundingRects(bool
    updateChildren)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html

    Parameters
    ----------

    updateChildren : bool
      Passed on as it is.
    """
    #  void QGraphicsItemPrivate::updatePaintedViewBoundingRects(bool
    #      updateChildren)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate30updatePaintedViewBoundingRectsEb',
        updateChildren,
    )

  def ensureSceneTransform(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::ensureSceneTransform()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#ensureSceneTransform
    """
    #  void QGraphicsItemPrivate::ensureSceneTransform()
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate20ensureSceneTransformEv',
    )

  def hasTranslateOnlySceneTransform(self) -> bool:
    """
    Calls Qt's 'bool QGraphicsItemPrivate::hasTranslateOnlySceneTransform()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html
    """
    #  bool QGraphicsItemPrivate::hasTranslateOnlySceneTransform()
    return self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate30hasTranslateOnlySceneTransformEv',
    )

  def invalidateChildrenSceneTransform(self) -> None:
    """
    Calls Qt's 'void
    QGraphicsItemPrivate::invalidateChildrenSceneTransform()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html
    """
    #  void QGraphicsItemPrivate::invalidateChildrenSceneTransform()
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate32invalidateChildrenSceneTransformE'
        'v',
    )

  @overload()
  @overload(bool)
  def markParentDirty(self, updateBoundingRect: bool = False) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::markParentDirty(bool
    updateBoundingRect)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#markParentDirty

    Parameters
    ----------

    updateBoundingRect : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QGraphicsItemPrivate::markParentDirty(bool updateBoundingRect)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate15markParentDirtyEb',
        updateBoundingRect,
    )

  @overload(bool, bool)
  def clearFocusHelper(
      self,
      giveFocusToParent: bool,
      hiddenByParentPanel: bool,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::clearFocusHelper(bool
    giveFocusToParent, bool hiddenByParentPanel)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#clearFocusHelper

    Parameters
    ----------

    giveFocusToParent : bool
      Passed on as it is.

    hiddenByParentPanel : bool
      Passed on as it is.
    """
    #  void QGraphicsItemPrivate::clearFocusHelper(bool giveFocusToParent,
    #      bool hiddenByParentPanel)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate16clearFocusHelperEbb',
        giveFocusToParent, hiddenByParentPanel,
    )

  @overload()
  @overload(QGraphicsItem)
  @overload(NoneType)
  @overload(QGraphicsItem, QGraphicsItem)
  @overload(QGraphicsItem, NoneType)
  @overload(NoneType, QGraphicsItem)
  @overload(NoneType, NoneType)
  def clearSubFocus(
      self,
      rootItem: Optional[QGraphicsItem] = None,
      stopItem: Optional[QGraphicsItem] = None,
  ) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::clearSubFocus(QGraphicsItem
    *rootItem, QGraphicsItem *stopItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#clearSubFocus

    Parameters
    ----------

    rootItem : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    stopItem : Optional[QGraphicsItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QGraphicsItemPrivate::clearSubFocus(QGraphicsItem *rootItem,
    #      QGraphicsItem *stopItem)
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate13clearSubFocusEP13QGraphicsItemS1_',
        self._addressOf(rootItem, 'QGraphicsItem'), self._addressOf(stopItem,
        'QGraphicsItem'),
    )

  def resetFocusProxy(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::resetFocusProxy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#resetFocusProxy
    """
    #  void QGraphicsItemPrivate::resetFocusProxy()
    self.uglySide.call('ritual_ZN20QGraphicsItemPrivate15resetFocusProxyEv')

  def subFocusItemChange(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::subFocusItemChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#subFocusItemChange
    """
    #  void QGraphicsItemPrivate::subFocusItemChange()
    ritual = 'ritual_ZN20QGraphicsItemPrivate18subFocusItemChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QGraphicsItemPrivate18subFocusItemChangeEv'
    self.uglySide.call(ritual)

  @overload(bool)
  def focusScopeItemChange(self, isSubFocusItem: bool) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::focusScopeItemChange(bool
    isSubFocusItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#focusScopeItemChange

    Parameters
    ----------

    isSubFocusItem : bool
      Passed on as it is.
    """
    #  void QGraphicsItemPrivate::focusScopeItemChange(bool isSubFocusItem)
    ritual = 'ritual_ZN20QGraphicsItemPrivate20focusScopeItemChangeEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QGraphicsItemPrivate20focusScopeItemChangeEb'
    self.uglySide.call(ritual, isSubFocusItem)

  def ensureSortedChildren(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::ensureSortedChildren()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#ensureSortedChildren
    """
    #  void QGraphicsItemPrivate::ensureSortedChildren()
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate20ensureSortedChildrenEv',
    )

  def ensureSequentialSiblingIndex(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::ensureSequentialSiblingIndex()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html
    """
    #  void QGraphicsItemPrivate::ensureSequentialSiblingIndex()
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate28ensureSequentialSiblingIndexEv',
    )

  def sendScenePosChange(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::sendScenePosChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#sendScenePosChange
    """
    #  void QGraphicsItemPrivate::sendScenePosChange()
    self.uglySide.call(
        'ritual_ZN20QGraphicsItemPrivate18sendScenePosChangeEv',
    )

  def siblingOrderChange(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::siblingOrderChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#siblingOrderChange
    """
    #  void QGraphicsItemPrivate::siblingOrderChange()
    ritual = 'ritual_ZN20QGraphicsItemPrivate18siblingOrderChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QGraphicsItemPrivate18siblingOrderChangeEv'
    self.uglySide.call(ritual)

  def resetWidth(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::resetWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#resetWidth
    """
    #  void QGraphicsItemPrivate::resetWidth()
    ritual = 'ritual_ZN20QGraphicsItemPrivate10resetWidthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QGraphicsItemPrivate10resetWidthEv'
    self.uglySide.call(ritual)

  def resetHeight(self) -> None:
    """
    Calls Qt's 'void QGraphicsItemPrivate::resetHeight()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgraphicsitemprivate.html#resetHeight
    """
    #  void QGraphicsItemPrivate::resetHeight()
    ritual = 'ritual_ZN20QGraphicsItemPrivate11resetHeightEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QGraphicsItemPrivate11resetHeightEv'
    self.uglySide.call(ritual)

  @staticmethod
  def ensureSceneTransformRecursive(*__, **_) -> Never:
    """
    Qt's 'void
    QGraphicsItemPrivate::ensureSceneTransformRecursive(QGraphicsItem
    **topMostDirtyItem)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGraphicsItemPrivate.ensureSceneTransformRecursive' has no cute "
        "function yet. Qt's 'void "
        "QGraphicsItemPrivate::ensureSceneTransformRecursive(QGraphicsItem "
        "**topMostDirtyItem)': takes a type Python has no way to hand over "
        "yet.")
