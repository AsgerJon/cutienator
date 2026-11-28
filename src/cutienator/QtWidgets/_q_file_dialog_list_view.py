"""
QFileDialogListView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFileDialogListView to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QListView, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QSize
  from ..QtGui import QKeyEvent
  from . import QFileDialogPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QFileDialogPrivate = WAIT['QFileDialogPrivate']
  QKeyEvent = WAIT['QKeyEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFileDialogListView(QListView):
  """
  The cute side of Qt's QFileDialogListView: a plain Python object standing
  in front of one C++ QFileDialogListView.

  It is built on the cute 'QListView', as Qt's QFileDialogListView is built
  on Qt's QListView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileDialogListView that has a ritual and that
  Python can call so far, 3 names in all: 'setFileDialogPrivate', 'sizeHint',
  'keyPressEvent'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QFileDialogListView is created at the first use, not by
    'QFileDialogListView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileDialogListView.
  - Qt tells when it has removed the C++ QFileDialogListView. Every call on
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
  __qt_class__ = 'QFileDialogListView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QFileDialogListView::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledialoglistview.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QFileDialogListView::sizeHint() const
    ritual = 'ritual_ZNK19QFileDialogListView8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QFileDialogListView8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFileDialogPrivate)
  @overload(NoneType)
  def setFileDialogPrivate(
      self,
      d_pointer: Optional[QFileDialogPrivate],
  ) -> None:
    """
    Calls Qt's 'void
    QFileDialogListView::setFileDialogPrivate(QFileDialogPrivate
    *d_pointer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialoglistview.html#setFileDialogPrivate

    Parameters
    ----------

    d_pointer : Optional[QFileDialogPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileDialogListView::setFileDialogPrivate(QFileDialogPrivate
    #      *d_pointer)
    self.uglySide.call(
        'ritual_ZN19QFileDialogListView20setFileDialogPrivateEP18QFileDialo'
        'gPrivate',
        self._addressOf(d_pointer),
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QFileDialogListView::QFileDialogListView(QWidget *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialoglistview.html#QFileDialogListView

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QFileDialogListView::QFileDialogListView(QWidget *parent)
    self._noteCreation(QFileDialogListView, lambda: Rituals.call(
        'ritual_ZN19QFileDialogListViewC1EP7QWidget',
        self._addressOf(parent),
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

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, e: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QFileDialogListView::keyPressEvent(QKeyEvent *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfiledialoglistview.html#keyPressEvent

    Parameters
    ----------

    e : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFileDialogListView::keyPressEvent(QKeyEvent *e)
    ritual = 'ritual_ZN19QFileDialogListView13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QFileDialogListView13keyPressEventEP9QKeyEvent')
    self.uglySide.call(ritual, self._addressOf(e))
