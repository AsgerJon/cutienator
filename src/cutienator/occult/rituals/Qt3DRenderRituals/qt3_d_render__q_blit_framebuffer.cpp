//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qblitframebuffer.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qblitframebuffer.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QBlitFramebuffer that Python can take functions over in. Every Qt3DRender::QBlitFramebuffer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QBlitFramebufferCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QBlitFramebufferCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QBlitFramebufferCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QBlitFramebufferCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QBlitFramebufferCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QBlitFramebufferCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QBlitFramebufferCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QBlitFramebuffer : public Qt3DRender::QBlitFramebuffer {
public:
  using Qt3DRender::QBlitFramebuffer::QBlitFramebuffer;
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
      CuteQt3DRender_QBlitFramebufferCall0 call = reinterpret_cast<CuteQt3DRender_QBlitFramebufferCall0>(taken[0]);
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
      CuteQt3DRender_QBlitFramebufferCall1 call = reinterpret_cast<CuteQt3DRender_QBlitFramebufferCall1>(taken[1]);
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
      CuteQt3DRender_QBlitFramebufferCall2 call = reinterpret_cast<CuteQt3DRender_QBlitFramebufferCall2>(taken[2]);
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
      CuteQt3DRender_QBlitFramebufferCall3 call = reinterpret_cast<CuteQt3DRender_QBlitFramebufferCall3>(taken[3]);
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
      CuteQt3DRender_QBlitFramebufferCall4 call = reinterpret_cast<CuteQt3DRender_QBlitFramebufferCall4>(taken[4]);
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
      CuteQt3DRender_QBlitFramebufferCall5 call = reinterpret_cast<CuteQt3DRender_QBlitFramebufferCall5>(taken[5]);
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
      CuteQt3DRender_QBlitFramebufferCall6 call = reinterpret_cast<CuteQt3DRender_QBlitFramebufferCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QBlitFramebuffer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender16QBlitFramebuffer10metaObjectEv(
    const Qt3DRender::QBlitFramebuffer *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QBlitFramebuffer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender16QBlitFramebuffer11qt_metacastEPKc(
    Qt3DRender::QBlitFramebuffer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QBlitFramebuffer::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender16QBlitFramebuffer11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QBlitFramebuffer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QBlitFramebuffer::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender16QBlitFramebuffer2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QBlitFramebuffer::tr(s, c, n));
}

//  Qt3DRender::QBlitFramebuffer::QBlitFramebuffer(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlitFramebuffer *ritual_ZN10Qt3DRender16QBlitFramebufferC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QBlitFramebuffer(parent);
}

//  Qt3DRender::QBlitFramebuffer::~QBlitFramebuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebufferD1Ev(
    Qt3DRender::QBlitFramebuffer *self) {
  delete self;
}

//  QRenderTarget *Qt3DRender::QBlitFramebuffer::source() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTarget *ritual_ZNK10Qt3DRender16QBlitFramebuffer6sourceEv(
    const Qt3DRender::QBlitFramebuffer *self) {
  return self->source();
}

//  QRenderTarget *Qt3DRender::QBlitFramebuffer::destination() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTarget *ritual_ZNK10Qt3DRender16QBlitFramebuffer11destinationEv(
    const Qt3DRender::QBlitFramebuffer *self) {
  return self->destination();
}

//  QRectF Qt3DRender::QBlitFramebuffer::sourceRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10Qt3DRender16QBlitFramebuffer10sourceRectEv(
    const Qt3DRender::QBlitFramebuffer *self) {
  return new QRectF(self->sourceRect());
}

//  QRectF Qt3DRender::QBlitFramebuffer::destinationRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10Qt3DRender16QBlitFramebuffer15destinationRectEv(
    const Qt3DRender::QBlitFramebuffer *self) {
  return new QRectF(self->destinationRect());
}

//  Qt3DRender::QRenderTargetOutput::AttachmentPoint
//      Qt3DRender::QBlitFramebuffer::sourceAttachmentPoint() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetOutput::AttachmentPoint ritual_ZNK10Qt3DRender16QBlitFramebuffer21sourceAttachmentPointEv(
    const Qt3DRender::QBlitFramebuffer *self) {
  return self->sourceAttachmentPoint();
}

//  Qt3DRender::QRenderTargetOutput::AttachmentPoint
//      Qt3DRender::QBlitFramebuffer::destinationAttachmentPoint() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetOutput::AttachmentPoint ritual_ZNK10Qt3DRender16QBlitFramebuffer26destinationAttachmentPointEv(
    const Qt3DRender::QBlitFramebuffer *self) {
  return self->destinationAttachmentPoint();
}

//  InterpolationMethod Qt3DRender::QBlitFramebuffer::interpolationMethod()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlitFramebuffer::InterpolationMethod ritual_ZNK10Qt3DRender16QBlitFramebuffer19interpolationMethodEv(
    const Qt3DRender::QBlitFramebuffer *self) {
  return self->interpolationMethod();
}

//  void Qt3DRender::QBlitFramebuffer::setSource(QRenderTarget *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer9setSourceEPNS_13QRenderTargetE(
    Qt3DRender::QBlitFramebuffer *self,
    Qt3DRender::QRenderTarget *source) {
  self->setSource(source);
}

//  void Qt3DRender::QBlitFramebuffer::setDestination(QRenderTarget
//      *destination)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer14setDestinationEPNS_13QRenderTargetE(
    Qt3DRender::QBlitFramebuffer *self,
    Qt3DRender::QRenderTarget *destination) {
  self->setDestination(destination);
}

//  void Qt3DRender::QBlitFramebuffer::setSourceRect(const QRectF
//      &sourceRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer13setSourceRectERK6QRectF(
    Qt3DRender::QBlitFramebuffer *self,
    const QRectF *sourceRect) {
  self->setSourceRect(*sourceRect);
}

//  void Qt3DRender::QBlitFramebuffer::setDestinationRect(const QRectF
//      &destinationRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer18setDestinationRectERK6QRectF(
    Qt3DRender::QBlitFramebuffer *self,
    const QRectF *destinationRect) {
  self->setDestinationRect(*destinationRect);
}

//  void Qt3DRender::QBlitFramebuffer::setSourceAttachmentPoint(Qt3DRender::Q
//      RenderTargetOutput::AttachmentPoint sourceAttachmentPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer24setSourceAttachmentPointENS_19QRenderTargetOutput15AttachmentPointE(
    Qt3DRender::QBlitFramebuffer *self,
    Qt3DRender::QRenderTargetOutput::AttachmentPoint sourceAttachmentPoint) {
  self->setSourceAttachmentPoint(sourceAttachmentPoint);
}

//  void Qt3DRender::QBlitFramebuffer::setDestinationAttachmentPoint(Qt3DRend
//      er::QRenderTargetOutput::AttachmentPoint destinationAttachmentPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer29setDestinationAttachmentPointENS_19QRenderTargetOutput15AttachmentPointE(
    Qt3DRender::QBlitFramebuffer *self,
    Qt3DRender::QRenderTargetOutput::AttachmentPoint destinationAttachmentPoint) {
  self->setDestinationAttachmentPoint(destinationAttachmentPoint);
}

//  void
//      Qt3DRender::QBlitFramebuffer::setInterpolationMethod(InterpolationMet
//      hod interpolationMethod)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer22setInterpolationMethodENS0_19InterpolationMethodE(
    Qt3DRender::QBlitFramebuffer *self,
    Qt3DRender::QBlitFramebuffer::InterpolationMethod interpolationMethod) {
  self->setInterpolationMethod(interpolationMethod);
}

//  void Qt3DRender::QBlitFramebuffer::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer13sourceChangedEv(
    Qt3DRender::QBlitFramebuffer *self) {
  self->sourceChanged();
}

//  void Qt3DRender::QBlitFramebuffer::destinationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer18destinationChangedEv(
    Qt3DRender::QBlitFramebuffer *self) {
  self->destinationChanged();
}

//  void Qt3DRender::QBlitFramebuffer::sourceRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer17sourceRectChangedEv(
    Qt3DRender::QBlitFramebuffer *self) {
  self->sourceRectChanged();
}

//  void Qt3DRender::QBlitFramebuffer::destinationRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer22destinationRectChangedEv(
    Qt3DRender::QBlitFramebuffer *self) {
  self->destinationRectChanged();
}

//  void Qt3DRender::QBlitFramebuffer::sourceAttachmentPointChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer28sourceAttachmentPointChangedEv(
    Qt3DRender::QBlitFramebuffer *self) {
  self->sourceAttachmentPointChanged();
}

//  void Qt3DRender::QBlitFramebuffer::destinationAttachmentPointChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer33destinationAttachmentPointChangedEv(
    Qt3DRender::QBlitFramebuffer *self) {
  self->destinationAttachmentPointChanged();
}

//  void Qt3DRender::QBlitFramebuffer::interpolationMethodChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QBlitFramebuffer26interpolationMethodChangedEv(
    Qt3DRender::QBlitFramebuffer *self) {
  self->interpolationMethodChanged();
}

//  Qt3DRender::QBlitFramebuffer::QBlitFramebuffer(QBlitFramebufferPrivate
//      &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlitFramebuffer *ritual_ZN10Qt3DRender16QBlitFramebufferC1ERNS_23QBlitFramebufferPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QBlitFramebufferPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QBlitFramebuffer(*dd, parent);
}

//  QBlitFramebufferPrivate *Qt3DRender::QBlitFramebuffer::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QBlitFramebufferPrivate *ritual_ZN10Qt3DRender16QBlitFramebuffer6d_funcEv(
    Qt3DRender::QBlitFramebuffer *self) {
  return self->d_func();
}

//  const QBlitFramebufferPrivate *Qt3DRender::QBlitFramebuffer::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QBlitFramebufferPrivate *ritual_ZNK10Qt3DRender16QBlitFramebuffer6d_funcEv(
    const Qt3DRender::QBlitFramebuffer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QBlitFramebuffer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QBlitFramebuffer(
    Qt3DRender::QBlitFramebuffer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QBlitFramebuffer *>(self)->take(key, call);
}
