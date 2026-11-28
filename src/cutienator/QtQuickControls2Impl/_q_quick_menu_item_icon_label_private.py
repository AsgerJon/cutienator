"""
QQuickMenuItemIconLabelPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickmenuitemiconlabel_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickMenuItemIconLabelPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickIconLabelPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QKeySequence
  from ..QtQuick import QQuickItem
  from . import QQuickMenuItemIconLabel
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMenuItemIconLabelPrivate(QQuickIconLabelPrivate):
  """
  The cute side of Qt's QQuickMenuItemIconLabelPrivate: a plain Python object
  standing in front of one C++ QQuickMenuItemIconLabelPrivate.

  It is built on the cute 'QQuickIconLabelPrivate', as Qt's
  QQuickMenuItemIconLabelPrivate is built on Qt's QQuickIconLabelPrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMenuItemIconLabelPrivate that has a ritual and
  that Python can call so far, 10 names in all: 'q_func', 'hasShortcut',
  'shortcut', 'createShortcutLabel', 'syncShortcutLabel',
  'updateImplicitSize', 'layout', 'itemDestroyed', 'textChange',
  'displayChange'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickMenuItemIconLabel
    *QQuickMenuItemIconLabelPrivate::q_func() const': takes in Python what
    'QQuickMenuItemIconLabel *QQuickMenuItemIconLabelPrivate::q_func()'
    takes.
  - Qt's 'QQuickMenuItemIconLabelPrivate::~QQuickMenuItemIconLabelPrivate()':
    the destructor: Python never removes a C++
    QQuickMenuItemIconLabelPrivate.

  What has no ritual
  ------------------

  3 of the 15 functions Qt declares: 3 leans on 'QQuickIconLabelPrivate.

  What to expect
  --------------

  - The C++ QQuickMenuItemIconLabelPrivate is created at the first use, not
    by 'QQuickMenuItemIconLabelPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMenuItemIconLabelPrivate.
  - Each name of Qt's QQuickMenuItemIconLabelPrivate that has no cute
    function yet, 'destroyShortcutLabel', 'updateOrSyncShortcutLabel',
    'updateShortcutLabel', holds a function that raises
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
  __qt_class__ = 'QQuickMenuItemIconLabelPrivate'

  #  A C++ QQuickMenuItemIconLabelPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMenuItemIconLabelPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasShortcut(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenuItemIconLabelPrivate::hasShortcut() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabelprivate.html#hasShortcut
    """
    #  bool QQuickMenuItemIconLabelPrivate::hasShortcut() const
    return self.uglySide.call(
        'ritual_ZNK30QQuickMenuItemIconLabelPrivate11hasShortcutEv',
    )

  def shortcut(self) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence QQuickMenuItemIconLabelPrivate::shortcut()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabelprivate.html#shortcut

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence QQuickMenuItemIconLabelPrivate::shortcut() const
    address = self.uglySide.call(
        'ritual_ZNK30QQuickMenuItemIconLabelPrivate8shortcutEv',
    )
    from ..QtGui import QKeySequence
    return QKeySequence._cuteOwning(address)

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

  def q_func(self) -> Optional[QQuickMenuItemIconLabel]:
    """
    Calls Qt's 'QQuickMenuItemIconLabel
    *QQuickMenuItemIconLabelPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabelprivate.html#q_func

    Returns
    -------

    Optional[QQuickMenuItemIconLabel]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuItemIconLabel *QQuickMenuItemIconLabelPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN30QQuickMenuItemIconLabelPrivate6q_funcEv',
    )
    from . import QQuickMenuItemIconLabel
    return QQuickMenuItemIconLabel._cuteAt(address)

  def createShortcutLabel(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenuItemIconLabelPrivate::createShortcutLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabelprivate.html
    """
    #  bool QQuickMenuItemIconLabelPrivate::createShortcutLabel()
    return self.uglySide.call(
        'ritual_ZN30QQuickMenuItemIconLabelPrivate19createShortcutLabelEv',
    )

  def syncShortcutLabel(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItemIconLabelPrivate::syncShortcutLabel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabelprivate.html
    """
    #  void QQuickMenuItemIconLabelPrivate::syncShortcutLabel()
    self.uglySide.call(
        'ritual_ZN30QQuickMenuItemIconLabelPrivate17syncShortcutLabelEv',
    )

  def updateImplicitSize(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItemIconLabelPrivate::updateImplicitSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabelprivate.html
    """
    #  void QQuickMenuItemIconLabelPrivate::updateImplicitSize()
    ritual = (
        'ritual_ZN30QQuickMenuItemIconLabelPrivate18updateImplicitSizeEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickMenuItemIconLabelPrivate18updateImplicitSiz'
          'eEv')
    self.uglySide.call(ritual)

  def layout(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItemIconLabelPrivate::layout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabelprivate.html#layout
    """
    #  void QQuickMenuItemIconLabelPrivate::layout()
    ritual = 'ritual_ZN30QQuickMenuItemIconLabelPrivate6layoutEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN30QQuickMenuItemIconLabelPrivate6layoutEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMenuItemIconLabelPrivate::itemDestroyed(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabelprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenuItemIconLabelPrivate::itemDestroyed(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN30QQuickMenuItemIconLabelPrivate13itemDestroyedEP10QQuick'
        'Item',
        self._addressOf(item),
    )

  def textChange(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItemIconLabelPrivate::textChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabelprivate.html#textChange
    """
    #  void QQuickMenuItemIconLabelPrivate::textChange()
    self.uglySide.call(
        'ritual_ZN30QQuickMenuItemIconLabelPrivate10textChangeEv',
    )

  def displayChange(self) -> None:
    """
    Calls Qt's 'void QQuickMenuItemIconLabelPrivate::displayChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenuitemiconlabelprivate.html#displayChange
    """
    #  void QQuickMenuItemIconLabelPrivate::displayChange()
    self.uglySide.call(
        'ritual_ZN30QQuickMenuItemIconLabelPrivate13displayChangeEv',
    )

  @staticmethod
  def destroyShortcutLabel(*__, **_) -> Never:
    """
    Qt's 'bool QQuickMenuItemIconLabelPrivate::destroyShortcutLabel()': leans
    on 'QQuickIconLabelPrivate::unwatchChanges(QQuickItem*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickMenuItemIconLabelPrivate.destroyShortcutLabel' has no cute "
        "function yet. Qt's 'bool "
        "QQuickMenuItemIconLabelPrivate::destroyShortcutLabel()': leans on "
        "'QQuickIconLabelPrivate::unwatchChanges(QQuickItem*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def updateOrSyncShortcutLabel(*__, **_) -> Never:
    """
    Qt's 'void QQuickMenuItemIconLabelPrivate::updateOrSyncShortcutLabel()':
    leans on 'QQuickIconLabelPrivate::unwatchChanges(QQuickItem*)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickMenuItemIconLabelPrivate.updateOrSyncShortcutLabel' has no "
        "cute function yet. Qt's 'void "
        "QQuickMenuItemIconLabelPrivate::updateOrSyncShortcutLabel()': "
        "leans on 'QQuickIconLabelPrivate::unwatchChanges(QQuickItem*)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def updateShortcutLabel(*__, **_) -> Never:
    """
    Qt's 'bool QQuickMenuItemIconLabelPrivate::updateShortcutLabel()': leans
    on 'QQuickIconLabelPrivate::unwatchChanges(QQuickItem*)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickMenuItemIconLabelPrivate.updateShortcutLabel' has no cute "
        "function yet. Qt's 'bool "
        "QQuickMenuItemIconLabelPrivate::updateShortcutLabel()': leans on "
        "'QQuickIconLabelPrivate::unwatchChanges(QQuickItem*)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")
