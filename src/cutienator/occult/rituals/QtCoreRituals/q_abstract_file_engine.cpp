//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractfileengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QAbstractFileEngine that Python can take functions over in. Every QAbstractFileEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQAbstractFileEngineCall0)(const void *, int *);
typedef bool (*CuteQAbstractFileEngineCall1)(const void *, int *);
typedef bool (*CuteQAbstractFileEngineCall2)(const void *, int *);
typedef qint64 (*CuteQAbstractFileEngineCall3)(const void *, int *);
typedef qint64 (*CuteQAbstractFileEngineCall4)(const void *, int *);
typedef bool (*CuteQAbstractFileEngineCall5)(const void *, qint64, int *);
typedef bool (*CuteQAbstractFileEngineCall6)(const void *, int *);
typedef bool (*CuteQAbstractFileEngineCall7)(const void *, int *);
typedef bool (*CuteQAbstractFileEngineCall8)(const void *, const QString *, int *);
typedef bool (*CuteQAbstractFileEngineCall9)(const void *, const QString *, int *);
typedef bool (*CuteQAbstractFileEngineCall10)(const void *, const QString *, int *);
typedef bool (*CuteQAbstractFileEngineCall11)(const void *, const QString *, int *);
typedef bool (*CuteQAbstractFileEngineCall12)(const void *, const QString *, bool, int *);
typedef bool (*CuteQAbstractFileEngineCall13)(const void *, qint64, int *);
typedef bool (*CuteQAbstractFileEngineCall14)(const void *, int *);
typedef bool (*CuteQAbstractFileEngineCall15)(const void *, int *);
typedef int (*CuteQAbstractFileEngineCall16)(const void *, int, int *);
typedef bool (*CuteQAbstractFileEngineCall17)(const void *, uint, int *);
typedef const QByteArray * (*CuteQAbstractFileEngineCall18)(const void *, int *);
typedef QString * (*CuteQAbstractFileEngineCall19)(const void *, int, int *);
typedef uint (*CuteQAbstractFileEngineCall20)(const void *, int, int *);
typedef QString * (*CuteQAbstractFileEngineCall21)(const void *, int, int *);
typedef void (*CuteQAbstractFileEngineCall22)(const void *, const QString *, int *);
typedef int (*CuteQAbstractFileEngineCall23)(const void *, int *);
typedef int (*CuteQAbstractFileEngineCall24)(const void *, QAbstractFileEngine *, int *);
typedef bool (*CuteQAbstractFileEngineCall25)(const void *, int, const QAbstractFileEngine::ExtensionOption *, QAbstractFileEngine::ExtensionReturn *, int *);
typedef bool (*CuteQAbstractFileEngineCall26)(const void *, int, int *);
class CuteQAbstractFileEngine : public QAbstractFileEngine {
public:
  using QAbstractFileEngine::QAbstractFileEngine;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine5closeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine5flushEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine10syncToDiskEv")) {
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
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4seekEx")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine12isSequentialEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine6removeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4copyERK7QString")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine6renameERK7QString")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine15renameOverwriteERK7QString")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4linkERK7QString")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine5rmdirERK7QStringb")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine7setSizeEx")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine13caseSensitiveEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine14isRelativePathEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine9fileFlagsE6QFlagsINS_8FileFlagEE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine14setPermissionsEj")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine2idEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine8fileNameENS_8FileNameE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine7ownerIdENS_9FileOwnerE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine5ownerENS_9FileOwnerE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine11setFileNameERK7QString")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine6handleEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine7cloneToEPS_")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine9extensionENS_9ExtensionEPKNS_15ExtensionOptionEPNS_15ExtensionReturnE")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine17supportsExtensionENS_9ExtensionE")) {
      taken[26] = call;
      return true;
    }
    return false;
  }

  //  bool QAbstractFileEngine::close()
  bool close() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractFileEngineCall0 call = reinterpret_cast<CuteQAbstractFileEngineCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::close();
  }

  //  bool QAbstractFileEngine::flush()
  bool flush() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractFileEngineCall1 call = reinterpret_cast<CuteQAbstractFileEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::flush();
  }

  //  bool QAbstractFileEngine::syncToDisk()
  bool syncToDisk() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractFileEngineCall2 call = reinterpret_cast<CuteQAbstractFileEngineCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::syncToDisk();
  }

  //  qint64 QAbstractFileEngine::size() const
  qint64 size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractFileEngineCall3 call = reinterpret_cast<CuteQAbstractFileEngineCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::size();
  }

  //  qint64 QAbstractFileEngine::pos() const
  qint64 pos() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractFileEngineCall4 call = reinterpret_cast<CuteQAbstractFileEngineCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::pos();
  }

  //  bool QAbstractFileEngine::seek(qint64 pos)
  bool seek(qint64 pos) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractFileEngineCall5 call = reinterpret_cast<CuteQAbstractFileEngineCall5>(taken[5]);
      bool given = call(this, pos, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::seek(pos);
  }

  //  bool QAbstractFileEngine::isSequential() const
  bool isSequential() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractFileEngineCall6 call = reinterpret_cast<CuteQAbstractFileEngineCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::isSequential();
  }

  //  bool QAbstractFileEngine::remove()
  bool remove() override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractFileEngineCall7 call = reinterpret_cast<CuteQAbstractFileEngineCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::remove();
  }

  //  bool QAbstractFileEngine::copy(const QString &newName)
  bool copy(const QString &newName) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractFileEngineCall8 call = reinterpret_cast<CuteQAbstractFileEngineCall8>(taken[8]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::copy(newName);
  }

  //  bool QAbstractFileEngine::rename(const QString &newName)
  bool rename(const QString &newName) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractFileEngineCall9 call = reinterpret_cast<CuteQAbstractFileEngineCall9>(taken[9]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::rename(newName);
  }

  //  bool QAbstractFileEngine::renameOverwrite(const QString &newName)
  bool renameOverwrite(const QString &newName) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractFileEngineCall10 call = reinterpret_cast<CuteQAbstractFileEngineCall10>(taken[10]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::renameOverwrite(newName);
  }

  //  bool QAbstractFileEngine::link(const QString &newName)
  bool link(const QString &newName) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractFileEngineCall11 call = reinterpret_cast<CuteQAbstractFileEngineCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractFileEngineCall12 call = reinterpret_cast<CuteQAbstractFileEngineCall12>(taken[12]);
      bool given = call(this, &dirName, recurseParentDirectories, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::rmdir(dirName, recurseParentDirectories);
  }

  //  bool QAbstractFileEngine::setSize(qint64 size)
  bool setSize(qint64 size) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractFileEngineCall13 call = reinterpret_cast<CuteQAbstractFileEngineCall13>(taken[13]);
      bool given = call(this, size, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::setSize(size);
  }

  //  bool QAbstractFileEngine::caseSensitive() const
  bool caseSensitive() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractFileEngineCall14 call = reinterpret_cast<CuteQAbstractFileEngineCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::caseSensitive();
  }

  //  bool QAbstractFileEngine::isRelativePath() const
  bool isRelativePath() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractFileEngineCall15 call = reinterpret_cast<CuteQAbstractFileEngineCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::isRelativePath();
  }

  //  FileFlags QAbstractFileEngine::fileFlags(FileFlags type) const
  QAbstractFileEngine::FileFlags fileFlags(
      QAbstractFileEngine::FileFlags type) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractFileEngineCall16 call = reinterpret_cast<CuteQAbstractFileEngineCall16>(taken[16]);
      int given = call(this, static_cast<int>(type.toInt()), &handled);
      if (handled) return QFlags<QAbstractFileEngine::FileFlag>::fromInt(given);
    }
    return QAbstractFileEngine::fileFlags(type);
  }

  //  bool QAbstractFileEngine::setPermissions(uint perms)
  bool setPermissions(uint perms) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractFileEngineCall17 call = reinterpret_cast<CuteQAbstractFileEngineCall17>(taken[17]);
      bool given = call(this, perms, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::setPermissions(perms);
  }

  //  QByteArray QAbstractFileEngine::id() const
  QByteArray id() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractFileEngineCall18 call = reinterpret_cast<CuteQAbstractFileEngineCall18>(taken[18]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractFileEngine::id();
  }

  //  QString QAbstractFileEngine::fileName(FileName file) const
  QString fileName(QAbstractFileEngine::FileName file) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractFileEngineCall19 call = reinterpret_cast<CuteQAbstractFileEngineCall19>(taken[19]);
      QString * given = call(this, static_cast<int>(file), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAbstractFileEngine::fileName(file);
  }

  //  uint QAbstractFileEngine::ownerId(FileOwner a0) const
  uint ownerId(QAbstractFileEngine::FileOwner a0) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractFileEngineCall20 call = reinterpret_cast<CuteQAbstractFileEngineCall20>(taken[20]);
      uint given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::ownerId(a0);
  }

  //  QString QAbstractFileEngine::owner(FileOwner a0) const
  QString owner(QAbstractFileEngine::FileOwner a0) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractFileEngineCall21 call = reinterpret_cast<CuteQAbstractFileEngineCall21>(taken[21]);
      QString * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAbstractFileEngine::owner(a0);
  }

  //  void QAbstractFileEngine::setFileName(const QString &file)
  void setFileName(const QString &file) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractFileEngineCall22 call = reinterpret_cast<CuteQAbstractFileEngineCall22>(taken[22]);
      call(this, &file, &handled);
      if (handled) return;
    }
    QAbstractFileEngine::setFileName(file);
  }

  //  int QAbstractFileEngine::handle() const
  int handle() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractFileEngineCall23 call = reinterpret_cast<CuteQAbstractFileEngineCall23>(taken[23]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::handle();
  }

  //  TriStateResult QAbstractFileEngine::cloneTo(QAbstractFileEngine
  //      *target)
  QAbstractFileEngine::TriStateResult cloneTo(
      QAbstractFileEngine *target) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractFileEngineCall24 call = reinterpret_cast<CuteQAbstractFileEngineCall24>(taken[24]);
      int given = call(this, target, &handled);
      if (handled) return static_cast<QAbstractFileEngine::TriStateResult>(given);
    }
    return QAbstractFileEngine::cloneTo(target);
  }

  //  bool QAbstractFileEngine::extension(Extension extension, const
  //      ExtensionOption *option, ExtensionReturn *output)
  bool extension(
      QAbstractFileEngine::Extension extension,
      const QAbstractFileEngine::ExtensionOption *option,
      QAbstractFileEngine::ExtensionReturn *output) override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractFileEngineCall25 call = reinterpret_cast<CuteQAbstractFileEngineCall25>(taken[25]);
      bool given = call(this, static_cast<int>(extension), option, output, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::extension(extension, option, output);
  }

  //  bool QAbstractFileEngine::supportsExtension(Extension extension)
  //      const
  bool supportsExtension(
      QAbstractFileEngine::Extension extension) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractFileEngineCall26 call = reinterpret_cast<CuteQAbstractFileEngineCall26>(taken[26]);
      bool given = call(this, static_cast<int>(extension), &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::supportsExtension(extension);
  }
};

//  QAbstractFileEngine::~QAbstractFileEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractFileEngineD1Ev(QAbstractFileEngine *self) {
  delete self;
}

//  bool QAbstractFileEngine::close()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine5closeEv(QAbstractFileEngine *self) {
  return self->close();
}

//  bool QAbstractFileEngine::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine5flushEv(QAbstractFileEngine *self) {
  return self->flush();
}

//  bool QAbstractFileEngine::syncToDisk()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine10syncToDiskEv(
    QAbstractFileEngine *self) {
  return self->syncToDisk();
}

//  qint64 QAbstractFileEngine::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QAbstractFileEngine4sizeEv(
    const QAbstractFileEngine *self) {
  return self->size();
}

//  qint64 QAbstractFileEngine::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QAbstractFileEngine3posEv(
    const QAbstractFileEngine *self) {
  return self->pos();
}

//  bool QAbstractFileEngine::seek(qint64 pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine4seekEx(
    QAbstractFileEngine *self,
    qint64 pos) {
  return self->seek(pos);
}

//  bool QAbstractFileEngine::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractFileEngine12isSequentialEv(
    const QAbstractFileEngine *self) {
  return self->isSequential();
}

//  bool QAbstractFileEngine::remove()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine6removeEv(QAbstractFileEngine *self) {
  return self->remove();
}

//  bool QAbstractFileEngine::copy(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine4copyERK7QString(
    QAbstractFileEngine *self,
    const QString *newName) {
  return self->copy(*newName);
}

//  bool QAbstractFileEngine::rename(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine6renameERK7QString(
    QAbstractFileEngine *self,
    const QString *newName) {
  return self->rename(*newName);
}

//  bool QAbstractFileEngine::renameOverwrite(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine15renameOverwriteERK7QString(
    QAbstractFileEngine *self,
    const QString *newName) {
  return self->renameOverwrite(*newName);
}

//  bool QAbstractFileEngine::link(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine4linkERK7QString(
    QAbstractFileEngine *self,
    const QString *newName) {
  return self->link(*newName);
}

//  bool QAbstractFileEngine::rmdir(const QString &dirName, bool
//      recurseParentDirectories) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractFileEngine5rmdirERK7QStringb(
    const QAbstractFileEngine *self,
    const QString *dirName,
    bool recurseParentDirectories) {
  return self->rmdir(*dirName, recurseParentDirectories);
}

//  bool QAbstractFileEngine::setSize(qint64 size)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine7setSizeEx(
    QAbstractFileEngine *self,
    qint64 size) {
  return self->setSize(size);
}

//  bool QAbstractFileEngine::caseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractFileEngine13caseSensitiveEv(
    const QAbstractFileEngine *self) {
  return self->caseSensitive();
}

//  bool QAbstractFileEngine::isRelativePath() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractFileEngine14isRelativePathEv(
    const QAbstractFileEngine *self) {
  return self->isRelativePath();
}

//  FileFlags QAbstractFileEngine::fileFlags(FileFlags type) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAbstractFileEngine9fileFlagsE6QFlagsINS_8FileFlagEE(
    const QAbstractFileEngine *self,
    int type) {
  return static_cast<int>(
      self->fileFlags(
          QFlags<QAbstractFileEngine::FileFlag>::fromInt(type)).toInt());
}

//  bool QAbstractFileEngine::setPermissions(uint perms)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine14setPermissionsEj(
    QAbstractFileEngine *self,
    uint perms) {
  return self->setPermissions(perms);
}

//  QByteArray QAbstractFileEngine::id() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QAbstractFileEngine2idEv(
    const QAbstractFileEngine *self) {
  return new QByteArray(self->id());
}

//  QString QAbstractFileEngine::fileName(FileName file) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QAbstractFileEngine8fileNameENS_8FileNameE(
    const QAbstractFileEngine *self,
    QAbstractFileEngine::FileName file) {
  return new QString(self->fileName(file));
}

//  uint QAbstractFileEngine::ownerId(FileOwner a0) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK19QAbstractFileEngine7ownerIdENS_9FileOwnerE(
    const QAbstractFileEngine *self,
    QAbstractFileEngine::FileOwner a0) {
  return self->ownerId(a0);
}

//  QString QAbstractFileEngine::owner(FileOwner a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QAbstractFileEngine5ownerENS_9FileOwnerE(
    const QAbstractFileEngine *self,
    QAbstractFileEngine::FileOwner a0) {
  return new QString(self->owner(a0));
}

//  void QAbstractFileEngine::setFileName(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractFileEngine11setFileNameERK7QString(
    QAbstractFileEngine *self,
    const QString *file) {
  self->setFileName(*file);
}

//  int QAbstractFileEngine::handle() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAbstractFileEngine6handleEv(
    const QAbstractFileEngine *self) {
  return self->handle();
}

//  TriStateResult QAbstractFileEngine::cloneTo(QAbstractFileEngine *target)
extern "C" Q_DECL_EXPORT
QAbstractFileEngine::TriStateResult ritual_ZN19QAbstractFileEngine7cloneToEPS_(
    QAbstractFileEngine *self,
    QAbstractFileEngine *target) {
  return self->cloneTo(target);
}

//  bool QAbstractFileEngine::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractFileEngine5atEndEv(
    const QAbstractFileEngine *self) {
  return self->atEnd();
}

//  bool QAbstractFileEngine::unmap(uchar *ptr)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine5unmapEPh(
    QAbstractFileEngine *self,
    uchar *ptr) {
  return self->unmap(ptr);
}

//  qint64 QAbstractFileEngine::write(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN19QAbstractFileEngine5writeEPKcx(
    QAbstractFileEngine *self,
    const char *data,
    qint64 len) {
  return self->write(data, len);
}

//  QString QAbstractFileEngine::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QAbstractFileEngine11errorStringEv(
    const QAbstractFileEngine *self) {
  return new QString(self->errorString());
}

//  bool QAbstractFileEngine::extension(Extension extension, const
//      ExtensionOption *option, ExtensionReturn *output)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractFileEngine9extensionENS_9ExtensionEPKNS_15ExtensionOptionEPNS_15ExtensionReturnE(
    QAbstractFileEngine *self,
    QAbstractFileEngine::Extension extension,
    const QAbstractFileEngine::ExtensionOption *option,
    QAbstractFileEngine::ExtensionReturn *output) {
  return self->extension(extension, option, output);
}

//  bool QAbstractFileEngine::supportsExtension(Extension extension) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractFileEngine17supportsExtensionENS_9ExtensionE(
    const QAbstractFileEngine *self,
    QAbstractFileEngine::Extension extension) {
  return self->supportsExtension(extension);
}

//  QAbstractFileEngine::QAbstractFileEngine()
extern "C" Q_DECL_EXPORT
QAbstractFileEngine *ritual_ZN19QAbstractFileEngineC1Ev() {
  return new CuteQAbstractFileEngine();
}

//  QAbstractFileEnginePrivate *QAbstractFileEngine::d_func()
extern "C" Q_DECL_EXPORT
QAbstractFileEnginePrivate *ritual_ZN19QAbstractFileEngine6d_funcEv(
    QAbstractFileEngine *self) {
  return self->d_func();
}

//  const QAbstractFileEnginePrivate *QAbstractFileEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractFileEnginePrivate *ritual_ZNK19QAbstractFileEngine6d_funcEv(
    const QAbstractFileEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractFileEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractFileEngine(
    QAbstractFileEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractFileEngine *>(self)->take(key, call);
}

//  bool QAbstractFileEngine::close()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractFileEngine5closeEv(QAbstractFileEngine *self) {
  return self->QAbstractFileEngine::close();
}

//  bool QAbstractFileEngine::flush()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractFileEngine5flushEv(QAbstractFileEngine *self) {
  return self->QAbstractFileEngine::flush();
}

//  bool QAbstractFileEngine::syncToDisk()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractFileEngine10syncToDiskEv(
    QAbstractFileEngine *self) {
  return self->QAbstractFileEngine::syncToDisk();
}

//  qint64 QAbstractFileEngine::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK19QAbstractFileEngine4sizeEv(
    const QAbstractFileEngine *self) {
  return self->QAbstractFileEngine::size();
}

//  qint64 QAbstractFileEngine::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK19QAbstractFileEngine3posEv(
    const QAbstractFileEngine *self) {
  return self->QAbstractFileEngine::pos();
}

//  bool QAbstractFileEngine::seek(qint64 pos)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractFileEngine4seekEx(
    QAbstractFileEngine *self,
    qint64 pos) {
  return self->QAbstractFileEngine::seek(pos);
}

//  bool QAbstractFileEngine::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QAbstractFileEngine12isSequentialEv(
    const QAbstractFileEngine *self) {
  return self->QAbstractFileEngine::isSequential();
}

//  bool QAbstractFileEngine::remove()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractFileEngine6removeEv(QAbstractFileEngine *self) {
  return self->QAbstractFileEngine::remove();
}

//  bool QAbstractFileEngine::copy(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractFileEngine4copyERK7QString(
    QAbstractFileEngine *self,
    const QString *newName) {
  return self->QAbstractFileEngine::copy(*newName);
}

//  bool QAbstractFileEngine::rename(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractFileEngine6renameERK7QString(
    QAbstractFileEngine *self,
    const QString *newName) {
  return self->QAbstractFileEngine::rename(*newName);
}

//  bool QAbstractFileEngine::renameOverwrite(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractFileEngine15renameOverwriteERK7QString(
    QAbstractFileEngine *self,
    const QString *newName) {
  return self->QAbstractFileEngine::renameOverwrite(*newName);
}

//  bool QAbstractFileEngine::link(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractFileEngine4linkERK7QString(
    QAbstractFileEngine *self,
    const QString *newName) {
  return self->QAbstractFileEngine::link(*newName);
}

//  bool QAbstractFileEngine::rmdir(const QString &dirName, bool
//      recurseParentDirectories) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QAbstractFileEngine5rmdirERK7QStringb(
    const QAbstractFileEngine *self,
    const QString *dirName,
    bool recurseParentDirectories) {
  return self->QAbstractFileEngine::rmdir(
      *dirName,
      recurseParentDirectories);
}

//  bool QAbstractFileEngine::setSize(qint64 size)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractFileEngine7setSizeEx(
    QAbstractFileEngine *self,
    qint64 size) {
  return self->QAbstractFileEngine::setSize(size);
}

//  bool QAbstractFileEngine::caseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QAbstractFileEngine13caseSensitiveEv(
    const QAbstractFileEngine *self) {
  return self->QAbstractFileEngine::caseSensitive();
}

//  bool QAbstractFileEngine::isRelativePath() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QAbstractFileEngine14isRelativePathEv(
    const QAbstractFileEngine *self) {
  return self->QAbstractFileEngine::isRelativePath();
}

//  FileFlags QAbstractFileEngine::fileFlags(FileFlags type) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAbstractFileEngine9fileFlagsE6QFlagsINS_8FileFlagEE(
    const QAbstractFileEngine *self,
    int type) {
  return static_cast<int>(
      self->QAbstractFileEngine::fileFlags(
          QFlags<QAbstractFileEngine::FileFlag>::fromInt(type)).toInt());
}

//  bool QAbstractFileEngine::setPermissions(uint perms)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractFileEngine14setPermissionsEj(
    QAbstractFileEngine *self,
    uint perms) {
  return self->QAbstractFileEngine::setPermissions(perms);
}

//  QByteArray QAbstractFileEngine::id() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK19QAbstractFileEngine2idEv(
    const QAbstractFileEngine *self) {
  return new QByteArray(self->QAbstractFileEngine::id());
}

//  QString QAbstractFileEngine::fileName(FileName file) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QAbstractFileEngine8fileNameENS_8FileNameE(
    const QAbstractFileEngine *self,
    QAbstractFileEngine::FileName file) {
  return new QString(self->QAbstractFileEngine::fileName(file));
}

//  uint QAbstractFileEngine::ownerId(FileOwner a0) const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK19QAbstractFileEngine7ownerIdENS_9FileOwnerE(
    const QAbstractFileEngine *self,
    QAbstractFileEngine::FileOwner a0) {
  return self->QAbstractFileEngine::ownerId(a0);
}

//  QString QAbstractFileEngine::owner(FileOwner a0) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QAbstractFileEngine5ownerENS_9FileOwnerE(
    const QAbstractFileEngine *self,
    QAbstractFileEngine::FileOwner a0) {
  return new QString(self->QAbstractFileEngine::owner(a0));
}

//  void QAbstractFileEngine::setFileName(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QAbstractFileEngine11setFileNameERK7QString(
    QAbstractFileEngine *self,
    const QString *file) {
  self->QAbstractFileEngine::setFileName(*file);
}

//  int QAbstractFileEngine::handle() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QAbstractFileEngine6handleEv(
    const QAbstractFileEngine *self) {
  return self->QAbstractFileEngine::handle();
}

//  TriStateResult QAbstractFileEngine::cloneTo(QAbstractFileEngine *target)
extern "C" Q_DECL_EXPORT
QAbstractFileEngine::TriStateResult ritual_own_ZN19QAbstractFileEngine7cloneToEPS_(
    QAbstractFileEngine *self,
    QAbstractFileEngine *target) {
  return self->QAbstractFileEngine::cloneTo(target);
}

//  bool QAbstractFileEngine::extension(Extension extension, const
//      ExtensionOption *option, ExtensionReturn *output)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAbstractFileEngine9extensionENS_9ExtensionEPKNS_15ExtensionOptionEPNS_15ExtensionReturnE(
    QAbstractFileEngine *self,
    QAbstractFileEngine::Extension extension,
    const QAbstractFileEngine::ExtensionOption *option,
    QAbstractFileEngine::ExtensionReturn *output) {
  return self->QAbstractFileEngine::extension(extension, option, output);
}

//  bool QAbstractFileEngine::supportsExtension(Extension extension) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QAbstractFileEngine17supportsExtensionENS_9ExtensionE(
    const QAbstractFileEngine *self,
    QAbstractFileEngine::Extension extension) {
  return self->QAbstractFileEngine::supportsExtension(extension);
}
