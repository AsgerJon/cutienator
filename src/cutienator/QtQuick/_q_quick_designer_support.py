"""
QQuickDesignerSupport binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdesignersupport_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickDesignerSupport to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject, QRectF, QSize
  from ..QtGui import QImage, QTransform
  from ..QtQml import QQmlContext
  from . import QQuickItem, QQuickView, QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQmlContext = WAIT['QQmlContext']
  QQuickItem = WAIT['QQuickItem']
  QQuickView = WAIT['QQuickView']
  QQuickWindow = WAIT['QQuickWindow']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDesignerSupport(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickDesignerSupport: a plain Python object standing
  in front of one C++ QQuickDesignerSupport.

  C++ hands a QQuickDesignerSupport around as a copy, so every C++
  QQuickDesignerSupport behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickDesignerSupport that has a ritual and that
  Python can call so far, 27 names in all: 'refFromEffectItem',
  'derefFromEffectItem', 'renderImageForItem', 'isDirty', 'addDirty',
  'resetDirty', 'windowTransform', 'parentTransform', 'isAnchoredTo',
  'areChildrenAnchoredTo', 'hasAnchor', 'anchorFillTargetItem',
  'anchorCenterInTargetItem', 'resetAnchor',
  'emitComponentCompleteSignalForAttachedProperty', 'statesForItem',
  'isComponentComplete', 'borderWidth', 'refreshExpressions', 'setRootItem',
  'isValidWidth', 'isValidHeight', 'updateDirtyNode', 'activateDesignerMode',
  'disableComponentComplete', 'enableComponentComplete', 'polishItems'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuickDesignerSupport::~QQuickDesignerSupport()': the destructor:
    Python removes its C++ QQuickDesignerSupport by it, and has no other use
    for it.
  - Qt's 'std::pair<QString, QObject *>
    QQuickDesignerSupport::anchorLineTarget(QQuickItem *item, const QString
    &name, QQmlContext *context)': gives a type Python has no way to take
    yet.

  What to expect
  --------------

  - The C++ QQuickDesignerSupport is created at the first use, not by
    'QQuickDesignerSupport(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickDesignerSupport back gives a copy the ritual
    made for Python, in a new cute QQuickDesignerSupport.
  - Each name of Qt's QQuickDesignerSupport that has no cute function yet,
    'anchorLineTarget', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QQuickDesignerSupport, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class DirtyType(CuteNum):
    """
    The enum 'QQuickDesignerSupport::DirtyType' of Qt, with the 22 names Qt
    gives in it.
    """

    TransformOrigin = Kee[int](1)
    Transform = Kee[int](2)
    BasicTransform = Kee[int](4)
    Position = Kee[int](8)
    Size = Kee[int](16)
    ZValue = Kee[int](32)
    Content = Kee[int](64)
    Smooth = Kee[int](128)
    OpacityValue = Kee[int](256)
    ChildrenChanged = Kee[int](512)
    ChildrenStackingChanged = Kee[int](1024)
    ParentChanged = Kee[int](2048)
    Clip = Kee[int](4096)
    Window = Kee[int](8192)
    EffectReference = Kee[int](32768)
    Visible = Kee[int](65536)
    HideReference = Kee[int](131072)
    TransformUpdateMask = Kee[int](8223)
    ComplexTransformUpdateMask = Kee[int](8194)
    ContentUpdateMask = Kee[int](8400)
    ChildrenUpdateMask = Kee[int](42496)
    AllMask = Kee[int](42719)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickItem, DirtyType)
  @overload(NoneType, DirtyType)
  def isDirty(
      referencedItem: Optional[QQuickItem],
      dirtyType: DirtyType,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupport::isDirty(QQuickItem
    *referencedItem, DirtyType dirtyType)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdesignersupport.html#isDirty

    Parameters
    ----------

    referencedItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dirtyType : DirtyType
      Passed on as its number.
    """
    #  bool QQuickDesignerSupport::isDirty(QQuickItem *referencedItem,
    #      DirtyType dirtyType)
    return Rituals.call(
        'ritual_ZN21QQuickDesignerSupport7isDirtyEP10QQuickItemNS_9DirtyTyp'
        'eE',
        CuteMixin._addressOf(referencedItem), dirtyType.value,
    )

  @staticmethod
  @overload(QQuickItem, DirtyType)
  @overload(NoneType, DirtyType)
  def addDirty(
      referencedItem: Optional[QQuickItem],
      dirtyType: DirtyType,
  ) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupport::addDirty(QQuickItem
    *referencedItem, DirtyType dirtyType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#addDirty

    Parameters
    ----------

    referencedItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dirtyType : DirtyType
      Passed on as its number.
    """
    #  void QQuickDesignerSupport::addDirty(QQuickItem *referencedItem,
    #      DirtyType dirtyType)
    Rituals.call(
        'ritual_ZN21QQuickDesignerSupport8addDirtyEP10QQuickItemNS_9DirtyTy'
        'peE',
        CuteMixin._addressOf(referencedItem), dirtyType.value,
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def resetDirty(referencedItem: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupport::resetDirty(QQuickItem
    *referencedItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#resetDirty

    Parameters
    ----------

    referencedItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupport::resetDirty(QQuickItem *referencedItem)
    Rituals.call(
        'ritual_ZN21QQuickDesignerSupport10resetDirtyEP10QQuickItem',
        CuteMixin._addressOf(referencedItem),
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def windowTransform(referencedItem: Optional[QQuickItem]) -> QTransform:
    """
    Calls Qt's 'QTransform QQuickDesignerSupport::windowTransform(QQuickItem
    *referencedItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#windowTransform

    Parameters
    ----------

    referencedItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QQuickDesignerSupport::windowTransform(QQuickItem
    #      *referencedItem)
    address = Rituals.call(
        'ritual_ZN21QQuickDesignerSupport15windowTransformEP10QQuickItem',
        CuteMixin._addressOf(referencedItem),
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def parentTransform(referencedItem: Optional[QQuickItem]) -> QTransform:
    """
    Calls Qt's 'QTransform QQuickDesignerSupport::parentTransform(QQuickItem
    *referencedItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#parentTransform

    Parameters
    ----------

    referencedItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QTransform
      A new cute QTransform around the copy Qt gave back. Python owns it.
    """
    #  QTransform QQuickDesignerSupport::parentTransform(QQuickItem
    #      *referencedItem)
    address = Rituals.call(
        'ritual_ZN21QQuickDesignerSupport15parentTransformEP10QQuickItem',
        CuteMixin._addressOf(referencedItem),
    )
    from ..QtGui import QTransform
    return QTransform._cuteOwning(address)

  @staticmethod
  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def isAnchoredTo(
      fromItem: Optional[QQuickItem],
      toItem: Optional[QQuickItem],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupport::isAnchoredTo(QQuickItem
    *fromItem, QQuickItem *toItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#isAnchoredTo

    Parameters
    ----------

    fromItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    toItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDesignerSupport::isAnchoredTo(QQuickItem *fromItem,
    #      QQuickItem *toItem)
    return Rituals.call(
        'ritual_ZN21QQuickDesignerSupport12isAnchoredToEP10QQuickItemS1_',
        CuteMixin._addressOf(fromItem), CuteMixin._addressOf(toItem),
    )

  @staticmethod
  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def areChildrenAnchoredTo(
      fromItem: Optional[QQuickItem],
      toItem: Optional[QQuickItem],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupport::areChildrenAnchoredTo(QQuickItem
    *fromItem, QQuickItem *toItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#areChildrenAnchoredTo

    Parameters
    ----------

    fromItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    toItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDesignerSupport::areChildrenAnchoredTo(QQuickItem
    #      *fromItem, QQuickItem *toItem)
    return Rituals.call(
        'ritual_ZN21QQuickDesignerSupport21areChildrenAnchoredToEP10QQuickI'
        'temS1_',
        CuteMixin._addressOf(fromItem), CuteMixin._addressOf(toItem),
    )

  @staticmethod
  @overload(QQuickItem, str)
  @overload(NoneType, str)
  def hasAnchor(item: Optional[QQuickItem], name: str) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupport::hasAnchor(QQuickItem *item, const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#hasAnchor

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuickDesignerSupport::hasAnchor(QQuickItem *item, const QString
    #      &name)
    return Rituals.call(
        'ritual_ZN21QQuickDesignerSupport9hasAnchorEP10QQuickItemRK7QString',
        CuteMixin._addressOf(item), name,
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def anchorFillTargetItem(
      item: Optional[QQuickItem],
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickDesignerSupport::anchorFillTargetItem(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#anchorFillTargetItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickDesignerSupport::anchorFillTargetItem(QQuickItem
    #      *item)
    address = Rituals.call(
        'ritual_ZN21QQuickDesignerSupport20anchorFillTargetItemEP10QQuickIt'
        'em',
        CuteMixin._addressOf(item),
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def anchorCenterInTargetItem(
      item: Optional[QQuickItem],
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickDesignerSupport::anchorCenterInTargetItem(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickDesignerSupport::anchorCenterInTargetItem(QQuickItem
    #      *item)
    address = Rituals.call(
        'ritual_ZN21QQuickDesignerSupport24anchorCenterInTargetItemEP10QQui'
        'ckItem',
        CuteMixin._addressOf(item),
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  @staticmethod
  @overload(QQuickItem, str)
  @overload(NoneType, str)
  def resetAnchor(item: Optional[QQuickItem], name: str) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupport::resetAnchor(QQuickItem *item,
    const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#resetAnchor

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickDesignerSupport::resetAnchor(QQuickItem *item, const
    #      QString &name)
    Rituals.call(
        'ritual_ZN21QQuickDesignerSupport11resetAnchorEP10QQuickItemRK7QStr'
        'ing',
        CuteMixin._addressOf(item), name,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def emitComponentCompleteSignalForAttachedProperty(
      item: Optional[QObject],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDesignerSupport::emitComponentCompleteSignalForAttachedProperty(
    QObject *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html

    Parameters
    ----------

    item : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupport::
    #      emitComponentCompleteSignalForAttachedProperty(QObject *item)
    Rituals.call(
        'ritual_ZN21QQuickDesignerSupport46emitComponentCompleteSignalForAt'
        'tachedPropertyEP7QObject',
        CuteMixin._addressOf(item, 'QObject'),
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def statesForItem(item: Optional[QQuickItem]) -> QList[QObject]:
    """
    Calls Qt's 'QList<QObject *>
    QQuickDesignerSupport::statesForItem(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#statesForItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QObject *> QQuickDesignerSupport::statesForItem(QQuickItem
    #      *item)
    address = Rituals.call(
        'ritual_ZN21QQuickDesignerSupport13statesForItemEP10QQuickItem',
        CuteMixin._addressOf(item),
    )
    from ..QtCore import QObject
    return QList[QObject]._cuteOwning(address)

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def isComponentComplete(item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupport::isComponentComplete(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#isComponentComplete

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDesignerSupport::isComponentComplete(QQuickItem *item)
    return Rituals.call(
        'ritual_ZN21QQuickDesignerSupport19isComponentCompleteEP10QQuickIte'
        'm',
        CuteMixin._addressOf(item),
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def borderWidth(item: Optional[QQuickItem]) -> int:
    """
    Calls Qt's 'int QQuickDesignerSupport::borderWidth(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#borderWidth

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QQuickDesignerSupport::borderWidth(QQuickItem *item)
    return Rituals.call(
        'ritual_ZN21QQuickDesignerSupport11borderWidthEP10QQuickItem',
        CuteMixin._addressOf(item),
    )

  @staticmethod
  @overload(QQmlContext)
  @overload(NoneType)
  def refreshExpressions(context: Optional[QQmlContext]) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupport::refreshExpressions(QQmlContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#refreshExpressions

    Parameters
    ----------

    context : Optional[QQmlContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupport::refreshExpressions(QQmlContext *context)
    Rituals.call(
        'ritual_ZN21QQuickDesignerSupport18refreshExpressionsEP11QQmlContex'
        't',
        CuteMixin._addressOf(context),
    )

  @staticmethod
  @overload(QQuickView, QQuickItem)
  @overload(QQuickView, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def setRootItem(
      view: Optional[QQuickView],
      item: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupport::setRootItem(QQuickView *view,
    QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#setRootItem

    Parameters
    ----------

    view : Optional[QQuickView]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupport::setRootItem(QQuickView *view, QQuickItem
    #      *item)
    Rituals.call(
        'ritual_ZN21QQuickDesignerSupport11setRootItemEP10QQuickViewP10QQui'
        'ckItem',
        CuteMixin._addressOf(view), CuteMixin._addressOf(item),
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def isValidWidth(item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupport::isValidWidth(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#isValidWidth

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDesignerSupport::isValidWidth(QQuickItem *item)
    return Rituals.call(
        'ritual_ZN21QQuickDesignerSupport12isValidWidthEP10QQuickItem',
        CuteMixin._addressOf(item),
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def isValidHeight(item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickDesignerSupport::isValidHeight(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#isValidHeight

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDesignerSupport::isValidHeight(QQuickItem *item)
    return Rituals.call(
        'ritual_ZN21QQuickDesignerSupport13isValidHeightEP10QQuickItem',
        CuteMixin._addressOf(item),
    )

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def updateDirtyNode(item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupport::updateDirtyNode(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#updateDirtyNode

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupport::updateDirtyNode(QQuickItem *item)
    Rituals.call(
        'ritual_ZN21QQuickDesignerSupport15updateDirtyNodeEP10QQuickItem',
        CuteMixin._addressOf(item),
    )

  @staticmethod
  def activateDesignerMode() -> None:
    """
    Calls Qt's 'void QQuickDesignerSupport::activateDesignerMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#activateDesignerMode
    """
    #  void QQuickDesignerSupport::activateDesignerMode()
    Rituals.call('ritual_ZN21QQuickDesignerSupport20activateDesignerModeEv')

  @staticmethod
  def disableComponentComplete() -> None:
    """
    Calls Qt's 'void QQuickDesignerSupport::disableComponentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html
    """
    #  void QQuickDesignerSupport::disableComponentComplete()
    Rituals.call(
        'ritual_ZN21QQuickDesignerSupport24disableComponentCompleteEv',
    )

  @staticmethod
  def enableComponentComplete() -> None:
    """
    Calls Qt's 'void QQuickDesignerSupport::enableComponentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#enableComponentComplete
    """
    #  void QQuickDesignerSupport::enableComponentComplete()
    Rituals.call(
        'ritual_ZN21QQuickDesignerSupport23enableComponentCompleteEv',
    )

  @staticmethod
  @overload(QQuickWindow)
  @overload(NoneType)
  def polishItems(window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupport::polishItems(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#polishItems

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDesignerSupport::polishItems(QQuickWindow *window)
    Rituals.call(
        'ritual_ZN21QQuickDesignerSupport11polishItemsEP12QQuickWindow',
        CuteMixin._addressOf(window),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDesignerSupport'

  #  Qt's '~QQuickDesignerSupport()'. Naming it makes this a value class:
  #  Python owns every C++ QQuickDesignerSupport behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QQuickDesignerSupportD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QQuickDesignerSupport::QQuickDesignerSupport()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#QQuickDesignerSupport
    """
    #  QQuickDesignerSupport::QQuickDesignerSupport()
    self._noteCreation(QQuickDesignerSupport, lambda: Rituals.call(
        'ritual_ZN21QQuickDesignerSupportC1Ev',
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

  @overload(QQuickItem)
  @overload(NoneType)
  @overload(QQuickItem, bool)
  @overload(NoneType, bool)
  def refFromEffectItem(
      self,
      referencedItem: Optional[QQuickItem],
      hide: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupport::refFromEffectItem(QQuickItem
    *referencedItem, bool hide)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#refFromEffectItem

    Parameters
    ----------

    referencedItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    hide : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickDesignerSupport::refFromEffectItem(QQuickItem
    #      *referencedItem, bool hide)
    self.uglySide.call(
        'ritual_ZN21QQuickDesignerSupport17refFromEffectItemEP10QQuickItemb',
        self._addressOf(referencedItem), hide,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  @overload(QQuickItem, bool)
  @overload(NoneType, bool)
  def derefFromEffectItem(
      self,
      referencedItem: Optional[QQuickItem],
      unhide: bool = True,
  ) -> None:
    """
    Calls Qt's 'void QQuickDesignerSupport::derefFromEffectItem(QQuickItem
    *referencedItem, bool unhide)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#derefFromEffectItem

    Parameters
    ----------

    referencedItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    unhide : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickDesignerSupport::derefFromEffectItem(QQuickItem
    #      *referencedItem, bool unhide)
    self.uglySide.call(
        'ritual_ZN21QQuickDesignerSupport19derefFromEffectItemEP10QQuickIte'
        'mb',
        self._addressOf(referencedItem), unhide,
    )

  @overload(QQuickItem, QRectF, QSize)
  @overload(NoneType, QRectF, QSize)
  def renderImageForItem(
      self,
      referencedItem: Optional[QQuickItem],
      boundingRect: QRectF,
      imageSize: QSize,
  ) -> QImage:
    """
    Calls Qt's 'QImage QQuickDesignerSupport::renderImageForItem(QQuickItem
    *referencedItem, const QRectF &boundingRect, const QSize &imageSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdesignersupport.html#renderImageForItem

    Parameters
    ----------

    referencedItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    boundingRect : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    imageSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickDesignerSupport::renderImageForItem(QQuickItem
    #      *referencedItem, const QRectF &boundingRect, const QSize
    #      &imageSize)
    address = self.uglySide.call(
        'ritual_ZN21QQuickDesignerSupport18renderImageForItemEP10QQuickItem'
        'RK6QRectFRK5QSize',
        self._addressOf(referencedItem), self._valueOf(boundingRect),
        self._valueOf(imageSize),
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  @staticmethod
  def anchorLineTarget(*__, **_) -> Never:
    """
    Qt's 'std::pair<QString, QObject *>
    QQuickDesignerSupport::anchorLineTarget(QQuickItem *item, const QString
    &name, QQmlContext *context)': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQuickDesignerSupport.anchorLineTarget' has no cute function yet. "
        "Qt's 'std::pair<QString, QObject *> "
        "QQuickDesignerSupport::anchorLineTarget(QQuickItem *item, const "
        "QString &name, QQmlContext *context)': gives a type Python has no "
        "way to take yet.")
