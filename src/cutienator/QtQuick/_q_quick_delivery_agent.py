"""
QQuickDeliveryAgent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickdeliveryagent_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickDeliveryAgent to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPointF
  from . import QQuickDeliveryAgentPrivate, QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickDeliveryAgent(QObject):
  """
  The cute side of Qt's QQuickDeliveryAgent: a plain Python object standing
  in front of one C++ QQuickDeliveryAgent.

  It is built on the cute 'QObject', as Qt's QQuickDeliveryAgent is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickDeliveryAgent that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'd_func',
  'rootItem', 'sceneTransform', 'setSceneTransform', 'event'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickDeliveryAgent::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickDeliveryAgent::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickDeliveryAgentPrivate *QQuickDeliveryAgent::d_func()
    const': takes in Python what 'QQuickDeliveryAgentPrivate
    *QQuickDeliveryAgent::d_func()' takes.
  - Qt's 'QQuickDeliveryAgent::~QQuickDeliveryAgent()': the destructor:
    Python never removes a C++ QQuickDeliveryAgent.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickDeliveryAgent is created at the first use, not by
    'QQuickDeliveryAgent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickDeliveryAgent.
  - Qt tells when it has removed the C++ QQuickDeliveryAgent. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The classes Qt writes inside QQuickDeliveryAgent, each a class in here
  #  as in C++.

  class Transform(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickDeliveryAgent::Transform: a plain Python
    object standing in front of one C++ QQuickDeliveryAgent::Transform.

    What exists
    -----------

    Every function of Qt's QQuickDeliveryAgent::Transform that has a ritual
    and that Python can call so far, 1 name in all: 'map'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickDeliveryAgent::Transform::~Transform()': the destructor:
      Python never removes a C++ QQuickDeliveryAgent::Transform.

    What to expect
    --------------

    - The C++ QQuickDeliveryAgent::Transform is created at the first use, not
      by 'QQuickDeliveryAgent::Transform(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QQuickDeliveryAgent::Transform.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QPointF = WAIT['QPointF']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickDeliveryAgent::Transform'

    #  A C++ QQuickDeliveryAgent::Transform Python makes is of a C++ class of
    #  ours, in which Python can take functions over. This ritual hands one
    #  over; see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QQuickDeliveryAgent_Transform'

    #  The functions Qt calls itself that QQuickDeliveryAgent::Transform is
    #  the first to declare. A class of a program built on it can write one
    #  anew, and Qt then calls that. For each name: the key C++ knows the
    #  function by, what it gives, and what it takes.
    __virtual_functions__ = {
        'map': (
            ('_ZN19QQuickDeliveryAgent9Transform3mapERK7QPointF',
             ('address', 'value', 'QtCore:QPointF'),
             (
                 ('address', 'value', 'QtCore:QPointF'),
             )),
        ),
    }

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

    @overload(QPointF)
    def map(self, point: QPointF) -> QPointF:
      """
      Calls Qt's 'QPointF QQuickDeliveryAgent::Transform::map(const QPointF
      &point)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qquickdeliveryagent-transform.html#map

      Parameters
      ----------

      point : QPointF
        Passed on as a value: Qt reads the C++ QPointF, which stays Python's
        own.

      Returns
      -------

      QPointF
        A new cute QPointF around the copy Qt gave back. Python owns it.
      """
      #  QPointF QQuickDeliveryAgent::Transform::map(const QPointF &point)
      address = self.uglySide.call(
          'ritual_ZN19QQuickDeliveryAgent9Transform3mapERK7QPointF',
          self._valueOf(point, 'QPointF'),
      )
      from ..QtCore import QPointF
      return QPointF._cuteOwning(address)

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
    Calls Qt's 'QString QQuickDeliveryAgent::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdeliveryagent.html#tr

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
    #  QString QQuickDeliveryAgent::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickDeliveryAgent2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickDeliveryAgent'

  #  A C++ QQuickDeliveryAgent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickDeliveryAgent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickDeliveryAgent::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickDeliveryAgent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickDeliveryAgent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def rootItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickDeliveryAgent::rootItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdeliveryagent.html#rootItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickDeliveryAgent::rootItem() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickDeliveryAgent8rootItemEv',
    )
    from . import QQuickItem
    return QQuickItem._cuteAt(address)

  def sceneTransform(self) -> Optional[Transform]:
    """
    Calls Qt's 'Transform *QQuickDeliveryAgent::sceneTransform() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagent.html#sceneTransform

    Returns
    -------

    Optional[Transform]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Transform *QQuickDeliveryAgent::sceneTransform() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickDeliveryAgent14sceneTransformEv',
    )
    return QQuickDeliveryAgent.Transform._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Transform)
  @overload(NoneType)
  def setSceneTransform(self, transform: Optional[Transform]) -> None:
    """
    Calls Qt's 'void QQuickDeliveryAgent::setSceneTransform(Transform
    *transform)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagent.html#setSceneTransform

    Parameters
    ----------

    transform : Optional[Transform]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickDeliveryAgent::setSceneTransform(Transform *transform)
    self.uglySide.call(
        'ritual_ZN19QQuickDeliveryAgent17setSceneTransformEPNS_9TransformE',
        self._addressOf(transform),
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

  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, rootItem: Optional[QQuickItem]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickDeliveryAgent::QQuickDeliveryAgent(QQuickItem *rootItem)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickdeliveryagent.html#QQuickDeliveryAgent

    Parameters
    ----------

    rootItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickDeliveryAgent::QQuickDeliveryAgent(QQuickItem *rootItem)
    self._noteCreation(QQuickDeliveryAgent, lambda: Rituals.call(
        'ritual_ZN19QQuickDeliveryAgentC1EP10QQuickItem',
        self._addressOf(rootItem),
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

  def d_func(self) -> Optional[QQuickDeliveryAgentPrivate]:
    """
    Calls Qt's 'QQuickDeliveryAgentPrivate *QQuickDeliveryAgent::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdeliveryagent.html#d_func

    Returns
    -------

    Optional[QQuickDeliveryAgentPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickDeliveryAgentPrivate *QQuickDeliveryAgent::d_func()
    address = self.uglySide.call('ritual_ZN19QQuickDeliveryAgent6d_funcEv')
    from . import QQuickDeliveryAgentPrivate
    return QQuickDeliveryAgentPrivate._cuteAt(address)

  @overload(QEvent)
  @overload(NoneType)
  def event(self, ev: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickDeliveryAgent::event(QEvent *ev)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickdeliveryagent.html#event

    Parameters
    ----------

    ev : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickDeliveryAgent::event(QEvent *ev)
    ritual = 'ritual_ZN19QQuickDeliveryAgent5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickDeliveryAgent5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(ev))
