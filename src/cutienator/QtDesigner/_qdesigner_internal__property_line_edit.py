"""
qdesigner_internal::PropertyLineEdit binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/propertylineedit_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PropertyLineEdit to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtWidgets import QLineEdit

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QContextMenuEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class PropertyLineEdit(QLineEdit):
  """
  The cute side of Qt's qdesigner_internal::PropertyLineEdit: a plain Python
  object standing in front of one C++ qdesigner_internal::PropertyLineEdit.

  It is built on the cute 'QLineEdit', as Qt's
  qdesigner_internal::PropertyLineEdit is built on Qt's QLineEdit, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PropertyLineEdit that has a
  ritual and that Python can call so far, 7 names in all: 'metaObject',
  'setWantNewLine', 'wantNewLine', 'event', 'contextMenuEvent',
  'insertNewLine', 'insertText'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::PropertyLineEdit::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::PropertyLineEdit::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 2 not a gap; 1 leans on
  'qdesigner_internal; 1 leans on 'vtable for qdesigner_internal.

  What to expect
  --------------

  - The C++ qdesigner_internal::PropertyLineEdit is created at the first use,
    not by 'qdesigner_internal::PropertyLineEdit(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::PropertyLineEdit.
  - Qt tells when it has removed the C++
    qdesigner_internal::PropertyLineEdit. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  - Each name of Qt's qdesigner_internal::PropertyLineEdit that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'qdesigner_internal::PropertyLineEdit'

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
    *qdesigner_internal::PropertyLineEdit::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertylineedit.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::PropertyLineEdit::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal16PropertyLineEdit10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def wantNewLine(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::PropertyLineEdit::wantNewLine()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertylineedit.html
    """
    #  bool qdesigner_internal::PropertyLineEdit::wantNewLine() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal16PropertyLineEdit11wantNewLineEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setWantNewLine(self, nl: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertyLineEdit::setWantNewLine(bool nl)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertylineedit.html

    Parameters
    ----------

    nl : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::PropertyLineEdit::setWantNewLine(bool nl)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal16PropertyLineEdit14setWantNewLineEb',
        nl,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'qdesigner_internal::PropertyLineEdit::PropertyLineEdit(QWidget
    *parent)': leans on 'vtable for qdesigner_internal::PropertyLineEdit',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'qdesigner_internal.PropertyLineEdit.__init__' has no cute "
        "function yet. Qt's "
        "'qdesigner_internal::PropertyLineEdit::PropertyLineEdit(QWidget "
        "*parent)': leans on 'vtable for "
        "qdesigner_internal::PropertyLineEdit', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::PropertyLineEdit::event(QEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertylineedit.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::PropertyLineEdit::event(QEvent *e)
    ritual = 'ritual_ZN18qdesigner_internal16PropertyLineEdit5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal16PropertyLineEdit5eventEP6QEve'
          'nt')
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, event: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertyLineEdit::contextMenuEvent(QContextMenuEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertylineedit.html

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::PropertyLineEdit::contextMenuEvent(
    #      QContextMenuEvent *event)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal16PropertyLineEdit16contextMenuEventE'
        'P17QContextMenuEvent',
        self._addressOf(event),
    )

  def insertNewLine(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PropertyLineEdit::insertNewLine()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertylineedit.html
    """
    #  void qdesigner_internal::PropertyLineEdit::insertNewLine()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal16PropertyLineEdit13insertNewLineEv',
    )

  @overload(str)
  def insertText(self, a0: str) -> None:
    """
    Calls Qt's 'void qdesigner_internal::PropertyLineEdit::insertText(const
    QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertylineedit.html

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PropertyLineEdit::insertText(const QString
    #      &a0)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal16PropertyLineEdit10insertTextERK7QSt'
        'ring',
        a0,
    )
