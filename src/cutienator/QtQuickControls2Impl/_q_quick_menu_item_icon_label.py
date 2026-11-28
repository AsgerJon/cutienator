"""
QQuickMenuItemIconLabel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickmenuitemiconlabel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMenuItemIconLabel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from . import QQuickIconLabel

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickMenuItemIconLabelPrivate
  from ..QtQuickTemplates2 import QQuickMenuItem


class QQuickMenuItemIconLabel(QQuickIconLabel):
  """
  The cute side of Qt's QQuickMenuItemIconLabel: a plain Python object
  standing in front of one C++ QQuickMenuItemIconLabel.

  It is built on the cute 'QQuickIconLabel', as Qt's QQuickMenuItemIconLabel
  is built on Qt's QQuickIconLabel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMenuItemIconLabel that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'menuItem',
  'menuItemChanged', 'componentComplete', 'd_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMenuItemIconLabel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickMenuItemIconLabel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickMenuItemIconLabel::~QQuickMenuItemIconLabel()': the
    destructor: Python never removes a C++ QQuickMenuItemIconLabel.
  - Qt's 'const QQuickMenuItemIconLabelPrivate
    *QQuickMenuItemIconLabel::d_func() const': takes in Python what
    'QQuickMenuItemIconLabelPrivate *QQuickMenuItemIconLabel::d_func()'
    takes.

  What has no ritual
  ------------------

  7 of the 16 functions Qt declares: 3 leans on 'QQuickMenuItemIconLabel; 2
  not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickMenuItemIconLabel is created at the first use, not by
    'QQuickMenuItemIconLabel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMenuItemIconLabel.
  - Qt tells when it has removed the C++ QQuickMenuItemIconLabel. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickMenuItemIconLabel that has no cute function yet,
    '__init__', 'setMenuItem', holds a function that raises
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
  __qt_class__ = 'QQuickMenuItemIconLabel'

  #  A C++ QQuickMenuItemIconLabel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMenuItemIconLabel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMenuItemIconLabel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMenuItemIconLabel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickMenuItemIconLabel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def menuItem(self) -> Optional[QQuickMenuItem]:
    """
    Calls Qt's 'QQuickMenuItem *QQuickMenuItemIconLabel::menuItem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabel.html#menuItem

    Returns
    -------

    Optional[QQuickMenuItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuItem *QQuickMenuItemIconLabel::menuItem() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuickMenuItemIconLabel8menuItemEv',
    )
    from ..QtQuickTemplates2 import QQuickMenuItem
    return QQuickMenuItem._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickMenuItemIconLabel::QQuickMenuItemIconLabel(QQuickItem
    *parent)': leans on
    'QQuickMenuItemIconLabel::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMenuItemIconLabel.__init__' has no cute function yet. Qt's "
        "'QQuickMenuItemIconLabel::QQuickMenuItemIconLabel(QQuickItem "
        "*parent)': leans on "
        "'QQuickMenuItemIconLabel::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def menuItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItemIconLabel::menuItemChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabel.html#menuItemChanged
    """
    #  void QQuickMenuItemIconLabel::menuItemChanged()
    self.uglySide.call(
        'ritual_ZN23QQuickMenuItemIconLabel15menuItemChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItemIconLabel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabel.html#componentComplete
    """
    #  void QQuickMenuItemIconLabel::componentComplete()
    ritual = 'ritual_ZN23QQuickMenuItemIconLabel17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQuickMenuItemIconLabel17componentCompleteEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQuickMenuItemIconLabelPrivate]:
    """
    Calls Qt's 'QQuickMenuItemIconLabelPrivate
    *QQuickMenuItemIconLabel::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabel.html#d_func

    Returns
    -------

    Optional[QQuickMenuItemIconLabelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuItemIconLabelPrivate *QQuickMenuItemIconLabel::d_func()
    address = self.uglySide.call(
        'ritual_ZN23QQuickMenuItemIconLabel6d_funcEv',
    )
    from . import QQuickMenuItemIconLabelPrivate
    return QQuickMenuItemIconLabelPrivate._cuteAt(address)

  @staticmethod
  def setMenuItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickMenuItemIconLabel::setMenuItem(QQuickMenuItem
    *menuItem)': leans on 'QQuickMenuItemIconLabel::menuItemChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMenuItemIconLabel.setMenuItem' has no cute function yet. "
        "Qt's 'void QQuickMenuItemIconLabel::setMenuItem(QQuickMenuItem "
        "*menuItem)': leans on "
        "'QQuickMenuItemIconLabel::menuItemChanged()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")
