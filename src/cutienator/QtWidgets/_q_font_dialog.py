"""
QFontDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qfontdialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFontDialog(QDialog):
  """
  The cute side of Qt's QFontDialog: a plain Python object standing in front
  of one C++ QFontDialog.

  It is built on the cute 'QDialog', as Qt's QFontDialog is built on Qt's
  QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFontDialog that has a ritual and that Python can
  call so far, 11 names in all: 'metaObject', 'tr', 'setCurrentFont',
  'currentFont', 'selectedFont', 'setOption', 'testOption', 'setOptions',
  'options', 'open', 'setVisible'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFontDialog::~QFontDialog()': the destructor: Python never removes
    a C++ QFontDialog.
  - Qt's 'QFont QFontDialog::getFont(bool *ok, QWidget *parent)': takes a
    number to change where it is.
  - Qt's 'QFont QFontDialog::getFont(bool *ok, const QFont &initial, QWidget
    *parent, const QString &title, FontDialogOptions options)': takes a
    number to change where it is.

  What has no ritual
  ------------------

  13 of the 29 functions Qt declares: 3 private; 3 protected; 2 takes or
  gives a type that cannot be passed yet; 2 a signal; 2 forbidden; 1 a
  template.

  What to expect
  --------------

  - The C++ QFontDialog is created at the first use, not by
    'QFontDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFontDialog.
  - Qt tells when it has removed the C++ QFontDialog. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QFontDialog, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class FontDialogOption(CuteFlags):
    """
    The flags enum 'QFontDialog::FontDialogOption' of Qt, with the 6 names Qt
    gives in it. Qt names the type of its combinations
    'QFontDialog::FontDialogOptions'.
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
    Calls Qt's 'QString QFontDialog::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#tr

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
    #  QString QFontDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QFontDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFontDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFontDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFontDialog::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QFontDialog10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentFont(self) -> QFont:
    """
    Calls Qt's 'QFont QFontDialog::currentFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#currentFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QFontDialog::currentFont() const
    address = self.uglySide.call('ritual_ZNK11QFontDialog11currentFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def selectedFont(self) -> QFont:
    """
    Calls Qt's 'QFont QFontDialog::selectedFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#selectedFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QFontDialog::selectedFont() const
    address = self.uglySide.call('ritual_ZNK11QFontDialog12selectedFontEv')
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  @overload(FontDialogOption)
  def testOption(self, option: FontDialogOption) -> bool:
    """
    Calls Qt's 'bool QFontDialog::testOption(FontDialogOption option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#testOption

    Parameters
    ----------

    option : FontDialogOption
      Passed on as its number.
    """
    #  bool QFontDialog::testOption(FontDialogOption option) const
    return self.uglySide.call(
        'ritual_ZNK11QFontDialog10testOptionENS_16FontDialogOptionE',
        option.value,
    )

  def options(self) -> FontDialogOptions:
    """
    Calls Qt's 'FontDialogOptions QFontDialog::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#options

    Returns
    -------

    FontDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  FontDialogOptions QFontDialog::options() const
    return QFontDialog.FontDialogOptions(self.uglySide.call(
        'ritual_ZNK11QFontDialog7optionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setCurrentFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QFontDialog::setCurrentFont(const QFont &font)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#setCurrentFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QFontDialog::setCurrentFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN11QFontDialog14setCurrentFontERK5QFont',
        self._valueOf(font),
    )

  @overload(FontDialogOption)
  @overload(FontDialogOption, bool)
  def setOption(self, option: FontDialogOption, on: bool = True) -> None:
    """
    Calls Qt's 'void QFontDialog::setOption(FontDialogOption option, bool
    on)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#setOption

    Parameters
    ----------

    option : FontDialogOption
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QFontDialog::setOption(FontDialogOption option, bool on)
    self.uglySide.call(
        'ritual_ZN11QFontDialog9setOptionENS_16FontDialogOptionEb',
        option.value, on,
    )

  @overload(FontDialogOptions)
  def setOptions(self, options: FontDialogOptions) -> None:
    """
    Calls Qt's 'void QFontDialog::setOptions(FontDialogOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#setOptions

    Parameters
    ----------

    options : FontDialogOptions
      Passed on as its number.
    """
    #  void QFontDialog::setOptions(FontDialogOptions options)
    self.uglySide.call(
        'ritual_ZN11QFontDialog10setOptionsE6QFlagsINS_16FontDialogOptionEE',
        options.value,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QFontDialog::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QFontDialog::setVisible(bool visible)
    self.uglySide.call('ritual_ZN11QFontDialog10setVisibleEb', visible)

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
    Notes what was given, for Qt's 'QFontDialog::QFontDialog(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#QFontDialog

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFontDialog::QFontDialog(QWidget *parent)
    self._noteCreation(QFontDialog, lambda: Rituals.call(
        'ritual_ZN11QFontDialogC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(QFont)
  @overload(QFont, QWidget)
  @overload(QFont, NoneType)
  def __init__(
      self,
      initial: QFont,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QFontDialog::QFontDialog(const QFont
    &initial, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#QFontDialog

    Parameters
    ----------

    initial : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFontDialog::QFontDialog(const QFont &initial, QWidget *parent)
    self._noteCreation(QFontDialog, lambda: Rituals.call(
        'ritual_ZN11QFontDialogC1ERK5QFontP7QWidget',
        self._valueOf(initial), self._addressOf(parent),
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

  @overload(QObject, str)
  @overload(QObject, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  def open(self, receiver: Optional[QObject], member: Optional[str]) -> None:
    """
    Calls Qt's 'void QFontDialog::open(QObject *receiver, const char
    *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qfontdialog.html#open

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QFontDialog::open(QObject *receiver, const char *member)
    self.uglySide.call(
        'ritual_ZN11QFontDialog4openEP7QObjectPKc',
        self._addressOf(receiver), self._bytesOf(member),
    )
