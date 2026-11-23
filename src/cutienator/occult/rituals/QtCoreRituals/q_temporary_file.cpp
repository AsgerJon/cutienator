//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtemporaryfile.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtemporaryfile.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QTemporaryFile may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTemporaryFile : QTemporaryFile {
  using QTemporaryFile::open;
};

//  A QTemporaryFile that Python can take functions over in. Every QTemporaryFile
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQTemporaryFileCall0)(const void *, int *);
typedef bool (*CuteQTemporaryFileCall1)(const void *, int, int *);
typedef qint64 (*CuteQTemporaryFileCall2)(const void *, int *);
typedef bool (*CuteQTemporaryFileCall3)(const void *, qint64, int *);
typedef int (*CuteQTemporaryFileCall4)(const void *, int *);
typedef bool (*CuteQTemporaryFileCall5)(const void *, int, int *);
typedef void (*CuteQTemporaryFileCall6)(const void *, int *);
typedef bool (*CuteQTemporaryFileCall7)(const void *, int *);
typedef qint64 (*CuteQTemporaryFileCall8)(const void *, int *);
typedef bool (*CuteQTemporaryFileCall9)(const void *, qint64, int *);
typedef bool (*CuteQTemporaryFileCall10)(const void *, int *);
typedef bool (*CuteQTemporaryFileCall11)(const void *, int *);
typedef qint64 (*CuteQTemporaryFileCall12)(const void *, int *);
typedef qint64 (*CuteQTemporaryFileCall13)(const void *, int *);
typedef bool (*CuteQTemporaryFileCall14)(const void *, int *);
typedef bool (*CuteQTemporaryFileCall15)(const void *, int, int *);
typedef bool (*CuteQTemporaryFileCall16)(const void *, int, int *);
typedef qint64 (*CuteQTemporaryFileCall17)(const void *, qint64, int *);
typedef bool (*CuteQTemporaryFileCall18)(const void *, QEvent *, int *);
typedef bool (*CuteQTemporaryFileCall19)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQTemporaryFileCall20)(const void *, QTimerEvent *, int *);
typedef void (*CuteQTemporaryFileCall21)(const void *, QChildEvent *, int *);
typedef void (*CuteQTemporaryFileCall22)(const void *, QEvent *, int *);
typedef void (*CuteQTemporaryFileCall23)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQTemporaryFileCall24)(const void *, const QMetaMethod *, int *);
class CuteQTemporaryFile : public QTemporaryFile {
public:
  using QTemporaryFile::QTemporaryFile;
  void *taken[25] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK11QFileDevice8fileNameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFileDevice6resizeEx")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFileDevice11permissionsEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFileDevice14setPermissionsE6QFlagsINS_10PermissionEE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[24] = call;
      return true;
    }
    return false;
  }

  //  QString QTemporaryFile::fileName() const
  QString fileName() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTemporaryFileCall0 call = reinterpret_cast<CuteQTemporaryFileCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QTemporaryFile::fileName();
  }

  //  bool QTemporaryFile::open(OpenMode flags)
  bool open(QIODeviceBase::OpenMode flags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTemporaryFileCall1 call = reinterpret_cast<CuteQTemporaryFileCall1>(taken[1]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QTemporaryFile::open(flags);
  }

  //  qint64 QFile::size() const
  qint64 size() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTemporaryFileCall2 call = reinterpret_cast<CuteQTemporaryFileCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFile::size();
  }

  //  bool QFile::resize(qint64 sz)
  bool resize(qint64 sz) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTemporaryFileCall3 call = reinterpret_cast<CuteQTemporaryFileCall3>(taken[3]);
      bool given = call(this, sz, &handled);
      if (handled) return given;
    }
    return QFile::resize(sz);
  }

  //  Permissions QFile::permissions() const
  QFileDevice::Permissions permissions() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQTemporaryFileCall4 call = reinterpret_cast<CuteQTemporaryFileCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return QFlags<QFileDevice::Permission>::fromInt(given);
    }
    return QFile::permissions();
  }

  //  bool QFile::setPermissions(Permissions permissionSpec)
  bool setPermissions(QFileDevice::Permissions permissionSpec) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTemporaryFileCall5 call = reinterpret_cast<CuteQTemporaryFileCall5>(taken[5]);
      bool given = call(this, static_cast<int>(permissionSpec.toInt()), &handled);
      if (handled) return given;
    }
    return QFile::setPermissions(permissionSpec);
  }

  //  void QFileDevice::close()
  void close() override {
    if (taken[6]) {
      int handled = 0;
      CuteQTemporaryFileCall6 call = reinterpret_cast<CuteQTemporaryFileCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QFileDevice::close();
  }

  //  bool QFileDevice::isSequential() const
  bool isSequential() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQTemporaryFileCall7 call = reinterpret_cast<CuteQTemporaryFileCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::isSequential();
  }

  //  qint64 QFileDevice::pos() const
  qint64 pos() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTemporaryFileCall8 call = reinterpret_cast<CuteQTemporaryFileCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::pos();
  }

  //  bool QFileDevice::seek(qint64 offset)
  bool seek(qint64 offset) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTemporaryFileCall9 call = reinterpret_cast<CuteQTemporaryFileCall9>(taken[9]);
      bool given = call(this, offset, &handled);
      if (handled) return given;
    }
    return QFileDevice::seek(offset);
  }

  //  bool QFileDevice::atEnd() const
  bool atEnd() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQTemporaryFileCall10 call = reinterpret_cast<CuteQTemporaryFileCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::atEnd();
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[11]) {
      int handled = 0;
      CuteQTemporaryFileCall11 call = reinterpret_cast<CuteQTemporaryFileCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQTemporaryFileCall12 call = reinterpret_cast<CuteQTemporaryFileCall12>(taken[12]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQTemporaryFileCall13 call = reinterpret_cast<CuteQTemporaryFileCall13>(taken[13]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQTemporaryFileCall14 call = reinterpret_cast<CuteQTemporaryFileCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[15]) {
      int handled = 0;
      CuteQTemporaryFileCall15 call = reinterpret_cast<CuteQTemporaryFileCall15>(taken[15]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[16]) {
      int handled = 0;
      CuteQTemporaryFileCall16 call = reinterpret_cast<CuteQTemporaryFileCall16>(taken[16]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[17]) {
      int handled = 0;
      CuteQTemporaryFileCall17 call = reinterpret_cast<CuteQTemporaryFileCall17>(taken[17]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQTemporaryFileCall18 call = reinterpret_cast<CuteQTemporaryFileCall18>(taken[18]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTemporaryFileCall19 call = reinterpret_cast<CuteQTemporaryFileCall19>(taken[19]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQTemporaryFileCall20 call = reinterpret_cast<CuteQTemporaryFileCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQTemporaryFileCall21 call = reinterpret_cast<CuteQTemporaryFileCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQTemporaryFileCall22 call = reinterpret_cast<CuteQTemporaryFileCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteQTemporaryFileCall23 call = reinterpret_cast<CuteQTemporaryFileCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTemporaryFileCall24 call = reinterpret_cast<CuteQTemporaryFileCall24>(taken[24]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QTemporaryFile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QTemporaryFile10metaObjectEv(
    const QTemporaryFile *self) {
  return self->metaObject();
}

//  QString QTemporaryFile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QTemporaryFile2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTemporaryFile::tr(s, c, n));
}

//  QTemporaryFile::QTemporaryFile()
extern "C" Q_DECL_EXPORT
QTemporaryFile *ritual_ZN14QTemporaryFileC1Ev() {
  return new CuteQTemporaryFile();
}

//  QTemporaryFile::QTemporaryFile(const QString &templateName)
extern "C" Q_DECL_EXPORT
QTemporaryFile *ritual_ZN14QTemporaryFileC1ERK7QString(
    const QString *templateName) {
  return new CuteQTemporaryFile(*templateName);
}

//  QTemporaryFile::QTemporaryFile(QObject *parent)
extern "C" Q_DECL_EXPORT
QTemporaryFile *ritual_ZN14QTemporaryFileC1EP7QObject(QObject *parent) {
  return new CuteQTemporaryFile(parent);
}

//  QTemporaryFile::QTemporaryFile(const QString &templateName, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QTemporaryFile *ritual_ZN14QTemporaryFileC1ERK7QStringP7QObject(
    const QString *templateName,
    QObject *parent) {
  return new CuteQTemporaryFile(*templateName, parent);
}

//  QTemporaryFile::~QTemporaryFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTemporaryFileD1Ev(QTemporaryFile *self) {
  delete self;
}

//  bool QTemporaryFile::autoRemove() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QTemporaryFile10autoRemoveEv(const QTemporaryFile *self) {
  return self->autoRemove();
}

//  void QTemporaryFile::setAutoRemove(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTemporaryFile13setAutoRemoveEb(
    QTemporaryFile *self,
    bool b) {
  self->setAutoRemove(b);
}

//  bool QTemporaryFile::open()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QTemporaryFile4openEv(QTemporaryFile *self) {
  return self->open();
}

//  QString QTemporaryFile::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QTemporaryFile8fileNameEv(const QTemporaryFile *self) {
  return new QString(self->fileName());
}

//  QString QTemporaryFile::fileTemplate() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QTemporaryFile12fileTemplateEv(
    const QTemporaryFile *self) {
  return new QString(self->fileTemplate());
}

//  void QTemporaryFile::setFileTemplate(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTemporaryFile15setFileTemplateERK7QString(
    QTemporaryFile *self,
    const QString *name) {
  self->setFileTemplate(*name);
}

//  bool QTemporaryFile::rename(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QTemporaryFile6renameERK7QString(
    QTemporaryFile *self,
    const QString *newName) {
  return self->rename(*newName);
}

//  bool QTemporaryFile::renameOverwrite(const QString &newName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QTemporaryFile15renameOverwriteERK7QString(
    QTemporaryFile *self,
    const QString *newName) {
  return self->renameOverwrite(*newName);
}

//  QTemporaryFile *QTemporaryFile::createNativeFile(const QString &fileName)
extern "C" Q_DECL_EXPORT
QTemporaryFile *ritual_ZN14QTemporaryFile16createNativeFileERK7QString(
    const QString *fileName) {
  return QTemporaryFile::createNativeFile(*fileName);
}

//  bool QTemporaryFile::open(OpenMode flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QTemporaryFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QTemporaryFile *self,
    int flags) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags));
}

//  a Python function taken by a CuteQTemporaryFile, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTemporaryFile(
    QTemporaryFile *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTemporaryFile *>(self)->take(key, call);
}

//  QString QTemporaryFile::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK14QTemporaryFile8fileNameEv(
    const QTemporaryFile *self) {
  return new QString(self->QTemporaryFile::fileName());
}

//  bool QTemporaryFile::open(OpenMode flags)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QTemporaryFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QTemporaryFile *self,
    int flags) {
  return static_cast<OwnQTemporaryFile *>(self)->OwnQTemporaryFile::open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags));
}
