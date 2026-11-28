"""
QQuick3DInstanceRange binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/randominstancing_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DInstanceRange to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QVariant
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from ..QtQuick3D import QQuick3DObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DObject = WAIT['QQuick3DObject']
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DInstanceRange(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DInstanceRange: a plain Python object standing
  in front of one C++ QQuick3DInstanceRange.

  What exists
  -----------

  Every function of Qt's QQuick3DInstanceRange that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'from_', 'to',
  'proportional', 'setFrom', 'setTo', 'setProportional', 'fromChanged',
  'toChanged', 'proportionalChanged', 'changed', 'updateSpatialNode'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DInstanceRange::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DInstanceRange::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DInstanceRange::~QQuick3DInstanceRange()': the destructor:
    Python never removes a C++ QQuick3DInstanceRange.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DInstanceRange is created at the first use, not by
    'QQuick3DInstanceRange(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DInstanceRange.
  - Qt tells when it has removed the C++ QQuick3DInstanceRange. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuick3DInstanceRange::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dinstancerange.html#tr

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
    #  QString QQuick3DInstanceRange::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuick3DInstanceRange2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DInstanceRange'

  #  A C++ QQuick3DInstanceRange Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DInstanceRange'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DInstanceRange::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancerange.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DInstanceRange::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DInstanceRange10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def from_(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuick3DInstanceRange::from() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dinstancerange.html#from

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuick3DInstanceRange::from() const
    address = self.uglySide.call('ritual_ZNK21QQuick3DInstanceRange4fromEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def to(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuick3DInstanceRange::to() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dinstancerange.html#to

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuick3DInstanceRange::to() const
    address = self.uglySide.call('ritual_ZNK21QQuick3DInstanceRange2toEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def proportional(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DInstanceRange::proportional() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancerange.html#proportional
    """
    #  bool QQuick3DInstanceRange::proportional() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DInstanceRange12proportionalEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setFrom(self, from_: QVariant) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceRange::setFrom(QVariant from)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dinstancerange.html#setFrom

    Parameters
    ----------

    from_ : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuick3DInstanceRange::setFrom(QVariant from)
    self.uglySide.call(
        'ritual_ZN21QQuick3DInstanceRange7setFromE8QVariant',
        self._valueOf(from_),
    )

  @overload(QVariant)
  def setTo(self, to: QVariant) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceRange::setTo(QVariant to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dinstancerange.html#setTo

    Parameters
    ----------

    to : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQuick3DInstanceRange::setTo(QVariant to)
    self.uglySide.call(
        'ritual_ZN21QQuick3DInstanceRange5setToE8QVariant',
        self._valueOf(to),
    )

  @overload(bool)
  def setProportional(self, proportional: bool) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceRange::setProportional(bool
    proportional)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancerange.html#setProportional

    Parameters
    ----------

    proportional : bool
      Passed on as it is.
    """
    #  void QQuick3DInstanceRange::setProportional(bool proportional)
    self.uglySide.call(
        'ritual_ZN21QQuick3DInstanceRange15setProportionalEb', proportional,
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DInstanceRange::QQuick3DInstanceRange(QQuick3DObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancerange.html#QQuick3DInstanceRange

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DInstanceRange::QQuick3DInstanceRange(QQuick3DObject *parent)
    self._noteCreation(QQuick3DInstanceRange, lambda: Rituals.call(
        'ritual_ZN21QQuick3DInstanceRangeC1EP14QQuick3DObject',
        self._addressOf(parent),
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

  def fromChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceRange::fromChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancerange.html#fromChanged
    """
    #  void QQuick3DInstanceRange::fromChanged()
    self.uglySide.call('ritual_ZN21QQuick3DInstanceRange11fromChangedEv')

  def toChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceRange::toChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancerange.html#toChanged
    """
    #  void QQuick3DInstanceRange::toChanged()
    self.uglySide.call('ritual_ZN21QQuick3DInstanceRange9toChangedEv')

  def proportionalChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceRange::proportionalChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancerange.html#proportionalChanged
    """
    #  void QQuick3DInstanceRange::proportionalChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DInstanceRange19proportionalChangedEv',
    )

  def changed(self) -> None:
    """
    Calls Qt's 'void QQuick3DInstanceRange::changed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dinstancerange.html#changed
    """
    #  void QQuick3DInstanceRange::changed()
    self.uglySide.call('ritual_ZN21QQuick3DInstanceRange7changedEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      a0: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DInstanceRange::updateSpatialNode(QSSGRenderGraphObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dinstancerange.html#updateSpatialNode

    Parameters
    ----------

    a0 : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DInstanceRange::updateSpatialNode(QSSGRenderGraphObject
    #      *a0)
    ritual = (
        'ritual_ZN21QQuick3DInstanceRange17updateSpatialNodeEP21QSSGRenderG'
        'raphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuick3DInstanceRange17updateSpatialNodeEP21QSSGR'
          'enderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)
