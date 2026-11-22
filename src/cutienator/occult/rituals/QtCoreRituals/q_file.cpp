//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfile.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qfile.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QFile that Python can take functions over in. Every QFile
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qint64 (*CuteQFileCall0)(const void *, int *);
typedef bool (*CuteQFileCall1)(const void *, qint64, int *);
typedef void (*CuteQFileCall2)(const void *, int *);
typedef bool (*CuteQFileCall3)(const void *, int *);
typedef qint64 (*CuteQFileCall4)(const void *, int *);
typedef bool (*CuteQFileCall5)(const void *, qint64, int *);
typedef bool (*CuteQFileCall6)(const void *, int *);
typedef bool (*CuteQFileCall7)(const void *, int *);
typedef qint64 (*CuteQFileCall8)(const void *, int *);
typedef qint64 (*CuteQFileCall9)(const void *, int *);
typedef bool (*CuteQFileCall10)(const void *, int *);
typedef bool (*CuteQFileCall11)(const void *, int, int *);
typedef bool (*CuteQFileCall12)(const void *, int, int *);
typedef qint64 (*CuteQFileCall13)(const void *, qint64, int *);
typedef bool (*CuteQFileCall14)(const void *, QEvent *, int *);
typedef bool (*CuteQFileCall15)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQFileCall16)(const void *, QTimerEvent *, int *);
typedef void (*CuteQFileCall17)(const void *, QChildEvent *, int *);
typedef void (*CuteQFileCall18)(const void *, QEvent *, int *);
typedef void (*CuteQFileCall19)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQFileCall20)(const void *, const QMetaMethod *, int *);
class CuteQFile : public QFile {
public:
  using QFile::QFile;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFileDevice6resizeEx")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[20] = call;
      return true;
    }
    return false;
  }

  //  qint64 QFile::size() const
  qint64 size() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileCall0 call = reinterpret_cast<CuteQFileCall0>(taken[0]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFile::size();
  }

  //  bool QFile::resize(qint64 sz)
  bool resize(qint64 sz) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFileCall1 call = reinterpret_cast<CuteQFileCall1>(taken[1]);
      bool given = call(this, sz, &handled);
      if (handled) return given;
    }
    return QFile::resize(sz);
  }

  //  void QFileDevice::close()
  void close() override {
    if (taken[2]) {
      int handled = 0;
      CuteQFileCall2 call = reinterpret_cast<CuteQFileCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QFileDevice::close();
  }

  //  bool QFileDevice::isSequential() const
  bool isSequential() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQFileCall3 call = reinterpret_cast<CuteQFileCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::isSequential();
  }

  //  qint64 QFileDevice::pos() const
  qint64 pos() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQFileCall4 call = reinterpret_cast<CuteQFileCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::pos();
  }

  //  bool QFileDevice::seek(qint64 offset)
  bool seek(qint64 offset) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFileCall5 call = reinterpret_cast<CuteQFileCall5>(taken[5]);
      bool given = call(this, offset, &handled);
      if (handled) return given;
    }
    return QFileDevice::seek(offset);
  }

  //  bool QFileDevice::atEnd() const
  bool atEnd() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFileCall6 call = reinterpret_cast<CuteQFileCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[7]) {
      int handled = 0;
      CuteQFileCall7 call = reinterpret_cast<CuteQFileCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFileCall8 call = reinterpret_cast<CuteQFileCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQFileCall9 call = reinterpret_cast<CuteQFileCall9>(taken[9]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFileCall10 call = reinterpret_cast<CuteQFileCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[11]) {
      int handled = 0;
      CuteQFileCall11 call = reinterpret_cast<CuteQFileCall11>(taken[11]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[12]) {
      int handled = 0;
      CuteQFileCall12 call = reinterpret_cast<CuteQFileCall12>(taken[12]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[13]) {
      int handled = 0;
      CuteQFileCall13 call = reinterpret_cast<CuteQFileCall13>(taken[13]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQFileCall14 call = reinterpret_cast<CuteQFileCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQFileCall15 call = reinterpret_cast<CuteQFileCall15>(taken[15]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQFileCall16 call = reinterpret_cast<CuteQFileCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFileCall17 call = reinterpret_cast<CuteQFileCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQFileCall18 call = reinterpret_cast<CuteQFileCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQFileCall19 call = reinterpret_cast<CuteQFileCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[20]) {
      int handled = 0;
      CuteQFileCall20 call = reinterpret_cast<CuteQFileCall20>(taken[20]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QFile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5QFile10metaObjectEv(const QFile *self) {
  return self->metaObject();
}

//  QString QFile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QFile2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QFile::tr(s, c, n));
}

//  QFile::QFile()
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1Ev() {
  return new CuteQFile();
}

//  QFile::QFile(const QString &name)
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1ERK7QString(const QString *name) {
  return new CuteQFile(*name);
}

//  QFile::QFile(QObject *parent)
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1EP7QObject(QObject *parent) {
  return new CuteQFile(parent);
}

//  QFile::QFile(const QString &name, QObject *parent)
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1ERK7QStringP7QObject(
    const QString *name,
    QObject *parent) {
  return new CuteQFile(*name, parent);
}

//  QFile::~QFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFileD1Ev(QFile *self) {
  delete self;
}

//  QString QFile::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QFile8fileNameEv(const QFile *self) {
  return new QString(self->fileName());
}

//  void QFile::setFileName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFile11setFileNameERK7QString(
    QFile *self,
    const QString *name) {
  self->setFileName(*name);
}

//  QByteArray QFile::encodeName(const QString &fileName)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN5QFile10encodeNameERK7QString(const QString *fileName) {
  return new QByteArray(QFile::encodeName(*fileName));
}

//  QString QFile::decodeName(const QByteArray &localFileName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QFile10decodeNameERK10QByteArray(
    const QByteArray *localFileName) {
  return new QString(QFile::decodeName(*localFileName));
}

//  QString QFile::decodeName(const char *localFileName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QFile10decodeNameEPKc(const char *localFileName) {
  return new QString(QFile::decodeName(localFileName));
}

//  bool QFile::exists() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFile6existsEv(const QFile *self) {
  return self->exists();
}

//  bool QFile::exists(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6existsERK7QString(const QString *fileName) {
  return QFile::exists(*fileName);
}

//  QString QFile::symLinkTarget() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QFile13symLinkTargetEv(const QFile *self) {
  return new QString(self->symLinkTarget());
}

//  QString QFile::symLinkTarget(const QString &fileName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QFile13symLinkTargetERK7QString(const QString *fileName) {
  return new QString(QFile::symLinkTarget(*fileName));
}

//  bool QFile::remove()
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6removeEv(QFile *self) {
  return self->remove();
}

//  bool QFile::remove(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6removeERK7QString(const QString *fileName) {
  return QFile::remove(*fileName);
}

//  bool QFile::supportsMoveToTrash()
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile19supportsMoveToTrashEv() {
  return QFile::supportsMoveToTrash();
}

//  bool QFile::moveToTrash()
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile11moveToTrashEv(QFile *self) {
  return self->moveToTrash();
}

//  bool QFile::moveToTrash(const QString &fileName, QString *pathInTrash)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile11moveToTrashERK7QStringPS0_(
    const QString *fileName,
    QString *pathInTrash) {
  return QFile::moveToTrash(*fileName, pathInTrash);
}

//  bool QFile::rename(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6renameERK7QString(QFile *self, const QString *newName) {
  return self->rename(*newName);
}

//  bool QFile::rename(const QString &oldName, const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6renameERK7QStringS2_(
    const QString *oldName,
    const QString *newName) {
  return QFile::rename(*oldName, *newName);
}

//  bool QFile::link(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4linkERK7QString(QFile *self, const QString *newName) {
  return self->link(*newName);
}

//  bool QFile::link(const QString &fileName, const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4linkERK7QStringS2_(
    const QString *fileName,
    const QString *newName) {
  return QFile::link(*fileName, *newName);
}

//  bool QFile::open(OpenMode flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QFile *self,
    int flags) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags));
}

//  bool QFile::open(OpenMode flags, Permissions permissions)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEES0_IN11QFileDevice10PermissionEE(
    QFile *self,
    int flags,
    int permissions) {
  return self->open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags),
      QFlags<QFileDevice::Permission>::fromInt(permissions));
}

//  bool QFile::open(int fd, OpenMode ioFlags, FileHandleFlags handleFlags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4openEi6QFlagsIN13QIODeviceBase12OpenModeFlagEES0_IN11QFileDevice14FileHandleFlagEE(
    QFile *self,
    int fd,
    int ioFlags,
    int handleFlags) {
  return self->open(
      fd,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(ioFlags),
      QFlags<QFileDevice::FileHandleFlag>::fromInt(handleFlags));
}

//  qint64 QFile::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK5QFile4sizeEv(const QFile *self) {
  return self->size();
}

//  bool QFile::resize(qint64 sz)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6resizeEx(QFile *self, qint64 sz) {
  return self->resize(sz);
}

//  bool QFile::resize(const QString &filename, qint64 sz)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6resizeERK7QStringx(const QString *filename, qint64 sz) {
  return QFile::resize(*filename, sz);
}

//  Permissions QFile::permissions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QFile11permissionsEv(const QFile *self) {
  return static_cast<int>(self->permissions().toInt());
}

//  Permissions QFile::permissions(const QString &filename)
extern "C" Q_DECL_EXPORT
int ritual_ZN5QFile11permissionsERK7QString(const QString *filename) {
  return static_cast<int>(QFile::permissions(*filename).toInt());
}

//  bool QFile::setPermissions(Permissions permissionSpec)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE(
    QFile *self,
    int permissionSpec) {
  return self->setPermissions(
      QFlags<QFileDevice::Permission>::fromInt(permissionSpec));
}

//  bool QFile::setPermissions(const QString &filename, Permissions
//      permissionSpec)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile14setPermissionsERK7QString6QFlagsIN11QFileDevice10PermissionEE(
    const QString *filename,
    int permissionSpec) {
  return QFile::setPermissions(
      *filename,
      QFlags<QFileDevice::Permission>::fromInt(permissionSpec));
}

//  a Python function taken by a CuteQFile, for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFile(QFile *self, const char *key, void *call) {
  return static_cast<CuteQFile *>(self)->take(key, call);
}

//  qint64 QFile::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK5QFile4sizeEv(const QFile *self) {
  return self->QFile::size();
}

//  bool QFile::resize(qint64 sz)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QFile6resizeEx(QFile *self, qint64 sz) {
  return self->QFile::resize(sz);
}
