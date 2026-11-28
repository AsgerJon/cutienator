"""
QQuickPlatformMessageDialog binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickplatformmessagedialog_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickPlatformMessageDialog to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QPlatformMessageDialogHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QWindow
  from . import QQuickMessageDialogImpl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPlatformMessageDialog(QPlatformMessageDialogHelper):
  """
  The cute side of Qt's QQuickPlatformMessageDialog: a plain Python object
  standing in front of one C++ QQuickPlatformMessageDialog.

  It is built on the cute 'QPlatformMessageDialogHelper', as Qt's
  QQuickPlatformMessageDialog is built on Qt's QPlatformMessageDialogHelper,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPlatformMessageDialog that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'tr', 'isValid',
  'exec', 'show', 'hide', 'dialog'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPlatformMessageDialog::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickPlatformMessageDialog::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickPlatformMessageDialog::~QQuickPlatformMessageDialog()': the
    destructor: Python never removes a C++ QQuickPlatformMessageDialog.

  What has no ritual
  ------------------

  2 of the 13 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickPlatformMessageDialog is created at the first use, not by
    'QQuickPlatformMessageDialog(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPlatformMessageDialog.
  - Qt tells when it has removed the C++ QQuickPlatformMessageDialog. Every
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
    Calls Qt's 'QString QQuickPlatformMessageDialog::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformmessagedialog.html#tr

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
    #  QString QQuickPlatformMessageDialog::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN27QQuickPlatformMessageDialog2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPlatformMessageDialog'

  #  A C++ QQuickPlatformMessageDialog Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickPlatformMessageDialog'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPlatformMessageDialog::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformmessagedialog.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPlatformMessageDialog::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickPlatformMessageDialog10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickPlatformMessageDialog::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformmessagedialog.html#isValid
    """
    #  bool QQuickPlatformMessageDialog::isValid() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickPlatformMessageDialog7isValidEv',
    )

  def dialog(self) -> Optional[QQuickMessageDialogImpl]:
    """
    Calls Qt's 'QQuickMessageDialogImpl
    *QQuickPlatformMessageDialog::dialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformmessagedialog.html#dialog

    Returns
    -------

    Optional[QQuickMessageDialogImpl]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMessageDialogImpl *QQuickPlatformMessageDialog::dialog() const
    address = self.uglySide.call(
        'ritual_ZNK27QQuickPlatformMessageDialog6dialogEv',
    )
    from . import QQuickMessageDialogImpl
    return QQuickMessageDialogImpl._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    'QQuickPlatformMessageDialog::QQuickPlatformMessageDialog(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformmessagedialog.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickPlatformMessageDialog::QQuickPlatformMessageDialog(QObject
    #      *parent)
    self._noteCreation(QQuickPlatformMessageDialog, lambda: Rituals.call(
        'ritual_ZN27QQuickPlatformMessageDialogC1EP7QObject',
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
    Calls Qt's 'void QQuickPlatformMessageDialog::exec()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformmessagedialog.html#exec
    """
    #  void QQuickPlatformMessageDialog::exec()
    ritual = 'ritual_ZN27QQuickPlatformMessageDialog4execEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuickPlatformMessageDialog4execEv'
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
    Calls Qt's 'bool QQuickPlatformMessageDialog::show(Qt::WindowFlags flags,
    Qt::WindowModality modality, QWindow *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformmessagedialog.html#show

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
    #  bool QQuickPlatformMessageDialog::show(Qt::WindowFlags flags,
    #      Qt::WindowModality modality, QWindow *parent)
    ritual = (
        'ritual_ZN27QQuickPlatformMessageDialog4showE6QFlagsIN2Qt10WindowTy'
        'peEENS1_14WindowModalityEP7QWindow')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickPlatformMessageDialog4showE6QFlagsIN2Qt10Wi'
          'ndowTypeEENS1_14WindowModalityEP7QWindow')
    return self.uglySide.call(
        ritual, flags.value, modality.value, self._addressOf(parent),
    )

  def hide(self) -> None:
    """
    Calls Qt's 'void QQuickPlatformMessageDialog::hide()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickplatformmessagedialog.html#hide
    """
    #  void QQuickPlatformMessageDialog::hide()
    ritual = 'ritual_ZN27QQuickPlatformMessageDialog4hideEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuickPlatformMessageDialog4hideEv'
    self.uglySide.call(ritual)
