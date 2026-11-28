"""
QPdfPageNavigator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtPdf/qpdfpagenavigator.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPointF
  from . import QPdfLink
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPdfLink = WAIT['QPdfLink']
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPdfPageNavigator(QObject):
  """
  The cute side of Qt's QPdfPageNavigator: a plain Python object standing in
  front of one C++ QPdfPageNavigator.

  It is built on the cute 'QObject', as Qt's QPdfPageNavigator is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPdfPageNavigator that has a ritual and that Python
  can call so far, 19 names in all: 'metaObject', 'tr', 'currentPage',
  'currentLocation', 'currentZoom', 'backAvailable', 'forwardAvailable',
  'clear', 'jump', 'update', 'forward', 'back', 'currentPageChanged',
  'currentLocationChanged', 'currentZoomChanged', 'backAvailableChanged',
  'forwardAvailableChanged', 'jumped', 'currentLink'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPdfPageNavigator::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPdfPageNavigator::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPdfPageNavigator::~QPdfPageNavigator()': the destructor: Python
    never removes a C++ QPdfPageNavigator.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPdfPageNavigator is created at the first use, not by
    'QPdfPageNavigator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPdfPageNavigator.
  - Qt tells when it has removed the C++ QPdfPageNavigator. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QPdfPageNavigator::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagenavigator.html#tr

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
    #  QString QPdfPageNavigator::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QPdfPageNavigator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPdfPageNavigator'

  #  A C++ QPdfPageNavigator Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPdfPageNavigator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QPdfPageNavigator::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagenavigator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPdfPageNavigator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QPdfPageNavigator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentPage(self) -> int:
    """
    Calls Qt's 'int QPdfPageNavigator::currentPage() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagenavigator.html#currentPage
    """
    #  int QPdfPageNavigator::currentPage() const
    return self.uglySide.call('ritual_ZNK17QPdfPageNavigator11currentPageEv')

  def currentLocation(self) -> QPointF:
    """
    Calls Qt's 'QPointF QPdfPageNavigator::currentLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagenavigator.html#currentLocation

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  QPointF QPdfPageNavigator::currentLocation() const
    address = self.uglySide.call(
        'ritual_ZNK17QPdfPageNavigator15currentLocationEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  def currentZoom(self) -> float:
    """
    Calls Qt's 'qreal QPdfPageNavigator::currentZoom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagenavigator.html#currentZoom
    """
    #  qreal QPdfPageNavigator::currentZoom() const
    return self.uglySide.call('ritual_ZNK17QPdfPageNavigator11currentZoomEv')

  def backAvailable(self) -> bool:
    """
    Calls Qt's 'bool QPdfPageNavigator::backAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagenavigator.html#backAvailable
    """
    #  bool QPdfPageNavigator::backAvailable() const
    return self.uglySide.call(
        'ritual_ZNK17QPdfPageNavigator13backAvailableEv',
    )

  def forwardAvailable(self) -> bool:
    """
    Calls Qt's 'bool QPdfPageNavigator::forwardAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagenavigator.html#forwardAvailable
    """
    #  bool QPdfPageNavigator::forwardAvailable() const
    return self.uglySide.call(
        'ritual_ZNK17QPdfPageNavigator16forwardAvailableEv',
    )

  def currentLink(self) -> QPdfLink:
    """
    Calls Qt's 'QPdfLink QPdfPageNavigator::currentLink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagenavigator.html#currentLink

    Returns
    -------

    QPdfLink
      A new cute QPdfLink around the copy Qt gave back. Python owns it.
    """
    #  QPdfLink QPdfPageNavigator::currentLink() const
    address = self.uglySide.call(
        'ritual_ZNK17QPdfPageNavigator11currentLinkEv',
    )
    from . import QPdfLink
    return QPdfLink._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QPdfPageNavigator::QPdfPageNavigator()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagenavigator.html#QPdfPageNavigator
    """
    #  QPdfPageNavigator::QPdfPageNavigator()
    self._noteCreation(QPdfPageNavigator, lambda: Rituals.call(
        'ritual_ZN17QPdfPageNavigatorC1Ev',
    ))

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's
    'QPdfPageNavigator::QPdfPageNavigator(QObject *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagenavigator.html#QPdfPageNavigator

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPdfPageNavigator::QPdfPageNavigator(QObject *parent)
    self._noteCreation(QPdfPageNavigator, lambda: Rituals.call(
        'ritual_ZN17QPdfPageNavigatorC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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
    Calls Qt's 'void QPdfPageNavigator::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagenavigator.html#clear
    """
    #  void QPdfPageNavigator::clear()
    self.uglySide.call('ritual_ZN17QPdfPageNavigator5clearEv')

  @overload(QPdfLink)
  def jump(self, destination: QPdfLink) -> None:
    """
    Calls Qt's 'void QPdfPageNavigator::jump(QPdfLink destination)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagenavigator.html#jump

    Parameters
    ----------

    destination : QPdfLink
      Passed on as a value: Qt reads the C++ QPdfLink, which stays Python's
      own.
    """
    #  void QPdfPageNavigator::jump(QPdfLink destination)
    self.uglySide.call(
        'ritual_ZN17QPdfPageNavigator4jumpE8QPdfLink',
        self._valueOf(destination),
    )

  @overload(int, QPointF)
  @overload(int, QPointF, float)
  def jump(self, page: int, location: QPointF, zoom: float = 0.0) -> None:
    """
    Calls Qt's 'void QPdfPageNavigator::jump(int page, const QPointF
    &location, qreal zoom)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagenavigator.html#jump

    Parameters
    ----------

    page : int
      Passed on as it is.

    location : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    zoom : float
      Passed on as it is. May be left out, as in Qt: it is then 0.0.
    """
    #  void QPdfPageNavigator::jump(int page, const QPointF &location, qreal
    #      zoom)
    self.uglySide.call(
        'ritual_ZN17QPdfPageNavigator4jumpEiRK7QPointFd',
        page, self._valueOf(location, 'QPointF'), zoom,
    )

  @overload(int, QPointF, float)
  def update(self, page: int, location: QPointF, zoom: float) -> None:
    """
    Calls Qt's 'void QPdfPageNavigator::update(int page, const QPointF
    &location, qreal zoom)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagenavigator.html#update

    Parameters
    ----------

    page : int
      Passed on as it is.

    location : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    zoom : float
      Passed on as it is.
    """
    #  void QPdfPageNavigator::update(int page, const QPointF &location,
    #      qreal zoom)
    self.uglySide.call(
        'ritual_ZN17QPdfPageNavigator6updateEiRK7QPointFd',
        page, self._valueOf(location, 'QPointF'), zoom,
    )

  def forward(self) -> None:
    """
    Calls Qt's 'void QPdfPageNavigator::forward()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagenavigator.html#forward
    """
    #  void QPdfPageNavigator::forward()
    self.uglySide.call('ritual_ZN17QPdfPageNavigator7forwardEv')

  def back(self) -> None:
    """
    Calls Qt's 'void QPdfPageNavigator::back()'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagenavigator.html#back
    """
    #  void QPdfPageNavigator::back()
    self.uglySide.call('ritual_ZN17QPdfPageNavigator4backEv')

  @overload(int)
  def currentPageChanged(self, page: int) -> None:
    """
    Calls Qt's 'void QPdfPageNavigator::currentPageChanged(int page)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagenavigator.html#currentPageChanged

    Parameters
    ----------

    page : int
      Passed on as it is.
    """
    #  void QPdfPageNavigator::currentPageChanged(int page)
    self.uglySide.call(
        'ritual_ZN17QPdfPageNavigator18currentPageChangedEi', page,
    )

  @overload(QPointF)
  def currentLocationChanged(self, location: QPointF) -> None:
    """
    Calls Qt's 'void QPdfPageNavigator::currentLocationChanged(QPointF
    location)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagenavigator.html#currentLocationChanged

    Parameters
    ----------

    location : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QPdfPageNavigator::currentLocationChanged(QPointF location)
    self.uglySide.call(
        'ritual_ZN17QPdfPageNavigator22currentLocationChangedE7QPointF',
        self._valueOf(location, 'QPointF'),
    )

  @overload(float)
  def currentZoomChanged(self, zoom: float) -> None:
    """
    Calls Qt's 'void QPdfPageNavigator::currentZoomChanged(qreal zoom)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagenavigator.html#currentZoomChanged

    Parameters
    ----------

    zoom : float
      Passed on as it is.
    """
    #  void QPdfPageNavigator::currentZoomChanged(qreal zoom)
    self.uglySide.call(
        'ritual_ZN17QPdfPageNavigator18currentZoomChangedEd', zoom,
    )

  @overload(bool)
  def backAvailableChanged(self, available: bool) -> None:
    """
    Calls Qt's 'void QPdfPageNavigator::backAvailableChanged(bool
    available)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagenavigator.html#backAvailableChanged

    Parameters
    ----------

    available : bool
      Passed on as it is.
    """
    #  void QPdfPageNavigator::backAvailableChanged(bool available)
    self.uglySide.call(
        'ritual_ZN17QPdfPageNavigator20backAvailableChangedEb', available,
    )

  @overload(bool)
  def forwardAvailableChanged(self, available: bool) -> None:
    """
    Calls Qt's 'void QPdfPageNavigator::forwardAvailableChanged(bool
    available)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpdfpagenavigator.html#forwardAvailableChanged

    Parameters
    ----------

    available : bool
      Passed on as it is.
    """
    #  void QPdfPageNavigator::forwardAvailableChanged(bool available)
    self.uglySide.call(
        'ritual_ZN17QPdfPageNavigator23forwardAvailableChangedEb', available,
    )

  @overload(QPdfLink)
  def jumped(self, current: QPdfLink) -> None:
    """
    Calls Qt's 'void QPdfPageNavigator::jumped(QPdfLink current)'.

    Qt's own words: https://doc.qt.io/qt-6/qpdfpagenavigator.html#jumped

    Parameters
    ----------

    current : QPdfLink
      Passed on as a value: Qt reads the C++ QPdfLink, which stays Python's
      own.
    """
    #  void QPdfPageNavigator::jumped(QPdfLink current)
    self.uglySide.call(
        'ritual_ZN17QPdfPageNavigator6jumpedE8QPdfLink',
        self._valueOf(current),
    )
