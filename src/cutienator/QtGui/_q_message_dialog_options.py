"""
QMessageDialogOptions binding of the Qt C++
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

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..QtCore import Qt
from . import QPlatformDialogHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPixmap = WAIT['QPixmap']


class QMessageDialogOptions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMessageDialogOptions: a plain Python object standing
  in front of one C++ QMessageDialogOptions.

  What exists
  -----------

  Every function of Qt's QMessageDialogOptions that has a ritual and that
  Python can call so far, 28 names in all: 'windowTitle', 'setWindowTitle',
  'setStandardIcon', 'standardIcon', 'setIconPixmap', 'iconPixmap',
  'setText', 'text', 'setInformativeText', 'informativeText',
  'setDetailedText', 'detailedText', 'setOption', 'testOption', 'setOptions',
  'options', 'setStandardButtons', 'standardButtons', 'removeButton',
  'customButton', 'clearCustomButtons', 'setCheckBox', 'checkBoxLabel',
  'checkBoxState', 'setEscapeButton', 'escapeButton', 'setDefaultButton',
  'defaultButton'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMessageDialogOptions::QMessageDialogOptions(
    QMessageDialogOptionsPrivate *dd)': names 'QMessageDialogOptionsPrivate',
    which has no cute class yet.
  - Qt's 'QMessageDialogOptions::~QMessageDialogOptions()': the destructor:
    Python never removes a C++ QMessageDialogOptions.
  - Qt's 'QSharedPointer<QMessageDialogOptions>
    QMessageDialogOptions::create()': gives a type Python has no way to take
    yet.
  - Qt's 'QSharedPointer<QMessageDialogOptions>
    QMessageDialogOptions::clone() const': gives a type Python has no way to
    take yet.
  - Qt's 'int QMessageDialogOptions::addButton(const QString &label,
    QPlatformDialogHelper::ButtonRole role, void *buttonImpl, int buttonId)':
    names 'void', which has no cute class yet.
  - Qt's 'const QList<CustomButton> &QMessageDialogOptions::customButtons()':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  5 of the 39 functions Qt declares: 3 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QMessageDialogOptions is created at the first use, not by
    'QMessageDialogOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMessageDialogOptions.
  - Each name of Qt's QMessageDialogOptions that has no cute function yet,
    '__init__', 'addButton', 'clone', 'create', 'customButtons', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QMessageDialogOptions, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Option(CuteFlags, scoped=True):
    """
    The flags enum 'QMessageDialogOptions::Option' of Qt, with the 1 names Qt
    gives in it. Qt names the type of its combinations
    'QMessageDialogOptions::Options'. C++ keeps these names inside the enum,
    so the class that holds the enum does not have them.
    """

    DontUseNativeDialog = 0x1

  Options = Option

  class StandardIcon(CuteNum):
    """
    The enum 'QMessageDialogOptions::StandardIcon' of Qt, with the 5 names Qt
    gives in it.
    """

    NoIcon = Kee[int](0)
    Information = Kee[int](1)
    Warning = Kee[int](2)
    Critical = Kee[int](3)
    Question = Kee[int](4)

  #  The classes Qt writes inside QMessageDialogOptions, each a class in here
  #  as in C++.

  class CustomButton(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QMessageDialogOptions::CustomButton: a plain Python
    object standing in front of one C++ QMessageDialogOptions::CustomButton.

    C++ hands a QMessageDialogOptions::CustomButton around as a copy, so
    every C++ QMessageDialogOptions::CustomButton behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QMessageDialogOptions::CustomButton yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QMessageDialogOptions::CustomButton::CustomButton(int id, const
      QString &label, QPlatformDialogHelper::ButtonRole role, void *button)':
      names 'void', which has no cute class yet.
    - Qt's 'QMessageDialogOptions::CustomButton::~CustomButton()': the
      destructor: Python removes its C++ QMessageDialogOptions::CustomButton
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QMessageDialogOptions::CustomButton is created at the first
      use, not by 'QMessageDialogOptions::CustomButton(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QMessageDialogOptions::CustomButton back gives a
      copy the ritual made for Python, in a new cute
      QMessageDialogOptions::CustomButton.
    - Each name of Qt's QMessageDialogOptions::CustomButton that has no cute
      function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QMessageDialogOptions::CustomButton'

    #  Qt's '~QMessageDialogOptions::CustomButton()'. Naming it makes this a
    #  value class: Python owns every C++ QMessageDialogOptions::CustomButton
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QMessageDialogOptions12CustomButtonD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      Qt's 'QMessageDialogOptions::CustomButton::CustomButton(int id, const
      QString &label, QPlatformDialogHelper::ButtonRole role, void *button)':
      names 'void', which has no cute class yet.
      """
      raise NotImplementedError(
          "'QMessageDialogOptions.CustomButton.__init__' has no cute "
          "function yet. Qt's "
          "'QMessageDialogOptions::CustomButton::CustomButton(int id, const "
          "QString &label, QPlatformDialogHelper::ButtonRole role, void "
          "*button)': names 'void', which has no cute class yet.")

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMessageDialogOptions'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def windowTitle(self) -> str:
    """
    Calls Qt's 'QString QMessageDialogOptions::windowTitle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#windowTitle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMessageDialogOptions::windowTitle() const
    return self.uglySide.call(
        'ritual_ZNK21QMessageDialogOptions11windowTitleEv',
    )

  def standardIcon(self) -> StandardIcon:
    """
    Calls Qt's 'StandardIcon QMessageDialogOptions::standardIcon() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#standardIcon

    Returns
    -------

    StandardIcon
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'StandardIcon(number)'
      gives.
    """
    #  StandardIcon QMessageDialogOptions::standardIcon() const
    return QMessageDialogOptions.StandardIcon(self.uglySide.call(
        'ritual_ZNK21QMessageDialogOptions12standardIconEv',
    ))

  def iconPixmap(self) -> QPixmap:
    """
    Calls Qt's 'QPixmap QMessageDialogOptions::iconPixmap() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#iconPixmap

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QMessageDialogOptions::iconPixmap() const
    address = self.uglySide.call(
        'ritual_ZNK21QMessageDialogOptions10iconPixmapEv',
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QMessageDialogOptions::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagedialogoptions.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMessageDialogOptions::text() const
    return self.uglySide.call('ritual_ZNK21QMessageDialogOptions4textEv')

  def informativeText(self) -> str:
    """
    Calls Qt's 'QString QMessageDialogOptions::informativeText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#informativeText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMessageDialogOptions::informativeText() const
    return self.uglySide.call(
        'ritual_ZNK21QMessageDialogOptions15informativeTextEv',
    )

  def detailedText(self) -> str:
    """
    Calls Qt's 'QString QMessageDialogOptions::detailedText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#detailedText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMessageDialogOptions::detailedText() const
    return self.uglySide.call(
        'ritual_ZNK21QMessageDialogOptions12detailedTextEv',
    )

  @overload(Option)
  def testOption(self, option: Option) -> bool:
    """
    Calls Qt's 'bool QMessageDialogOptions::testOption(Option option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#testOption

    Parameters
    ----------

    option : Option
      Passed on as its number.
    """
    #  bool QMessageDialogOptions::testOption(Option option) const
    return self.uglySide.call(
        'ritual_ZNK21QMessageDialogOptions10testOptionENS_6OptionE',
        option.value,
    )

  def options(self) -> Options:
    """
    Calls Qt's 'Options QMessageDialogOptions::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagedialogoptions.html#options

    Returns
    -------

    Options
      The value standing for the combination Qt gave back.
    """
    #  Options QMessageDialogOptions::options() const
    return QMessageDialogOptions.Options(self.uglySide.call(
        'ritual_ZNK21QMessageDialogOptions7optionsEv',
    ))

  def standardButtons(self) -> QPlatformDialogHelper.StandardButtons:
    """
    Calls Qt's 'QPlatformDialogHelper::StandardButtons
    QMessageDialogOptions::standardButtons() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#standardButtons

    Returns
    -------

    QPlatformDialogHelper.StandardButtons
      The value standing for the combination Qt gave back.
    """
    #  QPlatformDialogHelper::StandardButtons
    #      QMessageDialogOptions::standardButtons() const
    return QPlatformDialogHelper.StandardButtons(self.uglySide.call(
        'ritual_ZNK21QMessageDialogOptions15standardButtonsEv',
    ))

  def checkBoxLabel(self) -> str:
    """
    Calls Qt's 'QString QMessageDialogOptions::checkBoxLabel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#checkBoxLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMessageDialogOptions::checkBoxLabel() const
    return self.uglySide.call(
        'ritual_ZNK21QMessageDialogOptions13checkBoxLabelEv',
    )

  def checkBoxState(self) -> Qt.CheckState:
    """
    Calls Qt's 'Qt::CheckState QMessageDialogOptions::checkBoxState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#checkBoxState

    Returns
    -------

    Qt.CheckState
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.CheckState(number)'
      gives.
    """
    #  Qt::CheckState QMessageDialogOptions::checkBoxState() const
    return Qt.CheckState(self.uglySide.call(
        'ritual_ZNK21QMessageDialogOptions13checkBoxStateEv',
    ))

  def escapeButton(self) -> int:
    """
    Calls Qt's 'int QMessageDialogOptions::escapeButton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#escapeButton
    """
    #  int QMessageDialogOptions::escapeButton() const
    return self.uglySide.call(
        'ritual_ZNK21QMessageDialogOptions12escapeButtonEv',
    )

  def defaultButton(self) -> int:
    """
    Calls Qt's 'int QMessageDialogOptions::defaultButton() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#defaultButton
    """
    #  int QMessageDialogOptions::defaultButton() const
    return self.uglySide.call(
        'ritual_ZNK21QMessageDialogOptions13defaultButtonEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setWindowTitle(self, a0: str) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::setWindowTitle(const QString
    &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#setWindowTitle

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMessageDialogOptions::setWindowTitle(const QString &a0)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions14setWindowTitleERK7QString', a0,
    )

  @overload(StandardIcon)
  def setStandardIcon(self, icon: StandardIcon) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::setStandardIcon(StandardIcon
    icon)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#setStandardIcon

    Parameters
    ----------

    icon : StandardIcon
      Passed on as its number.
    """
    #  void QMessageDialogOptions::setStandardIcon(StandardIcon icon)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions15setStandardIconENS_12StandardIco'
        'nE',
        icon.value,
    )

  @overload(QPixmap)
  def setIconPixmap(self, pixmap: QPixmap) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::setIconPixmap(const QPixmap
    &pixmap)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#setIconPixmap

    Parameters
    ----------

    pixmap : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QMessageDialogOptions::setIconPixmap(const QPixmap &pixmap)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions13setIconPixmapERK7QPixmap',
        self._valueOf(pixmap),
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagedialogoptions.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMessageDialogOptions::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions7setTextERK7QString', text,
    )

  @overload(str)
  def setInformativeText(self, text: str) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::setInformativeText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#setInformativeText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMessageDialogOptions::setInformativeText(const QString &text)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions18setInformativeTextERK7QString',
        text,
    )

  @overload(str)
  def setDetailedText(self, text: str) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::setDetailedText(const QString
    &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#setDetailedText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QMessageDialogOptions::setDetailedText(const QString &text)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions15setDetailedTextERK7QString', text,
    )

  @overload(Option)
  @overload(Option, bool)
  def setOption(self, option: Option, on: bool = True) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::setOption(Option option, bool
    on)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#setOption

    Parameters
    ----------

    option : Option
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QMessageDialogOptions::setOption(Option option, bool on)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions9setOptionENS_6OptionEb',
        option.value, on,
    )

  @overload(Options)
  def setOptions(self, options: Options) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::setOptions(Options options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#setOptions

    Parameters
    ----------

    options : Options
      Passed on as its number.
    """
    #  void QMessageDialogOptions::setOptions(Options options)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions10setOptionsE6QFlagsINS_6OptionEE',
        options.value,
    )

  @overload(QPlatformDialogHelper.StandardButtons)
  def setStandardButtons(
      self,
      buttons: QPlatformDialogHelper.StandardButtons,
  ) -> None:
    """
    Calls Qt's 'void
    QMessageDialogOptions::setStandardButtons(QPlatformDialogHelper::
    StandardButtons buttons)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#setStandardButtons

    Parameters
    ----------

    buttons : QPlatformDialogHelper.StandardButtons
      Passed on as its number.
    """
    #  void QMessageDialogOptions::setStandardButtons(QPlatformDialogHelper::
    #      StandardButtons buttons)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions18setStandardButtonsE6QFlagsIN21QP'
        'latformDialogHelper14StandardButtonEE',
        buttons.value,
    )

  @overload(str, Qt.CheckState)
  def setCheckBox(self, label: str, state: Qt.CheckState) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::setCheckBox(const QString &label,
    Qt::CheckState state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#setCheckBox

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.

    state : Qt.CheckState
      Passed on as its number.
    """
    #  void QMessageDialogOptions::setCheckBox(const QString &label,
    #      Qt::CheckState state)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions11setCheckBoxERK7QStringN2Qt10Chec'
        'kStateE',
        label, state.value,
    )

  @overload(int)
  def setEscapeButton(self, id: int) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::setEscapeButton(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#setEscapeButton

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QMessageDialogOptions::setEscapeButton(int id)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions15setEscapeButtonEi', id,
    )

  @overload(int)
  def setDefaultButton(self, id: int) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::setDefaultButton(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#setDefaultButton

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QMessageDialogOptions::setDefaultButton(int id)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions16setDefaultButtonEi', id,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QMessageDialogOptions::QMessageDialogOptions(
    QMessageDialogOptionsPrivate *dd)': names 'QMessageDialogOptionsPrivate',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMessageDialogOptions.__init__' has no cute function yet. Qt's "
        "'QMessageDialogOptions::QMessageDialogOptions(QMessageDialogOptions"
        "Private *dd)': names 'QMessageDialogOptionsPrivate', which has no "
        "cute class yet.")

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

  @overload(int)
  def removeButton(self, id: int) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::removeButton(int id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#removeButton

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QMessageDialogOptions::removeButton(int id)
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions12removeButtonEi', id,
    )

  @overload(int)
  def customButton(self, id: int) -> Optional[CustomButton]:
    """
    Calls Qt's 'const CustomButton *QMessageDialogOptions::customButton(int
    id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#customButton

    Parameters
    ----------

    id : int
      Passed on as it is.

    Returns
    -------

    Optional[CustomButton]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const CustomButton *QMessageDialogOptions::customButton(int id)
    address = self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions12customButtonEi', id,
    )
    return QMessageDialogOptions.CustomButton._cuteAt(address)

  def clearCustomButtons(self) -> None:
    """
    Calls Qt's 'void QMessageDialogOptions::clearCustomButtons()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmessagedialogoptions.html#clearCustomButtons
    """
    #  void QMessageDialogOptions::clearCustomButtons()
    self.uglySide.call(
        'ritual_ZN21QMessageDialogOptions18clearCustomButtonsEv',
    )

  @staticmethod
  def addButton(*__, **_) -> Never:
    """
    Qt's 'int QMessageDialogOptions::addButton(const QString &label,
    QPlatformDialogHelper::ButtonRole role, void *buttonImpl, int buttonId)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QMessageDialogOptions.addButton' has no cute function yet. Qt's "
        "'int QMessageDialogOptions::addButton(const QString &label, "
        "QPlatformDialogHelper::ButtonRole role, void *buttonImpl, int "
        "buttonId)': names 'void', which has no cute class yet.")

  @staticmethod
  def clone(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QMessageDialogOptions>
    QMessageDialogOptions::clone() const': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QMessageDialogOptions.clone' has no cute function yet. Qt's "
        "'QSharedPointer<QMessageDialogOptions> "
        "QMessageDialogOptions::clone() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QMessageDialogOptions>
    QMessageDialogOptions::create()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QMessageDialogOptions.create' has no cute function yet. Qt's "
        "'QSharedPointer<QMessageDialogOptions> "
        "QMessageDialogOptions::create()': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def customButtons(*__, **_) -> Never:
    """
    Qt's 'const QList<CustomButton> &QMessageDialogOptions::customButtons()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QMessageDialogOptions.customButtons' has no cute function yet. "
        "Qt's 'const QList<CustomButton> "
        "&QMessageDialogOptions::customButtons()': gives a type Python has "
        "no way to take yet.")
