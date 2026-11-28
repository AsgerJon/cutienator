"""
QQuickPaletteColorProvider binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpalettecolorprovider_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickPaletteColorProvider to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtGui import QPalette

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtGui import QColor
  from . import QQuickAbstractPaletteProvider
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QQuickAbstractPaletteProvider = WAIT['QQuickAbstractPaletteProvider']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPaletteColorProvider(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickPaletteColorProvider: a plain Python object
  standing in front of one C++ QQuickPaletteColorProvider.

  What exists
  -----------

  Every function of Qt's QQuickPaletteColorProvider that has a ritual and
  that Python can call so far, 12 names in all: 'color', 'setColor',
  'resetColor', 'fromQPalette', 'palette', 'paletteProvider',
  'setPaletteProvider', 'reset', 'inheritPalette', 'doInheritPalette',
  'updateInheritedPalette', 'ensureRequestedPalette'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool
    QQuickPaletteColorProvider::copyColorGroup(QPalette::ColorGroup cg, const
    QQuickPaletteColorProvider &p)': takes a type Python has no way to hand
    over yet.

  What to expect
  --------------

  - The C++ QQuickPaletteColorProvider is created at the first use, not by
    'QQuickPaletteColorProvider(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPaletteColorProvider.
  - Each name of Qt's QQuickPaletteColorProvider that has no cute function
    yet, 'copyColorGroup', holds a function that raises
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
  __qt_class__ = 'QQuickPaletteColorProvider'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPalette.ColorGroup, QPalette.ColorRole)
  def color(
      self,
      group: QPalette.ColorGroup,
      role: QPalette.ColorRole,
  ) -> QColor:
    """
    Calls Qt's 'const QColor
    &QQuickPaletteColorProvider::color(QPalette::ColorGroup group,
    QPalette::ColorRole role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html#color

    Parameters
    ----------

    group : QPalette.ColorGroup
      Passed on as its number.

    role : QPalette.ColorRole
      Passed on as its number.

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  const QColor &QQuickPaletteColorProvider::color(QPalette::ColorGroup
    #      group, QPalette::ColorRole role) const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickPaletteColorProvider5colorEN8QPalette10ColorGrou'
        'pENS0_9ColorRoleE',
        group.value, role.value,
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def palette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickPaletteColorProvider::palette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html#palette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickPaletteColorProvider::palette() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickPaletteColorProvider7paletteEv',
    )
    return QPalette._cuteOwning(address)

  def paletteProvider(self) -> Optional[QQuickAbstractPaletteProvider]:
    """
    Calls Qt's 'const QQuickAbstractPaletteProvider
    *QQuickPaletteColorProvider::paletteProvider() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html#paletteProvider

    Returns
    -------

    Optional[QQuickAbstractPaletteProvider]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQuickAbstractPaletteProvider
    #      *QQuickPaletteColorProvider::paletteProvider() const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickPaletteColorProvider15paletteProviderEv',
    )
    from . import QQuickAbstractPaletteProvider
    return QQuickAbstractPaletteProvider._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPalette.ColorGroup, QPalette.ColorRole, QColor)
  def setColor(
      self,
      group: QPalette.ColorGroup,
      role: QPalette.ColorRole,
      color: QColor,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickPaletteColorProvider::setColor(QPalette::ColorGroup group,
    QPalette::ColorRole role, QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html#setColor

    Parameters
    ----------

    group : QPalette.ColorGroup
      Passed on as its number.

    role : QPalette.ColorRole
      Passed on as its number.

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  bool QQuickPaletteColorProvider::setColor(QPalette::ColorGroup group,
    #      QPalette::ColorRole role, QColor color)
    return self.uglySide.call(
        'ritual_ZN26QQuickPaletteColorProvider8setColorEN8QPalette10ColorGr'
        'oupENS0_9ColorRoleE6QColor',
        group.value, role.value, self._valueOf(color),
    )

  @overload(QQuickAbstractPaletteProvider)
  @overload(NoneType)
  def setPaletteProvider(
      self,
      paletteProvider: Optional[QQuickAbstractPaletteProvider],
  ) -> None:
    """
    Calls Qt's 'void QQuickPaletteColorProvider::setPaletteProvider(const
    QQuickAbstractPaletteProvider *paletteProvider)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html#setPaletteProvider

    Parameters
    ----------

    paletteProvider : Optional[QQuickAbstractPaletteProvider]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPaletteColorProvider::setPaletteProvider(const
    #      QQuickAbstractPaletteProvider *paletteProvider)
    self.uglySide.call(
        'ritual_ZN26QQuickPaletteColorProvider18setPaletteProviderEPK29QQui'
        'ckAbstractPaletteProvider',
        self._addressOf(paletteProvider),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPaletteColorProvider::QQuickPaletteColorProvider()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html
    """
    #  QQuickPaletteColorProvider::QQuickPaletteColorProvider()
    self._noteCreation(QQuickPaletteColorProvider, lambda: Rituals.call(
        'ritual_ZN26QQuickPaletteColorProviderC1Ev',
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

  @overload(QPalette.ColorGroup, QPalette.ColorRole)
  def resetColor(
      self,
      group: QPalette.ColorGroup,
      role: QPalette.ColorRole,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQuickPaletteColorProvider::resetColor(QPalette::ColorGroup group,
    QPalette::ColorRole role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html#resetColor

    Parameters
    ----------

    group : QPalette.ColorGroup
      Passed on as its number.

    role : QPalette.ColorRole
      Passed on as its number.
    """
    #  bool QQuickPaletteColorProvider::resetColor(QPalette::ColorGroup
    #      group, QPalette::ColorRole role)
    return self.uglySide.call(
        'ritual_ZN26QQuickPaletteColorProvider10resetColorEN8QPalette10Colo'
        'rGroupENS0_9ColorRoleE',
        group.value, role.value,
    )

  @overload(QPalette.ColorGroup)
  def resetColor(self, group: QPalette.ColorGroup) -> bool:
    """
    Calls Qt's 'bool
    QQuickPaletteColorProvider::resetColor(QPalette::ColorGroup group)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html#resetColor

    Parameters
    ----------

    group : QPalette.ColorGroup
      Passed on as its number.
    """
    #  bool QQuickPaletteColorProvider::resetColor(QPalette::ColorGroup
    #      group)
    return self.uglySide.call(
        'ritual_ZN26QQuickPaletteColorProvider10resetColorEN8QPalette10Colo'
        'rGroupE',
        group.value,
    )

  @overload(QPalette)
  def fromQPalette(self, p: QPalette) -> bool:
    """
    Calls Qt's 'bool QQuickPaletteColorProvider::fromQPalette(QPalette p)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html#fromQPalette

    Parameters
    ----------

    p : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  bool QQuickPaletteColorProvider::fromQPalette(QPalette p)
    return self.uglySide.call(
        'ritual_ZN26QQuickPaletteColorProvider12fromQPaletteE8QPalette',
        self._valueOf(p),
    )

  def reset(self) -> bool:
    """
    Calls Qt's 'bool QQuickPaletteColorProvider::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html#reset
    """
    #  bool QQuickPaletteColorProvider::reset()
    return self.uglySide.call(
        'ritual_ZN26QQuickPaletteColorProvider5resetEv',
    )

  @overload(QPalette)
  def inheritPalette(self, palette: QPalette) -> bool:
    """
    Calls Qt's 'bool QQuickPaletteColorProvider::inheritPalette(const
    QPalette &palette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html#inheritPalette

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  bool QQuickPaletteColorProvider::inheritPalette(const QPalette
    #      &palette)
    return self.uglySide.call(
        'ritual_ZN26QQuickPaletteColorProvider14inheritPaletteERK8QPalette',
        self._valueOf(palette),
    )

  @overload(QPalette)
  def doInheritPalette(self, palette: QPalette) -> bool:
    """
    Calls Qt's 'bool QQuickPaletteColorProvider::doInheritPalette(const
    QPalette &palette)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html#doInheritPalette

    Parameters
    ----------

    palette : QPalette
      Passed on as a value: Qt reads the C++ QPalette, which stays Python's
      own.
    """
    #  bool QQuickPaletteColorProvider::doInheritPalette(const QPalette
    #      &palette)
    return self.uglySide.call(
        'ritual_ZN26QQuickPaletteColorProvider16doInheritPaletteERK8QPalett'
        'e',
        self._valueOf(palette),
    )

  def updateInheritedPalette(self) -> bool:
    """
    Calls Qt's 'bool QQuickPaletteColorProvider::updateInheritedPalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html
    """
    #  bool QQuickPaletteColorProvider::updateInheritedPalette()
    return self.uglySide.call(
        'ritual_ZN26QQuickPaletteColorProvider22updateInheritedPaletteEv',
    )

  def ensureRequestedPalette(self) -> None:
    """
    Calls Qt's 'void QQuickPaletteColorProvider::ensureRequestedPalette()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpalettecolorprovider.html
    """
    #  void QQuickPaletteColorProvider::ensureRequestedPalette()
    self.uglySide.call(
        'ritual_ZN26QQuickPaletteColorProvider22ensureRequestedPaletteEv',
    )

  @staticmethod
  def copyColorGroup(*__, **_) -> Never:
    """
    Qt's 'bool
    QQuickPaletteColorProvider::copyColorGroup(QPalette::ColorGroup cg, const
    QQuickPaletteColorProvider &p)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQuickPaletteColorProvider.copyColorGroup' has no cute function "
        "yet. Qt's 'bool "
        "QQuickPaletteColorProvider::copyColorGroup(QPalette::ColorGroup "
        "cg, const QQuickPaletteColorProvider &p)': takes a type Python has "
        "no way to hand over yet.")
