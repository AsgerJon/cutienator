"""
QQuickLinearLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklinearlayout_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickLinearLayout to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickGridLayoutBase
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQuickLinearLayoutPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLinearLayout(QQuickGridLayoutBase):
  """
  The cute side of Qt's QQuickLinearLayout: a plain Python object standing in
  front of one C++ QQuickLinearLayout.

  It is built on the cute 'QQuickGridLayoutBase', as Qt's QQuickLinearLayout
  is built on Qt's QQuickGridLayoutBase, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickLinearLayout that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'tr', 'spacing',
  'setSpacing', 'uniformCellSizes', 'setUniformCellSizes',
  'insertLayoutItems', 'spacingChanged', 'uniformCellSizesChanged', 'd_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLinearLayout::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickLinearLayout::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickLinearLayout::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'const QQuickLinearLayoutPrivate *QQuickLinearLayout::d_func()
    const': takes in Python what 'QQuickLinearLayoutPrivate
    *QQuickLinearLayout::d_func()' takes.

  What has no ritual
  ------------------

  3 of the 18 functions Qt declares: 2 not a gap; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickLinearLayout is created at the first use, not by
    'QQuickLinearLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLinearLayout.
  - Qt tells when it has removed the C++ QQuickLinearLayout. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickLinearLayout that has no cute function yet,
    'insertLayoutItem', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QQuickLinearLayout::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklinearlayout.html#tr

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
    #  QString QQuickLinearLayout::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QQuickLinearLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLinearLayout'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickLinearLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklinearlayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLinearLayout::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QQuickLinearLayout10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def spacing(self) -> float:
    """
    Calls Qt's 'qreal QQuickLinearLayout::spacing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklinearlayout.html#spacing
    """
    #  qreal QQuickLinearLayout::spacing() const
    return self.uglySide.call('ritual_ZNK18QQuickLinearLayout7spacingEv')

  def uniformCellSizes(self) -> bool:
    """
    Calls Qt's 'bool QQuickLinearLayout::uniformCellSizes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklinearlayout.html#uniformCellSizes
    """
    #  bool QQuickLinearLayout::uniformCellSizes() const
    return self.uglySide.call(
        'ritual_ZNK18QQuickLinearLayout16uniformCellSizesEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setSpacing(self, spacing: float) -> None:
    """
    Calls Qt's 'void QQuickLinearLayout::setSpacing(qreal spacing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklinearlayout.html#setSpacing

    Parameters
    ----------

    spacing : float
      Passed on as it is.
    """
    #  void QQuickLinearLayout::setSpacing(qreal spacing)
    self.uglySide.call(
        'ritual_ZN18QQuickLinearLayout10setSpacingEd', spacing,
    )

  @overload(bool)
  def setUniformCellSizes(self, uniformCellSizes: bool) -> None:
    """
    Calls Qt's 'void QQuickLinearLayout::setUniformCellSizes(bool
    uniformCellSizes)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklinearlayout.html#setUniformCellSizes

    Parameters
    ----------

    uniformCellSizes : bool
      Passed on as it is.
    """
    #  void QQuickLinearLayout::setUniformCellSizes(bool uniformCellSizes)
    self.uglySide.call(
        'ritual_ZN18QQuickLinearLayout19setUniformCellSizesEb',
        uniformCellSizes,
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

  @overload(Qt.Orientation)
  @overload(Qt.Orientation, QQuickItem)
  @overload(Qt.Orientation, NoneType)
  def __init__(
      self,
      orientation: Qt.Orientation,
      parent: Optional[QQuickItem] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickLinearLayout::QQuickLinearLayout(Qt::Orientation orientation,
    QQuickItem *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklinearlayout.html#QQuickLinearLayout

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickLinearLayout::QQuickLinearLayout(Qt::Orientation orientation,
    #      QQuickItem *parent)
    self._noteCreation(QQuickLinearLayout, lambda: Rituals.call(
        'ritual_ZN18QQuickLinearLayoutC1EN2Qt11OrientationEP10QQuickItem',
        orientation.value, self._addressOf(parent),
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

  def insertLayoutItems(self) -> None:
    """
    Calls Qt's 'void QQuickLinearLayout::insertLayoutItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklinearlayout.html#insertLayoutItems
    """
    #  void QQuickLinearLayout::insertLayoutItems()
    ritual = 'ritual_ZN18QQuickLinearLayout17insertLayoutItemsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QQuickLinearLayout17insertLayoutItemsEv'
    self.uglySide.call(ritual)

  def spacingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLinearLayout::spacingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklinearlayout.html#spacingChanged
    """
    #  void QQuickLinearLayout::spacingChanged()
    self.uglySide.call('ritual_ZN18QQuickLinearLayout14spacingChangedEv')

  def uniformCellSizesChanged(self) -> None:
    """
    Calls Qt's 'void QQuickLinearLayout::uniformCellSizesChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklinearlayout.html#uniformCellSizesChanged
    """
    #  void QQuickLinearLayout::uniformCellSizesChanged()
    self.uglySide.call(
        'ritual_ZN18QQuickLinearLayout23uniformCellSizesChangedEv',
    )

  def d_func(self) -> Optional[QQuickLinearLayoutPrivate]:
    """
    Calls Qt's 'QQuickLinearLayoutPrivate *QQuickLinearLayout::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklinearlayout.html#d_func

    Returns
    -------

    Optional[QQuickLinearLayoutPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLinearLayoutPrivate *QQuickLinearLayout::d_func()
    address = self.uglySide.call('ritual_ZN18QQuickLinearLayout6d_funcEv')
    from . import QQuickLinearLayoutPrivate
    return QQuickLinearLayoutPrivate._cuteAt(address)

  @staticmethod
  def insertLayoutItem(*__, **_) -> Never:
    """
    Qt's 'void QQuickLinearLayout::insertLayoutItem(QQuickItem *item)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickLinearLayout.insertLayoutItem' has no cute function yet. "
        "Qt's 'void QQuickLinearLayout::insertLayoutItem(QQuickItem "
        "*item)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
