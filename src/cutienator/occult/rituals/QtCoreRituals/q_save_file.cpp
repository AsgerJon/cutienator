//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsavefile.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsavefile.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSaveFile that Python can take functions over in. Every QSaveFile
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSaveFileCall0)(const void *, int *);
typedef qint64 (*CuteQSaveFileCall1)(const void *, int *);
typedef bool (*CuteQSaveFileCall2)(const void *, qint64, int *);
typedef bool (*CuteQSaveFileCall3)(const void *, int *);
typedef qint64 (*CuteQSaveFileCall4)(const void *, int *);
typedef bool (*CuteQSaveFileCall5)(const void *, qint64, int *);
typedef bool (*CuteQSaveFileCall6)(const void *, int *);
typedef qint64 (*CuteQSaveFileCall7)(const void *, int *);
typedef qint64 (*CuteQSaveFileCall8)(const void *, int *);
typedef bool (*CuteQSaveFileCall9)(const void *, int *);
typedef bool (*CuteQSaveFileCall10)(const void *, int, int *);
typedef bool (*CuteQSaveFileCall11)(const void *, int, int *);
typedef qint64 (*CuteQSaveFileCall12)(const void *, qint64, int *);
typedef bool (*CuteQSaveFileCall13)(const void *, QEvent *, int *);
typedef bool (*CuteQSaveFileCall14)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQSaveFileCall15)(const void *, QTimerEvent *, int *);
typedef void (*CuteQSaveFileCall16)(const void *, QChildEvent *, int *);
typedef void (*CuteQSaveFileCall17)(const void *, QEvent *, int *);
typedef void (*CuteQSaveFileCall18)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQSaveFileCall19)(const void *, const QMetaMethod *, int *);
class CuteQSaveFile : public QSaveFile {
public:
  using QSaveFile::QSaveFile;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QIODevice12isSequentialEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice3posEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice4seekEx")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice5atEndEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice4sizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QFileDevice6resizeEx")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice5resetEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice14bytesAvailableEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice12bytesToWriteEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QIODevice11canReadLineEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice16waitForReadyReadEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice19waitForBytesWrittenEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN9QIODevice8skipDataEx")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[19] = call;
      return true;
    }
    return false;
  }

  //  bool QFileDevice::isSequential() const
  bool isSequential() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSaveFileCall0 call = reinterpret_cast<CuteQSaveFileCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::isSequential();
  }

  //  qint64 QFileDevice::pos() const
  qint64 pos() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSaveFileCall1 call = reinterpret_cast<CuteQSaveFileCall1>(taken[1]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::pos();
  }

  //  bool QFileDevice::seek(qint64 offset)
  bool seek(qint64 offset) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSaveFileCall2 call = reinterpret_cast<CuteQSaveFileCall2>(taken[2]);
      bool given = call(this, offset, &handled);
      if (handled) return given;
    }
    return QFileDevice::seek(offset);
  }

  //  bool QFileDevice::atEnd() const
  bool atEnd() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSaveFileCall3 call = reinterpret_cast<CuteQSaveFileCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::atEnd();
  }

  //  qint64 QFileDevice::size() const
  qint64 size() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSaveFileCall4 call = reinterpret_cast<CuteQSaveFileCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QFileDevice::size();
  }

  //  bool QFileDevice::resize(qint64 sz)
  bool resize(qint64 sz) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSaveFileCall5 call = reinterpret_cast<CuteQSaveFileCall5>(taken[5]);
      bool given = call(this, sz, &handled);
      if (handled) return given;
    }
    return QFileDevice::resize(sz);
  }

  //  bool QIODevice::reset()
  bool reset() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSaveFileCall6 call = reinterpret_cast<CuteQSaveFileCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::reset();
  }

  //  qint64 QIODevice::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQSaveFileCall7 call = reinterpret_cast<CuteQSaveFileCall7>(taken[7]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesAvailable();
  }

  //  qint64 QIODevice::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSaveFileCall8 call = reinterpret_cast<CuteQSaveFileCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::bytesToWrite();
  }

  //  bool QIODevice::canReadLine() const
  bool canReadLine() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQSaveFileCall9 call = reinterpret_cast<CuteQSaveFileCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QIODevice::canReadLine();
  }

  //  bool QIODevice::waitForReadyRead(int msecs)
  bool waitForReadyRead(int msecs) override {
    if (taken[10]) {
      int handled = 0;
      CuteQSaveFileCall10 call = reinterpret_cast<CuteQSaveFileCall10>(taken[10]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForReadyRead(msecs);
  }

  //  bool QIODevice::waitForBytesWritten(int msecs)
  bool waitForBytesWritten(int msecs) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSaveFileCall11 call = reinterpret_cast<CuteQSaveFileCall11>(taken[11]);
      bool given = call(this, msecs, &handled);
      if (handled) return given;
    }
    return QIODevice::waitForBytesWritten(msecs);
  }

  //  qint64 QIODevice::skipData(qint64 maxSize)
  qint64 skipData(qint64 maxSize) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSaveFileCall12 call = reinterpret_cast<CuteQSaveFileCall12>(taken[12]);
      qint64 given = call(this, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevice::skipData(maxSize);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSaveFileCall13 call = reinterpret_cast<CuteQSaveFileCall13>(taken[13]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQSaveFileCall14 call = reinterpret_cast<CuteQSaveFileCall14>(taken[14]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSaveFileCall15 call = reinterpret_cast<CuteQSaveFileCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQSaveFileCall16 call = reinterpret_cast<CuteQSaveFileCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSaveFileCall17 call = reinterpret_cast<CuteQSaveFileCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSaveFileCall18 call = reinterpret_cast<CuteQSaveFileCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSaveFileCall19 call = reinterpret_cast<CuteQSaveFileCall19>(taken[19]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QSaveFile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QSaveFile10metaObjectEv(
    const QSaveFile *self) {
  return self->metaObject();
}

//  QString QSaveFile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QSaveFile2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSaveFile::tr(s, c, n));
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

//  a Python function taken by a CuteQSaveFile, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSaveFile(QSaveFile *self, const char *key, void *call) {
  return static_cast<CuteQSaveFile *>(self)->take(key, call);
}
