"""
QQuickScrollBarAttachedPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickScrollBarAttachedPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QRectF
  from ..QtQuick import QQuickFlickable, QQuickGeometryChange, QQuickItem
  from . import QQuickScrollBarAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuickFlickable = WAIT['QQuickFlickable']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QQuickScrollBarAttached = WAIT['QQuickScrollBarAttached']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickScrollBarAttachedPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuickScrollBarAttachedPrivate: a plain Python object
  standing in front of one C++ QQuickScrollBarAttachedPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QQuickScrollBarAttachedPrivate is built on Qt's QObjectPrivate, and has
  everything that class has. Qt's QQuickScrollBarAttachedPrivate is built on
  Qt's QSafeQuickItemChangeListener<QQuickScrollBarAttachedPrivate> as well,
  which is not reflected.

  What exists
  -----------

  Every function of Qt's QQuickScrollBarAttachedPrivate that has a ritual and
  that Python can call so far, 16 names in all: 'get', 'setFlickable',
  'initHorizontal', 'initVertical', 'cleanupHorizontal', 'cleanupVertical',
  'activateHorizontal', 'activateVertical', 'scrollHorizontal',
  'mirrorVertical', 'layoutHorizontal', 'layoutVertical',
  'itemGeometryChanged', 'itemImplicitWidthChanged',
  'itemImplicitHeightChanged', 'itemDestroyed'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has no ritual
  ------------------

  1 of the 17 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickScrollBarAttachedPrivate is created at the first use, not
    by 'QQuickScrollBarAttachedPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickScrollBarAttachedPrivate.
  - Each name of Qt's QQuickScrollBarAttachedPrivate that has no cute
    function yet, 'scrollVertical', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickScrollBarAttached)
  @overload(NoneType)
  def get(
      attached: Optional[QQuickScrollBarAttached],
  ) -> Optional[QQuickScrollBarAttachedPrivate]:
    """
    Calls Qt's 'QQuickScrollBarAttachedPrivate
    *QQuickScrollBarAttachedPrivate::get(QQuickScrollBarAttached *attached)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html#get

    Parameters
    ----------

    attached : Optional[QQuickScrollBarAttached]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickScrollBarAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScrollBarAttachedPrivate
    #      *QQuickScrollBarAttachedPrivate::get(QQuickScrollBarAttached
    #      *attached)
    address = Rituals.call(
        'ritual_ZN30QQuickScrollBarAttachedPrivate3getEP23QQuickScrollBarAt'
        'tached',
        CuteMixin._addressOf(attached),
    )
    return QQuickScrollBarAttachedPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickScrollBarAttachedPrivate'

  #  A C++ QQuickScrollBarAttachedPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickScrollBarAttachedPrivate'

  #  The functions Qt calls itself that QQuickScrollBarAttachedPrivate is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'itemGeometryChanged': (
          ('_ZN30QQuickScrollBarAttachedPrivate19itemGeometryChangedEP10QQu'
           'ickItem20QQuickGeometryChangeRK6QRectF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('address', 'value', 'QtQuick:QQuickGeometryChange'),
               ('address', 'value', 'QtCore:QRectF'),
           )),
      ),
      'itemImplicitWidthChanged': (
          ('_ZN30QQuickScrollBarAttachedPrivate24itemImplicitWidthChangedEP'
           '10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemImplicitHeightChanged': (
          ('_ZN30QQuickScrollBarAttachedPrivate25itemImplicitHeightChangedE'
           'P10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'itemDestroyed': (
          ('_ZN30QQuickScrollBarAttachedPrivate13itemDestroyedEP10QQuickIte'
           'm',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickFlickable)
  @overload(NoneType)
  def setFlickable(self, flickable: Optional[QQuickFlickable]) -> None:
    """
    Calls Qt's 'void
    QQuickScrollBarAttachedPrivate::setFlickable(QQuickFlickable
    *flickable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html#setFlickable

    Parameters
    ----------

    flickable : Optional[QQuickFlickable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollBarAttachedPrivate::setFlickable(QQuickFlickable
    #      *flickable)
    self.uglySide.call(
        'ritual_ZN30QQuickScrollBarAttachedPrivate12setFlickableEP15QQuickF'
        'lickable',
        self._addressOf(flickable),
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

  def initHorizontal(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBarAttachedPrivate::initHorizontal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html#initHorizontal
    """
    #  void QQuickScrollBarAttachedPrivate::initHorizontal()
    self.uglySide.call(
        'ritual_ZN30QQuickScrollBarAttachedPrivate14initHorizontalEv',
    )

  def initVertical(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBarAttachedPrivate::initVertical()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html#initVertical
    """
    #  void QQuickScrollBarAttachedPrivate::initVertical()
    self.uglySide.call(
        'ritual_ZN30QQuickScrollBarAttachedPrivate12initVerticalEv',
    )

  def cleanupHorizontal(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBarAttachedPrivate::cleanupHorizontal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html
    """
    #  void QQuickScrollBarAttachedPrivate::cleanupHorizontal()
    self.uglySide.call(
        'ritual_ZN30QQuickScrollBarAttachedPrivate17cleanupHorizontalEv',
    )

  def cleanupVertical(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBarAttachedPrivate::cleanupVertical()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html
    """
    #  void QQuickScrollBarAttachedPrivate::cleanupVertical()
    self.uglySide.call(
        'ritual_ZN30QQuickScrollBarAttachedPrivate15cleanupVerticalEv',
    )

  def activateHorizontal(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBarAttachedPrivate::activateHorizontal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html
    """
    #  void QQuickScrollBarAttachedPrivate::activateHorizontal()
    self.uglySide.call(
        'ritual_ZN30QQuickScrollBarAttachedPrivate18activateHorizontalEv',
    )

  def activateVertical(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBarAttachedPrivate::activateVertical()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html
    """
    #  void QQuickScrollBarAttachedPrivate::activateVertical()
    self.uglySide.call(
        'ritual_ZN30QQuickScrollBarAttachedPrivate16activateVerticalEv',
    )

  def scrollHorizontal(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBarAttachedPrivate::scrollHorizontal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html
    """
    #  void QQuickScrollBarAttachedPrivate::scrollHorizontal()
    self.uglySide.call(
        'ritual_ZN30QQuickScrollBarAttachedPrivate16scrollHorizontalEv',
    )

  def mirrorVertical(self) -> None:
    """
    Calls Qt's 'void QQuickScrollBarAttachedPrivate::mirrorVertical()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html#mirrorVertical
    """
    #  void QQuickScrollBarAttachedPrivate::mirrorVertical()
    self.uglySide.call(
        'ritual_ZN30QQuickScrollBarAttachedPrivate14mirrorVerticalEv',
    )

  @overload()
  @overload(bool)
  def layoutHorizontal(self, move: bool = True) -> None:
    """
    Calls Qt's 'void QQuickScrollBarAttachedPrivate::layoutHorizontal(bool
    move)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html

    Parameters
    ----------

    move : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickScrollBarAttachedPrivate::layoutHorizontal(bool move)
    self.uglySide.call(
        'ritual_ZN30QQuickScrollBarAttachedPrivate16layoutHorizontalEb',
        move,
    )

  @overload()
  @overload(bool)
  def layoutVertical(self, move: bool = True) -> None:
    """
    Calls Qt's 'void QQuickScrollBarAttachedPrivate::layoutVertical(bool
    move)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html#layoutVertical

    Parameters
    ----------

    move : bool
      Passed on as it is. May be left out, as in Qt: it is then True.
    """
    #  void QQuickScrollBarAttachedPrivate::layoutVertical(bool move)
    self.uglySide.call(
        'ritual_ZN30QQuickScrollBarAttachedPrivate14layoutVerticalEb', move,
    )

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      item: Optional[QQuickItem],
      change: QQuickGeometryChange,
      diff: QRectF,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickScrollBarAttachedPrivate::itemGeometryChanged(QQuickItem *item,
    QQuickGeometryChange change, const QRectF &diff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    change : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    diff : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickScrollBarAttachedPrivate::itemGeometryChanged(QQuickItem
    #      *item, QQuickGeometryChange change, const QRectF &diff)
    ritual = (
        'ritual_ZN30QQuickScrollBarAttachedPrivate19itemGeometryChangedEP10'
        'QQuickItem20QQuickGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickScrollBarAttachedPrivate19itemGeometryChang'
          'edEP10QQuickItem20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual,
        self._addressOf(item), self._valueOf(change), self._valueOf(diff),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickScrollBarAttachedPrivate::itemImplicitWidthChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollBarAttachedPrivate::itemImplicitWidthChanged(
    #      QQuickItem *item)
    ritual = (
        'ritual_ZN30QQuickScrollBarAttachedPrivate24itemImplicitWidthChange'
        'dEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickScrollBarAttachedPrivate24itemImplicitWidth'
          'ChangedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void
    QQuickScrollBarAttachedPrivate::itemImplicitHeightChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollBarAttachedPrivate::itemImplicitHeightChanged(
    #      QQuickItem *item)
    ritual = (
        'ritual_ZN30QQuickScrollBarAttachedPrivate25itemImplicitHeightChang'
        'edEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickScrollBarAttachedPrivate25itemImplicitHeigh'
          'tChangedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickScrollBarAttachedPrivate::itemDestroyed(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollbarattachedprivate.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollBarAttachedPrivate::itemDestroyed(QQuickItem *item)
    ritual = (
        'ritual_ZN30QQuickScrollBarAttachedPrivate13itemDestroyedEP10QQuick'
        'Item')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN30QQuickScrollBarAttachedPrivate13itemDestroyedEP10'
          'QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @staticmethod
  def scrollVertical(*__, **_) -> Never:
    """
    Qt's 'void QQuickScrollBarAttachedPrivate::scrollVertical()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'QQuickFriendlyFlickable'.
    """
    raise NotImplementedError(
        "'QQuickScrollBarAttachedPrivate.scrollVertical' has no cute "
        "function yet. Qt's 'void "
        "QQuickScrollBarAttachedPrivate::scrollVertical()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: unknown type name 'QQuickFriendlyFlickable'.")
