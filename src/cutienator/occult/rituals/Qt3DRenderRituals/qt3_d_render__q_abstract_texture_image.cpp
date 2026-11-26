//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qabstracttextureimage.h, Qt 6.12.0. Changes made here are
//  lost.
#include <Qt3DRender/qabstracttextureimage.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::QAbstractTextureImage that Python can take functions over in. Every Qt3DRender::QAbstractTextureImage
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QAbstractTextureImageCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QAbstractTextureImageCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractTextureImageCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractTextureImageCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractTextureImageCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractTextureImageCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractTextureImageCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QAbstractTextureImage : public Qt3DRender::QAbstractTextureImage {
public:
  using Qt3DRender::QAbstractTextureImage::QAbstractTextureImage;
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
      CuteQt3DRender_QAbstractTextureImageCall0 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureImageCall0>(taken[0]);
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
      CuteQt3DRender_QAbstractTextureImageCall1 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureImageCall1>(taken[1]);
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
      CuteQt3DRender_QAbstractTextureImageCall2 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureImageCall2>(taken[2]);
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
      CuteQt3DRender_QAbstractTextureImageCall3 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureImageCall3>(taken[3]);
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
      CuteQt3DRender_QAbstractTextureImageCall4 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureImageCall4>(taken[4]);
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
      CuteQt3DRender_QAbstractTextureImageCall5 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureImageCall5>(taken[5]);
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
      CuteQt3DRender_QAbstractTextureImageCall6 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureImageCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QAbstractTextureImage::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender21QAbstractTextureImage10metaObjectEv(
    const Qt3DRender::QAbstractTextureImage *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QAbstractTextureImage::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender21QAbstractTextureImage11qt_metacastEPKc(
    Qt3DRender::QAbstractTextureImage *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QAbstractTextureImage::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender21QAbstractTextureImage11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QAbstractTextureImage *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QAbstractTextureImage::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender21QAbstractTextureImage2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QAbstractTextureImage::tr(s, c, n));
}

//  Qt3DRender::QAbstractTextureImage::~QAbstractTextureImage()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QAbstractTextureImageD1Ev(
    Qt3DRender::QAbstractTextureImage *self) {
  delete self;
}

//  int Qt3DRender::QAbstractTextureImage::mipLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender21QAbstractTextureImage8mipLevelEv(
    const Qt3DRender::QAbstractTextureImage *self) {
  return self->mipLevel();
}

//  int Qt3DRender::QAbstractTextureImage::layer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender21QAbstractTextureImage5layerEv(
    const Qt3DRender::QAbstractTextureImage *self) {
  return self->layer();
}

//  QAbstractTexture::CubeMapFace Qt3DRender::QAbstractTextureImage::face()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::CubeMapFace ritual_ZNK10Qt3DRender21QAbstractTextureImage4faceEv(
    const Qt3DRender::QAbstractTextureImage *self) {
  return self->face();
}

//  void Qt3DRender::QAbstractTextureImage::setMipLevel(int level)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QAbstractTextureImage11setMipLevelEi(
    Qt3DRender::QAbstractTextureImage *self,
    int level) {
  self->setMipLevel(level);
}

//  void Qt3DRender::QAbstractTextureImage::setLayer(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QAbstractTextureImage8setLayerEi(
    Qt3DRender::QAbstractTextureImage *self,
    int layer) {
  self->setLayer(layer);
}

//  void
//      Qt3DRender::QAbstractTextureImage::setFace(QAbstractTexture::CubeMapF
//      ace face)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QAbstractTextureImage7setFaceENS_16QAbstractTexture11CubeMapFaceE(
    Qt3DRender::QAbstractTextureImage *self,
    Qt3DRender::QAbstractTexture::CubeMapFace face) {
  self->setFace(face);
}

//  void Qt3DRender::QAbstractTextureImage::mipLevelChanged(int mipLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QAbstractTextureImage15mipLevelChangedEi(
    Qt3DRender::QAbstractTextureImage *self,
    int mipLevel) {
  self->mipLevelChanged(mipLevel);
}

//  void Qt3DRender::QAbstractTextureImage::layerChanged(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QAbstractTextureImage12layerChangedEi(
    Qt3DRender::QAbstractTextureImage *self,
    int layer) {
  self->layerChanged(layer);
}

//  void Qt3DRender::QAbstractTextureImage::faceChanged(QAbstractTexture::Cub
//      eMapFace face)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QAbstractTextureImage11faceChangedENS_16QAbstractTexture11CubeMapFaceE(
    Qt3DRender::QAbstractTextureImage *self,
    Qt3DRender::QAbstractTexture::CubeMapFace face) {
  self->faceChanged(face);
}

//  void Qt3DRender::QAbstractTextureImage::notifyDataGeneratorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QAbstractTextureImage26notifyDataGeneratorChangedEv(
    Qt3DRender::QAbstractTextureImage *self) {
  self->notifyDataGeneratorChanged();
}

//  QTextureImageDataGeneratorPtr
//      Qt3DRender::QAbstractTextureImage::dataGenerator() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureImageDataGeneratorPtr *ritual_ZNK10Qt3DRender21QAbstractTextureImage13dataGeneratorEv(
    const Qt3DRender::QAbstractTextureImage *self) {
  return new Qt3DRender::QTextureImageDataGeneratorPtr(
      self->dataGenerator());
}

//  QAbstractTextureImagePrivate *Qt3DRender::QAbstractTextureImage::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTextureImagePrivate *ritual_ZN10Qt3DRender21QAbstractTextureImage6d_funcEv(
    Qt3DRender::QAbstractTextureImage *self) {
  return self->d_func();
}

//  const QAbstractTextureImagePrivate
//      *Qt3DRender::QAbstractTextureImage::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QAbstractTextureImagePrivate *ritual_ZNK10Qt3DRender21QAbstractTextureImage6d_funcEv(
    const Qt3DRender::QAbstractTextureImage *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QAbstractTextureImage, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QAbstractTextureImage(
    Qt3DRender::QAbstractTextureImage *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QAbstractTextureImage *>(self)->take(key, call);
}

//  a Qt3DRender::QTextureImageDataGeneratorPtr a ritual of
//      Qt3DRender::QAbstractTextureImage gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QAbstractTextureImage__Qt3DRender_QTextureImageDataGeneratorPtr(
    Qt3DRender::QTextureImageDataGeneratorPtr *self) {
  delete self;
}
