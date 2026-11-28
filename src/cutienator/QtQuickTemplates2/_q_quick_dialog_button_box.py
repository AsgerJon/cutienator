"""
QQuickDialogButtonBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickDialogButtonBox to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QAccessible, QPlatformDialogHelper
from ..QtQuick import QQuickItem
from . import QQuickContainer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF
  from ..QtQml import QQmlComponent
  from . import QQuickAbstractButton, QQuickDialogButtonBoxAttached
  from . import QQuickDialogButtonBoxPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickAbstractButton = WAIT['QQuickAbstractButton']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDialogButtonBox(QQuickContainer):
  """
  The cute side of Qt's QQuickDialogButtonBox: a plain Python object standing
  in front of one C++ QQuickDialogButtonBox.

  It is built on the cute 'QQuickContainer', as Qt's QQuickDialogButtonBox is
  built on Qt's QQuickContainer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDialogButtonBox that has a ritual and that
  Python can call so far, 46 names in all: 'metaObject', 'tr',
  'qmlExtendedNamespace', 'position', 'setPosition', 'alignment',
  'setAlignment', 'resetAlignment', 'standardButtons', 'setStandardButtons',
  'standardButton', 'defaultStandardButton', 'setDefaultStandardButton',
  'defaultButton', 'setDefaultButton', 'delegate', 'setDelegate',
  'qmlAttachedProperties', 'buttonLayout', 'setButtonLayout',
  'resetButtonLayout', 'accepted', 'rejected', 'helpRequested', 'clicked',
  'positionChanged', 'alignmentChanged', 'standardButtonsChanged',
  'delegateChanged', 'applied', 'reset', 'discarded', 'buttonLayoutChanged',
  'defaultStandardButtonChanged', 'defaultButtonChanged', 'updatePolish',
  'componentComplete', 'geometryChange', 'contentItemChange', 'isContent',
  'itemAdded', 'itemRemoved', 'accessibleRole', 'event', 'itemChange',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDialogButtonBox::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickDialogButtonBox::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickDialogButtonBox::qt_qmlMarker_attached()': one of Qt's
    own inner workings.
  - Qt's 'void QQuickDialogButtonBox::qt_qmlMarker_extendedNamespace()': one
    of Qt's own inner workings.
  - Qt's 'QQuickDialogButtonBox::~QQuickDialogButtonBox()': the destructor:
    Python never removes a C++ QQuickDialogButtonBox.
  - Qt's 'const QQuickDialogButtonBoxPrivate *QQuickDialogButtonBox::d_func()
    const': takes in Python what 'QQuickDialogButtonBoxPrivate
    *QQuickDialogButtonBox::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 57 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickDialogButtonBox is created at the first use, not by
    'QQuickDialogButtonBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDialogButtonBox.
  - Qt tells when it has removed the C++ QQuickDialogButtonBox. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickDialogButtonBox, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Position(CuteNum):
    """
    The enum 'QQuickDialogButtonBox::Position' of Qt, with the 2 names Qt
    gives in it.
    """

    Header = Kee[int](0)
    Footer = Kee[int](1)

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
    Calls Qt's 'QString QQuickDialogButtonBox::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#tr

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
    #  QString QQuickDialogButtonBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickDialogButtonBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickDialogButtonBox::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDialogButtonBox::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN21QQuickDialogButtonBox20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickDialogButtonBoxAttached]:
    """
    Calls Qt's 'QQuickDialogButtonBoxAttached
    *QQuickDialogButtonBox::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickDialogButtonBoxAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogButtonBoxAttached
    #      *QQuickDialogButtonBox::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN21QQuickDialogButtonBox21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickDialogButtonBoxAttached
    return QQuickDialogButtonBoxAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDialogButtonBox'

  #  A C++ QQuickDialogButtonBox Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDialogButtonBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDialogButtonBox::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDialogButtonBox::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickDialogButtonBox10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> Position:
    """
    Calls Qt's 'Position QQuickDialogButtonBox::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#position

    Returns
    -------

    Position
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Position(number)' gives.
    """
    #  Position QQuickDialogButtonBox::position() const
    return QQuickDialogButtonBox.Position(self.uglySide.call(
        'ritual_ZNK21QQuickDialogButtonBox8positionEv',
    ))

  def alignment(self) -> Qt.Alignment:
    """
    Calls Qt's 'Qt::Alignment QQuickDialogButtonBox::alignment() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#alignment

    Returns
    -------

    Qt.Alignment
      The value standing for the combination Qt gave back.
    """
    #  Qt::Alignment QQuickDialogButtonBox::alignment() const
    return Qt.Alignment(self.uglySide.call(
        'ritual_ZNK21QQuickDialogButtonBox9alignmentEv',
    ))

  def standardButtons(self) -> QPlatformDialogHelper.StandardButtons:
    """
    Calls Qt's 'QPlatformDialogHelper::StandardButtons
    QQuickDialogButtonBox::standardButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#standardButtons

    Returns
    -------

    QPlatformDialogHelper.StandardButtons
      The value standing for the combination Qt gave back.
    """
    #  QPlatformDialogHelper::StandardButtons
    #      QQuickDialogButtonBox::standardButtons() const
    return QPlatformDialogHelper.StandardButtons(self.uglySide.call(
        'ritual_ZNK21QQuickDialogButtonBox15standardButtonsEv',
    ))

  @overload(QPlatformDialogHelper.StandardButton)
  def standardButton(
      self,
      button: QPlatformDialogHelper.StandardButton,
  ) -> Optional[QQuickAbstractButton]:
    """
    Calls Qt's 'QQuickAbstractButton
    *QQuickDialogButtonBox::standardButton(QPlatformDialogHelper::
    StandardButton button) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#standardButton

    Parameters
    ----------

    button : QPlatformDialogHelper.StandardButton
      Passed on as its number.

    Returns
    -------

    Optional[QQuickAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractButton
    #      *QQuickDialogButtonBox::standardButton(QPlatformDialogHelper::
    #      StandardButton button) const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickDialogButtonBox14standardButtonEN21QPlatformDial'
        'ogHelper14StandardButtonE',
        button.value,
    )
    from . import QQuickAbstractButton
    return QQuickAbstractButton._cuteAt(address)

  def defaultStandardButton(self) -> QPlatformDialogHelper.StandardButton:
    """
    Calls Qt's 'QPlatformDialogHelper::StandardButton
    QQuickDialogButtonBox::defaultStandardButton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#defaultStandardButton

    Returns
    -------

    QPlatformDialogHelper.StandardButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPlatformDialogHelper.StandardButton(number)' gives.
    """
    #  QPlatformDialogHelper::StandardButton
    #      QQuickDialogButtonBox::defaultStandardButton() const
    return QPlatformDialogHelper.StandardButton(self.uglySide.call(
        'ritual_ZNK21QQuickDialogButtonBox21defaultStandardButtonEv',
    ))

  def defaultButton(self) -> Optional[QQuickAbstractButton]:
    """
    Calls Qt's 'QQuickAbstractButton *QQuickDialogButtonBox::defaultButton()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#defaultButton

    Returns
    -------

    Optional[QQuickAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAbstractButton *QQuickDialogButtonBox::defaultButton() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickDialogButtonBox13defaultButtonEv',
    )
    from . import QQuickAbstractButton
    return QQuickAbstractButton._cuteAt(address)

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickDialogButtonBox::delegate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickDialogButtonBox::delegate() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickDialogButtonBox8delegateEv',
    )
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def buttonLayout(self) -> QPlatformDialogHelper.ButtonLayout:
    """
    Calls Qt's 'QPlatformDialogHelper::ButtonLayout
    QQuickDialogButtonBox::buttonLayout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#buttonLayout

    Returns
    -------

    QPlatformDialogHelper.ButtonLayout
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPlatformDialogHelper.ButtonLayout(number)' gives.
    """
    #  QPlatformDialogHelper::ButtonLayout
    #      QQuickDialogButtonBox::buttonLayout() const
    return QPlatformDialogHelper.ButtonLayout(self.uglySide.call(
        'ritual_ZNK21QQuickDialogButtonBox12buttonLayoutEv',
    ))

  @overload(QQuickItem)
  @overload(NoneType)
  def isContent(self, item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickDialogButtonBox::isContent(QQuickItem *item)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#isContent

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDialogButtonBox::isContent(QQuickItem *item) const
    ritual = 'ritual_ZNK21QQuickDialogButtonBox9isContentEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QQuickDialogButtonBox9isContentEP10QQuickItem')
    return self.uglySide.call(ritual, self._addressOf(item))

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickDialogButtonBox::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickDialogButtonBox::accessibleRole() const
    ritual = 'ritual_ZNK21QQuickDialogButtonBox14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickDialogButtonBox14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Position)
  def setPosition(self, position: Position) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::setPosition(Position position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#setPosition

    Parameters
    ----------

    position : Position
      Passed on as its number.
    """
    #  void QQuickDialogButtonBox::setPosition(Position position)
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox11setPositionENS_8PositionE',
        position.value,
    )

  @overload(Qt.Alignment)
  def setAlignment(self, alignment: Qt.Alignment) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::setAlignment(Qt::Alignment
    alignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#setAlignment

    Parameters
    ----------

    alignment : Qt.Alignment
      Passed on as its number.
    """
    #  void QQuickDialogButtonBox::setAlignment(Qt::Alignment alignment)
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox12setAlignmentE6QFlagsIN2Qt13Align'
        'mentFlagEE',
        alignment.value,
    )

  @overload(QPlatformDialogHelper.StandardButtons)
  def setStandardButtons(
      self,
      buttons: QPlatformDialogHelper.StandardButtons,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDialogButtonBox::setStandardButtons(QPlatformDialogHelper::
    StandardButtons buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#setStandardButtons

    Parameters
    ----------

    buttons : QPlatformDialogHelper.StandardButtons
      Passed on as its number.
    """
    #  void QQuickDialogButtonBox::setStandardButtons(QPlatformDialogHelper::
    #      StandardButtons buttons)
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox18setStandardButtonsE6QFlagsIN21QP'
        'latformDialogHelper14StandardButtonEE',
        buttons.value,
    )

  @overload(QPlatformDialogHelper.StandardButton)
  def setDefaultStandardButton(
      self,
      button: QPlatformDialogHelper.StandardButton,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDialogButtonBox::setDefaultStandardButton(QPlatformDialogHelper::
    StandardButton button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html

    Parameters
    ----------

    button : QPlatformDialogHelper.StandardButton
      Passed on as its number.
    """
    #  void QQuickDialogButtonBox::setDefaultStandardButton(
    #      QPlatformDialogHelper::StandardButton button)
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox24setDefaultStandardButtonEN21QPla'
        'tformDialogHelper14StandardButtonE',
        button.value,
    )

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def setDefaultButton(self, button: Optional[QQuickAbstractButton]) -> None:
    """
    Calls Qt's 'void
    QQuickDialogButtonBox::setDefaultButton(QQuickAbstractButton *button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#setDefaultButton

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDialogButtonBox::setDefaultButton(QQuickAbstractButton
    #      *button)
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox16setDefaultButtonEP20QQuickAbstra'
        'ctButton',
        self._addressOf(button),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::setDelegate(QQmlComponent
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDialogButtonBox::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox11setDelegateEP13QQmlComponent',
        self._addressOf(delegate),
    )

  @overload(QPlatformDialogHelper.ButtonLayout)
  def setButtonLayout(
      self,
      layout: QPlatformDialogHelper.ButtonLayout,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickDialogButtonBox::setButtonLayout(QPlatformDialogHelper::
    ButtonLayout layout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#setButtonLayout

    Parameters
    ----------

    layout : QPlatformDialogHelper.ButtonLayout
      Passed on as its number.
    """
    #  void QQuickDialogButtonBox::setButtonLayout(QPlatformDialogHelper::
    #      ButtonLayout layout)
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox15setButtonLayoutEN21QPlatformDial'
        'ogHelper12ButtonLayoutE',
        layout.value,
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
    'QQuickDialogButtonBox::QQuickDialogButtonBox(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#QQuickDialogButtonBox

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickDialogButtonBox::QQuickDialogButtonBox(QQuickItem *parent)
    self._noteCreation(QQuickDialogButtonBox, lambda: Rituals.call(
        'ritual_ZN21QQuickDialogButtonBoxC1EP10QQuickItem',
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

  def resetAlignment(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::resetAlignment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#resetAlignment
    """
    #  void QQuickDialogButtonBox::resetAlignment()
    self.uglySide.call('ritual_ZN21QQuickDialogButtonBox14resetAlignmentEv')

  def resetButtonLayout(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::resetButtonLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#resetButtonLayout
    """
    #  void QQuickDialogButtonBox::resetButtonLayout()
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox17resetButtonLayoutEv',
    )

  def accepted(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::accepted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#accepted
    """
    #  void QQuickDialogButtonBox::accepted()
    self.uglySide.call('ritual_ZN21QQuickDialogButtonBox8acceptedEv')

  def rejected(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::rejected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#rejected
    """
    #  void QQuickDialogButtonBox::rejected()
    self.uglySide.call('ritual_ZN21QQuickDialogButtonBox8rejectedEv')

  def helpRequested(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::helpRequested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#helpRequested
    """
    #  void QQuickDialogButtonBox::helpRequested()
    self.uglySide.call('ritual_ZN21QQuickDialogButtonBox13helpRequestedEv')

  @overload(QQuickAbstractButton)
  @overload(NoneType)
  def clicked(self, button: Optional[QQuickAbstractButton]) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::clicked(QQuickAbstractButton
    *button)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#clicked

    Parameters
    ----------

    button : Optional[QQuickAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDialogButtonBox::clicked(QQuickAbstractButton *button)
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox7clickedEP20QQuickAbstractButton',
        self._addressOf(button),
    )

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#positionChanged
    """
    #  void QQuickDialogButtonBox::positionChanged()
    self.uglySide.call('ritual_ZN21QQuickDialogButtonBox15positionChangedEv')

  def alignmentChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::alignmentChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#alignmentChanged
    """
    #  void QQuickDialogButtonBox::alignmentChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox16alignmentChangedEv',
    )

  def standardButtonsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::standardButtonsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#standardButtonsChanged
    """
    #  void QQuickDialogButtonBox::standardButtonsChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox22standardButtonsChangedEv',
    )

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#delegateChanged
    """
    #  void QQuickDialogButtonBox::delegateChanged()
    self.uglySide.call('ritual_ZN21QQuickDialogButtonBox15delegateChangedEv')

  def applied(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::applied()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#applied
    """
    #  void QQuickDialogButtonBox::applied()
    self.uglySide.call('ritual_ZN21QQuickDialogButtonBox7appliedEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#reset
    """
    #  void QQuickDialogButtonBox::reset()
    self.uglySide.call('ritual_ZN21QQuickDialogButtonBox5resetEv')

  def discarded(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::discarded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#discarded
    """
    #  void QQuickDialogButtonBox::discarded()
    self.uglySide.call('ritual_ZN21QQuickDialogButtonBox9discardedEv')

  def buttonLayoutChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::buttonLayoutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#buttonLayoutChanged
    """
    #  void QQuickDialogButtonBox::buttonLayoutChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox19buttonLayoutChangedEv',
    )

  def defaultStandardButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::defaultStandardButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html
    """
    #  void QQuickDialogButtonBox::defaultStandardButtonChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox28defaultStandardButtonChangedEv',
    )

  def defaultButtonChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::defaultButtonChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#defaultButtonChanged
    """
    #  void QQuickDialogButtonBox::defaultButtonChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickDialogButtonBox20defaultButtonChangedEv',
    )

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#updatePolish
    """
    #  void QQuickDialogButtonBox::updatePolish()
    ritual = 'ritual_ZN21QQuickDialogButtonBox12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickDialogButtonBox12updatePolishEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#componentComplete
    """
    #  void QQuickDialogButtonBox::componentComplete()
    ritual = 'ritual_ZN21QQuickDialogButtonBox17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickDialogButtonBox17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickDialogButtonBox::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN21QQuickDialogButtonBox14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickDialogButtonBox14geometryChangeERK6QRectFS2'
          '_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

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
    Calls Qt's 'void QQuickDialogButtonBox::contentItemChange(QQuickItem
    *newItem, QQuickItem *oldItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDialogButtonBox::contentItemChange(QQuickItem *newItem,
    #      QQuickItem *oldItem)
    ritual = (
        'ritual_ZN21QQuickDialogButtonBox17contentItemChangeEP10QQuickItemS'
        '1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickDialogButtonBox17contentItemChangeEP10QQuic'
          'kItemS1_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemAdded(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::itemAdded(int index, QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#itemAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDialogButtonBox::itemAdded(int index, QQuickItem *item)
    ritual = 'ritual_ZN21QQuickDialogButtonBox9itemAddedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickDialogButtonBox9itemAddedEiP10QQuickItem')
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemRemoved(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::itemRemoved(int index, QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#itemRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDialogButtonBox::itemRemoved(int index, QQuickItem *item)
    ritual = 'ritual_ZN21QQuickDialogButtonBox11itemRemovedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickDialogButtonBox11itemRemovedEiP10QQuickItem')
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDialogButtonBox::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDialogButtonBox::event(QEvent *e)
    ritual = 'ritual_ZN21QQuickDialogButtonBox5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickDialogButtonBox5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBox::itemChange(QQuickItem::ItemChange
    change, const QQuickItem::ItemChangeData &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickDialogButtonBox::itemChange(QQuickItem::ItemChange change,
    #      const QQuickItem::ItemChangeData &data)
    ritual = (
        'ritual_ZN21QQuickDialogButtonBox10itemChangeEN10QQuickItem10ItemCh'
        'angeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickDialogButtonBox10itemChangeEN10QQuickItem10'
          'ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  def d_func(self) -> Optional[QQuickDialogButtonBoxPrivate]:
    """
    Calls Qt's 'QQuickDialogButtonBoxPrivate
    *QQuickDialogButtonBox::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdialogbuttonbox.html#d_func

    Returns
    -------

    Optional[QQuickDialogButtonBoxPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogButtonBoxPrivate *QQuickDialogButtonBox::d_func()
    address = self.uglySide.call('ritual_ZN21QQuickDialogButtonBox6d_funcEv')
    from . import QQuickDialogButtonBoxPrivate
    return QQuickDialogButtonBoxPrivate._cuteAt(address)
