"""
QQuickIcon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickicon_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickIcon to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QObject, QUrl
  from ..QtGui import QColor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QObject = WAIT['QObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickIcon(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickIcon: a plain Python object standing in front
  of one C++ QQuickIcon.

  C++ hands a QQuickIcon around as a copy, so every C++ QQuickIcon behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQuickIcon that has a ritual and that Python can
  call so far, 25 names in all: '__eq__', '__ne__', 'isEmpty', 'name',
  'setName', 'resetName', 'source', 'setSource', 'resetSource',
  'resolvedSource', 'ensureRelativeSourceResolved', 'width', 'setWidth',
  'resetWidth', 'height', 'setHeight', 'resetHeight', 'color', 'setColor',
  'resetColor', 'resolveColor', 'cache', 'setCache', 'resetCache', 'resolve'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QQuickIcon::qt_qmlMarker_anonymous()': one of Qt's own inner
    workings.
  - Qt's 'QQuickIcon::~QQuickIcon()': the destructor: Python removes its C++
    QQuickIcon by it, and has no other use for it.
  - Qt's 'QQuickIcon &QQuickIcon::operator=(const QQuickIcon &other)':
    assignment: Python binds a name and has no operator for it.

  What has no ritual
  ------------------

  3 of the 33 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QQuickIcon is created at the first use, not by 'QQuickIcon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuickIcon back gives a copy the ritual made for
    Python, in a new cute QQuickIcon.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickIcon'

  #  Qt's '~QQuickIcon()'. Naming it makes this a value class: Python owns
  #  every C++ QQuickIcon behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QQuickIconD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QQuickIcon::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#isEmpty
    """
    #  bool QQuickIcon::isEmpty() const
    return self.uglySide.call('ritual_ZNK10QQuickIcon7isEmptyEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QQuickIcon::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickIcon::name() const
    return self.uglySide.call('ritual_ZNK10QQuickIcon4nameEv')

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickIcon::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickIcon::source() const
    address = self.uglySide.call('ritual_ZNK10QQuickIcon6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def resolvedSource(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickIcon::resolvedSource() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#resolvedSource

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickIcon::resolvedSource() const
    address = self.uglySide.call('ritual_ZNK10QQuickIcon14resolvedSourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def width(self) -> int:
    """
    Calls Qt's 'int QQuickIcon::width() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#width
    """
    #  int QQuickIcon::width() const
    return self.uglySide.call('ritual_ZNK10QQuickIcon5widthEv')

  def height(self) -> int:
    """
    Calls Qt's 'int QQuickIcon::height() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#height
    """
    #  int QQuickIcon::height() const
    return self.uglySide.call('ritual_ZNK10QQuickIcon6heightEv')

  def color(self) -> QColor:
    """
    Calls Qt's 'QColor QQuickIcon::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QQuickIcon::color() const
    address = self.uglySide.call('ritual_ZNK10QQuickIcon5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def cache(self) -> bool:
    """
    Calls Qt's 'bool QQuickIcon::cache() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#cache
    """
    #  bool QQuickIcon::cache() const
    return self.uglySide.call('ritual_ZNK10QQuickIcon5cacheEv')

  @overload(THIS)
  def resolve(self, other: QQuickIcon) -> QQuickIcon:
    """
    Calls Qt's 'QQuickIcon QQuickIcon::resolve(const QQuickIcon &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#resolve

    Parameters
    ----------

    other : QQuickIcon
      Passed on as a value: Qt reads the C++ QQuickIcon, which stays Python's
      own.

    Returns
    -------

    QQuickIcon
      A new cute QQuickIcon around the copy Qt gave back. Python owns it.
    """
    #  QQuickIcon QQuickIcon::resolve(const QQuickIcon &other) const
    address = self.uglySide.call(
        'ritual_ZNK10QQuickIcon7resolveERKS_', self._valueOf(other),
    )
    return QQuickIcon._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QQuickIcon::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickIcon::setName(const QString &name)
    self.uglySide.call('ritual_ZN10QQuickIcon7setNameERK7QString', name)

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuickIcon::setSource(const QUrl &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickIcon::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN10QQuickIcon9setSourceERK4QUrl', self._valueOf(source),
    )

  @overload(int)
  def setWidth(self, width: int) -> None:
    """
    Calls Qt's 'void QQuickIcon::setWidth(int width)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#setWidth

    Parameters
    ----------

    width : int
      Passed on as it is.
    """
    #  void QQuickIcon::setWidth(int width)
    self.uglySide.call('ritual_ZN10QQuickIcon8setWidthEi', width)

  @overload(int)
  def setHeight(self, height: int) -> None:
    """
    Calls Qt's 'void QQuickIcon::setHeight(int height)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#setHeight

    Parameters
    ----------

    height : int
      Passed on as it is.
    """
    #  void QQuickIcon::setHeight(int height)
    self.uglySide.call('ritual_ZN10QQuickIcon9setHeightEi', height)

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QQuickIcon::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QQuickIcon::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN10QQuickIcon8setColorERK6QColor', self._valueOf(color),
    )

  @overload(bool)
  def setCache(self, cache: bool) -> None:
    """
    Calls Qt's 'void QQuickIcon::setCache(bool cache)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#setCache

    Parameters
    ----------

    cache : bool
      Passed on as it is.
    """
    #  void QQuickIcon::setCache(bool cache)
    self.uglySide.call('ritual_ZN10QQuickIcon8setCacheEb', cache)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QQuickIcon) -> bool:
    """
    Calls Qt's 'bool QQuickIcon::operator==(const QQuickIcon &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#operator==

    Parameters
    ----------

    other : QQuickIcon
      Passed on as a value: Qt reads the C++ QQuickIcon, which stays Python's
      own.
    """
    #  bool QQuickIcon::operator==(const QQuickIcon &other) const
    return self.uglySide.call(
        'ritual_ZNK10QQuickIconeqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QQuickIcon) -> bool:
    """
    Calls Qt's 'bool QQuickIcon::operator!=(const QQuickIcon &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#operator!=

    Parameters
    ----------

    other : QQuickIcon
      Passed on as a value: Qt reads the C++ QQuickIcon, which stays Python's
      own.
    """
    #  bool QQuickIcon::operator!=(const QQuickIcon &other) const
    return self.uglySide.call(
        'ritual_ZNK10QQuickIconneERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QQuickIcon::QQuickIcon()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#QQuickIcon
    """
    #  QQuickIcon::QQuickIcon()
    self._noteCreation(QQuickIcon, lambda: Rituals.call(
        'ritual_ZN10QQuickIconC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QQuickIcon) -> None:
    """
    Notes what was given, for Qt's 'QQuickIcon::QQuickIcon(const QQuickIcon
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#QQuickIcon

    Parameters
    ----------

    other : QQuickIcon
      Passed on as a value: Qt reads the C++ QQuickIcon, which stays Python's
      own.
    """
    #  QQuickIcon::QQuickIcon(const QQuickIcon &other)
    self._noteCreation(QQuickIcon, lambda: Rituals.call(
        'ritual_ZN10QQuickIconC1ERKS_', self._valueOf(other),
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

  def resetName(self) -> None:
    """
    Calls Qt's 'void QQuickIcon::resetName()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#resetName
    """
    #  void QQuickIcon::resetName()
    self.uglySide.call('ritual_ZN10QQuickIcon9resetNameEv')

  def resetSource(self) -> None:
    """
    Calls Qt's 'void QQuickIcon::resetSource()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#resetSource
    """
    #  void QQuickIcon::resetSource()
    self.uglySide.call('ritual_ZN10QQuickIcon11resetSourceEv')

  @overload(QObject)
  @overload(NoneType)
  def ensureRelativeSourceResolved(self, owner: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickIcon::ensureRelativeSourceResolved(const QObject
    *owner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickicon.html#ensureRelativeSourceResolved

    Parameters
    ----------

    owner : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickIcon::ensureRelativeSourceResolved(const QObject *owner)
    self.uglySide.call(
        'ritual_ZN10QQuickIcon28ensureRelativeSourceResolvedEPK7QObject',
        self._addressOf(owner, 'QObject'),
    )

  def resetWidth(self) -> None:
    """
    Calls Qt's 'void QQuickIcon::resetWidth()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#resetWidth
    """
    #  void QQuickIcon::resetWidth()
    self.uglySide.call('ritual_ZN10QQuickIcon10resetWidthEv')

  def resetHeight(self) -> None:
    """
    Calls Qt's 'void QQuickIcon::resetHeight()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#resetHeight
    """
    #  void QQuickIcon::resetHeight()
    self.uglySide.call('ritual_ZN10QQuickIcon11resetHeightEv')

  def resetColor(self) -> None:
    """
    Calls Qt's 'void QQuickIcon::resetColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#resetColor
    """
    #  void QQuickIcon::resetColor()
    self.uglySide.call('ritual_ZN10QQuickIcon10resetColorEv')

  def resolveColor(self) -> None:
    """
    Calls Qt's 'void QQuickIcon::resolveColor()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#resolveColor
    """
    #  void QQuickIcon::resolveColor()
    self.uglySide.call('ritual_ZN10QQuickIcon12resolveColorEv')

  def resetCache(self) -> None:
    """
    Calls Qt's 'void QQuickIcon::resetCache()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickicon.html#resetCache
    """
    #  void QQuickIcon::resetCache()
    self.uglySide.call('ritual_ZN10QQuickIcon10resetCacheEv')
