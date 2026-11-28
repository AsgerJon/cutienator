"""
QQuickPlatformColorDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformcolordialog_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickPlatformColorDialog to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QPlatformColorDialogHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QWindow
  from . import QQuickColorDialogImpl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPlatformColorDialog(QPlatformColorDialogHelper):
  """
  The cute side of Qt's QQuickPlatformColorDialog: a plain Python object
  standing in front of one C++ QQuickPlatformColorDialog.

  It is built on the cute 'QPlatformColorDialogHelper', as Qt's
  QQuickPlatformColorDialog is built on Qt's QPlatformColorDialogHelper, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPlatformColorDialog that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'isValid',
  'setCurrentColor', 'currentColor', 'exec', 'show', 'hide', 'dialog'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPlatformColorDialog::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickPlatformColorDialog::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPlatformColorDialog::~QQuickPlatformColorDialog()': the
    destructor: Python never removes a C++ QQuickPlatformColorDialog.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPlatformColorDialog is created at the first use, not by
    'QQuickPlatformColorDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPlatformColorDialog.
  - Qt tells when it has removed the C++ QQuickPlatformColorDialog. Every
    call on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickPlatformColorDialog::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickplatformcolordialog.html#tr

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
    #  QString QQuickPlatformColorDialog::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QQuickPlatformColorDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPlatformColorDialog'

  #  A C++ QQuickPlatformColorDialog Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPlatformColorDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPlatformColorDialog::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformcolordialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPlatformColorDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickPlatformColorDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickPlatformColorDialog::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformcolordialog.html#isValid
    """
    #  bool QQuickPlatformColorDialog::isValid() const
    return self.uglySide.call(
        'ritual_ZNK25QQuickPlatformColorDialog7isValidEv',
    )

  def currentColor(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickPlatformColorDialog::currentColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformcolordialog.html#currentColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickPlatformColorDialog::currentColor() const
    ritual = 'ritual_ZNK25QQuickPlatformColorDialog12currentColorEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK25QQuickPlatformColorDialog12currentColorEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def dialog(self) -> Optional[QQuickColorDialogImpl]:
    """
    Calls Qt's 'QQuickColorDialogImpl *QQuickPlatformColorDialog::dialog()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformcolordialog.html#dialog

    Returns
    -------

    Optional[QQuickColorDialogImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickColorDialogImpl *QQuickPlatformColorDialog::dialog() const
    address = self.uglySide.call(
        'ritual_ZNK25QQuickPlatformColorDialog6dialogEv',
    )
    from . import QQuickColorDialogImpl
    return QQuickColorDialogImpl._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setCurrentColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickPlatformColorDialog::setCurrentColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformcolordialog.html#setCurrentColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickPlatformColorDialog::setCurrentColor(const QColor &color)
    ritual = (
        'ritual_ZN25QQuickPlatformColorDialog15setCurrentColorERK6QColor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickPlatformColorDialog15setCurrentColorERK6QCo'
          'lor')
    self.uglySide.call(ritual, self._valueOf(color))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPlatformColorDialog::QQuickPlatformColorDialog(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformcolordialog.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickPlatformColorDialog::QQuickPlatformColorDialog(QObject *parent)
    self._noteCreation(QQuickPlatformColorDialog, lambda: Rituals.call(
        'ritual_ZN25QQuickPlatformColorDialogC1EP7QObject',
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

  def exec(self) -> None:
    """
    Calls Qt's 'void QQuickPlatformColorDialog::exec()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformcolordialog.html#exec
    """
    #  void QQuickPlatformColorDialog::exec()
    ritual = 'ritual_ZN25QQuickPlatformColorDialog4execEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QQuickPlatformColorDialog4execEv'
    self.uglySide.call(ritual)

  @overload(Qt.WindowFlags, Qt.WindowModality, QWindow)
  @overload(Qt.WindowFlags, Qt.WindowModality, NoneType)
  def show(
      self,
      flags: Qt.WindowFlags,
      modality: Qt.WindowModality,
      parent: Optional[QWindow],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickPlatformColorDialog::show(Qt::WindowFlags flags,
    Qt::WindowModality modality, QWindow *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformcolordialog.html#show

    Parameters
    ----------

    flags : Qt.WindowFlags
      Passed on as its number.

    modality : Qt.WindowModality
      Passed on as its number.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPlatformColorDialog::show(Qt::WindowFlags flags,
    #      Qt::WindowModality modality, QWindow *parent)
    ritual = (
        'ritual_ZN25QQuickPlatformColorDialog4showE6QFlagsIN2Qt10WindowType'
        'EENS1_14WindowModalityEP7QWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickPlatformColorDialog4showE6QFlagsIN2Qt10Wind'
          'owTypeEENS1_14WindowModalityEP7QWindow')
    return self.uglySide.call(
        ritual, flags.value, modality.value, self._addressOf(parent),
    )

  def hide(self) -> None:
    """
    Calls Qt's 'void QQuickPlatformColorDialog::hide()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformcolordialog.html#hide
    """
    #  void QQuickPlatformColorDialog::hide()
    ritual = 'ritual_ZN25QQuickPlatformColorDialog4hideEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QQuickPlatformColorDialog4hideEv'
    self.uglySide.call(ritual)
