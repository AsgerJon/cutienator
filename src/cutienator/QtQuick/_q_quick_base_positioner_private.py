"""
QQuickBasePositionerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickBasePositionerPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QQuickBasePositioner, QQuickImplicitSizeItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from . import QQuickGeometryChange, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickBasePositionerPrivate(QQuickImplicitSizeItemPrivate):
  """
  The cute side of Qt's QQuickBasePositionerPrivate: a plain Python object
  standing in front of one C++ QQuickBasePositionerPrivate.

  It is built on the cute 'QQuickImplicitSizeItemPrivate', as Qt's
  QQuickBasePositionerPrivate is built on Qt's QQuickImplicitSizeItemPrivate,
  and has everything that class has. Qt's QQuickBasePositionerPrivate is
  built on Qt's QSafeQuickItemChangeListener<QQuickBasePositionerPrivate> as
  well, which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickBasePositionerPrivate that has a ritual and
  that Python can call so far, 18 names in all: 'q_func', 'init',
  'watchChanges', 'setPositioningDirty', 'mirrorChange', 'isLeftToRight',
  'itemSiblingOrderChanged', 'itemGeometryChanged', 'itemVisibilityChanged',
  'itemDestroyed', 'getLayoutDirection', 'getEffectiveLayoutDirection',
  'effectiveLayoutDirectionChange', 'padding', 'setTopPadding',
  'setLeftPadding', 'setRightPadding', 'setBottomPadding'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickBasePositioner *QQuickBasePositionerPrivate::q_func()
    const': takes in Python what 'QQuickBasePositioner
    *QQuickBasePositionerPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 21 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickBasePositionerPrivate is created at the first use, not by
    'QQuickBasePositionerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickBasePositionerPrivate.
  - Each name of Qt's QQuickBasePositionerPrivate that has no cute function
    yet, 'unwatchChanges', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQuickBasePositionerPrivate, each a class
  #  in here as in C++.

  class ExtraData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickBasePositionerPrivate::ExtraData: a plain
    Python object standing in front of one C++
    QQuickBasePositionerPrivate::ExtraData.

    C++ hands a QQuickBasePositionerPrivate::ExtraData around as a copy, so
    every C++ QQuickBasePositionerPrivate::ExtraData behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuickBasePositionerPrivate::ExtraData yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickBasePositionerPrivate::ExtraData::~ExtraData()': the
      destructor: Python removes its C++
      QQuickBasePositionerPrivate::ExtraData by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQuickBasePositionerPrivate::ExtraData is created at the first
      use, not by 'QQuickBasePositionerPrivate::ExtraData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickBasePositionerPrivate::ExtraData back gives a
      copy the ritual made for Python, in a new cute
      QQuickBasePositionerPrivate::ExtraData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickBasePositionerPrivate::ExtraData'

    #  Qt's '~QQuickBasePositionerPrivate::ExtraData()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QQuickBasePositionerPrivate::ExtraData behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN27QQuickBasePositionerPrivate9ExtraDataD1Ev')

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QQuickBasePositionerPrivate::ExtraData::ExtraData()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickbasepositionerprivate-extradata.html
      """
      #  QQuickBasePositionerPrivate::ExtraData::ExtraData()
      self._noteCreation(
          QQuickBasePositionerPrivate.ExtraData, lambda: Rituals.call(
              'ritual_ZN27QQuickBasePositionerPrivate9ExtraDataC1Ev',
          ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickBasePositioner)
  @overload(NoneType)
  def getLayoutDirection(
      positioner: Optional[QQuickBasePositioner],
  ) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection
    QQuickBasePositionerPrivate::getLayoutDirection(const
    QQuickBasePositioner *positioner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html

    Parameters
    ----------

    positioner : Optional[QQuickBasePositioner]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection
    #      QQuickBasePositionerPrivate::getLayoutDirection(const
    #      QQuickBasePositioner *positioner)
    return Qt.LayoutDirection(Rituals.call(
        'ritual_ZN27QQuickBasePositionerPrivate18getLayoutDirectionEPK20QQu'
        'ickBasePositioner',
        CuteMixin._addressOf(positioner),
    ))

  @staticmethod
  @overload(QQuickBasePositioner)
  @overload(NoneType)
  def getEffectiveLayoutDirection(
      positioner: Optional[QQuickBasePositioner],
  ) -> Qt.LayoutDirection:
    """
    Calls Qt's 'Qt::LayoutDirection
    QQuickBasePositionerPrivate::getEffectiveLayoutDirection(const
    QQuickBasePositioner *positioner)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html

    Parameters
    ----------

    positioner : Optional[QQuickBasePositioner]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.LayoutDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.LayoutDirection(number)' gives.
    """
    #  Qt::LayoutDirection
    #      QQuickBasePositionerPrivate::getEffectiveLayoutDirection(const
    #      QQuickBasePositioner *positioner)
    return Qt.LayoutDirection(Rituals.call(
        'ritual_ZN27QQuickBasePositionerPrivate27getEffectiveLayoutDirectio'
        'nEPK20QQuickBasePositioner',
        CuteMixin._addressOf(positioner),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickBasePositionerPrivate'

  #  A C++ QQuickBasePositionerPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickBasePositionerPrivate'

  #  The functions Qt calls itself that QQuickBasePositionerPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'itemSiblingOrderChanged': (
          ('_ZN27QQuickBasePositionerPrivate23itemSiblingOrderChangedEP10QQ'
           'uickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemGeometryChanged': (
          ('_ZN27QQuickBasePositionerPrivate19itemGeometryChangedEP10QQuick'
           'Item20QQuickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemVisibilityChanged': (
          ('_ZN27QQuickBasePositionerPrivate21itemVisibilityChangedEP10QQui'
           'ckItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemDestroyed': (
          ('_ZN27QQuickBasePositionerPrivate13itemDestroyedEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'effectiveLayoutDirectionChange': (
          ('_ZN27QQuickBasePositionerPrivate30effectiveLayoutDirectionChang'
           'eEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isLeftToRight(self) -> bool:
    """
    Calls Qt's 'bool QQuickBasePositionerPrivate::isLeftToRight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html#isLeftToRight
    """
    #  bool QQuickBasePositionerPrivate::isLeftToRight() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickBasePositionerPrivate13isLeftToRightEv',
    )

  def padding(self) -> float:
    """
    Calls Qt's 'qreal QQuickBasePositionerPrivate::padding() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html#padding
    """
    #  qreal QQuickBasePositionerPrivate::padding() const
    return self.uglySide.call(
        'ritual_ZNK27QQuickBasePositionerPrivate7paddingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setPositioningDirty(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositionerPrivate::setPositioningDirty()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html
    """
    #  void QQuickBasePositionerPrivate::setPositioningDirty()
    self.uglySide.call(
        'ritual_ZN27QQuickBasePositionerPrivate19setPositioningDirtyEv',
    )

  @overload(float)
  @overload(float, bool)
  def setTopPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickBasePositionerPrivate::setTopPadding(qreal value,
    bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html#setTopPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickBasePositionerPrivate::setTopPadding(qreal value, bool
    #      reset)
    self.uglySide.call(
        'ritual_ZN27QQuickBasePositionerPrivate13setTopPaddingEdb',
        value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setLeftPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickBasePositionerPrivate::setLeftPadding(qreal value,
    bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html#setLeftPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickBasePositionerPrivate::setLeftPadding(qreal value, bool
    #      reset)
    self.uglySide.call(
        'ritual_ZN27QQuickBasePositionerPrivate14setLeftPaddingEdb',
        value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setRightPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickBasePositionerPrivate::setRightPadding(qreal
    value, bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html#setRightPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickBasePositionerPrivate::setRightPadding(qreal value, bool
    #      reset)
    self.uglySide.call(
        'ritual_ZN27QQuickBasePositionerPrivate15setRightPaddingEdb',
        value, reset,
    )

  @overload(float)
  @overload(float, bool)
  def setBottomPadding(self, value: float, reset: bool = False) -> None:
    """
    Calls Qt's 'void QQuickBasePositionerPrivate::setBottomPadding(qreal
    value, bool reset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html#setBottomPadding

    Parameters
    ----------

    value : float
      Passed on as it is.

    reset : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QQuickBasePositionerPrivate::setBottomPadding(qreal value, bool
    #      reset)
    self.uglySide.call(
        'ritual_ZN27QQuickBasePositionerPrivate16setBottomPaddingEdb',
        value, reset,
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
    'QQuickBasePositionerPrivate::QQuickBasePositionerPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html
    """
    #  QQuickBasePositionerPrivate::QQuickBasePositionerPrivate()
    self._noteCreation(QQuickBasePositionerPrivate, lambda: Rituals.call(
        'ritual_ZN27QQuickBasePositionerPrivateC1Ev',
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

  def q_func(self) -> Optional[QQuickBasePositioner]:
    """
    Calls Qt's 'QQuickBasePositioner *QQuickBasePositionerPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html#q_func

    Returns
    -------

    Optional[QQuickBasePositioner]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickBasePositioner *QQuickBasePositionerPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN27QQuickBasePositionerPrivate6q_funcEv',
    )
    return QQuickBasePositioner._cuteAt(address)

  @overload(QQuickBasePositioner.PositionerType)
  def init(self, at: QQuickBasePositioner.PositionerType) -> None:
    """
    Calls Qt's 'void
    QQuickBasePositionerPrivate::init(QQuickBasePositioner::PositionerType
    at)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html#init

    Parameters
    ----------

    at : QQuickBasePositioner.PositionerType
      Passed on as its number.
    """
    #  void QQuickBasePositionerPrivate::init(QQuickBasePositioner::
    #      PositionerType at)
    self.uglySide.call(
        'ritual_ZN27QQuickBasePositionerPrivate4initEN20QQuickBasePositione'
        'r14PositionerTypeE',
        at.value,
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def watchChanges(self, other: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickBasePositionerPrivate::watchChanges(QQuickItem
    *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html#watchChanges

    Parameters
    ----------

    other : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBasePositionerPrivate::watchChanges(QQuickItem *other)
    self.uglySide.call(
        'ritual_ZN27QQuickBasePositionerPrivate12watchChangesEP10QQuickItem',
        self._addressOf(other),
    )

  def mirrorChange(self) -> None:
    """
    Calls Qt's 'void QQuickBasePositionerPrivate::mirrorChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html#mirrorChange
    """
    #  void QQuickBasePositionerPrivate::mirrorChange()
    ritual = 'ritual_ZN27QQuickBasePositionerPrivate12mirrorChangeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN27QQuickBasePositionerPrivate12mirrorChangeEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem)
  @overload(NoneType)
  def itemSiblingOrderChanged(self, other: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickBasePositionerPrivate::itemSiblingOrderChanged(QQuickItem *other)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html

    Parameters
    ----------

    other : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBasePositionerPrivate::itemSiblingOrderChanged(QQuickItem
    #      *other)
    ritual = (
        'ritual_ZN27QQuickBasePositionerPrivate23itemSiblingOrderChangedEP1'
        '0QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickBasePositionerPrivate23itemSiblingOrderChan'
          'gedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(other))

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      a0: Optional[QQuickItem],
      change: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickBasePositionerPrivate::itemGeometryChanged(QQuickItem *a0,
    QQuickGeometryChange change, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickBasePositionerPrivate::itemGeometryChanged(QQuickItem *a0,
    #      QQuickGeometryChange change, const QRectF &a2)
    ritual = (
        'ritual_ZN27QQuickBasePositionerPrivate19itemGeometryChangedEP10QQu'
        'ickItem20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickBasePositionerPrivate19itemGeometryChangedE'
          'P10QQuickItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(a0), self._valueOf(change), self._valueOf(a2),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemVisibilityChanged(self, a0: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickBasePositionerPrivate::itemVisibilityChanged(QQuickItem *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBasePositionerPrivate::itemVisibilityChanged(QQuickItem
    #      *a0)
    ritual = (
        'ritual_ZN27QQuickBasePositionerPrivate21itemVisibilityChangedEP10Q'
        'QuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickBasePositionerPrivate21itemVisibilityChange'
          'dEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickBasePositionerPrivate::itemDestroyed(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickBasePositionerPrivate::itemDestroyed(QQuickItem *item)
    ritual = (
        'ritual_ZN27QQuickBasePositionerPrivate13itemDestroyedEP10QQuickIte'
        'm')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickBasePositionerPrivate13itemDestroyedEP10QQu'
          'ickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  def effectiveLayoutDirectionChange(self) -> None:
    """
    Calls Qt's 'void
    QQuickBasePositionerPrivate::effectiveLayoutDirectionChange()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickbasepositionerprivate.html
    """
    #  void QQuickBasePositionerPrivate::effectiveLayoutDirectionChange()
    ritual = (
        'ritual_ZN27QQuickBasePositionerPrivate30effectiveLayoutDirectionCh'
        'angeEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN27QQuickBasePositionerPrivate30effectiveLayoutDirec'
          'tionChangeEv')
    self.uglySide.call(ritual)

  @staticmethod
  def unwatchChanges(*__, **_) -> Never:
    """
    Qt's 'void QQuickBasePositionerPrivate::unwatchChanges(QQuickItem
    *other)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'positionerWatchedChanges'.
    """
    raise NotImplementedError(
        "'QQuickBasePositionerPrivate.unwatchChanges' has no cute function "
        "yet. Qt's 'void "
        "QQuickBasePositionerPrivate::unwatchChanges(QQuickItem *other)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'positionerWatchedChanges'.")
