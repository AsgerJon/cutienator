//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsharedmemory.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(sharedmemory)
#include <QtCore/qsharedmemory.h>
#include <QtCore/qstring.h>
#include <QtCore/qtipccommon.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QSharedMemory that Python can take functions over in. Every QSharedMemory
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSharedMemoryCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSharedMemoryCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSharedMemoryCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSharedMemoryCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSharedMemoryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSharedMemoryCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSharedMemoryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSharedMemory : public QSharedMemory {
public:
  using QSharedMemory::QSharedMemory;
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
      CuteQSharedMemoryCall0 call = reinterpret_cast<CuteQSharedMemoryCall0>(taken[0]);
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
      CuteQSharedMemoryCall1 call = reinterpret_cast<CuteQSharedMemoryCall1>(taken[1]);
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
      CuteQSharedMemoryCall2 call = reinterpret_cast<CuteQSharedMemoryCall2>(taken[2]);
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
      CuteQSharedMemoryCall3 call = reinterpret_cast<CuteQSharedMemoryCall3>(taken[3]);
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
      CuteQSharedMemoryCall4 call = reinterpret_cast<CuteQSharedMemoryCall4>(taken[4]);
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
      CuteQSharedMemoryCall5 call = reinterpret_cast<CuteQSharedMemoryCall5>(taken[5]);
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
      CuteQSharedMemoryCall6 call = reinterpret_cast<CuteQSharedMemoryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSharedMemory::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QSharedMemory10metaObjectEv(
    const QSharedMemory *self) {
  return self->metaObject();
}

//  QString QSharedMemory::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QSharedMemory2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSharedMemory::tr(s, c, n));
}

//  QSharedMemoryPrivate *QSharedMemory::d_func()
extern "C" Q_DECL_EXPORT
QSharedMemoryPrivate *ritual_ZN13QSharedMemory6d_funcEv(
    QSharedMemory *self) {
  return self->d_func();
}

//  const QSharedMemoryPrivate *QSharedMemory::d_func() const
extern "C" Q_DECL_EXPORT
const QSharedMemoryPrivate *ritual_ZNK13QSharedMemory6d_funcEv(
    const QSharedMemory *self) {
  return self->d_func();
}

//  QSharedMemory::QSharedMemory(QObject *parent)
extern "C" Q_DECL_EXPORT
QSharedMemory *ritual_ZN13QSharedMemoryC1EP7QObject(QObject *parent) {
  return new CuteQSharedMemory(parent);
}

//  QSharedMemory::QSharedMemory(const QNativeIpcKey &key, QObject *parent)
extern "C" Q_DECL_EXPORT
QSharedMemory *ritual_ZN13QSharedMemoryC1ERK13QNativeIpcKeyP7QObject(
    const QNativeIpcKey *key,
    QObject *parent) {
  return new CuteQSharedMemory(*key, parent);
}

//  QSharedMemory::~QSharedMemory()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSharedMemoryD1Ev(QSharedMemory *self) {
  delete self;
}

//  QSharedMemory::QSharedMemory(const QString &key, QObject *parent)
extern "C" Q_DECL_EXPORT
QSharedMemory *ritual_ZN13QSharedMemoryC1ERK7QStringP7QObject(
    const QString *key,
    QObject *parent) {
  return new CuteQSharedMemory(*key, parent);
}

//  void QSharedMemory::setKey(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSharedMemory6setKeyERK7QString(
    QSharedMemory *self,
    const QString *key) {
  self->setKey(*key);
}

//  QString QSharedMemory::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QSharedMemory3keyEv(const QSharedMemory *self) {
  return new QString(self->key());
}

//  void QSharedMemory::setNativeKey(const QNativeIpcKey &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSharedMemory12setNativeKeyERK13QNativeIpcKey(
    QSharedMemory *self,
    const QNativeIpcKey *key) {
  self->setNativeKey(*key);
}

//  void QSharedMemory::setNativeKey(const QString &key, QNativeIpcKey::Type
//      type)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSharedMemory12setNativeKeyERK7QStringN13QNativeIpcKey4TypeE(
    QSharedMemory *self,
    const QString *key,
    QNativeIpcKey::Type type) {
  self->setNativeKey(*key, type);
}

//  QString QSharedMemory::nativeKey() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QSharedMemory9nativeKeyEv(const QSharedMemory *self) {
  return new QString(self->nativeKey());
}

//  QNativeIpcKey QSharedMemory::nativeIpcKey() const
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZNK13QSharedMemory12nativeIpcKeyEv(
    const QSharedMemory *self) {
  return new QNativeIpcKey(self->nativeIpcKey());
}

//  bool QSharedMemory::create(qsizetype size, AccessMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSharedMemory6createExNS_10AccessModeE(
    QSharedMemory *self,
    qsizetype size,
    QSharedMemory::AccessMode mode) {
  return self->create(size, mode);
}

//  qsizetype QSharedMemory::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QSharedMemory4sizeEv(const QSharedMemory *self) {
  return self->size();
}

//  bool QSharedMemory::attach(AccessMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSharedMemory6attachENS_10AccessModeE(
    QSharedMemory *self,
    QSharedMemory::AccessMode mode) {
  return self->attach(mode);
}

//  bool QSharedMemory::isAttached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QSharedMemory10isAttachedEv(const QSharedMemory *self) {
  return self->isAttached();
}

//  bool QSharedMemory::detach()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSharedMemory6detachEv(QSharedMemory *self) {
  return self->detach();
}

#if QT_CONFIG(systemsemaphore)
//  bool QSharedMemory::lock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSharedMemory4lockEv(QSharedMemory *self) {
  return self->lock();
}
#endif  // QT_CONFIG(systemsemaphore)

#if QT_CONFIG(systemsemaphore)
//  bool QSharedMemory::unlock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSharedMemory6unlockEv(QSharedMemory *self) {
  return self->unlock();
}
#endif  // QT_CONFIG(systemsemaphore)

//  SharedMemoryError QSharedMemory::error() const
extern "C" Q_DECL_EXPORT
QSharedMemory::SharedMemoryError ritual_ZNK13QSharedMemory5errorEv(
    const QSharedMemory *self) {
  return self->error();
}

//  QString QSharedMemory::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QSharedMemory11errorStringEv(
    const QSharedMemory *self) {
  return new QString(self->errorString());
}

//  bool QSharedMemory::isKeyTypeSupported(QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QSharedMemory18isKeyTypeSupportedEN13QNativeIpcKey4TypeE(
    QNativeIpcKey::Type type) {
  return QSharedMemory::isKeyTypeSupported(type);
}

//  QNativeIpcKey QSharedMemory::platformSafeKey(const QString &key,
//      QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZN13QSharedMemory15platformSafeKeyERK7QStringN13QNativeIpcKey4TypeE(
    const QString *key,
    QNativeIpcKey::Type type) {
  return new QNativeIpcKey(QSharedMemory::platformSafeKey(*key, type));
}

//  QNativeIpcKey QSharedMemory::legacyNativeKey(const QString &key,
//      QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
QNativeIpcKey *ritual_ZN13QSharedMemory15legacyNativeKeyERK7QStringN13QNativeIpcKey4TypeE(
    const QString *key,
    QNativeIpcKey::Type type) {
  return new QNativeIpcKey(QSharedMemory::legacyNativeKey(*key, type));
}

//  a Python function taken by a CuteQSharedMemory, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSharedMemory(
    QSharedMemory *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSharedMemory *>(self)->take(key, call);
}

#endif  // QT_CONFIG(sharedmemory)
