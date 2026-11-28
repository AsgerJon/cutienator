"""
QScxmlCompiler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/qscxmlcompiler.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QXmlStreamReader
  from . import QScxmlError, QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QXmlStreamReader = WAIT['QXmlStreamReader']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlCompiler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScxmlCompiler: a plain Python object standing in
  front of one C++ QScxmlCompiler.

  C++ hands a QScxmlCompiler around as a copy, so every C++ QScxmlCompiler
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QScxmlCompiler that has a ritual and that Python can
  call so far, 6 names in all: 'fileName', 'setFileName', 'loader',
  'setLoader', 'compile', 'errors'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QScxmlCompiler::~QScxmlCompiler()': the destructor: Python removes
    its C++ QScxmlCompiler by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QScxmlCompiler is created at the first use, not by
    'QScxmlCompiler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QScxmlCompiler back gives a copy the ritual made for
    Python, in a new cute QScxmlCompiler.
  """

  #  The classes Qt writes inside QScxmlCompiler, each a class in here as in
  #  C++.

  class Loader(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScxmlCompiler::Loader: a plain Python object
    standing in front of one C++ QScxmlCompiler::Loader.

    What exists
    -----------

    No function of Qt's QScxmlCompiler::Loader yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QScxmlCompiler::Loader::~Loader()': the destructor: Python never
      removes a C++ QScxmlCompiler::Loader.
    - Qt's 'QByteArray QScxmlCompiler::Loader::load(const QString &name,
      const QString &baseDir, QStringList *errors)': names 'QStringList',
      which has no cute class yet.

    What to expect
    --------------

    - The C++ QScxmlCompiler::Loader is created at the first use, not by
      'QScxmlCompiler::Loader(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - Python never removes the C++ QScxmlCompiler::Loader.
    - Each name of Qt's QScxmlCompiler::Loader that has no cute function yet,
      'load', holds a function that raises 'NotImplementedError', and its
      docstring says why.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScxmlCompiler::Loader'

    #  A C++ QScxmlCompiler::Loader Python makes is of a C++ class of ours,
    #  in which Python can take functions over. This ritual hands one over;
    #  see 'CuteMixin._takeOver'.
    __take_ritual__ = 'ritual_take_QScxmlCompiler_Loader'

    #  The functions Qt calls itself that QScxmlCompiler::Loader is the first
    #  to declare and that cannot be handed to Python yet, each as Qt
    #  declares it. A class of a program that writes one of them anew is
    #  refused, since Qt would never call what it wrote; see
    #  'CuteMixin._refuseLeftOut'.
    __virtual_left_out__ = {
        'load': (
            'QByteArray QScxmlCompiler::Loader::load(const QString &, '
            'const QString &, QStringList *)',
        ),
    }

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

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QScxmlCompiler::Loader::Loader()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlcompiler-loader.html#Loader
      """
      #  QScxmlCompiler::Loader::Loader()
      self._noteCreation(QScxmlCompiler.Loader, lambda: Rituals.call(
          'ritual_ZN14QScxmlCompiler6LoaderC1Ev',
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

    @staticmethod
    def load(*__, **_) -> Never:
      """
      Qt's 'QByteArray QScxmlCompiler::Loader::load(const QString &name,
      const QString &baseDir, QStringList *errors)': names 'QStringList',
      which has no cute class yet.
      """
      raise NotImplementedError(
          "'QScxmlCompiler.Loader.load' has no cute function yet. Qt's "
          "'QByteArray QScxmlCompiler::Loader::load(const QString &name, "
          "const QString &baseDir, QStringList *errors)': names "
          "'QStringList', which has no cute class yet.")

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlCompiler'

  #  Qt's '~QScxmlCompiler()'. Naming it makes this a value class: Python
  #  owns every C++ QScxmlCompiler behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QScxmlCompilerD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QScxmlCompiler::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcompiler.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlCompiler::fileName() const
    return self.uglySide.call('ritual_ZNK14QScxmlCompiler8fileNameEv')

  def loader(self) -> Optional[Loader]:
    """
    Calls Qt's 'Loader *QScxmlCompiler::loader() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcompiler.html#loader

    Returns
    -------

    Optional[Loader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Loader *QScxmlCompiler::loader() const
    address = self.uglySide.call('ritual_ZNK14QScxmlCompiler6loaderEv')
    return QScxmlCompiler.Loader._cuteAt(address)

  def errors(self) -> QList[QScxmlError]:
    """
    Calls Qt's 'QList<QScxmlError> QScxmlCompiler::errors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcompiler.html#errors

    Returns
    -------

    QList[QScxmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScxmlError> QScxmlCompiler::errors() const
    address = self.uglySide.call('ritual_ZNK14QScxmlCompiler6errorsEv')
    from . import QScxmlError
    return QList[QScxmlError]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QScxmlCompiler::setFileName(const QString &fileName)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcompiler.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlCompiler::setFileName(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN14QScxmlCompiler11setFileNameERK7QString', fileName,
    )

  @overload(Loader)
  @overload(NoneType)
  def setLoader(self, newLoader: Optional[Loader]) -> None:
    """
    Calls Qt's 'void QScxmlCompiler::setLoader(Loader *newLoader)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcompiler.html#setLoader

    Parameters
    ----------

    newLoader : Optional[Loader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlCompiler::setLoader(Loader *newLoader)
    self.uglySide.call(
        'ritual_ZN14QScxmlCompiler9setLoaderEPNS_6LoaderE',
        self._addressOf(newLoader),
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

  @overload(QXmlStreamReader)
  @overload(NoneType)
  def __init__(self, xmlReader: Optional[QXmlStreamReader]) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlCompiler::QScxmlCompiler(QXmlStreamReader *xmlReader)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcompiler.html#QScxmlCompiler

    Parameters
    ----------

    xmlReader : Optional[QXmlStreamReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QScxmlCompiler::QScxmlCompiler(QXmlStreamReader *xmlReader)
    self._noteCreation(QScxmlCompiler, lambda: Rituals.call(
        'ritual_ZN14QScxmlCompilerC1EP16QXmlStreamReader',
        self._addressOf(xmlReader),
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

  def compile(self) -> Optional[QScxmlStateMachine]:
    """
    Calls Qt's 'QScxmlStateMachine *QScxmlCompiler::compile()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcompiler.html#compile

    Returns
    -------

    Optional[QScxmlStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachine *QScxmlCompiler::compile()
    address = self.uglySide.call('ritual_ZN14QScxmlCompiler7compileEv')
    from . import QScxmlStateMachine
    return QScxmlStateMachine._cuteAt(address)
