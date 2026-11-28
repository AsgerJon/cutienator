"""
Qt3DRender::QSceneExporter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qsceneexporter_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::QSceneExporter to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QHash, QObject, QStringList
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSceneExporter(QObject):
  """
  The cute side of Qt's Qt3DRender::QSceneExporter: a plain Python object
  standing in front of one C++ Qt3DRender::QSceneExporter.

  It is built on the cute 'QObject', as Qt's Qt3DRender::QSceneExporter is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QSceneExporter that has a ritual and
  that Python can call so far, 7 names in all: 'metaObject', 'tr',
  'exportScene', 'errors', 'errorsChanged', 'logError', 'logInfo'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QSceneExporter::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QSceneExporter::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QSceneExporter::~QSceneExporter()': the destructor:
    Python never removes a C++ Qt3DRender::QSceneExporter.

  What has no ritual
  ------------------

  3 of the 13 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ Qt3DRender::QSceneExporter is created at the first use, not by
    'Qt3DRender::QSceneExporter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QSceneExporter.
  - Qt tells when it has removed the C++ Qt3DRender::QSceneExporter. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's Qt3DRender::QSceneExporter that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString Qt3DRender::QSceneExporter::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qsceneexporter.html#tr

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
    #  QString Qt3DRender::QSceneExporter::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender14QSceneExporter2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QSceneExporter'

  #  A C++ Qt3DRender::QSceneExporter Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QSceneExporter'

  #  The functions Qt calls itself that Qt3DRender::QSceneExporter is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'exportScene': (
          'bool Qt3DRender::QSceneExporter::exportScene(Qt3DCore::QEntity '
          '*, const QString &, const QString &, const QVariantHash &)',
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
    Calls Qt's 'const QMetaObject *Qt3DRender::QSceneExporter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneexporter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QSceneExporter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QSceneExporter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def errors(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DRender::QSceneExporter::errors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneexporter.html#errors

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::QSceneExporter::errors() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender14QSceneExporter6errorsEv',
    )
    return QStringList._cuteOwning(address)

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
    Qt's 'Qt3DRender::QSceneExporter::QSceneExporter()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'Qt3DRender.QSceneExporter.__init__' has no cute function yet. "
        "Qt's 'Qt3DRender::QSceneExporter::QSceneExporter()': the class is "
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

  @overload(WAIT['Qt3DCore.QEntity'], str, str, QHash[str, QVariant])
  @overload(NoneType, str, str, QHash[str, QVariant])
  def exportScene(
      self,
      sceneRoot: Optional[Qt3DCore.QEntity],
      outDir: str,
      exportName: str,
      options: QHash[str, QVariant],
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::QSceneExporter::exportScene(Qt3DCore::QEntity *sceneRoot,
    const QString &outDir, const QString &exportName, const QVariantHash
    &options)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneexporter.html#exportScene

    Parameters
    ----------

    sceneRoot : Optional[Qt3DCore.QEntity]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    outDir : str
      Passed on as it is: a QString is made of it for the call.

    exportName : str
      Passed on as it is: a QString is made of it for the call.

    options : QHash[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool Qt3DRender::QSceneExporter::exportScene(Qt3DCore::QEntity
    #      *sceneRoot, const QString &outDir, const QString &exportName,
    #      const QVariantHash &options)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneExporter11exportSceneEPN8Qt3DCore7QEn'
        'tityERK7QStringS6_RK5QHashIS4_8QVariantE',
        self._addressOf(sceneRoot), outDir, exportName,
        self._valueOf(options),
    )

  @overload(QStringList)
  def errorsChanged(self, errors: QStringList) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneExporter::errorsChanged(const
    QStringList &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneexporter.html#errorsChanged

    Parameters
    ----------

    errors : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void Qt3DRender::QSceneExporter::errorsChanged(const QStringList
    #      &errors)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneExporter13errorsChangedERK5QListI7QSt'
        'ringE',
        self._valueOf(errors),
    )

  @overload(str)
  def logError(self, error: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneExporter::logError(const QString
    &error)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneexporter.html#logError

    Parameters
    ----------

    error : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QSceneExporter::logError(const QString &error)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneExporter8logErrorERK7QString', error,
    )

  @overload(str)
  def logInfo(self, info: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneExporter::logInfo(const QString
    &info)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneexporter.html#logInfo

    Parameters
    ----------

    info : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QSceneExporter::logInfo(const QString &info)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender14QSceneExporter7logInfoERK7QString', info,
    )
