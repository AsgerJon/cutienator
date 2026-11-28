"""
QQStyleKitControlProperties binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsStyleKit/6.12.0/QtLabsStyleKit/private/qqstylekitcontrolproperties_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQStyleKitControlProperties to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQSK, QQStyleKitPropertyGroup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQStyleKitControlState, QQStyleKitDelegateProperties
  from . import QQStyleKitHandleProperties, QQStyleKitIndicatorWithSubTypes
  from . import QQStyleKitReader, QQStyleKitStyle, QQStyleKitTextProperties
  from ..QtQuick import QQuickTransition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickTransition = WAIT['QQuickTransition']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQStyleKitControlProperties(QQStyleKitPropertyGroup):
  """
  The cute side of Qt's QQStyleKitControlProperties: a plain Python object
  standing in front of one C++ QQStyleKitControlProperties.

  It is built on the cute 'QQStyleKitPropertyGroup', as Qt's
  QQStyleKitControlProperties is built on Qt's QQStyleKitPropertyGroup, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQStyleKitControlProperties that has a ritual and
  that Python can call so far, 36 names in all: 'metaObject', 'tr',
  'emitChangedForAllStyleProperties', 'style', 'subclass',
  'asQQStyleKitReader', 'asQQStyleKitState', 'spacing', 'setSpacing',
  'padding', 'setPadding', 'leftPadding', 'setLeftPadding', 'rightPadding',
  'setRightPadding', 'topPadding', 'setTopPadding', 'bottomPadding',
  'setBottomPadding', 'transition', 'setTransition', 'text', 'background',
  'handle', 'indicator', 'backgroundChanged', 'handleChanged',
  'indicatorChanged', 'spacingChanged', 'paddingChanged',
  'leftPaddingChanged', 'rightPaddingChanged', 'topPaddingChanged',
  'bottomPaddingChanged', 'transitionChanged', 'textChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQStyleKitControlProperties::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQStyleKitControlProperties::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQStyleKitControlProperties::qt_qmlMarker_uncreatable()': one
    of Qt's own inner workings.
  - Qt's 'void
    QQStyleKitControlProperties::forEachUsedDelegate(std::function<void
    (QQStyleKitDelegateProperties *, QQSK::Delegate, const QString &)> f)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 46 functions Qt declares: 2 not a gap; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QQStyleKitControlProperties is created at the first use, not by
    'QQStyleKitControlProperties(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQStyleKitControlProperties.
  - Qt tells when it has removed the C++ QQStyleKitControlProperties. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQStyleKitControlProperties that has no cute function
    yet, 'emitGlobally', 'forEachUsedDelegate', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQStyleKitControlProperties::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#tr

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
    #  QString QQStyleKitControlProperties::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QQStyleKitControlProperties2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQStyleKitControlProperties'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQStyleKitControlProperties::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQStyleKitControlProperties::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def style(self) -> Optional[QQStyleKitStyle]:
    """
    Calls Qt's 'QQStyleKitStyle *QQStyleKitControlProperties::style() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#style

    Returns
    -------

    Optional[QQStyleKitStyle]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitStyle *QQStyleKitControlProperties::style() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties5styleEv',
    )
    from . import QQStyleKitStyle
    return QQStyleKitStyle._cuteAt(address)

  def subclass(self) -> QQSK.Subclass:
    """
    Calls Qt's 'QQSK::Subclass QQStyleKitControlProperties::subclass()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#subclass

    Returns
    -------

    QQSK.Subclass
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QQSK.Subclass(number)'
      gives.
    """
    #  QQSK::Subclass QQStyleKitControlProperties::subclass() const
    return QQSK.Subclass(self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties8subclassEv',
    ))

  def asQQStyleKitReader(self) -> Optional[QQStyleKitReader]:
    """
    Calls Qt's 'QQStyleKitReader
    *QQStyleKitControlProperties::asQQStyleKitReader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html

    Returns
    -------

    Optional[QQStyleKitReader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitReader *QQStyleKitControlProperties::asQQStyleKitReader()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties18asQQStyleKitReaderEv',
    )
    from . import QQStyleKitReader
    return QQStyleKitReader._cuteAt(address)

  def asQQStyleKitState(self) -> Optional[QQStyleKitControlState]:
    """
    Calls Qt's 'QQStyleKitControlState
    *QQStyleKitControlProperties::asQQStyleKitState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#asQQStyleKitState

    Returns
    -------

    Optional[QQStyleKitControlState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitControlState
    #      *QQStyleKitControlProperties::asQQStyleKitState() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties17asQQStyleKitStateEv',
    )
    from . import QQStyleKitControlState
    return QQStyleKitControlState._cuteAt(address)

  def spacing(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitControlProperties::spacing() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#spacing
    """
    #  qreal QQStyleKitControlProperties::spacing() const
    return self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties7spacingEv',
    )

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitControlProperties::padding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#padding
    """
    #  qreal QQStyleKitControlProperties::padding() const
    return self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties7paddingEv',
    )

  def leftPadding(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitControlProperties::leftPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#leftPadding
    """
    #  qreal QQStyleKitControlProperties::leftPadding() const
    return self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties11leftPaddingEv',
    )

  def rightPadding(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitControlProperties::rightPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#rightPadding
    """
    #  qreal QQStyleKitControlProperties::rightPadding() const
    return self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties12rightPaddingEv',
    )

  def topPadding(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitControlProperties::topPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#topPadding
    """
    #  qreal QQStyleKitControlProperties::topPadding() const
    return self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties10topPaddingEv',
    )

  def bottomPadding(self) -> float:
    """
    Calls Qt's 'qreal QQStyleKitControlProperties::bottomPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#bottomPadding
    """
    #  qreal QQStyleKitControlProperties::bottomPadding() const
    return self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties13bottomPaddingEv',
    )

  def transition(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQStyleKitControlProperties::transition()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#transition

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQStyleKitControlProperties::transition() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties10transitionEv',
    )
    from ..QtQuick import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def text(self) -> Optional[QQStyleKitTextProperties]:
    """
    Calls Qt's 'QQStyleKitTextProperties *QQStyleKitControlProperties::text()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#text

    Returns
    -------

    Optional[QQStyleKitTextProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitTextProperties *QQStyleKitControlProperties::text() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties4textEv',
    )
    from . import QQStyleKitTextProperties
    return QQStyleKitTextProperties._cuteAt(address)

  def background(self) -> Optional[QQStyleKitDelegateProperties]:
    """
    Calls Qt's 'QQStyleKitDelegateProperties
    *QQStyleKitControlProperties::background() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#background

    Returns
    -------

    Optional[QQStyleKitDelegateProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitDelegateProperties
    #      *QQStyleKitControlProperties::background() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties10backgroundEv',
    )
    from . import QQStyleKitDelegateProperties
    return QQStyleKitDelegateProperties._cuteAt(address)

  def handle(self) -> Optional[QQStyleKitHandleProperties]:
    """
    Calls Qt's 'QQStyleKitHandleProperties
    *QQStyleKitControlProperties::handle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#handle

    Returns
    -------

    Optional[QQStyleKitHandleProperties]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitHandleProperties *QQStyleKitControlProperties::handle()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties6handleEv',
    )
    from . import QQStyleKitHandleProperties
    return QQStyleKitHandleProperties._cuteAt(address)

  def indicator(self) -> Optional[QQStyleKitIndicatorWithSubTypes]:
    """
    Calls Qt's 'QQStyleKitIndicatorWithSubTypes
    *QQStyleKitControlProperties::indicator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#indicator

    Returns
    -------

    Optional[QQStyleKitIndicatorWithSubTypes]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQStyleKitIndicatorWithSubTypes
    #      *QQStyleKitControlProperties::indicator() const
    address = self.uglySide.call(
        'ritual_ZNK27QQStyleKitControlProperties9indicatorEv',
    )
    from . import QQStyleKitIndicatorWithSubTypes
    return QQStyleKitIndicatorWithSubTypes._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::setSpacing(qreal spacing)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#setSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QQStyleKitControlProperties::setSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties10setSpacingEd', spacing,
    )

  @overload(float)
  def setPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::setPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#setPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQStyleKitControlProperties::setPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties10setPaddingEd', padding,
    )

  @overload(float)
  def setLeftPadding(self, leftPadding: float) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::setLeftPadding(qreal
    leftPadding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#setLeftPadding

    Parameters
    ----------

    leftPadding : float
      Passed on as it is.
    """
    #  void QQStyleKitControlProperties::setLeftPadding(qreal leftPadding)
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties14setLeftPaddingEd',
        leftPadding,
    )

  @overload(float)
  def setRightPadding(self, rightPadding: float) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::setRightPadding(qreal
    rightPadding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#setRightPadding

    Parameters
    ----------

    rightPadding : float
      Passed on as it is.
    """
    #  void QQStyleKitControlProperties::setRightPadding(qreal rightPadding)
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties15setRightPaddingEd',
        rightPadding,
    )

  @overload(float)
  def setTopPadding(self, topPadding: float) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::setTopPadding(qreal
    topPadding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#setTopPadding

    Parameters
    ----------

    topPadding : float
      Passed on as it is.
    """
    #  void QQStyleKitControlProperties::setTopPadding(qreal topPadding)
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties13setTopPaddingEd',
        topPadding,
    )

  @overload(float)
  def setBottomPadding(self, bottomPadding: float) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::setBottomPadding(qreal
    bottomPadding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#setBottomPadding

    Parameters
    ----------

    bottomPadding : float
      Passed on as it is.
    """
    #  void QQStyleKitControlProperties::setBottomPadding(qreal
    #      bottomPadding)
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties16setBottomPaddingEd',
        bottomPadding,
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setTransition(self, transition: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void
    QQStyleKitControlProperties::setTransition(QQuickTransition
    *transition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#setTransition

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQStyleKitControlProperties::setTransition(QQuickTransition
    #      *transition)
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties13setTransitionEP16QQuickTra'
        'nsition',
        self._addressOf(transition),
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

  @overload(QQSK.PropertyGroup)
  @overload(QQSK.PropertyGroup, QObject)
  @overload(QQSK.PropertyGroup, NoneType)
  def __init__(
      self,
      group: QQSK.PropertyGroup,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQStyleKitControlProperties::QQStyleKitControlProperties(QQSK::
    PropertyGroup group, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html

    Parameters
    ----------

    group : QQSK.PropertyGroup
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQStyleKitControlProperties::QQStyleKitControlProperties(QQSK::
    #      PropertyGroup group, QObject *parent)
    self._noteCreation(QQStyleKitControlProperties, lambda: Rituals.call(
        'ritual_ZN27QQStyleKitControlPropertiesC1EN4QQSK13PropertyGroupEP7Q'
        'Object',
        group.value, self._addressOf(parent, 'QObject'),
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

  @overload(QQStyleKitPropertyGroup.EmitFlags)
  def emitChangedForAllStyleProperties(
      self,
      emitFlags: QQStyleKitPropertyGroup.EmitFlags,
  ) -> None:
    """
    Calls Qt's 'void
    QQStyleKitControlProperties::emitChangedForAllStyleProperties(EmitFlags
    emitFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html

    Parameters
    ----------

    emitFlags : QQStyleKitPropertyGroup.EmitFlags
      Passed on as its number.
    """
    #  void QQStyleKitControlProperties::emitChangedForAllStyleProperties(
    #      EmitFlags emitFlags)
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties32emitChangedForAllStyleProp'
        'ertiesE6QFlagsIN23QQStyleKitPropertyGroup8EmitFlagEE',
        emitFlags.value,
    )

  def backgroundChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::backgroundChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#backgroundChanged
    """
    #  void QQStyleKitControlProperties::backgroundChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties17backgroundChangedEv',
    )

  def handleChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::handleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#handleChanged
    """
    #  void QQStyleKitControlProperties::handleChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties13handleChangedEv',
    )

  def indicatorChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::indicatorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#indicatorChanged
    """
    #  void QQStyleKitControlProperties::indicatorChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties16indicatorChangedEv',
    )

  def spacingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::spacingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#spacingChanged
    """
    #  void QQStyleKitControlProperties::spacingChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties14spacingChangedEv',
    )

  def paddingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::paddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#paddingChanged
    """
    #  void QQStyleKitControlProperties::paddingChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties14paddingChangedEv',
    )

  def leftPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::leftPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html
    """
    #  void QQStyleKitControlProperties::leftPaddingChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties18leftPaddingChangedEv',
    )

  def rightPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::rightPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html
    """
    #  void QQStyleKitControlProperties::rightPaddingChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties19rightPaddingChangedEv',
    )

  def topPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::topPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#topPaddingChanged
    """
    #  void QQStyleKitControlProperties::topPaddingChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties17topPaddingChangedEv',
    )

  def bottomPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::bottomPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html
    """
    #  void QQStyleKitControlProperties::bottomPaddingChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties20bottomPaddingChangedEv',
    )

  def transitionChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::transitionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#transitionChanged
    """
    #  void QQStyleKitControlProperties::transitionChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties17transitionChangedEv',
    )

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQStyleKitControlProperties::textChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqstylekitcontrolproperties.html#textChanged
    """
    #  void QQStyleKitControlProperties::textChanged()
    self.uglySide.call(
        'ritual_ZN27QQStyleKitControlProperties11textChangedEv',
    )

  @staticmethod
  def emitGlobally(*__, **_) -> Never:
    """
    Qt's 'QQStyleKitControlProperties::emitGlobally': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQStyleKitControlProperties.emitGlobally' has no cute function "
        "yet. Qt's 'QQStyleKitControlProperties::emitGlobally': a template: "
        "a pattern and no single function.")

  @staticmethod
  def forEachUsedDelegate(*__, **_) -> Never:
    """
    Qt's 'void
    QQStyleKitControlProperties::forEachUsedDelegate(std::function<void
    (QQStyleKitDelegateProperties *, QQSK::Delegate, const QString &)> f)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQStyleKitControlProperties.forEachUsedDelegate' has no cute "
        "function yet. Qt's 'void "
        "QQStyleKitControlProperties::forEachUsedDelegate(std::function<void"
        " (QQStyleKitDelegateProperties *, QQSK::Delegate, const QString "
        "&)> f)': takes a type Python has no way to hand over yet.")
