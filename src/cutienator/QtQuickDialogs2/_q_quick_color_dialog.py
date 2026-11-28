"""
QQuickColorDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2/6.12.0/QtQuickDialogs2/private/qquickcolordialog_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickColorDialog to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QColorDialogOptions
from . import QQuickAbstractDialog

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QPlatformDialogHelper
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QPlatformDialogHelper = WAIT['QPlatformDialogHelper']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickColorDialog(QQuickAbstractDialog):
  """
  The cute side of Qt's QQuickColorDialog: a plain Python object standing in
  front of one C++ QQuickColorDialog.

  It is built on the cute 'QQuickAbstractDialog', as Qt's QQuickColorDialog
  is built on Qt's QQuickAbstractDialog, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickColorDialog that has a ritual and that Python
  can call so far, 13 names in all: 'metaObject', 'tr',
  'qmlExtendedNamespace', 'selectedColor', 'setSelectedColor', 'options',
  'setOptions', 'resetOptions', 'selectedColorChanged', 'optionsChanged',
  'useNativeDialog', 'onCreate', 'onShow'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickColorDialog::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickColorDialog::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickColorDialog::qt_qmlMarker_extendedNamespace()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickColorDialog is created at the first use, not by
    'QQuickColorDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickColorDialog.
  - Qt tells when it has removed the C++ QQuickColorDialog. Every call on the
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
    Calls Qt's 'QString QQuickColorDialog::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialog.html#tr

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
    #  QString QQuickColorDialog::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickColorDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickColorDialog::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialog.html#qmlExtendedNamespace

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickColorDialog::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN17QQuickColorDialog20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickColorDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickColorDialog::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickColorDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickColorDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def selectedColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickColorDialog::selectedColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialog.html#selectedColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickColorDialog::selectedColor() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickColorDialog13selectedColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def options(self) -> QColorDialogOptions.ColorDialogOptions:
    """
    Calls Qt's 'QColorDialogOptions::ColorDialogOptions
    QQuickColorDialog::options() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialog.html#options

    Returns
    -------

    QColorDialogOptions.ColorDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  QColorDialogOptions::ColorDialogOptions QQuickColorDialog::options()
    #      const
    return QColorDialogOptions.ColorDialogOptions(self.uglySide.call(
        'ritual_ZNK17QQuickColorDialog7optionsEv',
    ))

  def useNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QQuickColorDialog::useNativeDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialog.html#useNativeDialog
    """
    #  bool QQuickColorDialog::useNativeDialog() const
    ritual = 'ritual_ZNK17QQuickColorDialog15useNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QQuickColorDialog15useNativeDialogEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setSelectedColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickColorDialog::setSelectedColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialog.html#setSelectedColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickColorDialog::setSelectedColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN17QQuickColorDialog16setSelectedColorERK6QColor',
        self._valueOf(color),
    )

  @overload(QColorDialogOptions.ColorDialogOptions)
  def setOptions(
      self,
      options: QColorDialogOptions.ColorDialogOptions,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickColorDialog::setOptions(QColorDialogOptions::ColorDialogOptions
    options)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialog.html#setOptions

    Parameters
    ----------

    options : QColorDialogOptions.ColorDialogOptions
      Passed on as its number.
    """
    #  void QQuickColorDialog::setOptions(QColorDialogOptions::
    #      ColorDialogOptions options)
    self.uglySide.call(
        'ritual_ZN17QQuickColorDialog10setOptionsE6QFlagsIN19QColorDialogOp'
        'tions17ColorDialogOptionEE',
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
    'QQuickColorDialog::QQuickColorDialog(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialog.html#QQuickColorDialog

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickColorDialog::QQuickColorDialog(QObject *parent)
    self._noteCreation(QQuickColorDialog, lambda: Rituals.call(
        'ritual_ZN17QQuickColorDialogC1EP7QObject',
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
    Calls Qt's 'void QQuickColorDialog::resetOptions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialog.html#resetOptions
    """
    #  void QQuickColorDialog::resetOptions()
    self.uglySide.call('ritual_ZN17QQuickColorDialog12resetOptionsEv')

  def selectedColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorDialog::selectedColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialog.html#selectedColorChanged
    """
    #  void QQuickColorDialog::selectedColorChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickColorDialog20selectedColorChangedEv',
    )

  def optionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickColorDialog::optionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcolordialog.html#optionsChanged
    """
    #  void QQuickColorDialog::optionsChanged()
    self.uglySide.call('ritual_ZN17QQuickColorDialog14optionsChangedEv')

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onCreate(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickColorDialog::onCreate(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialog.html#onCreate

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickColorDialog::onCreate(QPlatformDialogHelper *dialog)
    ritual = 'ritual_ZN17QQuickColorDialog8onCreateEP21QPlatformDialogHelper'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickColorDialog8onCreateEP21QPlatformDialogHelp'
          'er')
    self.uglySide.call(ritual, self._addressOf(dialog))

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onShow(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void QQuickColorDialog::onShow(QPlatformDialogHelper
    *dialog)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcolordialog.html#onShow

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickColorDialog::onShow(QPlatformDialogHelper *dialog)
    ritual = 'ritual_ZN17QQuickColorDialog6onShowEP21QPlatformDialogHelper'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickColorDialog6onShowEP21QPlatformDialogHelper')
    self.uglySide.call(ritual, self._addressOf(dialog))
