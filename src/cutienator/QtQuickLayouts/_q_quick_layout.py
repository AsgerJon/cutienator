"""
QQuickLayout binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickLayouts/6.12.0/QtQuickLayouts/private/qquicklayout_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickLayout to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QLayoutPolicy
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QObject, QRectF, QSizeF
  from . import QQuickLayoutAttached, QQuickLayoutPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickLayoutAttached = WAIT['QQuickLayoutAttached']
  QRectF = WAIT['QRectF']
  QSizeF = WAIT['QSizeF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickLayout(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuickLayout: a plain Python object standing in front
  of one C++ QQuickLayout.

  What exists
  -----------

  Every function of Qt's QQuickLayout that has a ritual and that Python can
  call so far, 33 names in all: 'metaObject', 'tr', 'qmlAttachedProperties',
  'componentComplete', 'sizeHint', 'setAlignment', 'setStretchFactor',
  'invalidate', 'updateLayoutItems', 'ensureLayoutItemsUpdated', 'itemAt',
  'itemCount', 'rearrange', 'effectiveSizePolicy_helper', 'shouldIgnoreItem',
  'checkAnchors', 'itemChange', 'geometryChange', 'isReady',
  'deactivateRecur', 'invalidated', 'invalidatedArrangement', 'isMirrored',
  'itemSiblingOrderChanged', 'itemImplicitWidthChanged',
  'itemImplicitHeightChanged', 'itemDestroyed', 'itemVisibilityChanged',
  'maybeSubscribeToBaseLineOffsetChanges', '_q_dumpLayoutTree',
  'updatePolish', 'invalidateSenderItem', 'd_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickLayout::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickLayout::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickLayout::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'void QQuickLayout::qt_qmlMarker_attached()': one of Qt's own inner
    workings.
  - Qt's 'QQuickLayout::QQuickLayout(QQuickLayoutPrivate &dd, QQuickItem
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QQuickLayout::~QQuickLayout()': the destructor: Python never
    removes a C++ QQuickLayout.
  - Qt's 'void QQuickLayout::effectiveSizeHints_helper(QQuickItem *item,
    QSizeF *cachedSizeHints, QQuickLayoutAttached **info, bool
    useFallbackToWidthOrHeight)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QQuickLayout::dumpLayoutTreeRecursive(int level, QString &buf)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickLayoutPrivate *QQuickLayout::d_func() const': takes in
    Python what 'QQuickLayoutPrivate *QQuickLayout::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 44 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickLayout is created at the first use, not by
    'QQuickLayout(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickLayout.
  - Qt tells when it has removed the C++ QQuickLayout. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQuickLayout that has no cute function yet, '__init__',
    'dumpLayoutTreeRecursive', 'effectiveSizeHints_helper', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickLayout, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class EnsureLayoutItemsUpdatedOption(CuteFlags):
    """
    The flags enum 'QQuickLayout::EnsureLayoutItemsUpdatedOption' of Qt, with
    the 2 names Qt gives in it. Qt names the type of its combinations
    'QQuickLayout::EnsureLayoutItemsUpdatedOptions'.
    """

    Recursive = 0x1
    ApplySizeHints = 0x2

  EnsureLayoutItemsUpdatedOptions = EnsureLayoutItemsUpdatedOption

  class SizeHint(CuteNum):
    """
    The enum 'QQuickLayout::SizeHint' of Qt, with the 4 names Qt gives in it.
    """

    MinimumSize = Kee[int](0)
    PreferredSize = Kee[int](1)
    MaximumSize = Kee[int](2)
    NSizes = Kee[int](3)

  class SizePolicy(CuteNum):
    """
    The enum 'QQuickLayout::SizePolicy' of Qt, with the 2 names Qt gives in
    it.
    """

    SizePolicyImplicit = Kee[int](1)
    SizePolicyExplicit = Kee[int](2)

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
    Calls Qt's 'QString QQuickLayout::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#tr

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
    #  QString QQuickLayout::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuickLayout2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickLayoutAttached]:
    """
    Calls Qt's 'QQuickLayoutAttached
    *QQuickLayout::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickLayoutAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLayoutAttached *QQuickLayout::qmlAttachedProperties(QObject
    #      *object)
    address = Rituals.call(
        'ritual_ZN12QQuickLayout21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickLayoutAttached
    return QQuickLayoutAttached._cuteAt(address)

  @staticmethod
  @overload(QQuickItem, Qt.Orientation, QQuickLayoutAttached)
  @overload(QQuickItem, Qt.Orientation, NoneType)
  @overload(NoneType, Qt.Orientation, QQuickLayoutAttached)
  @overload(NoneType, Qt.Orientation, NoneType)
  def effectiveSizePolicy_helper(
      item: Optional[QQuickItem],
      orientation: Qt.Orientation,
      info: Optional[QQuickLayoutAttached],
  ) -> QLayoutPolicy.Policy:
    """
    Calls Qt's 'QLayoutPolicy::Policy
    QQuickLayout::effectiveSizePolicy_helper(QQuickItem *item,
    Qt::Orientation orientation, QQuickLayoutAttached *info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html#effectiveSizePolicy_helper

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    orientation : Qt.Orientation
      Passed on as its number.

    info : Optional[QQuickLayoutAttached]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QLayoutPolicy.Policy
      The value standing for the combination Qt gave back.
    """
    #  QLayoutPolicy::Policy
    #      QQuickLayout::effectiveSizePolicy_helper(QQuickItem *item,
    #      Qt::Orientation orientation, QQuickLayoutAttached *info)
    return QLayoutPolicy.Policy(Rituals.call(
        'ritual_ZN12QQuickLayout26effectiveSizePolicy_helperEP10QQuickItemN'
        '2Qt11OrientationEP20QQuickLayoutAttached',
        CuteMixin._addressOf(item), orientation.value,
        CuteMixin._addressOf(info),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickLayout'

  #  A C++ QQuickLayout Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickLayout'

  #  The functions Qt calls itself that QQuickLayout is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'sizeHint': (
          ('_ZNK12QQuickLayout8sizeHintEN2Qt8SizeHintE',
           ('address', 'value', 'QtCore:QSizeF'),
           (
               ('int', 'enum', 'QtCore:Qt.SizeHint'),
           )),
      ),
      'setAlignment': (
          ('_ZN12QQuickLayout12setAlignmentEP10QQuickItem6QFlagsIN2Qt13Alig'
           'nmentFlagEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('int', 'flags', 'QtCore:Qt.AlignmentFlag'),
           )),
      ),
      'setStretchFactor': (
          ('_ZN12QQuickLayout16setStretchFactorEP10QQuickItemiN2Qt11Orienta'
           'tionE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
               ('int', 'number', ''),
               ('int', 'enum', 'QtCore:Qt.Orientation'),
           )),
      ),
      'invalidate': (
          ('_ZN12QQuickLayout10invalidateEP10QQuickItem',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQuick:QQuickItem'),
           )),
      ),
      'updateLayoutItems': (
          ('_ZN12QQuickLayout17updateLayoutItemsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'itemAt': (
          ('_ZNK12QQuickLayout6itemAtEi',
           ('address', 'address', 'QtQuick:QQuickItem'),
           (
               ('int', 'number', ''),
           )),
      ),
      'itemCount': (
          ('_ZNK12QQuickLayout9itemCountEv',
           ('int', 'number', ''),
           ()),
      ),
      'rearrange': (
          ('_ZN12QQuickLayout9rearrangeERK6QSizeF',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QSizeF'),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickLayout::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickLayout::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickLayout10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(Qt.SizeHint)
  def sizeHint(self, whichSizeHint: Qt.SizeHint) -> QSizeF:
    """
    Calls Qt's 'QSizeF QQuickLayout::sizeHint(Qt::SizeHint whichSizeHint)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#sizeHint

    Parameters
    ----------

    whichSizeHint : Qt.SizeHint
      Passed on as its number.

    Returns
    -------

    QSizeF
      A new cute QSizeF around the copy Qt gave back. Python owns it.
    """
    #  QSizeF QQuickLayout::sizeHint(Qt::SizeHint whichSizeHint) const
    address = self.uglySide.call(
        'ritual_ZNK12QQuickLayout8sizeHintEN2Qt8SizeHintE',
        whichSizeHint.value,
    )
    from ..QtCore import QSizeF
    return QSizeF._cuteOwning(address)

  @overload(int)
  def itemAt(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickLayout::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickLayout::itemAt(int index) const
    address = self.uglySide.call('ritual_ZNK12QQuickLayout6itemAtEi', index)
    return QQuickItem._cuteAt(address)

  def itemCount(self) -> int:
    """
    Calls Qt's 'int QQuickLayout::itemCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#itemCount
    """
    #  int QQuickLayout::itemCount() const
    return self.uglySide.call('ritual_ZNK12QQuickLayout9itemCountEv')

  @overload(QQuickItem)
  @overload(NoneType)
  def shouldIgnoreItem(self, child: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickLayout::shouldIgnoreItem(QQuickItem *child)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#shouldIgnoreItem

    Parameters
    ----------

    child : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickLayout::shouldIgnoreItem(QQuickItem *child) const
    return self.uglySide.call(
        'ritual_ZNK12QQuickLayout16shouldIgnoreItemEP10QQuickItem',
        self._addressOf(child),
    )

  def isReady(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayout::isReady() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#isReady
    """
    #  bool QQuickLayout::isReady() const
    return self.uglySide.call('ritual_ZNK12QQuickLayout7isReadyEv')

  def invalidated(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayout::invalidated() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#invalidated
    """
    #  bool QQuickLayout::invalidated() const
    return self.uglySide.call('ritual_ZNK12QQuickLayout11invalidatedEv')

  def invalidatedArrangement(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayout::invalidatedArrangement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html#invalidatedArrangement
    """
    #  bool QQuickLayout::invalidatedArrangement() const
    return self.uglySide.call(
        'ritual_ZNK12QQuickLayout22invalidatedArrangementEv',
    )

  def isMirrored(self) -> bool:
    """
    Calls Qt's 'bool QQuickLayout::isMirrored() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#isMirrored
    """
    #  bool QQuickLayout::isMirrored() const
    return self.uglySide.call('ritual_ZNK12QQuickLayout10isMirroredEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem, Qt.Alignment)
  @overload(NoneType, Qt.Alignment)
  def setAlignment(
      self,
      item: Optional[QQuickItem],
      align: Qt.Alignment,
  ) -> None:
    """
    Calls Qt's 'void QQuickLayout::setAlignment(QQuickItem *item,
    Qt::Alignment align)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#setAlignment

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    align : Qt.Alignment
      Passed on as its number.
    """
    #  void QQuickLayout::setAlignment(QQuickItem *item, Qt::Alignment align)
    self.uglySide.call(
        'ritual_ZN12QQuickLayout12setAlignmentEP10QQuickItem6QFlagsIN2Qt13A'
        'lignmentFlagEE',
        self._addressOf(item), align.value,
    )

  @overload(QQuickItem, int, Qt.Orientation)
  @overload(NoneType, int, Qt.Orientation)
  def setStretchFactor(
      self,
      item: Optional[QQuickItem],
      stretchFactor: int,
      orient: Qt.Orientation,
  ) -> None:
    """
    Calls Qt's 'void QQuickLayout::setStretchFactor(QQuickItem *item, int
    stretchFactor, Qt::Orientation orient)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#setStretchFactor

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    stretchFactor : int
      Passed on as it is.

    orient : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickLayout::setStretchFactor(QQuickItem *item, int
    #      stretchFactor, Qt::Orientation orient)
    self.uglySide.call(
        'ritual_ZN12QQuickLayout16setStretchFactorEP10QQuickItemiN2Qt11Orie'
        'ntationE',
        self._addressOf(item), stretchFactor, orient.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickLayout::QQuickLayout(QQuickLayoutPrivate &dd, QQuickItem
    *parent)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickLayout.__init__' has no cute function yet. Qt's "
        "'QQuickLayout::QQuickLayout(QQuickLayoutPrivate &dd, QQuickItem "
        "*parent)': takes a type Python has no way to hand over yet.")

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

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickLayout::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html#componentComplete
    """
    #  void QQuickLayout::componentComplete()
    ritual = 'ritual_ZN12QQuickLayout17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickLayout17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def invalidate(self, childItem: Optional[QQuickItem] = None) -> None:
    """
    Calls Qt's 'void QQuickLayout::invalidate(QQuickItem *childItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#invalidate

    Parameters
    ----------

    childItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickLayout::invalidate(QQuickItem *childItem)
    ritual = 'ritual_ZN12QQuickLayout10invalidateEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickLayout10invalidateEP10QQuickItem'
    self.uglySide.call(ritual, self._addressOf(childItem))

  def updateLayoutItems(self) -> None:
    """
    Calls Qt's 'void QQuickLayout::updateLayoutItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html#updateLayoutItems
    """
    #  void QQuickLayout::updateLayoutItems()
    self.uglySide.call('ritual_ZN12QQuickLayout17updateLayoutItemsEv')

  @overload()
  @overload(EnsureLayoutItemsUpdatedOptions)
  def ensureLayoutItemsUpdated(
      self,
      options: EnsureLayoutItemsUpdatedOptions = (
          EnsureLayoutItemsUpdatedOptions()),
  ) -> None:
    """
    Calls Qt's 'void
    QQuickLayout::ensureLayoutItemsUpdated(EnsureLayoutItemsUpdatedOptions
    options) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html#ensureLayoutItemsUpdated

    Parameters
    ----------

    options : EnsureLayoutItemsUpdatedOptions
      Passed on as its number. May be left out, as in Qt: it is then
      EnsureLayoutItemsUpdatedOptions().
    """
    #  void QQuickLayout::ensureLayoutItemsUpdated(
    #      EnsureLayoutItemsUpdatedOptions options) const
    self.uglySide.call(
        'ritual_ZNK12QQuickLayout24ensureLayoutItemsUpdatedE6QFlagsINS_30En'
        'sureLayoutItemsUpdatedOptionEE',
        options.value,
    )

  @overload(QSizeF)
  def rearrange(self, a0: QSizeF) -> None:
    """
    Calls Qt's 'void QQuickLayout::rearrange(const QSizeF &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#rearrange

    Parameters
    ----------

    a0 : QSizeF
      Passed on as a value: Qt reads the C++ QSizeF, which stays Python's
      own.
    """
    #  void QQuickLayout::rearrange(const QSizeF &a0)
    ritual = 'ritual_ZN12QQuickLayout9rearrangeERK6QSizeF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickLayout9rearrangeERK6QSizeF'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(QQuickItem)
  @overload(NoneType)
  def checkAnchors(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickLayout::checkAnchors(QQuickItem *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#checkAnchors

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLayout::checkAnchors(QQuickItem *item) const
    self.uglySide.call(
        'ritual_ZNK12QQuickLayout12checkAnchorsEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      value: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickLayout::itemChange(ItemChange change, const
    ItemChangeData &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    value : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickLayout::itemChange(ItemChange change, const ItemChangeData
    #      &value)
    ritual = (
        'ritual_ZN12QQuickLayout10itemChangeEN10QQuickItem10ItemChangeERKNS'
        '0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickLayout10itemChangeEN10QQuickItem10ItemChang'
          'eERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(value))

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickLayout::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickLayout::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN12QQuickLayout14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickLayout14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  def deactivateRecur(self) -> None:
    """
    Calls Qt's 'void QQuickLayout::deactivateRecur()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#deactivateRecur
    """
    #  void QQuickLayout::deactivateRecur()
    self.uglySide.call('ritual_ZN12QQuickLayout15deactivateRecurEv')

  @overload(QQuickItem)
  @overload(NoneType)
  def itemSiblingOrderChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickLayout::itemSiblingOrderChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html#itemSiblingOrderChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLayout::itemSiblingOrderChanged(QQuickItem *item)
    ritual = 'ritual_ZN12QQuickLayout23itemSiblingOrderChangedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickLayout23itemSiblingOrderChangedEP10QQuickIt'
          'em')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitWidthChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickLayout::itemImplicitWidthChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html#itemImplicitWidthChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLayout::itemImplicitWidthChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN12QQuickLayout24itemImplicitWidthChangedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickLayout24itemImplicitWidthChangedEP10QQuickI'
          'tem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemImplicitHeightChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickLayout::itemImplicitHeightChanged(QQuickItem
    *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html#itemImplicitHeightChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLayout::itemImplicitHeightChanged(QQuickItem *item)
    ritual = (
        'ritual_ZN12QQuickLayout25itemImplicitHeightChangedEP10QQuickItem')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickLayout25itemImplicitHeightChangedEP10QQuick'
          'Item')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemDestroyed(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickLayout::itemDestroyed(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#itemDestroyed

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLayout::itemDestroyed(QQuickItem *item)
    ritual = 'ritual_ZN12QQuickLayout13itemDestroyedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickLayout13itemDestroyedEP10QQuickItem'
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def itemVisibilityChanged(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickLayout::itemVisibilityChanged(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html#itemVisibilityChanged

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLayout::itemVisibilityChanged(QQuickItem *item)
    ritual = 'ritual_ZN12QQuickLayout21itemVisibilityChangedEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQuickLayout21itemVisibilityChangedEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def maybeSubscribeToBaseLineOffsetChanges(
      self,
      item: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void
    QQuickLayout::maybeSubscribeToBaseLineOffsetChanges(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickLayout::maybeSubscribeToBaseLineOffsetChanges(QQuickItem
    #      *item)
    self.uglySide.call(
        'ritual_ZN12QQuickLayout37maybeSubscribeToBaseLineOffsetChangesEP10'
        'QQuickItem',
        self._addressOf(item),
    )

  def _q_dumpLayoutTree(self) -> None:
    """
    Calls Qt's 'void QQuickLayout::_q_dumpLayoutTree() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html#_q_dumpLayoutTree
    """
    #  void QQuickLayout::_q_dumpLayoutTree() const
    self.uglySide.call('ritual_ZNK12QQuickLayout17_q_dumpLayoutTreeEv')

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickLayout::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#updatePolish
    """
    #  void QQuickLayout::updatePolish()
    ritual = 'ritual_ZN12QQuickLayout12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickLayout12updatePolishEv'
    self.uglySide.call(ritual)

  def invalidateSenderItem(self) -> None:
    """
    Calls Qt's 'void QQuickLayout::invalidateSenderItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicklayout.html#invalidateSenderItem
    """
    #  void QQuickLayout::invalidateSenderItem()
    self.uglySide.call('ritual_ZN12QQuickLayout20invalidateSenderItemEv')

  def d_func(self) -> Optional[QQuickLayoutPrivate]:
    """
    Calls Qt's 'QQuickLayoutPrivate *QQuickLayout::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicklayout.html#d_func

    Returns
    -------

    Optional[QQuickLayoutPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickLayoutPrivate *QQuickLayout::d_func()
    address = self.uglySide.call('ritual_ZN12QQuickLayout6d_funcEv')
    from . import QQuickLayoutPrivate
    return QQuickLayoutPrivate._cuteAt(address)

  @staticmethod
  def dumpLayoutTreeRecursive(*__, **_) -> Never:
    """
    Qt's 'void QQuickLayout::dumpLayoutTreeRecursive(int level, QString &buf)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickLayout.dumpLayoutTreeRecursive' has no cute function yet. "
        "Qt's 'void QQuickLayout::dumpLayoutTreeRecursive(int level, "
        "QString &buf) const': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def effectiveSizeHints_helper(*__, **_) -> Never:
    """
    Qt's 'void QQuickLayout::effectiveSizeHints_helper(QQuickItem *item,
    QSizeF *cachedSizeHints, QQuickLayoutAttached **info, bool
    useFallbackToWidthOrHeight)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QQuickLayout.effectiveSizeHints_helper' has no cute function yet. "
        "Qt's 'void QQuickLayout::effectiveSizeHints_helper(QQuickItem "
        "*item, QSizeF *cachedSizeHints, QQuickLayoutAttached **info, bool "
        "useFallbackToWidthOrHeight)': takes a type Python has no way to "
        "hand over yet.")
