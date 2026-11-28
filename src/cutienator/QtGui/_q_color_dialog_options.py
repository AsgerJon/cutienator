"""
QColorDialogOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/qpa/qplatformdialoghelper.h, Qt 6.12.0. Changes made
#  here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QColorDialogOptions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QColorDialogOptions: a plain Python object standing
  in front of one C++ QColorDialogOptions.

  What exists
  -----------

  Every function of Qt's QColorDialogOptions that has a ritual and that
  Python can call so far, 11 names in all: 'windowTitle', 'setWindowTitle',
  'setOption', 'testOption', 'setOptions', 'options', 'customColorCount',
  'customColor', 'setCustomColor', 'standardColor', 'setStandardColor'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorDialogOptions::QColorDialogOptions(QColorDialogOptionsPrivate
    *dd)': names 'QColorDialogOptionsPrivate', which has no cute class yet.
  - Qt's 'QColorDialogOptions::~QColorDialogOptions()': the destructor:
    Python never removes a C++ QColorDialogOptions.
  - Qt's 'QSharedPointer<QColorDialogOptions> QColorDialogOptions::create()':
    gives a type Python has no way to take yet.
  - Qt's 'QSharedPointer<QColorDialogOptions> QColorDialogOptions::clone()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  7 of the 22 functions Qt declares: 3 not a gap; 2 forbidden; 2 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QColorDialogOptions is created at the first use, not by
    'QColorDialogOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QColorDialogOptions.
  - Each name of Qt's QColorDialogOptions that has no cute function yet,
    '__init__', 'clone', 'create', 'customColors', 'standardColors', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QColorDialogOptions, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class ColorDialogOption(CuteFlags):
    """
    The flags enum 'QColorDialogOptions::ColorDialogOption' of Qt, with the 4
    names Qt gives in it. Qt names the type of its combinations
    'QColorDialogOptions::ColorDialogOptions'.
    """

    ShowAlphaChannel = 0x1
    NoButtons = 0x2
    DontUseNativeDialog = 0x4
    NoEyeDropperButton = 0x8

  ColorDialogOptions = ColorDialogOption

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def customColorCount() -> int:
    """
    Calls Qt's 'int QColorDialogOptions::customColorCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolordialogoptions.html#customColorCount
    """
    #  int QColorDialogOptions::customColorCount()
    return Rituals.call('ritual_ZN19QColorDialogOptions16customColorCountEv')

  @staticmethod
  @overload(int)
  def customColor(index: int) -> int:
    """
    Calls Qt's 'QRgb QColorDialogOptions::customColor(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolordialogoptions.html#customColor

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  QRgb QColorDialogOptions::customColor(int index)
    return Rituals.call(
        'ritual_ZN19QColorDialogOptions11customColorEi', index,
    )

  @staticmethod
  @overload(int, int)
  def setCustomColor(index: int, color: int) -> None:
    """
    Calls Qt's 'void QColorDialogOptions::setCustomColor(int index, QRgb
    color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolordialogoptions.html#setCustomColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : int
      Passed on as it is.
    """
    #  void QColorDialogOptions::setCustomColor(int index, QRgb color)
    Rituals.call(
        'ritual_ZN19QColorDialogOptions14setCustomColorEij', index, color,
    )

  @staticmethod
  @overload(int)
  def standardColor(index: int) -> int:
    """
    Calls Qt's 'QRgb QColorDialogOptions::standardColor(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolordialogoptions.html#standardColor

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  QRgb QColorDialogOptions::standardColor(int index)
    return Rituals.call(
        'ritual_ZN19QColorDialogOptions13standardColorEi', index,
    )

  @staticmethod
  @overload(int, int)
  def setStandardColor(index: int, color: int) -> None:
    """
    Calls Qt's 'void QColorDialogOptions::setStandardColor(int index, QRgb
    color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolordialogoptions.html#setStandardColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : int
      Passed on as it is.
    """
    #  void QColorDialogOptions::setStandardColor(int index, QRgb color)
    Rituals.call(
        'ritual_ZN19QColorDialogOptions16setStandardColorEij', index, color,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorDialogOptions'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def windowTitle(self) -> str:
    """
    Calls Qt's 'QString QColorDialogOptions::windowTitle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolordialogoptions.html#windowTitle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QColorDialogOptions::windowTitle() const
    return self.uglySide.call(
        'ritual_ZNK19QColorDialogOptions11windowTitleEv',
    )

  @overload(ColorDialogOption)
  def testOption(self, option: ColorDialogOption) -> bool:
    """
    Calls Qt's 'bool QColorDialogOptions::testOption(ColorDialogOption
    option) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolordialogoptions.html#testOption

    Parameters
    ----------

    option : ColorDialogOption
      Passed on as its number.
    """
    #  bool QColorDialogOptions::testOption(ColorDialogOption option) const
    return self.uglySide.call(
        'ritual_ZNK19QColorDialogOptions10testOptionENS_17ColorDialogOption'
        'E',
        option.value,
    )

  def options(self) -> ColorDialogOptions:
    """
    Calls Qt's 'ColorDialogOptions QColorDialogOptions::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialogoptions.html#options

    Returns
    -------

    ColorDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  ColorDialogOptions QColorDialogOptions::options() const
    return QColorDialogOptions.ColorDialogOptions(self.uglySide.call(
        'ritual_ZNK19QColorDialogOptions7optionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setWindowTitle(self, a0: str) -> None:
    """
    Calls Qt's 'void QColorDialogOptions::setWindowTitle(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolordialogoptions.html#setWindowTitle

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QColorDialogOptions::setWindowTitle(const QString &a0)
    self.uglySide.call(
        'ritual_ZN19QColorDialogOptions14setWindowTitleERK7QString', a0,
    )

  @overload(ColorDialogOption)
  @overload(ColorDialogOption, bool)
  def setOption(self, option: ColorDialogOption, on: bool = True) -> None:
    """
    Calls Qt's 'void QColorDialogOptions::setOption(ColorDialogOption option,
    bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialogoptions.html#setOption

    Parameters
    ----------

    option : ColorDialogOption
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QColorDialogOptions::setOption(ColorDialogOption option, bool on)
    self.uglySide.call(
        'ritual_ZN19QColorDialogOptions9setOptionENS_17ColorDialogOptionEb',
        option.value, on,
    )

  @overload(ColorDialogOptions)
  def setOptions(self, options: ColorDialogOptions) -> None:
    """
    Calls Qt's 'void QColorDialogOptions::setOptions(ColorDialogOptions
    options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcolordialogoptions.html#setOptions

    Parameters
    ----------

    options : ColorDialogOptions
      Passed on as its number.
    """
    #  void QColorDialogOptions::setOptions(ColorDialogOptions options)
    self.uglySide.call(
        'ritual_ZN19QColorDialogOptions10setOptionsE6QFlagsINS_17ColorDialo'
        'gOptionEE',
        options.value,
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
    Qt's 'QColorDialogOptions::QColorDialogOptions(QColorDialogOptionsPrivate
    *dd)': names 'QColorDialogOptionsPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QColorDialogOptions.__init__' has no cute function yet. Qt's "
        "'QColorDialogOptions::QColorDialogOptions(QColorDialogOptionsPrivat"
        "e *dd)': names 'QColorDialogOptionsPrivate', which has no cute "
        "class yet.")

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

  @staticmethod
  def clone(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QColorDialogOptions> QColorDialogOptions::clone()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QColorDialogOptions.clone' has no cute function yet. Qt's "
        "'QSharedPointer<QColorDialogOptions> QColorDialogOptions::clone() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QColorDialogOptions> QColorDialogOptions::create()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QColorDialogOptions.create' has no cute function yet. Qt's "
        "'QSharedPointer<QColorDialogOptions> "
        "QColorDialogOptions::create()': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def customColors(*__, **_) -> Never:
    """
    Qt's 'QRgb *QColorDialogOptions::customColors()': takes or gives a type
    that cannot be passed yet: QRgb *.
    """
    raise NotImplementedError(
        "'QColorDialogOptions.customColors' has no cute function yet. Qt's "
        "'QRgb *QColorDialogOptions::customColors()': takes or gives a type "
        "that cannot be passed yet: QRgb *.")

  @staticmethod
  def standardColors(*__, **_) -> Never:
    """
    Qt's 'QRgb *QColorDialogOptions::standardColors()': takes or gives a type
    that cannot be passed yet: QRgb *.
    """
    raise NotImplementedError(
        "'QColorDialogOptions.standardColors' has no cute function yet. "
        "Qt's 'QRgb *QColorDialogOptions::standardColors()': takes or gives "
        "a type that cannot be passed yet: QRgb *.")
