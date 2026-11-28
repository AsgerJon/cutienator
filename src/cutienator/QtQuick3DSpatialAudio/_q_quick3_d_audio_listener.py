"""
QQuick3DAudioListener binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3daudiolistener_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DAudioListener to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtSpatialAudio import QAudioListener
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DAudioListener(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DAudioListener: a plain Python object standing
  in front of one C++ QQuick3DAudioListener.

  What exists
  -----------

  Every function of Qt's QQuick3DAudioListener that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'listener',
  'updateSpatialNode', 'updatePosition', 'updateRotation'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DAudioListener::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DAudioListener::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DAudioListener::~QQuick3DAudioListener()': the destructor:
    Python never removes a C++ QQuick3DAudioListener.

  What has no ritual
  ------------------

  4 of the 12 functions Qt declares: 2 not a gap; 2 leans on
  'QQuick3DAudioListener.

  What to expect
  --------------

  - The C++ QQuick3DAudioListener is created at the first use, not by
    'QQuick3DAudioListener(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DAudioListener.
  - Qt tells when it has removed the C++ QQuick3DAudioListener. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DAudioListener that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DAudioListener'

  #  A C++ QQuick3DAudioListener Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DAudioListener'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DAudioListener::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudiolistener.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DAudioListener::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuick3DAudioListener10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
    Qt's 'QQuick3DAudioListener::QQuick3DAudioListener()': leans on
    'QQuick3DAudioListener::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DAudioListener.__init__' has no cute function yet. Qt's "
        "'QQuick3DAudioListener::QQuick3DAudioListener()': leans on "
        "'QQuick3DAudioListener::qt_metacall(QMetaObject::Call, int, "
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

  def listener(self) -> Optional[QAudioListener]:
    """
    Calls Qt's 'QAudioListener *QQuick3DAudioListener::listener()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudiolistener.html#listener

    Returns
    -------

    Optional[QAudioListener]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioListener *QQuick3DAudioListener::listener()
    address = self.uglySide.call(
        'ritual_ZN21QQuick3DAudioListener8listenerEv',
    )
    from ..QtSpatialAudio import QAudioListener
    return QAudioListener._cuteAt(address)

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      a0: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DAudioListener::updateSpatialNode(QSSGRenderGraphObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudiolistener.html#updateSpatialNode

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
    #      *QQuick3DAudioListener::updateSpatialNode(QSSGRenderGraphObject
    #      *a0)
    ritual = (
        'ritual_ZN21QQuick3DAudioListener17updateSpatialNodeEP21QSSGRenderG'
        'raphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuick3DAudioListener17updateSpatialNodeEP21QSSGR'
          'enderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)

  def updatePosition(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioListener::updatePosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudiolistener.html#updatePosition
    """
    #  void QQuick3DAudioListener::updatePosition()
    self.uglySide.call('ritual_ZN21QQuick3DAudioListener14updatePositionEv')

  def updateRotation(self) -> None:
    """
    Calls Qt's 'void QQuick3DAudioListener::updateRotation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3daudiolistener.html#updateRotation
    """
    #  void QQuick3DAudioListener::updateRotation()
    self.uglySide.call('ritual_ZN21QQuick3DAudioListener14updateRotationEv')
