"""
QHelpContentItem binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpcontentitem.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QHelpContentItem(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHelpContentItem: a plain Python object standing in
  front of one C++ QHelpContentItem.

  What exists
  -----------

  Every function of Qt's QHelpContentItem that has a ritual and that Python
  can call so far, 7 names in all: 'child', 'childCount', 'title', 'url',
  'row', 'parent', 'childPosition'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHelpContentItem::~QHelpContentItem()': the destructor: Python
    never removes a C++ QHelpContentItem.

  What has no ritual
  ------------------

  4 of the 13 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QHelpContentItem is created at the first use, not by
    'QHelpContentItem(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHelpContentItem.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHelpContentItem'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def child(self, row: int) -> Optional[QHelpContentItem]:
    """
    Calls Qt's 'QHelpContentItem *QHelpContentItem::child(int row) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentitem.html#child

    Parameters
    ----------

    row : int
      Passed on as it is.

    Returns
    -------

    Optional[QHelpContentItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHelpContentItem *QHelpContentItem::child(int row) const
    address = self.uglySide.call('ritual_ZNK16QHelpContentItem5childEi', row)
    return QHelpContentItem._cuteAt(address)

  def childCount(self) -> int:
    """
    Calls Qt's 'int QHelpContentItem::childCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentitem.html#childCount
    """
    #  int QHelpContentItem::childCount() const
    return self.uglySide.call('ritual_ZNK16QHelpContentItem10childCountEv')

  def title(self) -> str:
    """
    Calls Qt's 'QString QHelpContentItem::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentitem.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QHelpContentItem::title() const
    return self.uglySide.call('ritual_ZNK16QHelpContentItem5titleEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QHelpContentItem::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentitem.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QHelpContentItem::url() const
    address = self.uglySide.call('ritual_ZNK16QHelpContentItem3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def row(self) -> int:
    """
    Calls Qt's 'int QHelpContentItem::row() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentitem.html#row
    """
    #  int QHelpContentItem::row() const
    return self.uglySide.call('ritual_ZNK16QHelpContentItem3rowEv')

  def parent(self) -> Optional[QHelpContentItem]:
    """
    Calls Qt's 'QHelpContentItem *QHelpContentItem::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpcontentitem.html#parent

    Returns
    -------

    Optional[QHelpContentItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QHelpContentItem *QHelpContentItem::parent() const
    address = self.uglySide.call('ritual_ZNK16QHelpContentItem6parentEv')
    return QHelpContentItem._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def childPosition(self, child: Optional[QHelpContentItem]) -> int:
    """
    Calls Qt's 'int QHelpContentItem::childPosition(QHelpContentItem *child)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentitem.html#childPosition

    Parameters
    ----------

    child : Optional[QHelpContentItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QHelpContentItem::childPosition(QHelpContentItem *child) const
    return self.uglySide.call(
        'ritual_ZNK16QHelpContentItem13childPositionEPS_',
        self._addressOf(child),
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

  @overload(str, QUrl)
  @overload(str, QUrl, THIS)
  @overload(str, QUrl, NoneType)
  def __init__(
      self,
      name: str,
      link: QUrl,
      parent: Optional[QHelpContentItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QHelpContentItem::QHelpContentItem(const
    QString &name, const QUrl &link, QHelpContentItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpcontentitem.html#QHelpContentItem

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    link : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[QHelpContentItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QHelpContentItem::QHelpContentItem(const QString &name, const QUrl
    #      &link, QHelpContentItem *parent)
    self._noteCreation(QHelpContentItem, lambda: Rituals.call(
        'ritual_ZN16QHelpContentItemC1ERK7QStringRK4QUrlPS_',
        name, self._valueOf(link), self._addressOf(parent),
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
