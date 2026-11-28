"""
QSSGRenderableObjectHandle binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderableObjectHandle to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtQuick3DUtils import QSSGRenderFlag
  from . import QSSGRenderableObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderFlag = WAIT['QSSGRenderFlag']
  QSSGRenderableObject = WAIT['QSSGRenderableObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSSGRenderableObjectHandle(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGRenderableObjectHandle: a plain Python object
  standing in front of one C++ QSSGRenderableObjectHandle.

  C++ hands a QSSGRenderableObjectHandle around as a copy, so every C++
  QSSGRenderableObjectHandle behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QSSGRenderableObjectHandle yet. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderableObjectHandle::~QSSGRenderableObjectHandle()': the
    destructor: Python removes its C++ QSSGRenderableObjectHandle by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QSSGRenderableObjectHandle is created at the first use, not by
    'QSSGRenderableObjectHandle(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGRenderableObjectHandle back gives a copy the
    ritual made for Python, in a new cute QSSGRenderableObjectHandle.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderableObjectHandle'

  #  Qt's '~QSSGRenderableObjectHandle()'. Naming it makes this a value
  #  class: Python owns every C++ QSSGRenderableObjectHandle behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QSSGRenderableObjectHandleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderableObjectHandle::QSSGRenderableObjectHandle()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjecthandle.html
    """
    #  QSSGRenderableObjectHandle::QSSGRenderableObjectHandle()
    self._noteCreation(QSSGRenderableObjectHandle, lambda: Rituals.call(
        'ritual_ZN26QSSGRenderableObjectHandleC1Ev',
    ))

  @overload(QSSGRenderableObject, float, QSSGRenderFlag)
  @overload(NoneType, float, QSSGRenderFlag)
  def __init__(
      self,
      o: Optional[QSSGRenderableObject],
      camDistSq: float,
      tag: QSSGRenderFlag,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderableObjectHandle::QSSGRenderableObjectHandle(
    QSSGRenderableObject *o, float camDistSq, QSSGRenderNodeTag tag)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderableobjecthandle.html

    Parameters
    ----------

    o : Optional[QSSGRenderableObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    camDistSq : float
      Passed on as it is.

    tag : QSSGRenderFlag
      Passed on as a value: Qt reads the C++ QSSGRenderFlag, which stays
      Python's own.
    """
    #  QSSGRenderableObjectHandle::QSSGRenderableObjectHandle(
    #      QSSGRenderableObject *o, float camDistSq, QSSGRenderNodeTag tag)
    self._noteCreation(QSSGRenderableObjectHandle, lambda: Rituals.call(
        'ritual_ZN26QSSGRenderableObjectHandleC1EP20QSSGRenderableObjectf14'
        'QSSGRenderFlag',
        self._addressOf(o), camDistSq, self._valueOf(tag),
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


#  Qt's 'QList<QSSGRenderableObjectHandle>': the list of
#  QSSGRenderableObjectHandle, which 'QList[QSSGRenderableObjectHandle]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QSSGRenderableObjectHandle. Qt has a name of its own for it.
QSSGRenderableObjectList = QList.createKind(
    QSSGRenderableObjectHandle, 'value',
    name='QSSGRenderableObjectList',
    make='ritual_list_make_QSSGRenderableObjectHandle',
    add='ritual_list_add_QSSGRenderableObjectHandle',
    size='ritual_list_size_QSSGRenderableObjectHandle',
    at='ritual_list_at_QSSGRenderableObjectHandle',
    drop='ritual_list_drop_QSSGRenderableObjectHandle',
)
