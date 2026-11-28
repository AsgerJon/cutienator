"""
QQuickLabsPlatformFontDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformfontdialog_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformFontDialog to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickLabsPlatformDialog
from ..QtGui import QFontDialogOptions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

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


class QQuickLabsPlatformFontDialog(QQuickLabsPlatformDialog):
  """
  The cute side of Qt's QQuickLabsPlatformFontDialog: a plain Python object
  standing in front of one C++ QQuickLabsPlatformFontDialog.

  It is built on the cute 'QQuickLabsPlatformDialog', as Qt's
  QQuickLabsPlatformFontDialog is built on Qt's QQuickLabsPlatformDialog, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformFontDialog that has a ritual and
  that Python can call so far, 13 names in all: 'metaObject',
  'qmlExtendedNamespace', 'font', 'currentFont', 'setCurrentFont', 'options',
  'fontChanged', 'currentFontChanged', 'optionsChanged', 'useNativeDialog',
  'onCreate', 'onShow', 'accept'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformFontDialog::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformFontDialog::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QQuickLabsPlatformFontDialog::qt_qmlMarker_extendedNamespace()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 22 functions Qt declares: 3 leans on
  'QQuickLabsPlatformFontDialog; 2 not a gap; 1 leans on 'vtable for
  QQuickLabsPlatformFontDialog', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformFontDialog is created at the first use, not by
    'QQuickLabsPlatformFontDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformFontDialog.
  - Qt tells when it has removed the C++ QQuickLabsPlatformFontDialog. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformFontDialog that has no cute function
    yet, '__init__', 'setFont', 'setOptions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformFontDialog::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuickLabsPlatformFontDialog::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN28QQuickLabsPlatformFontDialog20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformFontDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickLabsPlatformFontDialog::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformFontDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFontDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def font(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickLabsPlatformFontDialog::font() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html#font

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickLabsPlatformFontDialog::font() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFontDialog4fontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def currentFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickLabsPlatformFontDialog::currentFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html#currentFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickLabsPlatformFontDialog::currentFont() const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFontDialog11currentFontEv',
    )
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def options(self) -> QFontDialogOptions.FontDialogOptions:
    """
    Calls Qt's 'QFontDialogOptions::FontDialogOptions
    QQuickLabsPlatformFontDialog::options() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html#options

    Returns
    -------

    QFontDialogOptions.FontDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  QFontDialogOptions::FontDialogOptions
    #      QQuickLabsPlatformFontDialog::options() const
    return QFontDialogOptions.FontDialogOptions(self.uglySide.call(
        'ritual_ZNK28QQuickLabsPlatformFontDialog7optionsEv',
    ))

  def useNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformFontDialog::useNativeDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html#useNativeDialog
    """
    #  bool QQuickLabsPlatformFontDialog::useNativeDialog() const
    ritual = 'ritual_ZNK28QQuickLabsPlatformFontDialog15useNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QQuickLabsPlatformFontDialog15useNativeDialogEv')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setCurrentFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFontDialog::setCurrentFont(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html#setCurrentFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickLabsPlatformFontDialog::setCurrentFont(const QFont &font)
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFontDialog14setCurrentFontERK5QFont',
        self._valueOf(font),
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
    Qt's 'QQuickLabsPlatformFontDialog::QQuickLabsPlatformFontDialog(QObject
    *parent)': leans on 'vtable for QQuickLabsPlatformFontDialog', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFontDialog.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickLabsPlatformFontDialog::QQuickLabsPlatformFontDialog(QObject"
        " *parent)': leans on 'vtable for QQuickLabsPlatformFontDialog', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def fontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFontDialog::fontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html#fontChanged
    """
    #  void QQuickLabsPlatformFontDialog::fontChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFontDialog11fontChangedEv',
    )

  def currentFontChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFontDialog::currentFontChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html
    """
    #  void QQuickLabsPlatformFontDialog::currentFontChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFontDialog18currentFontChangedEv',
    )

  def optionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFontDialog::optionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html#optionsChanged
    """
    #  void QQuickLabsPlatformFontDialog::optionsChanged()
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFontDialog14optionsChangedEv',
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onCreate(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformFontDialog::onCreate(QPlatformDialogHelper *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html#onCreate

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformFontDialog::onCreate(QPlatformDialogHelper
    #      *dialog)
    self.uglySide.call(
        'ritual_ZN28QQuickLabsPlatformFontDialog8onCreateEP21QPlatformDialo'
        'gHelper',
        self._addressOf(dialog),
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onShow(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformFontDialog::onShow(QPlatformDialogHelper *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html#onShow

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformFontDialog::onShow(QPlatformDialogHelper
    #      *dialog)
    ritual = (
        'ritual_ZN28QQuickLabsPlatformFontDialog6onShowEP21QPlatformDialogH'
        'elper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QQuickLabsPlatformFontDialog6onShowEP21QPlatformD'
          'ialogHelper')
    self.uglySide.call(ritual, self._addressOf(dialog))

  def accept(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFontDialog::accept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfontdialog.html#accept
    """
    #  void QQuickLabsPlatformFontDialog::accept()
    self.uglySide.call('ritual_ZN28QQuickLabsPlatformFontDialog6acceptEv')

  @staticmethod
  def setFont(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFontDialog::setFont(const QFont &font)':
    leans on 'QQuickLabsPlatformFontDialog::fontChanged()', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFontDialog.setFont' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformFontDialog::setFont(const QFont "
        "&font)': leans on 'QQuickLabsPlatformFontDialog::fontChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFontDialog::setOptions(QFontDialogOptions::
    FontDialogOptions options)': leans on
    'QQuickLabsPlatformFontDialog::optionsChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFontDialog.setOptions' has no cute function "
        "yet. Qt's 'void "
        "QQuickLabsPlatformFontDialog::setOptions(QFontDialogOptions::FontDi"
        "alogOptions options)': leans on "
        "'QQuickLabsPlatformFontDialog::optionsChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
