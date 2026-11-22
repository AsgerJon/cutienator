"""
QMessageBox binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qmessagebox.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QPixmap
  from . import QAbstractButton, QCheckBox, QPushButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractButton = WAIT['QAbstractButton']
  QCheckBox = WAIT['QCheckBox']
  QPixmap = WAIT['QPixmap']
  QPushButton = WAIT['QPushButton']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMessageBox(QDialog):
  """
  The cute side of Qt's QMessageBox: a plain Python object standing in front
  of one C++ QMessageBox.

  It is built on the cute 'QDialog', as Qt's QMessageBox is built on Qt's
  QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMessageBox that has a ritual and that Python can
  call so far, 46 names in all: 'metaObject', 'tr', 'addButton',
  'removeButton', 'open', 'buttonRole', 'setStandardButtons',
  'standardButtons', 'standardButton', 'button', 'defaultButton',
  'setDefaultButton', 'escapeButton', 'setEscapeButton', 'clickedButton',
  'text', 'setText', 'icon', 'setIcon', 'iconPixmap', 'setIconPixmap',
  'textFormat', 'setTextFormat', 'setTextInteractionFlags',
  'textInteractionFlags', 'setCheckBox', 'checkBox', 'setOption',
  'testOption', 'setOptions', 'options', 'information', 'question',
  'warning', 'critical', 'about', 'aboutQt', 'buttonText', 'setButtonText',
  'informativeText', 'setInformativeText', 'detailedText', 'setDetailedText',
  'setWindowTitle', 'setWindowModality', 'standardIcon'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMessageBox::~QMessageBox()': the destructor: Python never removes
    a C++ QMessageBox.
  - Qt's 'StandardButton QMessageBox::information(QWidget *parent, const
    QString &title, const QString &text, StandardButton button0,
    StandardButton button1)': takes in Python what 'StandardButton
    QMessageBox::information(QWidget *parent, const QString &title, const
    QString &text, StandardButtons buttons, StandardButton defaultButton)'
    takes.
  - Qt's 'int QMessageBox::question(QWidget *parent, const QString &title,
    const QString &text, StandardButton button0, StandardButton button1)':
    takes in Python what 'StandardButton QMessageBox::question(QWidget
    *parent, const QString &title, const QString &text, StandardButtons
    buttons, StandardButton defaultButton)' takes.
  - Qt's 'int QMessageBox::warning(QWidget *parent, const QString &title,
    const QString &text, StandardButton button0, StandardButton button1)':
    takes in Python what 'StandardButton QMessageBox::warning(QWidget
    *parent, const QString &title, const QString &text, StandardButtons
    buttons, StandardButton defaultButton)' takes.
  - Qt's 'int QMessageBox::critical(QWidget *parent, const QString &title,
    const QString &text, StandardButton button0, StandardButton button1)':
    takes in Python what 'StandardButton QMessageBox::critical(QWidget
    *parent, const QString &title, const QString &text, StandardButtons
    buttons, StandardButton defaultButton)' takes.

  What has no ritual
  ------------------

  16 of the 82 functions Qt declares: 6 protected; 3 takes or gives a type
  that cannot be passed yet; 3 private; 2 forbidden; 1 a template; 1 a
  signal.

  What to expect
  --------------

  - The C++ QMessageBox is created at the first use, not by
    'QMessageBox(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMessageBox.
  - Qt tells when it has removed the C++ QMessageBox. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QMessageBox, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ButtonRole(CuteNum):
    """
    The enum 'QMessageBox::ButtonRole' of Qt, with the 11 names Qt gives in
    it.
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

  class Icon(CuteNum):
    """
    The enum 'QMessageBox::Icon' of Qt, with the 5 names Qt gives in it.
    """

    NoIcon = Kee[int](0)
    Information = Kee[int](1)
    Warning = Kee[int](2)
    Critical = Kee[int](3)
    Question = Kee[int](4)

  class Option(CuteFlags, scoped=True):
    """
    The flags enum 'QMessageBox::Option' of Qt, with the 1 names Qt gives in
    it. Qt names the type of its combinations 'QMessageBox::Options'. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    DontUseNativeDialog = 0x1

  Options = Option

  class StandardButton(CuteFlags):
    """
    The flags enum 'QMessageBox::StandardButton' of Qt, with the 27 names Qt
    gives in it. Qt names the type of its combinations
    'QMessageBox::StandardButtons'.
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
    YesAll = 0x8000
    NoAll = 0x20000
    Default = 0x100
    Escape = 0x200
    FlagMask = 0x300
    ButtonMask = -769

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
    Calls Qt's 'QString QMessageBox::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#tr

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
    #  QString QMessageBox::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QMessageBox2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  @overload(QWidget, str, str, StandardButtons)
  @overload(NoneType, str, str, StandardButtons)
  @overload(QWidget, str, str, StandardButtons, StandardButton)
  @overload(NoneType, str, str, StandardButtons, StandardButton)
  def information(
      parent: Optional[QWidget],
      title: str,
      text: str,
      buttons: StandardButtons = StandardButtons.Ok,
      defaultButton: StandardButton = StandardButton.NoButton,
  ) -> StandardButton:
    """
    Calls Qt's 'StandardButton QMessageBox::information(QWidget *parent,
    const QString &title, const QString &text, StandardButtons buttons,
    StandardButton defaultButton)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#information

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    buttons : StandardButtons
      Passed on as its number. May be left out, as in Qt: it is then
      StandardButtons.Ok.

    defaultButton : StandardButton
      Passed on as its number. May be left out, as in Qt: it is then
      StandardButton.NoButton.

    Returns
    -------

    StandardButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StandardButton(number)'
      gives.
    """
    #  StandardButton QMessageBox::information(QWidget *parent, const QString
    #      &title, const QString &text, StandardButtons buttons,
    #      StandardButton defaultButton)
    return QMessageBox.StandardButton(Rituals.call(
        'ritual_ZN11QMessageBox11informationEP7QWidgetRK7QStringS4_6QFlagsI'
        'NS_14StandardButtonEES6_',
        CuteMixin._addressOf(parent), title, text, buttons.value,
        defaultButton.value,
    ))

  @staticmethod
  @overload(QWidget, str, str, int)
  @overload(NoneType, str, str, int)
  @overload(QWidget, str, str, int, int)
  @overload(NoneType, str, str, int, int)
  @overload(QWidget, str, str, int, int, int)
  @overload(NoneType, str, str, int, int, int)
  def information(
      parent: Optional[QWidget],
      title: str,
      text: str,
      button0: int,
      button1: int = 0,
      button2: int = 0,
  ) -> int:
    """
    Calls Qt's 'int QMessageBox::information(QWidget *parent, const QString
    &title, const QString &text, int button0, int button1, int button2)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#information

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    button0 : int
      Passed on as it is.

    button1 : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    button2 : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QMessageBox::information(QWidget *parent, const QString &title,
    #      const QString &text, int button0, int button1, int button2)
    return Rituals.call(
        'ritual_ZN11QMessageBox11informationEP7QWidgetRK7QStringS4_iii',
        CuteMixin._addressOf(parent), title, text, button0, button1, button2,
    )

  @staticmethod
  @overload(QWidget, str, str, str)
  @overload(NoneType, str, str, str)
  @overload(QWidget, str, str, str, str)
  @overload(NoneType, str, str, str, str)
  @overload(QWidget, str, str, str, str, str)
  @overload(NoneType, str, str, str, str, str)
  @overload(QWidget, str, str, str, str, str, int)
  @overload(NoneType, str, str, str, str, str, int)
  @overload(QWidget, str, str, str, str, str, int, int)
  @overload(NoneType, str, str, str, str, str, int, int)
  def information(
      parent: Optional[QWidget],
      title: str,
      text: str,
      button0Text: str,
      button1Text: str = '',
      button2Text: str = '',
      defaultButtonNumber: int = 0,
      escapeButtonNumber: int = -1,
  ) -> int:
    """
    Calls Qt's 'int QMessageBox::information(QWidget *parent, const QString
    &title, const QString &text, const QString &button0Text, const QString
    &button1Text, const QString &button2Text, int defaultButtonNumber, int
    escapeButtonNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#information

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    button0Text : str
      Passed on as it is: a QString is made of it for the call.

    button1Text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    button2Text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    defaultButtonNumber : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    escapeButtonNumber : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QMessageBox::information(QWidget *parent, const QString &title,
    #      const QString &text, const QString &button0Text, const QString
    #      &button1Text, const QString &button2Text, int defaultButtonNumber,
    #      int escapeButtonNumber)
    return Rituals.call(
        'ritual_ZN11QMessageBox11informationEP7QWidgetRK7QStringS4_S4_S4_S4'
        '_ii',
        CuteMixin._addressOf(parent), title, text, button0Text, button1Text,
        button2Text, defaultButtonNumber, escapeButtonNumber,
    )

  @staticmethod
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  @overload(QWidget, str, str, StandardButtons)
  @overload(NoneType, str, str, StandardButtons)
  @overload(QWidget, str, str, StandardButtons, StandardButton)
  @overload(NoneType, str, str, StandardButtons, StandardButton)
  def question(
      parent: Optional[QWidget],
      title: str,
      text: str,
      buttons: StandardButtons = StandardButtons.Yes | StandardButtons.No,
      defaultButton: StandardButton = StandardButton.NoButton,
  ) -> StandardButton:
    """
    Calls Qt's 'StandardButton QMessageBox::question(QWidget *parent, const
    QString &title, const QString &text, StandardButtons buttons,
    StandardButton defaultButton)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#question

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    buttons : StandardButtons
      Passed on as its number. May be left out, as in Qt: it is then
      StandardButtons.Yes | StandardButtons.No.

    defaultButton : StandardButton
      Passed on as its number. May be left out, as in Qt: it is then
      StandardButton.NoButton.

    Returns
    -------

    StandardButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StandardButton(number)'
      gives.
    """
    #  StandardButton QMessageBox::question(QWidget *parent, const QString
    #      &title, const QString &text, StandardButtons buttons,
    #      StandardButton defaultButton)
    return QMessageBox.StandardButton(Rituals.call(
        'ritual_ZN11QMessageBox8questionEP7QWidgetRK7QStringS4_6QFlagsINS_1'
        '4StandardButtonEES6_',
        CuteMixin._addressOf(parent), title, text, buttons.value,
        defaultButton.value,
    ))

  @staticmethod
  @overload(QWidget, str, str, int)
  @overload(NoneType, str, str, int)
  @overload(QWidget, str, str, int, int)
  @overload(NoneType, str, str, int, int)
  @overload(QWidget, str, str, int, int, int)
  @overload(NoneType, str, str, int, int, int)
  def question(
      parent: Optional[QWidget],
      title: str,
      text: str,
      button0: int,
      button1: int = 0,
      button2: int = 0,
  ) -> int:
    """
    Calls Qt's 'int QMessageBox::question(QWidget *parent, const QString
    &title, const QString &text, int button0, int button1, int button2)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#question

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    button0 : int
      Passed on as it is.

    button1 : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    button2 : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QMessageBox::question(QWidget *parent, const QString &title, const
    #      QString &text, int button0, int button1, int button2)
    return Rituals.call(
        'ritual_ZN11QMessageBox8questionEP7QWidgetRK7QStringS4_iii',
        CuteMixin._addressOf(parent), title, text, button0, button1, button2,
    )

  @staticmethod
  @overload(QWidget, str, str, str)
  @overload(NoneType, str, str, str)
  @overload(QWidget, str, str, str, str)
  @overload(NoneType, str, str, str, str)
  @overload(QWidget, str, str, str, str, str)
  @overload(NoneType, str, str, str, str, str)
  @overload(QWidget, str, str, str, str, str, int)
  @overload(NoneType, str, str, str, str, str, int)
  @overload(QWidget, str, str, str, str, str, int, int)
  @overload(NoneType, str, str, str, str, str, int, int)
  def question(
      parent: Optional[QWidget],
      title: str,
      text: str,
      button0Text: str,
      button1Text: str = '',
      button2Text: str = '',
      defaultButtonNumber: int = 0,
      escapeButtonNumber: int = -1,
  ) -> int:
    """
    Calls Qt's 'int QMessageBox::question(QWidget *parent, const QString
    &title, const QString &text, const QString &button0Text, const QString
    &button1Text, const QString &button2Text, int defaultButtonNumber, int
    escapeButtonNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#question

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    button0Text : str
      Passed on as it is: a QString is made of it for the call.

    button1Text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    button2Text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    defaultButtonNumber : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    escapeButtonNumber : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QMessageBox::question(QWidget *parent, const QString &title, const
    #      QString &text, const QString &button0Text, const QString
    #      &button1Text, const QString &button2Text, int defaultButtonNumber,
    #      int escapeButtonNumber)
    return Rituals.call(
        'ritual_ZN11QMessageBox8questionEP7QWidgetRK7QStringS4_S4_S4_S4_ii',
        CuteMixin._addressOf(parent), title, text, button0Text, button1Text,
        button2Text, defaultButtonNumber, escapeButtonNumber,
    )

  @staticmethod
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  @overload(QWidget, str, str, StandardButtons)
  @overload(NoneType, str, str, StandardButtons)
  @overload(QWidget, str, str, StandardButtons, StandardButton)
  @overload(NoneType, str, str, StandardButtons, StandardButton)
  def warning(
      parent: Optional[QWidget],
      title: str,
      text: str,
      buttons: StandardButtons = StandardButtons.Ok,
      defaultButton: StandardButton = StandardButton.NoButton,
  ) -> StandardButton:
    """
    Calls Qt's 'StandardButton QMessageBox::warning(QWidget *parent, const
    QString &title, const QString &text, StandardButtons buttons,
    StandardButton defaultButton)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#warning

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    buttons : StandardButtons
      Passed on as its number. May be left out, as in Qt: it is then
      StandardButtons.Ok.

    defaultButton : StandardButton
      Passed on as its number. May be left out, as in Qt: it is then
      StandardButton.NoButton.

    Returns
    -------

    StandardButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StandardButton(number)'
      gives.
    """
    #  StandardButton QMessageBox::warning(QWidget *parent, const QString
    #      &title, const QString &text, StandardButtons buttons,
    #      StandardButton defaultButton)
    return QMessageBox.StandardButton(Rituals.call(
        'ritual_ZN11QMessageBox7warningEP7QWidgetRK7QStringS4_6QFlagsINS_14'
        'StandardButtonEES6_',
        CuteMixin._addressOf(parent), title, text, buttons.value,
        defaultButton.value,
    ))

  @staticmethod
  @overload(QWidget, str, str, int, int)
  @overload(NoneType, str, str, int, int)
  @overload(QWidget, str, str, int, int, int)
  @overload(NoneType, str, str, int, int, int)
  def warning(
      parent: Optional[QWidget],
      title: str,
      text: str,
      button0: int,
      button1: int,
      button2: int = 0,
  ) -> int:
    """
    Calls Qt's 'int QMessageBox::warning(QWidget *parent, const QString
    &title, const QString &text, int button0, int button1, int button2)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#warning

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    button0 : int
      Passed on as it is.

    button1 : int
      Passed on as it is.

    button2 : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QMessageBox::warning(QWidget *parent, const QString &title, const
    #      QString &text, int button0, int button1, int button2)
    return Rituals.call(
        'ritual_ZN11QMessageBox7warningEP7QWidgetRK7QStringS4_iii',
        CuteMixin._addressOf(parent), title, text, button0, button1, button2,
    )

  @staticmethod
  @overload(QWidget, str, str, str)
  @overload(NoneType, str, str, str)
  @overload(QWidget, str, str, str, str)
  @overload(NoneType, str, str, str, str)
  @overload(QWidget, str, str, str, str, str)
  @overload(NoneType, str, str, str, str, str)
  @overload(QWidget, str, str, str, str, str, int)
  @overload(NoneType, str, str, str, str, str, int)
  @overload(QWidget, str, str, str, str, str, int, int)
  @overload(NoneType, str, str, str, str, str, int, int)
  def warning(
      parent: Optional[QWidget],
      title: str,
      text: str,
      button0Text: str,
      button1Text: str = '',
      button2Text: str = '',
      defaultButtonNumber: int = 0,
      escapeButtonNumber: int = -1,
  ) -> int:
    """
    Calls Qt's 'int QMessageBox::warning(QWidget *parent, const QString
    &title, const QString &text, const QString &button0Text, const QString
    &button1Text, const QString &button2Text, int defaultButtonNumber, int
    escapeButtonNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#warning

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    button0Text : str
      Passed on as it is: a QString is made of it for the call.

    button1Text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    button2Text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    defaultButtonNumber : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    escapeButtonNumber : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QMessageBox::warning(QWidget *parent, const QString &title, const
    #      QString &text, const QString &button0Text, const QString
    #      &button1Text, const QString &button2Text, int defaultButtonNumber,
    #      int escapeButtonNumber)
    return Rituals.call(
        'ritual_ZN11QMessageBox7warningEP7QWidgetRK7QStringS4_S4_S4_S4_ii',
        CuteMixin._addressOf(parent), title, text, button0Text, button1Text,
        button2Text, defaultButtonNumber, escapeButtonNumber,
    )

  @staticmethod
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  @overload(QWidget, str, str, StandardButtons)
  @overload(NoneType, str, str, StandardButtons)
  @overload(QWidget, str, str, StandardButtons, StandardButton)
  @overload(NoneType, str, str, StandardButtons, StandardButton)
  def critical(
      parent: Optional[QWidget],
      title: str,
      text: str,
      buttons: StandardButtons = StandardButtons.Ok,
      defaultButton: StandardButton = StandardButton.NoButton,
  ) -> StandardButton:
    """
    Calls Qt's 'StandardButton QMessageBox::critical(QWidget *parent, const
    QString &title, const QString &text, StandardButtons buttons,
    StandardButton defaultButton)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#critical

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    buttons : StandardButtons
      Passed on as its number. May be left out, as in Qt: it is then
      StandardButtons.Ok.

    defaultButton : StandardButton
      Passed on as its number. May be left out, as in Qt: it is then
      StandardButton.NoButton.

    Returns
    -------

    StandardButton
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StandardButton(number)'
      gives.
    """
    #  StandardButton QMessageBox::critical(QWidget *parent, const QString
    #      &title, const QString &text, StandardButtons buttons,
    #      StandardButton defaultButton)
    return QMessageBox.StandardButton(Rituals.call(
        'ritual_ZN11QMessageBox8criticalEP7QWidgetRK7QStringS4_6QFlagsINS_1'
        '4StandardButtonEES6_',
        CuteMixin._addressOf(parent), title, text, buttons.value,
        defaultButton.value,
    ))

  @staticmethod
  @overload(QWidget, str, str, int, int)
  @overload(NoneType, str, str, int, int)
  @overload(QWidget, str, str, int, int, int)
  @overload(NoneType, str, str, int, int, int)
  def critical(
      parent: Optional[QWidget],
      title: str,
      text: str,
      button0: int,
      button1: int,
      button2: int = 0,
  ) -> int:
    """
    Calls Qt's 'int QMessageBox::critical(QWidget *parent, const QString
    &title, const QString &text, int button0, int button1, int button2)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#critical

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    button0 : int
      Passed on as it is.

    button1 : int
      Passed on as it is.

    button2 : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  int QMessageBox::critical(QWidget *parent, const QString &title, const
    #      QString &text, int button0, int button1, int button2)
    return Rituals.call(
        'ritual_ZN11QMessageBox8criticalEP7QWidgetRK7QStringS4_iii',
        CuteMixin._addressOf(parent), title, text, button0, button1, button2,
    )

  @staticmethod
  @overload(QWidget, str, str, str)
  @overload(NoneType, str, str, str)
  @overload(QWidget, str, str, str, str)
  @overload(NoneType, str, str, str, str)
  @overload(QWidget, str, str, str, str, str)
  @overload(NoneType, str, str, str, str, str)
  @overload(QWidget, str, str, str, str, str, int)
  @overload(NoneType, str, str, str, str, str, int)
  @overload(QWidget, str, str, str, str, str, int, int)
  @overload(NoneType, str, str, str, str, str, int, int)
  def critical(
      parent: Optional[QWidget],
      title: str,
      text: str,
      button0Text: str,
      button1Text: str = '',
      button2Text: str = '',
      defaultButtonNumber: int = 0,
      escapeButtonNumber: int = -1,
  ) -> int:
    """
    Calls Qt's 'int QMessageBox::critical(QWidget *parent, const QString
    &title, const QString &text, const QString &button0Text, const QString
    &button1Text, const QString &button2Text, int defaultButtonNumber, int
    escapeButtonNumber)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#critical

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    button0Text : str
      Passed on as it is: a QString is made of it for the call.

    button1Text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    button2Text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    defaultButtonNumber : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    escapeButtonNumber : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  int QMessageBox::critical(QWidget *parent, const QString &title, const
    #      QString &text, const QString &button0Text, const QString
    #      &button1Text, const QString &button2Text, int defaultButtonNumber,
    #      int escapeButtonNumber)
    return Rituals.call(
        'ritual_ZN11QMessageBox8criticalEP7QWidgetRK7QStringS4_S4_S4_S4_ii',
        CuteMixin._addressOf(parent), title, text, button0Text, button1Text,
        button2Text, defaultButtonNumber, escapeButtonNumber,
    )

  @staticmethod
  @overload(QWidget, str, str)
  @overload(NoneType, str, str)
  def about(parent: Optional[QWidget], title: str, text: str) -> None:
    """
    Calls Qt's 'void QMessageBox::about(QWidget *parent, const QString
    &title, const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#about

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMessageBox::about(QWidget *parent, const QString &title, const
    #      QString &text)
    Rituals.call(
        'ritual_ZN11QMessageBox5aboutEP7QWidgetRK7QStringS4_',
        CuteMixin._addressOf(parent), title, text,
    )

  @staticmethod
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, str)
  @overload(NoneType, str)
  def aboutQt(parent: Optional[QWidget], title: str = '') -> None:
    """
    Calls Qt's 'void QMessageBox::aboutQt(QWidget *parent, const QString
    &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#aboutQt

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    title : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QMessageBox::aboutQt(QWidget *parent, const QString &title)
    Rituals.call(
        'ritual_ZN11QMessageBox7aboutQtEP7QWidgetRK7QString',
        CuteMixin._addressOf(parent), title,
    )

  @staticmethod
  @overload(Icon)
  def standardIcon(icon: Icon) -> QPixmap:
    """
    Calls Qt's 'QPixmap QMessageBox::standardIcon(Icon icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#standardIcon

    Parameters
    ----------

    icon : Icon
      Passed on as its number.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QMessageBox::standardIcon(Icon icon)
    address = Rituals.call(
        'ritual_ZN11QMessageBox12standardIconENS_4IconE', icon.value,
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMessageBox'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMessageBox::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMessageBox::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QMessageBox10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QAbstractButton)
  @overload(NoneType)
  def buttonRole(self, button: Optional[QAbstractButton]) -> ButtonRole:
    """
    Calls Qt's 'ButtonRole QMessageBox::buttonRole(QAbstractButton *button)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#buttonRole

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
    #  ButtonRole QMessageBox::buttonRole(QAbstractButton *button) const
    return QMessageBox.ButtonRole(self.uglySide.call(
        'ritual_ZNK11QMessageBox10buttonRoleEP15QAbstractButton',
        self._addressOf(button),
    ))

  def standardButtons(self) -> StandardButtons:
    """
    Calls Qt's 'StandardButtons QMessageBox::standardButtons() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#standardButtons

    Returns
    -------

    StandardButtons
      The value standing for the combination Qt gave back.
    """
    #  StandardButtons QMessageBox::standardButtons() const
    return QMessageBox.StandardButtons(self.uglySide.call(
        'ritual_ZNK11QMessageBox15standardButtonsEv',
    ))

  @overload(QAbstractButton)
  @overload(NoneType)
  def standardButton(
      self,
      button: Optional[QAbstractButton],
  ) -> StandardButton:
    """
    Calls Qt's 'StandardButton QMessageBox::standardButton(QAbstractButton
    *button) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#standardButton

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
    #  StandardButton QMessageBox::standardButton(QAbstractButton *button)
    #      const
    return QMessageBox.StandardButton(self.uglySide.call(
        'ritual_ZNK11QMessageBox14standardButtonEP15QAbstractButton',
        self._addressOf(button),
    ))

  @overload(StandardButton)
  def button(self, which: StandardButton) -> Optional[QAbstractButton]:
    """
    Calls Qt's 'QAbstractButton *QMessageBox::button(StandardButton which)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#button

    Parameters
    ----------

    which : StandardButton
      Passed on as its number.

    Returns
    -------

    Optional[QAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractButton *QMessageBox::button(StandardButton which) const
    address = self.uglySide.call(
        'ritual_ZNK11QMessageBox6buttonENS_14StandardButtonE', which.value,
    )
    from . import QAbstractButton
    return QAbstractButton._cuteAt(address)

  def defaultButton(self) -> Optional[QPushButton]:
    """
    Calls Qt's 'QPushButton *QMessageBox::defaultButton() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#defaultButton

    Returns
    -------

    Optional[QPushButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPushButton *QMessageBox::defaultButton() const
    address = self.uglySide.call('ritual_ZNK11QMessageBox13defaultButtonEv')
    from . import QPushButton
    return QPushButton._cuteAt(address)

  def escapeButton(self) -> Optional[QAbstractButton]:
    """
    Calls Qt's 'QAbstractButton *QMessageBox::escapeButton() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#escapeButton

    Returns
    -------

    Optional[QAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractButton *QMessageBox::escapeButton() const
    address = self.uglySide.call('ritual_ZNK11QMessageBox12escapeButtonEv')
    from . import QAbstractButton
    return QAbstractButton._cuteAt(address)

  def clickedButton(self) -> Optional[QAbstractButton]:
    """
    Calls Qt's 'QAbstractButton *QMessageBox::clickedButton() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#clickedButton

    Returns
    -------

    Optional[QAbstractButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractButton *QMessageBox::clickedButton() const
    address = self.uglySide.call('ritual_ZNK11QMessageBox13clickedButtonEv')
    from . import QAbstractButton
    return QAbstractButton._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QMessageBox::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMessageBox::text() const
    return self.uglySide.call('ritual_ZNK11QMessageBox4textEv')

  def icon(self) -> Icon:
    """
    Calls Qt's 'Icon QMessageBox::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#icon

    Returns
    -------

    Icon
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Icon(number)' gives.
    """
    #  Icon QMessageBox::icon() const
    return QMessageBox.Icon(self.uglySide.call(
        'ritual_ZNK11QMessageBox4iconEv',
    ))

  def iconPixmap(self) -> QPixmap:
    """
    Calls Qt's 'QPixmap QMessageBox::iconPixmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#iconPixmap

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QMessageBox::iconPixmap() const
    address = self.uglySide.call('ritual_ZNK11QMessageBox10iconPixmapEv')
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  def textFormat(self) -> Qt.TextFormat:
    """
    Calls Qt's 'Qt::TextFormat QMessageBox::textFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#textFormat

    Returns
    -------

    Qt.TextFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TextFormat(number)'
      gives.
    """
    #  Qt::TextFormat QMessageBox::textFormat() const
    return Qt.TextFormat(self.uglySide.call(
        'ritual_ZNK11QMessageBox10textFormatEv',
    ))

  def textInteractionFlags(self) -> Qt.TextInteractionFlags:
    """
    Calls Qt's 'Qt::TextInteractionFlags QMessageBox::textInteractionFlags()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagebox.html#textInteractionFlags

    Returns
    -------

    Qt.TextInteractionFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::TextInteractionFlags QMessageBox::textInteractionFlags() const
    return Qt.TextInteractionFlags(self.uglySide.call(
        'ritual_ZNK11QMessageBox20textInteractionFlagsEv',
    ))

  def checkBox(self) -> Optional[QCheckBox]:
    """
    Calls Qt's 'QCheckBox *QMessageBox::checkBox() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#checkBox

    Returns
    -------

    Optional[QCheckBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCheckBox *QMessageBox::checkBox() const
    address = self.uglySide.call('ritual_ZNK11QMessageBox8checkBoxEv')
    from . import QCheckBox
    return QCheckBox._cuteAt(address)

  @overload(Option)
  def testOption(self, option: Option) -> bool:
    """
    Calls Qt's 'bool QMessageBox::testOption(Option option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#testOption

    Parameters
    ----------

    option : Option
      Passed on as its number.
    """
    #  bool QMessageBox::testOption(Option option) const
    return self.uglySide.call(
        'ritual_ZNK11QMessageBox10testOptionENS_6OptionE', option.value,
    )

  def options(self) -> Options:
    """
    Calls Qt's 'Options QMessageBox::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#options

    Returns
    -------

    Options
      The value standing for the combination Qt gave back.
    """
    #  Options QMessageBox::options() const
    return QMessageBox.Options(self.uglySide.call(
        'ritual_ZNK11QMessageBox7optionsEv',
    ))

  @overload(int)
  def buttonText(self, button: int) -> str:
    """
    Calls Qt's 'QString QMessageBox::buttonText(int button) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#buttonText

    Parameters
    ----------

    button : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMessageBox::buttonText(int button) const
    return self.uglySide.call(
        'ritual_ZNK11QMessageBox10buttonTextEi', button,
    )

  def informativeText(self) -> str:
    """
    Calls Qt's 'QString QMessageBox::informativeText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#informativeText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMessageBox::informativeText() const
    return self.uglySide.call('ritual_ZNK11QMessageBox15informativeTextEv')

  def detailedText(self) -> str:
    """
    Calls Qt's 'QString QMessageBox::detailedText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#detailedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMessageBox::detailedText() const
    return self.uglySide.call('ritual_ZNK11QMessageBox12detailedTextEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(StandardButtons)
  def setStandardButtons(self, buttons: StandardButtons) -> None:
    """
    Calls Qt's 'void QMessageBox::setStandardButtons(StandardButtons
    buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagebox.html#setStandardButtons

    Parameters
    ----------

    buttons : StandardButtons
      Passed on as its number.
    """
    #  void QMessageBox::setStandardButtons(StandardButtons buttons)
    self.uglySide.call(
        'ritual_ZN11QMessageBox18setStandardButtonsE6QFlagsINS_14StandardBu'
        'ttonEE',
        buttons.value,
    )

  @overload(QPushButton)
  @overload(NoneType)
  def setDefaultButton(self, button: Optional[QPushButton]) -> None:
    """
    Calls Qt's 'void QMessageBox::setDefaultButton(QPushButton *button)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setDefaultButton

    Parameters
    ----------

    button : Optional[QPushButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMessageBox::setDefaultButton(QPushButton *button)
    self.uglySide.call(
        'ritual_ZN11QMessageBox16setDefaultButtonEP11QPushButton',
        self._addressOf(button),
    )

  @overload(StandardButton)
  def setDefaultButton(self, button: StandardButton) -> None:
    """
    Calls Qt's 'void QMessageBox::setDefaultButton(StandardButton button)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setDefaultButton

    Parameters
    ----------

    button : StandardButton
      Passed on as its number.
    """
    #  void QMessageBox::setDefaultButton(StandardButton button)
    self.uglySide.call(
        'ritual_ZN11QMessageBox16setDefaultButtonENS_14StandardButtonE',
        button.value,
    )

  @overload(QAbstractButton)
  @overload(NoneType)
  def setEscapeButton(self, button: Optional[QAbstractButton]) -> None:
    """
    Calls Qt's 'void QMessageBox::setEscapeButton(QAbstractButton *button)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setEscapeButton

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMessageBox::setEscapeButton(QAbstractButton *button)
    self.uglySide.call(
        'ritual_ZN11QMessageBox15setEscapeButtonEP15QAbstractButton',
        self._addressOf(button),
    )

  @overload(StandardButton)
  def setEscapeButton(self, button: StandardButton) -> None:
    """
    Calls Qt's 'void QMessageBox::setEscapeButton(StandardButton button)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setEscapeButton

    Parameters
    ----------

    button : StandardButton
      Passed on as its number.
    """
    #  void QMessageBox::setEscapeButton(StandardButton button)
    self.uglySide.call(
        'ritual_ZN11QMessageBox15setEscapeButtonENS_14StandardButtonE',
        button.value,
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QMessageBox::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMessageBox::setText(const QString &text)
    self.uglySide.call('ritual_ZN11QMessageBox7setTextERK7QString', text)

  @overload(Icon)
  def setIcon(self, a0: Icon) -> None:
    """
    Calls Qt's 'void QMessageBox::setIcon(Icon a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setIcon

    Parameters
    ----------

    a0 : Icon
      Passed on as its number.
    """
    #  void QMessageBox::setIcon(Icon a0)
    self.uglySide.call('ritual_ZN11QMessageBox7setIconENS_4IconE', a0.value)

  @overload(QPixmap)
  def setIconPixmap(self, pixmap: QPixmap) -> None:
    """
    Calls Qt's 'void QMessageBox::setIconPixmap(const QPixmap &pixmap)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setIconPixmap

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QMessageBox::setIconPixmap(const QPixmap &pixmap)
    self.uglySide.call(
        'ritual_ZN11QMessageBox13setIconPixmapERK7QPixmap',
        self._valueOf(pixmap),
    )

  @overload(Qt.TextFormat)
  def setTextFormat(self, format: Qt.TextFormat) -> None:
    """
    Calls Qt's 'void QMessageBox::setTextFormat(Qt::TextFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setTextFormat

    Parameters
    ----------

    format : Qt.TextFormat
      Passed on as its number.
    """
    #  void QMessageBox::setTextFormat(Qt::TextFormat format)
    self.uglySide.call(
        'ritual_ZN11QMessageBox13setTextFormatEN2Qt10TextFormatE',
        format.value,
    )

  @overload(Qt.TextInteractionFlags)
  def setTextInteractionFlags(self, flags: Qt.TextInteractionFlags) -> None:
    """
    Calls Qt's 'void
    QMessageBox::setTextInteractionFlags(Qt::TextInteractionFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagebox.html#setTextInteractionFlags

    Parameters
    ----------

    flags : Qt.TextInteractionFlags
      Passed on as its number.
    """
    #  void QMessageBox::setTextInteractionFlags(Qt::TextInteractionFlags
    #      flags)
    self.uglySide.call(
        'ritual_ZN11QMessageBox23setTextInteractionFlagsE6QFlagsIN2Qt19Text'
        'InteractionFlagEE',
        flags.value,
    )

  @overload(QCheckBox)
  @overload(NoneType)
  def setCheckBox(self, cb: Optional[QCheckBox]) -> None:
    """
    Calls Qt's 'void QMessageBox::setCheckBox(QCheckBox *cb)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setCheckBox

    Parameters
    ----------

    cb : Optional[QCheckBox]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMessageBox::setCheckBox(QCheckBox *cb)
    self.uglySide.call(
        'ritual_ZN11QMessageBox11setCheckBoxEP9QCheckBox',
        self._addressOf(cb),
    )

  @overload(Option)
  @overload(Option, bool)
  def setOption(self, option: Option, on: bool = True) -> None:
    """
    Calls Qt's 'void QMessageBox::setOption(Option option, bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setOption

    Parameters
    ----------

    option : Option
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QMessageBox::setOption(Option option, bool on)
    self.uglySide.call(
        'ritual_ZN11QMessageBox9setOptionENS_6OptionEb', option.value, on,
    )

  @overload(Options)
  def setOptions(self, options: Options) -> None:
    """
    Calls Qt's 'void QMessageBox::setOptions(Options options)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setOptions

    Parameters
    ----------

    options : Options
      Passed on as its number.
    """
    #  void QMessageBox::setOptions(Options options)
    self.uglySide.call(
        'ritual_ZN11QMessageBox10setOptionsE6QFlagsINS_6OptionEE',
        options.value,
    )

  @overload(int, str)
  def setButtonText(self, button: int, text: str) -> None:
    """
    Calls Qt's 'void QMessageBox::setButtonText(int button, const QString
    &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setButtonText

    Parameters
    ----------

    button : int
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMessageBox::setButtonText(int button, const QString &text)
    self.uglySide.call(
        'ritual_ZN11QMessageBox13setButtonTextEiRK7QString', button, text,
    )

  @overload(str)
  def setInformativeText(self, text: str) -> None:
    """
    Calls Qt's 'void QMessageBox::setInformativeText(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagebox.html#setInformativeText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMessageBox::setInformativeText(const QString &text)
    self.uglySide.call(
        'ritual_ZN11QMessageBox18setInformativeTextERK7QString', text,
    )

  @overload(str)
  def setDetailedText(self, text: str) -> None:
    """
    Calls Qt's 'void QMessageBox::setDetailedText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setDetailedText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMessageBox::setDetailedText(const QString &text)
    self.uglySide.call(
        'ritual_ZN11QMessageBox15setDetailedTextERK7QString', text,
    )

  @overload(str)
  def setWindowTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QMessageBox::setWindowTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setWindowTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMessageBox::setWindowTitle(const QString &title)
    self.uglySide.call(
        'ritual_ZN11QMessageBox14setWindowTitleERK7QString', title,
    )

  @overload(Qt.WindowModality)
  def setWindowModality(self, windowModality: Qt.WindowModality) -> None:
    """
    Calls Qt's 'void QMessageBox::setWindowModality(Qt::WindowModality
    windowModality)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#setWindowModality

    Parameters
    ----------

    windowModality : Qt.WindowModality
      Passed on as its number.
    """
    #  void QMessageBox::setWindowModality(Qt::WindowModality windowModality)
    self.uglySide.call(
        'ritual_ZN11QMessageBox17setWindowModalityEN2Qt14WindowModalityE',
        windowModality.value,
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
    Notes what was given, for Qt's 'QMessageBox::QMessageBox(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#QMessageBox

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMessageBox::QMessageBox(QWidget *parent)
    self._noteCreation(QMessageBox, lambda: Rituals.call(
        'ritual_ZN11QMessageBoxC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(Icon, str, str)
  @overload(Icon, str, str, StandardButtons)
  @overload(Icon, str, str, StandardButtons, QWidget)
  @overload(Icon, str, str, StandardButtons, NoneType)
  @overload(Icon, str, str, StandardButtons, QWidget, Qt.WindowFlags)
  @overload(Icon, str, str, StandardButtons, NoneType, Qt.WindowFlags)
  def __init__(
      self,
      icon: Icon,
      title: str,
      text: str,
      buttons: StandardButtons = StandardButtons.NoButton,
      parent: Optional[QWidget] = None,
      flags: Qt.WindowFlags = (
          Qt.WindowFlags.Dialog |
          Qt.WindowFlags.MSWindowsFixedSizeDialogHint),
  ) -> None:
    """
    Notes what was given, for Qt's 'QMessageBox::QMessageBox(Icon icon, const
    QString &title, const QString &text, StandardButtons buttons, QWidget
    *parent, Qt::WindowFlags flags)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#QMessageBox

    Parameters
    ----------

    icon : Icon
      Passed on as its number.

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    buttons : StandardButtons
      Passed on as its number. May be left out, as in Qt: it is then
      StandardButtons.NoButton.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    flags : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags.Dialog | Qt.WindowFlags.MSWindowsFixedSizeDialogHint.
    """
    #  QMessageBox::QMessageBox(Icon icon, const QString &title, const
    #      QString &text, StandardButtons buttons, QWidget *parent,
    #      Qt::WindowFlags flags)
    self._noteCreation(QMessageBox, lambda: Rituals.call(
        'ritual_ZN11QMessageBoxC1ENS_4IconERK7QStringS3_6QFlagsINS_14Standa'
        'rdButtonEEP7QWidgetS4_IN2Qt10WindowTypeEE',
        icon.value, title, text, buttons.value, self._addressOf(parent),
        flags.value,
    ))

  @overload(str, str, Icon, int, int, int)
  @overload(str, str, Icon, int, int, int, QWidget)
  @overload(str, str, Icon, int, int, int, NoneType)
  @overload(str, str, Icon, int, int, int, QWidget, Qt.WindowFlags)
  @overload(str, str, Icon, int, int, int, NoneType, Qt.WindowFlags)
  def __init__(
      self,
      title: str,
      text: str,
      icon: Icon,
      button0: int,
      button1: int,
      button2: int,
      parent: Optional[QWidget] = None,
      f: Qt.WindowFlags = (
          Qt.WindowFlags.Dialog |
          Qt.WindowFlags.MSWindowsFixedSizeDialogHint),
  ) -> None:
    """
    Notes what was given, for Qt's 'QMessageBox::QMessageBox(const QString
    &title, const QString &text, Icon icon, int button0, int button1, int
    button2, QWidget *parent, Qt::WindowFlags f)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#QMessageBox

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    text : str
      Passed on as it is: a QString is made of it for the call.

    icon : Icon
      Passed on as its number.

    button0 : int
      Passed on as it is.

    button1 : int
      Passed on as it is.

    button2 : int
      Passed on as it is.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    f : Qt.WindowFlags
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.WindowFlags.Dialog | Qt.WindowFlags.MSWindowsFixedSizeDialogHint.
    """
    #  QMessageBox::QMessageBox(const QString &title, const QString &text,
    #      Icon icon, int button0, int button1, int button2, QWidget *parent,
    #      Qt::WindowFlags f)
    self._noteCreation(QMessageBox, lambda: Rituals.call(
        'ritual_ZN11QMessageBoxC1ERK7QStringS2_NS_4IconEiiiP7QWidget6QFlags'
        'IN2Qt10WindowTypeEE',
        title, text, icon.value, button0, button1, button2,
        self._addressOf(parent), f.value,
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
    Calls Qt's 'void QMessageBox::addButton(QAbstractButton *button,
    ButtonRole role)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#addButton

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    role : ButtonRole
      Passed on as its number.
    """
    #  void QMessageBox::addButton(QAbstractButton *button, ButtonRole role)
    self.uglySide.call(
        'ritual_ZN11QMessageBox9addButtonEP15QAbstractButtonNS_10ButtonRole'
        'E',
        self._addressOf(button), role.value,
    )

  @overload(str, ButtonRole)
  def addButton(self, text: str, role: ButtonRole) -> Optional[QPushButton]:
    """
    Calls Qt's 'QPushButton *QMessageBox::addButton(const QString &text,
    ButtonRole role)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#addButton

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
    #  QPushButton *QMessageBox::addButton(const QString &text, ButtonRole
    #      role)
    address = self.uglySide.call(
        'ritual_ZN11QMessageBox9addButtonERK7QStringNS_10ButtonRoleE',
        text, role.value,
    )
    from . import QPushButton
    return QPushButton._cuteAt(address)

  @overload(StandardButton)
  def addButton(self, button: StandardButton) -> Optional[QPushButton]:
    """
    Calls Qt's 'QPushButton *QMessageBox::addButton(StandardButton button)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#addButton

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
    #  QPushButton *QMessageBox::addButton(StandardButton button)
    address = self.uglySide.call(
        'ritual_ZN11QMessageBox9addButtonENS_14StandardButtonE',
        button.value,
    )
    from . import QPushButton
    return QPushButton._cuteAt(address)

  @overload(QAbstractButton)
  @overload(NoneType)
  def removeButton(self, button: Optional[QAbstractButton]) -> None:
    """
    Calls Qt's 'void QMessageBox::removeButton(QAbstractButton *button)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#removeButton

    Parameters
    ----------

    button : Optional[QAbstractButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMessageBox::removeButton(QAbstractButton *button)
    self.uglySide.call(
        'ritual_ZN11QMessageBox12removeButtonEP15QAbstractButton',
        self._addressOf(button),
    )

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def open(self, receiver: Optional[QObject], member: Optional[str]) -> None:
    """
    Calls Qt's 'void QMessageBox::open(QObject *receiver, const char
    *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagebox.html#open

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QMessageBox::open(QObject *receiver, const char *member)
    self.uglySide.call(
        'ritual_ZN11QMessageBox4openEP7QObjectPKc',
        self._addressOf(receiver), self._bytesOf(member),
    )
