//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qrandomaccessasyncfile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QRandomAccessAsyncFile that Python can take functions over in. Every QRandomAccessAsyncFile
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRandomAccessAsyncFileCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRandomAccessAsyncFileCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRandomAccessAsyncFileCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRandomAccessAsyncFileCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRandomAccessAsyncFileCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRandomAccessAsyncFileCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRandomAccessAsyncFileCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRandomAccessAsyncFile : public QRandomAccessAsyncFile {
public:
  using QRandomAccessAsyncFile::QRandomAccessAsyncFile;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileCall0 call = reinterpret_cast<CuteQRandomAccessAsyncFileCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileCall1 call = reinterpret_cast<CuteQRandomAccessAsyncFileCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileCall2 call = reinterpret_cast<CuteQRandomAccessAsyncFileCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileCall3 call = reinterpret_cast<CuteQRandomAccessAsyncFileCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileCall4 call = reinterpret_cast<CuteQRandomAccessAsyncFileCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileCall5 call = reinterpret_cast<CuteQRandomAccessAsyncFileCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRandomAccessAsyncFileCall6 call = reinterpret_cast<CuteQRandomAccessAsyncFileCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRandomAccessAsyncFile::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QRandomAccessAsyncFile10metaObjectEv(
    const QRandomAccessAsyncFile *self) {
  return self->metaObject();
}

//  QString QRandomAccessAsyncFile::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QRandomAccessAsyncFile2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRandomAccessAsyncFile::tr(s, c, n));
}

//  QRandomAccessAsyncFile::QRandomAccessAsyncFile(QObject *parent)
extern "C" Q_DECL_EXPORT
QRandomAccessAsyncFile *ritual_ZN22QRandomAccessAsyncFileC1EP7QObject(
    QObject *parent) {
  return new CuteQRandomAccessAsyncFile(parent);
}

//  QRandomAccessAsyncFile::~QRandomAccessAsyncFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QRandomAccessAsyncFileD1Ev(QRandomAccessAsyncFile *self) {
  delete self;
}

//  void QRandomAccessAsyncFile::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QRandomAccessAsyncFile5closeEv(
    QRandomAccessAsyncFile *self) {
  self->close();
}

//  qint64 QRandomAccessAsyncFile::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK22QRandomAccessAsyncFile4sizeEv(
    const QRandomAccessAsyncFile *self) {
  return self->size();
}

//  QIOOperation *QRandomAccessAsyncFile::open(const QString &filePath,
//      QIODeviceBase::OpenMode mode)
extern "C" Q_DECL_EXPORT
QIOOperation *ritual_ZN22QRandomAccessAsyncFile4openERK7QString6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QRandomAccessAsyncFile *self,
    const QString *filePath,
    int mode) {
  return self->open(
      *filePath,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}

//  QIOOperation *QRandomAccessAsyncFile::flush()
extern "C" Q_DECL_EXPORT
QIOOperation *ritual_ZN22QRandomAccessAsyncFile5flushEv(
    QRandomAccessAsyncFile *self) {
  return self->flush();
}

//  QIOReadOperation *QRandomAccessAsyncFile::read(qint64 offset, qint64
//      maxSize)
extern "C" Q_DECL_EXPORT
QIOReadOperation *ritual_ZN22QRandomAccessAsyncFile4readExx(
    QRandomAccessAsyncFile *self,
    qint64 offset,
    qint64 maxSize) {
  return self->read(offset, maxSize);
}

//  QIOWriteOperation *QRandomAccessAsyncFile::write(qint64 offset, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
QIOWriteOperation *ritual_ZN22QRandomAccessAsyncFile5writeExRK10QByteArray(
    QRandomAccessAsyncFile *self,
    qint64 offset,
    const QByteArray *data) {
  return self->write(offset, *data);
}

//  QRandomAccessAsyncFilePrivate *QRandomAccessAsyncFile::d_func()
extern "C" Q_DECL_EXPORT
QRandomAccessAsyncFilePrivate *ritual_ZN22QRandomAccessAsyncFile6d_funcEv(
    QRandomAccessAsyncFile *self) {
  return self->d_func();
}

//  const QRandomAccessAsyncFilePrivate *QRandomAccessAsyncFile::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QRandomAccessAsyncFilePrivate *ritual_ZNK22QRandomAccessAsyncFile6d_funcEv(
    const QRandomAccessAsyncFile *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQRandomAccessAsyncFile, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRandomAccessAsyncFile(
    QRandomAccessAsyncFile *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRandomAccessAsyncFile *>(self)->take(key, call);
}
