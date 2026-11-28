"""
QQuick3DObjectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dobject_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuick3DObjectPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate
from ..QtQml import QV4
from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
from . import QQuick3DObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from ..QtQuick import QQuickStateGroup
  from . import QQuick3DObjectChangeListener
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuick3DObjectChangeListener = WAIT['QQuick3DObjectChangeListener']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DObjectPrivate(QObjectPrivate):
  """
  The cute side of Qt's QQuick3DObjectPrivate: a plain Python object standing
  in front of one C++ QQuick3DObjectPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QQuick3DObjectPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DObjectPrivate that has a ritual and that
  Python can call so far, 27 names in all: 'q_func', 'get',
  'updateSpatialNode', 'init', 'state', 'setState',
  '_q_resourceObjectDeleted', '_q_cleanupContentItem2D',
  '_q_createJSWrapper', 'addItemChangeListener',
  'updateOrAddItemChangeListener', 'removeItemChangeListener', '_states',
  'dirtyToString', 'dirty', 'addToDirtyList', 'removeFromDirtyList',
  'hasFlag', 'setCulled', 'addChild', 'removeChild', 'siblingOrderChanged',
  'derefSceneManager', 'updateSubFocusItem', 'itemChange', 'updatePolish',
  'requestSecondaryUpdate'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuick3DObject *QQuick3DObjectPrivate::q_func() const': takes
    in Python what 'QQuick3DObject *QQuick3DObjectPrivate::q_func()' takes.
  - Qt's 'const QQuick3DObjectPrivate *QQuick3DObjectPrivate::get(const
    QQuick3DObject *item)': takes in Python what 'QQuick3DObjectPrivate
    *QQuick3DObjectPrivate::get(QQuick3DObject *item)' takes.
  - Qt's 'QQuick3DObjectPrivate::~QQuick3DObjectPrivate()': the destructor:
    Python never removes a C++ QQuick3DObjectPrivate.
  - Qt's 'QQmlListProperty<QObject> QQuick3DObjectPrivate::data()': gives a
    type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QObject> QQuick3DObjectPrivate::resources()':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuick3DObject>
    QQuick3DObjectPrivate::children()': gives a type Python has no way to
    take yet.
  - Qt's 'QQmlListProperty<QQuickState> QQuick3DObjectPrivate::states()':
    gives a type Python has no way to take yet.
  - Qt's 'QQmlListProperty<QQuickTransition>
    QQuick3DObjectPrivate::transitions()': gives a type Python has no way to
    take yet.
  - Qt's 'void QQuick3DObjectPrivate::data_append(QQmlListProperty<QObject>
    *a0, QObject *a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'qsizetype
    QQuick3DObjectPrivate::data_count(QQmlListProperty<QObject> *a0)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject *QQuick3DObjectPrivate::data_at(QQmlListProperty<QObject>
    *a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void QQuick3DObjectPrivate::data_clear(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'QObject
    *QQuick3DObjectPrivate::resources_at(QQmlListProperty<QObject> *a0,
    qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
  - Qt's 'void
    QQuick3DObjectPrivate::resources_append(QQmlListProperty<QObject> *a0,
    QObject *a1)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
  - Qt's 'qsizetype
    QQuick3DObjectPrivate::resources_count(QQmlListProperty<QObject> *a0)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void
    QQuick3DObjectPrivate::resources_clear(QQmlListProperty<QObject> *a0)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
  - Qt's 'void
    QQuick3DObjectPrivate::children_append(QQmlListProperty<QQuick3DObject>
    *a0, QQuick3DObject *a1)': names 'QQmlListProperty<QQuick3DObject>',
    which has no cute class yet.
  - Qt's 'qsizetype
    QQuick3DObjectPrivate::children_count(QQmlListProperty<QQuick3DObject>
    *a0)': names 'QQmlListProperty<QQuick3DObject>', which has no cute class
    yet.
  - Qt's 'QQuick3DObject
    *QQuick3DObjectPrivate::children_at(QQmlListProperty<QQuick3DObject> *a0,
    qsizetype a1)': names 'QQmlListProperty<QQuick3DObject>', which has no
    cute class yet.
  - Qt's 'void
    QQuick3DObjectPrivate::children_clear(QQmlListProperty<QQuick3DObject>
    *a0)': names 'QQmlListProperty<QQuick3DObject>', which has no cute class
    yet.
  - Qt's 'void QQuick3DObjectPrivate::refSceneManager(QQuick3DSceneManager
    &a0)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQuick3DObjectPrivate::refSceneManager(QQuick3DObject *obj,
    QQuick3DSceneManager &mgr)': takes a type Python has no way to hand over
    yet.

  What has no ritual
  ------------------

  2 of the 55 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QQuick3DObjectPrivate is created at the first use, not by
    'QQuick3DObjectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DObjectPrivate.
  - Each name of Qt's QQuick3DObjectPrivate that has no cute function yet,
    'attachWatcher', 'attachWatcherPriv', 'children_append', 'children_at',
    'children_clear', 'children_count', 'data', 'data_append', 'data_at',
    'data_clear', 'data_count', 'refSceneManager', 'resources',
    'resources_append', 'resources_at', 'resources_clear', 'resources_count',
    'states', 'transitions', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuick3DObjectPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ChangeType(CuteFlags):
    """
    The flags enum 'QQuick3DObjectPrivate::ChangeType' of Qt, with the 11
    names Qt gives in it. Qt names the type of its combinations
    'QQuick3DObjectPrivate::ChangeListener::ChangeTypes'.
    """

    Geometry = 0x1
    SiblingOrder = 0x2
    Visibility = 0x4
    Opacity = 0x8
    Destroyed = 0x10
    Parent = 0x20
    Children = 0x40
    Rotation = 0x80
    ImplicitWidth = 0x100
    ImplicitHeight = 0x200
    Enabled = 0x400

  ChangeTypes = ChangeType

  class DirtyType(CuteNum):
    """
    The enum 'QQuick3DObjectPrivate::DirtyType' of Qt, with the 23 names Qt
    gives in it.
    """

    TransformOrigin = Kee[int](1)
    Transform = Kee[int](2)
    BasicTransform = Kee[int](4)
    Position = Kee[int](8)
    Size = Kee[int](16)
    ZValue = Kee[int](32)
    Content = Kee[int](64)
    Smooth = Kee[int](128)
    OpacityValue = Kee[int](256)
    ChildrenChanged = Kee[int](512)
    ChildrenStackingChanged = Kee[int](1024)
    ParentChanged = Kee[int](2048)
    Clip = Kee[int](4096)
    Window = Kee[int](8192)
    EffectReference = Kee[int](32768)
    Visible = Kee[int](65536)
    HideReference = Kee[int](131072)
    Antialiasing = Kee[int](262144)
    InstanceRootChanged = Kee[int](524288)
    TransformUpdateMask = Kee[int](8207)
    ComplexTransformUpdateMask = Kee[int](8194)
    ContentUpdateMask = Kee[int](270544)
    ChildrenUpdateMask = Kee[int](42496)

  class Flags(CuteNum, scoped=True):
    """
    The enum 'QQuick3DObjectPrivate::Flags' of Qt, with the 2 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NULL = Kee[int](0)
    RequiresSecondaryUpdate = Kee[int](1)

  #  The classes Qt writes inside QQuick3DObjectPrivate, each a class in here
  #  as in C++.

  class ChangeListener(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DObjectPrivate::ChangeListener: a plain
    Python object standing in front of one C++
    QQuick3DObjectPrivate::ChangeListener.

    C++ hands a QQuick3DObjectPrivate::ChangeListener around as a copy, so
    every C++ QQuick3DObjectPrivate::ChangeListener behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQuick3DObjectPrivate::ChangeListener that has a
    ritual and that Python can call so far, 1 name in all: '__eq__'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuick3DObjectPrivate::ChangeListener::ChangeListener(
      QQuick3DObjectChangeListener *l, ChangeTypes t)': names the enum
      'QQuick3DObjectPrivate::ChangeType', whose class cannot be named here.
    - Qt's 'QQuick3DObjectPrivate::ChangeListener::~ChangeListener()': the
      destructor: Python removes its C++
      QQuick3DObjectPrivate::ChangeListener by it, and has no other use for
      it.

    What has no ritual
    ------------------

    1 of the 4 functions Qt declares: 1 the compiler refuses its ritual as it
    would be written here.

    What to expect
    --------------

    - The C++ QQuick3DObjectPrivate::ChangeListener is created at the first
      use, not by 'QQuick3DObjectPrivate::ChangeListener(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DObjectPrivate::ChangeListener back gives a
      copy the ritual made for Python, in a new cute
      QQuick3DObjectPrivate::ChangeListener.
    - Each name of Qt's QQuick3DObjectPrivate::ChangeListener that has no
      cute function yet, '__init__', holds a function that raises
      'NotImplementedError', and its docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DObjectPrivate::ChangeListener'

    #  Qt's '~QQuick3DObjectPrivate::ChangeListener()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QQuick3DObjectPrivate::ChangeListener behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN21QQuick3DObjectPrivate14ChangeListenerD1Ev')

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

    @overload(THIS)
    def __eq__(self, other: QQuick3DObjectPrivate.ChangeListener) -> bool:
      """
      Calls Qt's 'bool
      QQuick3DObjectPrivate::ChangeListener::operator==(const ChangeListener
      &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dobjectprivate-changelistener.html

      Parameters
      ----------

      other : QQuick3DObjectPrivate.ChangeListener
        Passed on as a value: Qt reads the C++
        QQuick3DObjectPrivate::ChangeListener, which stays Python's own.
      """
      #  bool QQuick3DObjectPrivate::ChangeListener::operator==(const
      #      ChangeListener &other) const
      return self.uglySide.call(
          'ritual_ZNK21QQuick3DObjectPrivate14ChangeListenereqERKS0_',
          self._valueOf(other),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    def __init__(*__, **_) -> Never:
      """
      - Qt's 'QQuick3DObjectPrivate::ChangeListener::ChangeListener(
        QQuick3DObjectChangeListener *l, ChangeTypes t)': names the enum
        'QQuick3DObjectPrivate::ChangeType', whose class cannot be named
        here.
      - Qt's 'QQuick3DObjectPrivate::ChangeListener::ChangeListener(
        QQuick3DObjectChangeListener *l)': the compiler refuses its ritual as
        it would be written here: call to constructor of
        'QQuick3DObjectPrivate::ChangeListener' is ambiguous.
      """
      raise NotImplementedError(
          "'QQuick3DObjectPrivate.ChangeListener.__init__' has no cute "
          "function yet. Qt's "
          "'QQuick3DObjectPrivate::ChangeListener::ChangeListener(QQuick3DOb"
          "jectChangeListener *l, ChangeTypes t)': names the enum "
          "'QQuick3DObjectPrivate::ChangeType', whose class cannot be named "
          "here. Qt's "
          "'QQuick3DObjectPrivate::ChangeListener::ChangeListener(QQuick3DOb"
          "jectChangeListener *l)': the compiler refuses its ritual as it "
          "would be written here: call to constructor of "
          "'QQuick3DObjectPrivate::ChangeListener' is ambiguous.")

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

  class ConnectionKey(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DObjectPrivate::ConnectionKey: a plain
    Python object standing in front of one C++
    QQuick3DObjectPrivate::ConnectionKey.

    C++ hands a QQuick3DObjectPrivate::ConnectionKey around as a copy, so
    every C++ QQuick3DObjectPrivate::ConnectionKey behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QQuick3DObjectPrivate::ConnectionKey that has a
    ritual and that Python can call so far, 1 name in all: '__eq__'. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuick3DObjectPrivate::ConnectionKey::~ConnectionKey()': the
      destructor: Python removes its C++ QQuick3DObjectPrivate::ConnectionKey
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuick3DObjectPrivate::ConnectionKey is created at the first
      use, not by 'QQuick3DObjectPrivate::ConnectionKey(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DObjectPrivate::ConnectionKey back gives a
      copy the ritual made for Python, in a new cute
      QQuick3DObjectPrivate::ConnectionKey.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DObjectPrivate::ConnectionKey'

    #  Qt's '~QQuick3DObjectPrivate::ConnectionKey()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QQuick3DObjectPrivate::ConnectionKey behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN21QQuick3DObjectPrivate13ConnectionKeyD1Ev'

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

    @overload(THIS)
    def __eq__(self, b: QQuick3DObjectPrivate.ConnectionKey) -> bool:
      """
      Calls Qt's 'bool operator==(const ConnectionKey &a, const ConnectionKey
      &b)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dobjectprivate-connectionkey.html

      Parameters
      ----------

      b : QQuick3DObjectPrivate.ConnectionKey
        Passed on as a value: Qt reads the C++
        QQuick3DObjectPrivate::ConnectionKey, which stays Python's own.
      """
      #  bool operator==(const ConnectionKey &a, const ConnectionKey &b)
      return Rituals.call(
          'ritual_ZeqRKN21QQuick3DObjectPrivate13ConnectionKeyES2_',
          CuteMixin._valueOf(self), CuteMixin._valueOf(b),
      )

    @overload.fallback
    def __eq__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  class ExtraData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DObjectPrivate::ExtraData: a plain Python
    object standing in front of one C++ QQuick3DObjectPrivate::ExtraData.

    C++ hands a QQuick3DObjectPrivate::ExtraData around as a copy, so every
    C++ QQuick3DObjectPrivate::ExtraData behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuick3DObjectPrivate::ExtraData yet. It can be made
    from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuick3DObjectPrivate::ExtraData::~ExtraData()': the destructor:
      Python removes its C++ QQuick3DObjectPrivate::ExtraData by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuick3DObjectPrivate::ExtraData is created at the first use,
      not by 'QQuick3DObjectPrivate::ExtraData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DObjectPrivate::ExtraData back gives a copy
      the ritual made for Python, in a new cute
      QQuick3DObjectPrivate::ExtraData.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DObjectPrivate::ExtraData'

    #  Qt's '~QQuick3DObjectPrivate::ExtraData()'. Naming it makes this a
    #  value class: Python owns every C++ QQuick3DObjectPrivate::ExtraData
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN21QQuick3DObjectPrivate9ExtraDataD1Ev'

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
      'QQuick3DObjectPrivate::ExtraData::ExtraData()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qquick3dobjectprivate-extradata.html#ExtraData
      """
      #  QQuick3DObjectPrivate::ExtraData::ExtraData()
      self._noteCreation(
          QQuick3DObjectPrivate.ExtraData, lambda: Rituals.call(
              'ritual_ZN21QQuick3DObjectPrivate9ExtraDataC1Ev',
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
  @overload(QQuick3DObject)
  @overload(NoneType)
  def get(item: Optional[QQuick3DObject]) -> Optional[QQuick3DObjectPrivate]:
    """
    Calls Qt's 'QQuick3DObjectPrivate
    *QQuick3DObjectPrivate::get(QQuick3DObject *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobjectprivate.html#get

    Parameters
    ----------

    item : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuick3DObjectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DObjectPrivate *QQuick3DObjectPrivate::get(QQuick3DObject
    #      *item)
    address = Rituals.call(
        'ritual_ZN21QQuick3DObjectPrivate3getEP14QQuick3DObject',
        CuteMixin._addressOf(item),
    )
    return QQuick3DObjectPrivate._cuteAt(address)

  @staticmethod
  @overload(QQuick3DObject, QSSGRenderGraphObject)
  @overload(QQuick3DObject, NoneType)
  @overload(NoneType, QSSGRenderGraphObject)
  @overload(NoneType, NoneType)
  def updateSpatialNode(
      o: Optional[QQuick3DObject],
      n: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DObjectPrivate::updateSpatialNode(QQuick3DObject *o,
    QSSGRenderGraphObject *n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#updateSpatialNode

    Parameters
    ----------

    o : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    n : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DObjectPrivate::updateSpatialNode(QQuick3DObject *o,
    #      QSSGRenderGraphObject *n)
    address = Rituals.call(
        'ritual_ZN21QQuick3DObjectPrivate17updateSpatialNodeEP14QQuick3DObj'
        'ectP21QSSGRenderGraphObject',
        CuteMixin._addressOf(o), CuteMixin._addressOf(n),
    )
    return QSSGRenderGraphObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DObjectPrivate'

  #  A C++ QQuick3DObjectPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DObjectPrivate'

  #  The functions Qt calls itself that QQuick3DObjectPrivate is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'updatePolish': (
          ('_ZN21QQuick3DObjectPrivate12updatePolishEv',
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

  def state(self) -> str:
    """
    Calls Qt's 'QString QQuick3DObjectPrivate::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobjectprivate.html#state

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DObjectPrivate::state() const
    return self.uglySide.call('ritual_ZNK21QQuick3DObjectPrivate5stateEv')

  def dirtyToString(self) -> str:
    """
    Calls Qt's 'QString QQuick3DObjectPrivate::dirtyToString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#dirtyToString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuick3DObjectPrivate::dirtyToString() const
    return self.uglySide.call(
        'ritual_ZNK21QQuick3DObjectPrivate13dirtyToStringEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setState(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::setState(const QString &a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#setState

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuick3DObjectPrivate::setState(const QString &a0)
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate8setStateERK7QString', a0,
    )

  @overload(bool)
  def setCulled(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::setCulled(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#setCulled

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuick3DObjectPrivate::setCulled(bool a0)
    self.uglySide.call('ritual_ZN21QQuick3DObjectPrivate9setCulledEb', a0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSSGRenderGraphObject.Type, int)
  def __init__(self, t: QSSGRenderGraphObject.Type, f: int) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DObjectPrivate::QQuick3DObjectPrivate(Type t, FlagsT f)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#QQuick3DObjectPrivate

    Parameters
    ----------

    t : QSSGRenderGraphObject.Type
      Passed on as its number.

    f : int
      Passed on as it is.
    """
    #  QQuick3DObjectPrivate::QQuick3DObjectPrivate(Type t, FlagsT f)
    self._noteCreation(QQuick3DObjectPrivate, lambda: Rituals.call(
        'ritual_ZN21QQuick3DObjectPrivateC1EN21QSSGRenderGraphObject4TypeEj',
        t.value, f,
    ))

  @overload(QSSGRenderGraphObject.Type, Flags)
  def __init__(self, t: QSSGRenderGraphObject.Type, f: Flags) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DObjectPrivate::QQuick3DObjectPrivate(Type t, Flags f)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#QQuick3DObjectPrivate

    Parameters
    ----------

    t : QSSGRenderGraphObject.Type
      Passed on as its number.

    f : Flags
      Passed on as its number.
    """
    #  QQuick3DObjectPrivate::QQuick3DObjectPrivate(Type t, Flags f)
    self._noteCreation(QQuick3DObjectPrivate, lambda: Rituals.call(
        'ritual_ZN21QQuick3DObjectPrivateC1EN21QSSGRenderGraphObject4TypeEN'
        'S_5FlagsE',
        t.value, f.value,
    ))

  @overload(QSSGRenderGraphObject.Type)
  def __init__(self, t: QSSGRenderGraphObject.Type) -> None:
    """
    Notes what was given, for Qt's
    'QQuick3DObjectPrivate::QQuick3DObjectPrivate(Type t)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#QQuick3DObjectPrivate

    Parameters
    ----------

    t : QSSGRenderGraphObject.Type
      Passed on as its number.
    """
    #  QQuick3DObjectPrivate::QQuick3DObjectPrivate(Type t)
    self._noteCreation(QQuick3DObjectPrivate, lambda: Rituals.call(
        'ritual_ZN21QQuick3DObjectPrivateC1EN21QSSGRenderGraphObject4TypeE',
        t.value,
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

  def q_func(self) -> Optional[QQuick3DObject]:
    """
    Calls Qt's 'QQuick3DObject *QQuick3DObjectPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobjectprivate.html#q_func

    Returns
    -------

    Optional[QQuick3DObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DObject *QQuick3DObjectPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QQuick3DObjectPrivate6q_funcEv')
    return QQuick3DObject._cuteAt(address)

  @overload(QQuick3DObject)
  @overload(NoneType)
  def init(self, parent: Optional[QQuick3DObject]) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::init(QQuick3DObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobjectprivate.html#init

    Parameters
    ----------

    parent : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObjectPrivate::init(QQuick3DObject *parent)
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate4initEP14QQuick3DObject',
        self._addressOf(parent),
    )

  @overload(QObject)
  @overload(NoneType)
  def _q_resourceObjectDeleted(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::_q_resourceObjectDeleted(QObject
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObjectPrivate::_q_resourceObjectDeleted(QObject *a0)
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate24_q_resourceObjectDeletedEP7QObje'
        'ct',
        self._addressOf(a0, 'QObject'),
    )

  def _q_cleanupContentItem2D(self) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::_q_cleanupContentItem2D()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#_q_cleanupContentItem2D
    """
    #  void QQuick3DObjectPrivate::_q_cleanupContentItem2D()
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate23_q_cleanupContentItem2DEv',
    )

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def _q_createJSWrapper(self, engine: Optional[QV4.ExecutionEngine]) -> int:
    """
    Calls Qt's 'quint64
    QQuick3DObjectPrivate::_q_createJSWrapper(QQmlV4ExecutionEnginePtr
    engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#_q_createJSWrapper

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  quint64
    #      QQuick3DObjectPrivate::_q_createJSWrapper(QQmlV4ExecutionEnginePtr
    #      engine)
    return self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate18_q_createJSWrapperEPN3QV415Execu'
        'tionEngineE',
        self._addressOf(engine),
    )

  @overload(QQuick3DObjectChangeListener, ChangeTypes)
  @overload(NoneType, ChangeTypes)
  def addItemChangeListener(
      self,
      listener: Optional[QQuick3DObjectChangeListener],
      types: ChangeTypes,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DObjectPrivate::addItemChangeListener(QQuick3DObjectChangeListener
    *listener, ChangeTypes types)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#addItemChangeListener

    Parameters
    ----------

    listener : Optional[QQuick3DObjectChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    types : ChangeTypes
      Passed on as its number.
    """
    #  void QQuick3DObjectPrivate::addItemChangeListener(
    #      QQuick3DObjectChangeListener *listener, ChangeTypes types)
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate21addItemChangeListenerEP28QQuick3'
        'DObjectChangeListener6QFlagsINS_10ChangeTypeEE',
        self._addressOf(listener), types.value,
    )

  @overload(QQuick3DObjectChangeListener, ChangeTypes)
  @overload(NoneType, ChangeTypes)
  def updateOrAddItemChangeListener(
      self,
      listener: Optional[QQuick3DObjectChangeListener],
      types: ChangeTypes,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::updateOrAddItemChangeListener(
    QQuick3DObjectChangeListener *listener, ChangeTypes types)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html

    Parameters
    ----------

    listener : Optional[QQuick3DObjectChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    types : ChangeTypes
      Passed on as its number.
    """
    #  void QQuick3DObjectPrivate::updateOrAddItemChangeListener(
    #      QQuick3DObjectChangeListener *listener, ChangeTypes types)
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate29updateOrAddItemChangeListenerEP2'
        '8QQuick3DObjectChangeListener6QFlagsINS_10ChangeTypeEE',
        self._addressOf(listener), types.value,
    )

  @overload(QQuick3DObjectChangeListener, ChangeTypes)
  @overload(NoneType, ChangeTypes)
  def removeItemChangeListener(
      self,
      a0: Optional[QQuick3DObjectChangeListener],
      types: ChangeTypes,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::removeItemChangeListener(
    QQuick3DObjectChangeListener *a0, ChangeTypes types)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html

    Parameters
    ----------

    a0 : Optional[QQuick3DObjectChangeListener]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    types : ChangeTypes
      Passed on as its number.
    """
    #  void QQuick3DObjectPrivate::removeItemChangeListener(
    #      QQuick3DObjectChangeListener *a0, ChangeTypes types)
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate24removeItemChangeListenerEP28QQui'
        'ck3DObjectChangeListener6QFlagsINS_10ChangeTypeEE',
        self._addressOf(a0), types.value,
    )

  def _states(self) -> Optional[QQuickStateGroup]:
    """
    Calls Qt's 'QQuickStateGroup *QQuick3DObjectPrivate::_states()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobjectprivate.html#_states

    Returns
    -------

    Optional[QQuickStateGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickStateGroup *QQuick3DObjectPrivate::_states()
    address = self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate7_statesEv',
    )
    from ..QtQuick import QQuickStateGroup
    return QQuickStateGroup._cuteAt(address)

  @overload(DirtyType)
  def dirty(self, a0: DirtyType) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::dirty(DirtyType a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobjectprivate.html#dirty

    Parameters
    ----------

    a0 : DirtyType
      Passed on as its number.
    """
    #  void QQuick3DObjectPrivate::dirty(DirtyType a0)
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate5dirtyENS_9DirtyTypeE', a0.value,
    )

  def addToDirtyList(self) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::addToDirtyList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#addToDirtyList
    """
    #  void QQuick3DObjectPrivate::addToDirtyList()
    self.uglySide.call('ritual_ZN21QQuick3DObjectPrivate14addToDirtyListEv')

  def removeFromDirtyList(self) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::removeFromDirtyList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#removeFromDirtyList
    """
    #  void QQuick3DObjectPrivate::removeFromDirtyList()
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate19removeFromDirtyListEv',
    )

  @overload(Flags)
  def hasFlag(self, flag: Flags) -> bool:
    """
    Calls Qt's 'bool QQuick3DObjectPrivate::hasFlag(Flags flag)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dobjectprivate.html#hasFlag

    Parameters
    ----------

    flag : Flags
      Passed on as its number.
    """
    #  bool QQuick3DObjectPrivate::hasFlag(Flags flag)
    return self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate7hasFlagENS_5FlagsE', flag.value,
    )

  @overload(QQuick3DObject)
  @overload(NoneType)
  def addChild(self, a0: Optional[QQuick3DObject]) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::addChild(QQuick3DObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#addChild

    Parameters
    ----------

    a0 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObjectPrivate::addChild(QQuick3DObject *a0)
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate8addChildEP14QQuick3DObject',
        self._addressOf(a0),
    )

  @overload(QQuick3DObject)
  @overload(NoneType)
  def removeChild(self, a0: Optional[QQuick3DObject]) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::removeChild(QQuick3DObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#removeChild

    Parameters
    ----------

    a0 : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObjectPrivate::removeChild(QQuick3DObject *a0)
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate11removeChildEP14QQuick3DObject',
        self._addressOf(a0),
    )

  def siblingOrderChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::siblingOrderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#siblingOrderChanged
    """
    #  void QQuick3DObjectPrivate::siblingOrderChanged()
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate19siblingOrderChangedEv',
    )

  @overload()
  def derefSceneManager(self) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::derefSceneManager()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#derefSceneManager
    """
    #  void QQuick3DObjectPrivate::derefSceneManager()
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate17derefSceneManagerEv',
    )

  @staticmethod
  @overload(QQuick3DObject)
  @overload(NoneType)
  def derefSceneManager(obj: Optional[QQuick3DObject]) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::derefSceneManager(QQuick3DObject
    *obj)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#derefSceneManager

    Parameters
    ----------

    obj : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DObjectPrivate::derefSceneManager(QQuick3DObject *obj)
    Rituals.call(
        'ritual_ZN21QQuick3DObjectPrivate17derefSceneManagerEP14QQuick3DObj'
        'ect',
        CuteMixin._addressOf(obj),
    )

  @overload(QQuick3DObject, bool)
  @overload(NoneType, bool)
  def updateSubFocusItem(
      self,
      scope: Optional[QQuick3DObject],
      focus: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::updateSubFocusItem(QQuick3DObject
    *scope, bool focus)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#updateSubFocusItem

    Parameters
    ----------

    scope : Optional[QQuick3DObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    focus : bool
      Passed on as it is.
    """
    #  void QQuick3DObjectPrivate::updateSubFocusItem(QQuick3DObject *scope,
    #      bool focus)
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate18updateSubFocusItemEP14QQuick3DOb'
        'jectb',
        self._addressOf(scope), focus,
    )

  @overload(QQuick3DObject.ItemChange, QQuick3DObject.ItemChangeData)
  def itemChange(
      self,
      a0: QQuick3DObject.ItemChange,
      a1: QQuick3DObject.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void
    QQuick3DObjectPrivate::itemChange(QQuick3DObject::ItemChange a0, const
    QQuick3DObject::ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#itemChange

    Parameters
    ----------

    a0 : QQuick3DObject.ItemChange
      Passed on as its number.

    a1 : QQuick3DObject.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuick3DObject::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuick3DObjectPrivate::itemChange(QQuick3DObject::ItemChange a0,
    #      const QQuick3DObject::ItemChangeData &a1)
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate10itemChangeEN14QQuick3DObject10It'
        'emChangeERKNS0_14ItemChangeDataE',
        a0.value, self._valueOf(a1),
    )

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#updatePolish
    """
    #  void QQuick3DObjectPrivate::updatePolish()
    ritual = 'ritual_ZN21QQuick3DObjectPrivate12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuick3DObjectPrivate12updatePolishEv'
    self.uglySide.call(ritual)

  def requestSecondaryUpdate(self) -> None:
    """
    Calls Qt's 'void QQuick3DObjectPrivate::requestSecondaryUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dobjectprivate.html#requestSecondaryUpdate
    """
    #  void QQuick3DObjectPrivate::requestSecondaryUpdate()
    self.uglySide.call(
        'ritual_ZN21QQuick3DObjectPrivate22requestSecondaryUpdateEv',
    )

  @staticmethod
  def attachWatcher(*__, **_) -> Never:
    """
    Qt's 'QQuick3DObjectPrivate::attachWatcher': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.attachWatcher' has no cute function yet. "
        "Qt's 'QQuick3DObjectPrivate::attachWatcher': a template: a pattern "
        "and no single function.")

  @staticmethod
  def attachWatcherPriv(*__, **_) -> Never:
    """
    Qt's 'QQuick3DObjectPrivate::attachWatcherPriv': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.attachWatcherPriv' has no cute function "
        "yet. Qt's 'QQuick3DObjectPrivate::attachWatcherPriv': a template: "
        "a pattern and no single function.")

  @staticmethod
  def children_append(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DObjectPrivate::children_append(QQmlListProperty<QQuick3DObject>
    *a0, QQuick3DObject *a1)': names 'QQmlListProperty<QQuick3DObject>',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.children_append' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DObjectPrivate::children_append(QQmlListProperty<QQuick3DObj"
        "ect> *a0, QQuick3DObject *a1)': names "
        "'QQmlListProperty<QQuick3DObject>', which has no cute class yet.")

  @staticmethod
  def children_at(*__, **_) -> Never:
    """
    Qt's 'QQuick3DObject
    *QQuick3DObjectPrivate::children_at(QQmlListProperty<QQuick3DObject> *a0,
    qsizetype a1)': names 'QQmlListProperty<QQuick3DObject>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.children_at' has no cute function yet. Qt's "
        "'QQuick3DObject "
        "*QQuick3DObjectPrivate::children_at(QQmlListProperty<QQuick3DObject"
        "> *a0, qsizetype a1)': names 'QQmlListProperty<QQuick3DObject>', "
        "which has no cute class yet.")

  @staticmethod
  def children_clear(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DObjectPrivate::children_clear(QQmlListProperty<QQuick3DObject>
    *a0)': names 'QQmlListProperty<QQuick3DObject>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.children_clear' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DObjectPrivate::children_clear(QQmlListProperty<QQuick3DObje"
        "ct> *a0)': names 'QQmlListProperty<QQuick3DObject>', which has no "
        "cute class yet.")

  @staticmethod
  def children_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuick3DObjectPrivate::children_count(QQmlListProperty<QQuick3DObject>
    *a0)': names 'QQmlListProperty<QQuick3DObject>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.children_count' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuick3DObjectPrivate::children_count(QQmlListProperty<QQuick3DObje"
        "ct> *a0)': names 'QQmlListProperty<QQuick3DObject>', which has no "
        "cute class yet.")

  @staticmethod
  def data(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuick3DObjectPrivate::data()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.data' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuick3DObjectPrivate::data()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def data_append(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DObjectPrivate::data_append(QQmlListProperty<QObject>
    *a0, QObject *a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.data_append' has no cute function yet. Qt's "
        "'void QQuick3DObjectPrivate::data_append(QQmlListProperty<QObject> "
        "*a0, QObject *a1)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def data_at(*__, **_) -> Never:
    """
    Qt's 'QObject *QQuick3DObjectPrivate::data_at(QQmlListProperty<QObject>
    *a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.data_at' has no cute function yet. Qt's "
        "'QObject *QQuick3DObjectPrivate::data_at(QQmlListProperty<QObject> "
        "*a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def data_clear(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DObjectPrivate::data_clear(QQmlListProperty<QObject>
    *a0)': names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.data_clear' has no cute function yet. Qt's "
        "'void QQuick3DObjectPrivate::data_clear(QQmlListProperty<QObject> "
        "*a0)': names 'QQmlListProperty<QObject>', which has no cute class "
        "yet.")

  @staticmethod
  def data_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuick3DObjectPrivate::data_count(QQmlListProperty<QObject> *a0)': names
    'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.data_count' has no cute function yet. Qt's "
        "'qsizetype "
        "QQuick3DObjectPrivate::data_count(QQmlListProperty<QObject> *a0)': "
        "names 'QQmlListProperty<QObject>', which has no cute class yet.")

  @staticmethod
  def refSceneManager(*__, **_) -> Never:
    """
    - Qt's 'void QQuick3DObjectPrivate::refSceneManager(QQuick3DSceneManager
      &a0)': takes a type Python has no way to hand over yet.
    - Qt's 'void QQuick3DObjectPrivate::refSceneManager(QQuick3DObject *obj,
      QQuick3DSceneManager &mgr)': takes a type Python has no way to hand
      over yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.refSceneManager' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DObjectPrivate::refSceneManager(QQuick3DSceneManager &a0)': "
        "takes a type Python has no way to hand over yet. Qt's 'void "
        "QQuick3DObjectPrivate::refSceneManager(QQuick3DObject *obj, "
        "QQuick3DSceneManager &mgr)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def resources(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuick3DObjectPrivate::resources()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.resources' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuick3DObjectPrivate::resources()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def resources_append(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DObjectPrivate::resources_append(QQmlListProperty<QObject> *a0,
    QObject *a1)': names 'QQmlListProperty<QObject>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.resources_append' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DObjectPrivate::resources_append(QQmlListProperty<QObject> "
        "*a0, QObject *a1)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def resources_at(*__, **_) -> Never:
    """
    Qt's 'QObject
    *QQuick3DObjectPrivate::resources_at(QQmlListProperty<QObject> *a0,
    qsizetype a1)': names 'QQmlListProperty<QObject>', which has no cute
    class yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.resources_at' has no cute function yet. "
        "Qt's 'QObject "
        "*QQuick3DObjectPrivate::resources_at(QQmlListProperty<QObject> "
        "*a0, qsizetype a1)': names 'QQmlListProperty<QObject>', which has "
        "no cute class yet.")

  @staticmethod
  def resources_clear(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DObjectPrivate::resources_clear(QQmlListProperty<QObject> *a0)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.resources_clear' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DObjectPrivate::resources_clear(QQmlListProperty<QObject> "
        "*a0)': names 'QQmlListProperty<QObject>', which has no cute class "
        "yet.")

  @staticmethod
  def resources_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype
    QQuick3DObjectPrivate::resources_count(QQmlListProperty<QObject> *a0)':
    names 'QQmlListProperty<QObject>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.resources_count' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQuick3DObjectPrivate::resources_count(QQmlListProperty<QObject> "
        "*a0)': names 'QQmlListProperty<QObject>', which has no cute class "
        "yet.")

  @staticmethod
  def states(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickState> QQuick3DObjectPrivate::states()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.states' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickState> QQuick3DObjectPrivate::states()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def transitions(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickTransition>
    QQuick3DObjectPrivate::transitions()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQuick3DObjectPrivate.transitions' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickTransition> "
        "QQuick3DObjectPrivate::transitions()': gives a type Python has no "
        "way to take yet.")
