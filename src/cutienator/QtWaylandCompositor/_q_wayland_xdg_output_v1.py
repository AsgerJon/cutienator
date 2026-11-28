"""
QWaylandXdgOutputV1 binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWaylandCompositor/qwaylandxdgoutputv1.h, Qt 6.12.0. Changes made here
#  are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QSize
  from . import QWaylandOutput, QWaylandXdgOutputManagerV1
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']
  QWaylandOutput = WAIT['QWaylandOutput']
  QWaylandXdgOutputManagerV1 = WAIT['QWaylandXdgOutputManagerV1']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWaylandXdgOutputV1(QObject):
  """
  The cute side of Qt's QWaylandXdgOutputV1: a plain Python object standing
  in front of one C++ QWaylandXdgOutputV1.

  It is built on the cute 'QObject', as Qt's QWaylandXdgOutputV1 is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QWaylandXdgOutputV1 that has a ritual and that
  Python can call so far, 20 names in all: 'metaObject', 'tr', 'manager',
  'output', 'name', 'setName', 'description', 'setDescription',
  'logicalPosition', 'setLogicalPosition', 'logicalSize', 'setLogicalSize',
  'logicalGeometry', 'managerChanged', 'outputChanged',
  'logicalPositionChanged', 'logicalSizeChanged', 'logicalGeometryChanged',
  'nameChanged', 'descriptionChanged'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWaylandXdgOutputV1::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWaylandXdgOutputV1::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QWaylandXdgOutputV1Private *QWaylandXdgOutputV1::d_func()': gives
    'QWaylandXdgOutputV1Private', which has no cute class yet.
  - Qt's 'const QWaylandXdgOutputV1Private *QWaylandXdgOutputV1::d_func()
    const': gives 'QWaylandXdgOutputV1Private', which has no cute class yet.
  - Qt's 'QQmlListProperty<QObject> QWaylandXdgOutputV1::data()': gives a
    type Python has no way to take yet.
  - Qt's 'void QWaylandXdgOutputV1::appendFunction(QQmlListProperty<QObject>
    *list, QObject *object)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'qsizetype
    QWaylandXdgOutputV1::countFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QWaylandXdgOutputV1::atFunction(QQmlListProperty<QObject>
    *list, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
  - Qt's 'void QWaylandXdgOutputV1::clearFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QWaylandXdgOutputV1::~QWaylandXdgOutputV1()': the destructor:
    Python never removes a C++ QWaylandXdgOutputV1.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QWaylandXdgOutputV1 is created at the first use, not by
    'QWaylandXdgOutputV1(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWaylandXdgOutputV1.
  - Qt tells when it has removed the C++ QWaylandXdgOutputV1. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QWaylandXdgOutputV1 that has no cute function yet,
    'appendFunction', 'atFunction', 'clearFunction', 'countFunction', 'data',
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
    Calls Qt's 'QString QWaylandXdgOutputV1::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#tr

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
    #  QString QWaylandXdgOutputV1::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QWaylandXdgOutputV12trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWaylandXdgOutputV1'

  #  A C++ QWaylandXdgOutputV1 Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QWaylandXdgOutputV1'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWaylandXdgOutputV1::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWaylandXdgOutputV1::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QWaylandXdgOutputV110metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def manager(self) -> Optional[QWaylandXdgOutputManagerV1]:
    """
    Calls Qt's 'QWaylandXdgOutputManagerV1 *QWaylandXdgOutputV1::manager()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#manager

    Returns
    -------

    Optional[QWaylandXdgOutputManagerV1]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandXdgOutputManagerV1 *QWaylandXdgOutputV1::manager() const
    address = self.uglySide.call('ritual_ZNK19QWaylandXdgOutputV17managerEv')
    from . import QWaylandXdgOutputManagerV1
    return QWaylandXdgOutputManagerV1._cuteAt(address)

  def output(self) -> Optional[QWaylandOutput]:
    """
    Calls Qt's 'QWaylandOutput *QWaylandXdgOutputV1::output() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#output

    Returns
    -------

    Optional[QWaylandOutput]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWaylandOutput *QWaylandXdgOutputV1::output() const
    address = self.uglySide.call('ritual_ZNK19QWaylandXdgOutputV16outputEv')
    from . import QWaylandOutput
    return QWaylandOutput._cuteAt(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QWaylandXdgOutputV1::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandXdgOutputV1::name() const
    return self.uglySide.call('ritual_ZNK19QWaylandXdgOutputV14nameEv')

  def description(self) -> str:
    """
    Calls Qt's 'QString QWaylandXdgOutputV1::description() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#description

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QWaylandXdgOutputV1::description() const
    return self.uglySide.call(
        'ritual_ZNK19QWaylandXdgOutputV111descriptionEv',
    )

  def logicalPosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint QWaylandXdgOutputV1::logicalPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#logicalPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QWaylandXdgOutputV1::logicalPosition() const
    address = self.uglySide.call(
        'ritual_ZNK19QWaylandXdgOutputV115logicalPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def logicalSize(self) -> QSize:
    """
    Calls Qt's 'QSize QWaylandXdgOutputV1::logicalSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#logicalSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QWaylandXdgOutputV1::logicalSize() const
    address = self.uglySide.call(
        'ritual_ZNK19QWaylandXdgOutputV111logicalSizeEv',
    )
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def logicalGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QWaylandXdgOutputV1::logicalGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#logicalGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QWaylandXdgOutputV1::logicalGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK19QWaylandXdgOutputV115logicalGeometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QWaylandXdgOutputV1::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWaylandXdgOutputV1::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgOutputV17setNameERK7QString', name,
    )

  @overload(str)
  def setDescription(self, name: str) -> None:
    """
    Calls Qt's 'void QWaylandXdgOutputV1::setDescription(const QString
    &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#setDescription

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QWaylandXdgOutputV1::setDescription(const QString &name)
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgOutputV114setDescriptionERK7QString', name,
    )

  @overload(QPoint)
  def setLogicalPosition(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QWaylandXdgOutputV1::setLogicalPosition(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#setLogicalPosition

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QWaylandXdgOutputV1::setLogicalPosition(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgOutputV118setLogicalPositionERK6QPoint',
        self._valueOf(position),
    )

  @overload(QSize)
  def setLogicalSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QWaylandXdgOutputV1::setLogicalSize(const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#setLogicalSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QWaylandXdgOutputV1::setLogicalSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgOutputV114setLogicalSizeERK5QSize',
        self._valueOf(size),
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
    'QWaylandXdgOutputV1::QWaylandXdgOutputV1()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#QWaylandXdgOutputV1
    """
    #  QWaylandXdgOutputV1::QWaylandXdgOutputV1()
    self._noteCreation(QWaylandXdgOutputV1, lambda: Rituals.call(
        'ritual_ZN19QWaylandXdgOutputV1C1Ev',
    ))

  @overload(QWaylandOutput, QWaylandXdgOutputManagerV1)
  @overload(QWaylandOutput, NoneType)
  @overload(NoneType, QWaylandXdgOutputManagerV1)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      output: Optional[QWaylandOutput],
      manager: Optional[QWaylandXdgOutputManagerV1],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QWaylandXdgOutputV1::QWaylandXdgOutputV1(QWaylandOutput *output,
    QWaylandXdgOutputManagerV1 *manager)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#QWaylandXdgOutputV1

    Parameters
    ----------

    output : Optional[QWaylandOutput]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    manager : Optional[QWaylandXdgOutputManagerV1]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWaylandXdgOutputV1::QWaylandXdgOutputV1(QWaylandOutput *output,
    #      QWaylandXdgOutputManagerV1 *manager)
    self._noteCreation(QWaylandXdgOutputV1, lambda: Rituals.call(
        'ritual_ZN19QWaylandXdgOutputV1C1EP14QWaylandOutputP26QWaylandXdgOu'
        'tputManagerV1',
        self._addressOf(output), self._addressOf(manager),
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

  def managerChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgOutputV1::managerChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#managerChanged
    """
    #  void QWaylandXdgOutputV1::managerChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgOutputV114managerChangedEv')

  def outputChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgOutputV1::outputChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#outputChanged
    """
    #  void QWaylandXdgOutputV1::outputChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgOutputV113outputChangedEv')

  def logicalPositionChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgOutputV1::logicalPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#logicalPositionChanged
    """
    #  void QWaylandXdgOutputV1::logicalPositionChanged()
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgOutputV122logicalPositionChangedEv',
    )

  def logicalSizeChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgOutputV1::logicalSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#logicalSizeChanged
    """
    #  void QWaylandXdgOutputV1::logicalSizeChanged()
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgOutputV118logicalSizeChangedEv',
    )

  def logicalGeometryChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgOutputV1::logicalGeometryChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#logicalGeometryChanged
    """
    #  void QWaylandXdgOutputV1::logicalGeometryChanged()
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgOutputV122logicalGeometryChangedEv',
    )

  def nameChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgOutputV1::nameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#nameChanged
    """
    #  void QWaylandXdgOutputV1::nameChanged()
    self.uglySide.call('ritual_ZN19QWaylandXdgOutputV111nameChangedEv')

  def descriptionChanged(self) -> None:
    """
    Calls Qt's 'void QWaylandXdgOutputV1::descriptionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwaylandxdgoutputv1.html#descriptionChanged
    """
    #  void QWaylandXdgOutputV1::descriptionChanged()
    self.uglySide.call(
        'ritual_ZN19QWaylandXdgOutputV118descriptionChangedEv',
    )

  @staticmethod
  def appendFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandXdgOutputV1::appendFunction(QQmlListProperty<QObject>
    *list, QObject *object)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgOutputV1.appendFunction' has no cute function yet. "
        "Qt's 'void "
        "QWaylandXdgOutputV1::appendFunction(QQmlListProperty<QObject> "
        "*list, QObject *object)': names 'QQmlListProperty<QObject>', which "
        "has no cute class yet.")

  @staticmethod
  def atFunction(*__, **_) -> Never:
    """
    Qt's 'QObject *QWaylandXdgOutputV1::atFunction(QQmlListProperty<QObject>
    *list, qsizetype index)': names 'QQmlListProperty<QObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgOutputV1.atFunction' has no cute function yet. Qt's "
        "'QObject "
        "*QWaylandXdgOutputV1::atFunction(QQmlListProperty<QObject> *list, "
        "qsizetype index)': names 'QQmlListProperty<QObject>', which has no "
        "cute class yet.")

  @staticmethod
  def clearFunction(*__, **_) -> Never:
    """
    Qt's 'void QWaylandXdgOutputV1::clearFunction(QQmlListProperty<QObject>
    *list)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgOutputV1.clearFunction' has no cute function yet. Qt's "
        "'void QWaylandXdgOutputV1::clearFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def countFunction(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QWaylandXdgOutputV1::countFunction(QQmlListProperty<QObject> *list)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgOutputV1.countFunction' has no cute function yet. Qt's "
        "'qsizetype "
        "QWaylandXdgOutputV1::countFunction(QQmlListProperty<QObject> "
        "*list)': names 'QQmlListProperty<QObject>', which has no cute "
        "class yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QWaylandXdgOutputV1::data()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QWaylandXdgOutputV1.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QWaylandXdgOutputV1::data()': gives a "
        "type Python has no way to take yet.")
