"""
QPlaceMatchRequest binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacematchrequest.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVariant
  from . import QPlace, QPlaceSearchResult
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlace = WAIT['QPlace']
  QPlaceSearchResult = WAIT['QPlaceSearchResult']
  QVariant = WAIT['QVariant']


class QPlaceMatchRequest(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaceMatchRequest: a plain Python object standing in
  front of one C++ QPlaceMatchRequest.

  C++ hands a QPlaceMatchRequest around as a copy, so every C++
  QPlaceMatchRequest behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceMatchRequest that has a ritual and that Python
  can call so far, 9 names in all: '__eq__', '__ne__', 'places', 'setPlaces',
  'setResults', 'parameters', 'setParameters', 'clear', 'isEqual'. It can be
  made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceMatchRequest::QPlaceMatchRequest(QPlaceMatchRequest
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QPlaceMatchRequest::~QPlaceMatchRequest()': the destructor: Python
    removes its C++ QPlaceMatchRequest by it, and has no other use for it.
  - Qt's 'QPlaceMatchRequest &QPlaceMatchRequest::operator=(const
    QPlaceMatchRequest &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QPlaceMatchRequest
    &QPlaceMatchRequest::operator=(QPlaceMatchRequest &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'void QPlaceMatchRequest::swap(QPlaceMatchRequest &other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QPlaceMatchRequestPrivate *QPlaceMatchRequest::d_func()': gives
    'QPlaceMatchRequestPrivate', which has no cute class yet.
  - Qt's 'const QPlaceMatchRequestPrivate *QPlaceMatchRequest::d_func()
    const': gives 'QPlaceMatchRequestPrivate', which has no cute class yet.

  What to expect
  --------------

  - The C++ QPlaceMatchRequest is created at the first use, not by
    'QPlaceMatchRequest(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceMatchRequest back gives a copy the ritual made
    for Python, in a new cute QPlaceMatchRequest.
  - Each name of Qt's QPlaceMatchRequest that has no cute function yet,
    'd_func', 'swap', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceMatchRequest'

  #  Qt's '~QPlaceMatchRequest()'. Naming it makes this a value class: Python
  #  owns every C++ QPlaceMatchRequest behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN18QPlaceMatchRequestD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def places(self) -> QList[QPlace]:
    """
    Calls Qt's 'QList<QPlace> QPlaceMatchRequest::places() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchrequest.html#places

    Returns
    -------

    QList[QPlace]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QPlace> QPlaceMatchRequest::places() const
    address = self.uglySide.call('ritual_ZNK18QPlaceMatchRequest6placesEv')
    from . import QPlace
    return QList[QPlace]._cuteOwning(address)

  def parameters(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QPlaceMatchRequest::parameters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchrequest.html#parameters

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QPlaceMatchRequest::parameters() const
    address = self.uglySide.call(
        'ritual_ZNK18QPlaceMatchRequest10parametersEv',
    )
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  @overload(THIS)
  def isEqual(self, other: QPlaceMatchRequest) -> bool:
    """
    Calls Qt's 'bool QPlaceMatchRequest::isEqual(const QPlaceMatchRequest
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchrequest.html#isEqual

    Parameters
    ----------

    other : QPlaceMatchRequest
      Passed on as a value: Qt reads the C++ QPlaceMatchRequest, which stays
      Python's own.
    """
    #  bool QPlaceMatchRequest::isEqual(const QPlaceMatchRequest &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK18QPlaceMatchRequest7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QPlace])
  def setPlaces(self, places: QList[QPlace]) -> None:
    """
    Calls Qt's 'void QPlaceMatchRequest::setPlaces(const QList<QPlace>
    &places)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchrequest.html#setPlaces

    Parameters
    ----------

    places : QList[QPlace]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlaceMatchRequest::setPlaces(const QList<QPlace> &places)
    self.uglySide.call(
        'ritual_ZN18QPlaceMatchRequest9setPlacesERK5QListI6QPlaceE',
        self._valueOf(places),
    )

  @overload(QList[QPlaceSearchResult])
  def setResults(self, results: QList[QPlaceSearchResult]) -> None:
    """
    Calls Qt's 'void QPlaceMatchRequest::setResults(const
    QList<QPlaceSearchResult> &results)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchrequest.html#setResults

    Parameters
    ----------

    results : QList[QPlaceSearchResult]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QPlaceMatchRequest::setResults(const QList<QPlaceSearchResult>
    #      &results)
    self.uglySide.call(
        'ritual_ZN18QPlaceMatchRequest10setResultsERK5QListI18QPlaceSearchR'
        'esultE',
        self._valueOf(results),
    )

  @overload(QMap[str, QVariant])
  def setParameters(self, parameters: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QPlaceMatchRequest::setParameters(const QVariantMap
    &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacematchrequest.html#setParameters

    Parameters
    ----------

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QPlaceMatchRequest::setParameters(const QVariantMap &parameters)
    self.uglySide.call(
        'ritual_ZN18QPlaceMatchRequest13setParametersERK4QMapI7QString8QVar'
        'iantE',
        self._valueOf(parameters),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPlaceMatchRequest) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlaceMatchRequest &lhs, const
    QPlaceMatchRequest &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchrequest.html#operator==

    Parameters
    ----------

    rhs : QPlaceMatchRequest
      Passed on as a value: Qt reads the C++ QPlaceMatchRequest, which stays
      Python's own.
    """
    #  bool operator==(const QPlaceMatchRequest &lhs, const
    #      QPlaceMatchRequest &rhs)
    return Rituals.call(
        'ritual_ZeqRK18QPlaceMatchRequestS1_',
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
  def __ne__(self, rhs: QPlaceMatchRequest) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPlaceMatchRequest &lhs, const
    QPlaceMatchRequest &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchrequest.html#operator!=

    Parameters
    ----------

    rhs : QPlaceMatchRequest
      Passed on as a value: Qt reads the C++ QPlaceMatchRequest, which stays
      Python's own.
    """
    #  bool operator!=(const QPlaceMatchRequest &lhs, const
    #      QPlaceMatchRequest &rhs)
    return Rituals.call(
        'ritual_ZneRK18QPlaceMatchRequestS1_',
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
    'QPlaceMatchRequest::QPlaceMatchRequest()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacematchrequest.html#QPlaceMatchRequest
    """
    #  QPlaceMatchRequest::QPlaceMatchRequest()
    self._noteCreation(QPlaceMatchRequest, lambda: Rituals.call(
        'ritual_ZN18QPlaceMatchRequestC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPlaceMatchRequest) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceMatchRequest::QPlaceMatchRequest(const QPlaceMatchRequest
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacematchrequest.html#QPlaceMatchRequest

    Parameters
    ----------

    other : QPlaceMatchRequest
      Passed on as a value: Qt reads the C++ QPlaceMatchRequest, which stays
      Python's own.
    """
    #  QPlaceMatchRequest::QPlaceMatchRequest(const QPlaceMatchRequest
    #      &other)
    self._noteCreation(QPlaceMatchRequest, lambda: Rituals.call(
        'ritual_ZN18QPlaceMatchRequestC1ERKS_', self._valueOf(other),
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
    Calls Qt's 'void QPlaceMatchRequest::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacematchrequest.html#clear
    """
    #  void QPlaceMatchRequest::clear()
    self.uglySide.call('ritual_ZN18QPlaceMatchRequest5clearEv')

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QPlaceMatchRequestPrivate *QPlaceMatchRequest::d_func()': gives
      'QPlaceMatchRequestPrivate', which has no cute class yet.
    - Qt's 'const QPlaceMatchRequestPrivate *QPlaceMatchRequest::d_func()
      const': gives 'QPlaceMatchRequestPrivate', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QPlaceMatchRequest.d_func' has no cute function yet. Qt's "
        "'QPlaceMatchRequestPrivate *QPlaceMatchRequest::d_func()': gives "
        "'QPlaceMatchRequestPrivate', which has no cute class yet. Qt's "
        "'const QPlaceMatchRequestPrivate *QPlaceMatchRequest::d_func() "
        "const': gives 'QPlaceMatchRequestPrivate', which has no cute class "
        "yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPlaceMatchRequest::swap(QPlaceMatchRequest &other)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaceMatchRequest.swap' has no cute function yet. Qt's 'void "
        "QPlaceMatchRequest::swap(QPlaceMatchRequest &other)': takes a type "
        "Python has no way to hand over yet.")
