"""
qdesigner_internal::QDesignerFormWindowManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_formwindowmanager_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means qdesigner_internal::QDesignerFormWindowManager to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QDesignerFormWindowManagerInterface, qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerFormWindowManager(QDesignerFormWindowManagerInterface):
  """
  The cute side of Qt's qdesigner_internal::QDesignerFormWindowManager: a
  plain Python object standing in front of one C++
  qdesigner_internal::QDesignerFormWindowManager.

  It is built on the cute 'QDesignerFormWindowManagerInterface', as Qt's
  qdesigner_internal::QDesignerFormWindowManager is built on Qt's
  QDesignerFormWindowManagerInterface, and has everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::QDesignerFormWindowManager that
  has a ritual and that Python can call so far, 4 names in all: 'metaObject',
  'tr', 'previewManager', 'showPluginDialog'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void
    *qdesigner_internal::QDesignerFormWindowManager::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::QDesignerFormWindowManager::qt_metacall(
    QMetaObject::Call a0, int a1, void **a2)': one of Qt's own inner
    workings.
  - Qt's 'qdesigner_internal::QDesignerFormWindowManager::
    ~QDesignerFormWindowManager()': the destructor: Python never removes a
    C++ qdesigner_internal::QDesignerFormWindowManager.

  What has no ritual
  ------------------

  3 of the 10 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ qdesigner_internal::QDesignerFormWindowManager is created at the
    first use, not by 'qdesigner_internal::QDesignerFormWindowManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++
    qdesigner_internal::QDesignerFormWindowManager.
  - Qt tells when it has removed the C++
    qdesigner_internal::QDesignerFormWindowManager. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's qdesigner_internal::QDesignerFormWindowManager that has
    no cute function yet, '__init__', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString
    qdesigner_internal::QDesignerFormWindowManager::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowmanager.html

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
    #  QString qdesigner_internal::QDesignerFormWindowManager::tr(const char
    #      *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal26QDesignerFormWindowManager2trEPKcS2'
        '_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::QDesignerFormWindowManager'

  #  A C++ qdesigner_internal::QDesignerFormWindowManager Python makes is of
  #  a C++ class of ours, in which Python can take functions over. This
  #  ritual hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_qdesigner_internal_QDesignerFormWindowManager'

  #  The functions Qt calls itself that
  #  qdesigner_internal::QDesignerFormWindowManager is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'previewManager': (
          ('_ZNK18qdesigner_internal26QDesignerFormWindowManager14previewMa'
           'nagerEv',
           ('address', 'address',
            'QtDesigner:qdesigner_internal.PreviewManager'),
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
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::QDesignerFormWindowManager::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowmanager.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::QDesignerFormWindowManager::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal26QDesignerFormWindowManager10metaOb'
        'jectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def previewManager(self) -> Optional[qdesigner_internal.PreviewManager]:
    """
    Calls Qt's 'PreviewManager
    *qdesigner_internal::QDesignerFormWindowManager::previewManager() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowmanager.html

    Returns
    -------

    Optional[qdesigner_internal.PreviewManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  PreviewManager
    #      *qdesigner_internal::QDesignerFormWindowManager::previewManager()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal26QDesignerFormWindowManager14previe'
        'wManagerEv',
    )
    return qdesigner_internal.PreviewManager._cuteAt(address)

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
    Qt's 'qdesigner_internal::QDesignerFormWindowManager::
    QDesignerFormWindowManager(QObject *parent)': the class is abstract, so
    C++ cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'qdesigner_internal.QDesignerFormWindowManager.__init__' has no "
        "cute function yet. Qt's "
        "'qdesigner_internal::QDesignerFormWindowManager::QDesignerFormWindo"
        "wManager(QObject *parent)': the class is abstract, so C++ cannot "
        "make one, and the C++ class of ours does not fill in every "
        "function it leaves open.")

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

  def showPluginDialog(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::QDesignerFormWindowManager::showPluginDialog()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-qdesignerformwindowmanager.html
    """
    #  void
    #      qdesigner_internal::QDesignerFormWindowManager::showPluginDialog()
    ritual = (
        'ritual_ZN18qdesigner_internal26QDesignerFormWindowManager16showPlu'
        'ginDialogEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal26QDesignerFormWindowManager16s'
          'howPluginDialogEv')
    self.uglySide.call(ritual)
