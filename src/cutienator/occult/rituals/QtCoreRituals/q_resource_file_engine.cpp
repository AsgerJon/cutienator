//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qresource_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qresource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qresource.h>
#include <QtCore/private/qresource_p.h>
#include <QtCore/private/qresource_iterator_p.h>
#include <QtCore/qset.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlocale.h>
#include <QtCore/qglobal.h>
#include <QtCore/qlist.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qendian.h>
#include <QtCore/qshareddata.h>
#include <qplatformdefs.h>
#include <QtCore/qendian.h>
#include <QtCore/private/qabstractfileengine_p.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/private/qsimd_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtCore/private/qsystemerror_p.h>
#ifndef QT_NO_COMPRESS
#  include <zconf.h>
#  include <zlib.h>
#endif
#if QT_CONFIG(zstd)
#  include <zstd.h>
#endif
#if defined(Q_OS_UNIX) && !defined(Q_OS_INTEGRITY)
#  include <sys/mman.h>
#  ifdef Q_OS_LINUX
#  elif defined(Q_OS_DARWIN)
#    include <mach/mach.h>
#    include <mach/vm_map.h>
#  endif
#endif
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qresource.cpp, line 1455, as _ZN19QResourceFileEngineD1Ev
#if !defined(QT_BOOTSTRAPPED)
inline QResourceFileEngine::~QResourceFileEngine()
{
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1498, as _ZN19QResourceFileEngine5flushEv
#if !defined(QT_BOOTSTRAPPED)
inline bool QResourceFileEngine::flush()
{
    return true;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1443, as _ZNK19QResourceFileEngine13caseSensitiveEv
#if !defined(QT_BOOTSTRAPPED)
inline bool QResourceFileEngine::caseSensitive() const
{
    return true;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1604, as _ZNK19QResourceFileEngine7ownerIdEN19QAbstractFileEngine9FileOwnerE
#if !defined(QT_BOOTSTRAPPED)
inline uint QResourceFileEngine::ownerId(FileOwner) const
{
    static const uint nobodyID = static_cast<uint>(-2);
    return nobodyID;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1644, as _ZNK19QResourceFileEngine17supportsExtensionEN19QAbstractFileEngine9ExtensionE
#if !defined(QT_BOOTSTRAPPED)
inline bool QResourceFileEngine::supportsExtension(Extension extension) const
{
    return (extension == UnMapExtension || extension == MapExtension);
}
#endif  // !defined(QT_BOOTSTRAPPED)
//  -----------------------------------------------------------------------

//  A QResourceFileEngine that Python can take functions over in. Every QResourceFileEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQResourceFileEngineCall0)(const void *, const QString *, int *);
typedef bool (*CuteQResourceFileEngineCall1)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall2)(const void *, int *);
typedef qint64 (*CuteQResourceFileEngineCall3)(const void *, int *);
typedef qint64 (*CuteQResourceFileEngineCall4)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall5)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall6)(const void *, qint64, int *);
typedef bool (*CuteQResourceFileEngineCall7)(const void *, int *);
typedef int (*CuteQResourceFileEngineCall8)(const void *, int, int *);
typedef QString * (*CuteQResourceFileEngineCall9)(const void *, int, int *);
typedef uint (*CuteQResourceFileEngineCall10)(const void *, int, int *);
typedef bool (*CuteQResourceFileEngineCall11)(const void *, int, const QAbstractFileEngine::ExtensionOption *, QAbstractFileEngine::ExtensionReturn *, int *);
typedef bool (*CuteQResourceFileEngineCall12)(const void *, int, int *);
typedef bool (*CuteQResourceFileEngineCall13)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall14)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall15)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall16)(const void *, const QString *, int *);
typedef bool (*CuteQResourceFileEngineCall17)(const void *, const QString *, int *);
typedef bool (*CuteQResourceFileEngineCall18)(const void *, const QString *, int *);
typedef bool (*CuteQResourceFileEngineCall19)(const void *, const QString *, int *);
typedef bool (*CuteQResourceFileEngineCall20)(const void *, const QString *, bool, int *);
typedef bool (*CuteQResourceFileEngineCall21)(const void *, qint64, int *);
typedef bool (*CuteQResourceFileEngineCall22)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall23)(const void *, uint, int *);
typedef const QByteArray * (*CuteQResourceFileEngineCall24)(const void *, int *);
typedef QString * (*CuteQResourceFileEngineCall25)(const void *, int, int *);
typedef int (*CuteQResourceFileEngineCall26)(const void *, int *);
typedef int (*CuteQResourceFileEngineCall27)(const void *, QAbstractFileEngine *, int *);
class CuteQResourceFileEngine : public QResourceFileEngine {
public:
  using QResourceFileEngine::QResourceFileEngine;
  void *taken[28] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine11setFileNameERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine5closeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine5flushEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine4sizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine3posEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine5atEndEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4seekEx")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine13caseSensitiveEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine9fileFlagsE6QFlagsINS_8FileFlagEE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine8fileNameENS_8FileNameE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine7ownerIdENS_9FileOwnerE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine9extensionENS_9ExtensionEPKNS_15ExtensionOptionEPNS_15ExtensionReturnE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine17supportsExtensionENS_9ExtensionE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine10syncToDiskEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine12isSequentialEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine6removeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4copyERK7QString")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine6renameERK7QString")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine15renameOverwriteERK7QString")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4linkERK7QString")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine5rmdirERK7QStringb")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine7setSizeEx")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine14isRelativePathEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine14setPermissionsEj")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine2idEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine5ownerENS_9FileOwnerE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine6handleEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine7cloneToEPS_")) {
      taken[27] = call;
      return true;
    }
    return false;
  }

  //  void QResourceFileEngine::setFileName(const QString &file)
  void setFileName(const QString &file) override {
    if (taken[0]) {
      int handled = 0;
      CuteQResourceFileEngineCall0 call = reinterpret_cast<CuteQResourceFileEngineCall0>(taken[0]);
      call(this, &file, &handled);
      if (handled) return;
    }
    QResourceFileEngine::setFileName(file);
  }

  //  bool QResourceFileEngine::close()
  bool close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQResourceFileEngineCall1 call = reinterpret_cast<CuteQResourceFileEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::close();
  }

  //  bool QResourceFileEngine::flush()
  bool flush() override {
    if (taken[2]) {
      int handled = 0;
      CuteQResourceFileEngineCall2 call = reinterpret_cast<CuteQResourceFileEngineCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::flush();
  }

  //  qint64 QResourceFileEngine::size() const
  qint64 size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQResourceFileEngineCall3 call = reinterpret_cast<CuteQResourceFileEngineCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::size();
  }

  //  qint64 QResourceFileEngine::pos() const
  qint64 pos() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQResourceFileEngineCall4 call = reinterpret_cast<CuteQResourceFileEngineCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::pos();
  }

  //  bool QResourceFileEngine::atEnd() const
  bool atEnd() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQResourceFileEngineCall5 call = reinterpret_cast<CuteQResourceFileEngineCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::atEnd();
  }

  //  bool QResourceFileEngine::seek(qint64 a0)
  bool seek(qint64 a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQResourceFileEngineCall6 call = reinterpret_cast<CuteQResourceFileEngineCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::seek(a0);
  }

  //  bool QResourceFileEngine::caseSensitive() const
  bool caseSensitive() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQResourceFileEngineCall7 call = reinterpret_cast<CuteQResourceFileEngineCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::caseSensitive();
  }

  //  FileFlags QResourceFileEngine::fileFlags(FileFlags type) const
  QAbstractFileEngine::FileFlags fileFlags(
      QAbstractFileEngine::FileFlags type) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQResourceFileEngineCall8 call = reinterpret_cast<CuteQResourceFileEngineCall8>(taken[8]);
      int given = call(this, static_cast<int>(type.toInt()), &handled);
      if (handled) return QFlags<QAbstractFileEngine::FileFlag>::fromInt(given);
    }
    return QResourceFileEngine::fileFlags(type);
  }

  //  QString QResourceFileEngine::fileName(QAbstractFileEngine::FileName
  //      file) const
  QString fileName(QAbstractFileEngine::FileName file) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQResourceFileEngineCall9 call = reinterpret_cast<CuteQResourceFileEngineCall9>(taken[9]);
      QString * given = call(this, static_cast<int>(file), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QResourceFileEngine::fileName(file);
  }

  //  uint QResourceFileEngine::ownerId(FileOwner a0) const
  uint ownerId(QAbstractFileEngine::FileOwner a0) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQResourceFileEngineCall10 call = reinterpret_cast<CuteQResourceFileEngineCall10>(taken[10]);
      uint given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::ownerId(a0);
  }

  //  bool QResourceFileEngine::extension(Extension extension, const
  //      ExtensionOption *option, ExtensionReturn *output)
  bool extension(
      QAbstractFileEngine::Extension extension,
      const QAbstractFileEngine::ExtensionOption *option,
      QAbstractFileEngine::ExtensionReturn *output) override {
    if (taken[11]) {
      int handled = 0;
      CuteQResourceFileEngineCall11 call = reinterpret_cast<CuteQResourceFileEngineCall11>(taken[11]);
      bool given = call(this, static_cast<int>(extension), option, output, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::extension(extension, option, output);
  }

  //  bool QResourceFileEngine::supportsExtension(Extension extension)
  //      const
  bool supportsExtension(
      QAbstractFileEngine::Extension extension) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQResourceFileEngineCall12 call = reinterpret_cast<CuteQResourceFileEngineCall12>(taken[12]);
      bool given = call(this, static_cast<int>(extension), &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::supportsExtension(extension);
  }

  //  bool QAbstractFileEngine::syncToDisk()
  bool syncToDisk() override {
    if (taken[13]) {
      int handled = 0;
      CuteQResourceFileEngineCall13 call = reinterpret_cast<CuteQResourceFileEngineCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::syncToDisk();
  }

  //  bool QAbstractFileEngine::isSequential() const
  bool isSequential() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQResourceFileEngineCall14 call = reinterpret_cast<CuteQResourceFileEngineCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::isSequential();
  }

  //  bool QAbstractFileEngine::remove()
  bool remove() override {
    if (taken[15]) {
      int handled = 0;
      CuteQResourceFileEngineCall15 call = reinterpret_cast<CuteQResourceFileEngineCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::remove();
  }

  //  bool QAbstractFileEngine::copy(const QString &newName)
  bool copy(const QString &newName) override {
    if (taken[16]) {
      int handled = 0;
      CuteQResourceFileEngineCall16 call = reinterpret_cast<CuteQResourceFileEngineCall16>(taken[16]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::copy(newName);
  }

  //  bool QAbstractFileEngine::rename(const QString &newName)
  bool rename(const QString &newName) override {
    if (taken[17]) {
      int handled = 0;
      CuteQResourceFileEngineCall17 call = reinterpret_cast<CuteQResourceFileEngineCall17>(taken[17]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::rename(newName);
  }

  //  bool QAbstractFileEngine::renameOverwrite(const QString &newName)
  bool renameOverwrite(const QString &newName) override {
    if (taken[18]) {
      int handled = 0;
      CuteQResourceFileEngineCall18 call = reinterpret_cast<CuteQResourceFileEngineCall18>(taken[18]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::renameOverwrite(newName);
  }

  //  bool QAbstractFileEngine::link(const QString &newName)
  bool link(const QString &newName) override {
    if (taken[19]) {
      int handled = 0;
      CuteQResourceFileEngineCall19 call = reinterpret_cast<CuteQResourceFileEngineCall19>(taken[19]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::link(newName);
  }

  //  bool QAbstractFileEngine::rmdir(const QString &dirName, bool
  //      recurseParentDirectories) const
  bool rmdir(
      const QString &dirName,
      bool recurseParentDirectories) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQResourceFileEngineCall20 call = reinterpret_cast<CuteQResourceFileEngineCall20>(taken[20]);
      bool given = call(this, &dirName, recurseParentDirectories, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::rmdir(dirName, recurseParentDirectories);
  }

  //  bool QAbstractFileEngine::setSize(qint64 size)
  bool setSize(qint64 size) override {
    if (taken[21]) {
      int handled = 0;
      CuteQResourceFileEngineCall21 call = reinterpret_cast<CuteQResourceFileEngineCall21>(taken[21]);
      bool given = call(this, size, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::setSize(size);
  }

  //  bool QAbstractFileEngine::isRelativePath() const
  bool isRelativePath() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQResourceFileEngineCall22 call = reinterpret_cast<CuteQResourceFileEngineCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::isRelativePath();
  }

  //  bool QAbstractFileEngine::setPermissions(uint perms)
  bool setPermissions(uint perms) override {
    if (taken[23]) {
      int handled = 0;
      CuteQResourceFileEngineCall23 call = reinterpret_cast<CuteQResourceFileEngineCall23>(taken[23]);
      bool given = call(this, perms, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::setPermissions(perms);
  }

  //  QByteArray QAbstractFileEngine::id() const
  QByteArray id() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQResourceFileEngineCall24 call = reinterpret_cast<CuteQResourceFileEngineCall24>(taken[24]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractFileEngine::id();
  }

  //  QString QAbstractFileEngine::owner(FileOwner a0) const
  QString owner(QAbstractFileEngine::FileOwner a0) const override {
    if (taken[25]) {
      int handled = 0;
      CuteQResourceFileEngineCall25 call = reinterpret_cast<CuteQResourceFileEngineCall25>(taken[25]);
      QString * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAbstractFileEngine::owner(a0);
  }

  //  int QAbstractFileEngine::handle() const
  int handle() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQResourceFileEngineCall26 call = reinterpret_cast<CuteQResourceFileEngineCall26>(taken[26]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::handle();
  }

  //  TriStateResult QAbstractFileEngine::cloneTo(QAbstractFileEngine
  //      *target)
  QAbstractFileEngine::TriStateResult cloneTo(
      QAbstractFileEngine *target) override {
    if (taken[27]) {
      int handled = 0;
      CuteQResourceFileEngineCall27 call = reinterpret_cast<CuteQResourceFileEngineCall27>(taken[27]);
      int given = call(this, target, &handled);
      if (handled) return static_cast<QAbstractFileEngine::TriStateResult>(given);
    }
    return QAbstractFileEngine::cloneTo(target);
  }
};

//  QResourceFileEngine::~QResourceFileEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QResourceFileEngineD1Ev(QResourceFileEngine *self) {
  delete self;
}

//  bool QResourceFileEngine::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QResourceFileEngine5flushEv(QResourceFileEngine *self) {
  return self->flush();
}

//  bool QResourceFileEngine::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QResourceFileEngine5atEndEv(
    const QResourceFileEngine *self) {
  return self->atEnd();
}

//  bool QResourceFileEngine::caseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QResourceFileEngine13caseSensitiveEv(
    const QResourceFileEngine *self) {
  return self->caseSensitive();
}

//  uint QResourceFileEngine::ownerId(FileOwner a0) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK19QResourceFileEngine7ownerIdEN19QAbstractFileEngine9FileOwnerE(
    const QResourceFileEngine *self,
    QAbstractFileEngine::FileOwner a0) {
  return self->ownerId(a0);
}

//  bool QResourceFileEngine::supportsExtension(Extension extension) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QResourceFileEngine17supportsExtensionEN19QAbstractFileEngine9ExtensionE(
    const QResourceFileEngine *self,
    QAbstractFileEngine::Extension extension) {
  return self->supportsExtension(extension);
}

//  a Python function taken by a CuteQResourceFileEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QResourceFileEngine(
    QResourceFileEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQResourceFileEngine *>(self)->take(key, call);
}

#if !defined(QT_BOOTSTRAPPED)
//  bool QResourceFileEngine::flush()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QResourceFileEngine5flushEv(QResourceFileEngine *self) {
  return self->QResourceFileEngine::flush();
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  bool QResourceFileEngine::caseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QResourceFileEngine13caseSensitiveEv(
    const QResourceFileEngine *self) {
  return self->QResourceFileEngine::caseSensitive();
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  uint QResourceFileEngine::ownerId(FileOwner a0) const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK19QResourceFileEngine7ownerIdEN19QAbstractFileEngine9FileOwnerE(
    const QResourceFileEngine *self,
    QAbstractFileEngine::FileOwner a0) {
  return self->QResourceFileEngine::ownerId(a0);
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  bool QResourceFileEngine::supportsExtension(Extension extension) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QResourceFileEngine17supportsExtensionEN19QAbstractFileEngine9ExtensionE(
    const QResourceFileEngine *self,
    QAbstractFileEngine::Extension extension) {
  return self->QResourceFileEngine::supportsExtension(extension);
}
#endif  // !defined(QT_BOOTSTRAPPED)
