"""
QDialogButtonBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qdialogbuttonbox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QKeySequence
  from . import QAbstractButton, QDialogButtonBoxPrivate, QPushButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractButton = WAIT['QAbstractButton']
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDialogButtonBox(QWidget):
  """
  The cute side of Qt's QDialogButtonBox: a plain Python object standing in
  front of one C++ QDialogButtonBox.

  It is built on the cute 'QWidget', as Qt's QDialogButtonBox is built on
  Qt's QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDialogButtonBox that has a ritual and that Python
  can call so far, 24 names in all: 'metaObject', 'tr', 'setOrientation',
  'orientation', 'addButton', 'removeButton', 'clear', 'buttons',
  'buttonRole', 'setStandardButtons', 'standardButtons', 'standardButton',
  'button', 'setCenterButtons', 'centerButtons', 'standardButtonText',
  'standardButtonShortcut', 'clicked', 'accepted', 'helpRequested',
  'rejected', 'changeEvent', 'event', 'd_func'. It can be made from Python,
  in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDialogButtonBox::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QDialogButtonBox::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDialogButtonBox::~QDialogButtonBox()': the destructor: Python
    never removes a C++ QDialogButtonBox.
  - Qt's 'const QDialogButtonBoxPrivate *QDialogButtonBox::d_func() const':
    takes in Python what 'QDialogButtonBoxPrivate
    *QDialogButtonBox::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 38 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QDialogButtonBox is created at the first use, not by
    'QDialogButtonBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDialogButtonBox.
  - Qt tells when it has removed the C++ QDialogButtonBox. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QDialogButtonBox, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ButtonLayout(CuteNum):
    """
    The enum 'QDialogButtonBox::ButtonLayout' of Qt, with the 5 names Qt
    gives in it.
    """

    WinLayout = Kee[int](0)
    MacLayout = Kee[int](1)
    KdeLayout = Kee[int](2)
    GnomeLayout = Kee[int](3)
    AndroidLayout = Kee[int](4)

  class ButtonRole(CuteNum):
    """
    The enum 'QDialogButtonBox::ButtonRole' of Qt, with the 11 names Qt gives
    in it.
    """

    InvalidRole = Kee[int](-1)
    AcceptRole = Kee[int](0)
    RejectRole = Kee[int](1)
    DestructiveRole = Kee[int](2)
    ActionRole = Kee[int](3)
    HelpRole = Kee[int](4)
    YesRole = Kee[int](5)
    NoRole = Kee[int](6)
    ResetRole = Kee[int](7)
    ApplyRole = Kee[int](8)
    NRoles = Kee[int](9)

  class StandardButton(CuteFlags):
    """
    The flags enum 'QDialogButtonBox::StandardButton' of Qt, with the 21
    names Qt gives in it. Qt names the type of its combinations
    'QDialogButtonBox::StandardButtons'.
    """

    NoButton = 0x0
    Ok = 0x400
    Save = 0x800
    SaveAll = 0x1000
    Open = 0x2000
    Yes = 0x4000
    YesToAll = 0x8000
    No = 0x10000
    NoToAll = 0x20000
    Abort = 0x40000
    Retry = 0x80000
    Ignore = 0x100000
    Close = 0x200000
    Cancel = 0x400000
    Discard = 0x800000
    Help = 0x1000000
    Apply = 0x2000000
    Reset = 0x4000000
    RestoreDefaults = 0x8000000
    FirstButton = 0x400
    LastButton = 0x8000000

  StandardButtons = StandardButton

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
    Calls Qt's 'QString QDialogButtonBox::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#tr

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
    #  QString QDialogButtonBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QDialogButtonBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(StandardButton)
  def standardButtonText(button: StandardButton) -> str:
    """
    Calls Qt's 'QString QDialogButtonBox::standardButtonText(StandardButton
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#standardButtonText

    Parameters
    ----------

    button : StandardButton
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDialogButtonBox::standardButtonText(StandardButton button)
    return Rituals.call(
        'ritual_ZN16QDialogButtonBox18standardButtonTextENS_14StandardButto'
        'nE',
        button.value,
    )

  @staticmethod
  @overload(StandardButton)
  def standardButtonShortcut(button: StandardButton) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence
    QDialogButtonBox::standardButtonShortcut(StandardButton button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#standardButtonShortcut

    Parameters
    ----------

    button : StandardButton
      Passed on as its number.

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence QDialogButtonBox::standardButtonShortcut(StandardButton
    #      button)
    address = Rituals.call(
        'ritual_ZN16QDialogButtonBox22standardButtonShortcutENS_14StandardB'
        'uttonE',
        button.value,
    )
    from ..QtGui import QKeySequence
    return QKeySequence._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDialogButtonBox'

  #  A C++ QDialogButtonBox Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDialogButtonBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDialogButtonBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDialogButtonBox::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QDialogButtonBox10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QDialogButtonBox::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QDialogButtonBox::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK16QDialogButtonBox11orientationEv',
    ))

  def buttons(self) -> QList[QAbstractButton]:
    """
    Calls Qt's 'QList<QAbstractButton *> QDialogButtonBox::buttons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#buttons

    Returns
    -------

    QList[QAbstractButton]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAbstractButton *> QDialogButtonBox::buttons() const
    address = self.uglySide.call('ritual_ZNK16QDialogButtonBox7buttonsEv')
    from . import QAbstractButton
    return QList[QAbstractButton]._cuteOwning(address)

  @overload(QAbstractButton)
  @overload(NoneType)
  def buttonRole(self, button: Optional[QAbstractButton]) -> ButtonRole:
    """
    Calls Qt's 'ButtonRole QDialogButtonBox::buttonRole(QAbstractButton
    *button) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#buttonRole

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    ButtonRole
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ButtonRole(number)'
      gives.
    """
    #  ButtonRole QDialogButtonBox::buttonRole(QAbstractButton *button) const
    return QDialogButtonBox.ButtonRole(self.uglySide.call(
        'ritual_ZNK16QDialogButtonBox10buttonRoleEP15QAbstractButton',
        self._addressOf(button),
    ))

  def standardButtons(self) -> StandardButtons:
    """
    Calls Qt's 'StandardButtons QDialogButtonBox::standardButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#standardButtons

    Returns
    -------

    StandardButtons
      The value standing for the combination Qt gave back.
    """
    #  StandardButtons QDialogButtonBox::standardButtons() const
    return QDialogButtonBox.StandardButtons(self.uglySide.call(
        'ritual_ZNK16QDialogButtonBox15standardButtonsEv',
    ))

  @overload(QAbstractButton)
  @overload(NoneType)
  def standardButton(
      self,
      button: Optional[QAbstractButton],
  ) -> StandardButton:
    """
    Calls Qt's 'StandardButton
    QDialogButtonBox::standardButton(QAbstractButton *button) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#standardButton

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    StandardButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StandardButton(number)'
      gives.
    """
    #  StandardButton QDialogButtonBox::standardButton(QAbstractButton
    #      *button) const
    return QDialogButtonBox.StandardButton(self.uglySide.call(
        'ritual_ZNK16QDialogButtonBox14standardButtonEP15QAbstractButton',
        self._addressOf(button),
    ))

  @overload(StandardButton)
  def button(self, which: StandardButton) -> Optional[QPushButton]:
    """
    Calls Qt's 'QPushButton *QDialogButtonBox::button(StandardButton which)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#button

    Parameters
    ----------

    which : StandardButton
      Passed on as its number.

    Returns
    -------

    Optional[QPushButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPushButton *QDialogButtonBox::button(StandardButton which) const
    address = self.uglySide.call(
        'ritual_ZNK16QDialogButtonBox6buttonENS_14StandardButtonE',
        which.value,
    )
    from . import QPushButton
    return QPushButton._cuteAt(address)

  def centerButtons(self) -> bool:
    """
    Calls Qt's 'bool QDialogButtonBox::centerButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#centerButtons
    """
    #  bool QDialogButtonBox::centerButtons() const
    return self.uglySide.call(
        'ritual_ZNK16QDialogButtonBox13centerButtonsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QDialogButtonBox::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QDialogButtonBox::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN16QDialogButtonBox14setOrientationEN2Qt11OrientationE',
        orientation.value,
    )

  @overload(StandardButtons)
  def setStandardButtons(self, buttons: StandardButtons) -> None:
    """
    Calls Qt's 'void QDialogButtonBox::setStandardButtons(StandardButtons
    buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#setStandardButtons

    Parameters
    ----------

    buttons : StandardButtons
      Passed on as its number.
    """
    #  void QDialogButtonBox::setStandardButtons(StandardButtons buttons)
    self.uglySide.call(
        'ritual_ZN16QDialogButtonBox18setStandardButtonsE6QFlagsINS_14Stand'
        'ardButtonEE',
        buttons.value,
    )

  @overload(bool)
  def setCenterButtons(self, center: bool) -> None:
    """
    Calls Qt's 'void QDialogButtonBox::setCenterButtons(bool center)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#setCenterButtons

    Parameters
    ----------

    center : bool
      Passed on as it is.
    """
    #  void QDialogButtonBox::setCenterButtons(bool center)
    self.uglySide.call(
        'ritual_ZN16QDialogButtonBox16setCenterButtonsEb', center,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDialogButtonBox::QDialogButtonBox(QWidget *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#QDialogButtonBox

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDialogButtonBox::QDialogButtonBox(QWidget *parent)
    self._noteCreation(QDialogButtonBox, lambda: Rituals.call(
        'ritual_ZN16QDialogButtonBoxC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(Qt.Orientation)
  @overload(Qt.Orientation, QWidget)
  @overload(Qt.Orientation, NoneType)
  def __init__(
      self,
      orientation: Qt.Orientation,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDialogButtonBox::QDialogButtonBox(Qt::Orientation orientation, QWidget
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#QDialogButtonBox

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDialogButtonBox::QDialogButtonBox(Qt::Orientation orientation,
    #      QWidget *parent)
    self._noteCreation(QDialogButtonBox, lambda: Rituals.call(
        'ritual_ZN16QDialogButtonBoxC1EN2Qt11OrientationEP7QWidget',
        orientation.value, self._addressOf(parent),
    ))

  @overload(StandardButtons)
  @overload(StandardButtons, QWidget)
  @overload(StandardButtons, NoneType)
  def __init__(
      self,
      buttons: StandardButtons,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDialogButtonBox::QDialogButtonBox(StandardButtons buttons, QWidget
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#QDialogButtonBox

    Parameters
    ----------

    buttons : StandardButtons
      Passed on as its number.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDialogButtonBox::QDialogButtonBox(StandardButtons buttons, QWidget
    #      *parent)
    self._noteCreation(QDialogButtonBox, lambda: Rituals.call(
        'ritual_ZN16QDialogButtonBoxC1E6QFlagsINS_14StandardButtonEEP7QWidg'
        'et',
        buttons.value, self._addressOf(parent),
    ))

  @overload(StandardButtons, Qt.Orientation)
  @overload(StandardButtons, Qt.Orientation, QWidget)
  @overload(StandardButtons, Qt.Orientation, NoneType)
  def __init__(
      self,
      buttons: StandardButtons,
      orientation: Qt.Orientation,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDialogButtonBox::QDialogButtonBox(StandardButtons buttons,
    Qt::Orientation orientation, QWidget *parent)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#QDialogButtonBox

    Parameters
    ----------

    buttons : StandardButtons
      Passed on as its number.

    orientation : Qt.Orientation
      Passed on as its number.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDialogButtonBox::QDialogButtonBox(StandardButtons buttons,
    #      Qt::Orientation orientation, QWidget *parent)
    self._noteCreation(QDialogButtonBox, lambda: Rituals.call(
        'ritual_ZN16QDialogButtonBoxC1E6QFlagsINS_14StandardButtonEEN2Qt11O'
        'rientationEP7QWidget',
        buttons.value, orientation.value, self._addressOf(parent),
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

  @overload(QAbstractButton, ButtonRole)
  @overload(NoneType, ButtonRole)
  def addButton(
      self,
      button: Optional[QAbstractButton],
      role: ButtonRole,
  ) -> None:
    """
    Calls Qt's 'void QDialogButtonBox::addButton(QAbstractButton *button,
    ButtonRole role)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#addButton

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    role : ButtonRole
      Passed on as its number.
    """
    #  void QDialogButtonBox::addButton(QAbstractButton *button, ButtonRole
    #      role)
    self.uglySide.call(
        'ritual_ZN16QDialogButtonBox9addButtonEP15QAbstractButtonNS_10Butto'
        'nRoleE',
        self._addressOf(button), role.value,
    )

  @overload(str, ButtonRole)
  def addButton(self, text: str, role: ButtonRole) -> Optional[QPushButton]:
    """
    Calls Qt's 'QPushButton *QDialogButtonBox::addButton(const QString &text,
    ButtonRole role)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#addButton

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    role : ButtonRole
      Passed on as its number.

    Returns
    -------

    Optional[QPushButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPushButton *QDialogButtonBox::addButton(const QString &text,
    #      ButtonRole role)
    address = self.uglySide.call(
        'ritual_ZN16QDialogButtonBox9addButtonERK7QStringNS_10ButtonRoleE',
        text, role.value,
    )
    from . import QPushButton
    return QPushButton._cuteAt(address)

  @overload(StandardButton)
  def addButton(self, button: StandardButton) -> Optional[QPushButton]:
    """
    Calls Qt's 'QPushButton *QDialogButtonBox::addButton(StandardButton
    button)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#addButton

    Parameters
    ----------

    button : StandardButton
      Passed on as its number.

    Returns
    -------

    Optional[QPushButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPushButton *QDialogButtonBox::addButton(StandardButton button)
    address = self.uglySide.call(
        'ritual_ZN16QDialogButtonBox9addButtonENS_14StandardButtonE',
        button.value,
    )
    from . import QPushButton
    return QPushButton._cuteAt(address)

  @overload(QAbstractButton)
  @overload(NoneType)
  def removeButton(self, button: Optional[QAbstractButton]) -> None:
    """
    Calls Qt's 'void QDialogButtonBox::removeButton(QAbstractButton
    *button)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#removeButton

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialogButtonBox::removeButton(QAbstractButton *button)
    self.uglySide.call(
        'ritual_ZN16QDialogButtonBox12removeButtonEP15QAbstractButton',
        self._addressOf(button),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QDialogButtonBox::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#clear
    """
    #  void QDialogButtonBox::clear()
    self.uglySide.call('ritual_ZN16QDialogButtonBox5clearEv')

  @overload(QAbstractButton)
  @overload(NoneType)
  def clicked(self, button: Optional[QAbstractButton]) -> None:
    """
    Calls Qt's 'void QDialogButtonBox::clicked(QAbstractButton *button)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#clicked

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialogButtonBox::clicked(QAbstractButton *button)
    self.uglySide.call(
        'ritual_ZN16QDialogButtonBox7clickedEP15QAbstractButton',
        self._addressOf(button),
    )

  def accepted(self) -> None:
    """
    Calls Qt's 'void QDialogButtonBox::accepted()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#accepted
    """
    #  void QDialogButtonBox::accepted()
    self.uglySide.call('ritual_ZN16QDialogButtonBox8acceptedEv')

  def helpRequested(self) -> None:
    """
    Calls Qt's 'void QDialogButtonBox::helpRequested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdialogbuttonbox.html#helpRequested
    """
    #  void QDialogButtonBox::helpRequested()
    self.uglySide.call('ritual_ZN16QDialogButtonBox13helpRequestedEv')

  def rejected(self) -> None:
    """
    Calls Qt's 'void QDialogButtonBox::rejected()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#rejected
    """
    #  void QDialogButtonBox::rejected()
    self.uglySide.call('ritual_ZN16QDialogButtonBox8rejectedEv')

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QDialogButtonBox::changeEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#changeEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDialogButtonBox::changeEvent(QEvent *event)
    ritual = 'ritual_ZN16QDialogButtonBox11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QDialogButtonBox11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QDialogButtonBox::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QDialogButtonBox::event(QEvent *event)
    ritual = 'ritual_ZN16QDialogButtonBox5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QDialogButtonBox5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QDialogButtonBoxPrivate]:
    """
    Calls Qt's 'QDialogButtonBoxPrivate *QDialogButtonBox::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdialogbuttonbox.html#d_func

    Returns
    -------

    Optional[QDialogButtonBoxPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDialogButtonBoxPrivate *QDialogButtonBox::d_func()
    address = self.uglySide.call('ritual_ZN16QDialogButtonBox6d_funcEv')
    from . import QDialogButtonBoxPrivate
    return QDialogButtonBoxPrivate._cuteAt(address)
