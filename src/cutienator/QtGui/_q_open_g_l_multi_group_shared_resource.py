"""
QOpenGLMultiGroupSharedResource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qopenglcontext_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QOpenGLMultiGroupSharedResource to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QOpenGLContext, QOpenGLContextGroup, QOpenGLSharedResource
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']
  QOpenGLContextGroup = WAIT['QOpenGLContextGroup']
  QOpenGLSharedResource = WAIT['QOpenGLSharedResource']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLMultiGroupSharedResource(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLMultiGroupSharedResource: a plain Python
  object standing in front of one C++ QOpenGLMultiGroupSharedResource.

  What exists
  -----------

  Every function of Qt's QOpenGLMultiGroupSharedResource that has a ritual
  and that Python can call so far, 4 names in all: 'insert', 'cleanup',
  'value', 'resources'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QOpenGLMultiGroupSharedResource::~QOpenGLMultiGroupSharedResource()':
    the destructor: Python never removes a C++
    QOpenGLMultiGroupSharedResource.

  What has no ritual
  ------------------

  1 of the 7 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QOpenGLMultiGroupSharedResource is created at the first use, not
    by 'QOpenGLMultiGroupSharedResource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLMultiGroupSharedResource.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLMultiGroupSharedResource'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def resources(self) -> QList[QOpenGLSharedResource]:
    """
    Calls Qt's 'QList<QOpenGLSharedResource *>
    QOpenGLMultiGroupSharedResource::resources() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglmultigroupsharedresource.html#resources

    Returns
    -------

    QList[QOpenGLSharedResource]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpenGLSharedResource *>
    #      QOpenGLMultiGroupSharedResource::resources() const
    address = self.uglySide.call(
        'ritual_ZNK31QOpenGLMultiGroupSharedResource9resourcesEv',
    )
    from . import QOpenGLSharedResource
    return QList[QOpenGLSharedResource]._cuteOwning(address)

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
    'QOpenGLMultiGroupSharedResource::QOpenGLMultiGroupSharedResource()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglmultigroupsharedresource.html
    """
    #  QOpenGLMultiGroupSharedResource::QOpenGLMultiGroupSharedResource()
    self._noteCreation(QOpenGLMultiGroupSharedResource, lambda: Rituals.call(
        'ritual_ZN31QOpenGLMultiGroupSharedResourceC1Ev',
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

  @overload(QOpenGLContext, QOpenGLSharedResource)
  @overload(QOpenGLContext, NoneType)
  @overload(NoneType, QOpenGLSharedResource)
  @overload(NoneType, NoneType)
  def insert(
      self,
      context: Optional[QOpenGLContext],
      value: Optional[QOpenGLSharedResource],
  ) -> None:
    """
    Calls Qt's 'void QOpenGLMultiGroupSharedResource::insert(QOpenGLContext
    *context, QOpenGLSharedResource *value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglmultigroupsharedresource.html#insert

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : Optional[QOpenGLSharedResource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLMultiGroupSharedResource::insert(QOpenGLContext *context,
    #      QOpenGLSharedResource *value)
    self.uglySide.call(
        'ritual_ZN31QOpenGLMultiGroupSharedResource6insertEP14QOpenGLContex'
        'tP21QOpenGLSharedResource',
        self._addressOf(context), self._addressOf(value),
    )

  @overload(QOpenGLContextGroup, QOpenGLSharedResource)
  @overload(QOpenGLContextGroup, NoneType)
  @overload(NoneType, QOpenGLSharedResource)
  @overload(NoneType, NoneType)
  def cleanup(
      self,
      group: Optional[QOpenGLContextGroup],
      value: Optional[QOpenGLSharedResource],
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLMultiGroupSharedResource::cleanup(QOpenGLContextGroup *group,
    QOpenGLSharedResource *value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglmultigroupsharedresource.html#cleanup

    Parameters
    ----------

    group : Optional[QOpenGLContextGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : Optional[QOpenGLSharedResource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLMultiGroupSharedResource::cleanup(QOpenGLContextGroup
    #      *group, QOpenGLSharedResource *value)
    self.uglySide.call(
        'ritual_ZN31QOpenGLMultiGroupSharedResource7cleanupEP19QOpenGLConte'
        'xtGroupP21QOpenGLSharedResource',
        self._addressOf(group), self._addressOf(value),
    )

  @overload(QOpenGLContext)
  @overload(NoneType)
  def value(
      self,
      context: Optional[QOpenGLContext],
  ) -> Optional[QOpenGLSharedResource]:
    """
    Calls Qt's 'QOpenGLSharedResource
    *QOpenGLMultiGroupSharedResource::value(QOpenGLContext *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglmultigroupsharedresource.html#value

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QOpenGLSharedResource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLSharedResource
    #      *QOpenGLMultiGroupSharedResource::value(QOpenGLContext *context)
    address = self.uglySide.call(
        'ritual_ZN31QOpenGLMultiGroupSharedResource5valueEP14QOpenGLContext',
        self._addressOf(context),
    )
    from . import QOpenGLSharedResource
    return QOpenGLSharedResource._cuteAt(address)
