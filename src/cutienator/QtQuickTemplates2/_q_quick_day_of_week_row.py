"""
QQuickDayOfWeekRow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdayofweekrow_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickDayOfWeekRow to be private: it declares the class in a
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


class QQuickDayOfWeekRow(QQuickControl):
  """
  The cute side of Qt's QQuickDayOfWeekRow: a plain Python object standing in
  front of one C++ QQuickDayOfWeekRow.

  It is built on the cute 'QQuickControl', as Qt's QQuickDayOfWeekRow is
  built on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDayOfWeekRow that has a ritual and that Python
  can call so far, 7 names in all: 'metaObject', 'sourceChanged',
  'delegateChanged', 'componentComplete', 'geometryChange', 'localeChange',
  'paddingChange'. None can be made from Python: one comes out of a function
  of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDayOfWeekRow::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickDayOfWeekRow::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickDayOfWeekRowPrivate *QQuickDayOfWeekRow::d_func()': gives
    'QQuickDayOfWeekRowPrivate', which has no cute class yet.
  - Qt's 'const QQuickDayOfWeekRowPrivate *QQuickDayOfWeekRow::d_func()
    const': gives 'QQuickDayOfWeekRowPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  10 of the 21 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 forbidden; 1 leans on 'QQuickDayOfWeekRow.

  What to expect
  --------------

  - The C++ QQuickDayOfWeekRow is created at the first use, not by
    'QQuickDayOfWeekRow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDayOfWeekRow.
  - Qt tells when it has removed the C++ QQuickDayOfWeekRow. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickDayOfWeekRow that has no cute function yet,
    '__init__', 'delegate', 'setDelegate', 'setSource', 'source', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDayOfWeekRow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDayOfWeekRow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdayofweekrow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDayOfWeekRow::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickDayOfWeekRow10metaObjectEv',
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
    Qt's 'QQuickDayOfWeekRow::QQuickDayOfWeekRow(QQuickItem *parent)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickDayOfWeekRowPrivate'.
    """
    raise NotImplementedError(
        "'QQuickDayOfWeekRow.__init__' has no cute function yet. Qt's "
        "'QQuickDayOfWeekRow::QQuickDayOfWeekRow(QQuickItem *parent)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QQuickDayOfWeekRowPrivate'.")

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

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDayOfWeekRow::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdayofweekrow.html#sourceChanged
    """
    #  void QQuickDayOfWeekRow::sourceChanged()
    self.uglySide.call('ritual_ZN18QQuickDayOfWeekRow13sourceChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickDayOfWeekRow::delegateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdayofweekrow.html#delegateChanged
    """
    #  void QQuickDayOfWeekRow::delegateChanged()
    self.uglySide.call('ritual_ZN18QQuickDayOfWeekRow15delegateChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickDayOfWeekRow::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdayofweekrow.html#componentComplete
    """
    #  void QQuickDayOfWeekRow::componentComplete()
    ritual = 'ritual_ZN18QQuickDayOfWeekRow17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickDayOfWeekRow17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickDayOfWeekRow::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdayofweekrow.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickDayOfWeekRow::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN18QQuickDayOfWeekRow14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickDayOfWeekRow14geometryChangeERK6QRectFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QLocale, QLocale)
  def localeChange(self, newLocale: QLocale, oldLocale: QLocale) -> None:
    """
    Calls Qt's 'void QQuickDayOfWeekRow::localeChange(const QLocale
    &newLocale, const QLocale &oldLocale)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdayofweekrow.html#localeChange

    Parameters
    ----------

    newLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    oldLocale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QQuickDayOfWeekRow::localeChange(const QLocale &newLocale, const
    #      QLocale &oldLocale)
    self.uglySide.call(
        'ritual_ZN18QQuickDayOfWeekRow12localeChangeERK7QLocaleS2_',
        self._valueOf(newLocale), self._valueOf(oldLocale),
    )

  @overload(QMarginsF, QMarginsF)
  def paddingChange(
      self,
      newPadding: QMarginsF,
      oldPadding: QMarginsF,
  ) -> None:
    """
    Calls Qt's 'void QQuickDayOfWeekRow::paddingChange(const QMarginsF
    &newPadding, const QMarginsF &oldPadding)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdayofweekrow.html#paddingChange

    Parameters
    ----------

    newPadding : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.

    oldPadding : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickDayOfWeekRow::paddingChange(const QMarginsF &newPadding,
    #      const QMarginsF &oldPadding)
    ritual = 'ritual_ZN18QQuickDayOfWeekRow13paddingChangeERK9QMarginsFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QQuickDayOfWeekRow13paddingChangeERK9QMarginsFS2_')
    self.uglySide.call(
        ritual, self._valueOf(newPadding), self._valueOf(oldPadding),
    )

  @staticmethod
  def delegate(*__, **_) -> Never:
    """
    Qt's 'QQmlComponent *QQuickDayOfWeekRow::delegate() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'const
    QQuickDayOfWeekRowPrivate'.
    """
    raise NotImplementedError(
        "'QQuickDayOfWeekRow.delegate' has no cute function yet. Qt's "
        "'QQmlComponent *QQuickDayOfWeekRow::delegate() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuickDayOfWeekRowPrivate'.")

  @staticmethod
  def setDelegate(*__, **_) -> Never:
    """
    Qt's 'void QQuickDayOfWeekRow::setDelegate(QQmlComponent *delegate)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuickDayOfWeekRowPrivate'.
    """
    raise NotImplementedError(
        "'QQuickDayOfWeekRow.setDelegate' has no cute function yet. Qt's "
        "'void QQuickDayOfWeekRow::setDelegate(QQmlComponent *delegate)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QQuickDayOfWeekRowPrivate'.")

  @staticmethod
  def setSource(*__, **_) -> Never:
    """
    Qt's 'void QQuickDayOfWeekRow::setSource(const QVariant &source)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuickDayOfWeekRowPrivate'.
    """
    raise NotImplementedError(
        "'QQuickDayOfWeekRow.setSource' has no cute function yet. Qt's "
        "'void QQuickDayOfWeekRow::setSource(const QVariant &source)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QQuickDayOfWeekRowPrivate'.")

  @staticmethod
  def source(*__, **_) -> Never:
    """
    Qt's 'QVariant QQuickDayOfWeekRow::source() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const
    QQuickDayOfWeekRowPrivate'.
    """
    raise NotImplementedError(
        "'QQuickDayOfWeekRow.source' has no cute function yet. Qt's "
        "'QVariant QQuickDayOfWeekRow::source() const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuickDayOfWeekRowPrivate'.")
