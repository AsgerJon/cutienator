"""
QPlaceSearchResult binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacesearchresult.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QPlaceIcon, QPlaceSearchResultPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlaceIcon = WAIT['QPlaceIcon']
  QPlaceSearchResultPrivate = WAIT['QPlaceSearchResultPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceSearchResult(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaceSearchResult: a plain Python object standing in
  front of one C++ QPlaceSearchResult.

  C++ hands a QPlaceSearchResult around as a copy, so every C++
  QPlaceSearchResult behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceSearchResult that has a ritual and that Python
  can call so far, 8 names in all: '__eq__', '__ne__', 'type', 'title',
  'setTitle', 'icon', 'setIcon', 'd_func'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceSearchResult::~QPlaceSearchResult()': the destructor: Python
    removes its C++ QPlaceSearchResult by it, and has no other use for it.
  - Qt's 'QPlaceSearchResult &QPlaceSearchResult::operator=(const
    QPlaceSearchResult &other)': assignment: Python binds a name and has no
    operator for it.

  What has no ritual
  ------------------

  1 of the 14 functions Qt declares: 1 leans on
  'QSharedDataPointer<QPlaceSearchResultPrivate>.

  What to expect
  --------------

  - The C++ QPlaceSearchResult is created at the first use, not by
    'QPlaceSearchResult(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceSearchResult back gives a copy the ritual made
    for Python, in a new cute QPlaceSearchResult.
  """

  #  The enums Qt writes inside QPlaceSearchResult, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class SearchResultType(CuteNum):
    """
    The enum 'QPlaceSearchResult::SearchResultType' of Qt, with the 3 names
    Qt gives in it.
    """

    UnknownSearchResult = Kee[int](0)
    PlaceResult = Kee[int](1)
    ProposedSearchResult = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceSearchResult'

  #  Qt's '~QPlaceSearchResult()'. Naming it makes this a value class: Python
  #  owns every C++ QPlaceSearchResult behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QPlaceSearchResultD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> SearchResultType:
    """
    Calls Qt's 'SearchResultType QPlaceSearchResult::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchresult.html#type

    Returns
    -------

    SearchResultType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'SearchResultType(number)'
      gives.
    """
    #  SearchResultType QPlaceSearchResult::type() const
    return QPlaceSearchResult.SearchResultType(self.uglySide.call(
        'ritual_ZNK18QPlaceSearchResult4typeEv',
    ))

  def title(self) -> str:
    """
    Calls Qt's 'QString QPlaceSearchResult::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchresult.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceSearchResult::title() const
    return self.uglySide.call('ritual_ZNK18QPlaceSearchResult5titleEv')

  def icon(self) -> QPlaceIcon:
    """
    Calls Qt's 'QPlaceIcon QPlaceSearchResult::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchresult.html#icon

    Returns
    -------

    QPlaceIcon
      A new cute QPlaceIcon around the copy Qt gave back. Python owns it.
    """
    #  QPlaceIcon QPlaceSearchResult::icon() const
    address = self.uglySide.call('ritual_ZNK18QPlaceSearchResult4iconEv')
    from . import QPlaceIcon
    return QPlaceIcon._cuteOwning(address)

  def d_func(self) -> Optional[QPlaceSearchResultPrivate]:
    """
    Calls Qt's 'const QPlaceSearchResultPrivate *QPlaceSearchResult::d_func()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchresult.html#d_func

    Returns
    -------

    Optional[QPlaceSearchResultPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPlaceSearchResultPrivate *QPlaceSearchResult::d_func() const
    address = self.uglySide.call('ritual_ZNK18QPlaceSearchResult6d_funcEv')
    from . import QPlaceSearchResultPrivate
    return QPlaceSearchResultPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QPlaceSearchResult::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchresult.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceSearchResult::setTitle(const QString &title)
    self.uglySide.call(
        'ritual_ZN18QPlaceSearchResult8setTitleERK7QString', title,
    )

  @overload(QPlaceIcon)
  def setIcon(self, icon: QPlaceIcon) -> None:
    """
    Calls Qt's 'void QPlaceSearchResult::setIcon(const QPlaceIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchresult.html#setIcon

    Parameters
    ----------

    icon : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.
    """
    #  void QPlaceSearchResult::setIcon(const QPlaceIcon &icon)
    self.uglySide.call(
        'ritual_ZN18QPlaceSearchResult7setIconERK10QPlaceIcon',
        self._valueOf(icon),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QPlaceSearchResult) -> bool:
    """
    Calls Qt's 'bool QPlaceSearchResult::operator==(const QPlaceSearchResult
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchresult.html#operator==

    Parameters
    ----------

    other : QPlaceSearchResult
      Passed on as a value: Qt reads the C++ QPlaceSearchResult, which stays
      Python's own.
    """
    #  bool QPlaceSearchResult::operator==(const QPlaceSearchResult &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QPlaceSearchResulteqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QPlaceSearchResult) -> bool:
    """
    Calls Qt's 'bool QPlaceSearchResult::operator!=(const QPlaceSearchResult
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchresult.html#operator!=

    Parameters
    ----------

    other : QPlaceSearchResult
      Passed on as a value: Qt reads the C++ QPlaceSearchResult, which stays
      Python's own.
    """
    #  bool QPlaceSearchResult::operator!=(const QPlaceSearchResult &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QPlaceSearchResultneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceSearchResult::QPlaceSearchResult()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchresult.html#QPlaceSearchResult
    """
    #  QPlaceSearchResult::QPlaceSearchResult()
    self._noteCreation(QPlaceSearchResult, lambda: Rituals.call(
        'ritual_ZN18QPlaceSearchResultC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPlaceSearchResult) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceSearchResult::QPlaceSearchResult(const QPlaceSearchResult
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchresult.html#QPlaceSearchResult

    Parameters
    ----------

    other : QPlaceSearchResult
      Passed on as a value: Qt reads the C++ QPlaceSearchResult, which stays
      Python's own.
    """
    #  QPlaceSearchResult::QPlaceSearchResult(const QPlaceSearchResult
    #      &other)
    self._noteCreation(QPlaceSearchResult, lambda: Rituals.call(
        'ritual_ZN18QPlaceSearchResultC1ERKS_', self._valueOf(other),
    ))

  @overload(QPlaceSearchResultPrivate)
  @overload(NoneType)
  def __init__(self, d: Optional[QPlaceSearchResultPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceSearchResult::QPlaceSearchResult(QPlaceSearchResultPrivate *d)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchresult.html#QPlaceSearchResult

    Parameters
    ----------

    d : Optional[QPlaceSearchResultPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlaceSearchResult::QPlaceSearchResult(QPlaceSearchResultPrivate *d)
    self._noteCreation(QPlaceSearchResult, lambda: Rituals.call(
        'ritual_ZN18QPlaceSearchResultC1EP25QPlaceSearchResultPrivate',
        self._addressOf(d),
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


#  Qt's 'QList<QPlaceSearchResult>': the list of QPlaceSearchResult, which
#  'QList[QPlaceSearchResult]' gives. It is made here, so that there is one
#  as soon as there can be a QPlaceSearchResult.
QList.createKind(
    QPlaceSearchResult, 'value',
    make='ritual_list_make_QPlaceSearchResult',
    add='ritual_list_add_QPlaceSearchResult',
    size='ritual_list_size_QPlaceSearchResult',
    at='ritual_list_at_QPlaceSearchResult',
    drop='ritual_list_drop_QPlaceSearchResult',
)
