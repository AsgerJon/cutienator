"""
QQuick3DObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/qquick3dobject.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
  from . import QQuick3DObjectPrivate, QQuick3DSceneManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DObject(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuick3DObject: a plain Python object standing in
  front of one C++ QQuick3DObject.

  It is built on the cute 'QObject', as Qt's QQuick3DObject is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuick3DObject is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DObject that has a ritual and that Python can
  call so far, 19 names in all: 'metaObject', 'tr', 'd_func', 'state',
  'setState', 'childItems', 'parentItem', 'update', 'setParentItem',
  'parentChanged', 'childrenChanged', 'stateChanged', 'updateSpatialNode',
  'markAllDirty', 'itemChange', 'classBegin', 'componentComplete',
  'isComponentComplete', 'preSync'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DObject::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuick3DObject::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuick3DObjectPrivate *QQuick3DObject::d_func() const': takes
    in Python what 'QQuick3DObjectPrivate *QQuick3DObject::d_func()' takes.
  - Qt's 'void QQuick3DObject::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QQuick3DObject::~QQuick3DObject()': the destructor: Python never
    removes a C++ QQuick3DObject.
  - Qt's 'QQuick3DObject::QQuick3DObject(QQuick3DObjectPrivate &dd,
    QQuick3DObject *parent)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  4 of the 30 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuick3DObject is created at the first use, not by
    'QQuick3DObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DObject.
  - Qt tells when it has removed the C++ QQuick3DObject. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuick3DObject, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class ItemChange(CuteNum):
    """
    The enum 'QQuick3DObject::ItemChange' of Qt, with the 11 names Qt gives
    in it.
    """

    ItemChildAddedChange = Kee[int](0)
    ItemChildRemovedChange = Kee[int](1)
    ItemSceneChange = Kee[int](2)
    ItemVisibleHasChanged = Kee[int](3)
    ItemParentHasChanged = Kee[int](4)
    ItemOpacityHasChanged = Kee[int](5)
    ItemActiveFocusHasChanged = Kee[int](6)
    ItemRotationHasChanged = Kee[int](7)
    ItemAntialiasingHasChanged = Kee[int](8)
    ItemDevicePixelRatioHasChanged = Kee[int](9)
    ItemEnabledHasChanged = Kee[int](10)

  #  The classes Qt writes inside QQuick3DObject, each a class in here as in
  #  C++.

  class ItemChangeData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DObject::ItemChangeData: a plain Python
    object standing in front of one C++ QQuick3DObject::ItemChangeData.

    C++ hands a QQuick3DObject::ItemChangeData around as a copy, so every C++
    QQuick3DObject::ItemChangeData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QQuick3DObject::ItemChangeData yet. It can be made
    from Python, in 4 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuick3DObject::ItemChangeData::~ItemChangeData()': the
      destructor: Python removes its C++ QQuick3DObject::ItemChangeData by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuick3DObject::ItemChangeData is created at the first use, not
      by 'QQuick3DObject::ItemChangeData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DObject::ItemChangeData back gives a copy
      the ritual made for Python, in a new cute
      QQuick3DObject::ItemChangeData.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQuick3DObject = WAIT['QQuick3DObject']
      QQuick3DSceneManager = WAIT['QQuick3DSceneManager']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DObject::ItemChangeData'

    #  Qt's '~QQuick3DObject::ItemChangeData()'. Naming it makes this a value
    #  class: Python owns every C++ QQuick3DObject::ItemChangeData behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN14QQuick3DObject14ItemChangeDataD1Ev'

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

    @overload(QQuick3DObject)
    @overload(NoneType)
    def __init__(self, v: Optional[QQuick3DObject]) -> None:
      """
      Notes what was given, for Qt's
      'QQuick3DObject::ItemChangeData::ItemChangeData(QQuick3DObject *v)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dobject-itemchangedata.html

      Parameters
      ----------

      v : Optional[QQuick3DObject]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQuick3DObject::ItemChangeData::ItemChangeData(QQuick3DObject *v)
      self._noteCreation(QQuick3DObject.ItemChangeData, lambda: Rituals.call(
          'ritual_ZN14QQuick3DObject14ItemChangeDataC1EPS_',
          self._addressOf(v),
      ))

    @overload(QQuick3DSceneManager)
    def __init__(self, v: Optional[QQuick3DSceneManager]) -> None:
      """
      Notes what was given, for Qt's
      'QQuick3DObject::ItemChangeData::ItemChangeData(QQuick3DSceneManager
      *v)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dobject-itemchangedata.html

      Parameters
      ----------

      v : Optional[QQuick3DSceneManager]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQuick3DObject::ItemChangeData::ItemChangeData(QQuick3DSceneManager
      #      *v)
      self._noteCreation(QQuick3DObject.ItemChangeData, lambda: Rituals.call(
          'ritual_ZN14QQuick3DObject14ItemChangeDataC1EP20QQuick3DSceneMana'
          'ger',
          self._addressOf(v),
      ))

    @overload(float)
    def __init__(self, v: float) -> None:
      """
      Notes what was given, for Qt's
      'QQuick3DObject::ItemChangeData::ItemChangeData(qreal v)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dobject-itemchangedata.html

      Parameters
      ----------

      v : float
        Passed on as it is.
      """
      #  QQuick3DObject::ItemChangeData::ItemChangeData(qreal v)
      self._noteCreation(QQuick3DObject.ItemChangeData, lambda: Rituals.call(
          'ritual_ZN14QQuick3DObject14ItemChangeDataC1Ed', v,
      ))

    @overload(bool)
    def __init__(self, v: bool) -> None:
      """
      Notes what was given, for Qt's
      'QQuick3DObject::ItemChangeData::ItemChangeData(bool v)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dobject-itemchangedata.html

      Parameters
      ----------

      v : bool
        Passed on as it is.
      """
      #  QQuick3DObject::ItemChangeData::ItemChangeData(bool v)
      self._noteCreation(QQuick3DObject.ItemChangeData, lambda: Rituals.call(
          'ritual_ZN14QQuick3DObject14ItemChangeDataC1Eb', v,
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
    Calls Qt's 'QString QQuick3DObject::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#tr

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
    #  QString QQuick3DObject::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuick3DObject2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DObject'

  #  Qt's QQuick3DObject is built on more than one class. The part of a C++
  #  QQuick3DObject that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQuick3DObject_QQmlParserStatus',
  }

  #  A C++ QQuick3DObject Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DObject'

  #  The functions Qt calls itself that QQuick3DObject is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updateSpatialNode': (
          ('_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObject',
           ('address', 'address',
            'QtQuick3DRuntimeRender:QSSGRenderGraphObject'),
           (
               ('address', 'address',
                'QtQuick3DRuntimeRender:QSSGRenderGraphObject'),
           )),
      ),
      'markAllDirty': (
          ('_ZN14QQuick3DObject12markAllDirtyEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'itemChange': (
          ('_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemChan'
           'geDataE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQuick3D:QQuick3DObject.ItemChange'),
               ('address', 'value',
                'QtQuick3D:QQuick3DObject.ItemChangeData'),
           )),
      ),
      'preSync': (
          ('_ZN14QQuick3DObject7preSyncEv',
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DObject::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DObject::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DObject10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def state(self) -> str:
    """
    Calls Qt's 'QString QQuick3DObject::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#state

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DObject::state() const
    return self.uglySide.call('ritual_ZNK14QQuick3DObject5stateEv')

  def childItems(self) -> QList[QQuick3DObject]:
    """
    Calls Qt's 'QList<QQuick3DObject *> QQuick3DObject::childItems() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#childItems

    Returns
    -------

    QList[QQuick3DObject]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuick3DObject *> QQuick3DObject::childItems() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DObject10childItemsEv')
    return QList[QQuick3DObject]._cuteOwning(address)

  def parentItem(self) -> Optional[QQuick3DObject]:
    """
    Calls Qt's 'QQuick3DObject *QQuick3DObject::parentItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#parentItem

    Returns
    -------

    Optional[QQuick3DObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DObject *QQuick3DObject::parentItem() const
    address = self.uglySide.call('ritual_ZNK14QQuick3DObject10parentItemEv')
    return QQuick3DObject._cuteAt(address)

  def isComponentComplete(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DObject::isComponentComplete() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobject.html#isComponentComplete
    """
    #  bool QQuick3DObject::isComponentComplete() const
    return self.uglySide.call(
        'ritual_ZNK14QQuick3DObject19isComponentCompleteEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setState(self, state: str) -> None:
    """
    Calls Qt's 'void QQuick3DObject::setState(const QString &state)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#setState

    Parameters
    ----------

    state : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuick3DObject::setState(const QString &state)
    self.uglySide.call(
        'ritual_ZN14QQuick3DObject8setStateERK7QString', state,
    )

  @overload(THIS)
  @overload(NoneType)
  def setParentItem(self, parentItem: Optional[QQuick3DObject]) -> None:
    """
    Calls Qt's 'void QQuick3DObject::setParentItem(QQuick3DObject
    *parentItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#setParentItem

    Parameters
    ----------

    parentItem : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObject::setParentItem(QQuick3DObject *parentItem)
    self.uglySide.call(
        'ritual_ZN14QQuick3DObject13setParentItemEPS_',
        self._addressOf(parentItem),
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
  @overload(THIS)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuick3DObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DObject::QQuick3DObject(QQuick3DObject *parent)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#QQuick3DObject

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuick3DObject::QQuick3DObject(QQuick3DObject *parent)
    self._noteCreation(QQuick3DObject, lambda: Rituals.call(
        'ritual_ZN14QQuick3DObjectC1EPS_', self._addressOf(parent),
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

  def d_func(self) -> Optional[QQuick3DObjectPrivate]:
    """
    Calls Qt's 'QQuick3DObjectPrivate *QQuick3DObject::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#d_func

    Returns
    -------

    Optional[QQuick3DObjectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DObjectPrivate *QQuick3DObject::d_func()
    address = self.uglySide.call('ritual_ZN14QQuick3DObject6d_funcEv')
    from . import QQuick3DObjectPrivate
    return QQuick3DObjectPrivate._cuteAt(address)

  def update(self) -> None:
    """
    Calls Qt's 'void QQuick3DObject::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#update
    """
    #  void QQuick3DObject::update()
    self.uglySide.call('ritual_ZN14QQuick3DObject6updateEv')

  def parentChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DObject::parentChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#parentChanged
    """
    #  void QQuick3DObject::parentChanged()
    self.uglySide.call('ritual_ZN14QQuick3DObject13parentChangedEv')

  def childrenChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DObject::childrenChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobject.html#childrenChanged
    """
    #  void QQuick3DObject::childrenChanged()
    self.uglySide.call('ritual_ZN14QQuick3DObject15childrenChangedEv')

  def stateChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DObject::stateChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#stateChanged
    """
    #  void QQuick3DObject::stateChanged()
    self.uglySide.call('ritual_ZN14QQuick3DObject12stateChangedEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      node: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DObject::updateSpatialNode(QSSGRenderGraphObject *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobject.html#updateSpatialNode

    Parameters
    ----------

    node : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DObject::updateSpatialNode(QSSGRenderGraphObject *node)
    ritual = (
        'ritual_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGraphObj'
        'ect')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuick3DObject17updateSpatialNodeEP21QSSGRenderGr'
          'aphObject')
    address = self.uglySide.call(ritual, self._addressOf(node))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def markAllDirty(self) -> None:
    """
    Calls Qt's 'void QQuick3DObject::markAllDirty()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#markAllDirty
    """
    #  void QQuick3DObject::markAllDirty()
    ritual = 'ritual_ZN14QQuick3DObject12markAllDirtyEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuick3DObject12markAllDirtyEv'
    self.uglySide.call(ritual)

  @overload(ItemChange, ItemChangeData)
  def itemChange(self, a0: ItemChange, a1: ItemChangeData) -> None:
    """
    Calls Qt's 'void QQuick3DObject::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#itemChange

    Parameters
    ----------

    a0 : ItemChange
      Passed on as its number.

    a1 : ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DObject::itemChange(ItemChange a0, const ItemChangeData
    #      &a1)
    ritual = (
        'ritual_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_14ItemC'
        'hangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN14QQuick3DObject10itemChangeENS_10ItemChangeERKNS_1'
          '4ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuick3DObject::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#classBegin
    """
    #  void QQuick3DObject::classBegin()
    ritual = 'ritual_ZN14QQuick3DObject10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuick3DObject10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuick3DObject::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobject.html#componentComplete
    """
    #  void QQuick3DObject::componentComplete()
    ritual = 'ritual_ZN14QQuick3DObject17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuick3DObject17componentCompleteEv'
    self.uglySide.call(ritual)

  def preSync(self) -> None:
    """
    Calls Qt's 'void QQuick3DObject::preSync()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobject.html#preSync
    """
    #  void QQuick3DObject::preSync()
    ritual = 'ritual_ZN14QQuick3DObject7preSyncEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN14QQuick3DObject7preSyncEv'
    self.uglySide.call(ritual)


#  Qt's 'QList<QQuick3DObject *>': the list of QQuick3DObject, which
#  'QList[QQuick3DObject]' gives. It is made here, so that there is one as
#  soon as there can be a QQuick3DObject.
QList.createKind(
    QQuick3DObject, 'address',
    make='ritual_list_make_QQuick3DObject_ptr',
    add='ritual_list_add_QQuick3DObject_ptr',
    size='ritual_list_size_QQuick3DObject_ptr',
    at='ritual_list_at_QQuick3DObject_ptr',
    drop='ritual_list_drop_QQuick3DObject_ptr',
)
