//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfsfileengine_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(QT_NO_FSFILEENGINE)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfsfileengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QFlags>
#include <QtCore/QIODeviceBase>
#include <optional>
#include <QtCore/QFile>
#include <QtCore/QString>
#include <QtCore/QDateTime>
#include <QtCore/QDirListing>
#include <QtCore/QList>

//  A QFSFileEngine that Python can take functions over in. Every QFSFileEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall0)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall1)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall2)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef qint64 (*CuteQFSFileEngineCall3)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef qint64 (*CuteQFSFileEngineCall4)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall5)(const void *, qint64, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall6)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall7)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall8)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall9)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall10)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall11)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall12)(const void *, const QString *, bool, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall13)(const void *, qint64, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall14)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall15)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef int (*CuteQFSFileEngineCall16)(const void *, int, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall17)(const void *, uint, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef const QByteArray * (*CuteQFSFileEngineCall18)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef QString * (*CuteQFSFileEngineCall19)(const void *, int, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef uint (*CuteQFSFileEngineCall20)(const void *, int, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef QString * (*CuteQFSFileEngineCall21)(const void *, int, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef void (*CuteQFSFileEngineCall22)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef int (*CuteQFSFileEngineCall23)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef qint64 (*CuteQFSFileEngineCall24)(const void *, char *, qint64, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef qint64 (*CuteQFSFileEngineCall25)(const void *, char *, qint64, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef int (*CuteQFSFileEngineCall26)(const void *, QAbstractFileEngine *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall27)(const void *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall28)(const void *, int, const QAbstractFileEngine::ExtensionOption *, QAbstractFileEngine::ExtensionReturn *, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
typedef bool (*CuteQFSFileEngineCall29)(const void *, int, int *);
#endif  // !defined(QT_NO_FSFILEENGINE)
class CuteQFSFileEngine : public QFSFileEngine {
public:
  using QFSFileEngine::QFSFileEngine;
  void *taken[30] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine5closeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine5flushEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine10syncToDiskEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine4sizeEv")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine3posEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4seekEx")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine12isSequentialEv")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine6removeEv")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4copyERK7QString")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine6renameERK7QString")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine15renameOverwriteERK7QString")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4linkERK7QString")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine5rmdirERK7QStringb")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine7setSizeEx")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine13caseSensitiveEv")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine14isRelativePathEv")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine9fileFlagsE6QFlagsINS_8FileFlagEE")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine14setPermissionsEj")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine2idEv")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine8fileNameENS_8FileNameE")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine7ownerIdENS_9FileOwnerE")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine5ownerENS_9FileOwnerE")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine11setFileNameERK7QString")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine6handleEv")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4readEPcx")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine8readLineEPcx")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine7cloneToEPS_")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK13QFSFileEngine13isUnnamedFileEv")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine9extensionENS_9ExtensionEPKNS_15ExtensionOptionEPNS_15ExtensionReturnE")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
#if !defined(QT_NO_FSFILEENGINE)
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine17supportsExtensionENS_9ExtensionE")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_FSFILEENGINE)
    return false;
  }

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::close()
  bool close() override {
    if (taken[0]) {
      int handled = 0;
      CuteQFSFileEngineCall0 call = reinterpret_cast<CuteQFSFileEngineCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::close();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::flush()
  bool flush() override {
    if (taken[1]) {
      int handled = 0;
      CuteQFSFileEngineCall1 call = reinterpret_cast<CuteQFSFileEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::flush();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::syncToDisk()
  bool syncToDisk() override {
    if (taken[2]) {
      int handled = 0;
      CuteQFSFileEngineCall2 call = reinterpret_cast<CuteQFSFileEngineCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::syncToDisk();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  qint64 QFSFileEngine::size() const
  qint64 size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQFSFileEngineCall3 call = reinterpret_cast<CuteQFSFileEngineCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::size();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  qint64 QFSFileEngine::pos() const
  qint64 pos() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQFSFileEngineCall4 call = reinterpret_cast<CuteQFSFileEngineCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::pos();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::seek(qint64 a0)
  bool seek(qint64 a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFSFileEngineCall5 call = reinterpret_cast<CuteQFSFileEngineCall5>(taken[5]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::seek(a0);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::isSequential() const
  bool isSequential() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFSFileEngineCall6 call = reinterpret_cast<CuteQFSFileEngineCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::isSequential();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::remove()
  bool remove() override {
    if (taken[7]) {
      int handled = 0;
      CuteQFSFileEngineCall7 call = reinterpret_cast<CuteQFSFileEngineCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::remove();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::copy(const QString &newName)
  bool copy(const QString &newName) override {
    if (taken[8]) {
      int handled = 0;
      CuteQFSFileEngineCall8 call = reinterpret_cast<CuteQFSFileEngineCall8>(taken[8]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::copy(newName);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::rename(const QString &newName)
  bool rename(const QString &newName) override {
    if (taken[9]) {
      int handled = 0;
      CuteQFSFileEngineCall9 call = reinterpret_cast<CuteQFSFileEngineCall9>(taken[9]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::rename(newName);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::renameOverwrite(const QString &newName)
  bool renameOverwrite(const QString &newName) override {
    if (taken[10]) {
      int handled = 0;
      CuteQFSFileEngineCall10 call = reinterpret_cast<CuteQFSFileEngineCall10>(taken[10]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::renameOverwrite(newName);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::link(const QString &newName)
  bool link(const QString &newName) override {
    if (taken[11]) {
      int handled = 0;
      CuteQFSFileEngineCall11 call = reinterpret_cast<CuteQFSFileEngineCall11>(taken[11]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::link(newName);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::rmdir(const QString &dirName, bool
  //      recurseParentDirectories) const
  bool rmdir(
      const QString &dirName,
      bool recurseParentDirectories) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQFSFileEngineCall12 call = reinterpret_cast<CuteQFSFileEngineCall12>(taken[12]);
      bool given = call(this, &dirName, recurseParentDirectories, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::rmdir(dirName, recurseParentDirectories);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::setSize(qint64 size)
  bool setSize(qint64 size) override {
    if (taken[13]) {
      int handled = 0;
      CuteQFSFileEngineCall13 call = reinterpret_cast<CuteQFSFileEngineCall13>(taken[13]);
      bool given = call(this, size, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::setSize(size);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::caseSensitive() const
  bool caseSensitive() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQFSFileEngineCall14 call = reinterpret_cast<CuteQFSFileEngineCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::caseSensitive();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::isRelativePath() const
  bool isRelativePath() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQFSFileEngineCall15 call = reinterpret_cast<CuteQFSFileEngineCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::isRelativePath();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  FileFlags QFSFileEngine::fileFlags(FileFlags type) const
  QAbstractFileEngine::FileFlags fileFlags(
      QAbstractFileEngine::FileFlags type) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQFSFileEngineCall16 call = reinterpret_cast<CuteQFSFileEngineCall16>(taken[16]);
      int given = call(this, static_cast<int>(type.toInt()), &handled);
      if (handled) return QFlags<QAbstractFileEngine::FileFlag>::fromInt(given);
    }
    return QFSFileEngine::fileFlags(type);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::setPermissions(uint perms)
  bool setPermissions(uint perms) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFSFileEngineCall17 call = reinterpret_cast<CuteQFSFileEngineCall17>(taken[17]);
      bool given = call(this, perms, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::setPermissions(perms);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  QByteArray QFSFileEngine::id() const
  QByteArray id() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQFSFileEngineCall18 call = reinterpret_cast<CuteQFSFileEngineCall18>(taken[18]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QFSFileEngine::id();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  QString QFSFileEngine::fileName(FileName file) const
  QString fileName(QAbstractFileEngine::FileName file) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQFSFileEngineCall19 call = reinterpret_cast<CuteQFSFileEngineCall19>(taken[19]);
      QString * given = call(this, static_cast<int>(file), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFSFileEngine::fileName(file);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  uint QFSFileEngine::ownerId(FileOwner a0) const
  uint ownerId(QAbstractFileEngine::FileOwner a0) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQFSFileEngineCall20 call = reinterpret_cast<CuteQFSFileEngineCall20>(taken[20]);
      uint given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QFSFileEngine::ownerId(a0);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  QString QFSFileEngine::owner(FileOwner a0) const
  QString owner(QAbstractFileEngine::FileOwner a0) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQFSFileEngineCall21 call = reinterpret_cast<CuteQFSFileEngineCall21>(taken[21]);
      QString * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFSFileEngine::owner(a0);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  void QFSFileEngine::setFileName(const QString &file)
  void setFileName(const QString &file) override {
    if (taken[22]) {
      int handled = 0;
      CuteQFSFileEngineCall22 call = reinterpret_cast<CuteQFSFileEngineCall22>(taken[22]);
      call(this, &file, &handled);
      if (handled) return;
    }
    QFSFileEngine::setFileName(file);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  int QFSFileEngine::handle() const
  int handle() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQFSFileEngineCall23 call = reinterpret_cast<CuteQFSFileEngineCall23>(taken[23]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::handle();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  qint64 QFSFileEngine::read(char *data, qint64 maxlen)
  qint64 read(char *data, qint64 maxlen) override {
    if (taken[24]) {
      int handled = 0;
      CuteQFSFileEngineCall24 call = reinterpret_cast<CuteQFSFileEngineCall24>(taken[24]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::read(data, maxlen);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  qint64 QFSFileEngine::readLine(char *data, qint64 maxlen)
  qint64 readLine(char *data, qint64 maxlen) override {
    if (taken[25]) {
      int handled = 0;
      CuteQFSFileEngineCall25 call = reinterpret_cast<CuteQFSFileEngineCall25>(taken[25]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::readLine(data, maxlen);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  TriStateResult QFSFileEngine::cloneTo(QAbstractFileEngine *target)
  QAbstractFileEngine::TriStateResult cloneTo(
      QAbstractFileEngine *target) override {
    if (taken[26]) {
      int handled = 0;
      CuteQFSFileEngineCall26 call = reinterpret_cast<CuteQFSFileEngineCall26>(taken[26]);
      int given = call(this, target, &handled);
      if (handled) return static_cast<QAbstractFileEngine::TriStateResult>(given);
    }
    return QFSFileEngine::cloneTo(target);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::isUnnamedFile() const
  bool isUnnamedFile() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQFSFileEngineCall27 call = reinterpret_cast<CuteQFSFileEngineCall27>(taken[27]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::isUnnamedFile();
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::extension(Extension extension, const
  //      ExtensionOption *option, ExtensionReturn *output)
  bool extension(
      QAbstractFileEngine::Extension extension,
      const QAbstractFileEngine::ExtensionOption *option,
      QAbstractFileEngine::ExtensionReturn *output) override {
    if (taken[28]) {
      int handled = 0;
      CuteQFSFileEngineCall28 call = reinterpret_cast<CuteQFSFileEngineCall28>(taken[28]);
      bool given = call(this, static_cast<int>(extension), option, output, &handled);
      if (handled) return given;
    }
    return QFSFileEngine::extension(extension, option, output);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
  //  bool QFSFileEngine::supportsExtension(Extension extension) const
  bool supportsExtension(
      QAbstractFileEngine::Extension extension) const override {
    if (taken[29]) {
      int handled = 0;
      CuteQFSFileEngineCall29 call = reinterpret_cast<CuteQFSFileEngineCall29>(taken[29]);
      bool given = call(this, static_cast<int>(extension), &handled);
      if (handled) return given;
    }
    return QFSFileEngine::supportsExtension(extension);
  }
#endif  // !defined(QT_NO_FSFILEENGINE)
};

//  QFSFileEnginePrivate *QFSFileEngine::d_func()
extern "C" Q_DECL_EXPORT
QFSFileEnginePrivate *ritual_ZN13QFSFileEngine6d_funcEv(
    QFSFileEngine *self) {
  return self->d_func();
}

//  const QFSFileEnginePrivate *QFSFileEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QFSFileEnginePrivate *ritual_ZNK13QFSFileEngine6d_funcEv(
    const QFSFileEngine *self) {
  return self->d_func();
}

//  QFSFileEngine::QFSFileEngine()
extern "C" Q_DECL_EXPORT
QFSFileEngine *ritual_ZN13QFSFileEngineC1Ev() {
  return new CuteQFSFileEngine();
}

//  QFSFileEngine::QFSFileEngine(const QString &file)
extern "C" Q_DECL_EXPORT
QFSFileEngine *ritual_ZN13QFSFileEngineC1ERK7QString(const QString *file) {
  return new CuteQFSFileEngine(*file);
}

//  QFSFileEngine::~QFSFileEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFSFileEngineD1Ev(QFSFileEngine *self) {
  delete self;
}

//  bool QFSFileEngine::open(QIODevice::OpenMode openMode,
//      std::optional<QFile::Permissions> permissions)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEESt8optionalIS0_IN11QFileDevice10PermissionEEE(
    QFSFileEngine *self,
    int openMode,
    const std::optional<QFile::Permissions> *permissions) {
  return self->open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode),
      *permissions);
}

//  bool QFSFileEngine::close()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine5closeEv(QFSFileEngine *self) {
  return self->close();
}

//  bool QFSFileEngine::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine5flushEv(QFSFileEngine *self) {
  return self->flush();
}

//  bool QFSFileEngine::syncToDisk()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine10syncToDiskEv(QFSFileEngine *self) {
  return self->syncToDisk();
}

//  qint64 QFSFileEngine::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QFSFileEngine4sizeEv(const QFSFileEngine *self) {
  return self->size();
}

//  qint64 QFSFileEngine::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QFSFileEngine3posEv(const QFSFileEngine *self) {
  return self->pos();
}

//  bool QFSFileEngine::seek(qint64 a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine4seekEx(QFSFileEngine *self, qint64 a0) {
  return self->seek(a0);
}

//  bool QFSFileEngine::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFSFileEngine12isSequentialEv(const QFSFileEngine *self) {
  return self->isSequential();
}

//  bool QFSFileEngine::remove()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine6removeEv(QFSFileEngine *self) {
  return self->remove();
}

//  bool QFSFileEngine::copy(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine4copyERK7QString(
    QFSFileEngine *self,
    const QString *newName) {
  return self->copy(*newName);
}

//  bool QFSFileEngine::rename(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine6renameERK7QString(
    QFSFileEngine *self,
    const QString *newName) {
  return self->rename(*newName);
}

//  bool QFSFileEngine::renameOverwrite(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine15renameOverwriteERK7QString(
    QFSFileEngine *self,
    const QString *newName) {
  return self->renameOverwrite(*newName);
}

//  bool QFSFileEngine::link(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine4linkERK7QString(
    QFSFileEngine *self,
    const QString *newName) {
  return self->link(*newName);
}

//  bool QFSFileEngine::mkdir(const QString &dirName, bool
//      createParentDirectories, std::optional<QFile::Permissions>
//      permissions) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFSFileEngine5mkdirERK7QStringbSt8optionalI6QFlagsIN11QFileDevice10PermissionEEE(
    const QFSFileEngine *self,
    const QString *dirName,
    bool createParentDirectories,
    const std::optional<QFile::Permissions> *permissions) {
  return self->mkdir(*dirName, createParentDirectories, *permissions);
}

//  bool QFSFileEngine::rmdir(const QString &dirName, bool
//      recurseParentDirectories) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFSFileEngine5rmdirERK7QStringb(
    const QFSFileEngine *self,
    const QString *dirName,
    bool recurseParentDirectories) {
  return self->rmdir(*dirName, recurseParentDirectories);
}

//  bool QFSFileEngine::setSize(qint64 size)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine7setSizeEx(QFSFileEngine *self, qint64 size) {
  return self->setSize(size);
}

//  bool QFSFileEngine::caseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFSFileEngine13caseSensitiveEv(const QFSFileEngine *self) {
  return self->caseSensitive();
}

//  bool QFSFileEngine::isRelativePath() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFSFileEngine14isRelativePathEv(const QFSFileEngine *self) {
  return self->isRelativePath();
}

//  FileFlags QFSFileEngine::fileFlags(FileFlags type) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QFSFileEngine9fileFlagsE6QFlagsIN19QAbstractFileEngine8FileFlagEE(
    const QFSFileEngine *self,
    int type) {
  return static_cast<int>(
      self->fileFlags(
          QFlags<QAbstractFileEngine::FileFlag>::fromInt(type)).toInt());
}

//  bool QFSFileEngine::setPermissions(uint perms)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine14setPermissionsEj(
    QFSFileEngine *self,
    uint perms) {
  return self->setPermissions(perms);
}

//  QByteArray QFSFileEngine::id() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QFSFileEngine2idEv(const QFSFileEngine *self) {
  return new QByteArray(self->id());
}

//  QString QFSFileEngine::fileName(FileName file) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QFSFileEngine8fileNameEN19QAbstractFileEngine8FileNameE(
    const QFSFileEngine *self,
    QAbstractFileEngine::FileName file) {
  return new QString(self->fileName(file));
}

//  uint QFSFileEngine::ownerId(FileOwner a0) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK13QFSFileEngine7ownerIdEN19QAbstractFileEngine9FileOwnerE(
    const QFSFileEngine *self,
    QAbstractFileEngine::FileOwner a0) {
  return self->ownerId(a0);
}

//  QString QFSFileEngine::owner(FileOwner a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QFSFileEngine5ownerEN19QAbstractFileEngine9FileOwnerE(
    const QFSFileEngine *self,
    QAbstractFileEngine::FileOwner a0) {
  return new QString(self->owner(a0));
}

//  bool QFSFileEngine::setFileTime(const QDateTime &newDate, QFile::FileTime
//      time)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine11setFileTimeERK9QDateTimeN11QFileDevice8FileTimeE(
    QFSFileEngine *self,
    const QDateTime *newDate,
    const QFile::FileTime *time) {
  return self->setFileTime(*newDate, *time);
}

//  QDateTime QFSFileEngine::fileTime(QFile::FileTime time) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK13QFSFileEngine8fileTimeEN11QFileDevice8FileTimeE(
    const QFSFileEngine *self,
    const QFile::FileTime *time) {
  return new QDateTime(self->fileTime(*time));
}

//  void QFSFileEngine::setFileName(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFSFileEngine11setFileNameERK7QString(
    QFSFileEngine *self,
    const QString *file) {
  self->setFileName(*file);
}

//  void QFSFileEngine::setFileEntry(QFileSystemEntry &&entry)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QFSFileEngine12setFileEntryEO16QFileSystemEntry(
    QFSFileEngine *self,
    QFileSystemEntry *entry) {
  self->setFileEntry(std::move(*entry));
}

//  int QFSFileEngine::handle() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QFSFileEngine6handleEv(const QFSFileEngine *self) {
  return self->handle();
}

#if !defined(QT_NO_FILESYSTEMITERATOR)
//  IteratorUniquePtr QFSFileEngine::beginEntryList(const QString &path,
//      QDirListing::IteratorFlags filters, const QStringList &filterNames)
extern "C" Q_DECL_EXPORT
QAbstractFileEngine::IteratorUniquePtr *ritual_ZN13QFSFileEngine14beginEntryListERK7QString6QFlagsIN11QDirListing12IteratorFlagEERK5QListIS0_E(
    QFSFileEngine *self,
    const QString *path,
    int filters,
    const QList<QString> *filterNames) {
  return new QAbstractFileEngine::IteratorUniquePtr(
      self->beginEntryList(
          *path,
          QFlags<QDirListing::IteratorFlag>::fromInt(filters),
          *filterNames));
}
#endif  // !defined(QT_NO_FILESYSTEMITERATOR)

//  qint64 QFSFileEngine::read(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN13QFSFileEngine4readEPcx(
    QFSFileEngine *self,
    char *data,
    qint64 maxlen) {
  return self->read(data, maxlen);
}

//  qint64 QFSFileEngine::readLine(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN13QFSFileEngine8readLineEPcx(
    QFSFileEngine *self,
    char *data,
    qint64 maxlen) {
  return self->readLine(data, maxlen);
}

//  qint64 QFSFileEngine::write(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN13QFSFileEngine5writeEPKcx(
    QFSFileEngine *self,
    const char *data,
    qint64 len) {
  return self->write(data, len);
}

//  TriStateResult QFSFileEngine::cloneTo(QAbstractFileEngine *target)
extern "C" Q_DECL_EXPORT
QAbstractFileEngine::TriStateResult ritual_ZN13QFSFileEngine7cloneToEP19QAbstractFileEngine(
    QFSFileEngine *self,
    QAbstractFileEngine *target) {
  return self->cloneTo(target);
}

//  bool QFSFileEngine::isUnnamedFile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFSFileEngine13isUnnamedFileEv(const QFSFileEngine *self) {
  return self->isUnnamedFile();
}

//  bool QFSFileEngine::extension(Extension extension, const ExtensionOption
//      *option, ExtensionReturn *output)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine9extensionEN19QAbstractFileEngine9ExtensionEPKNS0_15ExtensionOptionEPNS0_15ExtensionReturnE(
    QFSFileEngine *self,
    QAbstractFileEngine::Extension extension,
    const QAbstractFileEngine::ExtensionOption *option,
    QAbstractFileEngine::ExtensionReturn *output) {
  return self->extension(extension, option, output);
}

//  bool QFSFileEngine::supportsExtension(Extension extension) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QFSFileEngine17supportsExtensionEN19QAbstractFileEngine9ExtensionE(
    const QFSFileEngine *self,
    QAbstractFileEngine::Extension extension) {
  return self->supportsExtension(extension);
}

//  bool QFSFileEngine::open(QIODevice::OpenMode flags, int fd,
//      QFile::FileHandleFlags handleFlags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEEiS0_IN11QFileDevice14FileHandleFlagEE(
    QFSFileEngine *self,
    int flags,
    int fd,
    int handleFlags) {
  return self->open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags),
      fd,
      QFlags<QFileDevice::FileHandleFlag>::fromInt(handleFlags));
}

//  bool QFSFileEngine::open(QIODevice::OpenMode flags, FILE *fh,
//      QFile::FileHandleFlags handleFlags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEEP8_IO_FILES0_IN11QFileDevice14FileHandleFlagEE(
    QFSFileEngine *self,
    int flags,
    FILE *fh,
    int handleFlags) {
  return self->open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags),
      fh,
      QFlags<QFileDevice::FileHandleFlag>::fromInt(handleFlags));
}

//  bool QFSFileEngine::setCurrentPath(const QString &path)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine14setCurrentPathERK7QString(
    const QString *path) {
  return QFSFileEngine::setCurrentPath(*path);
}

//  QString QFSFileEngine::currentPath(const QString &path)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QFSFileEngine11currentPathERK7QString(
    const QString *path) {
  return new QString(QFSFileEngine::currentPath(*path));
}

//  QFileInfoList QFSFileEngine::drives()
extern "C" Q_DECL_EXPORT
QList<QFileInfo> *ritual_ZN13QFSFileEngine6drivesEv() {
  return new QList<QFileInfo>(QFSFileEngine::drives());
}

//  QFSFileEngine::QFSFileEngine(QFSFileEnginePrivate &dd)
extern "C" Q_DECL_EXPORT
QFSFileEngine *ritual_ZN13QFSFileEngineC1ER20QFSFileEnginePrivate(
    QFSFileEnginePrivate *dd) {
  return new CuteQFSFileEngine(*dd);
}

//  bool QFSFileEngine::rename_helper(const QString &newName, RenameMode
//      mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QFSFileEngine13rename_helperERK7QStringNS_10RenameModeE(
    QFSFileEngine *self,
    const QString *newName,
    QFSFileEngine::RenameMode mode) {
  return self->rename_helper(*newName, mode);
}

//  a Python function taken by a CuteQFSFileEngine, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFSFileEngine(
    QFSFileEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFSFileEngine *>(self)->take(key, call);
}

//  bool QFSFileEngine::close()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFSFileEngine5closeEv(QFSFileEngine *self) {
  return self->QFSFileEngine::close();
}

//  bool QFSFileEngine::flush()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFSFileEngine5flushEv(QFSFileEngine *self) {
  return self->QFSFileEngine::flush();
}

//  bool QFSFileEngine::syncToDisk()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFSFileEngine10syncToDiskEv(QFSFileEngine *self) {
  return self->QFSFileEngine::syncToDisk();
}

//  qint64 QFSFileEngine::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK13QFSFileEngine4sizeEv(const QFSFileEngine *self) {
  return self->QFSFileEngine::size();
}

//  qint64 QFSFileEngine::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK13QFSFileEngine3posEv(const QFSFileEngine *self) {
  return self->QFSFileEngine::pos();
}

//  bool QFSFileEngine::seek(qint64 a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFSFileEngine4seekEx(QFSFileEngine *self, qint64 a0) {
  return self->QFSFileEngine::seek(a0);
}

//  bool QFSFileEngine::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QFSFileEngine12isSequentialEv(
    const QFSFileEngine *self) {
  return self->QFSFileEngine::isSequential();
}

//  bool QFSFileEngine::remove()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFSFileEngine6removeEv(QFSFileEngine *self) {
  return self->QFSFileEngine::remove();
}

//  bool QFSFileEngine::copy(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFSFileEngine4copyERK7QString(
    QFSFileEngine *self,
    const QString *newName) {
  return self->QFSFileEngine::copy(*newName);
}

//  bool QFSFileEngine::rename(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFSFileEngine6renameERK7QString(
    QFSFileEngine *self,
    const QString *newName) {
  return self->QFSFileEngine::rename(*newName);
}

//  bool QFSFileEngine::renameOverwrite(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFSFileEngine15renameOverwriteERK7QString(
    QFSFileEngine *self,
    const QString *newName) {
  return self->QFSFileEngine::renameOverwrite(*newName);
}

//  bool QFSFileEngine::link(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFSFileEngine4linkERK7QString(
    QFSFileEngine *self,
    const QString *newName) {
  return self->QFSFileEngine::link(*newName);
}

//  bool QFSFileEngine::rmdir(const QString &dirName, bool
//      recurseParentDirectories) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QFSFileEngine5rmdirERK7QStringb(
    const QFSFileEngine *self,
    const QString *dirName,
    bool recurseParentDirectories) {
  return self->QFSFileEngine::rmdir(*dirName, recurseParentDirectories);
}

//  bool QFSFileEngine::setSize(qint64 size)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFSFileEngine7setSizeEx(
    QFSFileEngine *self,
    qint64 size) {
  return self->QFSFileEngine::setSize(size);
}

//  bool QFSFileEngine::caseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QFSFileEngine13caseSensitiveEv(
    const QFSFileEngine *self) {
  return self->QFSFileEngine::caseSensitive();
}

//  bool QFSFileEngine::isRelativePath() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QFSFileEngine14isRelativePathEv(
    const QFSFileEngine *self) {
  return self->QFSFileEngine::isRelativePath();
}

//  FileFlags QFSFileEngine::fileFlags(FileFlags type) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QFSFileEngine9fileFlagsE6QFlagsIN19QAbstractFileEngine8FileFlagEE(
    const QFSFileEngine *self,
    int type) {
  return static_cast<int>(
      self->QFSFileEngine::fileFlags(
          QFlags<QAbstractFileEngine::FileFlag>::fromInt(type)).toInt());
}

//  bool QFSFileEngine::setPermissions(uint perms)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFSFileEngine14setPermissionsEj(
    QFSFileEngine *self,
    uint perms) {
  return self->QFSFileEngine::setPermissions(perms);
}

//  QByteArray QFSFileEngine::id() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK13QFSFileEngine2idEv(const QFSFileEngine *self) {
  return new QByteArray(self->QFSFileEngine::id());
}

//  QString QFSFileEngine::fileName(FileName file) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK13QFSFileEngine8fileNameEN19QAbstractFileEngine8FileNameE(
    const QFSFileEngine *self,
    QAbstractFileEngine::FileName file) {
  return new QString(self->QFSFileEngine::fileName(file));
}

//  uint QFSFileEngine::ownerId(FileOwner a0) const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK13QFSFileEngine7ownerIdEN19QAbstractFileEngine9FileOwnerE(
    const QFSFileEngine *self,
    QAbstractFileEngine::FileOwner a0) {
  return self->QFSFileEngine::ownerId(a0);
}

//  QString QFSFileEngine::owner(FileOwner a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK13QFSFileEngine5ownerEN19QAbstractFileEngine9FileOwnerE(
    const QFSFileEngine *self,
    QAbstractFileEngine::FileOwner a0) {
  return new QString(self->QFSFileEngine::owner(a0));
}

//  void QFSFileEngine::setFileName(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QFSFileEngine11setFileNameERK7QString(
    QFSFileEngine *self,
    const QString *file) {
  self->QFSFileEngine::setFileName(*file);
}

//  int QFSFileEngine::handle() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK13QFSFileEngine6handleEv(const QFSFileEngine *self) {
  return self->QFSFileEngine::handle();
}

//  qint64 QFSFileEngine::read(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN13QFSFileEngine4readEPcx(
    QFSFileEngine *self,
    char *data,
    qint64 maxlen) {
  return self->QFSFileEngine::read(data, maxlen);
}

//  qint64 QFSFileEngine::readLine(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN13QFSFileEngine8readLineEPcx(
    QFSFileEngine *self,
    char *data,
    qint64 maxlen) {
  return self->QFSFileEngine::readLine(data, maxlen);
}

//  TriStateResult QFSFileEngine::cloneTo(QAbstractFileEngine *target)
extern "C" Q_DECL_EXPORT
QAbstractFileEngine::TriStateResult ritual_own_ZN13QFSFileEngine7cloneToEP19QAbstractFileEngine(
    QFSFileEngine *self,
    QAbstractFileEngine *target) {
  return self->QFSFileEngine::cloneTo(target);
}

//  bool QFSFileEngine::isUnnamedFile() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QFSFileEngine13isUnnamedFileEv(
    const QFSFileEngine *self) {
  return self->QFSFileEngine::isUnnamedFile();
}

//  bool QFSFileEngine::extension(Extension extension, const ExtensionOption
//      *option, ExtensionReturn *output)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN13QFSFileEngine9extensionEN19QAbstractFileEngine9ExtensionEPKNS0_15ExtensionOptionEPNS0_15ExtensionReturnE(
    QFSFileEngine *self,
    QAbstractFileEngine::Extension extension,
    const QAbstractFileEngine::ExtensionOption *option,
    QAbstractFileEngine::ExtensionReturn *output) {
  return self->QFSFileEngine::extension(extension, option, output);
}

//  bool QFSFileEngine::supportsExtension(Extension extension) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK13QFSFileEngine17supportsExtensionEN19QAbstractFileEngine9ExtensionE(
    const QFSFileEngine *self,
    QAbstractFileEngine::Extension extension) {
  return self->QFSFileEngine::supportsExtension(extension);
}

//  a QAbstractFileEngine::IteratorUniquePtr a ritual of QFSFileEngine gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QFSFileEngine__QAbstractFileEngine_IteratorUniquePtr(
    QAbstractFileEngine::IteratorUniquePtr *self) {
  delete self;
}

#endif  // !defined(QT_NO_FSFILEENGINE)
