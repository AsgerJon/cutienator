//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformgraphicsbuffer.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: added by hand, rituals for functions the generator
//  leaves out: 2. Kept as it is when the generator runs again.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformgraphicsbuffer.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtGui/qpixelformat.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPlatformGraphicsBuffer that Python can take functions over in. Every QPlatformGraphicsBuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPlatformGraphicsBufferCall0)(const void *, const QRect *, int *);
typedef void * (*CuteQPlatformGraphicsBufferCall1)(const void *, int *);
typedef int (*CuteQPlatformGraphicsBufferCall2)(const void *, int *);
typedef int (*CuteQPlatformGraphicsBufferCall3)(const void *, int *);
typedef bool (*CuteQPlatformGraphicsBufferCall4)(const void *, int, const QRect *, int *);
typedef void (*CuteQPlatformGraphicsBufferCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformGraphicsBufferCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformGraphicsBufferCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformGraphicsBufferCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformGraphicsBufferCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformGraphicsBufferCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformGraphicsBufferCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformGraphicsBufferCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformGraphicsBuffer : public QPlatformGraphicsBuffer {
public:
  using QPlatformGraphicsBuffer::QPlatformGraphicsBuffer;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QPlatformGraphicsBuffer13bindToTextureERK5QRect")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QPlatformGraphicsBuffer4dataEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QPlatformGraphicsBuffer12bytesPerLineEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QPlatformGraphicsBuffer6originEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QPlatformGraphicsBuffer6doLockE6QFlagsINS_10AccessTypeEERK5QRect")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QPlatformGraphicsBuffer8doUnlockEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QPlatformGraphicsBuffer::bindToTexture(const QRect &rect) const
  bool bindToTexture(const QRect &rect) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall0 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall0>(taken[0]);
      bool given = call(this, &rect, &handled);
      if (handled) return given;
    }
    return QPlatformGraphicsBuffer::bindToTexture(rect);
  }

  //  const uchar *QPlatformGraphicsBuffer::data() const
  const uchar *data() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall1 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<const uchar *>(given);
    }
    return QPlatformGraphicsBuffer::data();
  }

  //  int QPlatformGraphicsBuffer::bytesPerLine() const
  int bytesPerLine() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall2 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformGraphicsBuffer::bytesPerLine();
  }

  //  Origin QPlatformGraphicsBuffer::origin() const
  QPlatformGraphicsBuffer::Origin origin() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall3 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPlatformGraphicsBuffer::Origin>(given);
    }
    return QPlatformGraphicsBuffer::origin();
  }

  //  bool QPlatformGraphicsBuffer::doLock(AccessTypes access, const QRect
  //      &rect)
  bool doLock(
      QPlatformGraphicsBuffer::AccessTypes access,
      const QRect &rect) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall4 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall4>(taken[4]);
      bool given = call(this, static_cast<int>(access.toInt()), &rect, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QPlatformGraphicsBuffer::doUnlock()
  void doUnlock() override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall5 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall6 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall7 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall8 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall9 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall10 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall11 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformGraphicsBufferCall12 call = reinterpret_cast<CuteQPlatformGraphicsBufferCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformGraphicsBuffer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QPlatformGraphicsBuffer10metaObjectEv(
    const QPlatformGraphicsBuffer *self) {
  return self->metaObject();
}

//  void *QPlatformGraphicsBuffer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QPlatformGraphicsBuffer11qt_metacastEPKc(
    QPlatformGraphicsBuffer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformGraphicsBuffer::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QPlatformGraphicsBuffer11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformGraphicsBuffer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformGraphicsBuffer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QPlatformGraphicsBuffer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformGraphicsBuffer::tr(s, c, n));
}

//  QPlatformGraphicsBuffer::~QPlatformGraphicsBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformGraphicsBufferD1Ev(QPlatformGraphicsBuffer *self) {
  delete self;
}

//  AccessTypes QPlatformGraphicsBuffer::isLocked() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QPlatformGraphicsBuffer8isLockedEv(
    const QPlatformGraphicsBuffer *self) {
  return static_cast<int>(self->isLocked().toInt());
}

//  bool QPlatformGraphicsBuffer::lock(AccessTypes access, const QRect &rect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QPlatformGraphicsBuffer4lockE6QFlagsINS_10AccessTypeEERK5QRect(
    QPlatformGraphicsBuffer *self,
    int access,
    const QRect *rect) {
  return self->lock(
      QFlags<QPlatformGraphicsBuffer::AccessType>::fromInt(access),
      *rect);
}

//  void QPlatformGraphicsBuffer::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformGraphicsBuffer6unlockEv(
    QPlatformGraphicsBuffer *self) {
  self->unlock();
}

//  bool QPlatformGraphicsBuffer::bindToTexture(const QRect &rect) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QPlatformGraphicsBuffer13bindToTextureERK5QRect(
    const QPlatformGraphicsBuffer *self,
    const QRect *rect) {
  return self->bindToTexture(*rect);
}

//  const uchar *QPlatformGraphicsBuffer::data() const
extern "C" Q_DECL_EXPORT
const uchar *ritual_ZNK23QPlatformGraphicsBuffer4dataEv(
    const QPlatformGraphicsBuffer *self) {
  return self->data();
}

//  int QPlatformGraphicsBuffer::bytesPerLine() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QPlatformGraphicsBuffer12bytesPerLineEv(
    const QPlatformGraphicsBuffer *self) {
  return self->bytesPerLine();
}

//  int QPlatformGraphicsBuffer::byteCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QPlatformGraphicsBuffer9byteCountEv(
    const QPlatformGraphicsBuffer *self) {
  return self->byteCount();
}

//  Origin QPlatformGraphicsBuffer::origin() const
extern "C" Q_DECL_EXPORT
QPlatformGraphicsBuffer::Origin ritual_ZNK23QPlatformGraphicsBuffer6originEv(
    const QPlatformGraphicsBuffer *self) {
  return self->origin();
}

//  QSize QPlatformGraphicsBuffer::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK23QPlatformGraphicsBuffer4sizeEv(
    const QPlatformGraphicsBuffer *self) {
  return new QSize(self->size());
}

//  QPixelFormat QPlatformGraphicsBuffer::format() const
extern "C" Q_DECL_EXPORT
QPixelFormat *ritual_ZNK23QPlatformGraphicsBuffer6formatEv(
    const QPlatformGraphicsBuffer *self) {
  return new QPixelFormat(self->format());
}

//  void QPlatformGraphicsBuffer::unlocked(AccessTypes previousAccessTypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformGraphicsBuffer8unlockedE6QFlagsINS_10AccessTypeEE(
    QPlatformGraphicsBuffer *self,
    int previousAccessTypes) {
  self->unlocked(
      QFlags<QPlatformGraphicsBuffer::AccessType>::fromInt(previousAccessTypes));
}

//  QPlatformGraphicsBuffer::QPlatformGraphicsBuffer(const QSize &size, const
//      QPixelFormat &format)
extern "C" Q_DECL_EXPORT
QPlatformGraphicsBuffer *ritual_ZN23QPlatformGraphicsBufferC1ERK5QSizeRK12QPixelFormat(
    const QSize *size,
    const QPixelFormat *format) {
  return new CuteQPlatformGraphicsBuffer(*size, *format);
}

//  bool QPlatformGraphicsBuffer::doLock(AccessTypes access, const QRect
//      &rect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QPlatformGraphicsBuffer6doLockE6QFlagsINS_10AccessTypeEERK5QRect(
    QPlatformGraphicsBuffer *self,
    int access,
    const QRect *rect) {
  return self->doLock(
      QFlags<QPlatformGraphicsBuffer::AccessType>::fromInt(access),
      *rect);
}

//  void QPlatformGraphicsBuffer::doUnlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformGraphicsBuffer8doUnlockEv(
    QPlatformGraphicsBuffer *self) {
  self->doUnlock();
}

//  a Python function taken by a CuteQPlatformGraphicsBuffer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformGraphicsBuffer(
    QPlatformGraphicsBuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformGraphicsBuffer *>(self)->take(key, call);
}

//  bool QPlatformGraphicsBuffer::bindToTexture(const QRect &rect) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK23QPlatformGraphicsBuffer13bindToTextureERK5QRect(
    const QPlatformGraphicsBuffer *self,
    const QRect *rect) {
  return self->QPlatformGraphicsBuffer::bindToTexture(*rect);
}

//  const uchar *QPlatformGraphicsBuffer::data() const
extern "C" Q_DECL_EXPORT
const uchar *ritual_own_ZNK23QPlatformGraphicsBuffer4dataEv(
    const QPlatformGraphicsBuffer *self) {
  return self->QPlatformGraphicsBuffer::data();
}

//  int QPlatformGraphicsBuffer::bytesPerLine() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QPlatformGraphicsBuffer12bytesPerLineEv(
    const QPlatformGraphicsBuffer *self) {
  return self->QPlatformGraphicsBuffer::bytesPerLine();
}

//  Origin QPlatformGraphicsBuffer::origin() const
extern "C" Q_DECL_EXPORT
QPlatformGraphicsBuffer::Origin ritual_own_ZNK23QPlatformGraphicsBuffer6originEv(
    const QPlatformGraphicsBuffer *self) {
  return self->QPlatformGraphicsBuffer::origin();
}

//  uchar *QPlatformGraphicsBuffer::data()
extern "C" Q_DECL_EXPORT
uchar *ritual_ZN23QPlatformGraphicsBuffer4dataEv(
    QPlatformGraphicsBuffer *self) {
  return self->data();
}

//  uchar *QPlatformGraphicsBuffer::data()
extern "C" Q_DECL_EXPORT
uchar *ritual_own_ZN23QPlatformGraphicsBuffer4dataEv(
    QPlatformGraphicsBuffer *self) {
  return self->QPlatformGraphicsBuffer::data();
}
