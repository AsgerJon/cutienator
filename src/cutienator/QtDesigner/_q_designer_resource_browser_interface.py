"""
QDesignerResourceBrowserInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/abstractresourcebrowser.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDesignerResourceBrowserInterface(QWidget):
  """
  The cute side of Qt's QDesignerResourceBrowserInterface: a plain Python
  object standing in front of one C++ QDesignerResourceBrowserInterface.

  It is built on the cute 'QWidget', as Qt's
  QDesignerResourceBrowserInterface is built on Qt's QWidget, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QDesignerResourceBrowserInterface that has a ritual
  and that Python can call so far, 6 names in all: 'metaObject', 'tr',
  'setCurrentPath', 'currentPath', 'currentPathChanged', 'pathActivated'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDesignerResourceBrowserInterface::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int
    QDesignerResourceBrowserInterface::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's
    'QDesignerResourceBrowserInterface::~QDesignerResourceBrowserInterface(
    )': the destructor: Python never removes a C++
    QDesignerResourceBrowserInterface.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDesignerResourceBrowserInterface is created at the first use,
    not by 'QDesignerResourceBrowserInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDesignerResourceBrowserInterface.
  - Qt tells when it has removed the C++ QDesignerResourceBrowserInterface.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QDesignerResourceBrowserInterface::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerresourcebrowserinterface.html#tr

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
    #  QString QDesignerResourceBrowserInterface::tr(const char *s, const
    #      char *c, int n)
    return Rituals.call(
        'ritual_ZN33QDesignerResourceBrowserInterface2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDesignerResourceBrowserInterface'

  #  A C++ QDesignerResourceBrowserInterface Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDesignerResourceBrowserInterface'

  #  The functions Qt calls itself that QDesignerResourceBrowserInterface is
  #  the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setCurrentPath': (
          ('_ZN33QDesignerResourceBrowserInterface14setCurrentPathERK7QStri'
           'ng',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'currentPath': (
          ('_ZNK33QDesignerResourceBrowserInterface11currentPathEv',
           ('address', 'text', ''),
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
    *QDesignerResourceBrowserInterface::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerresourcebrowserinterface.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDesignerResourceBrowserInterface::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK33QDesignerResourceBrowserInterface10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def currentPath(self) -> str:
    """
    Calls Qt's 'QString QDesignerResourceBrowserInterface::currentPath()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerresourcebrowserinterface.html#currentPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDesignerResourceBrowserInterface::currentPath() const
    return self.uglySide.call(
        'ritual_ZNK33QDesignerResourceBrowserInterface11currentPathEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setCurrentPath(self, filePath: str) -> None:
    """
    Calls Qt's 'void QDesignerResourceBrowserInterface::setCurrentPath(const
    QString &filePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerresourcebrowserinterface.html

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerResourceBrowserInterface::setCurrentPath(const QString
    #      &filePath)
    self.uglySide.call(
        'ritual_ZN33QDesignerResourceBrowserInterface14setCurrentPathERK7QS'
        'tring',
        filePath,
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's
    'QDesignerResourceBrowserInterface::QDesignerResourceBrowserInterface(
    QWidget *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerresourcebrowserinterface.html

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDesignerResourceBrowserInterface::
    #      QDesignerResourceBrowserInterface(QWidget *parent)
    self._noteCreation(
        QDesignerResourceBrowserInterface, lambda: Rituals.call(
            'ritual_ZN33QDesignerResourceBrowserInterfaceC1EP7QWidget',
            self._addressOf(parent),
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

  @overload(str)
  def currentPathChanged(self, filePath: str) -> None:
    """
    Calls Qt's 'void
    QDesignerResourceBrowserInterface::currentPathChanged(const QString
    &filePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerresourcebrowserinterface.html

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerResourceBrowserInterface::currentPathChanged(const
    #      QString &filePath)
    self.uglySide.call(
        'ritual_ZN33QDesignerResourceBrowserInterface18currentPathChangedER'
        'K7QString',
        filePath,
    )

  @overload(str)
  def pathActivated(self, filePath: str) -> None:
    """
    Calls Qt's 'void QDesignerResourceBrowserInterface::pathActivated(const
    QString &filePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesignerresourcebrowserinterface.html

    Parameters
    ----------

    filePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDesignerResourceBrowserInterface::pathActivated(const QString
    #      &filePath)
    self.uglySide.call(
        'ritual_ZN33QDesignerResourceBrowserInterface13pathActivatedERK7QSt'
        'ring',
        filePath,
    )
