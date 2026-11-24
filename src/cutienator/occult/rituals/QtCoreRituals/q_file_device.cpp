//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfiledevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qfiledevice.h>
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QFileDevice that Python can take functions over in. Every QFileDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQFileDeviceCall0)(const void *, int *);
typedef bool (*CuteQFileDeviceCall1)(const void *, int *);
typedef QString * (*CuteQFileDeviceCall2)(const void *, int *);
typedef qint64 (*CuteQFileDeviceCall3)(const void *, int *);
typedef bool (*CuteQFileDeviceCall4)(const void *, qint64, int *);
typedef bool (*CuteQFileDeviceCall5)(const void *, int *);
typedef qint64 (*CuteQFileDeviceCall6)(const void *, int *);
typedef bool (*CuteQFileDeviceCall7)(const void *, qint64, int *);
typedef int (*CuteQFileDeviceCall8)(const void *, int *);
typedef bool (*CuteQFileDeviceCall9)(const void *, int, int *);
typedef bool (*CuteQFileDeviceCall10)(const void *, int, int *);
typedef bool (*CuteQFileDeviceCall11)(const void *, int *);
typedef qint64 (*CuteQFileDeviceCall12)(const void *, int *);
typedef qint64 (*CuteQFileDeviceCall13)(const void *, int *);
typedef bool (*CuteQFileDeviceCall14)(const void *, int *);
typedef bool (*CuteQFileDeviceCall15)(const void *, int, int *);
typedef bool (*CuteQFileDeviceCall16)(const void *, int, int *);
typedef qint64 (*CuteQFileDeviceCall17)(const void *, qint64, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileDeviceCall18)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQFileDeviceCall19)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDeviceCall20)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDeviceCall21)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDeviceCall22)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDeviceCall23)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQFileDeviceCall24)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQFileDevice : public QFileDevice {
public:
  using QFileDevice::QFileDevice;
  void *taken[25] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QIODevice5closeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFileDevice8fileNameEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFileDevice6resizeEx")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QFileDevice11permissionsEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFileDevice14setPermissionsE6QFlagsINS_10PermissionEE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QFileDevice::close()
  void close() override {
    if (taken[0]) {
      int handled = 0;
      CuteQFileDeviceCall0 call = reinterpret_cast<CuteQFileDeviceCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QFileDevice::close();
  }

  //  bool QFileDevice::isSequential() const
  bool isSequential() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQFileDeviceCall1 call = reinterpret_cast<CuteQFileDeviceCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::isSequential();
  }

  //  QString QFileDevice::fileName() const
  QString fileName() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQFileDeviceCall2 call = reinterpret_cast<CuteQFileDeviceCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QFileDevice::fileName();
  }

  //  qint64 QFileDevice::pos() const
  qint64 pos() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQFileDeviceCall3 call = reinterpret_cast<CuteQFileDeviceCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::pos();
  }

  //  bool QFileDevice::seek(qint64 offset)
  bool seek(qint64 offset) override {
    if (taken[4]) {
      int handled = 0;
      CuteQFileDeviceCall4 call = reinterpret_cast<CuteQFileDeviceCall4>(taken[4]);
      bool given = call(this, offset, &handled);
      if (handled) return given;
    }
    return QFileDevice::seek(offset);
  }

  //  bool QFileDevice::atEnd() const
  bool atEnd() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQFileDeviceCall5 call = reinterpret_cast<CuteQFileDeviceCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::atEnd();
  }

  //  qint64 QFileDevice::size() const
  qint64 size() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQFileDeviceCall6 call = reinterpret_cast<CuteQFileDeviceCall6>(taken[6]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::size();
  }

  //  bool QFileDevice::resize(qint64 sz)
  bool resize(qint64 sz) override {
    if (taken[7]) {
      int handled = 0;
      CuteQFileDeviceCall7 call = reinterpret_cast<CuteQFileDeviceCall7>(taken[7]);
      bool given = call(this, sz, &handled);
      if (handled) return given;
    }
    return QFileDevice::resize(sz);
  }

  //  Permissions QFileDevice::permissions() const
  QFileDevice::Permissions permissions() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQFileDeviceCall8 call = reinterpret_cast<CuteQFileDeviceCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return QFlags<QFileDevice::Permission>::fromInt(given);
    }
    return QFileDevice::permissions();
  }

  //  bool QFileDevice::setPermissions(Permissions permissionSpec)
  bool setPermissions(QFileDevice::Permissions permissionSpec) override {
    if (taken[9]) {
      int handled = 0;
      CuteQFileDeviceCall9 call = reinterpret_cast<CuteQFileDeviceCall9>(taken[9]);
      bool given = call(this, static_cast<int>(permissionSpec.toInt()), &handled);
      if (handled) return given;
    }
    return QFileDevice::setPermissions(permissionSpec);
  }

  //  bool QIODevice::open(QIODeviceBase::OpenMode mode)
  bool open(QIODeviceBase::OpenMode mode) override {
    if (taken[10]) {
      int handled = 0;
      CuteQFileDeviceCall10 call = reinterpret_cast<CuteQFileDeviceCall10>(taken[10]);
      bool given = call(this, static_cast<int>(mode.toInt()), &handled);
      if (handled) return given;
    }
    return QIODevice::open(mode);
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[11]) {
      int handled = 0;
      CuteQFileDeviceCall11 call = reinterpret_cast<CuteQFileDeviceCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQFileDeviceCall12 call = reinterpret_cast<CuteQFileDeviceCall12>(taken[12]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQFileDeviceCall13 call = reinterpret_cast<CuteQFileDeviceCall13>(taken[13]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQFileDeviceCall14 call = reinterpret_cast<CuteQFileDeviceCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[15]) {
      int handled = 0;
      CuteQFileDeviceCall15 call = reinterpret_cast<CuteQFileDeviceCall15>(taken[15]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[16]) {
      int handled = 0;
      CuteQFileDeviceCall16 call = reinterpret_cast<CuteQFileDeviceCall16>(taken[16]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[17]) {
      int handled = 0;
      CuteQFileDeviceCall17 call = reinterpret_cast<CuteQFileDeviceCall17>(taken[17]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQFileDeviceCall18 call = reinterpret_cast<CuteQFileDeviceCall18>(taken[18]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQFileDeviceCall19 call = reinterpret_cast<CuteQFileDeviceCall19>(taken[19]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQFileDeviceCall20 call = reinterpret_cast<CuteQFileDeviceCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQFileDeviceCall21 call = reinterpret_cast<CuteQFileDeviceCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQFileDeviceCall22 call = reinterpret_cast<CuteQFileDeviceCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[23]) {
      int handled = 0;
      CuteQFileDeviceCall23 call = reinterpret_cast<CuteQFileDeviceCall23>(taken[23]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[24]) {
      int handled = 0;
      CuteQFileDeviceCall24 call = reinterpret_cast<CuteQFileDeviceCall24>(taken[24]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

#if !defined(QT_NO_QOBJECT)
//  const QMetaObject *QFileDevice::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QFileDevice10metaObjectEv(
    const QFileDevice *self) {
  return self->metaObject();
}
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
//  QString QFileDevice::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QFileDevice2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFileDevice::tr(s, c, n));
}
#endif  // !defined(QT_NO_QOBJECT)

//  QFileDevicePrivate *QFileDevice::d_func()
extern "C" Q_DECL_EXPORT
QFileDevicePrivate *ritual_ZN11QFileDevice6d_funcEv(QFileDevice *self) {
  return self->d_func();
}

//  const QFileDevicePrivate *QFileDevice::d_func() const
extern "C" Q_DECL_EXPORT
const QFileDevicePrivate *ritual_ZNK11QFileDevice6d_funcEv(
    const QFileDevice *self) {
  return self->d_func();
}

//  QFileDevice::~QFileDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDeviceD1Ev(QFileDevice *self) {
  delete self;
}

//  FileError QFileDevice::error() const
extern "C" Q_DECL_EXPORT
QFileDevice::FileError ritual_ZNK11QFileDevice5errorEv(
    const QFileDevice *self) {
  return self->error();
}

//  void QFileDevice::unsetError()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDevice10unsetErrorEv(QFileDevice *self) {
  self->unsetError();
}

//  void QFileDevice::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFileDevice5closeEv(QFileDevice *self) {
  self->close();
}

//  bool QFileDevice::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFileDevice12isSequentialEv(const QFileDevice *self) {
  return self->isSequential();
}

//  int QFileDevice::handle() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFileDevice6handleEv(const QFileDevice *self) {
  return self->handle();
}

//  QString QFileDevice::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QFileDevice8fileNameEv(const QFileDevice *self) {
  return new QString(self->fileName());
}

//  qint64 QFileDevice::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QFileDevice3posEv(const QFileDevice *self) {
  return self->pos();
}

//  bool QFileDevice::seek(qint64 offset)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDevice4seekEx(QFileDevice *self, qint64 offset) {
  return self->seek(offset);
}

//  bool QFileDevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QFileDevice5atEndEv(const QFileDevice *self) {
  return self->atEnd();
}

//  bool QFileDevice::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDevice5flushEv(QFileDevice *self) {
  return self->flush();
}

//  qint64 QFileDevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK11QFileDevice4sizeEv(const QFileDevice *self) {
  return self->size();
}

//  bool QFileDevice::resize(qint64 sz)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDevice6resizeEx(QFileDevice *self, qint64 sz) {
  return self->resize(sz);
}

//  Permissions QFileDevice::permissions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QFileDevice11permissionsEv(const QFileDevice *self) {
  return static_cast<int>(self->permissions().toInt());
}

//  bool QFileDevice::setPermissions(Permissions permissionSpec)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDevice14setPermissionsE6QFlagsINS_10PermissionEE(
    QFileDevice *self,
    int permissionSpec) {
  return self->setPermissions(
      QFlags<QFileDevice::Permission>::fromInt(permissionSpec));
}

//  bool QFileDevice::unmap(uchar *address)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDevice5unmapEPh(QFileDevice *self, uchar *address) {
  return self->unmap(address);
}

//  QDateTime QFileDevice::fileTime(QFileDevice::FileTime time) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK11QFileDevice8fileTimeENS_8FileTimeE(
    const QFileDevice *self,
    QFileDevice::FileTime time) {
  return new QDateTime(self->fileTime(time));
}

//  bool QFileDevice::setFileTime(const QDateTime &newDate,
//      QFileDevice::FileTime fileTime)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QFileDevice11setFileTimeERK9QDateTimeNS_8FileTimeE(
    QFileDevice *self,
    const QDateTime *newDate,
    QFileDevice::FileTime fileTime) {
  return self->setFileTime(*newDate, fileTime);
}

//  QFileDevice::QFileDevice()
extern "C" Q_DECL_EXPORT
QFileDevice *ritual_ZN11QFileDeviceC1Ev() {
  return new CuteQFileDevice();
}

#if !(defined(QT_NO_QOBJECT))
//  QFileDevice::QFileDevice(QObject *parent)
extern "C" Q_DECL_EXPORT
QFileDevice *ritual_ZN11QFileDeviceC1EP7QObject(QObject *parent) {
  return new CuteQFileDevice(parent);
}
#endif  // !(defined(QT_NO_QOBJECT))

//  qint64 QFileDevice::writeData(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN11QFileDevice9writeDataEPKcx(
    QFileDevice *self,
    const char *data,
    qint64 len) {
  return self->writeData(data, len);
}

//  a Python function taken by a CuteQFileDevice, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QFileDevice(
    QFileDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQFileDevice *>(self)->take(key, call);
}

//  void QFileDevice::close()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QFileDevice5closeEv(QFileDevice *self) {
  self->QFileDevice::close();
}

//  bool QFileDevice::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QFileDevice12isSequentialEv(const QFileDevice *self) {
  return self->QFileDevice::isSequential();
}

//  QString QFileDevice::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK11QFileDevice8fileNameEv(const QFileDevice *self) {
  return new QString(self->QFileDevice::fileName());
}

//  qint64 QFileDevice::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK11QFileDevice3posEv(const QFileDevice *self) {
  return self->QFileDevice::pos();
}

//  bool QFileDevice::seek(qint64 offset)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QFileDevice4seekEx(QFileDevice *self, qint64 offset) {
  return self->QFileDevice::seek(offset);
}

//  bool QFileDevice::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QFileDevice5atEndEv(const QFileDevice *self) {
  return self->QFileDevice::atEnd();
}

//  qint64 QFileDevice::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK11QFileDevice4sizeEv(const QFileDevice *self) {
  return self->QFileDevice::size();
}

//  bool QFileDevice::resize(qint64 sz)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QFileDevice6resizeEx(QFileDevice *self, qint64 sz) {
  return self->QFileDevice::resize(sz);
}

//  Permissions QFileDevice::permissions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK11QFileDevice11permissionsEv(const QFileDevice *self) {
  return static_cast<int>(self->QFileDevice::permissions().toInt());
}

//  bool QFileDevice::setPermissions(Permissions permissionSpec)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QFileDevice14setPermissionsE6QFlagsINS_10PermissionEE(
    QFileDevice *self,
    int permissionSpec) {
  return self->QFileDevice::setPermissions(
      QFlags<QFileDevice::Permission>::fromInt(permissionSpec));
}
