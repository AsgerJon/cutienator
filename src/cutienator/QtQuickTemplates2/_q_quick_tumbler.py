"""
QQuickTumbler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktumbler_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickTumbler to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
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

  from ..QtCore import QMetaObject, QRectF, QVariant
  from ..QtGui import QFont, QKeyEvent
  from ..QtQml import QQmlComponent
  from . import QQuickTumblerAttached, QQuickTumblerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']
  QQmlComponent = WAIT['QQmlComponent']
  QRectF = WAIT['QRectF']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTumbler(QQuickControl):
  """
  The cute side of Qt's QQuickTumbler: a plain Python object standing in
  front of one C++ QQuickTumbler.

  It is built on the cute 'QQuickControl', as Qt's QQuickTumbler is built on
  Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTumbler that has a ritual and that Python can
  call so far, 37 names in all: 'metaObject', 'tr', 'model', 'setModel',
  'count', 'currentIndex', 'setCurrentIndex', 'currentItem', 'delegate',
  'setDelegate', 'visibleItemCount', 'setVisibleItemCount',
  'qmlAttachedProperties', 'wrap', 'setWrap', 'resetWrap', 'isMoving',
  'positionViewAtIndex', 'flickDeceleration', 'setFlickDeceleration',
  'resetFlickDeceleration', 'modelChanged', 'countChanged',
  'currentIndexChanged', 'currentItemChanged', 'delegateChanged',
  'visibleItemCountChanged', 'wrapChanged', 'movingChanged',
  'flickDecelerationChanged', 'geometryChange', 'componentComplete',
  'contentItemChange', 'keyPressEvent', 'updatePolish', 'defaultFont',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTumbler::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickTumbler::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickTumbler::qt_qmlMarker_attached()': one of Qt's own inner
    workings.
  - Qt's 'QQuickTumbler::~QQuickTumbler()': the destructor: Python never
    removes a C++ QQuickTumbler.
  - Qt's 'const QQuickTumblerPrivate *QQuickTumbler::d_func() const': takes
    in Python what 'QQuickTumblerPrivate *QQuickTumbler::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 47 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTumbler is created at the first use, not by
    'QQuickTumbler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTumbler.
  - Qt tells when it has removed the C++ QQuickTumbler. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickTumbler, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PositionMode(CuteNum):
    """
    The enum 'QQuickTumbler::PositionMode' of Qt, with the 6 names Qt gives
    in it.
    """

    Beginning = Kee[int](0)
    Center = Kee[int](1)
    End = Kee[int](2)
    Visible = Kee[int](3)
    Contain = Kee[int](4)
    SnapPosition = Kee[int](5)

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
    Calls Qt's 'QString QQuickTumbler::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#tr

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
    #  QString QQuickTumbler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickTumbler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickTumblerAttached]:
    """
    Calls Qt's 'QQuickTumblerAttached
    *QQuickTumbler::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTumblerAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTumblerAttached *QQuickTumbler::qmlAttachedProperties(QObject
    #      *object)
    address = Rituals.call(
        'ritual_ZN13QQuickTumbler21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickTumblerAttached
    return QQuickTumblerAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTumbler'

  #  A C++ QQuickTumbler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTumbler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTumbler::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTumbler::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickTumbler10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickTumbler::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickTumbler::model() const
    address = self.uglySide.call('ritual_ZNK13QQuickTumbler5modelEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickTumbler::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#count
    """
    #  int QQuickTumbler::count() const
    return self.uglySide.call('ritual_ZNK13QQuickTumbler5countEv')

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QQuickTumbler::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#currentIndex
    """
    #  int QQuickTumbler::currentIndex() const
    return self.uglySide.call('ritual_ZNK13QQuickTumbler12currentIndexEv')

  def currentItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickTumbler::currentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#currentItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickTumbler::currentItem() const
    address = self.uglySide.call('ritual_ZNK13QQuickTumbler11currentItemEv')
    return QQuickItem._cuteAt(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickTumbler::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickTumbler::delegate() const
    address = self.uglySide.call('ritual_ZNK13QQuickTumbler8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def visibleItemCount(self) -> int:
    """
    Calls Qt's 'int QQuickTumbler::visibleItemCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#visibleItemCount
    """
    #  int QQuickTumbler::visibleItemCount() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickTumbler16visibleItemCountEv',
    )

  def wrap(self) -> bool:
    """
    Calls Qt's 'bool QQuickTumbler::wrap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#wrap
    """
    #  bool QQuickTumbler::wrap() const
    return self.uglySide.call('ritual_ZNK13QQuickTumbler4wrapEv')

  def isMoving(self) -> bool:
    """
    Calls Qt's 'bool QQuickTumbler::isMoving() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#isMoving
    """
    #  bool QQuickTumbler::isMoving() const
    return self.uglySide.call('ritual_ZNK13QQuickTumbler8isMovingEv')

  def flickDeceleration(self) -> float:
    """
    Calls Qt's 'qreal QQuickTumbler::flickDeceleration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#flickDeceleration
    """
    #  qreal QQuickTumbler::flickDeceleration() const
    return self.uglySide.call(
        'ritual_ZNK13QQuickTumbler17flickDecelerationEv',
    )

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickTumbler::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickTumbler::defaultFont() const
    ritual = 'ritual_ZNK13QQuickTumbler11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickTumbler11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModel(self, model: QVariant) -> None:
    """
    Calls Qt's 'void QQuickTumbler::setModel(const QVariant &model)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#setModel

    Parameters
    ----------

    model : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickTumbler::setModel(const QVariant &model)
    self.uglySide.call(
        'ritual_ZN13QQuickTumbler8setModelERK8QVariant',
        self._valueOf(model),
    )

  @overload(int)
  def setCurrentIndex(self, currentIndex: int) -> None:
    """
    Calls Qt's 'void QQuickTumbler::setCurrentIndex(int currentIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#setCurrentIndex

    Parameters
    ----------

    currentIndex : int
      Passed on as it is.
    """
    #  void QQuickTumbler::setCurrentIndex(int currentIndex)
    self.uglySide.call(
        'ritual_ZN13QQuickTumbler15setCurrentIndexEi', currentIndex,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickTumbler::setDelegate(QQmlComponent *delegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTumbler::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN13QQuickTumbler11setDelegateEP13QQmlComponent',
        self._addressOf(delegate),
    )

  @overload(int)
  def setVisibleItemCount(self, visibleItemCount: int) -> None:
    """
    Calls Qt's 'void QQuickTumbler::setVisibleItemCount(int
    visibleItemCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#setVisibleItemCount

    Parameters
    ----------

    visibleItemCount : int
      Passed on as it is.
    """
    #  void QQuickTumbler::setVisibleItemCount(int visibleItemCount)
    self.uglySide.call(
        'ritual_ZN13QQuickTumbler19setVisibleItemCountEi', visibleItemCount,
    )

  @overload(bool)
  def setWrap(self, wrap: bool) -> None:
    """
    Calls Qt's 'void QQuickTumbler::setWrap(bool wrap)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#setWrap

    Parameters
    ----------

    wrap : bool
      Passed on as it is.
    """
    #  void QQuickTumbler::setWrap(bool wrap)
    self.uglySide.call('ritual_ZN13QQuickTumbler7setWrapEb', wrap)

  @overload(float)
  def setFlickDeceleration(self, newFlickDeceleration: float) -> None:
    """
    Calls Qt's 'void QQuickTumbler::setFlickDeceleration(qreal
    newFlickDeceleration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#setFlickDeceleration

    Parameters
    ----------

    newFlickDeceleration : float
      Passed on as it is.
    """
    #  void QQuickTumbler::setFlickDeceleration(qreal newFlickDeceleration)
    self.uglySide.call(
        'ritual_ZN13QQuickTumbler20setFlickDecelerationEd',
        newFlickDeceleration,
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
    Notes what was given, for Qt's 'QQuickTumbler::QQuickTumbler(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#QQuickTumbler

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTumbler::QQuickTumbler(QQuickItem *parent)
    self._noteCreation(QQuickTumbler, lambda: Rituals.call(
        'ritual_ZN13QQuickTumblerC1EP10QQuickItem', self._addressOf(parent),
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

  def resetWrap(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::resetWrap()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#resetWrap
    """
    #  void QQuickTumbler::resetWrap()
    self.uglySide.call('ritual_ZN13QQuickTumbler9resetWrapEv')

  @overload(int, PositionMode)
  def positionViewAtIndex(self, index: int, mode: PositionMode) -> None:
    """
    Calls Qt's 'void QQuickTumbler::positionViewAtIndex(int index,
    PositionMode mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#positionViewAtIndex

    Parameters
    ----------

    index : int
      Passed on as it is.

    mode : PositionMode
      Passed on as its number.
    """
    #  void QQuickTumbler::positionViewAtIndex(int index, PositionMode mode)
    self.uglySide.call(
        'ritual_ZN13QQuickTumbler19positionViewAtIndexEiNS_12PositionModeE',
        index, mode.value,
    )

  def resetFlickDeceleration(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::resetFlickDeceleration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#resetFlickDeceleration
    """
    #  void QQuickTumbler::resetFlickDeceleration()
    self.uglySide.call('ritual_ZN13QQuickTumbler22resetFlickDecelerationEv')

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::modelChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#modelChanged
    """
    #  void QQuickTumbler::modelChanged()
    self.uglySide.call('ritual_ZN13QQuickTumbler12modelChangedEv')

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#countChanged
    """
    #  void QQuickTumbler::countChanged()
    self.uglySide.call('ritual_ZN13QQuickTumbler12countChangedEv')

  def currentIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::currentIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#currentIndexChanged
    """
    #  void QQuickTumbler::currentIndexChanged()
    self.uglySide.call('ritual_ZN13QQuickTumbler19currentIndexChangedEv')

  def currentItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::currentItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#currentItemChanged
    """
    #  void QQuickTumbler::currentItemChanged()
    self.uglySide.call('ritual_ZN13QQuickTumbler18currentItemChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::delegateChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#delegateChanged
    """
    #  void QQuickTumbler::delegateChanged()
    self.uglySide.call('ritual_ZN13QQuickTumbler15delegateChangedEv')

  def visibleItemCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::visibleItemCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#visibleItemCountChanged
    """
    #  void QQuickTumbler::visibleItemCountChanged()
    self.uglySide.call('ritual_ZN13QQuickTumbler23visibleItemCountChangedEv')

  def wrapChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::wrapChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#wrapChanged
    """
    #  void QQuickTumbler::wrapChanged()
    self.uglySide.call('ritual_ZN13QQuickTumbler11wrapChangedEv')

  def movingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::movingChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#movingChanged
    """
    #  void QQuickTumbler::movingChanged()
    self.uglySide.call('ritual_ZN13QQuickTumbler13movingChangedEv')

  def flickDecelerationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::flickDecelerationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#flickDecelerationChanged
    """
    #  void QQuickTumbler::flickDecelerationChanged()
    self.uglySide.call(
        'ritual_ZN13QQuickTumbler24flickDecelerationChangedEv',
    )

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickTumbler::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickTumbler::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN13QQuickTumbler14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickTumbler14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#componentComplete
    """
    #  void QQuickTumbler::componentComplete()
    ritual = 'ritual_ZN13QQuickTumbler17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickTumbler17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def contentItemChange(
      self,
      newItem: Optional[QQuickItem],
      oldItem: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickTumbler::contentItemChange(QQuickItem *newItem,
    QQuickItem *oldItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktumbler.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTumbler::contentItemChange(QQuickItem *newItem, QQuickItem
    #      *oldItem)
    ritual = 'ritual_ZN13QQuickTumbler17contentItemChangeEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN13QQuickTumbler17contentItemChangeEP10QQuickItemS1_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickTumbler::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTumbler::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN13QQuickTumbler13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickTumbler13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickTumbler::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#updatePolish
    """
    #  void QQuickTumbler::updatePolish()
    ritual = 'ritual_ZN13QQuickTumbler12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QQuickTumbler12updatePolishEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQuickTumblerPrivate]:
    """
    Calls Qt's 'QQuickTumblerPrivate *QQuickTumbler::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktumbler.html#d_func

    Returns
    -------

    Optional[QQuickTumblerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTumblerPrivate *QQuickTumbler::d_func()
    address = self.uglySide.call('ritual_ZN13QQuickTumbler6d_funcEv')
    from . import QQuickTumblerPrivate
    return QQuickTumblerPrivate._cuteAt(address)
