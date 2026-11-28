"""
QQuickParentChange binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstateoperations_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickParentChange to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQuickStateActionEvent, QQuickStateOperation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QQmlScriptString
  from . import QQuickItem, QQuickStateAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlScriptString = WAIT['QQmlScriptString']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickParentChange(QQuickStateOperation, QQuickStateActionEvent):
  """
  The cute side of Qt's QQuickParentChange: a plain Python object standing in
  front of one C++ QQuickParentChange.

  It is built on the cute 'QQuickStateOperation', as Qt's QQuickParentChange
  is built on Qt's QQuickStateOperation, and has everything that class has.
  It is built on the cute 'QQuickStateActionEvent' as well, as Qt's
  QQuickParentChange is built on Qt's QQuickStateActionEvent too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickParentChange that has a ritual and that Python
  can call so far, 34 names in all: 'metaObject', 'tr', 'object',
  'setObject', 'parent', 'setParent', 'originalParent', 'x', 'setX',
  'xIsSet', 'y', 'setY', 'yIsSet', 'width', 'setWidth', 'widthIsSet',
  'height', 'setHeight', 'heightIsSet', 'scale', 'setScale', 'scaleIsSet',
  'rotation', 'setRotation', 'rotationIsSet', 'actions', 'saveOriginals',
  'execute', 'isReversable', 'reverse', 'type', 'mayOverride', 'rewind',
  'saveCurrentValues'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickParentChange::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickParentChange::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickParentChangePrivate *QQuickParentChange::d_func()': gives
    'QQuickParentChangePrivate', which has no cute class yet.
  - Qt's 'const QQuickParentChangePrivate *QQuickParentChange::d_func()
    const': gives 'QQuickParentChangePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 41 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickParentChange is created at the first use, not by
    'QQuickParentChange(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickParentChange.
  - Qt tells when it has removed the C++ QQuickParentChange. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickParentChange::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#tr

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
    #  QString QQuickParentChange::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickParentChange2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickParentChange'

  #  Qt's QQuickParentChange is built on more than one class. The part of a
  #  C++ QQuickParentChange that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickStateActionEvent':
          'ritual_cast_QQuickParentChange_QQuickStateActionEvent',
  }

  #  A C++ QQuickParentChange Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickParentChange'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickParentChange::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickParentChange::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickParentChange10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def object(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickParentChange::object() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#object

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickParentChange::object() const
    address = self.uglySide.call('ritual_ZNK18QQuickParentChange6objectEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def parent(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickParentChange::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#parent

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickParentChange::parent() const
    address = self.uglySide.call('ritual_ZNK18QQuickParentChange6parentEv')
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def originalParent(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickParentChange::originalParent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparentchange.html#originalParent

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickParentChange::originalParent() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickParentChange14originalParentEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def x(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickParentChange::x() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#x

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickParentChange::x() const
    address = self.uglySide.call('ritual_ZNK18QQuickParentChange1xEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def xIsSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickParentChange::xIsSet() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#xIsSet
    """
    #  bool QQuickParentChange::xIsSet() const
    return self.uglySide.call('ritual_ZNK18QQuickParentChange6xIsSetEv')

  def y(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickParentChange::y() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#y

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickParentChange::y() const
    address = self.uglySide.call('ritual_ZNK18QQuickParentChange1yEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def yIsSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickParentChange::yIsSet() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#yIsSet
    """
    #  bool QQuickParentChange::yIsSet() const
    return self.uglySide.call('ritual_ZNK18QQuickParentChange6yIsSetEv')

  def width(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickParentChange::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#width

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickParentChange::width() const
    address = self.uglySide.call('ritual_ZNK18QQuickParentChange5widthEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def widthIsSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickParentChange::widthIsSet() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#widthIsSet
    """
    #  bool QQuickParentChange::widthIsSet() const
    return self.uglySide.call('ritual_ZNK18QQuickParentChange10widthIsSetEv')

  def height(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickParentChange::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#height

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickParentChange::height() const
    address = self.uglySide.call('ritual_ZNK18QQuickParentChange6heightEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def heightIsSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickParentChange::heightIsSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparentchange.html#heightIsSet
    """
    #  bool QQuickParentChange::heightIsSet() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickParentChange11heightIsSetEv',
    )

  def scale(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickParentChange::scale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#scale

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickParentChange::scale() const
    address = self.uglySide.call('ritual_ZNK18QQuickParentChange5scaleEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def scaleIsSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickParentChange::scaleIsSet() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#scaleIsSet
    """
    #  bool QQuickParentChange::scaleIsSet() const
    return self.uglySide.call('ritual_ZNK18QQuickParentChange10scaleIsSetEv')

  def rotation(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickParentChange::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#rotation

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickParentChange::rotation() const
    address = self.uglySide.call('ritual_ZNK18QQuickParentChange8rotationEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def rotationIsSet(self) -> bool:
    """
    Calls Qt's 'bool QQuickParentChange::rotationIsSet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparentchange.html#rotationIsSet
    """
    #  bool QQuickParentChange::rotationIsSet() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickParentChange13rotationIsSetEv',
    )

  def type(self) -> QQuickStateActionEvent.EventType:
    """
    Calls Qt's 'EventType QQuickParentChange::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#type

    Returns
    -------

    QQuickStateActionEvent.EventType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickStateActionEvent.EventType(number)' gives.
    """
    #  EventType QQuickParentChange::type() const
    ritual = 'ritual_ZNK18QQuickParentChange4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QQuickParentChange4typeEv'
    return QQuickStateActionEvent.EventType(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem)
  @overload(NoneType)
  def setObject(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickParentChange::setObject(QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#setObject

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParentChange::setObject(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN18QQuickParentChange9setObjectEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setParent(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickParentChange::setParent(QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#setParent

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickParentChange::setParent(QQuickItem *a0)
    self.uglySide.call(
        'ritual_ZN18QQuickParentChange9setParentEP10QQuickItem',
        self._addressOf(a0),
    )

  @overload(QQmlScriptString)
  def setX(self, x: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickParentChange::setX(const QQmlScriptString &x)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#setX

    Parameters
    ----------

    x : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickParentChange::setX(const QQmlScriptString &x)
    self.uglySide.call(
        'ritual_ZN18QQuickParentChange4setXERK16QQmlScriptString',
        self._valueOf(x),
    )

  @overload(QQmlScriptString)
  def setY(self, y: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickParentChange::setY(const QQmlScriptString &y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#setY

    Parameters
    ----------

    y : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickParentChange::setY(const QQmlScriptString &y)
    self.uglySide.call(
        'ritual_ZN18QQuickParentChange4setYERK16QQmlScriptString',
        self._valueOf(y),
    )

  @overload(QQmlScriptString)
  def setWidth(self, width: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickParentChange::setWidth(const QQmlScriptString
    &width)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#setWidth

    Parameters
    ----------

    width : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickParentChange::setWidth(const QQmlScriptString &width)
    self.uglySide.call(
        'ritual_ZN18QQuickParentChange8setWidthERK16QQmlScriptString',
        self._valueOf(width),
    )

  @overload(QQmlScriptString)
  def setHeight(self, height: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickParentChange::setHeight(const QQmlScriptString
    &height)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#setHeight

    Parameters
    ----------

    height : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickParentChange::setHeight(const QQmlScriptString &height)
    self.uglySide.call(
        'ritual_ZN18QQuickParentChange9setHeightERK16QQmlScriptString',
        self._valueOf(height),
    )

  @overload(QQmlScriptString)
  def setScale(self, scale: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickParentChange::setScale(const QQmlScriptString
    &scale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#setScale

    Parameters
    ----------

    scale : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickParentChange::setScale(const QQmlScriptString &scale)
    self.uglySide.call(
        'ritual_ZN18QQuickParentChange8setScaleERK16QQmlScriptString',
        self._valueOf(scale),
    )

  @overload(QQmlScriptString)
  def setRotation(self, rotation: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickParentChange::setRotation(const QQmlScriptString
    &rotation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparentchange.html#setRotation

    Parameters
    ----------

    rotation : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickParentChange::setRotation(const QQmlScriptString &rotation)
    self.uglySide.call(
        'ritual_ZN18QQuickParentChange11setRotationERK16QQmlScriptString',
        self._valueOf(rotation),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickParentChange::QQuickParentChange(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparentchange.html#QQuickParentChange

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickParentChange::QQuickParentChange(QObject *parent)
    self._noteCreation(QQuickParentChange, lambda: Rituals.call(
        'ritual_ZN18QQuickParentChangeC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def actions(self) -> QList[QQuickStateAction]:
    """
    Calls Qt's 'ActionList QQuickParentChange::actions()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#actions

    Returns
    -------

    QList[QQuickStateAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  ActionList QQuickParentChange::actions()
    address = self.uglySide.call('ritual_ZN18QQuickParentChange7actionsEv')
    from . import QQuickStateAction
    return QList[QQuickStateAction]._cuteOwning(address)

  def saveOriginals(self) -> None:
    """
    Calls Qt's 'void QQuickParentChange::saveOriginals()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparentchange.html#saveOriginals
    """
    #  void QQuickParentChange::saveOriginals()
    ritual = 'ritual_ZN18QQuickParentChange13saveOriginalsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickParentChange13saveOriginalsEv'
    self.uglySide.call(ritual)

  def execute(self) -> None:
    """
    Calls Qt's 'void QQuickParentChange::execute()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#execute
    """
    #  void QQuickParentChange::execute()
    ritual = 'ritual_ZN18QQuickParentChange7executeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickParentChange7executeEv'
    self.uglySide.call(ritual)

  def isReversable(self) -> bool:
    """
    Calls Qt's 'bool QQuickParentChange::isReversable()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparentchange.html#isReversable
    """
    #  bool QQuickParentChange::isReversable()
    ritual = 'ritual_ZN18QQuickParentChange12isReversableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickParentChange12isReversableEv'
    return self.uglySide.call(ritual)

  def reverse(self) -> None:
    """
    Calls Qt's 'void QQuickParentChange::reverse()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#reverse
    """
    #  void QQuickParentChange::reverse()
    ritual = 'ritual_ZN18QQuickParentChange7reverseEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickParentChange7reverseEv'
    self.uglySide.call(ritual)

  @overload(QQuickStateActionEvent)
  @overload(NoneType)
  def mayOverride(self, other: Optional[QQuickStateActionEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickParentChange::mayOverride(QQuickStateActionEvent
    *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparentchange.html#mayOverride

    Parameters
    ----------

    other : Optional[QQuickStateActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickParentChange::mayOverride(QQuickStateActionEvent *other)
    ritual = (
        'ritual_ZN18QQuickParentChange11mayOverrideEP22QQuickStateActionEve'
        'nt')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickParentChange11mayOverrideEP22QQuickStateAct'
          'ionEvent')
    return self.uglySide.call(
        ritual, self._addressOf(other, 'QQuickStateActionEvent'),
    )

  def rewind(self) -> None:
    """
    Calls Qt's 'void QQuickParentChange::rewind()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickparentchange.html#rewind
    """
    #  void QQuickParentChange::rewind()
    ritual = 'ritual_ZN18QQuickParentChange6rewindEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickParentChange6rewindEv'
    self.uglySide.call(ritual)

  def saveCurrentValues(self) -> None:
    """
    Calls Qt's 'void QQuickParentChange::saveCurrentValues()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickparentchange.html#saveCurrentValues
    """
    #  void QQuickParentChange::saveCurrentValues()
    ritual = 'ritual_ZN18QQuickParentChange17saveCurrentValuesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickParentChange17saveCurrentValuesEv'
    self.uglySide.call(ritual)
