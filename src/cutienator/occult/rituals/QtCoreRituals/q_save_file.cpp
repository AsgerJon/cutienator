//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsavefile.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(temporaryfile)
#include <QtCore/qsavefile.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <filesystem>

//  A QSaveFile that Python can take functions over in. Every QSaveFile
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(temporaryfile)
typedef QString * (*CuteQSaveFileCall0)(const void *, int *);
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
typedef bool (*CuteQSaveFileCall1)(const void *, int, int *);
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
typedef void (*CuteQSaveFileCall2)(const void *, int *);
#endif  // QT_CONFIG(temporaryfile)
typedef bool (*CuteQSaveFileCall3)(const void *, int *);
typedef qint64 (*CuteQSaveFileCall4)(const void *, int *);
typedef bool (*CuteQSaveFileCall5)(const void *, qint64, int *);
typedef bool (*CuteQSaveFileCall6)(const void *, int *);
typedef qint64 (*CuteQSaveFileCall7)(const void *, int *);
typedef bool (*CuteQSaveFileCall8)(const void *, qint64, int *);
typedef int (*CuteQSaveFileCall9)(const void *, int *);
typedef bool (*CuteQSaveFileCall10)(const void *, int, int *);
typedef qint64 (*CuteQSaveFileCall11)(const void *, char *, qint64, int *);
typedef qint64 (*CuteQSaveFileCall12)(const void *, char *, qint64, int *);
typedef bool (*CuteQSaveFileCall13)(const void *, int *);
typedef qint64 (*CuteQSaveFileCall14)(const void *, int *);
typedef qint64 (*CuteQSaveFileCall15)(const void *, int *);
typedef bool (*CuteQSaveFileCall16)(const void *, int *);
typedef bool (*CuteQSaveFileCall17)(const void *, int, int *);
typedef bool (*CuteQSaveFileCall18)(const void *, int, int *);
typedef qint64 (*CuteQSaveFileCall19)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSaveFileCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSaveFileCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSaveFileCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSaveFileCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSaveFileCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSaveFileCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSaveFileCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSaveFile : public QSaveFile {
public:
  using QSaveFile::QSaveFile;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZNK11QFileDevice8fileNameEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(temporaryfile)
#if QT_CONFIG(temporaryfile)
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(temporaryfile)
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
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFileDevice6resizeEx")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFileDevice11permissionsEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFileDevice14setPermissionsE6QFlagsINS_10PermissionEE")) {
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

#if QT_CONFIG(temporaryfile)
  //  QString QSaveFile::fileName() const
  QString fileName() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSaveFileCall0 call = reinterpret_cast<CuteQSaveFileCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QSaveFile::fileName();
  }
#endif  // QT_CONFIG(temporaryfile)

#if QT_CONFIG(temporaryfile)
  //  bool QSaveFile::open(OpenMode flags)
  bool open(QIODeviceBase::OpenMode flags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSaveFileCall1 call = reinterpret_cast<CuteQSaveFileCall1>(taken[1]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QSaveFile::open(flags);
  }
#endif  // QT_CONFIG(temporaryfile)

#if QT_CONFIG(temporaryfile)
  //  void QSaveFile::close()
  void close() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSaveFileCall2 call = reinterpret_cast<CuteQSaveFileCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QSaveFile::close();
  }
#endif  // QT_CONFIG(temporaryfile)

  //  bool QFileDevice::isSequential() const
  bool isSequential() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSaveFileCall3 call = reinterpret_cast<CuteQSaveFileCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::isSequential();
  }

  //  qint64 QFileDevice::pos() const
  qint64 pos() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSaveFileCall4 call = reinterpret_cast<CuteQSaveFileCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::pos();
  }

  //  bool QFileDevice::seek(qint64 offset)
  bool seek(qint64 offset) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSaveFileCall5 call = reinterpret_cast<CuteQSaveFileCall5>(taken[5]);
      bool given = call(this, offset, &handled);
      if (handled) return given;
    }
    return QFileDevice::seek(offset);
  }

  //  bool QFileDevice::atEnd() const
  bool atEnd() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSaveFileCall6 call = reinterpret_cast<CuteQSaveFileCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::atEnd();
  }

  //  qint64 QFileDevice::size() const
  qint64 size() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSaveFileCall7 call = reinterpret_cast<CuteQSaveFileCall7>(taken[7]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::size();
  }

  //  bool QFileDevice::resize(qint64 sz)
  bool resize(qint64 sz) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSaveFileCall8 call = reinterpret_cast<CuteQSaveFileCall8>(taken[8]);
      bool given = call(this, sz, &handled);
      if (handled) return given;
    }
    return QFileDevice::resize(sz);
  }

  //  Permissions QFileDevice::permissions() const
  QFileDevice::Permissions permissions() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSaveFileCall9 call = reinterpret_cast<CuteQSaveFileCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return QFlags<QFileDevice::Permission>::fromInt(given);
    }
    return QFileDevice::permissions();
  }

  //  bool QFileDevice::setPermissions(Permissions permissionSpec)
  bool setPermissions(QFileDevice::Permissions permissionSpec) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSaveFileCall10 call = reinterpret_cast<CuteQSaveFileCall10>(taken[10]);
      bool given = call(this, static_cast<int>(permissionSpec.toInt()), &handled);
      if (handled) return given;
    }
    return QFileDevice::setPermissions(permissionSpec);
  }

  //  qint64 QFileDevice::readData(char *data, qint64 maxlen)
  qint64 readData(char *data, qint64 maxlen) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSaveFileCall11 call = reinterpret_cast<CuteQSaveFileCall11>(taken[11]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QFileDevice::readData(data, maxlen);
  }

  //  qint64 QFileDevice::readLineData(char *data, qint64 maxlen)
  qint64 readLineData(char *data, qint64 maxlen) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSaveFileCall12 call = reinterpret_cast<CuteQSaveFileCall12>(taken[12]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QFileDevice::readLineData(data, maxlen);
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[13]) {
      int handled = 0;
      CuteQSaveFileCall13 call = reinterpret_cast<CuteQSaveFileCall13>(taken[13]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQSaveFileCall14 call = reinterpret_cast<CuteQSaveFileCall14>(taken[14]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQSaveFileCall15 call = reinterpret_cast<CuteQSaveFileCall15>(taken[15]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSaveFileCall16 call = reinterpret_cast<CuteQSaveFileCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSaveFileCall17 call = reinterpret_cast<CuteQSaveFileCall17>(taken[17]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSaveFileCall18 call = reinterpret_cast<CuteQSaveFileCall18>(taken[18]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSaveFileCall19 call = reinterpret_cast<CuteQSaveFileCall19>(taken[19]);
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
      CuteQSaveFileCall20 call = reinterpret_cast<CuteQSaveFileCall20>(taken[20]);
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
      CuteQSaveFileCall21 call = reinterpret_cast<CuteQSaveFileCall21>(taken[21]);
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
      CuteQSaveFileCall22 call = reinterpret_cast<CuteQSaveFileCall22>(taken[22]);
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
      CuteQSaveFileCall23 call = reinterpret_cast<CuteQSaveFileCall23>(taken[23]);
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
      CuteQSaveFileCall24 call = reinterpret_cast<CuteQSaveFileCall24>(taken[24]);
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
      CuteQSaveFileCall25 call = reinterpret_cast<CuteQSaveFileCall25>(taken[25]);
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
      CuteQSaveFileCall26 call = reinterpret_cast<CuteQSaveFileCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSaveFile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QSaveFile10metaObjectEv(
    const QSaveFile *self) {
  return self->metaObject();
}

//  void *QSaveFile::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN9QSaveFile11qt_metacastEPKc(QSaveFile *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSaveFile::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QSaveFile11qt_metacallEN11QMetaObject4CallEiPPv(
    QSaveFile *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSaveFile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QSaveFile2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSaveFile::tr(s, c, n));
}

//  QSaveFilePrivate *QSaveFile::d_func()
extern "C" Q_DECL_EXPORT
QSaveFilePrivate *ritual_ZN9QSaveFile6d_funcEv(QSaveFile *self) {
  return self->d_func();
}

//  const QSaveFilePrivate *QSaveFile::d_func() const
extern "C" Q_DECL_EXPORT
const QSaveFilePrivate *ritual_ZNK9QSaveFile6d_funcEv(
    const QSaveFile *self) {
  return self->d_func();
}

//  QSaveFile::QSaveFile(QObject *parent)
extern "C" Q_DECL_EXPORT
QSaveFile *ritual_ZN9QSaveFileC1EP7QObject(QObject *parent) {
  return new CuteQSaveFile(parent);
}

//  QSaveFile::QSaveFile(const QString &name, QObject *parent)
extern "C" Q_DECL_EXPORT
QSaveFile *ritual_ZN9QSaveFileC1ERK7QStringP7QObject(
    const QString *name,
    QObject *parent) {
  return new CuteQSaveFile(*name, parent);
}

//  QSaveFile::~QSaveFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSaveFileD1Ev(QSaveFile *self) {
  delete self;
}

//  QString QSaveFile::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QSaveFile8fileNameEv(const QSaveFile *self) {
  return new QString(self->fileName());
}

//  void QSaveFile::setFileName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSaveFile11setFileNameERK7QString(
    QSaveFile *self,
    const QString *name) {
  self->setFileName(*name);
}

//  bool QSaveFile::open(OpenMode flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSaveFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QSaveFile *self,
    int flags) {
  return self->open(QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags));
}

//  bool QSaveFile::commit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN9QSaveFile6commitEv(QSaveFile *self) {
  return self->commit();
}

//  void QSaveFile::cancelWriting()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSaveFile13cancelWritingEv(QSaveFile *self) {
  self->cancelWriting();
}

//  void QSaveFile::setDirectWriteFallback(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSaveFile22setDirectWriteFallbackEb(
    QSaveFile *self,
    bool enabled) {
  self->setDirectWriteFallback(enabled);
}

//  bool QSaveFile::directWriteFallback() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSaveFile19directWriteFallbackEv(const QSaveFile *self) {
  return self->directWriteFallback();
}

#if QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)
//  std::filesystem::path QSaveFile::filesystemFileName() const
extern "C" Q_DECL_EXPORT
std::filesystem::path *ritual_ZNK9QSaveFile18filesystemFileNameB5cxx11Ev(
    const QSaveFile *self) {
  return new std::filesystem::path(self->filesystemFileName());
}
#endif  // QT_CONFIG(cxx17_filesystem) || defined(Q_QDOC)

//  qint64 QSaveFile::writeData(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN9QSaveFile9writeDataEPKcx(
    QSaveFile *self,
    const char *data,
    qint64 len) {
  return self->writeData(data, len);
}

//  void QSaveFile::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSaveFile5closeEv(QSaveFile *self) {
  self->close();
}

//  a Python function taken by a CuteQSaveFile, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSaveFile(QSaveFile *self, const char *key, void *call) {
  return static_cast<CuteQSaveFile *>(self)->take(key, call);
}

//  QString QSaveFile::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK9QSaveFile8fileNameEv(const QSaveFile *self) {
  return new QString(self->QSaveFile::fileName());
}

//  bool QSaveFile::open(OpenMode flags)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN9QSaveFile4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QSaveFile *self,
    int flags) {
  return self->QSaveFile::open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags));
}

//  void QSaveFile::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN9QSaveFile5closeEv(QSaveFile *self) {
  self->QSaveFile::close();
}

//  a std::filesystem::path a ritual of QSaveFile gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSaveFile__std_filesystem_path(
    std::filesystem::path *self) {
  delete self;
}

#endif  // QT_CONFIG(temporaryfile)
