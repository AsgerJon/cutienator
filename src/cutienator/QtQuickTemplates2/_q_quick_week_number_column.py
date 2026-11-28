"""
QQuickWeekNumberColumn binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickweeknumbercolumn_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickWeekNumberColumn to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLocale, QMarginsF, QMetaObject, QRectF
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocale = WAIT['QLocale']
  QMarginsF = WAIT['QMarginsF']
  QRectF = WAIT['QRectF']


class QQuickWeekNumberColumn(QQuickControl):
  """
  The cute side of Qt's QQuickWeekNumberColumn: a plain Python object
  standing in front of one C++ QQuickWeekNumberColumn.

  It is built on the cute 'QQuickControl', as Qt's QQuickWeekNumberColumn is
  built on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWeekNumberColumn that has a ritual and that
  Python can call so far, 9 names in all: 'metaObject', 'monthChanged',
  'yearChanged', 'sourceChanged', 'delegateChanged', 'componentComplete',
  'geometryChange', 'localeChange', 'paddingChange'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWeekNumberColumn::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickWeekNumberColumn::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickWeekNumberColumnPrivate *QQuickWeekNumberColumn::d_func()':
    gives 'QQuickWeekNumberColumnPrivate', which has no cute class yet.
  - Qt's 'const QQuickWeekNumberColumnPrivate
    *QQuickWeekNumberColumn::d_func() const': gives
    'QQuickWeekNumberColumnPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  14 of the 27 functions Qt declares: 9 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 forbidden; 1 leans on 'QQuickWeekNumberColumn.

  What to expect
  --------------

  - The C++ QQuickWeekNumberColumn is created at the first use, not by
    'QQuickWeekNumberColumn(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWeekNumberColumn.
  - Qt tells when it has removed the C++ QQuickWeekNumberColumn. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickWeekNumberColumn that has no cute function yet,
    '__init__', 'delegate', 'month', 'setDelegate', 'setMonth', 'setSource',
    'setYear', 'source', 'year', holds a function that raises
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
  __qt_class__ = 'QQuickWeekNumberColumn'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWeekNumberColumn::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbercolumn.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWeekNumberColumn::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQuickWeekNumberColumn10metaObjectEv',
    )
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
    Qt's 'QQuickWeekNumberColumn::QQuickWeekNumberColumn(QQuickItem
    *parent)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: member access into incomplete type
    'QQuickWeekNumberColumnPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberColumn.__init__' has no cute function yet. Qt's "
        "'QQuickWeekNumberColumn::QQuickWeekNumberColumn(QQuickItem "
        "*parent)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QQuickWeekNumberColumnPrivate'.")

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
    Calls Qt's 'void QQuickWeekNumberColumn::monthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbercolumn.html#monthChanged
    """
    #  void QQuickWeekNumberColumn::monthChanged()
    self.uglySide.call('ritual_ZN22QQuickWeekNumberColumn12monthChangedEv')

  def yearChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWeekNumberColumn::yearChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbercolumn.html#yearChanged
    """
    #  void QQuickWeekNumberColumn::yearChanged()
    self.uglySide.call('ritual_ZN22QQuickWeekNumberColumn11yearChangedEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWeekNumberColumn::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbercolumn.html#sourceChanged
    """
    #  void QQuickWeekNumberColumn::sourceChanged()
    self.uglySide.call('ritual_ZN22QQuickWeekNumberColumn13sourceChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickWeekNumberColumn::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbercolumn.html#delegateChanged
    """
    #  void QQuickWeekNumberColumn::delegateChanged()
    self.uglySide.call(
        'ritual_ZN22QQuickWeekNumberColumn15delegateChangedEv',
    )

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickWeekNumberColumn::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbercolumn.html#componentComplete
    """
    #  void QQuickWeekNumberColumn::componentComplete()
    ritual = 'ritual_ZN22QQuickWeekNumberColumn17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN22QQuickWeekNumberColumn17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickWeekNumberColumn::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbercolumn.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickWeekNumberColumn::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN22QQuickWeekNumberColumn14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickWeekNumberColumn14geometryChangeERK6QRectFS'
          '2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QLocale, QLocale)
  def localeChange(self, newLocale: QLocale, oldLocale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickWeekNumberColumn::localeChange(const QLocale
    &newLocale, const QLocale &oldLocale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbercolumn.html#localeChange

    Parameters
    ----------

    newLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    oldLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickWeekNumberColumn::localeChange(const QLocale &newLocale,
    #      const QLocale &oldLocale)
    self.uglySide.call(
        'ritual_ZN22QQuickWeekNumberColumn12localeChangeERK7QLocaleS2_',
        self._valueOf(newLocale), self._valueOf(oldLocale),
    )

  @overload(QMarginsF, QMarginsF)
  def paddingChange(
      self,
      newPadding: QMarginsF,
      oldPadding: QMarginsF,
  ) -> None:
    """
    Calls Qt's 'void QQuickWeekNumberColumn::paddingChange(const QMarginsF
    &newPadding, const QMarginsF &oldPadding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickweeknumbercolumn.html#paddingChange

    Parameters
    ----------

    newPadding : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldPadding : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickWeekNumberColumn::paddingChange(const QMarginsF
    #      &newPadding, const QMarginsF &oldPadding)
    ritual = (
        'ritual_ZN22QQuickWeekNumberColumn13paddingChangeERK9QMarginsFS2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN22QQuickWeekNumberColumn13paddingChangeERK9QMargins'
          'FS2_')
    self.uglySide.call(
        ritual, self._valueOf(newPadding), self._valueOf(oldPadding),
    )

  @staticmethod
  def delegate(*__, **_) -> Never:
    """
    Qt's 'QQmlComponent *QQuickWeekNumberColumn::delegate() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    QQuickWeekNumberColumnPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberColumn.delegate' has no cute function yet. Qt's "
        "'QQmlComponent *QQuickWeekNumberColumn::delegate() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuickWeekNumberColumnPrivate'.")

  @staticmethod
  def month(*__, **_) -> Never:
    """
    Qt's 'int QQuickWeekNumberColumn::month() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const
    QQuickWeekNumberColumnPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberColumn.month' has no cute function yet. Qt's 'int "
        "QQuickWeekNumberColumn::month() const': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type 'const "
        "QQuickWeekNumberColumnPrivate'.")

  @staticmethod
  def setDelegate(*__, **_) -> Never:
    """
    Qt's 'void QQuickWeekNumberColumn::setDelegate(QQmlComponent *delegate)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuickWeekNumberColumnPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberColumn.setDelegate' has no cute function yet. "
        "Qt's 'void QQuickWeekNumberColumn::setDelegate(QQmlComponent "
        "*delegate)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QQuickWeekNumberColumnPrivate'.")

  @staticmethod
  def setMonth(*__, **_) -> Never:
    """
    Qt's 'void QQuickWeekNumberColumn::setMonth(int month)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type
    'QQuickWeekNumberColumnPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberColumn.setMonth' has no cute function yet. Qt's "
        "'void QQuickWeekNumberColumn::setMonth(int month)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QQuickWeekNumberColumnPrivate'.")

  @staticmethod
  def setSource(*__, **_) -> Never:
    """
    Qt's 'void QQuickWeekNumberColumn::setSource(const QVariant &source)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuickWeekNumberColumnPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberColumn.setSource' has no cute function yet. Qt's "
        "'void QQuickWeekNumberColumn::setSource(const QVariant &source)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QQuickWeekNumberColumnPrivate'.")

  @staticmethod
  def setYear(*__, **_) -> Never:
    """
    Qt's 'void QQuickWeekNumberColumn::setYear(int year)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type
    'QQuickWeekNumberColumnPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberColumn.setYear' has no cute function yet. Qt's "
        "'void QQuickWeekNumberColumn::setYear(int year)': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QQuickWeekNumberColumnPrivate'.")

  @staticmethod
  def source(*__, **_) -> Never:
    """
    Qt's 'QVariant QQuickWeekNumberColumn::source() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'const
    QQuickWeekNumberColumnPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberColumn.source' has no cute function yet. Qt's "
        "'QVariant QQuickWeekNumberColumn::source() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type 'const "
        "QQuickWeekNumberColumnPrivate'.")

  @staticmethod
  def year(*__, **_) -> Never:
    """
    Qt's 'int QQuickWeekNumberColumn::year() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuickWeekNumberColumnPrivate'.
    """
    raise NotImplementedError(
        "'QQuickWeekNumberColumn.year' has no cute function yet. Qt's 'int "
        "QQuickWeekNumberColumn::year() const': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type 'const "
        "QQuickWeekNumberColumnPrivate'.")
