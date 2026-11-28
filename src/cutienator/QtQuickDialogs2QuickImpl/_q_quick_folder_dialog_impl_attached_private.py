"""
QQuickFolderDialogImplAttachedPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFolderDialogImplAttachedPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QQuickFolderDialogImplAttached


class QQuickFolderDialogImplAttachedPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickFolderDialogImplAttachedPrivate: a plain Python
  object standing in front of one C++ QQuickFolderDialogImplAttachedPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QQuickFolderDialogImplAttachedPrivate is built on Qt's QObjectPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFolderDialogImplAttachedPrivate that has a
  ritual and that Python can call so far, 2 names in all: 'q_func',
  'folderDialogListViewCurrentIndexChanged'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickFolderDialogImplAttached
    *QQuickFolderDialogImplAttachedPrivate::q_func() const': takes in Python
    what 'QQuickFolderDialogImplAttached
    *QQuickFolderDialogImplAttachedPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QQuickFolderDialogImplAttachedPrivate is created at the first
    use, not by 'QQuickFolderDialogImplAttachedPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFolderDialogImplAttachedPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFolderDialogImplAttachedPrivate'

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

  def q_func(self) -> Optional[QQuickFolderDialogImplAttached]:
    """
    Calls Qt's 'QQuickFolderDialogImplAttached
    *QQuickFolderDialogImplAttachedPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplattachedprivate.html#q_func

    Returns
    -------

    Optional[QQuickFolderDialogImplAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFolderDialogImplAttached
    #      *QQuickFolderDialogImplAttachedPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN37QQuickFolderDialogImplAttachedPrivate6q_funcEv',
    )
    from . import QQuickFolderDialogImplAttached
    return QQuickFolderDialogImplAttached._cuteAt(address)

  def folderDialogListViewCurrentIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFolderDialogImplAttachedPrivate::
    folderDialogListViewCurrentIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfolderdialogimplattachedprivate.html
    """
    #  void QQuickFolderDialogImplAttachedPrivate::
    #      folderDialogListViewCurrentIndexChanged()
    self.uglySide.call(
        'ritual_ZN37QQuickFolderDialogImplAttachedPrivate39folderDialogList'
        'ViewCurrentIndexChangedEv',
    )
