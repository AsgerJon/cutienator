"""
QQuickBasePositioner binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickBasePositioner to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickImplicitSizeItem, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QSizeF
  from . import QQuickBasePositionerPrivate, QQuickPositionerAttached
  from . import QQuickTransition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickPositionerAttached = WAIT['QQuickPositionerAttached']
  QQuickTransition = WAIT['QQuickTransition']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickBasePositioner(QQuickImplicitSizeItem):
  """
  The cute side of Qt's QQuickBasePositioner: a plain Python object standing
  in front of one C++ QQuickBasePositioner.

  It is built on the cute 'QQuickImplicitSizeItem', as Qt's
  QQuickBasePositioner is built on Qt's QQuickImplicitSizeItem, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickBasePositioner that has a ritual and that
  Python can call so far, 45 names in all: 'metaObject', 'tr', 'spacing',
  'setSpacing', 'populate', 'setPopulate', 'move', 'setMove', 'add',
  'setAdd', 'qmlAttachedProperties', 'updateAttachedProperties', 'padding',
  'setPadding', 'resetPadding', 'topPadding', 'setTopPadding',
  'resetTopPadding', 'leftPadding', 'setLeftPadding', 'resetLeftPadding',
  'rightPadding', 'setRightPadding', 'resetRightPadding', 'bottomPadding',
  'setBottomPadding', 'resetBottomPadding', 'forceLayout',
  'componentComplete', 'itemChange', 'updatePolish', 'spacingChanged',
  'populateChanged', 'moveChanged', 'addChanged', 'paddingChanged',
  'topPaddingChanged', 'leftPaddingChanged', 'rightPaddingChanged',
  'bottomPaddingChanged', 'positioningComplete', 'prePositioning',
  'doPositioning', 'reportConflictingAnchors', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickBasePositioner::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickBasePositioner::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickBasePositioner::qt_qmlMarker_uncreatable()': one of Qt's
    own inner workings.
  - Qt's 'void QQuickBasePositioner::qt_qmlMarker_attached()': one of Qt's
    own inner workings.
  - Qt's 'QQuickBasePositioner::~QQuickBasePositioner()': the destructor:
    Python never removes a C++ QQuickBasePositioner.
  - Qt's
    'QQuickBasePositioner::QQuickBasePositioner(QQuickBasePositionerPrivate
    &dd, PositionerType at, QQuickItem *parent)': takes a type Python has no
    way to hand over yet.
  - Qt's 'void QQuickBasePositioner::positionItem(qreal x, qreal y,
    PositionedItem *target)': names 'QQuickBasePositioner::PositionedItem',
    which has no cute class yet.
  - Qt's 'void QQuickBasePositioner::positionItemX(qreal a0, PositionedItem
    *target)': names 'QQuickBasePositioner::PositionedItem', which has no
    cute class yet.
  - Qt's 'void QQuickBasePositioner::positionItemY(qreal a0, PositionedItem
    *target)': names 'QQuickBasePositioner::PositionedItem', which has no
    cute class yet.
  - Qt's 'const QQuickBasePositionerPrivate *QQuickBasePositioner::d_func()
    const': takes in Python what 'QQuickBasePositionerPrivate
    *QQuickBasePositioner::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 60 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickBasePositioner is created at the first use, not by
    'QQuickBasePositioner(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickBasePositioner.
  - Qt tells when it has removed the C++ QQuickBasePositioner. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickBasePositioner that has no cute function yet,
    'positionItem', 'positionItemX', 'positionItemY', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickBasePositioner, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class PositionerType(CuteNum):
    """
    The enum 'QQuickBasePositioner::PositionerType' of Qt, with the 4 names
    Qt gives in it.
    """

    NULL = Kee[int](0)
    Horizontal = Kee[int](1)
    Vertical = Kee[int](2)
    Both = Kee[int](3)

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
    Calls Qt's 'QString QQuickBasePositioner::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasepositioner.html#tr

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
    #  QString QQuickBasePositioner::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickBasePositioner2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      obj: Optional[QObject],
  ) -> Optional[QQuickPositionerAttached]:
    """
    Calls Qt's 'QQuickPositionerAttached
    *QQuickBasePositioner::qmlAttachedProperties(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#qmlAttachedProperties

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickPositionerAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPositionerAttached
    #      *QQuickBasePositioner::qmlAttachedProperties(QObject *obj)
    address = Rituals.call(
        'ritual_ZN20QQuickBasePositioner21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(obj, 'QObject'),
    )
    from . import QQuickPositionerAttached
    return QQuickPositionerAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickBasePositioner'

  #  A C++ QQuickBasePositioner Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickBasePositioner'

  #  The functions Qt calls itself that QQuickBasePositioner is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'doPositioning': (
          ('_ZN20QQuickBasePositioner13doPositioningEP6QSizeF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QSizeF'),
           )),
      ),
      'reportConflictingAnchors': (
          ('_ZN20QQuickBasePositioner24reportConflictingAnchorsEv',
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickBasePositioner::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickBasePositioner::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickBasePositioner10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def spacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickBasePositioner::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasepositioner.html#spacing
    """
    #  qreal QQuickBasePositioner::spacing() const
    return self.uglySide.call('ritual_ZNK20QQuickBasePositioner7spacingEv')

  def populate(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickBasePositioner::populate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasepositioner.html#populate

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickBasePositioner::populate() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickBasePositioner8populateEv',
    )
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def move(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickBasePositioner::move() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasepositioner.html#move

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickBasePositioner::move() const
    address = self.uglySide.call('ritual_ZNK20QQuickBasePositioner4moveEv')
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def add(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickBasePositioner::add() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasepositioner.html#add

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickBasePositioner::add() const
    address = self.uglySide.call('ritual_ZNK20QQuickBasePositioner3addEv')
    from . import QQuickTransition
    return QQuickTransition._cuteAt(address)

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QQuickBasePositioner::padding() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasepositioner.html#padding
    """
    #  qreal QQuickBasePositioner::padding() const
    return self.uglySide.call('ritual_ZNK20QQuickBasePositioner7paddingEv')

  def topPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickBasePositioner::topPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#topPadding
    """
    #  qreal QQuickBasePositioner::topPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickBasePositioner10topPaddingEv',
    )

  def leftPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickBasePositioner::leftPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#leftPadding
    """
    #  qreal QQuickBasePositioner::leftPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickBasePositioner11leftPaddingEv',
    )

  def rightPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickBasePositioner::rightPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#rightPadding
    """
    #  qreal QQuickBasePositioner::rightPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickBasePositioner12rightPaddingEv',
    )

  def bottomPadding(self) -> float:
    """
    Calls Qt's 'qreal QQuickBasePositioner::bottomPadding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#bottomPadding
    """
    #  qreal QQuickBasePositioner::bottomPadding() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickBasePositioner13bottomPaddingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setSpacing(self, a0: float) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::setSpacing(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#setSpacing

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQuickBasePositioner::setSpacing(qreal a0)
    self.uglySide.call('ritual_ZN20QQuickBasePositioner10setSpacingEd', a0)

  @overload(QQuickTransition)
  @overload(NoneType)
  def setPopulate(self, a0: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::setPopulate(QQuickTransition
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#setPopulate

    Parameters
    ----------

    a0 : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBasePositioner::setPopulate(QQuickTransition *a0)
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner11setPopulateEP16QQuickTransition',
        self._addressOf(a0),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setMove(self, a0: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::setMove(QQuickTransition *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasepositioner.html#setMove

    Parameters
    ----------

    a0 : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBasePositioner::setMove(QQuickTransition *a0)
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner7setMoveEP16QQuickTransition',
        self._addressOf(a0),
    )

  @overload(QQuickTransition)
  @overload(NoneType)
  def setAdd(self, a0: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::setAdd(QQuickTransition *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasepositioner.html#setAdd

    Parameters
    ----------

    a0 : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBasePositioner::setAdd(QQuickTransition *a0)
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner6setAddEP16QQuickTransition',
        self._addressOf(a0),
    )

  @overload(float)
  def setPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::setPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#setPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickBasePositioner::setPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner10setPaddingEd', padding,
    )

  @overload(float)
  def setTopPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::setTopPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#setTopPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickBasePositioner::setTopPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner13setTopPaddingEd', padding,
    )

  @overload(float)
  def setLeftPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::setLeftPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#setLeftPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickBasePositioner::setLeftPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner14setLeftPaddingEd', padding,
    )

  @overload(float)
  def setRightPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::setRightPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#setRightPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickBasePositioner::setRightPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner15setRightPaddingEd', padding,
    )

  @overload(float)
  def setBottomPadding(self, padding: float) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::setBottomPadding(qreal padding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#setBottomPadding

    Parameters
    ----------

    padding : float
      Passed on as it is.
    """
    #  void QQuickBasePositioner::setBottomPadding(qreal padding)
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner16setBottomPaddingEd', padding,
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

  @overload(PositionerType, QQuickItem)
  @overload(PositionerType, NoneType)
  def __init__(
      self,
      a0: PositionerType,
      parent: Optional[QQuickItem],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickBasePositioner::QQuickBasePositioner(PositionerType a0, QQuickItem
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#QQuickBasePositioner

    Parameters
    ----------

    a0 : PositionerType
      Passed on as its number.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickBasePositioner::QQuickBasePositioner(PositionerType a0,
    #      QQuickItem *parent)
    self._noteCreation(QQuickBasePositioner, lambda: Rituals.call(
        'ritual_ZN20QQuickBasePositionerC1ENS_14PositionerTypeEP10QQuickIte'
        'm',
        a0.value, self._addressOf(parent),
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

  @overload()
  @overload(QQuickPositionerAttached)
  @overload(NoneType)
  @overload(QQuickPositionerAttached, QQuickItem)
  @overload(QQuickPositionerAttached, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def updateAttachedProperties(
      self,
      specificProperty: Optional[QQuickPositionerAttached] = None,
      specificPropertyOwner: Optional[QQuickItem] = None,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickBasePositioner::updateAttachedProperties(QQuickPositionerAttached
    *specificProperty, QQuickItem *specificPropertyOwner) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#updateAttachedProperties

    Parameters
    ----------

    specificProperty : Optional[QQuickPositionerAttached]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    specificPropertyOwner : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickBasePositioner::updateAttachedProperties(
    #      QQuickPositionerAttached *specificProperty, QQuickItem
    #      *specificPropertyOwner) const
    self.uglySide.call(
        'ritual_ZNK20QQuickBasePositioner24updateAttachedPropertiesEP24QQui'
        'ckPositionerAttachedP10QQuickItem',
        self._addressOf(specificProperty),
        self._addressOf(specificPropertyOwner),
    )

  def resetPadding(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::resetPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#resetPadding
    """
    #  void QQuickBasePositioner::resetPadding()
    self.uglySide.call('ritual_ZN20QQuickBasePositioner12resetPaddingEv')

  def resetTopPadding(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::resetTopPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#resetTopPadding
    """
    #  void QQuickBasePositioner::resetTopPadding()
    self.uglySide.call('ritual_ZN20QQuickBasePositioner15resetTopPaddingEv')

  def resetLeftPadding(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::resetLeftPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#resetLeftPadding
    """
    #  void QQuickBasePositioner::resetLeftPadding()
    self.uglySide.call('ritual_ZN20QQuickBasePositioner16resetLeftPaddingEv')

  def resetRightPadding(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::resetRightPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#resetRightPadding
    """
    #  void QQuickBasePositioner::resetRightPadding()
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner17resetRightPaddingEv',
    )

  def resetBottomPadding(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::resetBottomPadding()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#resetBottomPadding
    """
    #  void QQuickBasePositioner::resetBottomPadding()
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner18resetBottomPaddingEv',
    )

  def forceLayout(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::forceLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#forceLayout
    """
    #  void QQuickBasePositioner::forceLayout()
    self.uglySide.call('ritual_ZN20QQuickBasePositioner11forceLayoutEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#componentComplete
    """
    #  void QQuickBasePositioner::componentComplete()
    ritual = 'ritual_ZN20QQuickBasePositioner17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickBasePositioner17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      a0: QQuickItem.ItemChange,
      a1: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#itemChange

    Parameters
    ----------

    a0 : QQuickItem.ItemChange
      Passed on as its number.

    a1 : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickBasePositioner::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    ritual = (
        'ritual_ZN20QQuickBasePositioner10itemChangeEN10QQuickItem10ItemCha'
        'ngeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickBasePositioner10itemChangeEN10QQuickItem10I'
          'temChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#updatePolish
    """
    #  void QQuickBasePositioner::updatePolish()
    ritual = 'ritual_ZN20QQuickBasePositioner12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickBasePositioner12updatePolishEv'
    self.uglySide.call(ritual)

  def spacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::spacingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#spacingChanged
    """
    #  void QQuickBasePositioner::spacingChanged()
    self.uglySide.call('ritual_ZN20QQuickBasePositioner14spacingChangedEv')

  def populateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::populateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#populateChanged
    """
    #  void QQuickBasePositioner::populateChanged()
    self.uglySide.call('ritual_ZN20QQuickBasePositioner15populateChangedEv')

  def moveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::moveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#moveChanged
    """
    #  void QQuickBasePositioner::moveChanged()
    self.uglySide.call('ritual_ZN20QQuickBasePositioner11moveChangedEv')

  def addChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::addChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#addChanged
    """
    #  void QQuickBasePositioner::addChanged()
    self.uglySide.call('ritual_ZN20QQuickBasePositioner10addChangedEv')

  def paddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::paddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#paddingChanged
    """
    #  void QQuickBasePositioner::paddingChanged()
    self.uglySide.call('ritual_ZN20QQuickBasePositioner14paddingChangedEv')

  def topPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::topPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#topPaddingChanged
    """
    #  void QQuickBasePositioner::topPaddingChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner17topPaddingChangedEv',
    )

  def leftPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::leftPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#leftPaddingChanged
    """
    #  void QQuickBasePositioner::leftPaddingChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner18leftPaddingChangedEv',
    )

  def rightPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::rightPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#rightPaddingChanged
    """
    #  void QQuickBasePositioner::rightPaddingChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner19rightPaddingChangedEv',
    )

  def bottomPaddingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::bottomPaddingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#bottomPaddingChanged
    """
    #  void QQuickBasePositioner::bottomPaddingChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner20bottomPaddingChangedEv',
    )

  def positioningComplete(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::positioningComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#positioningComplete
    """
    #  void QQuickBasePositioner::positioningComplete()
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner19positioningCompleteEv',
    )

  def prePositioning(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::prePositioning()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#prePositioning
    """
    #  void QQuickBasePositioner::prePositioning()
    self.uglySide.call('ritual_ZN20QQuickBasePositioner14prePositioningEv')

  @overload(QSizeF)
  @overload(NoneType)
  def doPositioning(self, contentSize: Optional[QSizeF]) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::doPositioning(QSizeF
    *contentSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#doPositioning

    Parameters
    ----------

    contentSize : Optional[QSizeF]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBasePositioner::doPositioning(QSizeF *contentSize)
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner13doPositioningEP6QSizeF',
        self._addressOf(contentSize),
    )

  def reportConflictingAnchors(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositioner::reportConflictingAnchors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositioner.html#reportConflictingAnchors
    """
    #  void QQuickBasePositioner::reportConflictingAnchors()
    self.uglySide.call(
        'ritual_ZN20QQuickBasePositioner24reportConflictingAnchorsEv',
    )

  def d_func(self) -> Optional[QQuickBasePositionerPrivate]:
    """
    Calls Qt's 'QQuickBasePositionerPrivate *QQuickBasePositioner::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbasepositioner.html#d_func

    Returns
    -------

    Optional[QQuickBasePositionerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickBasePositionerPrivate *QQuickBasePositioner::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickBasePositioner6d_funcEv')
    from . import QQuickBasePositionerPrivate
    return QQuickBasePositionerPrivate._cuteAt(address)

  @staticmethod
  def positionItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickBasePositioner::positionItem(qreal x, qreal y,
    PositionedItem *target)': names 'QQuickBasePositioner::PositionedItem',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickBasePositioner.positionItem' has no cute function yet. Qt's "
        "'void QQuickBasePositioner::positionItem(qreal x, qreal y, "
        "PositionedItem *target)': names "
        "'QQuickBasePositioner::PositionedItem', which has no cute class "
        "yet.")

  @staticmethod
  def positionItemX(*__, **_) -> Never:
    """
    Qt's 'void QQuickBasePositioner::positionItemX(qreal a0, PositionedItem
    *target)': names 'QQuickBasePositioner::PositionedItem', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickBasePositioner.positionItemX' has no cute function yet. "
        "Qt's 'void QQuickBasePositioner::positionItemX(qreal a0, "
        "PositionedItem *target)': names "
        "'QQuickBasePositioner::PositionedItem', which has no cute class "
        "yet.")

  @staticmethod
  def positionItemY(*__, **_) -> Never:
    """
    Qt's 'void QQuickBasePositioner::positionItemY(qreal a0, PositionedItem
    *target)': names 'QQuickBasePositioner::PositionedItem', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuickBasePositioner.positionItemY' has no cute function yet. "
        "Qt's 'void QQuickBasePositioner::positionItemY(qreal a0, "
        "PositionedItem *target)': names "
        "'QQuickBasePositioner::PositionedItem', which has no cute class "
        "yet.")
