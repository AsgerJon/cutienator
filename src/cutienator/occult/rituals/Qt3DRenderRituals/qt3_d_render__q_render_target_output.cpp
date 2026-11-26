//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qrendertargetoutput.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qrendertargetoutput.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QRenderTargetOutput that Python can take functions over in. Every Qt3DRender::QRenderTargetOutput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderTargetOutputCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRenderTargetOutputCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetOutputCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetOutputCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetOutputCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetOutputCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRenderTargetOutputCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QRenderTargetOutput : public Qt3DRender::QRenderTargetOutput {
public:
  using Qt3DRender::QRenderTargetOutput::QRenderTargetOutput;
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
      CuteQt3DRender_QRenderTargetOutputCall0 call = reinterpret_cast<CuteQt3DRender_QRenderTargetOutputCall0>(taken[0]);
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
      CuteQt3DRender_QRenderTargetOutputCall1 call = reinterpret_cast<CuteQt3DRender_QRenderTargetOutputCall1>(taken[1]);
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
      CuteQt3DRender_QRenderTargetOutputCall2 call = reinterpret_cast<CuteQt3DRender_QRenderTargetOutputCall2>(taken[2]);
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
      CuteQt3DRender_QRenderTargetOutputCall3 call = reinterpret_cast<CuteQt3DRender_QRenderTargetOutputCall3>(taken[3]);
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
      CuteQt3DRender_QRenderTargetOutputCall4 call = reinterpret_cast<CuteQt3DRender_QRenderTargetOutputCall4>(taken[4]);
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
      CuteQt3DRender_QRenderTargetOutputCall5 call = reinterpret_cast<CuteQt3DRender_QRenderTargetOutputCall5>(taken[5]);
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
      CuteQt3DRender_QRenderTargetOutputCall6 call = reinterpret_cast<CuteQt3DRender_QRenderTargetOutputCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QRenderTargetOutput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender19QRenderTargetOutput10metaObjectEv(
    const Qt3DRender::QRenderTargetOutput *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QRenderTargetOutput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender19QRenderTargetOutput11qt_metacastEPKc(
    Qt3DRender::QRenderTargetOutput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QRenderTargetOutput::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender19QRenderTargetOutput11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QRenderTargetOutput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QRenderTargetOutput::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender19QRenderTargetOutput2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QRenderTargetOutput::tr(s, c, n));
}

//  Qt3DRender::QRenderTargetOutput::QRenderTargetOutput(Qt3DCore::QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetOutput *ritual_ZN10Qt3DRender19QRenderTargetOutputC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRenderTargetOutput(parent);
}

//  Qt3DRender::QRenderTargetOutput::~QRenderTargetOutput()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderTargetOutputD1Ev(
    Qt3DRender::QRenderTargetOutput *self) {
  delete self;
}

//  AttachmentPoint Qt3DRender::QRenderTargetOutput::attachmentPoint() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetOutput::AttachmentPoint ritual_ZNK10Qt3DRender19QRenderTargetOutput15attachmentPointEv(
    const Qt3DRender::QRenderTargetOutput *self) {
  return self->attachmentPoint();
}

//  QAbstractTexture *Qt3DRender::QRenderTargetOutput::texture() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DRender19QRenderTargetOutput7textureEv(
    const Qt3DRender::QRenderTargetOutput *self) {
  return self->texture();
}

//  int Qt3DRender::QRenderTargetOutput::mipLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderTargetOutput8mipLevelEv(
    const Qt3DRender::QRenderTargetOutput *self) {
  return self->mipLevel();
}

//  int Qt3DRender::QRenderTargetOutput::layer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender19QRenderTargetOutput5layerEv(
    const Qt3DRender::QRenderTargetOutput *self) {
  return self->layer();
}

//  QAbstractTexture::CubeMapFace Qt3DRender::QRenderTargetOutput::face()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::CubeMapFace ritual_ZNK10Qt3DRender19QRenderTargetOutput4faceEv(
    const Qt3DRender::QRenderTargetOutput *self) {
  return self->face();
}

//  void Qt3DRender::QRenderTargetOutput::setAttachmentPoint(AttachmentPoint
//      attachmentPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderTargetOutput18setAttachmentPointENS0_15AttachmentPointE(
    Qt3DRender::QRenderTargetOutput *self,
    Qt3DRender::QRenderTargetOutput::AttachmentPoint attachmentPoint) {
  self->setAttachmentPoint(attachmentPoint);
}

//  void Qt3DRender::QRenderTargetOutput::setTexture(QAbstractTexture
//      *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderTargetOutput10setTextureEPNS_16QAbstractTextureE(
    Qt3DRender::QRenderTargetOutput *self,
    Qt3DRender::QAbstractTexture *texture) {
  self->setTexture(texture);
}

//  void Qt3DRender::QRenderTargetOutput::setMipLevel(int level)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderTargetOutput11setMipLevelEi(
    Qt3DRender::QRenderTargetOutput *self,
    int level) {
  self->setMipLevel(level);
}

//  void Qt3DRender::QRenderTargetOutput::setLayer(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderTargetOutput8setLayerEi(
    Qt3DRender::QRenderTargetOutput *self,
    int layer) {
  self->setLayer(layer);
}

//  void
//      Qt3DRender::QRenderTargetOutput::setFace(QAbstractTexture::CubeMapFac
//      e face)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderTargetOutput7setFaceENS_16QAbstractTexture11CubeMapFaceE(
    Qt3DRender::QRenderTargetOutput *self,
    Qt3DRender::QAbstractTexture::CubeMapFace face) {
  self->setFace(face);
}

//  void
//      Qt3DRender::QRenderTargetOutput::attachmentPointChanged(AttachmentPoi
//      nt attachmentPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderTargetOutput22attachmentPointChangedENS0_15AttachmentPointE(
    Qt3DRender::QRenderTargetOutput *self,
    Qt3DRender::QRenderTargetOutput::AttachmentPoint attachmentPoint) {
  self->attachmentPointChanged(attachmentPoint);
}

//  void Qt3DRender::QRenderTargetOutput::textureChanged(QAbstractTexture
//      *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderTargetOutput14textureChangedEPNS_16QAbstractTextureE(
    Qt3DRender::QRenderTargetOutput *self,
    Qt3DRender::QAbstractTexture *texture) {
  self->textureChanged(texture);
}

//  void Qt3DRender::QRenderTargetOutput::mipLevelChanged(int mipLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderTargetOutput15mipLevelChangedEi(
    Qt3DRender::QRenderTargetOutput *self,
    int mipLevel) {
  self->mipLevelChanged(mipLevel);
}

//  void Qt3DRender::QRenderTargetOutput::layerChanged(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderTargetOutput12layerChangedEi(
    Qt3DRender::QRenderTargetOutput *self,
    int layer) {
  self->layerChanged(layer);
}

//  void Qt3DRender::QRenderTargetOutput::faceChanged(QAbstractTexture::CubeM
//      apFace face)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QRenderTargetOutput11faceChangedENS_16QAbstractTexture11CubeMapFaceE(
    Qt3DRender::QRenderTargetOutput *self,
    Qt3DRender::QAbstractTexture::CubeMapFace face) {
  self->faceChanged(face);
}

//  Qt3DRender::QRenderTargetOutput::QRenderTargetOutput(QRenderTargetOutputP
//      rivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetOutput *ritual_ZN10Qt3DRender19QRenderTargetOutputC1ERNS_26QRenderTargetOutputPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QRenderTargetOutputPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRenderTargetOutput(*dd, parent);
}

//  QRenderTargetOutputPrivate *Qt3DRender::QRenderTargetOutput::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderTargetOutputPrivate *ritual_ZN10Qt3DRender19QRenderTargetOutput6d_funcEv(
    Qt3DRender::QRenderTargetOutput *self) {
  return self->d_func();
}

//  const QRenderTargetOutputPrivate
//      *Qt3DRender::QRenderTargetOutput::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderTargetOutputPrivate *ritual_ZNK10Qt3DRender19QRenderTargetOutput6d_funcEv(
    const Qt3DRender::QRenderTargetOutput *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QRenderTargetOutput, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderTargetOutput(
    Qt3DRender::QRenderTargetOutput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderTargetOutput *>(self)->take(key, call);
}
