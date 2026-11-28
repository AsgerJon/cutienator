"""
QQuickFileDialogDelegate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFileDialogDelegate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QKeyEvent
  from ..QtQuick import QQuickItem
  from . import QQuickFileDialogDelegatePrivate
  from ..QtQuickTemplates2 import QQuickDialog
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']
  QQuickDialog = WAIT['QQuickDialog']
  QQuickItem = WAIT['QQuickItem']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFileDialogDelegate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFileDialogDelegate: a plain Python object
  standing in front of one C++ QQuickFileDialogDelegate.

  What exists
  -----------

  Every function of Qt's QQuickFileDialogDelegate that has a ritual and that
  Python can call so far, 10 names in all: 'metaObject', 'tr', 'dialog',
  'setDialog', 'file', 'setFile', 'dialogChanged', 'fileChanged',
  'keyReleaseEvent', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFileDialogDelegate::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QQuickFileDialogDelegate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickFileDialogDelegatePrivate
    *QQuickFileDialogDelegate::d_func() const': takes in Python what
    'QQuickFileDialogDelegatePrivate *QQuickFileDialogDelegate::d_func()'
    takes.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickFileDialogDelegate is created at the first use, not by
    'QQuickFileDialogDelegate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFileDialogDelegate.
  - Qt tells when it has removed the C++ QQuickFileDialogDelegate. Every call
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
    Calls Qt's 'QString QQuickFileDialogDelegate::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialogdelegate.html#tr

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
    #  QString QQuickFileDialogDelegate::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QQuickFileDialogDelegate2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFileDialogDelegate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFileDialogDelegate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFileDialogDelegate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickFileDialogDelegate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dialog(self) -> Optional[QQuickDialog]:
    """
    Calls Qt's 'QQuickDialog *QQuickFileDialogDelegate::dialog() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegate.html#dialog

    Returns
    -------

    Optional[QQuickDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialog *QQuickFileDialogDelegate::dialog() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickFileDialogDelegate6dialogEv',
    )
    from ..QtQuickTemplates2 import QQuickDialog
    return QQuickDialog._cuteAt(address)

  def file(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickFileDialogDelegate::file() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfiledialogdelegate.html#file

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickFileDialogDelegate::file() const
    address = self.uglySide.call(
        'ritual_ZNK24QQuickFileDialogDelegate4fileEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickDialog)
  @overload(NoneType)
  def setDialog(self, dialog: Optional[QQuickDialog]) -> None:
    """
    Calls Qt's 'void QQuickFileDialogDelegate::setDialog(QQuickDialog
    *dialog)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegate.html#setDialog

    Parameters
    ----------

    dialog : Optional[QQuickDialog]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialogDelegate::setDialog(QQuickDialog *dialog)
    self.uglySide.call(
        'ritual_ZN24QQuickFileDialogDelegate9setDialogEP12QQuickDialog',
        self._addressOf(dialog),
    )

  @overload(QUrl)
  def setFile(self, file: QUrl) -> None:
    """
    Calls Qt's 'void QQuickFileDialogDelegate::setFile(const QUrl &file)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegate.html#setFile

    Parameters
    ----------

    file : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickFileDialogDelegate::setFile(const QUrl &file)
    self.uglySide.call(
        'ritual_ZN24QQuickFileDialogDelegate7setFileERK4QUrl',
        self._valueOf(file),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickFileDialogDelegate::QQuickFileDialogDelegate(QQuickItem *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegate.html

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFileDialogDelegate::QQuickFileDialogDelegate(QQuickItem *parent)
    self._noteCreation(QQuickFileDialogDelegate, lambda: Rituals.call(
        'ritual_ZN24QQuickFileDialogDelegateC1EP10QQuickItem',
        self._addressOf(parent),
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

  def dialogChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogDelegate::dialogChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegate.html#dialogChanged
    """
    #  void QQuickFileDialogDelegate::dialogChanged()
    self.uglySide.call(
        'ritual_ZN24QQuickFileDialogDelegate13dialogChangedEv',
    )

  def fileChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogDelegate::fileChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegate.html#fileChanged
    """
    #  void QQuickFileDialogDelegate::fileChanged()
    self.uglySide.call('ritual_ZN24QQuickFileDialogDelegate11fileChangedEv')

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyReleaseEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickFileDialogDelegate::keyReleaseEvent(QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegate.html#keyReleaseEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickFileDialogDelegate::keyReleaseEvent(QKeyEvent *event)
    ritual = (
        'ritual_ZN24QQuickFileDialogDelegate15keyReleaseEventEP9QKeyEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN24QQuickFileDialogDelegate15keyReleaseEventEP9QKeyE'
          'vent')
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QQuickFileDialogDelegatePrivate]:
    """
    Calls Qt's 'QQuickFileDialogDelegatePrivate
    *QQuickFileDialogDelegate::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegate.html#d_func

    Returns
    -------

    Optional[QQuickFileDialogDelegatePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileDialogDelegatePrivate *QQuickFileDialogDelegate::d_func()
    address = self.uglySide.call(
        'ritual_ZN24QQuickFileDialogDelegate6d_funcEv',
    )
    from . import QQuickFileDialogDelegatePrivate
    return QQuickFileDialogDelegatePrivate._cuteAt(address)
