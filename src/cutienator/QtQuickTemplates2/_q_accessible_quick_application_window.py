"""
QAccessibleQuickApplicationWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qaccessiblequickapplicationwindow_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QAccessibleQuickApplicationWindow to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAccessible, QAccessibleAttributesInterface
from ..QtQuick import QAccessibleQuickWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QVariant
  from . import QQuickApplicationWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickApplicationWindow = WAIT['QQuickApplicationWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAccessibleQuickApplicationWindow(QAccessibleQuickWindow, QAccessibleAttributesInterface):
  """
  The cute side of Qt's QAccessibleQuickApplicationWindow: a plain Python
  object standing in front of one C++ QAccessibleQuickApplicationWindow.

  It is built on the cute 'QAccessibleQuickWindow', as Qt's
  QAccessibleQuickApplicationWindow is built on Qt's QAccessibleQuickWindow,
  and has everything that class has. It is built on the cute
  'QAccessibleAttributesInterface' as well, as Qt's
  QAccessibleQuickApplicationWindow is built on Qt's
  QAccessibleAttributesInterface too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QAccessibleQuickApplicationWindow that has a ritual
  and that Python can call so far, 2 names in all: 'attributeValue',
  'applicationWindow'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *QAccessibleQuickApplicationWindow::interface_cast(QAccessible::
    InterfaceType t)': gives 'void', which has no cute class yet.
  - Qt's 'QList<QAccessible::Attribute>
    QAccessibleQuickApplicationWindow::attributeKeys() const': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ QAccessibleQuickApplicationWindow is created at the first use,
    not by 'QAccessibleQuickApplicationWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAccessibleQuickApplicationWindow.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAccessibleQuickApplicationWindow'

  #  Qt's QAccessibleQuickApplicationWindow is built on more than one class.
  #  The part of a C++ QAccessibleQuickApplicationWindow that belongs to a
  #  class after the first begins somewhere inside the object, and the ritual
  #  named for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QAccessibleAttributesInterface':
          'ritual_cast_QAccessibleQuickApplicationWindow_QAccessibleAttributesInterface',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAccessible.Attribute)
  def attributeValue(self, key: QAccessible.Attribute) -> QVariant:
    """
    Calls Qt's 'QVariant
    QAccessibleQuickApplicationWindow::attributeValue(QAccessible::Attribute
    key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickapplicationwindow.html

    Parameters
    ----------

    key : QAccessible.Attribute
      Passed on as its number.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant
    #      QAccessibleQuickApplicationWindow::attributeValue(QAccessible::
    #      Attribute key) const
    ritual = (
        'ritual_ZNK33QAccessibleQuickApplicationWindow14attributeValueEN11Q'
        'Accessible9AttributeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK33QAccessibleQuickApplicationWindow14attributeValu'
          'eEN11QAccessible9AttributeE')
    address = self.uglySide.call(ritual, key.value)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def applicationWindow(self) -> Optional[QQuickApplicationWindow]:
    """
    Calls Qt's 'QQuickApplicationWindow
    *QAccessibleQuickApplicationWindow::applicationWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickapplicationwindow.html

    Returns
    -------

    Optional[QQuickApplicationWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickApplicationWindow
    #      *QAccessibleQuickApplicationWindow::applicationWindow() const
    address = self.uglySide.call(
        'ritual_ZNK33QAccessibleQuickApplicationWindow17applicationWindowEv',
    )
    from . import QQuickApplicationWindow
    return QQuickApplicationWindow._cuteAt(address)

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

  @overload(QQuickApplicationWindow)
  @overload(NoneType)
  def __init__(self, window: Optional[QQuickApplicationWindow]) -> None:
    """
    Notes what was given, for Qt's
    'QAccessibleQuickApplicationWindow::QAccessibleQuickApplicationWindow(
    QQuickApplicationWindow *window)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qaccessiblequickapplicationwindow.html

    Parameters
    ----------

    window : Optional[QQuickApplicationWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QAccessibleQuickApplicationWindow::
    #      QAccessibleQuickApplicationWindow(QQuickApplicationWindow *window)
    self._noteCreation(
        QAccessibleQuickApplicationWindow, lambda: Rituals.call(
            'ritual_ZN33QAccessibleQuickApplicationWindowC1EP23QQuickApplic'
            'ationWindow',
            self._addressOf(window),
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
