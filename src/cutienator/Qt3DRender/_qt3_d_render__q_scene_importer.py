"""
Qt3DRender::QSceneImporter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qsceneimporter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QSceneImporter to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject, QStringList
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSceneImporter(QObject):
  """
  The cute side of Qt's Qt3DRender::QSceneImporter: a plain Python object
  standing in front of one C++ Qt3DRender::QSceneImporter.

  It is built on the cute 'QObject', as Qt's Qt3DRender::QSceneImporter is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QSceneImporter that has a ritual and
  that Python can call so far, 14 names in all: 'metaObject', 'tr',
  'setSource', 'setData', 'areFileTypesSupported', 'scene', 'node', 'status',
  'errors', 'statusChanged', 'errorsChanged', 'setStatus', 'logError',
  'logInfo'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QSceneImporter::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QSceneImporter::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QSceneImporter::~QSceneImporter()': the destructor:
    Python never removes a C++ Qt3DRender::QSceneImporter.

  What has no ritual
  ------------------

  3 of the 20 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ Qt3DRender::QSceneImporter is created at the first use, not by
    'Qt3DRender::QSceneImporter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QSceneImporter.
  - Qt tells when it has removed the C++ Qt3DRender::QSceneImporter. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QSceneImporter that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside Qt3DRender::QSceneImporter, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ParserStatus(CuteNum):
    """
    The enum 'Qt3DRender::QSceneImporter::ParserStatus' of Qt, with the 4
    names Qt gives in it.
    """

    Empty = Kee[int](0)
    Loading = Kee[int](1)
    Loaded = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString Qt3DRender::QSceneImporter::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#tr

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
    #  QString Qt3DRender::QSceneImporter::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender14QSceneImporter2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QSceneImporter'

  #  A C++ Qt3DRender::QSceneImporter Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QSceneImporter'

  #  The functions Qt calls itself that Qt3DRender::QSceneImporter is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'areFileTypesSupported': (
          'bool Qt3DRender::QSceneImporter::areFileTypesSupported(const '
          'QStringList &) const',
      ),
  }

  #  The functions Qt calls itself that Qt3DRender::QSceneImporter is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'setSource': (
          ('_ZN10Qt3DRender14QSceneImporter9setSourceERK4QUrl',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QUrl'),
           )),
      ),
      'setData': (
          ('_ZN10Qt3DRender14QSceneImporter7setDataERK10QByteArrayRK7QStrin'
           'g',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
               ('address', 'text', ''),
           )),
      ),
      'scene': (
          ('_ZN10Qt3DRender14QSceneImporter5sceneERK7QString',
           ('address', 'address', 'Qt3DCore:Qt3DCore.QEntity'),
           (
               ('address', 'text', ''),
           )),
      ),
      'node': (
          ('_ZN10Qt3DRender14QSceneImporter4nodeERK7QString',
           ('address', 'address', 'Qt3DCore:Qt3DCore.QEntity'),
           (
               ('address', 'text', ''),
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

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QSceneImporter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QSceneImporter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QSceneImporter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QStringList)
  def areFileTypesSupported(self, extensions: QStringList) -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QSceneImporter::areFileTypesSupported(const
    QStringList &extensions) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html

    Parameters
    ----------

    extensions : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool Qt3DRender::QSceneImporter::areFileTypesSupported(const
    #      QStringList &extensions) const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QSceneImporter21areFileTypesSupportedERK5Q'
        'ListI7QStringE',
        self._valueOf(extensions),
    )

  def status(self) -> ParserStatus:
    """
    Calls Qt's 'ParserStatus Qt3DRender::QSceneImporter::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#status

    Returns
    -------

    ParserStatus
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ParserStatus(number)'
      gives.
    """
    #  ParserStatus Qt3DRender::QSceneImporter::status() const
    return QSceneImporter.ParserStatus(self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QSceneImporter6statusEv',
    ))

  def errors(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DRender::QSceneImporter::errors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#errors

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::QSceneImporter::errors() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QSceneImporter6errorsEv',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneImporter::setSource(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QSceneImporter::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneImporter9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(QByteArray, str)
  def setData(self, data: QByteArray, basePath: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneImporter::setData(const QByteArray
    &data, const QString &basePath)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    basePath : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QSceneImporter::setData(const QByteArray &data, const
    #      QString &basePath)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneImporter7setDataERK10QByteArrayRK7QSt'
        'ring',
        self._valueOf(data), basePath,
    )

  @overload(ParserStatus)
  def setStatus(self, status: ParserStatus) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneImporter::setStatus(ParserStatus
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#setStatus

    Parameters
    ----------

    status : ParserStatus
      Passed on as its number.
    """
    #  void Qt3DRender::QSceneImporter::setStatus(ParserStatus status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneImporter9setStatusENS0_12ParserStatus'
        'E',
        status.value,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'Qt3DRender::QSceneImporter::QSceneImporter()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'Qt3DRender.QSceneImporter.__init__' has no cute function yet. "
        "Qt's 'Qt3DRender::QSceneImporter::QSceneImporter()': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  @overload()
  @overload(str)
  def scene(self, id: str = '') -> Optional[Qt3DCore.QEntity]:
    """
    Calls Qt's 'Qt3DCore::QEntity *Qt3DRender::QSceneImporter::scene(const
    QString &id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#scene

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    Optional[Qt3DCore.QEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QEntity *Qt3DRender::QSceneImporter::scene(const QString
    #      &id)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneImporter5sceneERK7QString', id,
    )
    return Qt3DCore.QEntity._cuteAt(address)

  @overload(str)
  def node(self, id: str) -> Optional[Qt3DCore.QEntity]:
    """
    Calls Qt's 'Qt3DCore::QEntity *Qt3DRender::QSceneImporter::node(const
    QString &id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#node

    Parameters
    ----------

    id : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[Qt3DCore.QEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QEntity *Qt3DRender::QSceneImporter::node(const QString &id)
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneImporter4nodeERK7QString', id,
    )
    return Qt3DCore.QEntity._cuteAt(address)

  @overload(ParserStatus)
  def statusChanged(self, status: ParserStatus) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneImporter::statusChanged(ParserStatus
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#statusChanged

    Parameters
    ----------

    status : ParserStatus
      Passed on as its number.
    """
    #  void Qt3DRender::QSceneImporter::statusChanged(ParserStatus status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneImporter13statusChangedENS0_12ParserS'
        'tatusE',
        status.value,
    )

  @overload(QStringList)
  def errorsChanged(self, errors: QStringList) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneImporter::errorsChanged(const
    QStringList &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#errorsChanged

    Parameters
    ----------

    errors : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DRender::QSceneImporter::errorsChanged(const QStringList
    #      &errors)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneImporter13errorsChangedERK5QListI7QSt'
        'ringE',
        self._valueOf(errors),
    )

  @overload(str)
  def logError(self, error: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneImporter::logError(const QString
    &error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#logError

    Parameters
    ----------

    error : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QSceneImporter::logError(const QString &error)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneImporter8logErrorERK7QString', error,
    )

  @overload(str)
  def logInfo(self, info: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneImporter::logInfo(const QString
    &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneimporter.html#logInfo

    Parameters
    ----------

    info : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QSceneImporter::logInfo(const QString &info)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneImporter7logInfoERK7QString', info,
    )
