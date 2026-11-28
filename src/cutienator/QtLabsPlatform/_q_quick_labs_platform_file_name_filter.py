"""
QQuickLabsPlatformFileNameFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qquicklabsplatformfiledialog_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickLabsPlatformFileNameFilter to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..QtCore import QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject


class QQuickLabsPlatformFileNameFilter(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLabsPlatformFileNameFilter: a plain Python
  object standing in front of one C++ QQuickLabsPlatformFileNameFilter.

  What exists
  -----------

  Every function of Qt's QQuickLabsPlatformFileNameFilter that has a ritual
  and that Python can call so far, 8 names in all: 'metaObject', 'index',
  'name', 'extensions', 'nameChanged', 'extensionsChanged', 'nameFilters',
  'nameFilter'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLabsPlatformFileNameFilter::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuickLabsPlatformFileNameFilter::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickLabsPlatformFileNameFilter::qt_qmlMarker_anonymous()':
    one of Qt's own inner workings.
  - Qt's 'QSharedPointer<QFileDialogOptions>
    QQuickLabsPlatformFileNameFilter::options() const': gives a type Python
    has no way to take yet.
  - Qt's 'void QQuickLabsPlatformFileNameFilter::setOptions(const
    QSharedPointer<QFileDialogOptions> &options)': takes a type Python has no
    way to hand over yet.

  What has no ritual
  ------------------

  7 of the 20 functions Qt declares: 3 leans on
  'QQuickLabsPlatformFileNameFilter; 2 not a gap; 1 the compiler refuses its
  ritual as it would be written here; 1 leans on 'vtable for
  QQuickLabsPlatformFileNameFilter', which Qt's source does not mark for use
  from outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickLabsPlatformFileNameFilter is created at the first use, not
    by 'QQuickLabsPlatformFileNameFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLabsPlatformFileNameFilter.
  - Qt tells when it has removed the C++ QQuickLabsPlatformFileNameFilter.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLabsPlatformFileNameFilter that has no cute
    function yet, '__init__', 'indexChanged', 'options', 'setIndex',
    'setOptions', 'update', holds a function that raises
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
  __qt_class__ = 'QQuickLabsPlatformFileNameFilter'

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
    *QQuickLabsPlatformFileNameFilter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfilenamefilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLabsPlatformFileNameFilter::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformFileNameFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def index(self) -> int:
    """
    Calls Qt's 'int QQuickLabsPlatformFileNameFilter::index() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfilenamefilter.html#index
    """
    #  int QQuickLabsPlatformFileNameFilter::index() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformFileNameFilter5indexEv',
    )

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformFileNameFilter::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfilenamefilter.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformFileNameFilter::name() const
    return self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformFileNameFilter4nameEv',
    )

  def extensions(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickLabsPlatformFileNameFilter::extensions()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfilenamefilter.html#extensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickLabsPlatformFileNameFilter::extensions() const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformFileNameFilter10extensionsEv',
    )
    return QStringList._cuteOwning(address)

  def nameFilters(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickLabsPlatformFileNameFilter::nameFilters()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfilenamefilter.html#nameFilters

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickLabsPlatformFileNameFilter::nameFilters() const
    address = self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformFileNameFilter11nameFiltersEv',
    )
    return QStringList._cuteOwning(address)

  @overload(int)
  def nameFilter(self, index: int) -> str:
    """
    Calls Qt's 'QString QQuickLabsPlatformFileNameFilter::nameFilter(int
    index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfilenamefilter.html#nameFilter

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickLabsPlatformFileNameFilter::nameFilter(int index) const
    return self.uglySide.call(
        'ritual_ZNK32QQuickLabsPlatformFileNameFilter10nameFilterEi', index,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickLabsPlatformFileNameFilter::QQuickLabsPlatformFileNameFilter(
    QObject *parent)': leans on 'vtable for
    QQuickLabsPlatformFileNameFilter', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileNameFilter.__init__' has no cute function "
        "yet. Qt's "
        "'QQuickLabsPlatformFileNameFilter::QQuickLabsPlatformFileNameFilter"
        "(QObject *parent)': leans on 'vtable for "
        "QQuickLabsPlatformFileNameFilter', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

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
  def nameChanged(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickLabsPlatformFileNameFilter::nameChanged(const
    QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfilenamefilter.html#nameChanged

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickLabsPlatformFileNameFilter::nameChanged(const QString
    #      &name)
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformFileNameFilter11nameChangedERK7QStrin'
        'g',
        name,
    )

  @overload(QStringList)
  def extensionsChanged(self, extensions: QStringList) -> None:
    """
    Calls Qt's 'void
    QQuickLabsPlatformFileNameFilter::extensionsChanged(const QStringList
    &extensions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklabsplatformfilenamefilter.html

    Parameters
    ----------

    extensions : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickLabsPlatformFileNameFilter::extensionsChanged(const
    #      QStringList &extensions)
    self.uglySide.call(
        'ritual_ZN32QQuickLabsPlatformFileNameFilter17extensionsChangedERK5'
        'QListI7QStringE',
        self._valueOf(extensions),
    )

  @staticmethod
  def indexChanged(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileNameFilter::indexChanged(int index)':
    the compiler refuses its ritual as it would be written here: redefinition
    of 'index' with a different type: 'const int' vs 'int'.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileNameFilter.indexChanged' has no cute "
        "function yet. Qt's 'void "
        "QQuickLabsPlatformFileNameFilter::indexChanged(int index)': the "
        "compiler refuses its ritual as it would be written here: "
        "redefinition of 'index' with a different type: 'const int' vs "
        "'int'.")

  @staticmethod
  def options(*__, **_) -> Never:
    """
    Qt's 'QSharedPointer<QFileDialogOptions>
    QQuickLabsPlatformFileNameFilter::options() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileNameFilter.options' has no cute function "
        "yet. Qt's 'QSharedPointer<QFileDialogOptions> "
        "QQuickLabsPlatformFileNameFilter::options() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def setIndex(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileNameFilter::setIndex(int index)': leans
    on 'QQuickLabsPlatformFileNameFilter::indexChanged(int)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileNameFilter.setIndex' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformFileNameFilter::setIndex(int "
        "index)': leans on "
        "'QQuickLabsPlatformFileNameFilter::indexChanged(int)', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setOptions(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileNameFilter::setOptions(const
    QSharedPointer<QFileDialogOptions> &options)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileNameFilter.setOptions' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformFileNameFilter::setOptions(const "
        "QSharedPointer<QFileDialogOptions> &options)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def update(*__, **_) -> Never:
    """
    Qt's 'void QQuickLabsPlatformFileNameFilter::update(const QString
    &filter)': leans on
    'QQuickLabsPlatformFileNameFilter::nameChanged(QString const&)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickLabsPlatformFileNameFilter.update' has no cute function "
        "yet. Qt's 'void QQuickLabsPlatformFileNameFilter::update(const "
        "QString &filter)': leans on "
        "'QQuickLabsPlatformFileNameFilter::nameChanged(QString const&)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
