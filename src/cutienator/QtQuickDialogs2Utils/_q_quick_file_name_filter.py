"""
QQuickFileNameFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickDialogs2Utils/6.12.0/QtQuickDialogs2Utils/private/qquickfilenamefilter_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickFileNameFilter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFileNameFilter(QObject):
  """
  The cute side of Qt's QQuickFileNameFilter: a plain Python object standing
  in front of one C++ QQuickFileNameFilter.

  It is built on the cute 'QObject', as Qt's QQuickFileNameFilter is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFileNameFilter that has a ritual and that
  Python can call so far, 14 names in all: 'metaObject', 'tr', 'index',
  'setIndex', 'name', 'extensions', 'globs', 'update', 'indexChanged',
  'nameChanged', 'extensionsChanged', 'globsChanged', 'nameFilters',
  'nameFilter'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFileNameFilter::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickFileNameFilter::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSharedPointer<QFileDialogOptions> QQuickFileNameFilter::options()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QQuickFileNameFilter::setOptions(const
    QSharedPointer<QFileDialogOptions> &options)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  2 of the 21 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFileNameFilter is created at the first use, not by
    'QQuickFileNameFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFileNameFilter.
  - Qt tells when it has removed the C++ QQuickFileNameFilter. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickFileNameFilter that has no cute function yet,
    'options', 'setOptions', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickFileNameFilter::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfilenamefilter.html#tr

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
    #  QString QQuickFileNameFilter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickFileNameFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFileNameFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFileNameFilter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfilenamefilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFileNameFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickFileNameFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def index(self) -> int:
    """
    Calls Qt's 'int QQuickFileNameFilter::index() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfilenamefilter.html#index
    """
    #  int QQuickFileNameFilter::index() const
    return self.uglySide.call('ritual_ZNK20QQuickFileNameFilter5indexEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickFileNameFilter::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfilenamefilter.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFileNameFilter::name() const
    return self.uglySide.call('ritual_ZNK20QQuickFileNameFilter4nameEv')

  def extensions(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickFileNameFilter::extensions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfilenamefilter.html#extensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickFileNameFilter::extensions() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickFileNameFilter10extensionsEv',
    )
    return QStringList._cuteOwning(address)

  def globs(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickFileNameFilter::globs() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfilenamefilter.html#globs

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickFileNameFilter::globs() const
    address = self.uglySide.call('ritual_ZNK20QQuickFileNameFilter5globsEv')
    return QStringList._cuteOwning(address)

  def nameFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickFileNameFilter::nameFilters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfilenamefilter.html#nameFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickFileNameFilter::nameFilters() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickFileNameFilter11nameFiltersEv',
    )
    return QStringList._cuteOwning(address)

  @overload(int)
  def nameFilter(self, index: int) -> str:
    """
    Calls Qt's 'QString QQuickFileNameFilter::nameFilter(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfilenamefilter.html#nameFilter

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFileNameFilter::nameFilter(int index) const
    return self.uglySide.call(
        'ritual_ZNK20QQuickFileNameFilter10nameFilterEi', index,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickFileNameFilter::setIndex(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfilenamefilter.html#setIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickFileNameFilter::setIndex(int index)
    self.uglySide.call('ritual_ZN20QQuickFileNameFilter8setIndexEi', index)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickFileNameFilter::QQuickFileNameFilter(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfilenamefilter.html#QQuickFileNameFilter

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFileNameFilter::QQuickFileNameFilter(QObject *parent)
    self._noteCreation(QQuickFileNameFilter, lambda: Rituals.call(
        'ritual_ZN20QQuickFileNameFilterC1EP7QObject',
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

  @overload(str)
  def update(self, filter: str) -> None:
    """
    Calls Qt's 'void QQuickFileNameFilter::update(const QString &filter)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickfilenamefilter.html#update

    Parameters
    ----------

    filter : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFileNameFilter::update(const QString &filter)
    self.uglySide.call(
        'ritual_ZN20QQuickFileNameFilter6updateERK7QString', filter,
    )

  @overload(int)
  def indexChanged(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickFileNameFilter::indexChanged(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfilenamefilter.html#indexChanged

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickFileNameFilter::indexChanged(int index)
    self.uglySide.call(
        'ritual_ZN20QQuickFileNameFilter12indexChangedEi', index,
    )

  @overload(str)
  def nameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickFileNameFilter::nameChanged(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfilenamefilter.html#nameChanged

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickFileNameFilter::nameChanged(const QString &name)
    self.uglySide.call(
        'ritual_ZN20QQuickFileNameFilter11nameChangedERK7QString', name,
    )

  @overload(QStringList)
  def extensionsChanged(self, extensions: QStringList) -> None:
    """
    Calls Qt's 'void QQuickFileNameFilter::extensionsChanged(const
    QStringList &extensions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfilenamefilter.html#extensionsChanged

    Parameters
    ----------

    extensions : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickFileNameFilter::extensionsChanged(const QStringList
    #      &extensions)
    self.uglySide.call(
        'ritual_ZN20QQuickFileNameFilter17extensionsChangedERK5QListI7QStri'
        'ngE',
        self._valueOf(extensions),
    )

  @overload(QStringList)
  def globsChanged(self, globs: QStringList) -> None:
    """
    Calls Qt's 'void QQuickFileNameFilter::globsChanged(const QStringList
    &globs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickfilenamefilter.html#globsChanged

    Parameters
    ----------

    globs : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickFileNameFilter::globsChanged(const QStringList &globs)
    self.uglySide.call(
        'ritual_ZN20QQuickFileNameFilter12globsChangedERK5QListI7QStringE',
        self._valueOf(globs),
    )

  @staticmethod
  def options(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QFileDialogOptions> QQuickFileNameFilter::options()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickFileNameFilter.options' has no cute function yet. Qt's "
        "'QSharedPointer<QFileDialogOptions> "
        "QQuickFileNameFilter::options() const': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QQuickFileNameFilter::setOptions(const
    QSharedPointer<QFileDialogOptions> &options)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickFileNameFilter.setOptions' has no cute function yet. Qt's "
        "'void QQuickFileNameFilter::setOptions(const "
        "QSharedPointer<QFileDialogOptions> &options)': takes a type Python "
        "has no way to hand over yet.")
