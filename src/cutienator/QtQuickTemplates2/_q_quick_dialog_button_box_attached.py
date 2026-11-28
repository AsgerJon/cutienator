"""
QQuickDialogButtonBoxAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickDialogButtonBoxAttached to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QPlatformDialogHelper

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickDialogButtonBox, QQuickDialogButtonBoxAttachedPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDialogButtonBoxAttached(QObject):
  """
  The cute side of Qt's QQuickDialogButtonBoxAttached: a plain Python object
  standing in front of one C++ QQuickDialogButtonBoxAttached.

  It is built on the cute 'QObject', as Qt's QQuickDialogButtonBoxAttached is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDialogButtonBoxAttached that has a ritual and
  that Python can call so far, 8 names in all: 'metaObject', 'tr',
  'buttonBox', 'buttonRole', 'setButtonRole', 'buttonBoxChanged',
  'buttonRoleChanged', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDialogButtonBoxAttached::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QQuickDialogButtonBoxAttached::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickDialogButtonBoxAttachedPrivate
    *QQuickDialogButtonBoxAttached::d_func() const': takes in Python what
    'QQuickDialogButtonBoxAttachedPrivate
    *QQuickDialogButtonBoxAttached::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickDialogButtonBoxAttached is created at the first use, not by
    'QQuickDialogButtonBoxAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDialogButtonBoxAttached.
  - Qt tells when it has removed the C++ QQuickDialogButtonBoxAttached. Every
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
    Calls Qt's 'QString QQuickDialogButtonBoxAttached::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxattached.html#tr

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
    #  QString QQuickDialogButtonBoxAttached::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QQuickDialogButtonBoxAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDialogButtonBoxAttached'

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
    *QQuickDialogButtonBoxAttached::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDialogButtonBoxAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickDialogButtonBoxAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def buttonBox(self) -> Optional[QQuickDialogButtonBox]:
    """
    Calls Qt's 'QQuickDialogButtonBox
    *QQuickDialogButtonBoxAttached::buttonBox() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxattached.html#buttonBox

    Returns
    -------

    Optional[QQuickDialogButtonBox]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogButtonBox *QQuickDialogButtonBoxAttached::buttonBox()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QQuickDialogButtonBoxAttached9buttonBoxEv',
    )
    from . import QQuickDialogButtonBox
    return QQuickDialogButtonBox._cuteAt(address)

  def buttonRole(self) -> QPlatformDialogHelper.ButtonRole:
    """
    Calls Qt's 'QPlatformDialogHelper::ButtonRole
    QQuickDialogButtonBoxAttached::buttonRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxattached.html#buttonRole

    Returns
    -------

    QPlatformDialogHelper.ButtonRole
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPlatformDialogHelper.ButtonRole(number)' gives.
    """
    #  QPlatformDialogHelper::ButtonRole
    #      QQuickDialogButtonBoxAttached::buttonRole() const
    return QPlatformDialogHelper.ButtonRole(self.uglySide.call(
        'ritual_ZNK29QQuickDialogButtonBoxAttached10buttonRoleEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPlatformDialogHelper.ButtonRole)
  def setButtonRole(self, role: QPlatformDialogHelper.ButtonRole) -> None:
    """
    Calls Qt's 'void
    QQuickDialogButtonBoxAttached::setButtonRole(QPlatformDialogHelper::
    ButtonRole role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxattached.html#setButtonRole

    Parameters
    ----------

    role : QPlatformDialogHelper.ButtonRole
      Passed on as its number.
    """
    #  void QQuickDialogButtonBoxAttached::setButtonRole(
    #      QPlatformDialogHelper::ButtonRole role)
    self.uglySide.call(
        'ritual_ZN29QQuickDialogButtonBoxAttached13setButtonRoleEN21QPlatfo'
        'rmDialogHelper10ButtonRoleE',
        role.value,
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
    'QQuickDialogButtonBoxAttached::QQuickDialogButtonBoxAttached(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxattached.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickDialogButtonBoxAttached::QQuickDialogButtonBoxAttached(QObject
    #      *parent)
    self._noteCreation(QQuickDialogButtonBoxAttached, lambda: Rituals.call(
        'ritual_ZN29QQuickDialogButtonBoxAttachedC1EP7QObject',
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

  def buttonBoxChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBoxAttached::buttonBoxChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxattached.html
    """
    #  void QQuickDialogButtonBoxAttached::buttonBoxChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickDialogButtonBoxAttached16buttonBoxChangedEv',
    )

  def buttonRoleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDialogButtonBoxAttached::buttonRoleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxattached.html
    """
    #  void QQuickDialogButtonBoxAttached::buttonRoleChanged()
    self.uglySide.call(
        'ritual_ZN29QQuickDialogButtonBoxAttached17buttonRoleChangedEv',
    )

  def d_func(self) -> Optional[QQuickDialogButtonBoxAttachedPrivate]:
    """
    Calls Qt's 'QQuickDialogButtonBoxAttachedPrivate
    *QQuickDialogButtonBoxAttached::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdialogbuttonboxattached.html#d_func

    Returns
    -------

    Optional[QQuickDialogButtonBoxAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDialogButtonBoxAttachedPrivate
    #      *QQuickDialogButtonBoxAttached::d_func()
    address = self.uglySide.call(
        'ritual_ZN29QQuickDialogButtonBoxAttached6d_funcEv',
    )
    from . import QQuickDialogButtonBoxAttachedPrivate
    return QQuickDialogButtonBoxAttachedPrivate._cuteAt(address)
