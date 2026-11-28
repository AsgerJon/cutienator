"""
QFontDialogOptions binding of the Qt C++
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

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QFontDialogOptions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFontDialogOptions: a plain Python object standing in
  front of one C++ QFontDialogOptions.

  What exists
  -----------

  Every function of Qt's QFontDialogOptions that has a ritual and that Python
  can call so far, 6 names in all: 'windowTitle', 'setWindowTitle',
  'setOption', 'testOption', 'setOptions', 'options'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontDialogOptions::QFontDialogOptions(QFontDialogOptionsPrivate
    *dd)': names 'QFontDialogOptionsPrivate', which has no cute class yet.
  - Qt's 'QFontDialogOptions::~QFontDialogOptions()': the destructor: Python
    never removes a C++ QFontDialogOptions.
  - Qt's 'QSharedPointer<QFontDialogOptions> QFontDialogOptions::create()':
    gives a type Python has no way to take yet.
  - Qt's 'QSharedPointer<QFontDialogOptions> QFontDialogOptions::clone()
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  5 of the 15 functions Qt declares: 3 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QFontDialogOptions is created at the first use, not by
    'QFontDialogOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFontDialogOptions.
  - Each name of Qt's QFontDialogOptions that has no cute function yet,
    '__init__', 'clone', 'create', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QFontDialogOptions, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class FontDialogOption(CuteFlags):
    """
    The flags enum 'QFontDialogOptions::FontDialogOption' of Qt, with the 6
    names Qt gives in it. Qt names the type of its combinations
    'QFontDialogOptions::FontDialogOptions'.
    """

    NoButtons = 0x1
    DontUseNativeDialog = 0x2
    ScalableFonts = 0x4
    NonScalableFonts = 0x8
    MonospacedFonts = 0x10
    ProportionalFonts = 0x20

  FontDialogOptions = FontDialogOption

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontDialogOptions'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def windowTitle(self) -> str:
    """
    Calls Qt's 'QString QFontDialogOptions::windowTitle() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdialogoptions.html#windowTitle

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFontDialogOptions::windowTitle() const
    return self.uglySide.call(
        'ritual_ZNK18QFontDialogOptions11windowTitleEv',
    )

  @overload(FontDialogOption)
  def testOption(self, option: FontDialogOption) -> bool:
    """
    Calls Qt's 'bool QFontDialogOptions::testOption(FontDialogOption option)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialogoptions.html#testOption

    Parameters
    ----------

    option : FontDialogOption
      Passed on as its number.
    """
    #  bool QFontDialogOptions::testOption(FontDialogOption option) const
    return self.uglySide.call(
        'ritual_ZNK18QFontDialogOptions10testOptionENS_16FontDialogOptionE',
        option.value,
    )

  def options(self) -> FontDialogOptions:
    """
    Calls Qt's 'FontDialogOptions QFontDialogOptions::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialogoptions.html#options

    Returns
    -------

    FontDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  FontDialogOptions QFontDialogOptions::options() const
    return QFontDialogOptions.FontDialogOptions(self.uglySide.call(
        'ritual_ZNK18QFontDialogOptions7optionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setWindowTitle(self, a0: str) -> None:
    """
    Calls Qt's 'void QFontDialogOptions::setWindowTitle(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfontdialogoptions.html#setWindowTitle

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFontDialogOptions::setWindowTitle(const QString &a0)
    self.uglySide.call(
        'ritual_ZN18QFontDialogOptions14setWindowTitleERK7QString', a0,
    )

  @overload(FontDialogOption)
  @overload(FontDialogOption, bool)
  def setOption(self, option: FontDialogOption, on: bool = True) -> None:
    """
    Calls Qt's 'void QFontDialogOptions::setOption(FontDialogOption option,
    bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialogoptions.html#setOption

    Parameters
    ----------

    option : FontDialogOption
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QFontDialogOptions::setOption(FontDialogOption option, bool on)
    self.uglySide.call(
        'ritual_ZN18QFontDialogOptions9setOptionENS_16FontDialogOptionEb',
        option.value, on,
    )

  @overload(FontDialogOptions)
  def setOptions(self, options: FontDialogOptions) -> None:
    """
    Calls Qt's 'void QFontDialogOptions::setOptions(FontDialogOptions
    options)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialogoptions.html#setOptions

    Parameters
    ----------

    options : FontDialogOptions
      Passed on as its number.
    """
    #  void QFontDialogOptions::setOptions(FontDialogOptions options)
    self.uglySide.call(
        'ritual_ZN18QFontDialogOptions10setOptionsE6QFlagsINS_16FontDialogO'
        'ptionEE',
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
    Qt's 'QFontDialogOptions::QFontDialogOptions(QFontDialogOptionsPrivate
    *dd)': names 'QFontDialogOptionsPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QFontDialogOptions.__init__' has no cute function yet. Qt's "
        "'QFontDialogOptions::QFontDialogOptions(QFontDialogOptionsPrivate "
        "*dd)': names 'QFontDialogOptionsPrivate', which has no cute class "
        "yet.")

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
    Qt's 'QSharedPointer<QFontDialogOptions> QFontDialogOptions::clone()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QFontDialogOptions.clone' has no cute function yet. Qt's "
        "'QSharedPointer<QFontDialogOptions> QFontDialogOptions::clone() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QFontDialogOptions> QFontDialogOptions::create()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QFontDialogOptions.create' has no cute function yet. Qt's "
        "'QSharedPointer<QFontDialogOptions> QFontDialogOptions::create()': "
        "gives a type Python has no way to take yet.")
