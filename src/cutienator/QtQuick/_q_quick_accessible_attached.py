"""
QQuickAccessibleAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickaccessibleattached_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickAccessibleAttached to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QAccessible

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAccessibleAttached(QObject):
  """
  The cute side of Qt's QQuickAccessibleAttached: a plain Python object
  standing in front of one C++ QQuickAccessibleAttached.

  It is built on the cute 'QObject', as Qt's QQuickAccessibleAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAccessibleAttached that has a ritual and that
  Python can call so far, 87 names in all: 'metaObject', 'tr',
  'qmlExtendedNamespace', 'checkable', 'set_checkable', 'checked',
  'set_checked', 'editable', 'set_editable', 'expandable', 'set_expandable',
  'expanded', 'set_expanded', 'focusable', 'set_focusable', 'focused',
  'set_focused', 'multiLine', 'set_multiLine', 'readOnly', 'set_readOnly',
  'selected', 'set_selected', 'selectable', 'set_selectable', 'pressed',
  'set_pressed', 'checkStateMixed', 'set_checkStateMixed', 'defaultButton',
  'set_defaultButton', 'passwordEdit', 'set_passwordEdit', 'selectableText',
  'set_selectableText', 'searchEdit', 'set_searchEdit', 'role', 'setRole',
  'name', 'wasNameExplicitlySet', 'setName', 'setNameImplicitly',
  'description', 'setDescription', 'setDescriptionImplicitly', 'id', 'setId',
  'labelledBy', 'setLabelledBy', 'setLabelledByInternal', 'labelFor',
  'setLabelFor', 'setLabelForInternal', 'qmlAttachedProperties',
  'attachedProperties', 'property', 'setProperty', 'findAccessible', 'state',
  'ignored', 'doAction', 'stripHtml', 'setProxying', 'announce',
  'valueChanged', 'cursorPositionChanged', 'setIgnored', 'roleChanged',
  'nameChanged', 'descriptionChanged', 'idChanged', 'ignoredChanged',
  'labelledByChanged', 'labelForChanged', 'pressAction', 'toggleAction',
  'increaseAction', 'decreaseAction', 'showOnScreenAction', 'scrollUpAction',
  'scrollDownAction', 'scrollLeftAction', 'scrollRightAction',
  'previousPageAction', 'nextPageAction', 'findRelation'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAccessibleAttached::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickAccessibleAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickAccessibleAttached::qt_qmlMarker_uncreatable()': one of
    Qt's own inner workings.
  - Qt's 'void QQuickAccessibleAttached::qt_qmlMarker_attached()': one of
    Qt's own inner workings.
  - Qt's 'void QQuickAccessibleAttached::qt_qmlMarker_extendedNamespace()':
    one of Qt's own inner workings.
  - Qt's 'QQuickAccessibleAttached::~QQuickAccessibleAttached()': the
    destructor: Python never removes a C++ QQuickAccessibleAttached.
  - Qt's 'void QQuickAccessibleAttached::availableActions(QStringList
    *actions) const': names 'QStringList', which has no cute class yet.

  What has no ritual
  ------------------

  19 of the 114 functions Qt declares: 17 cannot be called and cannot be
  called through the meta-object and cannot be copied; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAccessibleAttached is created at the first use, not by
    'QQuickAccessibleAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAccessibleAttached.
  - Qt tells when it has removed the C++ QQuickAccessibleAttached. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickAccessibleAttached that has no cute function yet,
    'availableActions', 'checkStateMixedChanged', 'checkableChanged',
    'checkedChanged', 'defaultButtonChanged', 'editableChanged',
    'expandableChanged', 'expandedChanged', 'focusableChanged',
    'focusedChanged', 'multiLineChanged', 'passwordEditChanged',
    'pressedChanged', 'readOnlyChanged', 'searchEditChanged',
    'selectableChanged', 'selectableTextChanged', 'selectedChanged', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickAccessibleAttached::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaccessibleattached.html#tr

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
    #  QString QQuickAccessibleAttached::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuickAccessibleAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickAccessibleAttached::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAccessibleAttached::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN24QQuickAccessibleAttached20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      obj: Optional[QObject],
  ) -> Optional[QQuickAccessibleAttached]:
    """
    Calls Qt's 'QQuickAccessibleAttached
    *QQuickAccessibleAttached::qmlAttachedProperties(QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickAccessibleAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAccessibleAttached
    #      *QQuickAccessibleAttached::qmlAttachedProperties(QObject *obj)
    address = Rituals.call(
        'ritual_ZN24QQuickAccessibleAttached21qmlAttachedPropertiesEP7QObje'
        'ct',
        CuteMixin._addressOf(obj, 'QObject'),
    )
    return QQuickAccessibleAttached._cuteAt(address)

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def attachedProperties(
      obj: Optional[QObject],
  ) -> Optional[QQuickAccessibleAttached]:
    """
    Calls Qt's 'QQuickAccessibleAttached
    *QQuickAccessibleAttached::attachedProperties(const QObject *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#attachedProperties

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickAccessibleAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAccessibleAttached
    #      *QQuickAccessibleAttached::attachedProperties(const QObject *obj)
    address = Rituals.call(
        'ritual_ZN24QQuickAccessibleAttached18attachedPropertiesEPK7QObject',
        CuteMixin._addressOf(obj, 'QObject'),
    )
    return QQuickAccessibleAttached._cuteAt(address)

  @staticmethod
  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def property(
      object: Optional[QObject],
      propertyName: Optional[str],
  ) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickAccessibleAttached::property(const QObject
    *object, const char *propertyName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#property

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickAccessibleAttached::property(const QObject *object,
    #      const char *propertyName)
    address = Rituals.call(
        'ritual_ZN24QQuickAccessibleAttached8propertyEPK7QObjectPKc',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._bytesOf(propertyName),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(QObject, str, QVariant)
  @overload(QObject, NoneType, QVariant)
  @overload(NoneType, str, QVariant)
  @overload(NoneType, NoneType, QVariant)
  def setProperty(
      object: Optional[QObject],
      propertyName: Optional[str],
      value: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::setProperty(QObject *object,
    const char *propertyName, const QVariant &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#setProperty

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    propertyName : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQuickAccessibleAttached::setProperty(QObject *object, const char
    #      *propertyName, const QVariant &value)
    return Rituals.call(
        'ritual_ZN24QQuickAccessibleAttached11setPropertyEP7QObjectPKcRK8QV'
        'ariant',
        CuteMixin._addressOf(object, 'QObject'),
        CuteMixin._bytesOf(propertyName), CuteMixin._valueOf(value),
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  @overload(QObject, QAccessible.Role)
  @overload(NoneType, QAccessible.Role)
  def findAccessible(
      object: Optional[QObject],
      role: QAccessible.Role = QAccessible.Role.NoRole,
  ) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQuickAccessibleAttached::findAccessible(QObject
    *object, QAccessible::Role role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#findAccessible

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    role : QAccessible.Role
      Passed on as its number. May be left out, as in Qt: it is then
      QAccessible.Role.NoRole.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQuickAccessibleAttached::findAccessible(QObject *object,
    #      QAccessible::Role role)
    address = Rituals.call(
        'ritual_ZN24QQuickAccessibleAttached14findAccessibleEP7QObjectN11QA'
        'ccessible4RoleE',
        CuteMixin._addressOf(object, 'QObject'), role.value,
    )
    return QObject._cuteAt(address)

  @staticmethod
  @overload(str)
  def stripHtml(html: str) -> str:
    """
    Calls Qt's 'QString QQuickAccessibleAttached::stripHtml(const QString
    &html)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#stripHtml

    Parameters
    ----------

    html : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickAccessibleAttached::stripHtml(const QString &html)
    return Rituals.call(
        'ritual_ZN24QQuickAccessibleAttached9stripHtmlERK7QString', html,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAccessibleAttached'

  #  A C++ QQuickAccessibleAttached Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAccessibleAttached'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAccessibleAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAccessibleAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def checkable(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::checkable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#checkable
    """
    #  bool QQuickAccessibleAttached::checkable() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached9checkableEv',
    )

  def checked(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::checked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#checked
    """
    #  bool QQuickAccessibleAttached::checked() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached7checkedEv',
    )

  def editable(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::editable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#editable
    """
    #  bool QQuickAccessibleAttached::editable() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached8editableEv',
    )

  def expandable(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::expandable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#expandable
    """
    #  bool QQuickAccessibleAttached::expandable() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached10expandableEv',
    )

  def expanded(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::expanded() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#expanded
    """
    #  bool QQuickAccessibleAttached::expanded() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached8expandedEv',
    )

  def focusable(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::focusable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#focusable
    """
    #  bool QQuickAccessibleAttached::focusable() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached9focusableEv',
    )

  def focused(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::focused() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#focused
    """
    #  bool QQuickAccessibleAttached::focused() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached7focusedEv',
    )

  def multiLine(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::multiLine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#multiLine
    """
    #  bool QQuickAccessibleAttached::multiLine() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached9multiLineEv',
    )

  def readOnly(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::readOnly() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#readOnly
    """
    #  bool QQuickAccessibleAttached::readOnly() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached8readOnlyEv',
    )

  def selected(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::selected() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#selected
    """
    #  bool QQuickAccessibleAttached::selected() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached8selectedEv',
    )

  def selectable(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::selectable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#selectable
    """
    #  bool QQuickAccessibleAttached::selectable() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached10selectableEv',
    )

  def pressed(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::pressed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#pressed
    """
    #  bool QQuickAccessibleAttached::pressed() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached7pressedEv',
    )

  def checkStateMixed(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::checkStateMixed() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#checkStateMixed
    """
    #  bool QQuickAccessibleAttached::checkStateMixed() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached15checkStateMixedEv',
    )

  def defaultButton(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::defaultButton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#defaultButton
    """
    #  bool QQuickAccessibleAttached::defaultButton() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached13defaultButtonEv',
    )

  def passwordEdit(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::passwordEdit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#passwordEdit
    """
    #  bool QQuickAccessibleAttached::passwordEdit() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached12passwordEditEv',
    )

  def selectableText(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::selectableText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#selectableText
    """
    #  bool QQuickAccessibleAttached::selectableText() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached14selectableTextEv',
    )

  def searchEdit(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::searchEdit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#searchEdit
    """
    #  bool QQuickAccessibleAttached::searchEdit() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached10searchEditEv',
    )

  def role(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickAccessibleAttached::role() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaccessibleattached.html#role

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickAccessibleAttached::role() const
    return QAccessible.Role(self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached4roleEv',
    ))

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickAccessibleAttached::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaccessibleattached.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickAccessibleAttached::name() const
    return self.uglySide.call('ritual_ZNK24QQuickAccessibleAttached4nameEv')

  def wasNameExplicitlySet(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::wasNameExplicitlySet() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#wasNameExplicitlySet
    """
    #  bool QQuickAccessibleAttached::wasNameExplicitlySet() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached20wasNameExplicitlySetEv',
    )

  def description(self) -> str:
    """
    Calls Qt's 'QString QQuickAccessibleAttached::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickAccessibleAttached::description() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached11descriptionEv',
    )

  def id(self) -> str:
    """
    Calls Qt's 'QString QQuickAccessibleAttached::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaccessibleattached.html#id

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickAccessibleAttached::id() const
    return self.uglySide.call('ritual_ZNK24QQuickAccessibleAttached2idEv')

  def labelledBy(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickAccessibleAttached::labelledBy() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#labelledBy

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickAccessibleAttached::labelledBy() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached10labelledByEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def labelFor(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickAccessibleAttached::labelFor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#labelFor

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickAccessibleAttached::labelFor() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached8labelForEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def state(self) -> QAccessible.State:
    """
    Calls Qt's 'QAccessible::State QQuickAccessibleAttached::state() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#state

    Returns
    -------

    QAccessible.State
      A new cute QAccessible::State around the copy Qt gave back. Python owns
      it.
    """
    #  QAccessible::State QQuickAccessibleAttached::state() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached5stateEv',
    )
    return QAccessible.State._cuteOwning(address)

  def ignored(self) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::ignored() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#ignored
    """
    #  bool QQuickAccessibleAttached::ignored() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached7ignoredEv',
    )

  @overload(QAccessible.Relation)
  def findRelation(
      self,
      relation: QAccessible.Relation,
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickAccessibleAttached::findRelation(QAccessible::Relation relation)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#findRelation

    Parameters
    ----------

    relation : QAccessible.Relation
      Passed on as its number.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem
    #      *QQuickAccessibleAttached::findRelation(QAccessible::Relation
    #      relation) const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickAccessibleAttached12findRelationE6QFlagsIN11QAcc'
        'essible12RelationFlagEE',
        relation.value,
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Role)
  def setRole(self, role: QAccessible.Role) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::setRole(QAccessible::Role
    role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#setRole

    Parameters
    ----------

    role : QAccessible.Role
      Passed on as its number.
    """
    #  void QQuickAccessibleAttached::setRole(QAccessible::Role role)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached7setRoleEN11QAccessible4RoleE',
        role.value,
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::setName(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickAccessibleAttached::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached7setNameERK7QString', name,
    )

  @overload(str)
  def setNameImplicitly(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::setNameImplicitly(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#setNameImplicitly

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickAccessibleAttached::setNameImplicitly(const QString &name)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached17setNameImplicitlyERK7QString',
        name,
    )

  @overload(str)
  def setDescription(self, description: str) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::setDescription(const QString
    &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#setDescription

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickAccessibleAttached::setDescription(const QString
    #      &description)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached14setDescriptionERK7QString',
        description,
    )

  @overload(str)
  def setDescriptionImplicitly(self, desc: str) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::setDescriptionImplicitly(const
    QString &desc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html

    Parameters
    ----------

    desc : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickAccessibleAttached::setDescriptionImplicitly(const QString
    #      &desc)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached24setDescriptionImplicitlyERK7Q'
        'String',
        desc,
    )

  @overload(str)
  def setId(self, id: str) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::setId(const QString &id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#setId

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickAccessibleAttached::setId(const QString &id)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached5setIdERK7QString', id,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setLabelledBy(self, labelledBy: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::setLabelledBy(QQuickItem
    *labelledBy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#setLabelledBy

    Parameters
    ----------

    labelledBy : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAccessibleAttached::setLabelledBy(QQuickItem *labelledBy)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached13setLabelledByEP10QQuickItem',
        self._addressOf(labelledBy),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setLabelledByInternal(self, labelledBy: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickAccessibleAttached::setLabelledByInternal(QQuickItem *labelledBy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html

    Parameters
    ----------

    labelledBy : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAccessibleAttached::setLabelledByInternal(QQuickItem
    #      *labelledBy)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached21setLabelledByInternalEP10QQui'
        'ckItem',
        self._addressOf(labelledBy),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setLabelFor(self, labelFor: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::setLabelFor(QQuickItem
    *labelFor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#setLabelFor

    Parameters
    ----------

    labelFor : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAccessibleAttached::setLabelFor(QQuickItem *labelFor)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached11setLabelForEP10QQuickItem',
        self._addressOf(labelFor),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setLabelForInternal(self, labelFor: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::setLabelForInternal(QQuickItem
    *labelFor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#setLabelForInternal

    Parameters
    ----------

    labelFor : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAccessibleAttached::setLabelForInternal(QQuickItem
    #      *labelFor)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached19setLabelForInternalEP10QQuick'
        'Item',
        self._addressOf(labelFor),
    )

  @overload(THIS)
  @overload(NoneType)
  def setProxying(
      self,
      proxying: Optional[QQuickAccessibleAttached],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickAccessibleAttached::setProxying(QQuickAccessibleAttached
    *proxying)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#setProxying

    Parameters
    ----------

    proxying : Optional[QQuickAccessibleAttached]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAccessibleAttached::setProxying(QQuickAccessibleAttached
    #      *proxying)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached11setProxyingEPS_',
        self._addressOf(proxying),
    )

  @overload(bool)
  def setIgnored(self, ignored: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::setIgnored(bool ignored)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#setIgnored

    Parameters
    ----------

    ignored : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::setIgnored(bool ignored)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached10setIgnoredEb', ignored,
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickAccessibleAttached::QQuickAccessibleAttached(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickAccessibleAttached::QQuickAccessibleAttached(QObject *parent)
    self._noteCreation(QQuickAccessibleAttached, lambda: Rituals.call(
        'ritual_ZN24QQuickAccessibleAttachedC1EP7QObject',
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

  @overload(bool)
  def set_checkable(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_checkable(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_checkable

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_checkable(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached13set_checkableEb', arg,
    )

  @overload(bool)
  def set_checked(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_checked(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_checked

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_checked(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached11set_checkedEb', arg,
    )

  @overload(bool)
  def set_editable(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_editable(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_editable

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_editable(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached12set_editableEb', arg,
    )

  @overload(bool)
  def set_expandable(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_expandable(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_expandable

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_expandable(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached14set_expandableEb', arg,
    )

  @overload(bool)
  def set_expanded(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_expanded(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_expanded

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_expanded(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached12set_expandedEb', arg,
    )

  @overload(bool)
  def set_focusable(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_focusable(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_focusable

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_focusable(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached13set_focusableEb', arg,
    )

  @overload(bool)
  def set_focused(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_focused(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_focused

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_focused(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached11set_focusedEb', arg,
    )

  @overload(bool)
  def set_multiLine(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_multiLine(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_multiLine

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_multiLine(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached13set_multiLineEb', arg,
    )

  @overload(bool)
  def set_readOnly(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_readOnly(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_readOnly

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_readOnly(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached12set_readOnlyEb', arg,
    )

  @overload(bool)
  def set_selected(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_selected(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_selected

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_selected(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached12set_selectedEb', arg,
    )

  @overload(bool)
  def set_selectable(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_selectable(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_selectable

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_selectable(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached14set_selectableEb', arg,
    )

  @overload(bool)
  def set_pressed(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_pressed(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_pressed

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_pressed(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached11set_pressedEb', arg,
    )

  @overload(bool)
  def set_checkStateMixed(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_checkStateMixed(bool
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_checkStateMixed

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_checkStateMixed(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached19set_checkStateMixedEb', arg,
    )

  @overload(bool)
  def set_defaultButton(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_defaultButton(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_defaultButton

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_defaultButton(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached17set_defaultButtonEb', arg,
    )

  @overload(bool)
  def set_passwordEdit(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_passwordEdit(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_passwordEdit

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_passwordEdit(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached16set_passwordEditEb', arg,
    )

  @overload(bool)
  def set_selectableText(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_selectableText(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_selectableText

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_selectableText(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached18set_selectableTextEb', arg,
    )

  @overload(bool)
  def set_searchEdit(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::set_searchEdit(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#set_searchEdit

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAccessibleAttached::set_searchEdit(bool arg)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached14set_searchEditEb', arg,
    )

  @overload(str)
  def doAction(self, actionName: str) -> bool:
    """
    Calls Qt's 'bool QQuickAccessibleAttached::doAction(const QString
    &actionName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#doAction

    Parameters
    ----------

    actionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuickAccessibleAttached::doAction(const QString &actionName)
    return self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached8doActionERK7QString',
        actionName,
    )

  @overload(str)
  @overload(str, QAccessible.AnnouncementPoliteness)
  def announce(
      self,
      message: str,
      politeness: QAccessible.AnnouncementPoliteness = (
          QAccessible.AnnouncementPoliteness.Polite),
  ) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::announce(const QString
    &message, QAccessible::AnnouncementPoliteness politeness)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#announce

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.

    politeness : QAccessible.AnnouncementPoliteness
      Passed on as its number. May be left out, as in Qt: it is then
      QAccessible.AnnouncementPoliteness.Polite.
    """
    #  void QQuickAccessibleAttached::announce(const QString &message,
    #      QAccessible::AnnouncementPoliteness politeness)
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached8announceERK7QStringN11QAccessi'
        'ble22AnnouncementPolitenessE',
        message, politeness.value,
    )

  def valueChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::valueChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#valueChanged
    """
    #  void QQuickAccessibleAttached::valueChanged()
    self.uglySide.call('ritual_ZN24QQuickAccessibleAttached12valueChangedEv')

  def cursorPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::cursorPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html
    """
    #  void QQuickAccessibleAttached::cursorPositionChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached21cursorPositionChangedEv',
    )

  def roleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::roleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#roleChanged
    """
    #  void QQuickAccessibleAttached::roleChanged()
    self.uglySide.call('ritual_ZN24QQuickAccessibleAttached11roleChangedEv')

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::nameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#nameChanged
    """
    #  void QQuickAccessibleAttached::nameChanged()
    self.uglySide.call('ritual_ZN24QQuickAccessibleAttached11nameChangedEv')

  def descriptionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::descriptionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#descriptionChanged
    """
    #  void QQuickAccessibleAttached::descriptionChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached18descriptionChangedEv',
    )

  def idChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::idChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#idChanged
    """
    #  void QQuickAccessibleAttached::idChanged()
    self.uglySide.call('ritual_ZN24QQuickAccessibleAttached9idChangedEv')

  def ignoredChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::ignoredChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#ignoredChanged
    """
    #  void QQuickAccessibleAttached::ignoredChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached14ignoredChangedEv',
    )

  def labelledByChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::labelledByChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#labelledByChanged
    """
    #  void QQuickAccessibleAttached::labelledByChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached17labelledByChangedEv',
    )

  def labelForChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::labelForChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#labelForChanged
    """
    #  void QQuickAccessibleAttached::labelForChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached15labelForChangedEv',
    )

  def pressAction(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::pressAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#pressAction
    """
    #  void QQuickAccessibleAttached::pressAction()
    self.uglySide.call('ritual_ZN24QQuickAccessibleAttached11pressActionEv')

  def toggleAction(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::toggleAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#toggleAction
    """
    #  void QQuickAccessibleAttached::toggleAction()
    self.uglySide.call('ritual_ZN24QQuickAccessibleAttached12toggleActionEv')

  def increaseAction(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::increaseAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#increaseAction
    """
    #  void QQuickAccessibleAttached::increaseAction()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached14increaseActionEv',
    )

  def decreaseAction(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::decreaseAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#decreaseAction
    """
    #  void QQuickAccessibleAttached::decreaseAction()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached14decreaseActionEv',
    )

  def showOnScreenAction(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::showOnScreenAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#showOnScreenAction
    """
    #  void QQuickAccessibleAttached::showOnScreenAction()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached18showOnScreenActionEv',
    )

  def scrollUpAction(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::scrollUpAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#scrollUpAction
    """
    #  void QQuickAccessibleAttached::scrollUpAction()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached14scrollUpActionEv',
    )

  def scrollDownAction(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::scrollDownAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#scrollDownAction
    """
    #  void QQuickAccessibleAttached::scrollDownAction()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached16scrollDownActionEv',
    )

  def scrollLeftAction(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::scrollLeftAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#scrollLeftAction
    """
    #  void QQuickAccessibleAttached::scrollLeftAction()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached16scrollLeftActionEv',
    )

  def scrollRightAction(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::scrollRightAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#scrollRightAction
    """
    #  void QQuickAccessibleAttached::scrollRightAction()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached17scrollRightActionEv',
    )

  def previousPageAction(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::previousPageAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#previousPageAction
    """
    #  void QQuickAccessibleAttached::previousPageAction()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached18previousPageActionEv',
    )

  def nextPageAction(self) -> None:
    """
    Calls Qt's 'void QQuickAccessibleAttached::nextPageAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickaccessibleattached.html#nextPageAction
    """
    #  void QQuickAccessibleAttached::nextPageAction()
    self.uglySide.call(
        'ritual_ZN24QQuickAccessibleAttached14nextPageActionEv',
    )

  @staticmethod
  def availableActions(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::availableActions(QStringList
    *actions) const': names 'QStringList', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.availableActions' has no cute function "
        "yet. Qt's 'void "
        "QQuickAccessibleAttached::availableActions(QStringList *actions) "
        "const': names 'QStringList', which has no cute class yet.")

  @staticmethod
  def checkStateMixedChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::checkStateMixedChanged(bool arg)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.checkStateMixedChanged' has no cute "
        "function yet. Qt's 'void "
        "QQuickAccessibleAttached::checkStateMixedChanged(bool arg)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def checkableChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::checkableChanged(bool arg)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.checkableChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::checkableChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def checkedChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::checkedChanged(bool arg)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.checkedChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::checkedChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def defaultButtonChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::defaultButtonChanged(bool arg)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.defaultButtonChanged' has no cute "
        "function yet. Qt's 'void "
        "QQuickAccessibleAttached::defaultButtonChanged(bool arg)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def editableChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::editableChanged(bool arg)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.editableChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::editableChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def expandableChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::expandableChanged(bool arg)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.expandableChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::expandableChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def expandedChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::expandedChanged(bool arg)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.expandedChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::expandedChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def focusableChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::focusableChanged(bool arg)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.focusableChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::focusableChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def focusedChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::focusedChanged(bool arg)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.focusedChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::focusedChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def multiLineChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::multiLineChanged(bool arg)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.multiLineChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::multiLineChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def passwordEditChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::passwordEditChanged(bool arg)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.passwordEditChanged' has no cute "
        "function yet. Qt's 'void "
        "QQuickAccessibleAttached::passwordEditChanged(bool arg)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def pressedChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::pressedChanged(bool arg)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.pressedChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::pressedChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def readOnlyChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::readOnlyChanged(bool arg)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.readOnlyChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::readOnlyChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def searchEditChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::searchEditChanged(bool arg)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.searchEditChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::searchEditChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def selectableChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::selectableChanged(bool arg)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.selectableChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::selectableChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def selectableTextChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::selectableTextChanged(bool arg)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.selectableTextChanged' has no cute "
        "function yet. Qt's 'void "
        "QQuickAccessibleAttached::selectableTextChanged(bool arg)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def selectedChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickAccessibleAttached::selectedChanged(bool arg)': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QQuickAccessibleAttached.selectedChanged' has no cute function "
        "yet. Qt's 'void QQuickAccessibleAttached::selectedChanged(bool "
        "arg)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
