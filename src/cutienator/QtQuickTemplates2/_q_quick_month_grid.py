"""
QQuickMonthGrid binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmonthgrid_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickMonthGrid to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QDateTime, QLocale, QMarginsF, QMetaObject, QRectF
  from ..QtCore import QTimerEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']
  QLocale = WAIT['QLocale']
  QMarginsF = WAIT['QMarginsF']
  QRectF = WAIT['QRectF']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMonthGrid(QQuickControl):
  """
  The cute side of Qt's QQuickMonthGrid: a plain Python object standing in
  front of one C++ QQuickMonthGrid.

  It is built on the cute 'QQuickControl', as Qt's QQuickMonthGrid is built
  on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMonthGrid that has a ritual and that Python
  can call so far, 16 names in all: 'metaObject', 'monthChanged',
  'yearChanged', 'sourceChanged', 'titleChanged', 'delegateChanged',
  'pressed', 'released', 'clicked', 'pressAndHold', 'componentComplete',
  'geometryChange', 'localeChange', 'paddingChange', 'updatePolish',
  'timerEvent'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMonthGrid::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickMonthGrid::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickMonthGridPrivate *QQuickMonthGrid::d_func()': gives
    'QQuickMonthGridPrivate', which has no cute class yet.
  - Qt's 'const QQuickMonthGridPrivate *QQuickMonthGrid::d_func() const':
    gives 'QQuickMonthGridPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  16 of the 36 functions Qt declares: 11 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 forbidden; 1 leans on 'QQuickMonthGrid.

  What to expect
  --------------

  - The C++ QQuickMonthGrid is created at the first use, not by
    'QQuickMonthGrid(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMonthGrid.
  - Qt tells when it has removed the C++ QQuickMonthGrid. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickMonthGrid that has no cute function yet,
    '__init__', 'delegate', 'month', 'setDelegate', 'setMonth', 'setSource',
    'setTitle', 'setYear', 'source', 'title', 'year', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMonthGrid'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMonthGrid::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMonthGrid::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickMonthGrid10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickMonthGrid::QQuickMonthGrid(QQuickItem *parent)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type
    'QQuickMonthGridPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthGrid.__init__' has no cute function yet. Qt's "
        "'QQuickMonthGrid::QQuickMonthGrid(QQuickItem *parent)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QQuickMonthGridPrivate'.")

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

  def monthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::monthChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#monthChanged
    """
    #  void QQuickMonthGrid::monthChanged()
    self.uglySide.call('ritual_ZN15QQuickMonthGrid12monthChangedEv')

  def yearChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::yearChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#yearChanged
    """
    #  void QQuickMonthGrid::yearChanged()
    self.uglySide.call('ritual_ZN15QQuickMonthGrid11yearChangedEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::sourceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#sourceChanged
    """
    #  void QQuickMonthGrid::sourceChanged()
    self.uglySide.call('ritual_ZN15QQuickMonthGrid13sourceChangedEv')

  def titleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::titleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#titleChanged
    """
    #  void QQuickMonthGrid::titleChanged()
    self.uglySide.call('ritual_ZN15QQuickMonthGrid12titleChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmonthgrid.html#delegateChanged
    """
    #  void QQuickMonthGrid::delegateChanged()
    self.uglySide.call('ritual_ZN15QQuickMonthGrid15delegateChangedEv')

  @overload(QDateTime)
  def pressed(self, date: QDateTime) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::pressed(QDateTime date)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#pressed

    Parameters
    ----------

    date : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QQuickMonthGrid::pressed(QDateTime date)
    self.uglySide.call(
        'ritual_ZN15QQuickMonthGrid7pressedE9QDateTime', self._valueOf(date),
    )

  @overload(QDateTime)
  def released(self, date: QDateTime) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::released(QDateTime date)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#released

    Parameters
    ----------

    date : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QQuickMonthGrid::released(QDateTime date)
    self.uglySide.call(
        'ritual_ZN15QQuickMonthGrid8releasedE9QDateTime',
        self._valueOf(date),
    )

  @overload(QDateTime)
  def clicked(self, date: QDateTime) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::clicked(QDateTime date)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#clicked

    Parameters
    ----------

    date : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QQuickMonthGrid::clicked(QDateTime date)
    self.uglySide.call(
        'ritual_ZN15QQuickMonthGrid7clickedE9QDateTime', self._valueOf(date),
    )

  @overload(QDateTime)
  def pressAndHold(self, date: QDateTime) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::pressAndHold(QDateTime date)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#pressAndHold

    Parameters
    ----------

    date : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  void QQuickMonthGrid::pressAndHold(QDateTime date)
    self.uglySide.call(
        'ritual_ZN15QQuickMonthGrid12pressAndHoldE9QDateTime',
        self._valueOf(date),
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmonthgrid.html#componentComplete
    """
    #  void QQuickMonthGrid::componentComplete()
    ritual = 'ritual_ZN15QQuickMonthGrid17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickMonthGrid17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmonthgrid.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickMonthGrid::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickMonthGrid14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickMonthGrid14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QLocale, QLocale)
  def localeChange(self, newLocale: QLocale, oldLocale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::localeChange(const QLocale &newLocale,
    const QLocale &oldLocale)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#localeChange

    Parameters
    ----------

    newLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    oldLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickMonthGrid::localeChange(const QLocale &newLocale, const
    #      QLocale &oldLocale)
    self.uglySide.call(
        'ritual_ZN15QQuickMonthGrid12localeChangeERK7QLocaleS2_',
        self._valueOf(newLocale), self._valueOf(oldLocale),
    )

  @overload(QMarginsF, QMarginsF)
  def paddingChange(
      self,
      newPadding: QMarginsF,
      oldPadding: QMarginsF,
  ) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::paddingChange(const QMarginsF
    &newPadding, const QMarginsF &oldPadding)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#paddingChange

    Parameters
    ----------

    newPadding : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldPadding : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickMonthGrid::paddingChange(const QMarginsF &newPadding, const
    #      QMarginsF &oldPadding)
    ritual = 'ritual_ZN15QQuickMonthGrid13paddingChangeERK9QMarginsFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickMonthGrid13paddingChangeERK9QMarginsFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newPadding), self._valueOf(oldPadding),
    )

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#updatePolish
    """
    #  void QQuickMonthGrid::updatePolish()
    ritual = 'ritual_ZN15QQuickMonthGrid12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickMonthGrid12updatePolishEv'
    self.uglySide.call(ritual)

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickMonthGrid::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmonthgrid.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMonthGrid::timerEvent(QTimerEvent *event)
    self.uglySide.call(
        'ritual_ZN15QQuickMonthGrid10timerEventEP11QTimerEvent',
        self._addressOf(event),
    )

  @staticmethod
  def delegate(*__, **_) -> Never:
    """
    Qt's 'QQmlComponent *QQuickMonthGrid::delegate() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'const
    QQuickMonthGridPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthGrid.delegate' has no cute function yet. Qt's "
        "'QQmlComponent *QQuickMonthGrid::delegate() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type 'const "
        "QQuickMonthGridPrivate'.")

  @staticmethod
  def month(*__, **_) -> Never:
    """
    Qt's 'int QQuickMonthGrid::month() const': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickMonthGridPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthGrid.month' has no cute function yet. Qt's 'int "
        "QQuickMonthGrid::month() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'const QQuickMonthGridPrivate'.")

  @staticmethod
  def setDelegate(*__, **_) -> Never:
    """
    Qt's 'void QQuickMonthGrid::setDelegate(QQmlComponent *delegate)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickMonthGridPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthGrid.setDelegate' has no cute function yet. Qt's 'void "
        "QQuickMonthGrid::setDelegate(QQmlComponent *delegate)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QQuickMonthGridPrivate'.")

  @staticmethod
  def setMonth(*__, **_) -> Never:
    """
    Qt's 'void QQuickMonthGrid::setMonth(int month)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QQuickMonthGridPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthGrid.setMonth' has no cute function yet. Qt's 'void "
        "QQuickMonthGrid::setMonth(int month)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type "
        "'QQuickMonthGridPrivate'.")

  @staticmethod
  def setSource(*__, **_) -> Never:
    """
    Qt's 'void QQuickMonthGrid::setSource(const QVariant &source)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickMonthGridPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthGrid.setSource' has no cute function yet. Qt's 'void "
        "QQuickMonthGrid::setSource(const QVariant &source)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QQuickMonthGridPrivate'.")

  @staticmethod
  def setTitle(*__, **_) -> Never:
    """
    Qt's 'void QQuickMonthGrid::setTitle(const QString &title)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type
    'QQuickMonthGridPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthGrid.setTitle' has no cute function yet. Qt's 'void "
        "QQuickMonthGrid::setTitle(const QString &title)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QQuickMonthGridPrivate'.")

  @staticmethod
  def setYear(*__, **_) -> Never:
    """
    Qt's 'void QQuickMonthGrid::setYear(int year)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QQuickMonthGridPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthGrid.setYear' has no cute function yet. Qt's 'void "
        "QQuickMonthGrid::setYear(int year)': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'QQuickMonthGridPrivate'.")

  @staticmethod
  def source(*__, **_) -> Never:
    """
    Qt's 'QVariant QQuickMonthGrid::source() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickMonthGridPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthGrid.source' has no cute function yet. Qt's 'QVariant "
        "QQuickMonthGrid::source() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'const QQuickMonthGridPrivate'.")

  @staticmethod
  def title(*__, **_) -> Never:
    """
    Qt's 'QString QQuickMonthGrid::title() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickMonthGridPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthGrid.title' has no cute function yet. Qt's 'QString "
        "QQuickMonthGrid::title() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'const QQuickMonthGridPrivate'.")

  @staticmethod
  def year(*__, **_) -> Never:
    """
    Qt's 'int QQuickMonthGrid::year() const': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickMonthGridPrivate'.
    """
    raise NotImplementedError(
        "'QQuickMonthGrid.year' has no cute function yet. Qt's 'int "
        "QQuickMonthGrid::year() const': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'const QQuickMonthGridPrivate'.")
