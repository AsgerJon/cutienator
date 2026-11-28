"""
QQuickImageSelector binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickimageselector_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickImageSelector to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObject, QStringList
from ..QtQml import QQmlParserStatus, QQmlPropertyValueInterceptor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl, QVariant
  from ..QtQml import QQmlProperty
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlProperty = WAIT['QQmlProperty']
  QVariant = WAIT['QVariant']


class QQuickImageSelector(QObject, QQmlParserStatus, QQmlPropertyValueInterceptor):
  """
  The cute side of Qt's QQuickImageSelector: a plain Python object standing
  in front of one C++ QQuickImageSelector.

  It is built on the cute 'QObject', as Qt's QQuickImageSelector is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickImageSelector is built on Qt's
  QQmlParserStatus too, and has everything that class has. It is built on the
  cute 'QQmlPropertyValueInterceptor' as well, as Qt's QQuickImageSelector is
  built on Qt's QQmlPropertyValueInterceptor too, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's QQuickImageSelector that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'source', 'name',
  'path', 'states', 'separator', 'cache', 'setCache', 'write', 'setTarget',
  'sourceChanged', 'classBegin', 'componentComplete', 'fileExtensions',
  'cacheKey', 'updateActiveStates', 'calculateScore'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickImageSelector::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickImageSelector::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  11 of the 30 functions Qt declares: 7 leans on 'QQuickImageSelector; 2 not
  a gap; 1 Qt's library has no name for it, and its code in Qt's source does
  not compile apart from its file; 1 leans on 'vtable for
  QQuickImageSelector', which Qt's source does not mark for use from outside
  Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuickImageSelector is created at the first use, not by
    'QQuickImageSelector(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickImageSelector.
  - Qt tells when it has removed the C++ QQuickImageSelector. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickImageSelector that has no cute function yet,
    '__init__', 'setName', 'setPath', 'setSeparator', 'setSource',
    'setStates', 'setUrl', 'updateSource', holds a function that raises
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
  __qt_class__ = 'QQuickImageSelector'

  #  Qt's QQuickImageSelector is built on more than one class. The part of a
  #  C++ QQuickImageSelector that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuickImageSelector_QQmlParserStatus',
      'QQmlPropertyValueInterceptor':
          'ritual_cast_QQuickImageSelector_QQmlPropertyValueInterceptor',
  }

  #  The functions Qt calls itself that QQuickImageSelector is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'fileExtensions': (
          'QStringList QQuickImageSelector::fileExtensions() const',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickImageSelector::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageselector.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickImageSelector::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickImageSelector10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickImageSelector::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageselector.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickImageSelector::source() const
    address = self.uglySide.call('ritual_ZNK19QQuickImageSelector6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickImageSelector::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageselector.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickImageSelector::name() const
    return self.uglySide.call('ritual_ZNK19QQuickImageSelector4nameEv')

  def path(self) -> str:
    """
    Calls Qt's 'QString QQuickImageSelector::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageselector.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickImageSelector::path() const
    return self.uglySide.call('ritual_ZNK19QQuickImageSelector4pathEv')

  def states(self) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList QQuickImageSelector::states() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageselector.html#states

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QQuickImageSelector::states() const
    address = self.uglySide.call('ritual_ZNK19QQuickImageSelector6statesEv')
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  def separator(self) -> str:
    """
    Calls Qt's 'QString QQuickImageSelector::separator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageselector.html#separator

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickImageSelector::separator() const
    return self.uglySide.call('ritual_ZNK19QQuickImageSelector9separatorEv')

  def cache(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageSelector::cache() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageselector.html#cache
    """
    #  bool QQuickImageSelector::cache() const
    return self.uglySide.call('ritual_ZNK19QQuickImageSelector5cacheEv')

  def fileExtensions(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickImageSelector::fileExtensions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageselector.html#fileExtensions

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickImageSelector::fileExtensions() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickImageSelector14fileExtensionsEv',
    )
    return QStringList._cuteOwning(address)

  def cacheKey(self) -> str:
    """
    Calls Qt's 'QString QQuickImageSelector::cacheKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageselector.html#cacheKey

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickImageSelector::cacheKey() const
    return self.uglySide.call('ritual_ZNK19QQuickImageSelector8cacheKeyEv')

  @overload(QStringList)
  def calculateScore(self, states: QStringList) -> int:
    """
    Calls Qt's 'int QQuickImageSelector::calculateScore(const QStringList
    &states) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageselector.html#calculateScore

    Parameters
    ----------

    states : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  int QQuickImageSelector::calculateScore(const QStringList &states)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QQuickImageSelector14calculateScoreERK5QListI7QStringE',
        self._valueOf(states),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setCache(self, cache: bool) -> None:
    """
    Calls Qt's 'void QQuickImageSelector::setCache(bool cache)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageselector.html#setCache

    Parameters
    ----------

    cache : bool
      Passed on as it is.
    """
    #  void QQuickImageSelector::setCache(bool cache)
    self.uglySide.call('ritual_ZN19QQuickImageSelector8setCacheEb', cache)

  @overload(QQmlProperty)
  def setTarget(self, property: QQmlProperty) -> None:
    """
    Calls Qt's 'void QQuickImageSelector::setTarget(const QQmlProperty
    &property)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageselector.html#setTarget

    Parameters
    ----------

    property : QQmlProperty
      Passed on as a value: Qt reads the C++ QQmlProperty, which stays
      Python's own.
    """
    #  void QQuickImageSelector::setTarget(const QQmlProperty &property)
    ritual = 'ritual_ZN19QQuickImageSelector9setTargetERK12QQmlProperty'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN19QQuickImageSelector9setTargetERK12QQmlProperty')
    self.uglySide.call(ritual, self._valueOf(property))

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
    Qt's 'QQuickImageSelector::QQuickImageSelector(QObject *parent)': leans
    on 'vtable for QQuickImageSelector', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickImageSelector.__init__' has no cute function yet. Qt's "
        "'QQuickImageSelector::QQuickImageSelector(QObject *parent)': leans "
        "on 'vtable for QQuickImageSelector', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

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

  @overload(QVariant)
  def write(self, value: QVariant) -> None:
    """
    Calls Qt's 'void QQuickImageSelector::write(const QVariant &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickimageselector.html#write

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuickImageSelector::write(const QVariant &value)
    self.uglySide.call(
        'ritual_ZN19QQuickImageSelector5writeERK8QVariant',
        self._valueOf(value),
    )

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuickImageSelector::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageselector.html#sourceChanged
    """
    #  void QQuickImageSelector::sourceChanged()
    self.uglySide.call('ritual_ZN19QQuickImageSelector13sourceChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickImageSelector::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageselector.html#classBegin
    """
    #  void QQuickImageSelector::classBegin()
    ritual = 'ritual_ZN19QQuickImageSelector10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickImageSelector10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickImageSelector::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageselector.html#componentComplete
    """
    #  void QQuickImageSelector::componentComplete()
    self.uglySide.call('ritual_ZN19QQuickImageSelector17componentCompleteEv')

  def updateActiveStates(self) -> bool:
    """
    Calls Qt's 'bool QQuickImageSelector::updateActiveStates()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickimageselector.html#updateActiveStates
    """
    #  bool QQuickImageSelector::updateActiveStates()
    return self.uglySide.call(
        'ritual_ZN19QQuickImageSelector18updateActiveStatesEv',
    )

  @staticmethod
  def setName(*__, **_) -> Never:
    """
    Qt's 'void QQuickImageSelector::setName(const QString &name)': leans on
    'QQuickImageSelector::updateSource()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickImageSelector.setName' has no cute function yet. Qt's 'void "
        "QQuickImageSelector::setName(const QString &name)': leans on "
        "'QQuickImageSelector::updateSource()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setPath(*__, **_) -> Never:
    """
    Qt's 'void QQuickImageSelector::setPath(const QString &path)': leans on
    'QQuickImageSelector::updateSource()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickImageSelector.setPath' has no cute function yet. Qt's 'void "
        "QQuickImageSelector::setPath(const QString &path)': leans on "
        "'QQuickImageSelector::updateSource()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setSeparator(*__, **_) -> Never:
    """
    Qt's 'void QQuickImageSelector::setSeparator(const QString &separator)':
    leans on 'QQuickImageSelector::updateSource()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickImageSelector.setSeparator' has no cute function yet. Qt's "
        "'void QQuickImageSelector::setSeparator(const QString "
        "&separator)': leans on 'QQuickImageSelector::updateSource()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setSource(*__, **_) -> Never:
    """
    Qt's 'void QQuickImageSelector::setSource(const QUrl &source)': leans on
    'QQuickImageSelector::sourceChanged()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickImageSelector.setSource' has no cute function yet. Qt's "
        "'void QQuickImageSelector::setSource(const QUrl &source)': leans "
        "on 'QQuickImageSelector::sourceChanged()', which Qt's source does "
        "not mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setStates(*__, **_) -> Never:
    """
    Qt's 'void QQuickImageSelector::setStates(const QVariantList &states)':
    leans on 'QQuickImageSelector::updateSource()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickImageSelector.setStates' has no cute function yet. Qt's "
        "'void QQuickImageSelector::setStates(const QVariantList &states)': "
        "leans on 'QQuickImageSelector::updateSource()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def setUrl(*__, **_) -> Never:
    """
    Qt's 'void QQuickImageSelector::setUrl(const QUrl &url)': leans on
    'QQuickImageSelector::updateSource()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickImageSelector.setUrl' has no cute function yet. Qt's 'void "
        "QQuickImageSelector::setUrl(const QUrl &url)': leans on "
        "'QQuickImageSelector::updateSource()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def updateSource(*__, **_) -> Never:
    """
    Qt's 'void QQuickImageSelector::updateSource()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'cacheSize'.
    """
    raise NotImplementedError(
        "'QQuickImageSelector.updateSource' has no cute function yet. Qt's "
        "'void QQuickImageSelector::updateSource()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'cacheSize'.")
