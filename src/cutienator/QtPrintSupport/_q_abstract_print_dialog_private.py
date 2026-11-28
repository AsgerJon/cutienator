"""
QAbstractPrintDialogPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPrintSupport/6.12.0/QtPrintSupport/private/qabstractprintdialog_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QAbstractPrintDialogPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList
from ..QtWidgets import QDialogPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtWidgets import QWidget
  from . import QAbstractPrintDialog, QPrinter
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPrinter = WAIT['QPrinter']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAbstractPrintDialogPrivate(QDialogPrivate):
  """
  The cute side of Qt's QAbstractPrintDialogPrivate: a plain Python object
  standing in front of one C++ QAbstractPrintDialogPrivate.

  It is built on the cute 'QDialogPrivate', as Qt's
  QAbstractPrintDialogPrivate is built on Qt's QDialogPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAbstractPrintDialogPrivate that has a ritual and
  that Python can call so far, 3 names in all: 'q_func', 'setTabs',
  'setPrinter'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QAbstractPrintDialog *QAbstractPrintDialogPrivate::q_func()
    const': takes in Python what 'QAbstractPrintDialog
    *QAbstractPrintDialogPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ QAbstractPrintDialogPrivate is created at the first use, not by
    'QAbstractPrintDialogPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAbstractPrintDialogPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAbstractPrintDialogPrivate'

  #  A C++ QAbstractPrintDialogPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAbstractPrintDialogPrivate'

  #  The functions Qt calls itself that QAbstractPrintDialogPrivate is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setTabs': (
          'void QAbstractPrintDialogPrivate::setTabs(const QList<QWidget '
          '*> &)',
      ),
  }

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

  @overload(QList[QWidget])
  def setTabs(self, a0: QList[QWidget]) -> None:
    """
    Calls Qt's 'void QAbstractPrintDialogPrivate::setTabs(const QList<QWidget
    *> &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprintdialogprivate.html#setTabs

    Parameters
    ----------

    a0 : QList[QWidget]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QAbstractPrintDialogPrivate::setTabs(const QList<QWidget *> &a0)
    self.uglySide.call(
        'ritual_ZN27QAbstractPrintDialogPrivate7setTabsERK5QListIP7QWidgetE',
        self._valueOf(a0),
    )

  @overload(QPrinter)
  @overload(NoneType)
  def setPrinter(self, newPrinter: Optional[QPrinter]) -> None:
    """
    Calls Qt's 'void QAbstractPrintDialogPrivate::setPrinter(QPrinter
    *newPrinter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprintdialogprivate.html#setPrinter

    Parameters
    ----------

    newPrinter : Optional[QPrinter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAbstractPrintDialogPrivate::setPrinter(QPrinter *newPrinter)
    self.uglySide.call(
        'ritual_ZN27QAbstractPrintDialogPrivate10setPrinterEP8QPrinter',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QAbstractPrintDialogPrivate::QAbstractPrintDialogPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprintdialogprivate.html
    """
    #  QAbstractPrintDialogPrivate::QAbstractPrintDialogPrivate()
    self._noteCreation(QAbstractPrintDialogPrivate, lambda: Rituals.call(
        'ritual_ZN27QAbstractPrintDialogPrivateC1Ev',
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

  def q_func(self) -> Optional[QAbstractPrintDialog]:
    """
    Calls Qt's 'QAbstractPrintDialog *QAbstractPrintDialogPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qabstractprintdialogprivate.html#q_func

    Returns
    -------

    Optional[QAbstractPrintDialog]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractPrintDialog *QAbstractPrintDialogPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QAbstractPrintDialogPrivate6q_funcEv',
    )
    from . import QAbstractPrintDialog
    return QAbstractPrintDialog._cuteAt(address)
