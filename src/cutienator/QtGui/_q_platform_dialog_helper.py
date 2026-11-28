"""
QPlatformDialogHelper binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
  from . import QWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformDialogHelper(QObject):
  """
  The cute side of Qt's QPlatformDialogHelper: a plain Python object standing
  in front of one C++ QPlatformDialogHelper.

  It is built on the cute 'QObject', as Qt's QPlatformDialogHelper is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformDialogHelper that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'styleHint',
  'exec', 'show', 'hide', 'defaultStyleHint', 'buttonRole', 'accept',
  'reject'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformDialogHelper::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlatformDialogHelper::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformDialogHelper::~QPlatformDialogHelper()': the destructor:
    Python never removes a C++ QPlatformDialogHelper.
  - Qt's 'const int *QPlatformDialogHelper::buttonLayout(Qt::Orientation
    orientation, ButtonLayout policy)': gives 'int', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 17 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformDialogHelper is created at the first use, not by
    'QPlatformDialogHelper(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformDialogHelper.
  - Qt tells when it has removed the C++ QPlatformDialogHelper. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformDialogHelper that has no cute function yet,
    'buttonLayout', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QPlatformDialogHelper, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ButtonLayout(CuteNum):
    """
    The enum 'QPlatformDialogHelper::ButtonLayout' of Qt, with the 6 names Qt
    gives in it.
    """

    UnknownLayout = Kee[int](-1)
    WinLayout = Kee[int](0)
    MacLayout = Kee[int](1)
    KdeLayout = Kee[int](2)
    GnomeLayout = Kee[int](3)
    AndroidLayout = Kee[int](4)

  class ButtonRole(CuteNum):
    """
    The enum 'QPlatformDialogHelper::ButtonRole' of Qt, with the 16 names Qt
    gives in it.
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
    RoleMask = Kee[int](268435455)
    AlternateRole = Kee[int](268435456)
    Stretch = Kee[int](536870912)
    Reverse = Kee[int](1073741824)
    EOL = Kee[int](-1)

  class DialogCode(CuteNum):
    """
    The enum 'QPlatformDialogHelper::DialogCode' of Qt, with the 2 names Qt
    gives in it.
    """

    Rejected = Kee[int](0)
    Accepted = Kee[int](1)

  class StandardButton(CuteFlags):
    """
    The flags enum 'QPlatformDialogHelper::StandardButton' of Qt, with the 23
    names Qt gives in it. Qt names the type of its combinations
    'QPlatformDialogHelper::StandardButtons'.
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
    LowestBit = 0xa
    HighestBit = 0x1b

  StandardButtons = StandardButton

  class StyleHint(CuteNum):
    """
    The enum 'QPlatformDialogHelper::StyleHint' of Qt, with the 1 names Qt
    gives in it.
    """

    DialogIsQtWindow = Kee[int](0)

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
    Calls Qt's 'QString QPlatformDialogHelper::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdialoghelper.html#tr

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
    #  QString QPlatformDialogHelper::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QPlatformDialogHelper2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(StyleHint)
  def defaultStyleHint(hint: StyleHint) -> QVariant:
    """
    Calls Qt's 'QVariant
    QPlatformDialogHelper::defaultStyleHint(QPlatformDialogHelper::StyleHint
    hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformdialoghelper.html#defaultStyleHint

    Parameters
    ----------

    hint : StyleHint
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant
    #      QPlatformDialogHelper::defaultStyleHint(QPlatformDialogHelper::
    #      StyleHint hint)
    address = Rituals.call(
        'ritual_ZN21QPlatformDialogHelper16defaultStyleHintENS_9StyleHintE',
        hint.value,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @staticmethod
  @overload(StandardButton)
  def buttonRole(button: StandardButton) -> ButtonRole:
    """
    Calls Qt's 'ButtonRole QPlatformDialogHelper::buttonRole(StandardButton
    button)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformdialoghelper.html#buttonRole

    Parameters
    ----------

    button : StandardButton
      Passed on as its number.

    Returns
    -------

    ButtonRole
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ButtonRole(number)'
      gives.
    """
    #  ButtonRole QPlatformDialogHelper::buttonRole(StandardButton button)
    return QPlatformDialogHelper.ButtonRole(Rituals.call(
        'ritual_ZN21QPlatformDialogHelper10buttonRoleENS_14StandardButtonE',
        button.value,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformDialogHelper'

  #  A C++ QPlatformDialogHelper Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformDialogHelper'

  #  The functions Qt calls itself that QPlatformDialogHelper is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'styleHint': (
          ('_ZNK21QPlatformDialogHelper9styleHintENS_9StyleHintE',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('int', 'enum', 'QtGui:QPlatformDialogHelper.StyleHint'),
           )),
      ),
      'exec': (
          ('_ZN21QPlatformDialogHelper4execEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'show': (
          ('_ZN21QPlatformDialogHelper4showE6QFlagsIN2Qt10WindowTypeEENS1_1'
           '4WindowModalityEP7QWindow',
           ('bool', 'number', ''),
           (
               ('int', 'flags', 'QtCore:Qt.WindowType'),
               ('int', 'enum', 'QtCore:Qt.WindowModality'),
               ('address', 'address', 'QtGui:QWindow'),
           )),
      ),
      'hide': (
          ('_ZN21QPlatformDialogHelper4hideEv',
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
    Calls Qt's 'const QMetaObject *QPlatformDialogHelper::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformdialoghelper.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformDialogHelper::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformDialogHelper10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(StyleHint)
  def styleHint(self, hint: StyleHint) -> QVariant:
    """
    Calls Qt's 'QVariant QPlatformDialogHelper::styleHint(StyleHint hint)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformdialoghelper.html#styleHint

    Parameters
    ----------

    hint : StyleHint
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlatformDialogHelper::styleHint(StyleHint hint) const
    ritual = 'ritual_ZNK21QPlatformDialogHelper9styleHintENS_9StyleHintE'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK21QPlatformDialogHelper9styleHintENS_9StyleHintE')
    address = self.uglySide.call(ritual, hint.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformDialogHelper::QPlatformDialogHelper()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformdialoghelper.html#QPlatformDialogHelper
    """
    #  QPlatformDialogHelper::QPlatformDialogHelper()
    self._noteCreation(QPlatformDialogHelper, lambda: Rituals.call(
        'ritual_ZN21QPlatformDialogHelperC1Ev',
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

  def exec(self) -> None:
    """
    Calls Qt's 'void QPlatformDialogHelper::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdialoghelper.html#exec
    """
    #  void QPlatformDialogHelper::exec()
    self.uglySide.call('ritual_ZN21QPlatformDialogHelper4execEv')

  @overload(Qt.WindowFlags, Qt.WindowModality, QWindow)
  @overload(Qt.WindowFlags, Qt.WindowModality, NoneType)
  def show(
      self,
      windowFlags: Qt.WindowFlags,
      windowModality: Qt.WindowModality,
      parent: Optional[QWindow],
  ) -> bool:
    """
    Calls Qt's 'bool QPlatformDialogHelper::show(Qt::WindowFlags windowFlags,
    Qt::WindowModality windowModality, QWindow *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdialoghelper.html#show

    Parameters
    ----------

    windowFlags : Qt.WindowFlags
      Passed on as its number.

    windowModality : Qt.WindowModality
      Passed on as its number.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QPlatformDialogHelper::show(Qt::WindowFlags windowFlags,
    #      Qt::WindowModality windowModality, QWindow *parent)
    return self.uglySide.call(
        'ritual_ZN21QPlatformDialogHelper4showE6QFlagsIN2Qt10WindowTypeEENS'
        '1_14WindowModalityEP7QWindow',
        windowFlags.value, windowModality.value, self._addressOf(parent),
    )

  def hide(self) -> None:
    """
    Calls Qt's 'void QPlatformDialogHelper::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdialoghelper.html#hide
    """
    #  void QPlatformDialogHelper::hide()
    self.uglySide.call('ritual_ZN21QPlatformDialogHelper4hideEv')

  def accept(self) -> None:
    """
    Calls Qt's 'void QPlatformDialogHelper::accept()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdialoghelper.html#accept
    """
    #  void QPlatformDialogHelper::accept()
    self.uglySide.call('ritual_ZN21QPlatformDialogHelper6acceptEv')

  def reject(self) -> None:
    """
    Calls Qt's 'void QPlatformDialogHelper::reject()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformdialoghelper.html#reject
    """
    #  void QPlatformDialogHelper::reject()
    self.uglySide.call('ritual_ZN21QPlatformDialogHelper6rejectEv')

  @staticmethod
  def buttonLayout(*__, **_) -> Never:
    """
    Qt's 'const int *QPlatformDialogHelper::buttonLayout(Qt::Orientation
    orientation, ButtonLayout policy)': gives 'int', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QPlatformDialogHelper.buttonLayout' has no cute function yet. "
        "Qt's 'const int "
        "*QPlatformDialogHelper::buttonLayout(Qt::Orientation orientation, "
        "ButtonLayout policy)': gives 'int', which has no cute class yet.")
