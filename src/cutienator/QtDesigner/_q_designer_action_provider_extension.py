"""
QDesignerActionProviderExtension binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/actionprovider_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QDesignerActionProviderExtension to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPoint, QRect
  from ..QtGui import QAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerActionProviderExtension(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDesignerActionProviderExtension: a plain Python
  object standing in front of one C++ QDesignerActionProviderExtension.

  What exists
  -----------

  Every function of Qt's QDesignerActionProviderExtension that has a ritual
  and that Python can call so far, 3 names in all: 'actionGeometry',
  'actionAt', 'adjustIndicator'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QDesignerActionProviderExtension::~QDesignerActionProviderExtension()':
    the destructor: Python never removes a C++
    QDesignerActionProviderExtension.

  What to expect
  --------------

  - The C++ QDesignerActionProviderExtension is created at the first use, not
    by 'QDesignerActionProviderExtension(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerActionProviderExtension.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerActionProviderExtension'

  #  A C++ QDesignerActionProviderExtension Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerActionProviderExtension'

  #  The functions Qt calls itself that QDesignerActionProviderExtension is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'actionGeometry': (
          ('_ZNK32QDesignerActionProviderExtension14actionGeometryEP7QActio'
           'n',
           ('address', 'value', 'QtCore:QRect'),
           (
               ('address', 'address', 'QtGui:QAction'),
           )),
      ),
      'actionAt': (
          ('_ZNK32QDesignerActionProviderExtension8actionAtERK6QPoint',
           ('address', 'address', 'QtGui:QAction'),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
      'adjustIndicator': (
          ('_ZN32QDesignerActionProviderExtension15adjustIndicatorERK6QPoin'
           't',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAction)
  @overload(NoneType)
  def actionGeometry(self, action: Optional[QAction]) -> QRect:
    """
    Calls Qt's 'QRect
    QDesignerActionProviderExtension::actionGeometry(QAction *action) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneractionproviderextension.html

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QDesignerActionProviderExtension::actionGeometry(QAction
    #      *action) const
    address = self.uglySide.call(
        'ritual_ZNK32QDesignerActionProviderExtension14actionGeometryEP7QAc'
        'tion',
        self._addressOf(action),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def actionAt(self, pos: QPoint) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QDesignerActionProviderExtension::actionAt(const
    QPoint &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneractionproviderextension.html#actionAt

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QDesignerActionProviderExtension::actionAt(const QPoint &pos)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QDesignerActionProviderExtension8actionAtERK6QPoint',
        self._valueOf(pos),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

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

  @overload(QPoint)
  def adjustIndicator(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void QDesignerActionProviderExtension::adjustIndicator(const
    QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigneractionproviderextension.html

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QDesignerActionProviderExtension::adjustIndicator(const QPoint
    #      &pos)
    self.uglySide.call(
        'ritual_ZN32QDesignerActionProviderExtension15adjustIndicatorERK6QP'
        'oint',
        self._valueOf(pos),
    )
