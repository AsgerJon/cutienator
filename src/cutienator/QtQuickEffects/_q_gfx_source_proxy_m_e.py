"""
QGfxSourceProxyME binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickEffects/6.12.0/QtQuickEffects/private/qgfxsourceproxy_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QGfxSourceProxyME to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQuick import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QRectF

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGfxSourceProxyME(QQuickItem):
  """
  The cute side of Qt's QGfxSourceProxyME: a plain Python object standing in
  front of one C++ QGfxSourceProxyME.

  It is built on the cute 'QQuickItem', as Qt's QGfxSourceProxyME is built on
  Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGfxSourceProxyME that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'input', 'output',
  'sourceRect', 'isActive', 'interpolation', 'updatePolish', 'inputChanged',
  'outputChanged', 'sourceRectChanged', 'activeChanged',
  'interpolationChanged', 'repolish', 'findLayer'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QGfxSourceProxyME::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QGfxSourceProxyME::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QGfxSourceProxyME::~QGfxSourceProxyME()': the destructor: Python
    never removes a C++ QGfxSourceProxyME.

  What has no ritual
  ------------------

  10 of the 27 functions Qt declares: 8 leans on 'QGfxSourceProxyME; 2 not a
  gap.

  What to expect
  --------------

  - The C++ QGfxSourceProxyME is created at the first use, not by
    'QGfxSourceProxyME(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGfxSourceProxyME.
  - Qt tells when it has removed the C++ QGfxSourceProxyME. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QGfxSourceProxyME that has no cute function yet,
    '__init__', 'resetInput', 'setInput', 'setInterpolation', 'setOutput',
    'setSourceRect', 'useProxy', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGfxSourceProxyME, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Interpolation(CuteNum, scoped=True):
    """
    The enum 'QGfxSourceProxyME::Interpolation' of Qt, with the 3 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Any = Kee[int](0)
    Nearest = Kee[int](1)
    Linear = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickItem)
  @overload(NoneType)
  def findLayer(a0: Optional[QQuickItem]) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QGfxSourceProxyME::findLayer(QQuickItem *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qgfxsourceproxyme.html#findLayer

    Parameters
    ----------

    a0 : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QGfxSourceProxyME::findLayer(QQuickItem *a0)
    address = Rituals.call(
        'ritual_ZN17QGfxSourceProxyME9findLayerEP10QQuickItem',
        CuteMixin._addressOf(a0),
    )
    return QObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGfxSourceProxyME'

  #  A C++ QGfxSourceProxyME Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGfxSourceProxyME'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QGfxSourceProxyME::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgfxsourceproxyme.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QGfxSourceProxyME::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QGfxSourceProxyME10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def input(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QGfxSourceProxyME::input() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgfxsourceproxyme.html#input

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QGfxSourceProxyME::input() const
    address = self.uglySide.call('ritual_ZNK17QGfxSourceProxyME5inputEv')
    return QQuickItem._cuteAt(address)

  def output(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QGfxSourceProxyME::output() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgfxsourceproxyme.html#output

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QGfxSourceProxyME::output() const
    address = self.uglySide.call('ritual_ZNK17QGfxSourceProxyME6outputEv')
    return QQuickItem._cuteAt(address)

  def sourceRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QGfxSourceProxyME::sourceRect() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgfxsourceproxyme.html#sourceRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QGfxSourceProxyME::sourceRect() const
    address = self.uglySide.call(
        'ritual_ZNK17QGfxSourceProxyME10sourceRectEv',
    )
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QGfxSourceProxyME::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgfxsourceproxyme.html#isActive
    """
    #  bool QGfxSourceProxyME::isActive() const
    return self.uglySide.call('ritual_ZNK17QGfxSourceProxyME8isActiveEv')

  def interpolation(self) -> Interpolation:
    """
    Calls Qt's 'Interpolation QGfxSourceProxyME::interpolation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgfxsourceproxyme.html#interpolation

    Returns
    -------

    Interpolation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Interpolation(number)'
      gives.
    """
    #  Interpolation QGfxSourceProxyME::interpolation() const
    return QGfxSourceProxyME.Interpolation(self.uglySide.call(
        'ritual_ZNK17QGfxSourceProxyME13interpolationEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QGfxSourceProxyME::QGfxSourceProxyME(QQuickItem *parentItem)':
    leans on 'QGfxSourceProxyME::qt_metacall(QMetaObject::Call, int,
    void**)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGfxSourceProxyME.__init__' has no cute function yet. Qt's "
        "'QGfxSourceProxyME::QGfxSourceProxyME(QQuickItem *parentItem)': "
        "leans on 'QGfxSourceProxyME::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QGfxSourceProxyME::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgfxsourceproxyme.html#updatePolish
    """
    #  void QGfxSourceProxyME::updatePolish()
    self.uglySide.call('ritual_ZN17QGfxSourceProxyME12updatePolishEv')

  def inputChanged(self) -> None:
    """
    Calls Qt's 'void QGfxSourceProxyME::inputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgfxsourceproxyme.html#inputChanged
    """
    #  void QGfxSourceProxyME::inputChanged()
    self.uglySide.call('ritual_ZN17QGfxSourceProxyME12inputChangedEv')

  def outputChanged(self) -> None:
    """
    Calls Qt's 'void QGfxSourceProxyME::outputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgfxsourceproxyme.html#outputChanged
    """
    #  void QGfxSourceProxyME::outputChanged()
    self.uglySide.call('ritual_ZN17QGfxSourceProxyME13outputChangedEv')

  def sourceRectChanged(self) -> None:
    """
    Calls Qt's 'void QGfxSourceProxyME::sourceRectChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgfxsourceproxyme.html#sourceRectChanged
    """
    #  void QGfxSourceProxyME::sourceRectChanged()
    self.uglySide.call('ritual_ZN17QGfxSourceProxyME17sourceRectChangedEv')

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QGfxSourceProxyME::activeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgfxsourceproxyme.html#activeChanged
    """
    #  void QGfxSourceProxyME::activeChanged()
    self.uglySide.call('ritual_ZN17QGfxSourceProxyME13activeChangedEv')

  def interpolationChanged(self) -> None:
    """
    Calls Qt's 'void QGfxSourceProxyME::interpolationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgfxsourceproxyme.html#interpolationChanged
    """
    #  void QGfxSourceProxyME::interpolationChanged()
    self.uglySide.call(
        'ritual_ZN17QGfxSourceProxyME20interpolationChangedEv',
    )

  def repolish(self) -> None:
    """
    Calls Qt's 'void QGfxSourceProxyME::repolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qgfxsourceproxyme.html#repolish
    """
    #  void QGfxSourceProxyME::repolish()
    self.uglySide.call('ritual_ZN17QGfxSourceProxyME8repolishEv')

  @staticmethod
  def resetInput(*__, **_) -> Never:
    """
    Qt's 'void QGfxSourceProxyME::resetInput()': leans on
    'QGfxSourceProxyME::inputChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGfxSourceProxyME.resetInput' has no cute function yet. Qt's "
        "'void QGfxSourceProxyME::resetInput()': leans on "
        "'QGfxSourceProxyME::inputChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setInput(*__, **_) -> Never:
    """
    Qt's 'void QGfxSourceProxyME::setInput(QQuickItem *input)': leans on
    'QGfxSourceProxyME::inputChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGfxSourceProxyME.setInput' has no cute function yet. Qt's 'void "
        "QGfxSourceProxyME::setInput(QQuickItem *input)': leans on "
        "'QGfxSourceProxyME::inputChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setInterpolation(*__, **_) -> Never:
    """
    Qt's 'void QGfxSourceProxyME::setInterpolation(Interpolation i)': leans
    on 'QGfxSourceProxyME::interpolationChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGfxSourceProxyME.setInterpolation' has no cute function yet. "
        "Qt's 'void QGfxSourceProxyME::setInterpolation(Interpolation i)': "
        "leans on 'QGfxSourceProxyME::interpolationChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def setOutput(*__, **_) -> Never:
    """
    Qt's 'void QGfxSourceProxyME::setOutput(QQuickItem *output)': leans on
    'QGfxSourceProxyME::activeChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGfxSourceProxyME.setOutput' has no cute function yet. Qt's 'void "
        "QGfxSourceProxyME::setOutput(QQuickItem *output)': leans on "
        "'QGfxSourceProxyME::activeChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setSourceRect(*__, **_) -> Never:
    """
    Qt's 'void QGfxSourceProxyME::setSourceRect(const QRectF &sourceRect)':
    leans on 'QGfxSourceProxyME::sourceRectChanged()', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGfxSourceProxyME.setSourceRect' has no cute function yet. Qt's "
        "'void QGfxSourceProxyME::setSourceRect(const QRectF &sourceRect)': "
        "leans on 'QGfxSourceProxyME::sourceRectChanged()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def useProxy(*__, **_) -> Never:
    """
    Qt's 'void QGfxSourceProxyME::useProxy()': leans on
    'QGfxSourceProxyME::activeChanged()', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QGfxSourceProxyME.useProxy' has no cute function yet. Qt's 'void "
        "QGfxSourceProxyME::useProxy()': leans on "
        "'QGfxSourceProxyME::activeChanged()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
