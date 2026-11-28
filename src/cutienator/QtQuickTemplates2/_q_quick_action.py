"""
QQuickAction binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickaction_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickAction to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QKeySequence
  from . import QQuickIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QKeySequence = WAIT['QKeySequence']
  QQuickIcon = WAIT['QQuickIcon']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAction(QObject):
  """
  The cute side of Qt's QQuickAction: a plain Python object standing in front
  of one C++ QQuickAction.

  It is built on the cute 'QObject', as Qt's QQuickAction is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAction that has a ritual and that Python can
  call so far, 27 names in all: 'metaObject', 'tr', 'text', 'setText',
  'icon', 'setIcon', 'isEnabled', 'setEnabled', 'resetEnabled', 'isChecked',
  'setChecked', 'isCheckable', 'setCheckable', 'shortcut', 'setShortcut',
  'toggle', 'trigger', 'textChanged', 'iconChanged', 'enabledChanged',
  'checkedChanged', 'checkableChanged', 'shortcutChanged', 'toggled',
  'triggered', 'event', 'eventFilter'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAction::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickAction::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickAction::~QQuickAction()': the destructor: Python never
    removes a C++ QQuickAction.
  - Qt's 'QQuickActionPrivate *QQuickAction::d_func()': gives
    'QQuickActionPrivate', which has no cute class yet.
  - Qt's 'const QQuickActionPrivate *QQuickAction::d_func() const': gives
    'QQuickActionPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 37 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickAction is created at the first use, not by
    'QQuickAction(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAction.
  - Qt tells when it has removed the C++ QQuickAction. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QQuickAction::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#tr

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
    #  QString QQuickAction::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuickAction2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAction'

  #  A C++ QQuickAction Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAction'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAction::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAction::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickAction10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickAction::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickAction::text() const
    return self.uglySide.call('ritual_ZNK12QQuickAction4textEv')

  def icon(self) -> QQuickIcon:
    """
    Calls Qt's 'QQuickIcon QQuickAction::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#icon

    Returns
    -------

    QQuickIcon
      A new cute QQuickIcon around the copy Qt gave back. Python owns it.
    """
    #  QQuickIcon QQuickAction::icon() const
    address = self.uglySide.call('ritual_ZNK12QQuickAction4iconEv')
    from . import QQuickIcon
    return QQuickIcon._cuteOwning(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickAction::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#isEnabled
    """
    #  bool QQuickAction::isEnabled() const
    return self.uglySide.call('ritual_ZNK12QQuickAction9isEnabledEv')

  def isChecked(self) -> bool:
    """
    Calls Qt's 'bool QQuickAction::isChecked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#isChecked
    """
    #  bool QQuickAction::isChecked() const
    return self.uglySide.call('ritual_ZNK12QQuickAction9isCheckedEv')

  def isCheckable(self) -> bool:
    """
    Calls Qt's 'bool QQuickAction::isCheckable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#isCheckable
    """
    #  bool QQuickAction::isCheckable() const
    return self.uglySide.call('ritual_ZNK12QQuickAction11isCheckableEv')

  def shortcut(self) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence QQuickAction::shortcut() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#shortcut

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence QQuickAction::shortcut() const
    address = self.uglySide.call('ritual_ZNK12QQuickAction8shortcutEv')
    from ..QtGui import QKeySequence
    return QKeySequence._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickAction::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickAction::setText(const QString &text)
    self.uglySide.call('ritual_ZN12QQuickAction7setTextERK7QString', text)

  @overload(QQuickIcon)
  def setIcon(self, icon: QQuickIcon) -> None:
    """
    Calls Qt's 'void QQuickAction::setIcon(const QQuickIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#setIcon

    Parameters
    ----------

    icon : QQuickIcon
      Passed on as a value: Qt reads the C++ QQuickIcon, which stays Python's
      own.
    """
    #  void QQuickAction::setIcon(const QQuickIcon &icon)
    self.uglySide.call(
        'ritual_ZN12QQuickAction7setIconERK10QQuickIcon',
        self._valueOf(icon),
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickAction::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickAction::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN12QQuickAction10setEnabledEb', enabled)

  @overload(bool)
  def setChecked(self, checked: bool) -> None:
    """
    Calls Qt's 'void QQuickAction::setChecked(bool checked)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#setChecked

    Parameters
    ----------

    checked : bool
      Passed on as it is.
    """
    #  void QQuickAction::setChecked(bool checked)
    self.uglySide.call('ritual_ZN12QQuickAction10setCheckedEb', checked)

  @overload(bool)
  def setCheckable(self, checkable: bool) -> None:
    """
    Calls Qt's 'void QQuickAction::setCheckable(bool checkable)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#setCheckable

    Parameters
    ----------

    checkable : bool
      Passed on as it is.
    """
    #  void QQuickAction::setCheckable(bool checkable)
    self.uglySide.call('ritual_ZN12QQuickAction12setCheckableEb', checkable)

  @overload(QKeySequence)
  def setShortcut(self, shortcut: QKeySequence) -> None:
    """
    Calls Qt's 'void QQuickAction::setShortcut(const QKeySequence
    &shortcut)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#setShortcut

    Parameters
    ----------

    shortcut : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  void QQuickAction::setShortcut(const QKeySequence &shortcut)
    self.uglySide.call(
        'ritual_ZN12QQuickAction11setShortcutERK12QKeySequence',
        self._valueOf(shortcut),
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
    Notes what was given, for Qt's 'QQuickAction::QQuickAction(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#QQuickAction

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAction::QQuickAction(QObject *parent)
    self._noteCreation(QQuickAction, lambda: Rituals.call(
        'ritual_ZN12QQuickActionC1EP7QObject',
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

  def resetEnabled(self) -> None:
    """
    Calls Qt's 'void QQuickAction::resetEnabled()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#resetEnabled
    """
    #  void QQuickAction::resetEnabled()
    self.uglySide.call('ritual_ZN12QQuickAction12resetEnabledEv')

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def toggle(self, source: Optional[QObject] = None) -> None:
    """
    Calls Qt's 'void QQuickAction::toggle(QObject *source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#toggle

    Parameters
    ----------

    source : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickAction::toggle(QObject *source)
    self.uglySide.call(
        'ritual_ZN12QQuickAction6toggleEP7QObject',
        self._addressOf(source, 'QObject'),
    )

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def trigger(self, source: Optional[QObject] = None) -> None:
    """
    Calls Qt's 'void QQuickAction::trigger(QObject *source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#trigger

    Parameters
    ----------

    source : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickAction::trigger(QObject *source)
    self.uglySide.call(
        'ritual_ZN12QQuickAction7triggerEP7QObject',
        self._addressOf(source, 'QObject'),
    )

  @overload(str)
  def textChanged(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickAction::textChanged(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#textChanged

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickAction::textChanged(const QString &text)
    self.uglySide.call(
        'ritual_ZN12QQuickAction11textChangedERK7QString', text,
    )

  @overload(QQuickIcon)
  def iconChanged(self, icon: QQuickIcon) -> None:
    """
    Calls Qt's 'void QQuickAction::iconChanged(const QQuickIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#iconChanged

    Parameters
    ----------

    icon : QQuickIcon
      Passed on as a value: Qt reads the C++ QQuickIcon, which stays Python's
      own.
    """
    #  void QQuickAction::iconChanged(const QQuickIcon &icon)
    self.uglySide.call(
        'ritual_ZN12QQuickAction11iconChangedERK10QQuickIcon',
        self._valueOf(icon),
    )

  @overload(bool)
  def enabledChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickAction::enabledChanged(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#enabledChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickAction::enabledChanged(bool enabled)
    self.uglySide.call('ritual_ZN12QQuickAction14enabledChangedEb', enabled)

  @overload(bool)
  def checkedChanged(self, checked: bool) -> None:
    """
    Calls Qt's 'void QQuickAction::checkedChanged(bool checked)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#checkedChanged

    Parameters
    ----------

    checked : bool
      Passed on as it is.
    """
    #  void QQuickAction::checkedChanged(bool checked)
    self.uglySide.call('ritual_ZN12QQuickAction14checkedChangedEb', checked)

  @overload(bool)
  def checkableChanged(self, checkable: bool) -> None:
    """
    Calls Qt's 'void QQuickAction::checkableChanged(bool checkable)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#checkableChanged

    Parameters
    ----------

    checkable : bool
      Passed on as it is.
    """
    #  void QQuickAction::checkableChanged(bool checkable)
    self.uglySide.call(
        'ritual_ZN12QQuickAction16checkableChangedEb', checkable,
    )

  @overload(QKeySequence)
  def shortcutChanged(self, shortcut: QKeySequence) -> None:
    """
    Calls Qt's 'void QQuickAction::shortcutChanged(const QKeySequence
    &shortcut)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#shortcutChanged

    Parameters
    ----------

    shortcut : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  void QQuickAction::shortcutChanged(const QKeySequence &shortcut)
    self.uglySide.call(
        'ritual_ZN12QQuickAction15shortcutChangedERK12QKeySequence',
        self._valueOf(shortcut),
    )

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def toggled(self, source: Optional[QObject] = None) -> None:
    """
    Calls Qt's 'void QQuickAction::toggled(QObject *source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#toggled

    Parameters
    ----------

    source : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickAction::toggled(QObject *source)
    self.uglySide.call(
        'ritual_ZN12QQuickAction7toggledEP7QObject',
        self._addressOf(source, 'QObject'),
    )

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def triggered(self, source: Optional[QObject] = None) -> None:
    """
    Calls Qt's 'void QQuickAction::triggered(QObject *source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#triggered

    Parameters
    ----------

    source : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickAction::triggered(QObject *source)
    self.uglySide.call(
        'ritual_ZN12QQuickAction9triggeredEP7QObject',
        self._addressOf(source, 'QObject'),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickAction::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickAction::event(QEvent *event)
    ritual = 'ritual_ZN12QQuickAction5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickAction5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickAction::eventFilter(QObject *object, QEvent
    *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickaction.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickAction::eventFilter(QObject *object, QEvent *event)
    ritual = 'ritual_ZN12QQuickAction11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickAction11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
    )
