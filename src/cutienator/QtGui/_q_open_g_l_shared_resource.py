"""
QOpenGLSharedResource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qopenglcontext_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QOpenGLSharedResource to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QOpenGLContext, QOpenGLContextGroup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLContext = WAIT['QOpenGLContext']
  QOpenGLContextGroup = WAIT['QOpenGLContextGroup']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLSharedResource(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLSharedResource: a plain Python object standing
  in front of one C++ QOpenGLSharedResource.

  What exists
  -----------

  Every function of Qt's QOpenGLSharedResource that has a ritual and that
  Python can call so far, 4 names in all: 'group', 'free',
  'invalidateResource', 'freeResource'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLSharedResource::~QOpenGLSharedResource()': the destructor:
    Python never removes a C++ QOpenGLSharedResource.

  What has no ritual
  ------------------

  4 of the 10 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QOpenGLSharedResource is created at the first use, not by
    'QOpenGLSharedResource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLSharedResource.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLSharedResource'

  #  A C++ QOpenGLSharedResource Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLSharedResource'

  #  The functions Qt calls itself that QOpenGLSharedResource is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'invalidateResource': (
          ('_ZN21QOpenGLSharedResource18invalidateResourceEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'freeResource': (
          ('_ZN21QOpenGLSharedResource12freeResourceEP14QOpenGLContext',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtGui:QOpenGLContext'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def group(self) -> Optional[QOpenGLContextGroup]:
    """
    Calls Qt's 'QOpenGLContextGroup *QOpenGLSharedResource::group() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglsharedresource.html#group

    Returns
    -------

    Optional[QOpenGLContextGroup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLContextGroup *QOpenGLSharedResource::group() const
    address = self.uglySide.call('ritual_ZNK21QOpenGLSharedResource5groupEv')
    from . import QOpenGLContextGroup
    return QOpenGLContextGroup._cuteAt(address)

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

  @overload(QOpenGLContextGroup)
  @overload(NoneType)
  def __init__(self, group: Optional[QOpenGLContextGroup]) -> None:
    """
    Notes what was given, for Qt's
    'QOpenGLSharedResource::QOpenGLSharedResource(QOpenGLContextGroup
    *group)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglsharedresource.html#QOpenGLSharedResource

    Parameters
    ----------

    group : Optional[QOpenGLContextGroup]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QOpenGLSharedResource::QOpenGLSharedResource(QOpenGLContextGroup
    #      *group)
    self._noteCreation(QOpenGLSharedResource, lambda: Rituals.call(
        'ritual_ZN21QOpenGLSharedResourceC1EP19QOpenGLContextGroup',
        self._addressOf(group),
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

  def free(self) -> None:
    """
    Calls Qt's 'void QOpenGLSharedResource::free()'.

    Qt's own words: https://doc.qt.io/qt-6/qopenglsharedresource.html#free
    """
    #  void QOpenGLSharedResource::free()
    self.uglySide.call('ritual_ZN21QOpenGLSharedResource4freeEv')

  def invalidateResource(self) -> None:
    """
    Calls Qt's 'void QOpenGLSharedResource::invalidateResource()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglsharedresource.html#invalidateResource
    """
    #  void QOpenGLSharedResource::invalidateResource()
    self.uglySide.call(
        'ritual_ZN21QOpenGLSharedResource18invalidateResourceEv',
    )

  @overload(QOpenGLContext)
  @overload(NoneType)
  def freeResource(self, context: Optional[QOpenGLContext]) -> None:
    """
    Calls Qt's 'void QOpenGLSharedResource::freeResource(QOpenGLContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglsharedresource.html#freeResource

    Parameters
    ----------

    context : Optional[QOpenGLContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLSharedResource::freeResource(QOpenGLContext *context)
    self.uglySide.call(
        'ritual_ZN21QOpenGLSharedResource12freeResourceEP14QOpenGLContext',
        self._addressOf(context),
    )


#  Qt's 'QList<QOpenGLSharedResource *>': the list of QOpenGLSharedResource,
#  which 'QList[QOpenGLSharedResource]' gives. It is made here, so that there
#  is one as soon as there can be a QOpenGLSharedResource.
QList.createKind(
    QOpenGLSharedResource, 'address',
    make='ritual_list_make_QOpenGLSharedResource_ptr',
    add='ritual_list_add_QOpenGLSharedResource_ptr',
    size='ritual_list_size_QOpenGLSharedResource_ptr',
    at='ritual_list_at_QOpenGLSharedResource_ptr',
    drop='ritual_list_drop_QOpenGLSharedResource_ptr',
)
