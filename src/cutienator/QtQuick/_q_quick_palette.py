"""
QQuickPalette binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpalette_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickPalette to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QPalette
from . import QQuickColorGroup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickAbstractPaletteProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickAbstractPaletteProvider = WAIT['QQuickAbstractPaletteProvider']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPalette(QQuickColorGroup):
  """
  The cute side of Qt's QQuickPalette: a plain Python object standing in
  front of one C++ QQuickPalette.

  It is built on the cute 'QQuickColorGroup', as Qt's QQuickPalette is built
  on Qt's QQuickColorGroup, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPalette that has a ritual and that Python can
  call so far, 24 names in all: 'metaObject', 'tr', 'active', 'inactive',
  'disabled', 'resetActive', 'resetInactive', 'resetDisabled',
  'currentColorGroup', 'setCurrentGroup', 'fromQPalette', 'toQPalette',
  'paletteProvider', 'setPaletteProvider', 'reset', 'inheritPalette',
  'setActive', 'setInactive', 'setDisabled', 'activeChanged',
  'inactiveChanged', 'disabledChanged', 'registerColorGroup',
  'defaultCurrentGroup'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPalette::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickPalette::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickColorGroup::GroupPtr
    QQuickPalette::colorGroup(QPalette::ColorGroup groupTag) const': gives a
    type Python has no way to take yet.
  - Qt's 'QQuickColorGroup::GroupPtr
    QQuickPalette::findColorGroup(QPalette::ColorGroup groupTag) const':
    gives a type Python has no way to take yet.
  - Qt's 'bool QQuickPalette::isValidColorGroup(QPalette::ColorGroup
    groupTag, const QQuickColorGroup::GroupPtr &colorGroup) const': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  7 of the 37 functions Qt declares: 4 forbidden; 2 not a gap; 1 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QQuickPalette is created at the first use, not by
    'QQuickPalette(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPalette.
  - Qt tells when it has removed the C++ QQuickPalette. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickPalette that has no cute function yet,
    'colorGroup', 'findColorGroup', 'isValidColorGroup', 'setColorGroup',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
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
    Calls Qt's 'QString QQuickPalette::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#tr

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
    #  QString QQuickPalette::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QQuickPalette2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def defaultCurrentGroup() -> QPalette.ColorGroup:
    """
    Calls Qt's 'QPalette::ColorGroup QQuickPalette::defaultCurrentGroup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalette.html#defaultCurrentGroup

    Returns
    -------

    QPalette.ColorGroup
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPalette.ColorGroup(number)' gives.
    """
    #  QPalette::ColorGroup QQuickPalette::defaultCurrentGroup()
    return QPalette.ColorGroup(Rituals.call(
        'ritual_ZN13QQuickPalette19defaultCurrentGroupEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPalette'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPalette::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPalette::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QQuickPalette10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def active(self) -> Optional[QQuickColorGroup]:
    """
    Calls Qt's 'QQuickColorGroup *QQuickPalette::active() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#active

    Returns
    -------

    Optional[QQuickColorGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickColorGroup *QQuickPalette::active() const
    address = self.uglySide.call('ritual_ZNK13QQuickPalette6activeEv')
    return QQuickColorGroup._cuteAt(address)

  def inactive(self) -> Optional[QQuickColorGroup]:
    """
    Calls Qt's 'QQuickColorGroup *QQuickPalette::inactive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#inactive

    Returns
    -------

    Optional[QQuickColorGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickColorGroup *QQuickPalette::inactive() const
    address = self.uglySide.call('ritual_ZNK13QQuickPalette8inactiveEv')
    return QQuickColorGroup._cuteAt(address)

  def disabled(self) -> Optional[QQuickColorGroup]:
    """
    Calls Qt's 'QQuickColorGroup *QQuickPalette::disabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#disabled

    Returns
    -------

    Optional[QQuickColorGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickColorGroup *QQuickPalette::disabled() const
    address = self.uglySide.call('ritual_ZNK13QQuickPalette8disabledEv')
    return QQuickColorGroup._cuteAt(address)

  def currentColorGroup(self) -> QPalette.ColorGroup:
    """
    Calls Qt's 'QPalette::ColorGroup QQuickPalette::currentColorGroup()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalette.html#currentColorGroup

    Returns
    -------

    QPalette.ColorGroup
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QPalette.ColorGroup(number)' gives.
    """
    #  QPalette::ColorGroup QQuickPalette::currentColorGroup() const
    ritual = 'ritual_ZNK13QQuickPalette17currentColorGroupEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13QQuickPalette17currentColorGroupEv'
    return QPalette.ColorGroup(self.uglySide.call(ritual))

  def toQPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickPalette::toQPalette() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#toQPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickPalette::toQPalette() const
    address = self.uglySide.call('ritual_ZNK13QQuickPalette10toQPaletteEv')
    return QPalette._cuteOwning(address)

  def paletteProvider(self) -> Optional[QQuickAbstractPaletteProvider]:
    """
    Calls Qt's 'const QQuickAbstractPaletteProvider
    *QQuickPalette::paletteProvider() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#paletteProvider

    Returns
    -------

    Optional[QQuickAbstractPaletteProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQuickAbstractPaletteProvider *QQuickPalette::paletteProvider()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK13QQuickPalette15paletteProviderEv',
    )
    from . import QQuickAbstractPaletteProvider
    return QQuickAbstractPaletteProvider._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPalette.ColorGroup)
  def setCurrentGroup(self, currentGroup: QPalette.ColorGroup) -> None:
    """
    Calls Qt's 'void QQuickPalette::setCurrentGroup(QPalette::ColorGroup
    currentGroup)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#setCurrentGroup

    Parameters
    ----------

    currentGroup : QPalette.ColorGroup
      Passed on as its number.
    """
    #  void QQuickPalette::setCurrentGroup(QPalette::ColorGroup currentGroup)
    self.uglySide.call(
        'ritual_ZN13QQuickPalette15setCurrentGroupEN8QPalette10ColorGroupE',
        currentGroup.value,
    )

  @overload(QQuickAbstractPaletteProvider)
  @overload(NoneType)
  def setPaletteProvider(
      self,
      paletteProvider: Optional[QQuickAbstractPaletteProvider],
  ) -> None:
    """
    Calls Qt's 'void QQuickPalette::setPaletteProvider(const
    QQuickAbstractPaletteProvider *paletteProvider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalette.html#setPaletteProvider

    Parameters
    ----------

    paletteProvider : Optional[QQuickAbstractPaletteProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPalette::setPaletteProvider(const
    #      QQuickAbstractPaletteProvider *paletteProvider)
    self.uglySide.call(
        'ritual_ZN13QQuickPalette18setPaletteProviderEPK29QQuickAbstractPal'
        'etteProvider',
        self._addressOf(paletteProvider),
    )

  @overload(QQuickColorGroup)
  @overload(NoneType)
  def setActive(self, active: Optional[QQuickColorGroup]) -> None:
    """
    Calls Qt's 'void QQuickPalette::setActive(QQuickColorGroup *active)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#setActive

    Parameters
    ----------

    active : Optional[QQuickColorGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPalette::setActive(QQuickColorGroup *active)
    self.uglySide.call(
        'ritual_ZN13QQuickPalette9setActiveEP16QQuickColorGroup',
        self._addressOf(active),
    )

  @overload(QQuickColorGroup)
  @overload(NoneType)
  def setInactive(self, inactive: Optional[QQuickColorGroup]) -> None:
    """
    Calls Qt's 'void QQuickPalette::setInactive(QQuickColorGroup *inactive)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#setInactive

    Parameters
    ----------

    inactive : Optional[QQuickColorGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPalette::setInactive(QQuickColorGroup *inactive)
    self.uglySide.call(
        'ritual_ZN13QQuickPalette11setInactiveEP16QQuickColorGroup',
        self._addressOf(inactive),
    )

  @overload(QQuickColorGroup)
  @overload(NoneType)
  def setDisabled(self, disabled: Optional[QQuickColorGroup]) -> None:
    """
    Calls Qt's 'void QQuickPalette::setDisabled(QQuickColorGroup *disabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#setDisabled

    Parameters
    ----------

    disabled : Optional[QQuickColorGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPalette::setDisabled(QQuickColorGroup *disabled)
    self.uglySide.call(
        'ritual_ZN13QQuickPalette11setDisabledEP16QQuickColorGroup',
        self._addressOf(disabled),
    )

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
    Notes what was given, for Qt's 'QQuickPalette::QQuickPalette(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#QQuickPalette

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPalette::QQuickPalette(QObject *parent)
    self._noteCreation(QQuickPalette, lambda: Rituals.call(
        'ritual_ZN13QQuickPaletteC1EP7QObject',
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

  def resetActive(self) -> None:
    """
    Calls Qt's 'void QQuickPalette::resetActive()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#resetActive
    """
    #  void QQuickPalette::resetActive()
    self.uglySide.call('ritual_ZN13QQuickPalette11resetActiveEv')

  def resetInactive(self) -> None:
    """
    Calls Qt's 'void QQuickPalette::resetInactive()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#resetInactive
    """
    #  void QQuickPalette::resetInactive()
    self.uglySide.call('ritual_ZN13QQuickPalette13resetInactiveEv')

  def resetDisabled(self) -> None:
    """
    Calls Qt's 'void QQuickPalette::resetDisabled()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#resetDisabled
    """
    #  void QQuickPalette::resetDisabled()
    self.uglySide.call('ritual_ZN13QQuickPalette13resetDisabledEv')

  @overload(QPalette)
  def fromQPalette(self, palette: QPalette) -> None:
    """
    Calls Qt's 'void QQuickPalette::fromQPalette(QPalette palette)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#fromQPalette

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QQuickPalette::fromQPalette(QPalette palette)
    self.uglySide.call(
        'ritual_ZN13QQuickPalette12fromQPaletteE8QPalette',
        self._valueOf(palette),
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickPalette::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#reset
    """
    #  void QQuickPalette::reset()
    self.uglySide.call('ritual_ZN13QQuickPalette5resetEv')

  @overload(QPalette)
  def inheritPalette(self, palette: QPalette) -> None:
    """
    Calls Qt's 'void QQuickPalette::inheritPalette(const QPalette &palette)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#inheritPalette

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  void QQuickPalette::inheritPalette(const QPalette &palette)
    self.uglySide.call(
        'ritual_ZN13QQuickPalette14inheritPaletteERK8QPalette',
        self._valueOf(palette),
    )

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPalette::activeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#activeChanged
    """
    #  void QQuickPalette::activeChanged()
    self.uglySide.call('ritual_ZN13QQuickPalette13activeChangedEv')

  def inactiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPalette::inactiveChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#inactiveChanged
    """
    #  void QQuickPalette::inactiveChanged()
    self.uglySide.call('ritual_ZN13QQuickPalette15inactiveChangedEv')

  def disabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPalette::disabledChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpalette.html#disabledChanged
    """
    #  void QQuickPalette::disabledChanged()
    self.uglySide.call('ritual_ZN13QQuickPalette15disabledChangedEv')

  @overload(QQuickColorGroup, QPalette.ColorGroup)
  @overload(NoneType, QPalette.ColorGroup)
  def registerColorGroup(
      self,
      group: Optional[QQuickColorGroup],
      groupTag: QPalette.ColorGroup,
  ) -> None:
    """
    Calls Qt's 'void QQuickPalette::registerColorGroup(QQuickColorGroup
    *group, QPalette::ColorGroup groupTag)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalette.html#registerColorGroup

    Parameters
    ----------

    group : Optional[QQuickColorGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    groupTag : QPalette.ColorGroup
      Passed on as its number.
    """
    #  void QQuickPalette::registerColorGroup(QQuickColorGroup *group,
    #      QPalette::ColorGroup groupTag)
    self.uglySide.call(
        'ritual_ZN13QQuickPalette18registerColorGroupEP16QQuickColorGroupN8'
        'QPalette10ColorGroupE',
        self._addressOf(group), groupTag.value,
    )

  @staticmethod
  def colorGroup(*__, **_) -> Never:
    """
    Qt's 'QQuickColorGroup::GroupPtr
    QQuickPalette::colorGroup(QPalette::ColorGroup groupTag) const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPalette.colorGroup' has no cute function yet. Qt's "
        "'QQuickColorGroup::GroupPtr "
        "QQuickPalette::colorGroup(QPalette::ColorGroup groupTag) const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def findColorGroup(*__, **_) -> Never:
    """
    Qt's 'QQuickColorGroup::GroupPtr
    QQuickPalette::findColorGroup(QPalette::ColorGroup groupTag) const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPalette.findColorGroup' has no cute function yet. Qt's "
        "'QQuickColorGroup::GroupPtr "
        "QQuickPalette::findColorGroup(QPalette::ColorGroup groupTag) "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def isValidColorGroup(*__, **_) -> Never:
    """
    Qt's 'bool QQuickPalette::isValidColorGroup(QPalette::ColorGroup
    groupTag, const QQuickColorGroup::GroupPtr &colorGroup) const': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickPalette.isValidColorGroup' has no cute function yet. Qt's "
        "'bool QQuickPalette::isValidColorGroup(QPalette::ColorGroup "
        "groupTag, const QQuickColorGroup::GroupPtr &colorGroup) const': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setColorGroup(*__, **_) -> Never:
    """
    Qt's 'void QQuickPalette::setColorGroup(QPalette::ColorGroup groupTag,
    const QQuickColorGroup::GroupPtr &group, void (QQuickPalette::*)()
    notifier)': takes or gives a type that cannot be passed yet: void
    (QQuickPalette::*)().
    """
    raise NotImplementedError(
        "'QQuickPalette.setColorGroup' has no cute function yet. Qt's 'void "
        "QQuickPalette::setColorGroup(QPalette::ColorGroup groupTag, const "
        "QQuickColorGroup::GroupPtr &group, void (QQuickPalette::*)() "
        "notifier)': takes or gives a type that cannot be passed yet: void "
        "(QQuickPalette::*)().")
