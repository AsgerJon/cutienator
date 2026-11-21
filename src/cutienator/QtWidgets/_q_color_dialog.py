"""
QColorDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qcolordialog.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QColorDialogColorDialogOption, QDialog, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QColorDialog(QDialog):
  """
  The cute side of Qt's QColorDialog: a plain Python object standing in front
  of one C++ QColorDialog.

  It is built on the cute 'QDialog', as Qt's QColorDialog is built on Qt's
  QDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QColorDialog that has a ritual and that Python can
  call so far, 17 names in all: 'metaObject', 'tr', 'setCurrentColor',
  'currentColor', 'selectedColor', 'setOption', 'testOption', 'setOptions',
  'options', 'open', 'setVisible', 'getColor', 'customCount', 'customColor',
  'setCustomColor', 'standardColor', 'setStandardColor'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QColorDialog::~QColorDialog()': the destructor: Python never
    removes a C++ QColorDialog.

  What has no ritual
  ------------------

  12 of the 32 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 a signal; 2 protected; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QColorDialog is created at the first use, not by
    'QColorDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QColorDialog.
  - Qt tells when it has removed the C++ QColorDialog. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QColorDialog, and the names Qt has for the
  #  combinations of its flags enums.
  ColorDialogOption = QColorDialogColorDialogOption
  ColorDialogOptions = QColorDialogColorDialogOption

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
    Calls Qt's 'QString QColorDialog::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#tr

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
    #  QString QColorDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QColorDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QColor)
  @overload(QColor, QWidget)
  @overload(QColor, NoneType)
  @overload(QColor, QWidget, str)
  @overload(QColor, NoneType, str)
  @overload(QColor, QWidget, str, ColorDialogOptions)
  @overload(QColor, NoneType, str, ColorDialogOptions)
  def getColor(
      initial: QColor,
      parent: Optional[QWidget] = None,
      title: str = '',
      options: ColorDialogOptions = ColorDialogOptions(),
  ) -> QColor:
    """
    Calls Qt's 'QColor QColorDialog::getColor(const QColor &initial, QWidget
    *parent, const QString &title, ColorDialogOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#getColor

    Parameters
    ----------

    initial : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    title : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    options : ColorDialogOptions
      Passed on as its number. May be left out, as in Qt: it is then
      ColorDialogOptions().

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColorDialog::getColor(const QColor &initial, QWidget *parent,
    #      const QString &title, ColorDialogOptions options)
    address = Rituals.call(
        'ritual_ZN12QColorDialog8getColorERK6QColorP7QWidgetRK7QString6QFla'
        'gsINS_17ColorDialogOptionEE',
        CuteMixin._valueOf(initial), CuteMixin._addressOf(parent), title,
        options.value,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  def customCount() -> int:
    """
    Calls Qt's 'int QColorDialog::customCount()'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#customCount
    """
    #  int QColorDialog::customCount()
    return Rituals.call('ritual_ZN12QColorDialog11customCountEv')

  @staticmethod
  @overload(int)
  def customColor(index: int) -> QColor:
    """
    Calls Qt's 'QColor QColorDialog::customColor(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#customColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColorDialog::customColor(int index)
    address = Rituals.call('ritual_ZN12QColorDialog11customColorEi', index)
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(int, QColor)
  def setCustomColor(index: int, color: QColor) -> None:
    """
    Calls Qt's 'void QColorDialog::setCustomColor(int index, QColor color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#setCustomColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QColorDialog::setCustomColor(int index, QColor color)
    Rituals.call(
        'ritual_ZN12QColorDialog14setCustomColorEi6QColor',
        index, CuteMixin._valueOf(color),
    )

  @staticmethod
  @overload(int)
  def standardColor(index: int) -> QColor:
    """
    Calls Qt's 'QColor QColorDialog::standardColor(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#standardColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColorDialog::standardColor(int index)
    address = Rituals.call('ritual_ZN12QColorDialog13standardColorEi', index)
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @staticmethod
  @overload(int, QColor)
  def setStandardColor(index: int, color: QColor) -> None:
    """
    Calls Qt's 'void QColorDialog::setStandardColor(int index, QColor
    color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#setStandardColor

    Parameters
    ----------

    index : int
      Passed on as it is.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QColorDialog::setStandardColor(int index, QColor color)
    Rituals.call(
        'ritual_ZN12QColorDialog16setStandardColorEi6QColor',
        index, CuteMixin._valueOf(color),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QColorDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QColorDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QColorDialog::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QColorDialog10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentColor(self) -> QColor:
    """
    Calls Qt's 'QColor QColorDialog::currentColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#currentColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColorDialog::currentColor() const
    address = self.uglySide.call('ritual_ZNK12QColorDialog12currentColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def selectedColor(self) -> QColor:
    """
    Calls Qt's 'QColor QColorDialog::selectedColor() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#selectedColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QColorDialog::selectedColor() const
    address = self.uglySide.call('ritual_ZNK12QColorDialog13selectedColorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(ColorDialogOption)
  def testOption(self, option: ColorDialogOption) -> bool:
    """
    Calls Qt's 'bool QColorDialog::testOption(ColorDialogOption option)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#testOption

    Parameters
    ----------

    option : ColorDialogOption
      Passed on as its number.
    """
    #  bool QColorDialog::testOption(ColorDialogOption option) const
    return self.uglySide.call(
        'ritual_ZNK12QColorDialog10testOptionENS_17ColorDialogOptionE',
        option.value,
    )

  def options(self) -> ColorDialogOptions:
    """
    Calls Qt's 'ColorDialogOptions QColorDialog::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#options

    Returns
    -------

    ColorDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  ColorDialogOptions QColorDialog::options() const
    return QColorDialog.ColorDialogOptions(self.uglySide.call(
        'ritual_ZNK12QColorDialog7optionsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setCurrentColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QColorDialog::setCurrentColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#setCurrentColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QColorDialog::setCurrentColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN12QColorDialog15setCurrentColorERK6QColor',
        self._valueOf(color),
    )

  @overload(ColorDialogOption)
  @overload(ColorDialogOption, bool)
  def setOption(self, option: ColorDialogOption, on: bool = True) -> None:
    """
    Calls Qt's 'void QColorDialog::setOption(ColorDialogOption option, bool
    on)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#setOption

    Parameters
    ----------

    option : ColorDialogOption
      Passed on as its number.

    on : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QColorDialog::setOption(ColorDialogOption option, bool on)
    self.uglySide.call(
        'ritual_ZN12QColorDialog9setOptionENS_17ColorDialogOptionEb',
        option.value, on,
    )

  @overload(ColorDialogOptions)
  def setOptions(self, options: ColorDialogOptions) -> None:
    """
    Calls Qt's 'void QColorDialog::setOptions(ColorDialogOptions options)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#setOptions

    Parameters
    ----------

    options : ColorDialogOptions
      Passed on as its number.
    """
    #  void QColorDialog::setOptions(ColorDialogOptions options)
    self.uglySide.call(
        'ritual_ZN12QColorDialog10setOptionsE6QFlagsINS_17ColorDialogOption'
        'EE',
        options.value,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QColorDialog::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QColorDialog::setVisible(bool visible)
    self.uglySide.call('ritual_ZN12QColorDialog10setVisibleEb', visible)

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
    Notes what was given, for Qt's 'QColorDialog::QColorDialog(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#QColorDialog

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QColorDialog::QColorDialog(QWidget *parent)
    self._noteCreation(QColorDialog, lambda: Rituals.call(
        'ritual_ZN12QColorDialogC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(QColor)
  @overload(QColor, QWidget)
  @overload(QColor, NoneType)
  def __init__(
      self,
      initial: QColor,
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QColorDialog::QColorDialog(const QColor
    &initial, QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#QColorDialog

    Parameters
    ----------

    initial : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QColorDialog::QColorDialog(const QColor &initial, QWidget *parent)
    self._noteCreation(QColorDialog, lambda: Rituals.call(
        'ritual_ZN12QColorDialogC1ERK6QColorP7QWidget',
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
    Calls Qt's 'void QColorDialog::open(QObject *receiver, const char
    *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qcolordialog.html#open

    Parameters
    ----------

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QColorDialog::open(QObject *receiver, const char *member)
    self.uglySide.call(
        'ritual_ZN12QColorDialog4openEP7QObjectPKc',
        self._addressOf(receiver), self._bytesOf(member),
    )
