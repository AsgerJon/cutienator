"""
QPageSetupDialogPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/6.12.0/QtPrintSupport/private/qpagesetupdialog_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPageSetupDialogPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtWidgets import QDialogPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPageSetupDialog, QPrinter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPrinter = WAIT['QPrinter']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPageSetupDialogPrivate(QDialogPrivate):
  """
  The cute side of Qt's QPageSetupDialogPrivate: a plain Python object
  standing in front of one C++ QPageSetupDialogPrivate.

  It is built on the cute 'QDialogPrivate', as Qt's QPageSetupDialogPrivate
  is built on Qt's QDialogPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPageSetupDialogPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'setPrinter'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPageSetupDialog *QPageSetupDialogPrivate::q_func() const':
    takes in Python what 'QPageSetupDialog
    *QPageSetupDialogPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QPageSetupDialogPrivate is created at the first use, not by
    'QPageSetupDialogPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPageSetupDialogPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPageSetupDialogPrivate'

  #  A C++ QPageSetupDialogPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPageSetupDialogPrivate'

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

  @overload(QPrinter)
  @overload(NoneType)
  def setPrinter(self, newPrinter: Optional[QPrinter]) -> None:
    """
    Calls Qt's 'void QPageSetupDialogPrivate::setPrinter(QPrinter
    *newPrinter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagesetupdialogprivate.html#setPrinter

    Parameters
    ----------

    newPrinter : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPageSetupDialogPrivate::setPrinter(QPrinter *newPrinter)
    self.uglySide.call(
        'ritual_ZN23QPageSetupDialogPrivate10setPrinterEP8QPrinter',
        self._addressOf(newPrinter),
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

  @overload(QPrinter)
  @overload(NoneType)
  def __init__(self, printer: Optional[QPrinter]) -> None:
    """
    Notes what was given, for Qt's
    'QPageSetupDialogPrivate::QPageSetupDialogPrivate(QPrinter *printer)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagesetupdialogprivate.html

    Parameters
    ----------

    printer : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPageSetupDialogPrivate::QPageSetupDialogPrivate(QPrinter *printer)
    self._noteCreation(QPageSetupDialogPrivate, lambda: Rituals.call(
        'ritual_ZN23QPageSetupDialogPrivateC1EP8QPrinter',
        self._addressOf(printer),
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

  def q_func(self) -> Optional[QPageSetupDialog]:
    """
    Calls Qt's 'QPageSetupDialog *QPageSetupDialogPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpagesetupdialogprivate.html#q_func

    Returns
    -------

    Optional[QPageSetupDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPageSetupDialog *QPageSetupDialogPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QPageSetupDialogPrivate6q_funcEv',
    )
    from . import QPageSetupDialog
    return QPageSetupDialog._cuteAt(address)
