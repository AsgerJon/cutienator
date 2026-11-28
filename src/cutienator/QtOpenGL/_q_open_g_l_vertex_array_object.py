"""
QOpenGLVertexArrayObject binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/qopenglvertexarrayobject.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLVertexArrayObject(QObject):
  """
  The cute side of Qt's QOpenGLVertexArrayObject: a plain Python object
  standing in front of one C++ QOpenGLVertexArrayObject.

  It is built on the cute 'QObject', as Qt's QOpenGLVertexArrayObject is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QOpenGLVertexArrayObject that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'create',
  'destroy', 'isCreated', 'objectId', 'bind', 'release'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QOpenGLVertexArrayObject::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QOpenGLVertexArrayObject::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QOpenGLVertexArrayObject::~QOpenGLVertexArrayObject()': the
    destructor: Python never removes a C++ QOpenGLVertexArrayObject.
  - Qt's 'QOpenGLVertexArrayObjectPrivate
    *QOpenGLVertexArrayObject::d_func()': gives
    'QOpenGLVertexArrayObjectPrivate', which has no cute class yet.
  - Qt's 'const QOpenGLVertexArrayObjectPrivate
    *QOpenGLVertexArrayObject::d_func() const': gives
    'QOpenGLVertexArrayObjectPrivate', which has no cute class yet.
  - Qt's 'QOpenGLVertexArrayObject::QOpenGLVertexArrayObject(
    QOpenGLVertexArrayObjectPrivate &dd)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLVertexArrayObject is created at the first use, not by
    'QOpenGLVertexArrayObject(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLVertexArrayObject.
  - Qt tells when it has removed the C++ QOpenGLVertexArrayObject. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The classes Qt writes inside QOpenGLVertexArrayObject, each a class in
  #  here as in C++.

  class Binder(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QOpenGLVertexArrayObject::Binder: a plain Python
    object standing in front of one C++ QOpenGLVertexArrayObject::Binder.

    What exists
    -----------

    Every function of Qt's QOpenGLVertexArrayObject::Binder that has a ritual
    and that Python can call so far, 2 names in all: 'release', 'rebind'. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QOpenGLVertexArrayObject::Binder::~Binder()': the destructor:
      Python never removes a C++ QOpenGLVertexArrayObject::Binder.

    What has no ritual
    ------------------

    2 of the 6 functions Qt declares: 2 forbidden.

    What to expect
    --------------

    - The C++ QOpenGLVertexArrayObject::Binder is created at the first use,
      not by 'QOpenGLVertexArrayObject::Binder(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QOpenGLVertexArrayObject::Binder.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QOpenGLVertexArrayObject = WAIT['QOpenGLVertexArrayObject']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QOpenGLVertexArrayObject::Binder'

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

    @overload(QOpenGLVertexArrayObject)
    @overload(NoneType)
    def __init__(self, v: Optional[QOpenGLVertexArrayObject]) -> None:
      """
      Notes what was given, for Qt's
      'QOpenGLVertexArrayObject::Binder::Binder(QOpenGLVertexArrayObject
      *v)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qopenglvertexarrayobject-binder.html#Binder

      Parameters
      ----------

      v : Optional[QOpenGLVertexArrayObject]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QOpenGLVertexArrayObject::Binder::Binder(QOpenGLVertexArrayObject
      #      *v)
      self._noteCreation(
          QOpenGLVertexArrayObject.Binder, lambda: Rituals.call(
              'ritual_ZN24QOpenGLVertexArrayObject6BinderC1EPS_',
              self._addressOf(v),
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

    def release(self) -> None:
      """
      Calls Qt's 'void QOpenGLVertexArrayObject::Binder::release()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopenglvertexarrayobject-binder.html#release
      """
      #  void QOpenGLVertexArrayObject::Binder::release()
      self.uglySide.call(
          'ritual_ZN24QOpenGLVertexArrayObject6Binder7releaseEv',
      )

    def rebind(self) -> None:
      """
      Calls Qt's 'void QOpenGLVertexArrayObject::Binder::rebind()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qopenglvertexarrayobject-binder.html#rebind
      """
      #  void QOpenGLVertexArrayObject::Binder::rebind()
      self.uglySide.call(
          'ritual_ZN24QOpenGLVertexArrayObject6Binder6rebindEv',
      )

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
    Calls Qt's 'QString QOpenGLVertexArrayObject::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#tr

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
    #  QString QOpenGLVertexArrayObject::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN24QOpenGLVertexArrayObject2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLVertexArrayObject'

  #  A C++ QOpenGLVertexArrayObject Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLVertexArrayObject'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QOpenGLVertexArrayObject::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QOpenGLVertexArrayObject::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK24QOpenGLVertexArrayObject10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isCreated(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLVertexArrayObject::isCreated() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#isCreated
    """
    #  bool QOpenGLVertexArrayObject::isCreated() const
    return self.uglySide.call(
        'ritual_ZNK24QOpenGLVertexArrayObject9isCreatedEv',
    )

  def objectId(self) -> int:
    """
    Calls Qt's 'GLuint QOpenGLVertexArrayObject::objectId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#objectId
    """
    #  GLuint QOpenGLVertexArrayObject::objectId() const
    return self.uglySide.call(
        'ritual_ZNK24QOpenGLVertexArrayObject8objectIdEv',
    )

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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLVertexArrayObject::QOpenGLVertexArrayObject(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobject.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QOpenGLVertexArrayObject::QOpenGLVertexArrayObject(QObject *parent)
    self._noteCreation(QOpenGLVertexArrayObject, lambda: Rituals.call(
        'ritual_ZN24QOpenGLVertexArrayObjectC1EP7QObject',
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

  def create(self) -> bool:
    """
    Calls Qt's 'bool QOpenGLVertexArrayObject::create()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#create
    """
    #  bool QOpenGLVertexArrayObject::create()
    return self.uglySide.call('ritual_ZN24QOpenGLVertexArrayObject6createEv')

  def destroy(self) -> None:
    """
    Calls Qt's 'void QOpenGLVertexArrayObject::destroy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#destroy
    """
    #  void QOpenGLVertexArrayObject::destroy()
    self.uglySide.call('ritual_ZN24QOpenGLVertexArrayObject7destroyEv')

  def bind(self) -> None:
    """
    Calls Qt's 'void QOpenGLVertexArrayObject::bind()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#bind
    """
    #  void QOpenGLVertexArrayObject::bind()
    self.uglySide.call('ritual_ZN24QOpenGLVertexArrayObject4bindEv')

  def release(self) -> None:
    """
    Calls Qt's 'void QOpenGLVertexArrayObject::release()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglvertexarrayobject.html#release
    """
    #  void QOpenGLVertexArrayObject::release()
    self.uglySide.call('ritual_ZN24QOpenGLVertexArrayObject7releaseEv')
