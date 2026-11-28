"""
QQuickSelectionRectangle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickselectionrectangle_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickSelectionRectangle to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QQmlComponent
  from . import QQuickSelectionRectangleAttached
  from . import QQuickSelectionRectanglePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSelectionRectangle(QQuickControl):
  """
  The cute side of Qt's QQuickSelectionRectangle: a plain Python object
  standing in front of one C++ QQuickSelectionRectangle.

  It is built on the cute 'QQuickControl', as Qt's QQuickSelectionRectangle
  is built on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSelectionRectangle that has a ritual and that
  Python can call so far, 20 names in all: 'metaObject', 'tr', 'target',
  'setTarget', 'active', 'dragging', 'selectionMode', 'setSelectionMode',
  'topLeftHandle', 'setTopLeftHandle', 'bottomRightHandle',
  'setBottomRightHandle', 'qmlAttachedProperties', 'targetChanged',
  'activeChanged', 'draggingChanged', 'topLeftHandleChanged',
  'bottomRightHandleChanged', 'selectionModeChanged', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSelectionRectangle::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickSelectionRectangle::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickSelectionRectangle::qt_qmlMarker_attached()': one of
    Qt's own inner workings.
  - Qt's 'const QQuickSelectionRectanglePrivate
    *QQuickSelectionRectangle::d_func() const': takes in Python what
    'QQuickSelectionRectanglePrivate *QQuickSelectionRectangle::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 29 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSelectionRectangle is created at the first use, not by
    'QQuickSelectionRectangle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSelectionRectangle.
  - Qt tells when it has removed the C++ QQuickSelectionRectangle. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickSelectionRectangle, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class SelectionMode(CuteNum):
    """
    The enum 'QQuickSelectionRectangle::SelectionMode' of Qt, with the 3
    names Qt gives in it.
    """

    Drag = Kee[int](0)
    PressAndHold = Kee[int](1)
    Auto = Kee[int](2)

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
    Calls Qt's 'QString QQuickSelectionRectangle::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickselectionrectangle.html#tr

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
    #  QString QQuickSelectionRectangle::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuickSelectionRectangle2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      obj: Optional[QObject],
  ) -> Optional[QQuickSelectionRectangleAttached]:
    """
    Calls Qt's 'QQuickSelectionRectangleAttached
    *QQuickSelectionRectangle::qmlAttachedProperties(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickSelectionRectangleAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSelectionRectangleAttached
    #      *QQuickSelectionRectangle::qmlAttachedProperties(QObject *obj)
    address = Rituals.call(
        'ritual_ZN24QQuickSelectionRectangle21qmlAttachedPropertiesEP7QObje'
        'ct',
        CuteMixin._addressOf(obj, 'QObject'),
    )
    from . import QQuickSelectionRectangleAttached
    return QQuickSelectionRectangleAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSelectionRectangle'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSelectionRectangle::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSelectionRectangle::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickSelectionRectangle10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def target(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickSelectionRectangle::target() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#target

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickSelectionRectangle::target() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickSelectionRectangle6targetEv',
    )
    return QQuickItem._cuteAt(address)

  def selectionMode(self) -> SelectionMode:
    """
    Calls Qt's 'SelectionMode QQuickSelectionRectangle::selectionMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#selectionMode

    Returns
    -------

    SelectionMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SelectionMode(number)'
      gives.
    """
    #  SelectionMode QQuickSelectionRectangle::selectionMode() const
    return QQuickSelectionRectangle.SelectionMode(self.uglySide.call(
        'ritual_ZNK24QQuickSelectionRectangle13selectionModeEv',
    ))

  def topLeftHandle(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickSelectionRectangle::topLeftHandle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#topLeftHandle

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickSelectionRectangle::topLeftHandle() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickSelectionRectangle13topLeftHandleEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def bottomRightHandle(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickSelectionRectangle::bottomRightHandle()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#bottomRightHandle

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickSelectionRectangle::bottomRightHandle() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickSelectionRectangle17bottomRightHandleEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setTarget(self, target: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectangle::setTarget(QQuickItem
    *target)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#setTarget

    Parameters
    ----------

    target : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSelectionRectangle::setTarget(QQuickItem *target)
    self.uglySide.call(
        'ritual_ZN24QQuickSelectionRectangle9setTargetEP10QQuickItem',
        self._addressOf(target),
    )

  @overload(SelectionMode)
  def setSelectionMode(self, selectionMode: SelectionMode) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectangle::setSelectionMode(SelectionMode
    selectionMode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#setSelectionMode

    Parameters
    ----------

    selectionMode : SelectionMode
      Passed on as its number.
    """
    #  void QQuickSelectionRectangle::setSelectionMode(SelectionMode
    #      selectionMode)
    self.uglySide.call(
        'ritual_ZN24QQuickSelectionRectangle16setSelectionModeENS_13Selecti'
        'onModeE',
        selectionMode.value,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setTopLeftHandle(self, topLeftHandle: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectangle::setTopLeftHandle(QQmlComponent
    *topLeftHandle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#setTopLeftHandle

    Parameters
    ----------

    topLeftHandle : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSelectionRectangle::setTopLeftHandle(QQmlComponent
    #      *topLeftHandle)
    self.uglySide.call(
        'ritual_ZN24QQuickSelectionRectangle16setTopLeftHandleEP13QQmlCompo'
        'nent',
        self._addressOf(topLeftHandle),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setBottomRightHandle(
      self,
      bottomRightHandle: Optional[QQmlComponent],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickSelectionRectangle::setBottomRightHandle(QQmlComponent
    *bottomRightHandle)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#setBottomRightHandle

    Parameters
    ----------

    bottomRightHandle : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSelectionRectangle::setBottomRightHandle(QQmlComponent
    #      *bottomRightHandle)
    self.uglySide.call(
        'ritual_ZN24QQuickSelectionRectangle20setBottomRightHandleEP13QQmlC'
        'omponent',
        self._addressOf(bottomRightHandle),
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
    Notes what was given, for Qt's
    'QQuickSelectionRectangle::QQuickSelectionRectangle(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSelectionRectangle::QQuickSelectionRectangle(QQuickItem *parent)
    self._noteCreation(QQuickSelectionRectangle, lambda: Rituals.call(
        'ritual_ZN24QQuickSelectionRectangleC1EP10QQuickItem',
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

  def active(self) -> bool:
    """
    Calls Qt's 'bool QQuickSelectionRectangle::active()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#active
    """
    #  bool QQuickSelectionRectangle::active()
    return self.uglySide.call('ritual_ZN24QQuickSelectionRectangle6activeEv')

  def dragging(self) -> bool:
    """
    Calls Qt's 'bool QQuickSelectionRectangle::dragging()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#dragging
    """
    #  bool QQuickSelectionRectangle::dragging()
    return self.uglySide.call(
        'ritual_ZN24QQuickSelectionRectangle8draggingEv',
    )

  def targetChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectangle::targetChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#targetChanged
    """
    #  void QQuickSelectionRectangle::targetChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickSelectionRectangle13targetChangedEv',
    )

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectangle::activeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#activeChanged
    """
    #  void QQuickSelectionRectangle::activeChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickSelectionRectangle13activeChangedEv',
    )

  def draggingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectangle::draggingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#draggingChanged
    """
    #  void QQuickSelectionRectangle::draggingChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickSelectionRectangle15draggingChangedEv',
    )

  def topLeftHandleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectangle::topLeftHandleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#topLeftHandleChanged
    """
    #  void QQuickSelectionRectangle::topLeftHandleChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickSelectionRectangle20topLeftHandleChangedEv',
    )

  def bottomRightHandleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectangle::bottomRightHandleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html
    """
    #  void QQuickSelectionRectangle::bottomRightHandleChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickSelectionRectangle24bottomRightHandleChangedEv',
    )

  def selectionModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSelectionRectangle::selectionModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#selectionModeChanged
    """
    #  void QQuickSelectionRectangle::selectionModeChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickSelectionRectangle20selectionModeChangedEv',
    )

  def d_func(self) -> Optional[QQuickSelectionRectanglePrivate]:
    """
    Calls Qt's 'QQuickSelectionRectanglePrivate
    *QQuickSelectionRectangle::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickselectionrectangle.html#d_func

    Returns
    -------

    Optional[QQuickSelectionRectanglePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSelectionRectanglePrivate *QQuickSelectionRectangle::d_func()
    address = self.uglySide.call(
        'ritual_ZN24QQuickSelectionRectangle6d_funcEv',
    )
    from . import QQuickSelectionRectanglePrivate
    return QQuickSelectionRectanglePrivate._cuteAt(address)
