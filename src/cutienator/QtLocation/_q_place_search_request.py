"""
QPlaceSearchRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacesearchrequest.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QLocation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
  from ..QtPositioning import QGeoShape
  from . import QPlaceCategory, QPlaceSearchRequestPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGeoShape = WAIT['QGeoShape']
  QPlaceCategory = WAIT['QPlaceCategory']
  QVariant = WAIT['QVariant']


class QPlaceSearchRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaceSearchRequest: a plain Python object standing
  in front of one C++ QPlaceSearchRequest.

  C++ hands a QPlaceSearchRequest around as a copy, so every C++
  QPlaceSearchRequest behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceSearchRequest that has a ritual and that
  Python can call so far, 22 names in all: '__eq__', '__ne__', 'searchTerm',
  'setSearchTerm', 'categories', 'setCategory', 'setCategories',
  'searchArea', 'setSearchArea', 'recommendationId', 'setRecommendationId',
  'searchContext', 'setSearchContext', 'visibilityScope',
  'setVisibilityScope', 'relevanceHint', 'setRelevanceHint', 'limit',
  'setLimit', 'clear', 'isEqual', 'd_func'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceSearchRequest::QPlaceSearchRequest(QPlaceSearchRequest
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QPlaceSearchRequest::~QPlaceSearchRequest()': the destructor:
    Python removes its C++ QPlaceSearchRequest by it, and has no other use
    for it.
  - Qt's 'QPlaceSearchRequest &QPlaceSearchRequest::operator=(const
    QPlaceSearchRequest &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QPlaceSearchRequest
    &QPlaceSearchRequest::operator=(QPlaceSearchRequest &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QPlaceSearchRequest::swap(QPlaceSearchRequest &other)': takes
    a type Python has no way to hand over yet.
  - Qt's 'const QPlaceSearchRequestPrivate *QPlaceSearchRequest::d_func()
    const': takes in Python what 'QPlaceSearchRequestPrivate
    *QPlaceSearchRequest::d_func()' takes.

  What to expect
  --------------

  - The C++ QPlaceSearchRequest is created at the first use, not by
    'QPlaceSearchRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceSearchRequest back gives a copy the ritual made
    for Python, in a new cute QPlaceSearchRequest.
  - Each name of Qt's QPlaceSearchRequest that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QPlaceSearchRequest, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class RelevanceHint(CuteNum):
    """
    The enum 'QPlaceSearchRequest::RelevanceHint' of Qt, with the 3 names Qt
    gives in it.
    """

    UnspecifiedHint = Kee[int](0)
    DistanceHint = Kee[int](1)
    LexicalPlaceNameHint = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceSearchRequest'

  #  Qt's '~QPlaceSearchRequest()'. Naming it makes this a value class:
  #  Python owns every C++ QPlaceSearchRequest behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QPlaceSearchRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def searchTerm(self) -> str:
    """
    Calls Qt's 'QString QPlaceSearchRequest::searchTerm() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#searchTerm

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceSearchRequest::searchTerm() const
    return self.uglySide.call(
        'ritual_ZNK19QPlaceSearchRequest10searchTermEv',
    )

  def categories(self) -> QList[QPlaceCategory]:
    """
    Calls Qt's 'QList<QPlaceCategory> QPlaceSearchRequest::categories()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#categories

    Returns
    -------

    QList[QPlaceCategory]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlaceCategory> QPlaceSearchRequest::categories() const
    address = self.uglySide.call(
        'ritual_ZNK19QPlaceSearchRequest10categoriesEv',
    )
    from . import QPlaceCategory
    return QList[QPlaceCategory]._cuteOwning(address)

  def searchArea(self) -> QGeoShape:
    """
    Calls Qt's 'QGeoShape QPlaceSearchRequest::searchArea() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#searchArea

    Returns
    -------

    QGeoShape
      A new cute QGeoShape around the copy Qt gave back. Python owns it.
    """
    #  QGeoShape QPlaceSearchRequest::searchArea() const
    address = self.uglySide.call(
        'ritual_ZNK19QPlaceSearchRequest10searchAreaEv',
    )
    from ..QtPositioning import QGeoShape
    return QGeoShape._cuteOwning(address)

  def recommendationId(self) -> str:
    """
    Calls Qt's 'QString QPlaceSearchRequest::recommendationId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#recommendationId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceSearchRequest::recommendationId() const
    return self.uglySide.call(
        'ritual_ZNK19QPlaceSearchRequest16recommendationIdEv',
    )

  def searchContext(self) -> QVariant:
    """
    Calls Qt's 'QVariant QPlaceSearchRequest::searchContext() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#searchContext

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QPlaceSearchRequest::searchContext() const
    address = self.uglySide.call(
        'ritual_ZNK19QPlaceSearchRequest13searchContextEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def visibilityScope(self) -> QLocation.VisibilityScope:
    """
    Calls Qt's 'QLocation::VisibilityScope
    QPlaceSearchRequest::visibilityScope() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#visibilityScope

    Returns
    -------

    QLocation.VisibilityScope
      The value standing for the combination Qt gave back.
    """
    #  QLocation::VisibilityScope QPlaceSearchRequest::visibilityScope()
    #      const
    return QLocation.VisibilityScope(self.uglySide.call(
        'ritual_ZNK19QPlaceSearchRequest15visibilityScopeEv',
    ))

  def relevanceHint(self) -> RelevanceHint:
    """
    Calls Qt's 'RelevanceHint QPlaceSearchRequest::relevanceHint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#relevanceHint

    Returns
    -------

    RelevanceHint
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'RelevanceHint(number)'
      gives.
    """
    #  RelevanceHint QPlaceSearchRequest::relevanceHint() const
    return QPlaceSearchRequest.RelevanceHint(self.uglySide.call(
        'ritual_ZNK19QPlaceSearchRequest13relevanceHintEv',
    ))

  def limit(self) -> int:
    """
    Calls Qt's 'int QPlaceSearchRequest::limit() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchrequest.html#limit
    """
    #  int QPlaceSearchRequest::limit() const
    return self.uglySide.call('ritual_ZNK19QPlaceSearchRequest5limitEv')

  @overload(THIS)
  def isEqual(self, other: QPlaceSearchRequest) -> bool:
    """
    Calls Qt's 'bool QPlaceSearchRequest::isEqual(const QPlaceSearchRequest
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchrequest.html#isEqual

    Parameters
    ----------

    other : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.
    """
    #  bool QPlaceSearchRequest::isEqual(const QPlaceSearchRequest &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QPlaceSearchRequest7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setSearchTerm(self, term: str) -> None:
    """
    Calls Qt's 'void QPlaceSearchRequest::setSearchTerm(const QString
    &term)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#setSearchTerm

    Parameters
    ----------

    term : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceSearchRequest::setSearchTerm(const QString &term)
    self.uglySide.call(
        'ritual_ZN19QPlaceSearchRequest13setSearchTermERK7QString', term,
    )

  @overload(QPlaceCategory)
  def setCategory(self, category: QPlaceCategory) -> None:
    """
    Calls Qt's 'void QPlaceSearchRequest::setCategory(const QPlaceCategory
    &category)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#setCategory

    Parameters
    ----------

    category : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.
    """
    #  void QPlaceSearchRequest::setCategory(const QPlaceCategory &category)
    self.uglySide.call(
        'ritual_ZN19QPlaceSearchRequest11setCategoryERK14QPlaceCategory',
        self._valueOf(category),
    )

  @overload(QList[QPlaceCategory])
  def setCategories(self, categories: QList[QPlaceCategory]) -> None:
    """
    Calls Qt's 'void QPlaceSearchRequest::setCategories(const
    QList<QPlaceCategory> &categories)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#setCategories

    Parameters
    ----------

    categories : QList[QPlaceCategory]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlaceSearchRequest::setCategories(const QList<QPlaceCategory>
    #      &categories)
    self.uglySide.call(
        'ritual_ZN19QPlaceSearchRequest13setCategoriesERK5QListI14QPlaceCat'
        'egoryE',
        self._valueOf(categories),
    )

  @overload(QGeoShape)
  def setSearchArea(self, area: QGeoShape) -> None:
    """
    Calls Qt's 'void QPlaceSearchRequest::setSearchArea(const QGeoShape
    &area)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#setSearchArea

    Parameters
    ----------

    area : QGeoShape
      Passed on as a value: Qt reads the C++ QGeoShape, which stays Python's
      own.
    """
    #  void QPlaceSearchRequest::setSearchArea(const QGeoShape &area)
    self.uglySide.call(
        'ritual_ZN19QPlaceSearchRequest13setSearchAreaERK9QGeoShape',
        self._valueOf(area),
    )

  @overload(str)
  def setRecommendationId(self, recommendationId: str) -> None:
    """
    Calls Qt's 'void QPlaceSearchRequest::setRecommendationId(const QString
    &recommendationId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#setRecommendationId

    Parameters
    ----------

    recommendationId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceSearchRequest::setRecommendationId(const QString
    #      &recommendationId)
    self.uglySide.call(
        'ritual_ZN19QPlaceSearchRequest19setRecommendationIdERK7QString',
        recommendationId,
    )

  @overload(QVariant)
  def setSearchContext(self, context: QVariant) -> None:
    """
    Calls Qt's 'void QPlaceSearchRequest::setSearchContext(const QVariant
    &context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#setSearchContext

    Parameters
    ----------

    context : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QPlaceSearchRequest::setSearchContext(const QVariant &context)
    self.uglySide.call(
        'ritual_ZN19QPlaceSearchRequest16setSearchContextERK8QVariant',
        self._valueOf(context),
    )

  @overload(QLocation.VisibilityScope)
  def setVisibilityScope(
      self,
      visibilityScopes: QLocation.VisibilityScope,
  ) -> None:
    """
    Calls Qt's 'void
    QPlaceSearchRequest::setVisibilityScope(QLocation::VisibilityScope
    visibilityScopes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#setVisibilityScope

    Parameters
    ----------

    visibilityScopes : QLocation.VisibilityScope
      Passed on as its number.
    """
    #  void
    #      QPlaceSearchRequest::setVisibilityScope(QLocation::VisibilityScope
    #      visibilityScopes)
    self.uglySide.call(
        'ritual_ZN19QPlaceSearchRequest18setVisibilityScopeE6QFlagsIN9QLoca'
        'tion10VisibilityEE',
        visibilityScopes.value,
    )

  @overload(RelevanceHint)
  def setRelevanceHint(self, hint: RelevanceHint) -> None:
    """
    Calls Qt's 'void QPlaceSearchRequest::setRelevanceHint(RelevanceHint
    hint)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#setRelevanceHint

    Parameters
    ----------

    hint : RelevanceHint
      Passed on as its number.
    """
    #  void QPlaceSearchRequest::setRelevanceHint(RelevanceHint hint)
    self.uglySide.call(
        'ritual_ZN19QPlaceSearchRequest16setRelevanceHintENS_13RelevanceHin'
        'tE',
        hint.value,
    )

  @overload(int)
  def setLimit(self, limit: int) -> None:
    """
    Calls Qt's 'void QPlaceSearchRequest::setLimit(int limit)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchrequest.html#setLimit

    Parameters
    ----------

    limit : int
      Passed on as it is.
    """
    #  void QPlaceSearchRequest::setLimit(int limit)
    self.uglySide.call('ritual_ZN19QPlaceSearchRequest8setLimitEi', limit)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPlaceSearchRequest) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlaceSearchRequest &lhs, const
    QPlaceSearchRequest &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#operator==

    Parameters
    ----------

    rhs : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.
    """
    #  bool operator==(const QPlaceSearchRequest &lhs, const
    #      QPlaceSearchRequest &rhs)
    return Rituals.call(
        'ritual_ZeqRK19QPlaceSearchRequestS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
  def __ne__(self, rhs: QPlaceSearchRequest) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPlaceSearchRequest &lhs, const
    QPlaceSearchRequest &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#operator!=

    Parameters
    ----------

    rhs : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.
    """
    #  bool operator!=(const QPlaceSearchRequest &lhs, const
    #      QPlaceSearchRequest &rhs)
    return Rituals.call(
        'ritual_ZneRK19QPlaceSearchRequestS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
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
    'QPlaceSearchRequest::QPlaceSearchRequest()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#QPlaceSearchRequest
    """
    #  QPlaceSearchRequest::QPlaceSearchRequest()
    self._noteCreation(QPlaceSearchRequest, lambda: Rituals.call(
        'ritual_ZN19QPlaceSearchRequestC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPlaceSearchRequest) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceSearchRequest::QPlaceSearchRequest(const QPlaceSearchRequest
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacesearchrequest.html#QPlaceSearchRequest

    Parameters
    ----------

    other : QPlaceSearchRequest
      Passed on as a value: Qt reads the C++ QPlaceSearchRequest, which stays
      Python's own.
    """
    #  QPlaceSearchRequest::QPlaceSearchRequest(const QPlaceSearchRequest
    #      &other)
    self._noteCreation(QPlaceSearchRequest, lambda: Rituals.call(
        'ritual_ZN19QPlaceSearchRequestC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QPlaceSearchRequest::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchrequest.html#clear
    """
    #  void QPlaceSearchRequest::clear()
    self.uglySide.call('ritual_ZN19QPlaceSearchRequest5clearEv')

  def d_func(self) -> Optional[QPlaceSearchRequestPrivate]:
    """
    Calls Qt's 'QPlaceSearchRequestPrivate *QPlaceSearchRequest::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesearchrequest.html#d_func

    Returns
    -------

    Optional[QPlaceSearchRequestPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceSearchRequestPrivate *QPlaceSearchRequest::d_func()
    address = self.uglySide.call('ritual_ZN19QPlaceSearchRequest6d_funcEv')
    from . import QPlaceSearchRequestPrivate
    return QPlaceSearchRequestPrivate._cuteAt(address)

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPlaceSearchRequest::swap(QPlaceSearchRequest &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaceSearchRequest.swap' has no cute function yet. Qt's 'void "
        "QPlaceSearchRequest::swap(QPlaceSearchRequest &other)': takes a "
        "type Python has no way to hand over yet.")
