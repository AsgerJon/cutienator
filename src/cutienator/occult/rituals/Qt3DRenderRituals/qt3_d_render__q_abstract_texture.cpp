//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qabstracttexture.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qabstracttexture.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <Qt3DRender/qtexturedataupdate.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::QAbstractTexture that Python can take functions over in. Every Qt3DRender::QAbstractTexture
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QAbstractTextureCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QAbstractTextureCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractTextureCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractTextureCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractTextureCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractTextureCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QAbstractTextureCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QAbstractTexture : public Qt3DRender::QAbstractTexture {
public:
  using Qt3DRender::QAbstractTexture::QAbstractTexture;
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
      CuteQt3DRender_QAbstractTextureCall0 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureCall0>(taken[0]);
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
      CuteQt3DRender_QAbstractTextureCall1 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureCall1>(taken[1]);
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
      CuteQt3DRender_QAbstractTextureCall2 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureCall2>(taken[2]);
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
      CuteQt3DRender_QAbstractTextureCall3 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureCall3>(taken[3]);
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
      CuteQt3DRender_QAbstractTextureCall4 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureCall4>(taken[4]);
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
      CuteQt3DRender_QAbstractTextureCall5 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureCall5>(taken[5]);
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
      CuteQt3DRender_QAbstractTextureCall6 call = reinterpret_cast<CuteQt3DRender_QAbstractTextureCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QAbstractTexture::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender16QAbstractTexture10metaObjectEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QAbstractTexture::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender16QAbstractTexture11qt_metacastEPKc(
    Qt3DRender::QAbstractTexture *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QAbstractTexture::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender16QAbstractTexture11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QAbstractTexture *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QAbstractTexture::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender16QAbstractTexture2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QAbstractTexture::tr(s, c, n));
}

//  Qt3DRender::QAbstractTexture::~QAbstractTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTextureD1Ev(
    Qt3DRender::QAbstractTexture *self) {
  delete self;
}

//  Target Qt3DRender::QAbstractTexture::target() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::Target ritual_ZNK10Qt3DRender16QAbstractTexture6targetEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->target();
}

//  TextureFormat Qt3DRender::QAbstractTexture::format() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::TextureFormat ritual_ZNK10Qt3DRender16QAbstractTexture6formatEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->format();
}

//  bool Qt3DRender::QAbstractTexture::generateMipMaps() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender16QAbstractTexture15generateMipMapsEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->generateMipMaps();
}

//  Status Qt3DRender::QAbstractTexture::status() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::Status ritual_ZNK10Qt3DRender16QAbstractTexture6statusEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->status();
}

//  void Qt3DRender::QAbstractTexture::addTextureImage(QAbstractTextureImage
//      *textureImage)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture15addTextureImageEPNS_21QAbstractTextureImageE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTextureImage *textureImage) {
  self->addTextureImage(textureImage);
}

//  void
//      Qt3DRender::QAbstractTexture::removeTextureImage(QAbstractTextureImag
//      e *textureImage)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture18removeTextureImageEPNS_21QAbstractTextureImageE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTextureImage *textureImage) {
  self->removeTextureImage(textureImage);
}

//  QList<QAbstractTextureImage *>
//      Qt3DRender::QAbstractTexture::textureImages() const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::QAbstractTextureImage *> *ritual_ZNK10Qt3DRender16QAbstractTexture13textureImagesEv(
    const Qt3DRender::QAbstractTexture *self) {
  return new QList<Qt3DRender::QAbstractTextureImage *>(
      self->textureImages());
}

//  void Qt3DRender::QAbstractTexture::setWrapMode(const QTextureWrapMode
//      &wrapMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture11setWrapModeERKNS_16QTextureWrapModeE(
    Qt3DRender::QAbstractTexture *self,
    const Qt3DRender::QTextureWrapMode *wrapMode) {
  self->setWrapMode(*wrapMode);
}

//  QTextureWrapMode *Qt3DRender::QAbstractTexture::wrapMode()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureWrapMode *ritual_ZN10Qt3DRender16QAbstractTexture8wrapModeEv(
    Qt3DRender::QAbstractTexture *self) {
  return self->wrapMode();
}

//  void Qt3DRender::QAbstractTexture::setSize(int width, int height, int
//      depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture7setSizeEiii(
    Qt3DRender::QAbstractTexture *self,
    int width,
    int height,
    int depth) {
  self->setSize(width, height, depth);
}

//  Filter Qt3DRender::QAbstractTexture::minificationFilter() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::Filter ritual_ZNK10Qt3DRender16QAbstractTexture18minificationFilterEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->minificationFilter();
}

//  Filter Qt3DRender::QAbstractTexture::magnificationFilter() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::Filter ritual_ZNK10Qt3DRender16QAbstractTexture19magnificationFilterEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->magnificationFilter();
}

//  float Qt3DRender::QAbstractTexture::maximumAnisotropy() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender16QAbstractTexture17maximumAnisotropyEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->maximumAnisotropy();
}

//  ComparisonFunction Qt3DRender::QAbstractTexture::comparisonFunction()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::ComparisonFunction ritual_ZNK10Qt3DRender16QAbstractTexture18comparisonFunctionEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->comparisonFunction();
}

//  ComparisonMode Qt3DRender::QAbstractTexture::comparisonMode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::ComparisonMode ritual_ZNK10Qt3DRender16QAbstractTexture14comparisonModeEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->comparisonMode();
}

//  int Qt3DRender::QAbstractTexture::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender16QAbstractTexture5widthEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->width();
}

//  int Qt3DRender::QAbstractTexture::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender16QAbstractTexture6heightEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->height();
}

//  int Qt3DRender::QAbstractTexture::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender16QAbstractTexture5depthEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->depth();
}

//  int Qt3DRender::QAbstractTexture::layers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender16QAbstractTexture6layersEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->layers();
}

//  int Qt3DRender::QAbstractTexture::samples() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender16QAbstractTexture7samplesEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->samples();
}

//  int Qt3DRender::QAbstractTexture::mipLevels() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender16QAbstractTexture9mipLevelsEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->mipLevels();
}

//  HandleType Qt3DRender::QAbstractTexture::handleType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture::HandleType ritual_ZNK10Qt3DRender16QAbstractTexture10handleTypeEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->handleType();
}

//  QVariant Qt3DRender::QAbstractTexture::handle() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10Qt3DRender16QAbstractTexture6handleEv(
    const Qt3DRender::QAbstractTexture *self) {
  return new QVariant(self->handle());
}

//  void Qt3DRender::QAbstractTexture::updateData(const QTextureDataUpdate
//      &update)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture10updateDataERKNS_18QTextureDataUpdateE(
    Qt3DRender::QAbstractTexture *self,
    const Qt3DRender::QTextureDataUpdate *update) {
  self->updateData(*update);
}

//  void Qt3DRender::QAbstractTexture::setFormat(TextureFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture9setFormatENS0_13TextureFormatE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::TextureFormat format) {
  self->setFormat(format);
}

//  void Qt3DRender::QAbstractTexture::setGenerateMipMaps(bool gen)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture18setGenerateMipMapsEb(
    Qt3DRender::QAbstractTexture *self,
    bool gen) {
  self->setGenerateMipMaps(gen);
}

//  void Qt3DRender::QAbstractTexture::setWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture8setWidthEi(
    Qt3DRender::QAbstractTexture *self,
    int width) {
  self->setWidth(width);
}

//  void Qt3DRender::QAbstractTexture::setHeight(int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture9setHeightEi(
    Qt3DRender::QAbstractTexture *self,
    int height) {
  self->setHeight(height);
}

//  void Qt3DRender::QAbstractTexture::setDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture8setDepthEi(
    Qt3DRender::QAbstractTexture *self,
    int depth) {
  self->setDepth(depth);
}

//  void Qt3DRender::QAbstractTexture::setMinificationFilter(Filter f)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture21setMinificationFilterENS0_6FilterE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::Filter f) {
  self->setMinificationFilter(f);
}

//  void Qt3DRender::QAbstractTexture::setMagnificationFilter(Filter f)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture22setMagnificationFilterENS0_6FilterE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::Filter f) {
  self->setMagnificationFilter(f);
}

//  void Qt3DRender::QAbstractTexture::setMaximumAnisotropy(float anisotropy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture20setMaximumAnisotropyEf(
    Qt3DRender::QAbstractTexture *self,
    float anisotropy) {
  self->setMaximumAnisotropy(anisotropy);
}

//  void
//      Qt3DRender::QAbstractTexture::setComparisonFunction(ComparisonFunctio
//      n function)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture21setComparisonFunctionENS0_18ComparisonFunctionE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::ComparisonFunction function) {
  self->setComparisonFunction(function);
}

//  void Qt3DRender::QAbstractTexture::setComparisonMode(ComparisonMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture17setComparisonModeENS0_14ComparisonModeE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::ComparisonMode mode) {
  self->setComparisonMode(mode);
}

//  void Qt3DRender::QAbstractTexture::setLayers(int layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture9setLayersEi(
    Qt3DRender::QAbstractTexture *self,
    int layers) {
  self->setLayers(layers);
}

//  void Qt3DRender::QAbstractTexture::setSamples(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture10setSamplesEi(
    Qt3DRender::QAbstractTexture *self,
    int samples) {
  self->setSamples(samples);
}

//  void Qt3DRender::QAbstractTexture::setMipLevels(int mipLevels)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture12setMipLevelsEi(
    Qt3DRender::QAbstractTexture *self,
    int mipLevels) {
  self->setMipLevels(mipLevels);
}

//  void Qt3DRender::QAbstractTexture::formatChanged(TextureFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture13formatChangedENS0_13TextureFormatE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::TextureFormat format) {
  self->formatChanged(format);
}

//  void Qt3DRender::QAbstractTexture::statusChanged(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture13statusChangedENS0_6StatusE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::Status status) {
  self->statusChanged(status);
}

//  void Qt3DRender::QAbstractTexture::generateMipMapsChanged(bool
//      generateMipMaps)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture22generateMipMapsChangedEb(
    Qt3DRender::QAbstractTexture *self,
    bool generateMipMaps) {
  self->generateMipMapsChanged(generateMipMaps);
}

//  void Qt3DRender::QAbstractTexture::widthChanged(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture12widthChangedEi(
    Qt3DRender::QAbstractTexture *self,
    int width) {
  self->widthChanged(width);
}

//  void Qt3DRender::QAbstractTexture::heightChanged(int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture13heightChangedEi(
    Qt3DRender::QAbstractTexture *self,
    int height) {
  self->heightChanged(height);
}

//  void Qt3DRender::QAbstractTexture::depthChanged(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture12depthChangedEi(
    Qt3DRender::QAbstractTexture *self,
    int depth) {
  self->depthChanged(depth);
}

//  void Qt3DRender::QAbstractTexture::magnificationFilterChanged(Filter
//      magnificationFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture26magnificationFilterChangedENS0_6FilterE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::Filter magnificationFilter) {
  self->magnificationFilterChanged(magnificationFilter);
}

//  void Qt3DRender::QAbstractTexture::minificationFilterChanged(Filter
//      minificationFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture25minificationFilterChangedENS0_6FilterE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::Filter minificationFilter) {
  self->minificationFilterChanged(minificationFilter);
}

//  void Qt3DRender::QAbstractTexture::maximumAnisotropyChanged(float
//      maximumAnisotropy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture24maximumAnisotropyChangedEf(
    Qt3DRender::QAbstractTexture *self,
    float maximumAnisotropy) {
  self->maximumAnisotropyChanged(maximumAnisotropy);
}

//  void Qt3DRender::QAbstractTexture::comparisonFunctionChanged(ComparisonFu
//      nction comparisonFunction)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture25comparisonFunctionChangedENS0_18ComparisonFunctionE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::ComparisonFunction comparisonFunction) {
  self->comparisonFunctionChanged(comparisonFunction);
}

//  void Qt3DRender::QAbstractTexture::comparisonModeChanged(ComparisonMode
//      comparisonMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture21comparisonModeChangedENS0_14ComparisonModeE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::ComparisonMode comparisonMode) {
  self->comparisonModeChanged(comparisonMode);
}

//  void Qt3DRender::QAbstractTexture::layersChanged(int layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture13layersChangedEi(
    Qt3DRender::QAbstractTexture *self,
    int layers) {
  self->layersChanged(layers);
}

//  void Qt3DRender::QAbstractTexture::samplesChanged(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture14samplesChangedEi(
    Qt3DRender::QAbstractTexture *self,
    int samples) {
  self->samplesChanged(samples);
}

//  void Qt3DRender::QAbstractTexture::handleTypeChanged(HandleType
//      handleType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture17handleTypeChangedENS0_10HandleTypeE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::HandleType handleType) {
  self->handleTypeChanged(handleType);
}

//  void Qt3DRender::QAbstractTexture::handleChanged(QVariant handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture13handleChangedE8QVariant(
    Qt3DRender::QAbstractTexture *self,
    const QVariant *handle) {
  self->handleChanged(*handle);
}

//  void Qt3DRender::QAbstractTexture::mipLevelsChanged(int mipLevels)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture16mipLevelsChangedEi(
    Qt3DRender::QAbstractTexture *self,
    int mipLevels) {
  self->mipLevelsChanged(mipLevels);
}

//  Qt3DRender::QAbstractTexture::QAbstractTexture(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZN10Qt3DRender16QAbstractTextureC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QAbstractTexture(parent);
}

//  Qt3DRender::QAbstractTexture::QAbstractTexture(Target target,
//      Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZN10Qt3DRender16QAbstractTextureC1ENS0_6TargetEPN8Qt3DCore5QNodeE(
    Qt3DRender::QAbstractTexture::Target target,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QAbstractTexture(target, parent);
}

//  Qt3DRender::QAbstractTexture::QAbstractTexture(QAbstractTexturePrivate
//      &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexture *ritual_ZN10Qt3DRender16QAbstractTextureC1ERNS_23QAbstractTexturePrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QAbstractTexturePrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QAbstractTexture(*dd, parent);
}

//  void Qt3DRender::QAbstractTexture::setStatus(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture9setStatusENS0_6StatusE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::Status status) {
  self->setStatus(status);
}

//  void Qt3DRender::QAbstractTexture::setHandle(const QVariant &handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture9setHandleERK8QVariant(
    Qt3DRender::QAbstractTexture *self,
    const QVariant *handle) {
  self->setHandle(*handle);
}

//  void Qt3DRender::QAbstractTexture::setHandleType(HandleType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QAbstractTexture13setHandleTypeENS0_10HandleTypeE(
    Qt3DRender::QAbstractTexture *self,
    Qt3DRender::QAbstractTexture::HandleType type) {
  self->setHandleType(type);
}

//  QAbstractTexturePrivate *Qt3DRender::QAbstractTexture::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractTexturePrivate *ritual_ZN10Qt3DRender16QAbstractTexture6d_funcEv(
    Qt3DRender::QAbstractTexture *self) {
  return self->d_func();
}

//  const QAbstractTexturePrivate *Qt3DRender::QAbstractTexture::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QAbstractTexturePrivate *ritual_ZNK10Qt3DRender16QAbstractTexture6d_funcEv(
    const Qt3DRender::QAbstractTexture *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QAbstractTexture, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QAbstractTexture(
    Qt3DRender::QAbstractTexture *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QAbstractTexture *>(self)->take(key, call);
}

//  a QList<Qt3DRender::QAbstractTextureImage *> a ritual of
//      Qt3DRender::QAbstractTexture gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QAbstractTexture__QList_Qt3DRender_QAbstractTextureImage(
    QList<Qt3DRender::QAbstractTextureImage *> *self) {
  delete self;
}
