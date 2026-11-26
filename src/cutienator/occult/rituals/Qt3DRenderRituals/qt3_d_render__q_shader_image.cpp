//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qshaderimage.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qshaderimage.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QShaderImage that Python can take functions over in. Every Qt3DRender::QShaderImage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QShaderImageCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QShaderImageCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderImageCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderImageCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderImageCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderImageCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QShaderImageCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QShaderImage : public Qt3DRender::QShaderImage {
public:
  using Qt3DRender::QShaderImage::QShaderImage;
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
      CuteQt3DRender_QShaderImageCall0 call = reinterpret_cast<CuteQt3DRender_QShaderImageCall0>(taken[0]);
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
      CuteQt3DRender_QShaderImageCall1 call = reinterpret_cast<CuteQt3DRender_QShaderImageCall1>(taken[1]);
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
      CuteQt3DRender_QShaderImageCall2 call = reinterpret_cast<CuteQt3DRender_QShaderImageCall2>(taken[2]);
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
      CuteQt3DRender_QShaderImageCall3 call = reinterpret_cast<CuteQt3DRender_QShaderImageCall3>(taken[3]);
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
      CuteQt3DRender_QShaderImageCall4 call = reinterpret_cast<CuteQt3DRender_QShaderImageCall4>(taken[4]);
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
      CuteQt3DRender_QShaderImageCall5 call = reinterpret_cast<CuteQt3DRender_QShaderImageCall5>(taken[5]);
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
      CuteQt3DRender_QShaderImageCall6 call = reinterpret_cast<CuteQt3DRender_QShaderImageCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QShaderImage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender12QShaderImage10metaObjectEv(
    const Qt3DRender::QShaderImage *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QShaderImage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender12QShaderImage11qt_metacastEPKc(
    Qt3DRender::QShaderImage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QShaderImage::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender12QShaderImage11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QShaderImage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QShaderImage::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender12QShaderImage2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QShaderImage::tr(s, c, n));
}

//  Qt3DRender::QShaderImage::QShaderImage(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderImage *ritual_ZN10Qt3DRender12QShaderImageC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QShaderImage(parent);
}

//  Qt3DRender::QShaderImage::~QShaderImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImageD1Ev(
    Qt3DRender::QShaderImage *self) {
  delete self;
}

//  Qt3DRender::QAbstractTexture *Qt3DRender::QShaderImage::texture() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZNK10Qt3DRender12QShaderImage7textureEv(
    const Qt3DRender::QShaderImage *self) {
  return self->texture();
}

//  bool Qt3DRender::QShaderImage::layered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender12QShaderImage7layeredEv(
    const Qt3DRender::QShaderImage *self) {
  return self->layered();
}

//  int Qt3DRender::QShaderImage::mipLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender12QShaderImage8mipLevelEv(
    const Qt3DRender::QShaderImage *self) {
  return self->mipLevel();
}

//  int Qt3DRender::QShaderImage::layer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender12QShaderImage5layerEv(
    const Qt3DRender::QShaderImage *self) {
  return self->layer();
}

//  Access Qt3DRender::QShaderImage::access() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderImage::Access ritual_ZNK10Qt3DRender12QShaderImage6accessEv(
    const Qt3DRender::QShaderImage *self) {
  return self->access();
}

//  ImageFormat Qt3DRender::QShaderImage::format() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderImage::ImageFormat ritual_ZNK10Qt3DRender12QShaderImage6formatEv(
    const Qt3DRender::QShaderImage *self) {
  return self->format();
}

//  void Qt3DRender::QShaderImage::setTexture(Qt3DRender::QAbstractTexture
//      *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImage10setTextureEPNS_16QAbstractTextureE(
    Qt3DRender::QShaderImage *self,
    Qt3DRender::QAbstractTexture *texture) {
  self->setTexture(texture);
}

//  void Qt3DRender::QShaderImage::setLayered(bool layered)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImage10setLayeredEb(
    Qt3DRender::QShaderImage *self,
    bool layered) {
  self->setLayered(layered);
}

//  void Qt3DRender::QShaderImage::setMipLevel(int mipLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImage11setMipLevelEi(
    Qt3DRender::QShaderImage *self,
    int mipLevel) {
  self->setMipLevel(mipLevel);
}

//  void Qt3DRender::QShaderImage::setLayer(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImage8setLayerEi(
    Qt3DRender::QShaderImage *self,
    int layer) {
  self->setLayer(layer);
}

//  void Qt3DRender::QShaderImage::setAccess(Access access)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImage9setAccessENS0_6AccessE(
    Qt3DRender::QShaderImage *self,
    Qt3DRender::QShaderImage::Access access) {
  self->setAccess(access);
}

//  void Qt3DRender::QShaderImage::setFormat(ImageFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImage9setFormatENS0_11ImageFormatE(
    Qt3DRender::QShaderImage *self,
    Qt3DRender::QShaderImage::ImageFormat format) {
  self->setFormat(format);
}

//  void
//      Qt3DRender::QShaderImage::textureChanged(Qt3DRender::QAbstractTexture
//      *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImage14textureChangedEPNS_16QAbstractTextureE(
    Qt3DRender::QShaderImage *self,
    Qt3DRender::QAbstractTexture *texture) {
  self->textureChanged(texture);
}

//  void Qt3DRender::QShaderImage::layeredChanged(bool layered)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImage14layeredChangedEb(
    Qt3DRender::QShaderImage *self,
    bool layered) {
  self->layeredChanged(layered);
}

//  void Qt3DRender::QShaderImage::mipLevelChanged(int mipLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImage15mipLevelChangedEi(
    Qt3DRender::QShaderImage *self,
    int mipLevel) {
  self->mipLevelChanged(mipLevel);
}

//  void Qt3DRender::QShaderImage::layerChanged(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImage12layerChangedEi(
    Qt3DRender::QShaderImage *self,
    int layer) {
  self->layerChanged(layer);
}

//  void Qt3DRender::QShaderImage::accessChanged(Access access)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImage13accessChangedENS0_6AccessE(
    Qt3DRender::QShaderImage *self,
    Qt3DRender::QShaderImage::Access access) {
  self->accessChanged(access);
}

//  void Qt3DRender::QShaderImage::formatChanged(ImageFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender12QShaderImage13formatChangedENS0_11ImageFormatE(
    Qt3DRender::QShaderImage *self,
    Qt3DRender::QShaderImage::ImageFormat format) {
  self->formatChanged(format);
}

//  QShaderImagePrivate *Qt3DRender::QShaderImage::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderImagePrivate *ritual_ZN10Qt3DRender12QShaderImage6d_funcEv(
    Qt3DRender::QShaderImage *self) {
  return self->d_func();
}

//  const QShaderImagePrivate *Qt3DRender::QShaderImage::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QShaderImagePrivate *ritual_ZNK10Qt3DRender12QShaderImage6d_funcEv(
    const Qt3DRender::QShaderImage *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QShaderImage, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QShaderImage(
    Qt3DRender::QShaderImage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QShaderImage *>(self)->take(key, call);
}
