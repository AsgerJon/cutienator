"""
QUndoView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qundoview.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QListView, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QIcon, QUndoGroup, QUndoStack
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIcon = WAIT['QIcon']
  QUndoGroup = WAIT['QUndoGroup']
  QUndoStack = WAIT['QUndoStack']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUndoView(QListView):
  """
  The cute side of Qt's QUndoView: a plain Python object standing in front of
  one C++ QUndoView.

  It is built on the cute 'QListView', as Qt's QUndoView is built on Qt's
  QListView, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QUndoView that has a ritual and that Python can call
  so far, 10 names in all: 'metaObject', 'tr', 'stack', 'group',
  'setEmptyLabel', 'emptyLabel', 'setCleanIcon', 'cleanIcon', 'setStack',
  'setGroup'. It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUndoView::~QUndoView()': the destructor: Python never removes a
    C++ QUndoView.

  What has no ritual
  ------------------

  8 of the 22 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 forbidden; 1 a template; 1 declared and nowhere to be found.

  What to expect
  --------------

  - The C++ QUndoView is created at the first use, not by 'QUndoView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QUndoView.
  - Qt tells when it has removed the C++ QUndoView. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QUndoView::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUndoView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QUndoView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUndoView'

  #  A C++ QUndoView Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QUndoView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QUndoView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QUndoView::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QUndoView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def stack(self) -> Optional[QUndoStack]:
    """
    Calls Qt's 'QUndoStack *QUndoView::stack() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#stack

    Returns
    -------

    Optional[QUndoStack]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUndoStack *QUndoView::stack() const
    address = self.uglySide.call('ritual_ZNK9QUndoView5stackEv')
    from ..QtGui import QUndoStack
    return QUndoStack._cuteAt(address)

  def group(self) -> Optional[QUndoGroup]:
    """
    Calls Qt's 'QUndoGroup *QUndoView::group() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#group

    Returns
    -------

    Optional[QUndoGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUndoGroup *QUndoView::group() const
    address = self.uglySide.call('ritual_ZNK9QUndoView5groupEv')
    from ..QtGui import QUndoGroup
    return QUndoGroup._cuteAt(address)

  def emptyLabel(self) -> str:
    """
    Calls Qt's 'QString QUndoView::emptyLabel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#emptyLabel

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUndoView::emptyLabel() const
    return self.uglySide.call('ritual_ZNK9QUndoView10emptyLabelEv')

  def cleanIcon(self) -> QIcon:
    """
    Calls Qt's 'QIcon QUndoView::cleanIcon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#cleanIcon

    Returns
    -------

    QIcon
      A new cute QIcon around the copy Qt gave back. Python owns it.
    """
    #  QIcon QUndoView::cleanIcon() const
    address = self.uglySide.call('ritual_ZNK9QUndoView9cleanIconEv')
    from ..QtGui import QIcon
    return QIcon._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setEmptyLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QUndoView::setEmptyLabel(const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#setEmptyLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QUndoView::setEmptyLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN9QUndoView13setEmptyLabelERK7QString', label,
    )

  @overload(QIcon)
  def setCleanIcon(self, icon: QIcon) -> None:
    """
    Calls Qt's 'void QUndoView::setCleanIcon(const QIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#setCleanIcon

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.
    """
    #  void QUndoView::setCleanIcon(const QIcon &icon)
    self.uglySide.call(
        'ritual_ZN9QUndoView12setCleanIconERK5QIcon', self._valueOf(icon),
    )

  @overload(QUndoStack)
  @overload(NoneType)
  def setStack(self, stack: Optional[QUndoStack]) -> None:
    """
    Calls Qt's 'void QUndoView::setStack(QUndoStack *stack)'.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#setStack

    Parameters
    ----------

    stack : Optional[QUndoStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUndoView::setStack(QUndoStack *stack)
    self.uglySide.call(
        'ritual_ZN9QUndoView8setStackEP10QUndoStack', self._addressOf(stack),
    )

  @overload(QUndoGroup)
  @overload(NoneType)
  def setGroup(self, group: Optional[QUndoGroup]) -> None:
    """
    Calls Qt's 'void QUndoView::setGroup(QUndoGroup *group)'.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#setGroup

    Parameters
    ----------

    group : Optional[QUndoGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUndoView::setGroup(QUndoGroup *group)
    self.uglySide.call(
        'ritual_ZN9QUndoView8setGroupEP10QUndoGroup', self._addressOf(group),
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
    Notes what was given, for Qt's 'QUndoView::QUndoView(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#QUndoView

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QUndoView::QUndoView(QWidget *parent)
    self._noteCreation(QUndoView, lambda: Rituals.call(
        'ritual_ZN9QUndoViewC1EP7QWidget', self._addressOf(parent),
    ))

  @overload(QUndoStack)
  @overload(QUndoStack, QWidget)
  @overload(QUndoStack, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      stack: Optional[QUndoStack],
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QUndoView::QUndoView(QUndoStack *stack,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#QUndoView

    Parameters
    ----------

    stack : Optional[QUndoStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QUndoView::QUndoView(QUndoStack *stack, QWidget *parent)
    self._noteCreation(QUndoView, lambda: Rituals.call(
        'ritual_ZN9QUndoViewC1EP10QUndoStackP7QWidget',
        self._addressOf(stack), self._addressOf(parent),
    ))

  @overload(QUndoGroup)
  @overload(QUndoGroup, QWidget)
  @overload(QUndoGroup, NoneType)
  def __init__(
      self,
      group: Optional[QUndoGroup],
      parent: Optional[QWidget] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QUndoView::QUndoView(QUndoGroup *group,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qundoview.html#QUndoView

    Parameters
    ----------

    group : Optional[QUndoGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QUndoView::QUndoView(QUndoGroup *group, QWidget *parent)
    self._noteCreation(QUndoView, lambda: Rituals.call(
        'ritual_ZN9QUndoViewC1EP10QUndoGroupP7QWidget',
        self._addressOf(group), self._addressOf(parent),
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
