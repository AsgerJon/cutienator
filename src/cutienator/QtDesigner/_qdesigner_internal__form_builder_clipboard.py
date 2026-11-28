"""
qdesigner_internal::FormBuilderClipboard binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qsimpleresource_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::FormBuilderClipboard to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class FormBuilderClipboard(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's qdesigner_internal::FormBuilderClipboard: a plain
  Python object standing in front of one C++
  qdesigner_internal::FormBuilderClipboard.

  C++ hands a qdesigner_internal::FormBuilderClipboard around as a copy, so
  every C++ qdesigner_internal::FormBuilderClipboard behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::FormBuilderClipboard that has a
  ritual and that Python can call so far, 1 name in all: 'empty'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::FormBuilderClipboard::~FormBuilderClipboard()':
    the destructor: Python removes its C++
    qdesigner_internal::FormBuilderClipboard by it, and has no other use for
    it.

  What to expect
  --------------

  - The C++ qdesigner_internal::FormBuilderClipboard is created at the first
    use, not by 'qdesigner_internal::FormBuilderClipboard(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::FormBuilderClipboard back gives a
    copy the ritual made for Python, in a new cute
    qdesigner_internal::FormBuilderClipboard.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::FormBuilderClipboard'

  #  Qt's '~qdesigner_internal::FormBuilderClipboard()'. Naming it makes this
  #  a value class: Python owns every C++
  #  qdesigner_internal::FormBuilderClipboard behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18qdesigner_internal20FormBuilderClipboardD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def empty(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::FormBuilderClipboard::empty()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formbuilderclipboard.html#empty
    """
    #  bool qdesigner_internal::FormBuilderClipboard::empty() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal20FormBuilderClipboard5emptyEv',
    )

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::FormBuilderClipboard::FormBuilderClipboard()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formbuilderclipboard.html
    """
    #  qdesigner_internal::FormBuilderClipboard::FormBuilderClipboard()
    self._noteCreation(FormBuilderClipboard, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal20FormBuilderClipboardC1Ev',
    ))

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, w: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::FormBuilderClipboard::FormBuilderClipboard(QWidget
    *w)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-formbuilderclipboard.html

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::FormBuilderClipboard::FormBuilderClipboard(QWidget
    #      *w)
    self._noteCreation(FormBuilderClipboard, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal20FormBuilderClipboardC1EP7QWidget',
        self._addressOf(w),
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
