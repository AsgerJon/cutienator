"""
QQuickHeaderViewBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickheaderview_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickHeaderViewBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from ..QtQuick import QQuickItem, QQuickTableView

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickHeaderViewBasePrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickHeaderViewBase(QQuickTableView):
  """
  The cute side of Qt's QQuickHeaderViewBase: a plain Python object standing
  in front of one C++ QQuickHeaderViewBase.

  It is built on the cute 'QQuickTableView', as Qt's QQuickHeaderViewBase is
  built on Qt's QQuickTableView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickHeaderViewBase that has a ritual and that
  Python can call so far, 6 names in all: 'metaObject', 'tr', 'd_func',
  'textRole', 'setTextRole', 'textRoleChanged'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickHeaderViewBase::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickHeaderViewBase::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickHeaderViewBasePrivate *QQuickHeaderViewBase::d_func()
    const': takes in Python what 'QQuickHeaderViewBasePrivate
    *QQuickHeaderViewBase::d_func()' takes.
  - Qt's 'QQuickHeaderViewBase::~QQuickHeaderViewBase()': the destructor:
    Python never removes a C++ QQuickHeaderViewBase.
  - Qt's
    'QQuickHeaderViewBase::QQuickHeaderViewBase(QQuickHeaderViewBasePrivate
    &dd, QQuickItem *parent)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickHeaderViewBase is created at the first use, not by
    'QQuickHeaderViewBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickHeaderViewBase.
  - Qt tells when it has removed the C++ QQuickHeaderViewBase. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickHeaderViewBase::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickheaderviewbase.html#tr

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
    #  QString QQuickHeaderViewBase::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickHeaderViewBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickHeaderViewBase'

  #  A C++ QQuickHeaderViewBase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickHeaderViewBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickHeaderViewBase::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickHeaderViewBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickHeaderViewBase10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textRole(self) -> str:
    """
    Calls Qt's 'QString QQuickHeaderViewBase::textRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickheaderviewbase.html#textRole

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickHeaderViewBase::textRole() const
    return self.uglySide.call('ritual_ZNK20QQuickHeaderViewBase8textRoleEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTextRole(self, role: str) -> None:
    """
    Calls Qt's 'void QQuickHeaderViewBase::setTextRole(const QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbase.html#setTextRole

    Parameters
    ----------

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickHeaderViewBase::setTextRole(const QString &role)
    self.uglySide.call(
        'ritual_ZN20QQuickHeaderViewBase11setTextRoleERK7QString', role,
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

  @overload(Qt.Orientation)
  @overload(Qt.Orientation, QQuickItem)
  @overload(Qt.Orientation, NoneType)
  def __init__(
      self,
      orient: Qt.Orientation,
      parent: Optional[QQuickItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickHeaderViewBase::QQuickHeaderViewBase(Qt::Orientation orient,
    QQuickItem *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbase.html#QQuickHeaderViewBase

    Parameters
    ----------

    orient : Qt.Orientation
      Passed on as its number.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickHeaderViewBase::QQuickHeaderViewBase(Qt::Orientation orient,
    #      QQuickItem *parent)
    self._noteCreation(QQuickHeaderViewBase, lambda: Rituals.call(
        'ritual_ZN20QQuickHeaderViewBaseC1EN2Qt11OrientationEP10QQuickItem',
        orient.value, self._addressOf(parent),
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

  def d_func(self) -> Optional[QQuickHeaderViewBasePrivate]:
    """
    Calls Qt's 'QQuickHeaderViewBasePrivate *QQuickHeaderViewBase::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickheaderviewbase.html#d_func

    Returns
    -------

    Optional[QQuickHeaderViewBasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickHeaderViewBasePrivate *QQuickHeaderViewBase::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickHeaderViewBase6d_funcEv')
    from . import QQuickHeaderViewBasePrivate
    return QQuickHeaderViewBasePrivate._cuteAt(address)

  def textRoleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickHeaderViewBase::textRoleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickheaderviewbase.html#textRoleChanged
    """
    #  void QQuickHeaderViewBase::textRoleChanged()
    self.uglySide.call('ritual_ZN20QQuickHeaderViewBase15textRoleChangedEv')
