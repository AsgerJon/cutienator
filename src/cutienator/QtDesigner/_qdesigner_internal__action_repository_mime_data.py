"""
qdesigner_internal::ActionRepositoryMimeData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/actionrepository_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ActionRepositoryMimeData to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QMimeData, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QAction, QDragMoveEvent, QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QDragMoveEvent = WAIT['QDragMoveEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ActionRepositoryMimeData(QMimeData):
  """
  The cute side of Qt's qdesigner_internal::ActionRepositoryMimeData: a plain
  Python object standing in front of one C++
  qdesigner_internal::ActionRepositoryMimeData.

  It is built on the cute 'QMimeData', as Qt's
  qdesigner_internal::ActionRepositoryMimeData is built on Qt's QMimeData,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ActionRepositoryMimeData that
  has a ritual and that Python can call so far, 6 names in all: 'metaObject',
  'tr', 'actionList', 'formats', 'actionDragPixmap', 'accept'. It can be made
  from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *qdesigner_internal::ActionRepositoryMimeData::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::ActionRepositoryMimeData::qt_metacall(QMetaObject::
    Call a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::ActionRepositoryMimeData is created at the
    first use, not by 'qdesigner_internal::ActionRepositoryMimeData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::ActionRepositoryMimeData.
  - Qt tells when it has removed the C++
    qdesigner_internal::ActionRepositoryMimeData. Every call on the cute
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
    Calls Qt's 'QString
    qdesigner_internal::ActionRepositoryMimeData::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionrepositorymimedata.html

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
    #  QString qdesigner_internal::ActionRepositoryMimeData::tr(const char
    #      *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal24ActionRepositoryMimeData2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QAction)
  @overload(NoneType)
  def actionDragPixmap(action: Optional[QAction]) -> QPixmap:
    """
    Calls Qt's 'QPixmap
    qdesigner_internal::ActionRepositoryMimeData::actionDragPixmap(const
    QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionrepositorymimedata.html

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap
    #      qdesigner_internal::ActionRepositoryMimeData::actionDragPixmap(
    #      const QAction *action)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal24ActionRepositoryMimeData16actionDra'
        'gPixmapEPK7QAction',
        CuteMixin._addressOf(action),
    )
    from ..QtGui import QPixmap
    return QPixmap._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ActionRepositoryMimeData'

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
    *qdesigner_internal::ActionRepositoryMimeData::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionrepositorymimedata.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::ActionRepositoryMimeData::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal24ActionRepositoryMimeData10metaObje'
        'ctEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def actionList(self) -> QList[QAction]:
    """
    Calls Qt's 'const ActionList
    &qdesigner_internal::ActionRepositoryMimeData::actionList() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionrepositorymimedata.html

    Returns
    -------

    QList[QAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  const ActionList
    #      &qdesigner_internal::ActionRepositoryMimeData::actionList() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal24ActionRepositoryMimeData10actionLi'
        'stEv',
    )
    from ..QtGui import QAction
    return QList[QAction]._cuteOwning(address)

  def formats(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::ActionRepositoryMimeData::formats() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionrepositorymimedata.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList qdesigner_internal::ActionRepositoryMimeData::formats()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal24ActionRepositoryMimeData7formatsEv',
    )
    return QStringList._cuteOwning(address)

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

  @overload(QList[QAction], Qt.DropAction)
  def __init__(self, a0: QList[QAction], dropAction: Qt.DropAction) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ActionRepositoryMimeData::ActionRepositoryMimeData(
    const ActionList &a0, Qt::DropAction dropAction)', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionrepositorymimedata.html

    Parameters
    ----------

    a0 : QList[QAction]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    dropAction : Qt.DropAction
      Passed on as its number.
    """
    #  qdesigner_internal::ActionRepositoryMimeData::
    #      ActionRepositoryMimeData(const ActionList &a0, Qt::DropAction
    #      dropAction)
    self._noteCreation(ActionRepositoryMimeData, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal24ActionRepositoryMimeDataC1ERK5QList'
        'IP7QActionEN2Qt10DropActionE',
        self._valueOf(a0), dropAction.value,
    ))

  @overload(QAction, Qt.DropAction)
  @overload(NoneType, Qt.DropAction)
  def __init__(
      self,
      a0: Optional[QAction],
      dropAction: Qt.DropAction,
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ActionRepositoryMimeData::ActionRepositoryMimeData(
    QAction *a0, Qt::DropAction dropAction)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionrepositorymimedata.html

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dropAction : Qt.DropAction
      Passed on as its number.
    """
    #  qdesigner_internal::ActionRepositoryMimeData::
    #      ActionRepositoryMimeData(QAction *a0, Qt::DropAction dropAction)
    self._noteCreation(ActionRepositoryMimeData, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal24ActionRepositoryMimeDataC1EP7QActio'
        'nN2Qt10DropActionE',
        self._addressOf(a0), dropAction.value,
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

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def accept(self, event: Optional[QDragMoveEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ActionRepositoryMimeData::accept(QDragMoveEvent
    *event) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-actionrepositorymimedata.html

    Parameters
    ----------

    event : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ActionRepositoryMimeData::accept(
    #      QDragMoveEvent *event) const
    self.uglySide.call(
        'ritual_ZNK18qdesigner_internal24ActionRepositoryMimeData6acceptEP1'
        '4QDragMoveEvent',
        self._addressOf(event),
    )
