"""
QQuickLabsPlatformColorDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformcolordialog_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformColorDialog to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QQuickLabsPlatformDialog
from ..QtGui import QColorDialogOptions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

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


class QQuickLabsPlatformColorDialog(QQuickLabsPlatformDialog):
  """
  The cute side of Qt's QQuickLabsPlatformColorDialog: a plain Python object
  standing in front of one C++ QQuickLabsPlatformColorDialog.

  It is built on the cute 'QQuickLabsPlatformDialog', as Qt's
  QQuickLabsPlatformColorDialog is built on Qt's QQuickLabsPlatformDialog,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformColorDialog that has a ritual and
  that Python can call so far, 13 names in all: 'metaObject',
  'qmlExtendedNamespace', 'color', 'currentColor', 'setCurrentColor',
  'options', 'colorChanged', 'currentColorChanged', 'optionsChanged',
  'useNativeDialog', 'onCreate', 'onShow', 'accept'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformColorDialog::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformColorDialog::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void
    QQuickLabsPlatformColorDialog::qt_qmlMarker_extendedNamespace()': one of
    Qt's own inner workings.

  What has no ritual
  ------------------

  6 of the 22 functions Qt declares: 3 leans on
  'QQuickLabsPlatformColorDialog; 2 not a gap; 1 leans on 'vtable for
  QQuickLabsPlatformColorDialog', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformColorDialog is created at the first use, not by
    'QQuickLabsPlatformColorDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformColorDialog.
  - Qt tells when it has removed the C++ QQuickLabsPlatformColorDialog. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformColorDialog that has no cute function
    yet, '__init__', 'setColor', 'setOptions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def qmlExtendedNamespace() -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformColorDialog::qmlExtendedNamespace()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *QQuickLabsPlatformColorDialog::qmlExtendedNamespace()
    address = Rituals.call(
        'ritual_ZN29QQuickLabsPlatformColorDialog20qmlExtendedNamespaceEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLabsPlatformColorDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QQuickLabsPlatformColorDialog::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformColorDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickLabsPlatformColorDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickLabsPlatformColorDialog::color() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickLabsPlatformColorDialog::color() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickLabsPlatformColorDialog5colorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def currentColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickLabsPlatformColorDialog::currentColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html#currentColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickLabsPlatformColorDialog::currentColor() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickLabsPlatformColorDialog12currentColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def options(self) -> QColorDialogOptions.ColorDialogOptions:
    """
    Calls Qt's 'QColorDialogOptions::ColorDialogOptions
    QQuickLabsPlatformColorDialog::options() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html#options

    Returns
    -------

    QColorDialogOptions.ColorDialogOptions
      The value standing for the combination Qt gave back.
    """
    #  QColorDialogOptions::ColorDialogOptions
    #      QQuickLabsPlatformColorDialog::options() const
    return QColorDialogOptions.ColorDialogOptions(self.uglySide.call(
        'ritual_ZNK29QQuickLabsPlatformColorDialog7optionsEv',
    ))

  def useNativeDialog(self) -> bool:
    """
    Calls Qt's 'bool QQuickLabsPlatformColorDialog::useNativeDialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html#useNativeDialog
    """
    #  bool QQuickLabsPlatformColorDialog::useNativeDialog() const
    ritual = 'ritual_ZNK29QQuickLabsPlatformColorDialog15useNativeDialogEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QQuickLabsPlatformColorDialog15useNativeDialogEv')
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setCurrentColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformColorDialog::setCurrentColor(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html#setCurrentColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickLabsPlatformColorDialog::setCurrentColor(const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN29QQuickLabsPlatformColorDialog15setCurrentColorERK6QColo'
        'r',
        self._valueOf(color),
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
    Qt's
    'QQuickLabsPlatformColorDialog::QQuickLabsPlatformColorDialog(QObject
    *parent)': leans on 'vtable for QQuickLabsPlatformColorDialog', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformColorDialog.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickLabsPlatformColorDialog::QQuickLabsPlatformColorDialog(QObje"
        "ct *parent)': leans on 'vtable for QQuickLabsPlatformColorDialog', "
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

  def colorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformColorDialog::colorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html#colorChanged
    """
    #  void QQuickLabsPlatformColorDialog::colorChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickLabsPlatformColorDialog12colorChangedEv',
    )

  def currentColorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformColorDialog::currentColorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html
    """
    #  void QQuickLabsPlatformColorDialog::currentColorChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickLabsPlatformColorDialog19currentColorChangedEv',
    )

  def optionsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformColorDialog::optionsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html#optionsChanged
    """
    #  void QQuickLabsPlatformColorDialog::optionsChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickLabsPlatformColorDialog14optionsChangedEv',
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onCreate(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformColorDialog::onCreate(QPlatformDialogHelper *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html#onCreate

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformColorDialog::onCreate(QPlatformDialogHelper
    #      *dialog)
    self.uglySide.call(
        'ritual_ZN29QQuickLabsPlatformColorDialog8onCreateEP21QPlatformDial'
        'ogHelper',
        self._addressOf(dialog),
    )

  @overload(QPlatformDialogHelper)
  @overload(NoneType)
  def onShow(self, dialog: Optional[QPlatformDialogHelper]) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformColorDialog::onShow(QPlatformDialogHelper *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html#onShow

    Parameters
    ----------

    dialog : Optional[QPlatformDialogHelper]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLabsPlatformColorDialog::onShow(QPlatformDialogHelper
    #      *dialog)
    ritual = (
        'ritual_ZN29QQuickLabsPlatformColorDialog6onShowEP21QPlatformDialog'
        'Helper')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QQuickLabsPlatformColorDialog6onShowEP21QPlatform'
          'DialogHelper')
    self.uglySide.call(ritual, self._addressOf(dialog))

  def accept(self) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformColorDialog::accept()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformcolordialog.html#accept
    """
    #  void QQuickLabsPlatformColorDialog::accept()
    self.uglySide.call('ritual_ZN29QQuickLabsPlatformColorDialog6acceptEv')

  @staticmethod
  def setColor(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformColorDialog::setColor(const QColor &color)':
    leans on 'QQuickLabsPlatformColorDialog::colorChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformColorDialog.setColor' has no cute function yet. "
        "Qt's 'void QQuickLabsPlatformColorDialog::setColor(const QColor "
        "&color)': leans on "
        "'QQuickLabsPlatformColorDialog::colorChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickLabsPlatformColorDialog::setOptions(QColorDialogOptions::
    ColorDialogOptions options)': leans on
    'QQuickLabsPlatformColorDialog::optionsChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformColorDialog.setOptions' has no cute function "
        "yet. Qt's 'void "
        "QQuickLabsPlatformColorDialog::setOptions(QColorDialogOptions::Colo"
        "rDialogOptions options)': leans on "
        "'QQuickLabsPlatformColorDialog::optionsChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
