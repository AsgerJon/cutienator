"""
QQuickFileDialogDelegatePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFileDialogDelegatePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQuickFileDialogDelegate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickFileDialogDelegate = WAIT['QQuickFileDialogDelegate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFileDialogDelegatePrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickFileDialogDelegatePrivate: a plain Python
  object standing in front of one C++ QQuickFileDialogDelegatePrivate.

  What exists
  -----------

  Every function of Qt's QQuickFileDialogDelegatePrivate that has a ritual
  and that Python can call so far, 7 names in all: 'q_func', 'get',
  'highlightFile', 'chooseFile', 'destroyTapHandler', 'handleLongPress',
  'acceptKeyClick'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickFileDialogDelegate
    *QQuickFileDialogDelegatePrivate::q_func() const': takes in Python what
    'QQuickFileDialogDelegate *QQuickFileDialogDelegatePrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 leans on 'vtable for
  QQuickFileDialogTapHandler', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickFileDialogDelegatePrivate is created at the first use, not
    by 'QQuickFileDialogDelegatePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFileDialogDelegatePrivate.
  - Each name of Qt's QQuickFileDialogDelegatePrivate that has no cute
    function yet, 'initTapHandler', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickFileDialogDelegate)
  @overload(NoneType)
  def get(
      delegate: Optional[QQuickFileDialogDelegate],
  ) -> Optional[QQuickFileDialogDelegatePrivate]:
    """
    Calls Qt's 'QQuickFileDialogDelegatePrivate
    *QQuickFileDialogDelegatePrivate::get(QQuickFileDialogDelegate
    *delegate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegateprivate.html#get

    Parameters
    ----------

    delegate : Optional[QQuickFileDialogDelegate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickFileDialogDelegatePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileDialogDelegatePrivate
    #      *QQuickFileDialogDelegatePrivate::get(QQuickFileDialogDelegate
    #      *delegate)
    address = Rituals.call(
        'ritual_ZN31QQuickFileDialogDelegatePrivate3getEP24QQuickFileDialog'
        'Delegate',
        CuteMixin._addressOf(delegate),
    )
    return QQuickFileDialogDelegatePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFileDialogDelegatePrivate'

  #  A C++ QQuickFileDialogDelegatePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickFileDialogDelegatePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Key)
  def acceptKeyClick(self, key: Qt.Key) -> bool:
    """
    Calls Qt's 'bool QQuickFileDialogDelegatePrivate::acceptKeyClick(Qt::Key
    key) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegateprivate.html

    Parameters
    ----------

    key : Qt.Key
      Passed on as its number.
    """
    #  bool QQuickFileDialogDelegatePrivate::acceptKeyClick(Qt::Key key)
    #      const
    ritual = (
        'ritual_ZNK31QQuickFileDialogDelegatePrivate14acceptKeyClickEN2Qt3K'
        'eyE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK31QQuickFileDialogDelegatePrivate14acceptKeyClickE'
          'N2Qt3KeyE')
    return self.uglySide.call(ritual, key.value)

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

  def q_func(self) -> Optional[QQuickFileDialogDelegate]:
    """
    Calls Qt's 'QQuickFileDialogDelegate
    *QQuickFileDialogDelegatePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegateprivate.html#q_func

    Returns
    -------

    Optional[QQuickFileDialogDelegate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickFileDialogDelegate *QQuickFileDialogDelegatePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN31QQuickFileDialogDelegatePrivate6q_funcEv',
    )
    from . import QQuickFileDialogDelegate
    return QQuickFileDialogDelegate._cuteAt(address)

  def highlightFile(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogDelegatePrivate::highlightFile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegateprivate.html#highlightFile
    """
    #  void QQuickFileDialogDelegatePrivate::highlightFile()
    self.uglySide.call(
        'ritual_ZN31QQuickFileDialogDelegatePrivate13highlightFileEv',
    )

  def chooseFile(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogDelegatePrivate::chooseFile()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegateprivate.html#chooseFile
    """
    #  void QQuickFileDialogDelegatePrivate::chooseFile()
    self.uglySide.call(
        'ritual_ZN31QQuickFileDialogDelegatePrivate10chooseFileEv',
    )

  def destroyTapHandler(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogDelegatePrivate::destroyTapHandler()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegateprivate.html
    """
    #  void QQuickFileDialogDelegatePrivate::destroyTapHandler()
    self.uglySide.call(
        'ritual_ZN31QQuickFileDialogDelegatePrivate17destroyTapHandlerEv',
    )

  def handleLongPress(self) -> None:
    """
    Calls Qt's 'void QQuickFileDialogDelegatePrivate::handleLongPress()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfiledialogdelegateprivate.html
    """
    #  void QQuickFileDialogDelegatePrivate::handleLongPress()
    self.uglySide.call(
        'ritual_ZN31QQuickFileDialogDelegatePrivate15handleLongPressEv',
    )

  @staticmethod
  def initTapHandler(*__, **_) -> Never:
    """
    Qt's 'void QQuickFileDialogDelegatePrivate::initTapHandler()': leans on
    'vtable for QQuickFileDialogTapHandler', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickFileDialogDelegatePrivate.initTapHandler' has no cute "
        "function yet. Qt's 'void "
        "QQuickFileDialogDelegatePrivate::initTapHandler()': leans on "
        "'vtable for QQuickFileDialogTapHandler', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")
