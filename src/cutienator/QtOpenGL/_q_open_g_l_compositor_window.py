"""
QOpenGLCompositorWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpenGL/6.12.0/QtOpenGL/private/qopenglcompositor_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QOpenGLCompositorWindow to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QPlatformTextureList, QWindow
  from . import QOpenGLCompositorBackingStore
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpenGLCompositorBackingStore = WAIT['QOpenGLCompositorBackingStore']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QOpenGLCompositorWindow(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpenGLCompositorWindow: a plain Python object
  standing in front of one C++ QOpenGLCompositorWindow.

  What exists
  -----------

  Every function of Qt's QOpenGLCompositorWindow that has a ritual and that
  Python can call so far, 6 names in all: 'sourceWindow', 'textures',
  'beginCompositing', 'endCompositing', 'setBackingStore', 'backingStore'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpenGLCompositorWindow::~QOpenGLCompositorWindow()': the
    destructor: Python never removes a C++ QOpenGLCompositorWindow.

  What to expect
  --------------

  - The C++ QOpenGLCompositorWindow is created at the first use, not by
    'QOpenGLCompositorWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QOpenGLCompositorWindow.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpenGLCompositorWindow'

  #  A C++ QOpenGLCompositorWindow Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QOpenGLCompositorWindow'

  #  The functions Qt calls itself that QOpenGLCompositorWindow is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'sourceWindow': (
          ('_ZNK23QOpenGLCompositorWindow12sourceWindowEv',
           ('address', 'address', 'QtGui:QWindow'),
           ()),
      ),
      'textures': (
          ('_ZNK23QOpenGLCompositorWindow8texturesEv',
           ('address', 'address', 'QtGui:QPlatformTextureList'),
           ()),
      ),
      'beginCompositing': (
          ('_ZN23QOpenGLCompositorWindow16beginCompositingEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'endCompositing': (
          ('_ZN23QOpenGLCompositorWindow14endCompositingEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setBackingStore': (
          ('_ZN23QOpenGLCompositorWindow15setBackingStoreEP29QOpenGLComposi'
           'torBackingStore',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address',
                'QtOpenGL:QOpenGLCompositorBackingStore'),
           )),
      ),
      'backingStore': (
          ('_ZNK23QOpenGLCompositorWindow12backingStoreEv',
           ('address', 'address', 'QtOpenGL:QOpenGLCompositorBackingStore'),
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

  def sourceWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QOpenGLCompositorWindow::sourceWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorwindow.html#sourceWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QOpenGLCompositorWindow::sourceWindow() const
    address = self.uglySide.call(
        'ritual_ZNK23QOpenGLCompositorWindow12sourceWindowEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def textures(self) -> Optional[QPlatformTextureList]:
    """
    Calls Qt's 'const QPlatformTextureList
    *QOpenGLCompositorWindow::textures() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorwindow.html#textures

    Returns
    -------

    Optional[QPlatformTextureList]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QPlatformTextureList *QOpenGLCompositorWindow::textures() const
    address = self.uglySide.call(
        'ritual_ZNK23QOpenGLCompositorWindow8texturesEv',
    )
    from ..QtGui import QPlatformTextureList
    return QPlatformTextureList._cuteAt(address)

  def backingStore(self) -> Optional[QOpenGLCompositorBackingStore]:
    """
    Calls Qt's 'QOpenGLCompositorBackingStore
    *QOpenGLCompositorWindow::backingStore() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorwindow.html#backingStore

    Returns
    -------

    Optional[QOpenGLCompositorBackingStore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QOpenGLCompositorBackingStore *QOpenGLCompositorWindow::backingStore()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK23QOpenGLCompositorWindow12backingStoreEv',
    )
    from . import QOpenGLCompositorBackingStore
    return QOpenGLCompositorBackingStore._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpenGLCompositorBackingStore)
  @overload(NoneType)
  def setBackingStore(
      self,
      backingStore: Optional[QOpenGLCompositorBackingStore],
  ) -> None:
    """
    Calls Qt's 'void
    QOpenGLCompositorWindow::setBackingStore(QOpenGLCompositorBackingStore
    *backingStore)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorwindow.html#setBackingStore

    Parameters
    ----------

    backingStore : Optional[QOpenGLCompositorBackingStore]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QOpenGLCompositorWindow::setBackingStore(
    #      QOpenGLCompositorBackingStore *backingStore)
    self.uglySide.call(
        'ritual_ZN23QOpenGLCompositorWindow15setBackingStoreEP29QOpenGLComp'
        'ositorBackingStore',
        self._addressOf(backingStore),
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

  def beginCompositing(self) -> None:
    """
    Calls Qt's 'void QOpenGLCompositorWindow::beginCompositing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorwindow.html#beginCompositing
    """
    #  void QOpenGLCompositorWindow::beginCompositing()
    ritual = 'ritual_ZN23QOpenGLCompositorWindow16beginCompositingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QOpenGLCompositorWindow16beginCompositingEv'
    self.uglySide.call(ritual)

  def endCompositing(self) -> None:
    """
    Calls Qt's 'void QOpenGLCompositorWindow::endCompositing()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopenglcompositorwindow.html#endCompositing
    """
    #  void QOpenGLCompositorWindow::endCompositing()
    ritual = 'ritual_ZN23QOpenGLCompositorWindow14endCompositingEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QOpenGLCompositorWindow14endCompositingEv'
    self.uglySide.call(ritual)


#  Qt's 'QList<QOpenGLCompositorWindow *>': the list of
#  QOpenGLCompositorWindow, which 'QList[QOpenGLCompositorWindow]' gives. It
#  is made here, so that there is one as soon as there can be a
#  QOpenGLCompositorWindow.
QList.createKind(
    QOpenGLCompositorWindow, 'address',
    make='ritual_list_make_QOpenGLCompositorWindow_ptr',
    add='ritual_list_add_QOpenGLCompositorWindow_ptr',
    size='ritual_list_size_QOpenGLCompositorWindow_ptr',
    at='ritual_list_at_QOpenGLCompositorWindow_ptr',
    drop='ritual_list_drop_QOpenGLCompositorWindow_ptr',
)
