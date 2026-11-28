"""
QQuickButtonGroup binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickbuttongroup_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickButtonGroup to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickAbstractButton, QQuickButtonGroupAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickAbstractButton = WAIT['QQuickAbstractButton']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickButtonGroup(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickButtonGroup: a plain Python object standing in
  front of one C++ QQuickButtonGroup.

  It is built on the cute 'QObject', as Qt's QQuickButtonGroup is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickButtonGroup is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickButtonGroup that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'checkedButton', 'setCheckedButton',
  'isExclusive', 'setExclusive', 'checkState', 'setCheckState', 'addButton',
  'removeButton', 'checkedButtonChanged', 'buttonsChanged', 'clicked',
  'exclusiveChanged', 'checkStateChanged', 'classBegin', 'componentComplete'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickButtonGroup::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickButtonGroup::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickButtonGroup::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickButtonGroup::~QQuickButtonGroup()': the destructor: Python
    never removes a C++ QQuickButtonGroup.
  - Qt's 'QQmlListProperty<QQuickAbstractButton>
    QQuickButtonGroup::buttons()': gives a type Python has no way to take
    yet.
  - Qt's 'QQuickButtonGroupPrivate *QQuickButtonGroup::d_func()': gives
    'QQuickButtonGroupPrivate', which has no cute class yet.
  - Qt's 'const QQuickButtonGroupPrivate *QQuickButtonGroup::d_func() const':
    gives 'QQuickButtonGroupPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 30 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickButtonGroup is created at the first use, not by
    'QQuickButtonGroup(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickButtonGroup.
  - Qt tells when it has removed the C++ QQuickButtonGroup. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickButtonGroup that has no cute function yet,
    'buttons', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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
    Calls Qt's 'QString QQuickButtonGroup::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbuttongroup.html#tr

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
    #  QString QQuickButtonGroup::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickButtonGroup2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickButtonGroupAttached]:
    """
    Calls Qt's 'QQuickButtonGroupAttached
    *QQuickButtonGroup::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbuttongroup.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickButtonGroupAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickButtonGroupAttached
    #      *QQuickButtonGroup::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN17QQuickButtonGroup21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickButtonGroupAttached
    return QQuickButtonGroupAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickButtonGroup'

  #  Qt's QQuickButtonGroup is built on more than one class. The part of a
  #  C++ QQuickButtonGroup that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickButtonGroup_QQmlParserStatus',
  }

  #  A C++ QQuickButtonGroup Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickButtonGroup'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickButtonGroup::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbuttongroup.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickButtonGroup::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickButtonGroup10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def checkedButton(self) -> Optional[QQuickAbstractButton]:
    """
    Calls Qt's 'QQuickAbstractButton *QQuickButtonGroup::checkedButton()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbuttongroup.html#checkedButton

    Returns
    -------

    Optional[QQuickAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractButton *QQuickButtonGroup::checkedButton() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickButtonGroup13checkedButtonEv',
    )
    from . import QQuickAbstractButton
    return QQuickAbstractButton._cuteAt(address)

  def isExclusive(self) -> bool:
    """
    Calls Qt's 'bool QQuickButtonGroup::isExclusive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbuttongroup.html#isExclusive
    """
    #  bool QQuickButtonGroup::isExclusive() const
    return self.uglySide.call('ritual_ZNK17QQuickButtonGroup11isExclusiveEv')

  def checkState(self) -> Qt.CheckState:
    """
    Calls Qt's 'Qt::CheckState QQuickButtonGroup::checkState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbuttongroup.html#checkState

    Returns
    -------

    Qt.CheckState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CheckState(number)'
      gives.
    """
    #  Qt::CheckState QQuickButtonGroup::checkState() const
    return Qt.CheckState(self.uglySide.call(
        'ritual_ZNK17QQuickButtonGroup10checkStateEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def setCheckedButton(
      self,
      checkedButton: Optional[QQuickAbstractButton],
  ) -> None:
    """
    Calls Qt's 'void QQuickButtonGroup::setCheckedButton(QQuickAbstractButton
    *checkedButton)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbuttongroup.html#setCheckedButton

    Parameters
    ----------

    checkedButton : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickButtonGroup::setCheckedButton(QQuickAbstractButton
    #      *checkedButton)
    self.uglySide.call(
        'ritual_ZN17QQuickButtonGroup16setCheckedButtonEP20QQuickAbstractBu'
        'tton',
        self._addressOf(checkedButton),
    )

  @overload(bool)
  def setExclusive(self, exclusive: bool) -> None:
    """
    Calls Qt's 'void QQuickButtonGroup::setExclusive(bool exclusive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbuttongroup.html#setExclusive

    Parameters
    ----------

    exclusive : bool
      Passed on as it is.
    """
    #  void QQuickButtonGroup::setExclusive(bool exclusive)
    self.uglySide.call(
        'ritual_ZN17QQuickButtonGroup12setExclusiveEb', exclusive,
    )

  @overload(Qt.CheckState)
  def setCheckState(self, state: Qt.CheckState) -> None:
    """
    Calls Qt's 'void QQuickButtonGroup::setCheckState(Qt::CheckState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbuttongroup.html#setCheckState

    Parameters
    ----------

    state : Qt.CheckState
      Passed on as its number.
    """
    #  void QQuickButtonGroup::setCheckState(Qt::CheckState state)
    self.uglySide.call(
        'ritual_ZN17QQuickButtonGroup13setCheckStateEN2Qt10CheckStateE',
        state.value,
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
    'QQuickButtonGroup::QQuickButtonGroup(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbuttongroup.html#QQuickButtonGroup

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickButtonGroup::QQuickButtonGroup(QObject *parent)
    self._noteCreation(QQuickButtonGroup, lambda: Rituals.call(
        'ritual_ZN17QQuickButtonGroupC1EP7QObject',
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

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def addButton(self, button: Optional[QQuickAbstractButton]) -> None:
    """
    Calls Qt's 'void QQuickButtonGroup::addButton(QQuickAbstractButton
    *button)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbuttongroup.html#addButton

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickButtonGroup::addButton(QQuickAbstractButton *button)
    self.uglySide.call(
        'ritual_ZN17QQuickButtonGroup9addButtonEP20QQuickAbstractButton',
        self._addressOf(button),
    )

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def removeButton(self, button: Optional[QQuickAbstractButton]) -> None:
    """
    Calls Qt's 'void QQuickButtonGroup::removeButton(QQuickAbstractButton
    *button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbuttongroup.html#removeButton

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickButtonGroup::removeButton(QQuickAbstractButton *button)
    self.uglySide.call(
        'ritual_ZN17QQuickButtonGroup12removeButtonEP20QQuickAbstractButton',
        self._addressOf(button),
    )

  def checkedButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQuickButtonGroup::checkedButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbuttongroup.html#checkedButtonChanged
    """
    #  void QQuickButtonGroup::checkedButtonChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickButtonGroup20checkedButtonChangedEv',
    )

  def buttonsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickButtonGroup::buttonsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbuttongroup.html#buttonsChanged
    """
    #  void QQuickButtonGroup::buttonsChanged()
    self.uglySide.call('ritual_ZN17QQuickButtonGroup14buttonsChangedEv')

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def clicked(self, button: Optional[QQuickAbstractButton]) -> None:
    """
    Calls Qt's 'void QQuickButtonGroup::clicked(QQuickAbstractButton
    *button)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbuttongroup.html#clicked

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickButtonGroup::clicked(QQuickAbstractButton *button)
    self.uglySide.call(
        'ritual_ZN17QQuickButtonGroup7clickedEP20QQuickAbstractButton',
        self._addressOf(button),
    )

  def exclusiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickButtonGroup::exclusiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbuttongroup.html#exclusiveChanged
    """
    #  void QQuickButtonGroup::exclusiveChanged()
    self.uglySide.call('ritual_ZN17QQuickButtonGroup16exclusiveChangedEv')

  def checkStateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickButtonGroup::checkStateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbuttongroup.html#checkStateChanged
    """
    #  void QQuickButtonGroup::checkStateChanged()
    self.uglySide.call('ritual_ZN17QQuickButtonGroup17checkStateChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickButtonGroup::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickbuttongroup.html#classBegin
    """
    #  void QQuickButtonGroup::classBegin()
    ritual = 'ritual_ZN17QQuickButtonGroup10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickButtonGroup10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickButtonGroup::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbuttongroup.html#componentComplete
    """
    #  void QQuickButtonGroup::componentComplete()
    ritual = 'ritual_ZN17QQuickButtonGroup17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickButtonGroup17componentCompleteEv'
    self.uglySide.call(ritual)

  @staticmethod
  def buttons(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickAbstractButton>
    QQuickButtonGroup::buttons()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQuickButtonGroup.buttons' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickAbstractButton> "
        "QQuickButtonGroup::buttons()': gives a type Python has no way to "
        "take yet.")
