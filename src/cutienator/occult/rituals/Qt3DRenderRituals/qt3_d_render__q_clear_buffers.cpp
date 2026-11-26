//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qclearbuffers.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qclearbuffers.h>
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QClearBuffers that Python can take functions over in. Every Qt3DRender::QClearBuffers
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QClearBuffersCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QClearBuffersCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QClearBuffersCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QClearBuffersCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QClearBuffersCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QClearBuffersCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QClearBuffersCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QClearBuffers : public Qt3DRender::QClearBuffers {
public:
  using Qt3DRender::QClearBuffers::QClearBuffers;
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
      CuteQt3DRender_QClearBuffersCall0 call = reinterpret_cast<CuteQt3DRender_QClearBuffersCall0>(taken[0]);
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
      CuteQt3DRender_QClearBuffersCall1 call = reinterpret_cast<CuteQt3DRender_QClearBuffersCall1>(taken[1]);
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
      CuteQt3DRender_QClearBuffersCall2 call = reinterpret_cast<CuteQt3DRender_QClearBuffersCall2>(taken[2]);
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
      CuteQt3DRender_QClearBuffersCall3 call = reinterpret_cast<CuteQt3DRender_QClearBuffersCall3>(taken[3]);
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
      CuteQt3DRender_QClearBuffersCall4 call = reinterpret_cast<CuteQt3DRender_QClearBuffersCall4>(taken[4]);
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
      CuteQt3DRender_QClearBuffersCall5 call = reinterpret_cast<CuteQt3DRender_QClearBuffersCall5>(taken[5]);
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
      CuteQt3DRender_QClearBuffersCall6 call = reinterpret_cast<CuteQt3DRender_QClearBuffersCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QClearBuffers::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender13QClearBuffers10metaObjectEv(
    const Qt3DRender::QClearBuffers *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QClearBuffers::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender13QClearBuffers11qt_metacastEPKc(
    Qt3DRender::QClearBuffers *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QClearBuffers::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender13QClearBuffers11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QClearBuffers *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QClearBuffers::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender13QClearBuffers2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QClearBuffers::tr(s, c, n));
}

//  Qt3DRender::QClearBuffers::QClearBuffers(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QClearBuffers *ritual_ZN10Qt3DRender13QClearBuffersC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QClearBuffers(parent);
}

//  Qt3DRender::QClearBuffers::~QClearBuffers()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QClearBuffersD1Ev(
    Qt3DRender::QClearBuffers *self) {
  delete self;
}

//  BufferType Qt3DRender::QClearBuffers::buffers() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QClearBuffers::BufferType ritual_ZNK10Qt3DRender13QClearBuffers7buffersEv(
    const Qt3DRender::QClearBuffers *self) {
  return self->buffers();
}

//  QColor Qt3DRender::QClearBuffers::clearColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DRender13QClearBuffers10clearColorEv(
    const Qt3DRender::QClearBuffers *self) {
  return new QColor(self->clearColor());
}

//  float Qt3DRender::QClearBuffers::clearDepthValue() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender13QClearBuffers15clearDepthValueEv(
    const Qt3DRender::QClearBuffers *self) {
  return self->clearDepthValue();
}

//  int Qt3DRender::QClearBuffers::clearStencilValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender13QClearBuffers17clearStencilValueEv(
    const Qt3DRender::QClearBuffers *self) {
  return self->clearStencilValue();
}

//  QRenderTargetOutput *Qt3DRender::QClearBuffers::colorBuffer() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetOutput *ritual_ZNK10Qt3DRender13QClearBuffers11colorBufferEv(
    const Qt3DRender::QClearBuffers *self) {
  return self->colorBuffer();
}

//  void Qt3DRender::QClearBuffers::setBuffers(BufferType buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QClearBuffers10setBuffersENS0_10BufferTypeE(
    Qt3DRender::QClearBuffers *self,
    Qt3DRender::QClearBuffers::BufferType buffers) {
  self->setBuffers(buffers);
}

//  void Qt3DRender::QClearBuffers::setClearColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QClearBuffers13setClearColorERK6QColor(
    Qt3DRender::QClearBuffers *self,
    const QColor *color) {
  self->setClearColor(*color);
}

//  void Qt3DRender::QClearBuffers::setClearDepthValue(float clearDepthValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QClearBuffers18setClearDepthValueEf(
    Qt3DRender::QClearBuffers *self,
    float clearDepthValue) {
  self->setClearDepthValue(clearDepthValue);
}

//  void Qt3DRender::QClearBuffers::setClearStencilValue(int
//      clearStencilValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QClearBuffers20setClearStencilValueEi(
    Qt3DRender::QClearBuffers *self,
    int clearStencilValue) {
  self->setClearStencilValue(clearStencilValue);
}

//  void Qt3DRender::QClearBuffers::setColorBuffer(QRenderTargetOutput
//      *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QClearBuffers14setColorBufferEPNS_19QRenderTargetOutputE(
    Qt3DRender::QClearBuffers *self,
    Qt3DRender::QRenderTargetOutput *buffer) {
  self->setColorBuffer(buffer);
}

//  void Qt3DRender::QClearBuffers::buffersChanged(BufferType buffers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QClearBuffers14buffersChangedENS0_10BufferTypeE(
    Qt3DRender::QClearBuffers *self,
    Qt3DRender::QClearBuffers::BufferType buffers) {
  self->buffersChanged(buffers);
}

//  void Qt3DRender::QClearBuffers::clearColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QClearBuffers17clearColorChangedERK6QColor(
    Qt3DRender::QClearBuffers *self,
    const QColor *color) {
  self->clearColorChanged(*color);
}

//  void Qt3DRender::QClearBuffers::clearDepthValueChanged(float
//      clearDepthValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QClearBuffers22clearDepthValueChangedEf(
    Qt3DRender::QClearBuffers *self,
    float clearDepthValue) {
  self->clearDepthValueChanged(clearDepthValue);
}

//  void Qt3DRender::QClearBuffers::clearStencilValueChanged(int
//      clearStencilValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QClearBuffers24clearStencilValueChangedEi(
    Qt3DRender::QClearBuffers *self,
    int clearStencilValue) {
  self->clearStencilValueChanged(clearStencilValue);
}

//  void Qt3DRender::QClearBuffers::colorBufferChanged(QRenderTargetOutput
//      *buffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QClearBuffers18colorBufferChangedEPNS_19QRenderTargetOutputE(
    Qt3DRender::QClearBuffers *self,
    Qt3DRender::QRenderTargetOutput *buffer) {
  self->colorBufferChanged(buffer);
}

//  Qt3DRender::QClearBuffers::QClearBuffers(QClearBuffersPrivate &dd,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QClearBuffers *ritual_ZN10Qt3DRender13QClearBuffersC1ERNS_20QClearBuffersPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QClearBuffersPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QClearBuffers(*dd, parent);
}

//  QClearBuffersPrivate *Qt3DRender::QClearBuffers::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QClearBuffersPrivate *ritual_ZN10Qt3DRender13QClearBuffers6d_funcEv(
    Qt3DRender::QClearBuffers *self) {
  return self->d_func();
}

//  const QClearBuffersPrivate *Qt3DRender::QClearBuffers::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QClearBuffersPrivate *ritual_ZNK10Qt3DRender13QClearBuffers6d_funcEv(
    const Qt3DRender::QClearBuffers *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QClearBuffers, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QClearBuffers(
    Qt3DRender::QClearBuffers *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QClearBuffers *>(self)->take(key, call);
}
