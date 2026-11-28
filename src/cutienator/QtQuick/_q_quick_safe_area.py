"""
QQuickSafeArea binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicksafearea_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickSafeArea to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickItemChangeListener

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMarginsF, QMetaObject, QRectF
  from . import QQuickGeometryChange, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMarginsF = WAIT['QMarginsF']
  QQuickGeometryChange = WAIT['QQuickGeometryChange']
  QQuickItem = WAIT['QQuickItem']
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSafeArea(QObject, QQuickItemChangeListener):
  """
  The cute side of Qt's QQuickSafeArea: a plain Python object standing in
  front of one C++ QQuickSafeArea.

  It is built on the cute 'QObject', as Qt's QQuickSafeArea is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQuickItemChangeListener' as well, as Qt's QQuickSafeArea is built on Qt's
  QQuickItemChangeListener too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSafeArea that has a ritual and that Python can
  call so far, 15 names in all: 'metaObject', 'tr', 'qmlAttachedProperties',
  'margins', 'additionalMargins', 'setAdditionalMargins',
  'updateSafeAreasRecursively', 'marginsChanged', 'additionalMarginsChanged',
  'windowChanged', 'updateSafeArea', 'itemTransformChanged',
  'itemGeometryChanged', 'addSourceItem', 'removeSourceItem'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSafeArea::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickSafeArea::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickSafeArea::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'void QQuickSafeArea::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQuickSafeArea::~QQuickSafeArea()': the destructor: Python never
    removes a C++ QQuickSafeArea.
  - Qt's 'QDebug operator<<(QDebug debug, const QQuickSafeArea *safeArea)':
    an operator between other classes, written inside this one.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickSafeArea is created at the first use, not by
    'QQuickSafeArea(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSafeArea.
  - Qt tells when it has removed the C++ QQuickSafeArea. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QQuickSafeArea::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksafearea.html#tr

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
    #  QString QQuickSafeArea::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickSafeArea2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      attachee: Optional[QObject],
  ) -> Optional[QQuickSafeArea]:
    """
    Calls Qt's 'QQuickSafeArea *QQuickSafeArea::qmlAttachedProperties(QObject
    *attachee)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksafearea.html#qmlAttachedProperties

    Parameters
    ----------

    attachee : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickSafeArea]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSafeArea *QQuickSafeArea::qmlAttachedProperties(QObject
    #      *attachee)
    address = Rituals.call(
        'ritual_ZN14QQuickSafeArea21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(attachee, 'QObject'),
    )
    return QQuickSafeArea._cuteAt(address)

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def updateSafeAreasRecursively(fromItem: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSafeArea::updateSafeAreasRecursively(QQuickItem
    *fromItem)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksafearea.html#updateSafeAreasRecursively

    Parameters
    ----------

    fromItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSafeArea::updateSafeAreasRecursively(QQuickItem *fromItem)
    Rituals.call(
        'ritual_ZN14QQuickSafeArea26updateSafeAreasRecursivelyEP10QQuickIte'
        'm',
        CuteMixin._addressOf(fromItem),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSafeArea'

  #  Qt's QQuickSafeArea is built on more than one class. The part of a C++
  #  QQuickSafeArea that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQuickItemChangeListener':
          'ritual_cast_QQuickSafeArea_QQuickItemChangeListener',
  }

  #  A C++ QQuickSafeArea Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSafeArea'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSafeArea::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksafearea.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSafeArea::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickSafeArea10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def margins(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQuickSafeArea::margins() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksafearea.html#margins

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQuickSafeArea::margins() const
    address = self.uglySide.call('ritual_ZNK14QQuickSafeArea7marginsEv')
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  def additionalMargins(self) -> QMarginsF:
    """
    Calls Qt's 'QMarginsF QQuickSafeArea::additionalMargins() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksafearea.html#additionalMargins

    Returns
    -------

    QMarginsF
      A new cute QMarginsF around the copy Qt gave back. Python owns it.
    """
    #  QMarginsF QQuickSafeArea::additionalMargins() const
    address = self.uglySide.call(
        'ritual_ZNK14QQuickSafeArea17additionalMarginsEv',
    )
    from ..QtCore import QMarginsF
    return QMarginsF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMarginsF)
  def setAdditionalMargins(self, additionalMargins: QMarginsF) -> None:
    """
    Calls Qt's 'void QQuickSafeArea::setAdditionalMargins(const QMarginsF
    &additionalMargins)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksafearea.html#setAdditionalMargins

    Parameters
    ----------

    additionalMargins : QMarginsF
      Passed on as a value: Qt reads the C++ QMarginsF, which stays Python's
      own.
    """
    #  void QQuickSafeArea::setAdditionalMargins(const QMarginsF
    #      &additionalMargins)
    self.uglySide.call(
        'ritual_ZN14QQuickSafeArea20setAdditionalMarginsERK9QMarginsF',
        self._valueOf(additionalMargins),
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, attachee: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickSafeArea::QQuickSafeArea(QQuickItem
    *attachee)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicksafearea.html#QQuickSafeArea

    Parameters
    ----------

    attachee : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSafeArea::QQuickSafeArea(QQuickItem *attachee)
    self._noteCreation(QQuickSafeArea, lambda: Rituals.call(
        'ritual_ZN14QQuickSafeAreaC1EP10QQuickItem',
        self._addressOf(attachee),
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

  def marginsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSafeArea::marginsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksafearea.html#marginsChanged
    """
    #  void QQuickSafeArea::marginsChanged()
    self.uglySide.call('ritual_ZN14QQuickSafeArea14marginsChangedEv')

  def additionalMarginsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSafeArea::additionalMarginsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksafearea.html#additionalMarginsChanged
    """
    #  void QQuickSafeArea::additionalMarginsChanged()
    self.uglySide.call(
        'ritual_ZN14QQuickSafeArea24additionalMarginsChangedEv',
    )

  def windowChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSafeArea::windowChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksafearea.html#windowChanged
    """
    #  void QQuickSafeArea::windowChanged()
    self.uglySide.call('ritual_ZN14QQuickSafeArea13windowChangedEv')

  def updateSafeArea(self) -> None:
    """
    Calls Qt's 'void QQuickSafeArea::updateSafeArea()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksafearea.html#updateSafeArea
    """
    #  void QQuickSafeArea::updateSafeArea()
    self.uglySide.call('ritual_ZN14QQuickSafeArea14updateSafeAreaEv')

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def itemTransformChanged(
      self,
      a0: Optional[QQuickItem],
      a1: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickSafeArea::itemTransformChanged(QQuickItem *a0,
    QQuickItem *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksafearea.html#itemTransformChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSafeArea::itemTransformChanged(QQuickItem *a0, QQuickItem
    #      *a1)
    ritual = (
        'ritual_ZN14QQuickSafeArea20itemTransformChangedEP10QQuickItemS1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickSafeArea20itemTransformChangedEP10QQuickIte'
          'mS1_')
    self.uglySide.call(ritual, self._addressOf(a0), self._addressOf(a1))

  @overload(QQuickItem, QQuickGeometryChange, QRectF)
  @overload(NoneType, QQuickGeometryChange, QRectF)
  def itemGeometryChanged(
      self,
      a0: Optional[QQuickItem],
      a1: QQuickGeometryChange,
      a2: QRectF,
  ) -> None:
    """
    Calls Qt's 'void QQuickSafeArea::itemGeometryChanged(QQuickItem *a0,
    QQuickGeometryChange a1, const QRectF &a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksafearea.html#itemGeometryChanged

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QQuickGeometryChange
      Passed on as a value: Qt reads the C++ QQuickGeometryChange, which
      stays Python's own.

    a2 : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickSafeArea::itemGeometryChanged(QQuickItem *a0,
    #      QQuickGeometryChange a1, const QRectF &a2)
    ritual = (
        'ritual_ZN14QQuickSafeArea19itemGeometryChangedEP10QQuickItem20QQui'
        'ckGeometryChangeRK6QRectF')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickSafeArea19itemGeometryChangedEP10QQuickItem'
          '20QQuickGeometryChangeRK6QRectF')
    self.uglySide.call(
        ritual, self._addressOf(a0), self._valueOf(a1), self._valueOf(a2),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def addSourceItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSafeArea::addSourceItem(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksafearea.html#addSourceItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSafeArea::addSourceItem(QQuickItem *item)
    ritual = 'ritual_ZN14QQuickSafeArea13addSourceItemEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuickSafeArea13addSourceItemEP10QQuickItem'
    self.uglySide.call(ritual, self._addressOf(item))

  @overload(QQuickItem)
  @overload(NoneType)
  def removeSourceItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSafeArea::removeSourceItem(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksafearea.html#removeSourceItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSafeArea::removeSourceItem(QQuickItem *item)
    ritual = 'ritual_ZN14QQuickSafeArea16removeSourceItemEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuickSafeArea16removeSourceItemEP10QQuickItem')
    self.uglySide.call(ritual, self._addressOf(item))
