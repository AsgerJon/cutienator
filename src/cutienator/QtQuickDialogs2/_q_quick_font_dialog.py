"""
QQuickFontDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickfontdialog_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickFontDialog to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QFontDialogOptions
from . import QQuickAbstractDialog

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont, QPlatformDialogHelper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QPlatformDialogHelper = WAIT['QPlatformDialogHelper']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFontDialog(QQuickAbstractDialog):
  """
  The cute side of Qt's QQuickFontDialog: a plain Python object standing in
  front of one C++ QQuickFontDialog.

  It is built on the cute 'QQuickAbstractDialog', as Qt's QQuickFontDialog is
  built on Qt's QQuickAbstractDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFontDialog that has a ritual and that Python
  can call so far, 16 names in all: 'metaObject', 'tr',
  'qmlExtendedNamespace', 'setCurrentFont', 'currentFont', 'setSelectedFont',
  'selectedFont', 'options', 'setOptions', 'resetOptions',
  'selectedFontChanged', 'currentFontChanged', 'optionsChanged',
  'useNativeDialog', 'onCreate', 'onShow'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFontDialog::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickFontDialog::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickFontDialog::qt_qmlMarker_extendedNamespace()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFontDialog is created at the first use, not by
    'QQuickFontDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFontDialog.
  - Qt tells when it has removed the C++ QQuickFontDialog. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickFontDialog::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontdialog.html#tr

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
    #  QString QQuickFontDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickFontDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFontDialog::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialog.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFontDialog::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN16QQuickFontDialog20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFontDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFontDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFontDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFontDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickFontDialog::currentFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontdialog.html#currentFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickFontDialog::currentFont() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFontDialog11currentFontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def selectedFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickFontDialog::selectedFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontdialog.html#selectedFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickFontDialog::selectedFont() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickFontDialog12selectedFontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def options(self) -> QFontDialogOptions.FontDialogOptions:
    """
    Calls Qt's 'QFontDialogOptions::FontDialogOptions
    QQuickFontDialog::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontdialog.html#options

    Returns
    -------

    QFontDialogOptions.FontDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  QFontDialogOptions::FontDialogOptions QQuickFontDialog::options()
    #      const
    return QFontDialogOptions.FontDialogOptions(self.uglySide.call(
        'ritual_ZNK16QQuickFontDialog7optionsEv',
    ))

  def useNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QQuickFontDialog::useNativeDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialog.html#useNativeDialog
    """
    #  bool QQuickFontDialog::useNativeDialog() const
    ritual = 'ritual_ZNK16QQuickFontDialog15useNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QQuickFontDialog15useNativeDialogEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setCurrentFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickFontDialog::setCurrentFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialog.html#setCurrentFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickFontDialog::setCurrentFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN16QQuickFontDialog14setCurrentFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QFont)
  def setSelectedFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickFontDialog::setSelectedFont(const QFont &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialog.html#setSelectedFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickFontDialog::setSelectedFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN16QQuickFontDialog15setSelectedFontERK5QFont',
        self._valueOf(font),
    )

  @overload(QFontDialogOptions.FontDialogOptions)
  def setOptions(
      self,
      options: QFontDialogOptions.FontDialogOptions,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickFontDialog::setOptions(QFontDialogOptions::FontDialogOptions
    options)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontdialog.html#setOptions

    Parameters
    ----------

    options : QFontDialogOptions.FontDialogOptions
      Passed on as its number.
    """
    #  void
    #      QQuickFontDialog::setOptions(QFontDialogOptions::FontDialogOptions
    #      options)
    self.uglySide.call(
        'ritual_ZN16QQuickFontDialog10setOptionsE6QFlagsIN18QFontDialogOpti'
        'ons16FontDialogOptionEE',
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickFontDialog::QQuickFontDialog(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialog.html#QQuickFontDialog

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFontDialog::QQuickFontDialog(QObject *parent)
    self._noteCreation(QQuickFontDialog, lambda: Rituals.call(
        'ritual_ZN16QQuickFontDialogC1EP7QObject',
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

  def resetOptions(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialog::resetOptions()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontdialog.html#resetOptions
    """
    #  void QQuickFontDialog::resetOptions()
    self.uglySide.call('ritual_ZN16QQuickFontDialog12resetOptionsEv')

  def selectedFontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialog::selectedFontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialog.html#selectedFontChanged
    """
    #  void QQuickFontDialog::selectedFontChanged()
    self.uglySide.call('ritual_ZN16QQuickFontDialog19selectedFontChangedEv')

  def currentFontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialog::currentFontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialog.html#currentFontChanged
    """
    #  void QQuickFontDialog::currentFontChanged()
    self.uglySide.call('ritual_ZN16QQuickFontDialog18currentFontChangedEv')

  def optionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFontDialog::optionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfontdialog.html#optionsChanged
    """
    #  void QQuickFontDialog::optionsChanged()
    self.uglySide.call('ritual_ZN16QQuickFontDialog14optionsChangedEv')

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onCreate(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickFontDialog::onCreate(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontdialog.html#onCreate

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialog::onCreate(QPlatformDialogHelper *dialog)
    ritual = 'ritual_ZN16QQuickFontDialog8onCreateEP21QPlatformDialogHelper'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickFontDialog8onCreateEP21QPlatformDialogHelpe'
          'r')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onShow(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickFontDialog::onShow(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfontdialog.html#onShow

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFontDialog::onShow(QPlatformDialogHelper *dialog)
    ritual = 'ritual_ZN16QQuickFontDialog6onShowEP21QPlatformDialogHelper'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QQuickFontDialog6onShowEP21QPlatformDialogHelper')
    self.uglySide.call(ritual, self._addressOf(dialog))
