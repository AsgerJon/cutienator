//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfile.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by hand,
//  instances of templates of the class: 15. Kept as it is when the generator
//  runs again.
#include <QtCore/qfile.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <filesystem>
#include <QtCore/QString>
#include <optional>
#include <QtCore/QFileDevice>
#include <QtCore/qobject.h>

//  A QFile that Python can take functions over in. Every QFile
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef QString * (*CuteQFileCall0)(const void *, int *);
typedef bool (*CuteQFileCall1)(const void *, int, int *);
typedef qint64 (*CuteQFileCall2)(const void *, int *);
typedef bool (*CuteQFileCall3)(const void *, qint64, int *);
typedef int (*CuteQFileCall4)(const void *, int *);
typedef bool (*CuteQFileCall5)(const void *, int, int *);
typedef void (*CuteQFileCall6)(const void *, int *);
typedef bool (*CuteQFileCall7)(const void *, int *);
typedef qint64 (*CuteQFileCall8)(const void *, int *);
typedef bool (*CuteQFileCall9)(const void *, qint64, int *);
typedef bool (*CuteQFileCall10)(const void *, int *);
typedef qint64 (*CuteQFileCall11)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQFileCall12)(const void *, char *, qint64, int *);
typedef bool (*CuteQFileCall13)(const void *, int *);
typedef qint64 (*CuteQFileCall14)(const void *, int *);
typedef qint64 (*CuteQFileCall15)(const void *, int *);
typedef bool (*CuteQFileCall16)(const void *, int *);
typedef bool (*CuteQFileCall17)(const void *, int, int *);
typedef bool (*CuteQFileCall18)(const void *, int, int *);
typedef qint64 (*CuteQFileCall19)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFile : public QFile {
public:
  using QFile::QFile;
  void *taken[27] = {};

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
    if (!std::strcmp(key, "_ZN9QIODevice8readDataEPcx")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice12readLineDataEPcx")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[19] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QString QFile::fileName() const
  QString fileName() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileCall0 call = reinterpret_cast<CuteQFileCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFile::fileName();
  }

  //  bool QFile::open(OpenMode flags)
  bool open(QIODeviceBase::OpenMode flags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQFileCall1 call = reinterpret_cast<CuteQFileCall1>(taken[1]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QFile::open(flags);
  }

  //  qint64 QFile::size() const
  qint64 size() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQFileCall2 call = reinterpret_cast<CuteQFileCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFile::size();
  }

  //  bool QFile::resize(qint64 sz)
  bool resize(qint64 sz) override {
    if (taken[3]) {
      int handled = 0;
      CuteQFileCall3 call = reinterpret_cast<CuteQFileCall3>(taken[3]);
      bool given = call(this, sz, &handled);
      if (handled) return given;
    }
    return QFile::resize(sz);
  }

  //  Permissions QFile::permissions() const
  QFileDevice::Permissions permissions() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQFileCall4 call = reinterpret_cast<CuteQFileCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return QFlags<QFileDevice::Permission>::fromInt(given);
    }
    return QFile::permissions();
  }

  //  bool QFile::setPermissions(Permissions permissionSpec)
  bool setPermissions(QFileDevice::Permissions permissionSpec) override {
    if (taken[5]) {
      int handled = 0;
      CuteQFileCall5 call = reinterpret_cast<CuteQFileCall5>(taken[5]);
      bool given = call(this, static_cast<int>(permissionSpec.toInt()), &handled);
      if (handled) return given;
    }
    return QFile::setPermissions(permissionSpec);
  }

  //  void QFileDevice::close()
  void close() override {
    if (taken[6]) {
      int handled = 0;
      CuteQFileCall6 call = reinterpret_cast<CuteQFileCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QFileDevice::close();
  }

  //  bool QFileDevice::isSequential() const
  bool isSequential() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQFileCall7 call = reinterpret_cast<CuteQFileCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::isSequential();
  }

  //  qint64 QFileDevice::pos() const
  qint64 pos() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFileCall8 call = reinterpret_cast<CuteQFileCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::pos();
  }

  //  bool QFileDevice::seek(qint64 offset)
  bool seek(qint64 offset) override {
    if (taken[9]) {
      int handled = 0;
      CuteQFileCall9 call = reinterpret_cast<CuteQFileCall9>(taken[9]);
      bool given = call(this, offset, &handled);
      if (handled) return given;
    }
    return QFileDevice::seek(offset);
  }

  //  bool QFileDevice::atEnd() const
  bool atEnd() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQFileCall10 call = reinterpret_cast<CuteQFileCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::atEnd();
  }

  //  qint64 QFileDevice::readData(char *data, qint64 maxlen)
  qint64 readData(char *data, qint64 maxlen) override {
    if (taken[11]) {
      int handled = 0;
      CuteQFileCall11 call = reinterpret_cast<CuteQFileCall11>(taken[11]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QFileDevice::readData(data, maxlen);
  }

  //  qint64 QFileDevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[12]) {
      int handled = 0;
      CuteQFileCall12 call = reinterpret_cast<CuteQFileCall12>(taken[12]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QFileDevice::readLineData(data, maxlen);
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[13]) {
      int handled = 0;
      CuteQFileCall13 call = reinterpret_cast<CuteQFileCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQFileCall14 call = reinterpret_cast<CuteQFileCall14>(taken[14]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQFileCall15 call = reinterpret_cast<CuteQFileCall15>(taken[15]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQFileCall16 call = reinterpret_cast<CuteQFileCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFileCall17 call = reinterpret_cast<CuteQFileCall17>(taken[17]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[18]) {
      int handled = 0;
      CuteQFileCall18 call = reinterpret_cast<CuteQFileCall18>(taken[18]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[19]) {
      int handled = 0;
      CuteQFileCall19 call = reinterpret_cast<CuteQFileCall19>(taken[19]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQFileCall20 call = reinterpret_cast<CuteQFileCall20>(taken[20]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQFileCall21 call = reinterpret_cast<CuteQFileCall21>(taken[21]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQFileCall22 call = reinterpret_cast<CuteQFileCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQFileCall23 call = reinterpret_cast<CuteQFileCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQFileCall24 call = reinterpret_cast<CuteQFileCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQFileCall25 call = reinterpret_cast<CuteQFileCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteQFileCall26 call = reinterpret_cast<CuteQFileCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

#if !defined(QT_NO_QOBJECT)
//  const QMetaObject *QFile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5QFile10metaObjectEv(const QFile *self) {
  return self->metaObject();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  void *QFile::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN5QFile11qt_metacastEPKc(QFile *self, const char *a0) {
  return self->qt_metacast(a0);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  int QFile::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN5QFile11qt_metacallEN11QMetaObject4CallEiPPv(
    QFile *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  QString QFile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QFile2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QFile::tr(s, c, n));
}
#endif  // !defined(QT_NO_QOBJECT)

//  QFilePrivate *QFile::d_func()
extern "C" Q_DECL_EXPORT
QFilePrivate *ritual_ZN5QFile6d_funcEv(QFile *self) {
  return self->d_func();
}

//  const QFilePrivate *QFile::d_func() const
extern "C" Q_DECL_EXPORT
const QFilePrivate *ritual_ZNK5QFile6d_funcEv(const QFile *self) {
  return self->d_func();
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

#if !defined(QT_NO_QOBJECT)
//  QFile::QFile(QObject *parent)
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1EP7QObject(QObject *parent) {
  return new CuteQFile(parent);
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  QFile::QFile(const QString &name, QObject *parent)
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1ERK7QStringP7QObject(
    const QString *name,
    QObject *parent) {
  return new CuteQFile(*name, parent);
}
#endif  // !defined(QT_NO_QOBJECT)

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

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QFile::filesystemFileName() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK5QFile18filesystemFileNameB5cxx11Ev(
    const QFile *self) {
  return new std::filesystem::path(self->filesystemFileName());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

//  void QFile::setFileName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFile11setFileNameERK7QString(
    QFile *self,
    const QString *name) {
  self->setFileName(*name);
}

#if !(defined(Q_OS_DARWIN))
//  QByteArray QFile::encodeName(const QString &fileName)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN5QFile10encodeNameERK7QString(const QString *fileName) {
  return new QByteArray(QFile::encodeName(*fileName));
}
#endif  // !(defined(Q_OS_DARWIN))

#if !(defined(Q_OS_DARWIN))
//  QString QFile::decodeName(const QByteArray &localFileName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QFile10decodeNameERK10QByteArray(
    const QByteArray *localFileName) {
  return new QString(QFile::decodeName(*localFileName));
}
#endif  // !(defined(Q_OS_DARWIN))

#if !(defined(Q_OS_DARWIN))
//  QString QFile::decodeName(const char *localFileName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QFile10decodeNameEPKc(const char *localFileName) {
  return new QString(QFile::decodeName(localFileName));
}
#endif  // !(defined(Q_OS_DARWIN))

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

#if (!(defined(Q_QDOC))) && (QT_CONFIG(cxx17_filesystem))
//  std::filesystem::path QFile::filesystemSymLinkTarget() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK5QFile23filesystemSymLinkTargetB5cxx11Ev(
    const QFile *self) {
  return new std::filesystem::path(self->filesystemSymLinkTarget());
}
#endif  // (!(defined(Q_QDOC))) && (QT_CONFIG(cxx17_filesystem))

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

#if QT_CONFIG(temporaryfile)
//  bool QFile::copy(const QString &newName,
//      std::optional<QFileDevice::Permissions> perm)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4copyERK7QStringSt8optionalI6QFlagsIN11QFileDevice10PermissionEEE(
    QFile *self,
    const QString *newName,
    const std::optional<QFileDevice::Permissions> *perm) {
  return self->copy(*newName, *perm);
}
#endif  // QT_CONFIG(temporaryfile)

#if QT_CONFIG(temporaryfile)
//  bool QFile::copy(const QString &fileName, const QString &newName,
//      std::optional<QFileDevice::Permissions> perm)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4copyERK7QStringS2_St8optionalI6QFlagsIN11QFileDevice10PermissionEEE(
    const QString *fileName,
    const QString *newName,
    const std::optional<QFileDevice::Permissions> *perm) {
  return QFile::copy(*fileName, *newName, *perm);
}
#endif  // QT_CONFIG(temporaryfile)

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

//  bool QFile::open(FILE *f, OpenMode ioFlags, FileHandleFlags handleFlags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4openEP8_IO_FILE6QFlagsIN13QIODeviceBase12OpenModeFlagEES2_IN11QFileDevice14FileHandleFlagEE(
    QFile *self,
    FILE *f,
    int ioFlags,
    int handleFlags) {
  return self->open(
      f,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(ioFlags),
      QFlags<QFileDevice::FileHandleFlag>::fromInt(handleFlags));
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

#if !(defined(QT_NO_QOBJECT))
//  QFile::QFile(QFilePrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1ER12QFilePrivateP7QObject(
    QFilePrivate *dd,
    QObject *parent) {
  return new CuteQFile(*dd, parent);
}
#endif  // !(defined(QT_NO_QOBJECT))

//  a Python function taken by a CuteQFile, for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFile(QFile *self, const char *key, void *call) {
  return static_cast<CuteQFile *>(self)->take(key, call);
}

//  QString QFile::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK5QFile8fileNameEv(const QFile *self) {
  return new QString(self->QFile::fileName());
}

//  bool QFile::open(OpenMode flags)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QFile *self,
    int flags) {
  return self->QFile::open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags));
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

//  Permissions QFile::permissions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK5QFile11permissionsEv(const QFile *self) {
  return static_cast<int>(self->QFile::permissions().toInt());
}

//  bool QFile::setPermissions(Permissions permissionSpec)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN5QFile14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE(
    QFile *self,
    int permissionSpec) {
  return self->QFile::setPermissions(
      QFlags<QFileDevice::Permission>::fromInt(permissionSpec));
}

//  a std::filesystem::path a ritual of QFile gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QFile__std_filesystem_path(std::filesystem::path *self) {
  delete self;
}

#if QT_CONFIG(cxx17_filesystem)
//  QFile::QFile(const T &name) [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1INSt10filesystem7__cxx114pathELi0EEERKT_(
    const std::filesystem::path *name) {
  return new QFile(*name);
}

#if !defined(QT_NO_QOBJECT)
//  QFile::QFile(const T &path, QObject *parent)
//      [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
QFile *ritual_ZN5QFileC1INSt10filesystem7__cxx114pathELi0EEERKT_P7QObject(
    const std::filesystem::path *path,
    QObject *parent) {
  return new QFile(*path, parent);
}
#endif  // !defined(QT_NO_QOBJECT)

//  void QFile::setFileName(const T &name) [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFile11setFileNameINSt10filesystem7__cxx114pathELi0EEEvRKT_(
    QFile *self,
    const std::filesystem::path *name) {
  self->setFileName<std::filesystem::path>(*name);
}

//  static bool QFile::exists(const T &fileName)
//      [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6existsINSt10filesystem7__cxx114pathELi0EEEbRKT_(
    const std::filesystem::path *fileName) {
  return QFile::exists<std::filesystem::path>(*fileName);
}

//  static std::filesystem::path QFile::filesystemSymLinkTarget(
//      const T &fileName) [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZN5QFile23filesystemSymLinkTargetB5cxx11INSt10filesystem7__cxx114pathELi0EEES3_RKT_(
    const std::filesystem::path *fileName) {
  return new std::filesystem::path(
      QFile::filesystemSymLinkTarget<std::filesystem::path>(*fileName));
}

//  static bool QFile::remove(const T &fileName)
//      [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6removeINSt10filesystem7__cxx114pathELi0EEEbRKT_(
    const std::filesystem::path *fileName) {
  return QFile::remove<std::filesystem::path>(*fileName);
}

//  static bool QFile::moveToTrash(const T &fileName,
//      QString *pathInTrash) [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile11moveToTrashINSt10filesystem7__cxx114pathELi0EEEbRKT_P7QString(
    const std::filesystem::path *fileName,
    QString *pathInTrash) {
  return QFile::moveToTrash<std::filesystem::path>(
      *fileName, pathInTrash);
}

//  bool QFile::rename(const T &newName) [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6renameINSt10filesystem7__cxx114pathELi0EEEbRKT_(
    QFile *self,
    const std::filesystem::path *newName) {
  return self->rename<std::filesystem::path>(*newName);
}

//  static bool QFile::rename(const T &oldName, const T &newName)
//      [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile6renameINSt10filesystem7__cxx114pathELi0EEEbRKT_S6_(
    const std::filesystem::path *oldName,
    const std::filesystem::path *newName) {
  return QFile::rename<std::filesystem::path>(*oldName, *newName);
}

//  bool QFile::link(const T &newName) [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4linkINSt10filesystem7__cxx114pathELi0EEEbRKT_(
    QFile *self,
    const std::filesystem::path *newName) {
  return self->link<std::filesystem::path>(*newName);
}

//  static bool QFile::link(const T &fileName, const T &newName)
//      [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4linkINSt10filesystem7__cxx114pathELi0EEEbRKT_S6_(
    const std::filesystem::path *fileName,
    const std::filesystem::path *newName) {
  return QFile::link<std::filesystem::path>(*fileName, *newName);
}

#if QT_CONFIG(temporaryfile)
//  bool QFile::copy(const T &newName) [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4copyINSt10filesystem7__cxx114pathELi0EEEbRKT_(
    QFile *self,
    const std::filesystem::path *newName) {
  return self->copy<std::filesystem::path>(*newName);
}
#endif  // QT_CONFIG(temporaryfile)

#if QT_CONFIG(temporaryfile)
//  static bool QFile::copy(const T &fileName, const T &newName)
//      [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile4copyINSt10filesystem7__cxx114pathELi0EEEbRKT_S6_(
    const std::filesystem::path *fileName,
    const std::filesystem::path *newName) {
  return QFile::copy<std::filesystem::path>(*fileName, *newName);
}
#endif  // QT_CONFIG(temporaryfile)

//  static Permissions QFile::permissions(const T &filename)
//      [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
int ritual_ZN5QFile11permissionsINSt10filesystem7__cxx114pathELi0EEE6QFlagsIN11QFileDevice10PermissionEERKT_(
    const std::filesystem::path *filename) {
  return static_cast<int>(
      QFile::permissions<std::filesystem::path>(*filename).toInt());
}

//  static bool QFile::setPermissions(const T &filename,
//      Permissions permissionSpec) [T = std::filesystem::path]
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QFile14setPermissionsINSt10filesystem7__cxx114pathELi0EEEbRKT_6QFlagsIN11QFileDevice10PermissionEE(
    const std::filesystem::path *filename,
    int permissionSpec) {
  return QFile::setPermissions<std::filesystem::path>(
      *filename,
      QFlags<QFileDevice::Permission>::fromInt(permissionSpec));
}
#endif  // QT_CONFIG(cxx17_filesystem)
