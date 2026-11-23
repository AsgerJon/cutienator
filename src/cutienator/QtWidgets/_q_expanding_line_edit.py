"""
QExpandingLineEdit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qitemeditorfactory_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QExpandingLineEdit to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QLineEdit

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QExpandingLineEdit(QLineEdit):
  """
  The cute side of Qt's QExpandingLineEdit: a plain Python object standing in
  front of one C++ QExpandingLineEdit.

  It is built on the cute 'QLineEdit', as Qt's QExpandingLineEdit is built on
  Qt's QLineEdit, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QExpandingLineEdit that has a ritual and that Python
  can call so far, 5 names in all: 'metaObject', 'setWidgetOwnsGeometry',
  'changeEvent', 'resizeToContents', 'updateMinimumWidth'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has no ritual
  ------------------

  6 of the 11 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 1 a template; 1 declared and nowhere to be found; 1 leans on
  'QExpandingLineEdit; 1 leans on 'vtable for QExpandingLineEdit', which Qt's
  library does not offer and Qt's source has no code for that could be taken.

  What to expect
  --------------

  - The C++ QExpandingLineEdit is created at the first use, not by
    'QExpandingLineEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QExpandingLineEdit.
  - Qt tells when it has removed the C++ QExpandingLineEdit. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QExpandingLineEdit'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QExpandingLineEdit::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qexpandinglineedit.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QExpandingLineEdit::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QExpandingLineEdit10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setWidgetOwnsGeometry(self, value: bool) -> None:
    """
    Calls Qt's 'void QExpandingLineEdit::setWidgetOwnsGeometry(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qexpandinglineedit.html#setWidgetOwnsGeometry

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QExpandingLineEdit::setWidgetOwnsGeometry(bool value)
    self.uglySide.call(
        'ritual_ZN18QExpandingLineEdit21setWidgetOwnsGeometryEb', value,
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

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, e: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QExpandingLineEdit::changeEvent(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qexpandinglineedit.html#changeEvent

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QExpandingLineEdit::changeEvent(QEvent *e)
    ritual = 'ritual_ZN18QExpandingLineEdit11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QExpandingLineEdit11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  def resizeToContents(self) -> None:
    """
    Calls Qt's 'void QExpandingLineEdit::resizeToContents()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qexpandinglineedit.html#resizeToContents
    """
    #  void QExpandingLineEdit::resizeToContents()
    self.uglySide.call('ritual_ZN18QExpandingLineEdit16resizeToContentsEv')

  def updateMinimumWidth(self) -> None:
    """
    Calls Qt's 'void QExpandingLineEdit::updateMinimumWidth()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qexpandinglineedit.html#updateMinimumWidth
    """
    #  void QExpandingLineEdit::updateMinimumWidth()
    self.uglySide.call('ritual_ZN18QExpandingLineEdit18updateMinimumWidthEv')
