"""
QQuickFileDialogImplAttachedPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFileDialogImplAttachedPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickFileDialogImplAttached


class QQuickFileDialogImplAttachedPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickFileDialogImplAttachedPrivate: a plain Python
  object standing in front of one C++ QQuickFileDialogImplAttachedPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QQuickFileDialogImplAttachedPrivate is built on Qt's QObjectPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFileDialogImplAttachedPrivate that has a
  ritual and that Python can call so far, 3 names in all:
  'fileNameEditedByUser', 'fileNameEditingByUserFinished', 'q_func'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickFileDialogImplAttached
    *QQuickFileDialogImplAttachedPrivate::q_func() const': takes in Python
    what 'QQuickFileDialogImplAttached
    *QQuickFileDialogImplAttachedPrivate::q_func()' takes.

  What has no ritual
  ------------------

  2 of the 6 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickFileDialogImplAttachedPrivate is created at the first use,
    not by 'QQuickFileDialogImplAttachedPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFileDialogImplAttachedPrivate.
  - Each name of Qt's QQuickFileDialogImplAttachedPrivate that has no cute
    function yet, 'fileDialogListViewCurrentIndexChanged',
    'nameFiltersComboBoxItemActivated', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFileDialogImplAttachedPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def fileNameEditedByUser(self) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttachedPrivate::fileNameEditedByUser()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattachedprivate.html
    """
    #  void QQuickFileDialogImplAttachedPrivate::fileNameEditedByUser()
    self.uglySide.call(
        'ritual_ZN35QQuickFileDialogImplAttachedPrivate20fileNameEditedByUs'
        'erEv',
    )

  def fileNameEditingByUserFinished(self) -> None:
    """
    Calls Qt's 'void
    QQuickFileDialogImplAttachedPrivate::fileNameEditingByUserFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattachedprivate.html
    """
    #  void QQuickFileDialogImplAttachedPrivate::
    #      fileNameEditingByUserFinished()
    self.uglySide.call(
        'ritual_ZN35QQuickFileDialogImplAttachedPrivate29fileNameEditingByU'
        'serFinishedEv',
    )

  def q_func(self) -> Optional[QQuickFileDialogImplAttached]:
    """
    Calls Qt's 'QQuickFileDialogImplAttached
    *QQuickFileDialogImplAttachedPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogimplattachedprivate.html#q_func

    Returns
    -------

    Optional[QQuickFileDialogImplAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileDialogImplAttached
    #      *QQuickFileDialogImplAttachedPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN35QQuickFileDialogImplAttachedPrivate6q_funcEv',
    )
    from . import QQuickFileDialogImplAttached
    return QQuickFileDialogImplAttached._cuteAt(address)

  @staticmethod
  def fileDialogListViewCurrentIndexChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickFileDialogImplAttachedPrivate::
    fileDialogListViewCurrentIndexChanged()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file: use
    of undeclared identifier 'lcAttachedCurrentIndex'.
    """
    raise NotImplementedError(
        "'QQuickFileDialogImplAttachedPrivate.fileDialogListViewCurrentIndex"
        "Changed' has no cute function yet. Qt's 'void "
        "QQuickFileDialogImplAttachedPrivate::fileDialogListViewCurrentIndex"
        "Changed()': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'lcAttachedCurrentIndex'.")

  @staticmethod
  def nameFiltersComboBoxItemActivated(*__, **_) -> Never:
    """
    Qt's 'void
    QQuickFileDialogImplAttachedPrivate::nameFiltersComboBoxItemActivated(int
    index)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'lcAttachedNameFilters'.
    """
    raise NotImplementedError(
        "'QQuickFileDialogImplAttachedPrivate.nameFiltersComboBoxItemActivat"
        "ed' has no cute function yet. Qt's 'void "
        "QQuickFileDialogImplAttachedPrivate::nameFiltersComboBoxItemActivat"
        "ed(int index)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'lcAttachedNameFilters'.")
