"""
QQuickPlatformFontDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformfontdialog_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickPlatformFontDialog to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QPlatformFontDialogHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QFont, QWindow
  from . import QQuickFontDialogImpl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFont = WAIT['QFont']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPlatformFontDialog(QPlatformFontDialogHelper):
  """
  The cute side of Qt's QQuickPlatformFontDialog: a plain Python object
  standing in front of one C++ QQuickPlatformFontDialog.

  It is built on the cute 'QPlatformFontDialogHelper', as Qt's
  QQuickPlatformFontDialog is built on Qt's QPlatformFontDialogHelper, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPlatformFontDialog that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'tr', 'isValid',
  'setCurrentFont', 'currentFont', 'exec', 'show', 'hide', 'dialog'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPlatformFontDialog::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickPlatformFontDialog::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPlatformFontDialog::~QQuickPlatformFontDialog()': the
    destructor: Python never removes a C++ QQuickPlatformFontDialog.

  What has no ritual
  ------------------

  2 of the 15 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPlatformFontDialog is created at the first use, not by
    'QQuickPlatformFontDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPlatformFontDialog.
  - Qt tells when it has removed the C++ QQuickPlatformFontDialog. Every call
    on the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickPlatformFontDialog::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickplatformfontdialog.html#tr

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
    #  QString QQuickPlatformFontDialog::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuickPlatformFontDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPlatformFontDialog'

  #  A C++ QQuickPlatformFontDialog Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPlatformFontDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPlatformFontDialog::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfontdialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPlatformFontDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickPlatformFontDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickPlatformFontDialog::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfontdialog.html#isValid
    """
    #  bool QQuickPlatformFontDialog::isValid() const
    return self.uglySide.call(
        'ritual_ZNK24QQuickPlatformFontDialog7isValidEv',
    )

  def currentFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickPlatformFontDialog::currentFont() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfontdialog.html#currentFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickPlatformFontDialog::currentFont() const
    ritual = 'ritual_ZNK24QQuickPlatformFontDialog11currentFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK24QQuickPlatformFontDialog11currentFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def dialog(self) -> Optional[QQuickFontDialogImpl]:
    """
    Calls Qt's 'QQuickFontDialogImpl *QQuickPlatformFontDialog::dialog()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfontdialog.html#dialog

    Returns
    -------

    Optional[QQuickFontDialogImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFontDialogImpl *QQuickPlatformFontDialog::dialog() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickPlatformFontDialog6dialogEv',
    )
    from . import QQuickFontDialogImpl
    return QQuickFontDialogImpl._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFont)
  def setCurrentFont(self, font: QFont) -> None:
    """
    Calls Qt's 'void QQuickPlatformFontDialog::setCurrentFont(const QFont
    &font)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfontdialog.html#setCurrentFont

    Parameters
    ----------

    font : QFont
      Passed on as a value: Qt reads the C++ QFont, which stays Python's own.
    """
    #  void QQuickPlatformFontDialog::setCurrentFont(const QFont &font)
    ritual = 'ritual_ZN24QQuickPlatformFontDialog14setCurrentFontERK5QFont'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickPlatformFontDialog14setCurrentFontERK5QFont')
    self.uglySide.call(ritual, self._valueOf(font))

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
    'QQuickPlatformFontDialog::QQuickPlatformFontDialog(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformfontdialog.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickPlatformFontDialog::QQuickPlatformFontDialog(QObject *parent)
    self._noteCreation(QQuickPlatformFontDialog, lambda: Rituals.call(
        'ritual_ZN24QQuickPlatformFontDialogC1EP7QObject',
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
    Calls Qt's 'void QQuickPlatformFontDialog::exec()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickplatformfontdialog.html#exec
    """
    #  void QQuickPlatformFontDialog::exec()
    ritual = 'ritual_ZN24QQuickPlatformFontDialog4execEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickPlatformFontDialog4execEv'
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
    Calls Qt's 'bool QQuickPlatformFontDialog::show(Qt::WindowFlags flags,
    Qt::WindowModality modality, QWindow *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickplatformfontdialog.html#show

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
    #  bool QQuickPlatformFontDialog::show(Qt::WindowFlags flags,
    #      Qt::WindowModality modality, QWindow *parent)
    ritual = (
        'ritual_ZN24QQuickPlatformFontDialog4showE6QFlagsIN2Qt10WindowTypeE'
        'ENS1_14WindowModalityEP7QWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickPlatformFontDialog4showE6QFlagsIN2Qt10Windo'
          'wTypeEENS1_14WindowModalityEP7QWindow')
    return self.uglySide.call(
        ritual, flags.value, modality.value, self._addressOf(parent),
    )

  def hide(self) -> None:
    """
    Calls Qt's 'void QQuickPlatformFontDialog::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickplatformfontdialog.html#hide
    """
    #  void QQuickPlatformFontDialog::hide()
    ritual = 'ritual_ZN24QQuickPlatformFontDialog4hideEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickPlatformFontDialog4hideEv'
    self.uglySide.call(ritual)
