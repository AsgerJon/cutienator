"""
QQuickAnchorSet binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickstateoperations_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickAnchorSet to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QQmlScriptString
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlScriptString = WAIT['QQmlScriptString']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnchorSet(QObject):
  """
  The cute side of Qt's QQuickAnchorSet: a plain Python object standing in
  front of one C++ QQuickAnchorSet.

  It is built on the cute 'QObject', as Qt's QQuickAnchorSet is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnchorSet that has a ritual and that Python
  can call so far, 23 names in all: 'metaObject', 'tr', 'left', 'setLeft',
  'resetLeft', 'right', 'setRight', 'resetRight', 'horizontalCenter',
  'setHorizontalCenter', 'resetHorizontalCenter', 'top', 'setTop',
  'resetTop', 'bottom', 'setBottom', 'resetBottom', 'verticalCenter',
  'setVerticalCenter', 'resetVerticalCenter', 'baseline', 'setBaseline',
  'resetBaseline'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAnchorSet::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickAnchorSet::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickAnchorSet::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'QQuickAnchorSet::~QQuickAnchorSet()': the destructor: Python never
    removes a C++ QQuickAnchorSet.
  - Qt's 'QQuickAnchorSetPrivate *QQuickAnchorSet::d_func()': gives
    'QQuickAnchorSetPrivate', which has no cute class yet.
  - Qt's 'const QQuickAnchorSetPrivate *QQuickAnchorSet::d_func() const':
    gives 'QQuickAnchorSetPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 35 functions Qt declares: 2 not a gap; 2 forbidden; 1 cannot be
  called and cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QQuickAnchorSet is created at the first use, not by
    'QQuickAnchorSet(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnchorSet.
  - Qt tells when it has removed the C++ QQuickAnchorSet. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickAnchorSet that has no cute function yet,
    'usedAnchors', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QQuickAnchorSet::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#tr

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
    #  QString QQuickAnchorSet::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickAnchorSet2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnchorSet'

  #  A C++ QQuickAnchorSet Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnchorSet'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAnchorSet::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAnchorSet::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickAnchorSet10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def left(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickAnchorSet::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#left

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickAnchorSet::left() const
    address = self.uglySide.call('ritual_ZNK15QQuickAnchorSet4leftEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def right(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickAnchorSet::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#right

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickAnchorSet::right() const
    address = self.uglySide.call('ritual_ZNK15QQuickAnchorSet5rightEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def horizontalCenter(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickAnchorSet::horizontalCenter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorset.html#horizontalCenter

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickAnchorSet::horizontalCenter() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickAnchorSet16horizontalCenterEv',
    )
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def top(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickAnchorSet::top() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#top

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickAnchorSet::top() const
    address = self.uglySide.call('ritual_ZNK15QQuickAnchorSet3topEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def bottom(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickAnchorSet::bottom() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#bottom

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickAnchorSet::bottom() const
    address = self.uglySide.call('ritual_ZNK15QQuickAnchorSet6bottomEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def verticalCenter(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickAnchorSet::verticalCenter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorset.html#verticalCenter

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickAnchorSet::verticalCenter() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickAnchorSet14verticalCenterEv',
    )
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  def baseline(self) -> QQmlScriptString:
    """
    Calls Qt's 'QQmlScriptString QQuickAnchorSet::baseline() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#baseline

    Returns
    -------

    QQmlScriptString
      A new cute QQmlScriptString around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlScriptString QQuickAnchorSet::baseline() const
    address = self.uglySide.call('ritual_ZNK15QQuickAnchorSet8baselineEv')
    from ..QtQml import QQmlScriptString
    return QQmlScriptString._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlScriptString)
  def setLeft(self, edge: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::setLeft(const QQmlScriptString &edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#setLeft

    Parameters
    ----------

    edge : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickAnchorSet::setLeft(const QQmlScriptString &edge)
    self.uglySide.call(
        'ritual_ZN15QQuickAnchorSet7setLeftERK16QQmlScriptString',
        self._valueOf(edge),
    )

  @overload(QQmlScriptString)
  def setRight(self, edge: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::setRight(const QQmlScriptString
    &edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#setRight

    Parameters
    ----------

    edge : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickAnchorSet::setRight(const QQmlScriptString &edge)
    self.uglySide.call(
        'ritual_ZN15QQuickAnchorSet8setRightERK16QQmlScriptString',
        self._valueOf(edge),
    )

  @overload(QQmlScriptString)
  def setHorizontalCenter(self, edge: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::setHorizontalCenter(const
    QQmlScriptString &edge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorset.html#setHorizontalCenter

    Parameters
    ----------

    edge : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickAnchorSet::setHorizontalCenter(const QQmlScriptString
    #      &edge)
    self.uglySide.call(
        'ritual_ZN15QQuickAnchorSet19setHorizontalCenterERK16QQmlScriptStri'
        'ng',
        self._valueOf(edge),
    )

  @overload(QQmlScriptString)
  def setTop(self, edge: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::setTop(const QQmlScriptString &edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#setTop

    Parameters
    ----------

    edge : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickAnchorSet::setTop(const QQmlScriptString &edge)
    self.uglySide.call(
        'ritual_ZN15QQuickAnchorSet6setTopERK16QQmlScriptString',
        self._valueOf(edge),
    )

  @overload(QQmlScriptString)
  def setBottom(self, edge: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::setBottom(const QQmlScriptString
    &edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#setBottom

    Parameters
    ----------

    edge : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickAnchorSet::setBottom(const QQmlScriptString &edge)
    self.uglySide.call(
        'ritual_ZN15QQuickAnchorSet9setBottomERK16QQmlScriptString',
        self._valueOf(edge),
    )

  @overload(QQmlScriptString)
  def setVerticalCenter(self, edge: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::setVerticalCenter(const
    QQmlScriptString &edge)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorset.html#setVerticalCenter

    Parameters
    ----------

    edge : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickAnchorSet::setVerticalCenter(const QQmlScriptString &edge)
    self.uglySide.call(
        'ritual_ZN15QQuickAnchorSet17setVerticalCenterERK16QQmlScriptString',
        self._valueOf(edge),
    )

  @overload(QQmlScriptString)
  def setBaseline(self, edge: QQmlScriptString) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::setBaseline(const QQmlScriptString
    &edge)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#setBaseline

    Parameters
    ----------

    edge : QQmlScriptString
      Passed on as a value: Qt reads the C++ QQmlScriptString, which stays
      Python's own.
    """
    #  void QQuickAnchorSet::setBaseline(const QQmlScriptString &edge)
    self.uglySide.call(
        'ritual_ZN15QQuickAnchorSet11setBaselineERK16QQmlScriptString',
        self._valueOf(edge),
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
    Notes what was given, for Qt's 'QQuickAnchorSet::QQuickAnchorSet(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorset.html#QQuickAnchorSet

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAnchorSet::QQuickAnchorSet(QObject *parent)
    self._noteCreation(QQuickAnchorSet, lambda: Rituals.call(
        'ritual_ZN15QQuickAnchorSetC1EP7QObject',
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

  def resetLeft(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::resetLeft()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#resetLeft
    """
    #  void QQuickAnchorSet::resetLeft()
    self.uglySide.call('ritual_ZN15QQuickAnchorSet9resetLeftEv')

  def resetRight(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::resetRight()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#resetRight
    """
    #  void QQuickAnchorSet::resetRight()
    self.uglySide.call('ritual_ZN15QQuickAnchorSet10resetRightEv')

  def resetHorizontalCenter(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::resetHorizontalCenter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorset.html#resetHorizontalCenter
    """
    #  void QQuickAnchorSet::resetHorizontalCenter()
    self.uglySide.call('ritual_ZN15QQuickAnchorSet21resetHorizontalCenterEv')

  def resetTop(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::resetTop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#resetTop
    """
    #  void QQuickAnchorSet::resetTop()
    self.uglySide.call('ritual_ZN15QQuickAnchorSet8resetTopEv')

  def resetBottom(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::resetBottom()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#resetBottom
    """
    #  void QQuickAnchorSet::resetBottom()
    self.uglySide.call('ritual_ZN15QQuickAnchorSet11resetBottomEv')

  def resetVerticalCenter(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::resetVerticalCenter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanchorset.html#resetVerticalCenter
    """
    #  void QQuickAnchorSet::resetVerticalCenter()
    self.uglySide.call('ritual_ZN15QQuickAnchorSet19resetVerticalCenterEv')

  def resetBaseline(self) -> None:
    """
    Calls Qt's 'void QQuickAnchorSet::resetBaseline()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanchorset.html#resetBaseline
    """
    #  void QQuickAnchorSet::resetBaseline()
    self.uglySide.call('ritual_ZN15QQuickAnchorSet13resetBaselineEv')

  @staticmethod
  def usedAnchors(*__, **_) -> Never:
    """
    Qt's 'QQuickAnchors::Anchors QQuickAnchorSet::usedAnchors() const':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuickAnchorSet.usedAnchors' has no cute function yet. Qt's "
        "'QQuickAnchors::Anchors QQuickAnchorSet::usedAnchors() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
