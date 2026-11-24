//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(async_io)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QRandomAccessAsyncFileBackend that Python can take functions over in. Every QRandomAccessAsyncFileBackend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQRandomAccessAsyncFileBackendCall0)(const void *, int *);
typedef void (*CuteQRandomAccessAsyncFileBackendCall1)(const void *, QIOOperation *, int *);
typedef void (*CuteQRandomAccessAsyncFileBackendCall2)(const void *, int *);
typedef qint64 (*CuteQRandomAccessAsyncFileBackendCall3)(const void *, int *);
typedef void * (*CuteQRandomAccessAsyncFileBackendCall4)(const void *, const QString *, int, int *);
typedef void * (*CuteQRandomAccessAsyncFileBackendCall5)(const void *, int *);
typedef void * (*CuteQRandomAccessAsyncFileBackendCall6)(const void *, qint64, qint64, int *);
typedef void * (*CuteQRandomAccessAsyncFileBackendCall7)(const void *, qint64, const QByteArray *, int *);
class CuteQRandomAccessAsyncFileBackend : public QRandomAccessAsyncFileBackend {
public:
  using QRandomAccessAsyncFileBackend::QRandomAccessAsyncFileBackend;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend4initEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend13cancelAndWaitEP12QIOOperation")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend5closeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29QRandomAccessAsyncFileBackend4sizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend4openERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend5flushEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend4readExx")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QRandomAccessAsyncFileBackend5writeExRK10QByteArray")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  bool QRandomAccessAsyncFileBackend::init()
  bool init() override {
    if (taken[0]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileBackendCall0 call = reinterpret_cast<CuteQRandomAccessAsyncFileBackendCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QRandomAccessAsyncFileBackend::cancelAndWait(QIOOperation *op)
  void cancelAndWait(QIOOperation *op) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileBackendCall1 call = reinterpret_cast<CuteQRandomAccessAsyncFileBackendCall1>(taken[1]);
      call(this, op, &handled);
      if (handled) return;
    }
  }

  //  void QRandomAccessAsyncFileBackend::close()
  void close() override {
    if (taken[2]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileBackendCall2 call = reinterpret_cast<CuteQRandomAccessAsyncFileBackendCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  qint64 QRandomAccessAsyncFileBackend::size() const
  qint64 size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileBackendCall3 call = reinterpret_cast<CuteQRandomAccessAsyncFileBackendCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QIOOperation *QRandomAccessAsyncFileBackend::open(const QString
  //      &path, QIODeviceBase::OpenMode mode)
  QIOOperation *open(
      const QString &path,
      QIODeviceBase::OpenMode mode) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileBackendCall4 call = reinterpret_cast<CuteQRandomAccessAsyncFileBackendCall4>(taken[4]);
      void * given = call(this, &path, static_cast<int>(mode.toInt()), &handled);
      if (handled) return static_cast<QIOOperation *>(given);
    }
    return {};
  }

  //  QIOOperation *QRandomAccessAsyncFileBackend::flush()
  QIOOperation *flush() override {
    if (taken[5]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileBackendCall5 call = reinterpret_cast<CuteQRandomAccessAsyncFileBackendCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QIOOperation *>(given);
    }
    return {};
  }

  //  QIOReadOperation *QRandomAccessAsyncFileBackend::read(qint64 offset,
  //      qint64 maxSize)
  QIOReadOperation *read(qint64 offset, qint64 maxSize) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileBackendCall6 call = reinterpret_cast<CuteQRandomAccessAsyncFileBackendCall6>(taken[6]);
      void * given = call(this, offset, maxSize, &handled);
      if (handled) return static_cast<QIOReadOperation *>(given);
    }
    return {};
  }

  //  QIOWriteOperation *QRandomAccessAsyncFileBackend::write(qint64
  //      offset, const QByteArray &data)
  QIOWriteOperation *write(qint64 offset, const QByteArray &data) override {
    if (taken[7]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileBackendCall7 call = reinterpret_cast<CuteQRandomAccessAsyncFileBackendCall7>(taken[7]);
      void * given = call(this, offset, &data, &handled);
      if (handled) return static_cast<QIOWriteOperation *>(given);
    }
    return {};
  }
};

//  QRandomAccessAsyncFileBackend::~QRandomAccessAsyncFileBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QRandomAccessAsyncFileBackendD1Ev(
    QRandomAccessAsyncFileBackend *self) {
  delete self;
}

//  bool QRandomAccessAsyncFileBackend::init()
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QRandomAccessAsyncFileBackend4initEv(
    QRandomAccessAsyncFileBackend *self) {
  return self->init();
}

//  void QRandomAccessAsyncFileBackend::cancelAndWait(QIOOperation *op)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QRandomAccessAsyncFileBackend13cancelAndWaitEP12QIOOperation(
    QRandomAccessAsyncFileBackend *self,
    QIOOperation *op) {
  self->cancelAndWait(op);
}

//  void QRandomAccessAsyncFileBackend::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QRandomAccessAsyncFileBackend5closeEv(
    QRandomAccessAsyncFileBackend *self) {
  self->close();
}

//  qint64 QRandomAccessAsyncFileBackend::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK29QRandomAccessAsyncFileBackend4sizeEv(
    const QRandomAccessAsyncFileBackend *self) {
  return self->size();
}

//  QIOOperation *QRandomAccessAsyncFileBackend::open(const QString &path,
//      QIODeviceBase::OpenMode mode)
extern "C" Q_DECL_EXPORT
QIOOperation *ritual_ZN29QRandomAccessAsyncFileBackend4openERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QRandomAccessAsyncFileBackend *self,
    const QString *path,
    int mode) {
  return self->open(
      *path,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  QIOOperation *QRandomAccessAsyncFileBackend::flush()
extern "C" Q_DECL_EXPORT
QIOOperation *ritual_ZN29QRandomAccessAsyncFileBackend5flushEv(
    QRandomAccessAsyncFileBackend *self) {
  return self->flush();
}

//  QIOReadOperation *QRandomAccessAsyncFileBackend::read(qint64 offset,
//      qint64 maxSize)
extern "C" Q_DECL_EXPORT
QIOReadOperation *ritual_ZN29QRandomAccessAsyncFileBackend4readExx(
    QRandomAccessAsyncFileBackend *self,
    qint64 offset,
    qint64 maxSize) {
  return self->read(offset, maxSize);
}

//  QIOWriteOperation *QRandomAccessAsyncFileBackend::write(qint64 offset,
//      const QByteArray &data)
extern "C" Q_DECL_EXPORT
QIOWriteOperation *ritual_ZN29QRandomAccessAsyncFileBackend5writeExRK10QByteArray(
    QRandomAccessAsyncFileBackend *self,
    qint64 offset,
    const QByteArray *data) {
  return self->write(offset, *data);
}

//  a Python function taken by a CuteQRandomAccessAsyncFileBackend, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRandomAccessAsyncFileBackend(
    QRandomAccessAsyncFileBackend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRandomAccessAsyncFileBackend *>(self)->take(key, call);
}

#endif  // QT_CONFIG(async_io)
