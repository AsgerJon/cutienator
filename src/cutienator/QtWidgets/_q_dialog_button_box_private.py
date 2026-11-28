"""
QDialogButtonBoxPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qdialogbuttonbox_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDialogButtonBoxPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QDialogButtonBox, QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent
  from . import QAbstractButton, QPushButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractButton = WAIT['QAbstractButton']
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDialogButtonBoxPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QDialogButtonBoxPrivate: a plain Python object
  standing in front of one C++ QDialogButtonBoxPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QDialogButtonBoxPrivate
  is built on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDialogButtonBoxPrivate that has a ritual and that
  Python can call so far, 17 names in all: 'q_func', 'createStandardButtons',
  'removeButton', 'layoutButtons', 'initLayout', 'resetLayout',
  'createButton', 'addButton', 'handleButtonDestroyed',
  'handleButtonClicked', 'handleButtonShowAndHide', 'addButtonsToLayout',
  'ensureFirstAcceptIsDefault', 'retranslateStrings', 'disconnectAll',
  'allButtons', 'visibleButtons'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QDialogButtonBox *QDialogButtonBoxPrivate::q_func() const':
    takes in Python what 'QDialogButtonBox
    *QDialogButtonBoxPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 20 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QDialogButtonBoxPrivate is created at the first use, not by
    'QDialogButtonBoxPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDialogButtonBoxPrivate.
  - Each name of Qt's QDialogButtonBoxPrivate that has no cute function yet,
    'buttonRole', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QDialogButtonBoxPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class AddRule(CuteNum, scoped=True):
    """
    The enum 'QDialogButtonBoxPrivate::AddRule' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Connect = Kee[int](0)
    SkipConnect = Kee[int](1)

  class LayoutRule(CuteNum, scoped=True):
    """
    The enum 'QDialogButtonBoxPrivate::LayoutRule' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    DoLayout = Kee[int](0)
    SkipLayout = Kee[int](1)

  class RemoveReason(CuteNum, scoped=True):
    """
    The enum 'QDialogButtonBoxPrivate::RemoveReason' of Qt, with the 3 names
    Qt gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    HideEvent = Kee[int](0)
    ManualRemove = Kee[int](1)
    Destroyed = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDialogButtonBoxPrivate'

  #  A C++ QDialogButtonBoxPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDialogButtonBoxPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def allButtons(self) -> QList[QAbstractButton]:
    """
    Calls Qt's 'QList<QAbstractButton *>
    QDialogButtonBoxPrivate::allButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#allButtons

    Returns
    -------

    QList[QAbstractButton]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractButton *> QDialogButtonBoxPrivate::allButtons() const
    address = self.uglySide.call(
        'ritual_ZNK23QDialogButtonBoxPrivate10allButtonsEv',
    )
    from . import QAbstractButton
    return QList[QAbstractButton]._cuteOwning(address)

  def visibleButtons(self) -> QList[QAbstractButton]:
    """
    Calls Qt's 'QList<QAbstractButton *>
    QDialogButtonBoxPrivate::visibleButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#visibleButtons

    Returns
    -------

    QList[QAbstractButton]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractButton *> QDialogButtonBoxPrivate::visibleButtons()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK23QDialogButtonBoxPrivate14visibleButtonsEv',
    )
    from . import QAbstractButton
    return QList[QAbstractButton]._cuteOwning(address)

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

  @overload(Qt.Orientation)
  def __init__(self, orient: Qt.Orientation) -> None:
    """
    Notes what was given, for Qt's
    'QDialogButtonBoxPrivate::QDialogButtonBoxPrivate(Qt::Orientation
    orient)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html

    Parameters
    ----------

    orient : Qt.Orientation
      Passed on as its number.
    """
    #  QDialogButtonBoxPrivate::QDialogButtonBoxPrivate(Qt::Orientation
    #      orient)
    self._noteCreation(QDialogButtonBoxPrivate, lambda: Rituals.call(
        'ritual_ZN23QDialogButtonBoxPrivateC1EN2Qt11OrientationE',
        orient.value,
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

  def q_func(self) -> Optional[QDialogButtonBox]:
    """
    Calls Qt's 'QDialogButtonBox *QDialogButtonBoxPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#q_func

    Returns
    -------

    Optional[QDialogButtonBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDialogButtonBox *QDialogButtonBoxPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QDialogButtonBoxPrivate6q_funcEv',
    )
    return QDialogButtonBox._cuteAt(address)

  @overload(QDialogButtonBox.StandardButtons)
  def createStandardButtons(
      self,
      buttons: QDialogButtonBox.StandardButtons,
  ) -> None:
    """
    Calls Qt's 'void
    QDialogButtonBoxPrivate::createStandardButtons(QDialogButtonBox::
    StandardButtons buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#createStandardButtons

    Parameters
    ----------

    buttons : QDialogButtonBox.StandardButtons
      Passed on as its number.
    """
    #  void QDialogButtonBoxPrivate::createStandardButtons(QDialogButtonBox::
    #      StandardButtons buttons)
    self.uglySide.call(
        'ritual_ZN23QDialogButtonBoxPrivate21createStandardButtonsE6QFlagsI'
        'N16QDialogButtonBox14StandardButtonEE',
        buttons.value,
    )

  @overload(QAbstractButton, RemoveReason)
  @overload(NoneType, RemoveReason)
  def removeButton(
      self,
      button: Optional[QAbstractButton],
      reason: RemoveReason,
  ) -> None:
    """
    Calls Qt's 'void QDialogButtonBoxPrivate::removeButton(QAbstractButton
    *button, RemoveReason reason)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#removeButton

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reason : RemoveReason
      Passed on as its number.
    """
    #  void QDialogButtonBoxPrivate::removeButton(QAbstractButton *button,
    #      RemoveReason reason)
    self.uglySide.call(
        'ritual_ZN23QDialogButtonBoxPrivate12removeButtonEP15QAbstractButto'
        'nNS_12RemoveReasonE',
        self._addressOf(button), reason.value,
    )

  def layoutButtons(self) -> None:
    """
    Calls Qt's 'void QDialogButtonBoxPrivate::layoutButtons()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#layoutButtons
    """
    #  void QDialogButtonBoxPrivate::layoutButtons()
    self.uglySide.call('ritual_ZN23QDialogButtonBoxPrivate13layoutButtonsEv')

  def initLayout(self) -> None:
    """
    Calls Qt's 'void QDialogButtonBoxPrivate::initLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#initLayout
    """
    #  void QDialogButtonBoxPrivate::initLayout()
    self.uglySide.call('ritual_ZN23QDialogButtonBoxPrivate10initLayoutEv')

  def resetLayout(self) -> None:
    """
    Calls Qt's 'void QDialogButtonBoxPrivate::resetLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#resetLayout
    """
    #  void QDialogButtonBoxPrivate::resetLayout()
    self.uglySide.call('ritual_ZN23QDialogButtonBoxPrivate11resetLayoutEv')

  @overload(QDialogButtonBox.StandardButton)
  @overload(QDialogButtonBox.StandardButton, LayoutRule)
  def createButton(
      self,
      button: QDialogButtonBox.StandardButton,
      layoutRule: LayoutRule = LayoutRule.DoLayout,
  ) -> Optional[QPushButton]:
    """
    Calls Qt's 'QPushButton
    *QDialogButtonBoxPrivate::createButton(QDialogButtonBox::StandardButton
    button, LayoutRule layoutRule)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#createButton

    Parameters
    ----------

    button : QDialogButtonBox.StandardButton
      Passed on as its number.

    layoutRule : LayoutRule
      Passed on as its number. May be left out, as in Qt: it is then
      LayoutRule.DoLayout.

    Returns
    -------

    Optional[QPushButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPushButton *QDialogButtonBoxPrivate::createButton(QDialogButtonBox::
    #      StandardButton button, LayoutRule layoutRule)
    address = self.uglySide.call(
        'ritual_ZN23QDialogButtonBoxPrivate12createButtonEN16QDialogButtonB'
        'ox14StandardButtonENS_10LayoutRuleE',
        button.value, layoutRule.value,
    )
    from . import QPushButton
    return QPushButton._cuteAt(address)

  @overload(QAbstractButton, QDialogButtonBox.ButtonRole)
  @overload(NoneType, QDialogButtonBox.ButtonRole)
  @overload(QAbstractButton, QDialogButtonBox.ButtonRole, LayoutRule)
  @overload(NoneType, QDialogButtonBox.ButtonRole, LayoutRule)
  @overload(
      QAbstractButton, QDialogButtonBox.ButtonRole, LayoutRule, AddRule,
  )
  @overload(NoneType, QDialogButtonBox.ButtonRole, LayoutRule, AddRule)
  def addButton(
      self,
      button: Optional[QAbstractButton],
      role: QDialogButtonBox.ButtonRole,
      layoutRule: LayoutRule = LayoutRule.DoLayout,
      addRule: AddRule = AddRule.Connect,
  ) -> None:
    """
    Calls Qt's 'void QDialogButtonBoxPrivate::addButton(QAbstractButton
    *button, QDialogButtonBox::ButtonRole role, LayoutRule layoutRule,
    AddRule addRule)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#addButton

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    role : QDialogButtonBox.ButtonRole
      Passed on as its number.

    layoutRule : LayoutRule
      Passed on as its number. May be left out, as in Qt: it is then
      LayoutRule.DoLayout.

    addRule : AddRule
      Passed on as its number. May be left out, as in Qt: it is then
      AddRule.Connect.
    """
    #  void QDialogButtonBoxPrivate::addButton(QAbstractButton *button,
    #      QDialogButtonBox::ButtonRole role, LayoutRule layoutRule, AddRule
    #      addRule)
    self.uglySide.call(
        'ritual_ZN23QDialogButtonBoxPrivate9addButtonEP15QAbstractButtonN16'
        'QDialogButtonBox10ButtonRoleENS_10LayoutRuleENS_7AddRuleE',
        self._addressOf(button), role.value, layoutRule.value, addRule.value,
    )

  def handleButtonDestroyed(self) -> None:
    """
    Calls Qt's 'void QDialogButtonBoxPrivate::handleButtonDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#handleButtonDestroyed
    """
    #  void QDialogButtonBoxPrivate::handleButtonDestroyed()
    self.uglySide.call(
        'ritual_ZN23QDialogButtonBoxPrivate21handleButtonDestroyedEv',
    )

  def handleButtonClicked(self) -> None:
    """
    Calls Qt's 'void QDialogButtonBoxPrivate::handleButtonClicked()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#handleButtonClicked
    """
    #  void QDialogButtonBoxPrivate::handleButtonClicked()
    self.uglySide.call(
        'ritual_ZN23QDialogButtonBoxPrivate19handleButtonClickedEv',
    )

  @overload(QAbstractButton, QEvent)
  @overload(QAbstractButton, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def handleButtonShowAndHide(
      self,
      button: Optional[QAbstractButton],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    QDialogButtonBoxPrivate::handleButtonShowAndHide(QAbstractButton *button,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDialogButtonBoxPrivate::handleButtonShowAndHide(QAbstractButton
    #      *button, QEvent *event)
    return self.uglySide.call(
        'ritual_ZN23QDialogButtonBoxPrivate23handleButtonShowAndHideEP15QAb'
        'stractButtonP6QEvent',
        self._addressOf(button), self._addressOf(event),
    )

  @overload(QList[QAbstractButton], bool)
  def addButtonsToLayout(
      self,
      buttonList: QList[QAbstractButton],
      reverse: bool,
  ) -> None:
    """
    Calls Qt's 'void QDialogButtonBoxPrivate::addButtonsToLayout(const
    QList<QAbstractButton *> &buttonList, bool reverse)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#addButtonsToLayout

    Parameters
    ----------

    buttonList : QList[QAbstractButton]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    reverse : bool
      Passed on as it is.
    """
    #  void QDialogButtonBoxPrivate::addButtonsToLayout(const
    #      QList<QAbstractButton *> &buttonList, bool reverse)
    self.uglySide.call(
        'ritual_ZN23QDialogButtonBoxPrivate18addButtonsToLayoutERK5QListIP1'
        '5QAbstractButtonEb',
        self._valueOf(buttonList), reverse,
    )

  def ensureFirstAcceptIsDefault(self) -> None:
    """
    Calls Qt's 'void QDialogButtonBoxPrivate::ensureFirstAcceptIsDefault()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html
    """
    #  void QDialogButtonBoxPrivate::ensureFirstAcceptIsDefault()
    self.uglySide.call(
        'ritual_ZN23QDialogButtonBoxPrivate26ensureFirstAcceptIsDefaultEv',
    )

  def retranslateStrings(self) -> None:
    """
    Calls Qt's 'void QDialogButtonBoxPrivate::retranslateStrings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#retranslateStrings
    """
    #  void QDialogButtonBoxPrivate::retranslateStrings()
    self.uglySide.call(
        'ritual_ZN23QDialogButtonBoxPrivate18retranslateStringsEv',
    )

  def disconnectAll(self) -> None:
    """
    Calls Qt's 'void QDialogButtonBoxPrivate::disconnectAll()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonboxprivate.html#disconnectAll
    """
    #  void QDialogButtonBoxPrivate::disconnectAll()
    self.uglySide.call('ritual_ZN23QDialogButtonBoxPrivate13disconnectAllEv')

  @staticmethod
  def buttonRole(*__, **_) -> Never:
    """
    Qt's 'QDialogButtonBox::ButtonRole
    QDialogButtonBoxPrivate::buttonRole(QAbstractButton *button) const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QDialogButtonBoxPrivate.buttonRole' has no cute function yet. "
        "Qt's 'QDialogButtonBox::ButtonRole "
        "QDialogButtonBoxPrivate::buttonRole(QAbstractButton *button) "
        "const': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
