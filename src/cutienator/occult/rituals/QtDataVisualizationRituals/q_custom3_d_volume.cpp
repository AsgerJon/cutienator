//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qcustom3dvolume.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDataVisualization/qcustom3dvolume.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qimage.h>
#include <QtGui/qcolor.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>
#include <QtGui/QRgb>

//  A QCustom3DVolume that Python can take functions over in. Every QCustom3DVolume
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustom3DVolumeCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCustom3DVolumeCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DVolumeCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DVolumeCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DVolumeCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DVolumeCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCustom3DVolumeCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCustom3DVolume : public QCustom3DVolume {
public:
  using QCustom3DVolume::QCustom3DVolume;
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
      CuteQCustom3DVolumeCall0 call = reinterpret_cast<CuteQCustom3DVolumeCall0>(taken[0]);
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
      CuteQCustom3DVolumeCall1 call = reinterpret_cast<CuteQCustom3DVolumeCall1>(taken[1]);
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
      CuteQCustom3DVolumeCall2 call = reinterpret_cast<CuteQCustom3DVolumeCall2>(taken[2]);
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
      CuteQCustom3DVolumeCall3 call = reinterpret_cast<CuteQCustom3DVolumeCall3>(taken[3]);
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
      CuteQCustom3DVolumeCall4 call = reinterpret_cast<CuteQCustom3DVolumeCall4>(taken[4]);
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
      CuteQCustom3DVolumeCall5 call = reinterpret_cast<CuteQCustom3DVolumeCall5>(taken[5]);
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
      CuteQCustom3DVolumeCall6 call = reinterpret_cast<CuteQCustom3DVolumeCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCustom3DVolume::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QCustom3DVolume10metaObjectEv(
    const QCustom3DVolume *self) {
  return self->metaObject();
}

//  void *QCustom3DVolume::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QCustom3DVolume11qt_metacastEPKc(
    QCustom3DVolume *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCustom3DVolume::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QCustom3DVolume11qt_metacallEN11QMetaObject4CallEiPPv(
    QCustom3DVolume *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QCustom3DVolume::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QCustom3DVolume2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCustom3DVolume::tr(s, c, n));
}

//  QCustom3DVolume::QCustom3DVolume(QObject *parent)
extern "C" Q_DECL_EXPORT
QCustom3DVolume *ritual_ZN15QCustom3DVolumeC1EP7QObject(QObject *parent) {
  return new CuteQCustom3DVolume(parent);
}

//  QCustom3DVolume::QCustom3DVolume(const QVector3D &position, const
//      QVector3D &scaling, const QQuaternion &rotation, int textureWidth,
//      int textureHeight, int textureDepth, QList<uchar> *textureData,
//      QImage::Format textureFormat, const QList<QRgb> &colorTable, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QCustom3DVolume *ritual_ZN15QCustom3DVolumeC1ERK9QVector3DS2_RK11QQuaternioniiiP5QListIhEN6QImage6FormatERKS6_IjEP7QObject(
    const QVector3D *position,
    const QVector3D *scaling,
    const QQuaternion *rotation,
    int textureWidth,
    int textureHeight,
    int textureDepth,
    QList<uchar> *textureData,
    QImage::Format textureFormat,
    const QList<QRgb> *colorTable,
    QObject *parent) {
  return new CuteQCustom3DVolume(
      *position,
      *scaling,
      *rotation,
      textureWidth,
      textureHeight,
      textureDepth,
      textureData,
      textureFormat,
      *colorTable,
      parent);
}

//  QCustom3DVolume::~QCustom3DVolume()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolumeD1Ev(QCustom3DVolume *self) {
  delete self;
}

//  void QCustom3DVolume::setTextureWidth(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume15setTextureWidthEi(
    QCustom3DVolume *self,
    int value) {
  self->setTextureWidth(value);
}

//  int QCustom3DVolume::textureWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCustom3DVolume12textureWidthEv(
    const QCustom3DVolume *self) {
  return self->textureWidth();
}

//  void QCustom3DVolume::setTextureHeight(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume16setTextureHeightEi(
    QCustom3DVolume *self,
    int value) {
  self->setTextureHeight(value);
}

//  int QCustom3DVolume::textureHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCustom3DVolume13textureHeightEv(
    const QCustom3DVolume *self) {
  return self->textureHeight();
}

//  void QCustom3DVolume::setTextureDepth(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume15setTextureDepthEi(
    QCustom3DVolume *self,
    int value) {
  self->setTextureDepth(value);
}

//  int QCustom3DVolume::textureDepth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCustom3DVolume12textureDepthEv(
    const QCustom3DVolume *self) {
  return self->textureDepth();
}

//  void QCustom3DVolume::setTextureDimensions(int width, int height, int
//      depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume20setTextureDimensionsEiii(
    QCustom3DVolume *self,
    int width,
    int height,
    int depth) {
  self->setTextureDimensions(width, height, depth);
}

//  int QCustom3DVolume::textureDataWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCustom3DVolume16textureDataWidthEv(
    const QCustom3DVolume *self) {
  return self->textureDataWidth();
}

//  void QCustom3DVolume::setSliceIndexX(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume14setSliceIndexXEi(
    QCustom3DVolume *self,
    int value) {
  self->setSliceIndexX(value);
}

//  int QCustom3DVolume::sliceIndexX() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCustom3DVolume11sliceIndexXEv(const QCustom3DVolume *self) {
  return self->sliceIndexX();
}

//  void QCustom3DVolume::setSliceIndexY(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume14setSliceIndexYEi(
    QCustom3DVolume *self,
    int value) {
  self->setSliceIndexY(value);
}

//  int QCustom3DVolume::sliceIndexY() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCustom3DVolume11sliceIndexYEv(const QCustom3DVolume *self) {
  return self->sliceIndexY();
}

//  void QCustom3DVolume::setSliceIndexZ(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume14setSliceIndexZEi(
    QCustom3DVolume *self,
    int value) {
  self->setSliceIndexZ(value);
}

//  int QCustom3DVolume::sliceIndexZ() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QCustom3DVolume11sliceIndexZEv(const QCustom3DVolume *self) {
  return self->sliceIndexZ();
}

//  void QCustom3DVolume::setSliceIndices(int x, int y, int z)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume15setSliceIndicesEiii(
    QCustom3DVolume *self,
    int x,
    int y,
    int z) {
  self->setSliceIndices(x, y, z);
}

//  void QCustom3DVolume::setColorTable(const QList<QRgb> &colors)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume13setColorTableERK5QListIjE(
    QCustom3DVolume *self,
    const QList<QRgb> *colors) {
  self->setColorTable(*colors);
}

//  QList<QRgb> QCustom3DVolume::colorTable() const
extern "C" Q_DECL_EXPORT
QList<QRgb> *ritual_ZNK15QCustom3DVolume10colorTableEv(
    const QCustom3DVolume *self) {
  return new QList<QRgb>(self->colorTable());
}

//  void QCustom3DVolume::setTextureData(QList<uchar> *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume14setTextureDataEP5QListIhE(
    QCustom3DVolume *self,
    QList<uchar> *data) {
  self->setTextureData(data);
}

//  QList<uchar> *QCustom3DVolume::createTextureData(const QList<QImage *>
//      &images)
extern "C" Q_DECL_EXPORT
QList<uchar> *ritual_ZN15QCustom3DVolume17createTextureDataERK5QListIP6QImageE(
    QCustom3DVolume *self,
    const QList<QImage *> *images) {
  return self->createTextureData(*images);
}

//  QList<uchar> *QCustom3DVolume::textureData() const
extern "C" Q_DECL_EXPORT
QList<uchar> *ritual_ZNK15QCustom3DVolume11textureDataEv(
    const QCustom3DVolume *self) {
  return self->textureData();
}

//  void QCustom3DVolume::setSubTextureData(Qt::Axis axis, int index, const
//      uchar *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume17setSubTextureDataEN2Qt4AxisEiPKh(
    QCustom3DVolume *self,
    Qt::Axis axis,
    int index,
    const uchar *data) {
  self->setSubTextureData(axis, index, data);
}

//  void QCustom3DVolume::setSubTextureData(Qt::Axis axis, int index, const
//      QImage &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume17setSubTextureDataEN2Qt4AxisEiRK6QImage(
    QCustom3DVolume *self,
    Qt::Axis axis,
    int index,
    const QImage *image) {
  self->setSubTextureData(axis, index, *image);
}

//  void QCustom3DVolume::setTextureFormat(QImage::Format format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume16setTextureFormatEN6QImage6FormatE(
    QCustom3DVolume *self,
    QImage::Format format) {
  self->setTextureFormat(format);
}

//  QImage::Format QCustom3DVolume::textureFormat() const
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZNK15QCustom3DVolume13textureFormatEv(
    const QCustom3DVolume *self) {
  return self->textureFormat();
}

//  void QCustom3DVolume::setAlphaMultiplier(float mult)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume18setAlphaMultiplierEf(
    QCustom3DVolume *self,
    float mult) {
  self->setAlphaMultiplier(mult);
}

//  float QCustom3DVolume::alphaMultiplier() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK15QCustom3DVolume15alphaMultiplierEv(
    const QCustom3DVolume *self) {
  return self->alphaMultiplier();
}

//  void QCustom3DVolume::setPreserveOpacity(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume18setPreserveOpacityEb(
    QCustom3DVolume *self,
    bool enable) {
  self->setPreserveOpacity(enable);
}

//  bool QCustom3DVolume::preserveOpacity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCustom3DVolume15preserveOpacityEv(
    const QCustom3DVolume *self) {
  return self->preserveOpacity();
}

//  void QCustom3DVolume::setUseHighDefShader(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume19setUseHighDefShaderEb(
    QCustom3DVolume *self,
    bool enable) {
  self->setUseHighDefShader(enable);
}

//  bool QCustom3DVolume::useHighDefShader() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCustom3DVolume16useHighDefShaderEv(
    const QCustom3DVolume *self) {
  return self->useHighDefShader();
}

//  void QCustom3DVolume::setDrawSlices(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume13setDrawSlicesEb(
    QCustom3DVolume *self,
    bool enable) {
  self->setDrawSlices(enable);
}

//  bool QCustom3DVolume::drawSlices() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCustom3DVolume10drawSlicesEv(const QCustom3DVolume *self) {
  return self->drawSlices();
}

//  void QCustom3DVolume::setDrawSliceFrames(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume18setDrawSliceFramesEb(
    QCustom3DVolume *self,
    bool enable) {
  self->setDrawSliceFrames(enable);
}

//  bool QCustom3DVolume::drawSliceFrames() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QCustom3DVolume15drawSliceFramesEv(
    const QCustom3DVolume *self) {
  return self->drawSliceFrames();
}

//  void QCustom3DVolume::setSliceFrameColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume18setSliceFrameColorERK6QColor(
    QCustom3DVolume *self,
    const QColor *color) {
  self->setSliceFrameColor(*color);
}

//  QColor QCustom3DVolume::sliceFrameColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QCustom3DVolume15sliceFrameColorEv(
    const QCustom3DVolume *self) {
  return new QColor(self->sliceFrameColor());
}

//  void QCustom3DVolume::setSliceFrameWidths(const QVector3D &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume19setSliceFrameWidthsERK9QVector3D(
    QCustom3DVolume *self,
    const QVector3D *values) {
  self->setSliceFrameWidths(*values);
}

//  QVector3D QCustom3DVolume::sliceFrameWidths() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK15QCustom3DVolume16sliceFrameWidthsEv(
    const QCustom3DVolume *self) {
  return new QVector3D(self->sliceFrameWidths());
}

//  void QCustom3DVolume::setSliceFrameGaps(const QVector3D &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume17setSliceFrameGapsERK9QVector3D(
    QCustom3DVolume *self,
    const QVector3D *values) {
  self->setSliceFrameGaps(*values);
}

//  QVector3D QCustom3DVolume::sliceFrameGaps() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK15QCustom3DVolume14sliceFrameGapsEv(
    const QCustom3DVolume *self) {
  return new QVector3D(self->sliceFrameGaps());
}

//  void QCustom3DVolume::setSliceFrameThicknesses(const QVector3D &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume24setSliceFrameThicknessesERK9QVector3D(
    QCustom3DVolume *self,
    const QVector3D *values) {
  self->setSliceFrameThicknesses(*values);
}

//  QVector3D QCustom3DVolume::sliceFrameThicknesses() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK15QCustom3DVolume21sliceFrameThicknessesEv(
    const QCustom3DVolume *self) {
  return new QVector3D(self->sliceFrameThicknesses());
}

//  QImage QCustom3DVolume::renderSlice(Qt::Axis axis, int index)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN15QCustom3DVolume11renderSliceEN2Qt4AxisEi(
    QCustom3DVolume *self,
    Qt::Axis axis,
    int index) {
  return new QImage(self->renderSlice(axis, index));
}

//  void QCustom3DVolume::textureWidthChanged(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume19textureWidthChangedEi(
    QCustom3DVolume *self,
    int value) {
  self->textureWidthChanged(value);
}

//  void QCustom3DVolume::textureHeightChanged(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume20textureHeightChangedEi(
    QCustom3DVolume *self,
    int value) {
  self->textureHeightChanged(value);
}

//  void QCustom3DVolume::textureDepthChanged(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume19textureDepthChangedEi(
    QCustom3DVolume *self,
    int value) {
  self->textureDepthChanged(value);
}

//  void QCustom3DVolume::sliceIndexXChanged(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume18sliceIndexXChangedEi(
    QCustom3DVolume *self,
    int value) {
  self->sliceIndexXChanged(value);
}

//  void QCustom3DVolume::sliceIndexYChanged(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume18sliceIndexYChangedEi(
    QCustom3DVolume *self,
    int value) {
  self->sliceIndexYChanged(value);
}

//  void QCustom3DVolume::sliceIndexZChanged(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume18sliceIndexZChangedEi(
    QCustom3DVolume *self,
    int value) {
  self->sliceIndexZChanged(value);
}

//  void QCustom3DVolume::colorTableChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume17colorTableChangedEv(QCustom3DVolume *self) {
  self->colorTableChanged();
}

//  void QCustom3DVolume::textureDataChanged(QList<uchar> *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume18textureDataChangedEP5QListIhE(
    QCustom3DVolume *self,
    QList<uchar> *data) {
  self->textureDataChanged(data);
}

//  void QCustom3DVolume::textureFormatChanged(QImage::Format format)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume20textureFormatChangedEN6QImage6FormatE(
    QCustom3DVolume *self,
    QImage::Format format) {
  self->textureFormatChanged(format);
}

//  void QCustom3DVolume::alphaMultiplierChanged(float mult)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume22alphaMultiplierChangedEf(
    QCustom3DVolume *self,
    float mult) {
  self->alphaMultiplierChanged(mult);
}

//  void QCustom3DVolume::preserveOpacityChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume22preserveOpacityChangedEb(
    QCustom3DVolume *self,
    bool enabled) {
  self->preserveOpacityChanged(enabled);
}

//  void QCustom3DVolume::useHighDefShaderChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume23useHighDefShaderChangedEb(
    QCustom3DVolume *self,
    bool enabled) {
  self->useHighDefShaderChanged(enabled);
}

//  void QCustom3DVolume::drawSlicesChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume17drawSlicesChangedEb(
    QCustom3DVolume *self,
    bool enabled) {
  self->drawSlicesChanged(enabled);
}

//  void QCustom3DVolume::drawSliceFramesChanged(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume22drawSliceFramesChangedEb(
    QCustom3DVolume *self,
    bool enabled) {
  self->drawSliceFramesChanged(enabled);
}

//  void QCustom3DVolume::sliceFrameColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume22sliceFrameColorChangedERK6QColor(
    QCustom3DVolume *self,
    const QColor *color) {
  self->sliceFrameColorChanged(*color);
}

//  void QCustom3DVolume::sliceFrameWidthsChanged(const QVector3D &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume23sliceFrameWidthsChangedERK9QVector3D(
    QCustom3DVolume *self,
    const QVector3D *values) {
  self->sliceFrameWidthsChanged(*values);
}

//  void QCustom3DVolume::sliceFrameGapsChanged(const QVector3D &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume21sliceFrameGapsChangedERK9QVector3D(
    QCustom3DVolume *self,
    const QVector3D *values) {
  self->sliceFrameGapsChanged(*values);
}

//  void QCustom3DVolume::sliceFrameThicknessesChanged(const QVector3D
//      &values)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QCustom3DVolume28sliceFrameThicknessesChangedERK9QVector3D(
    QCustom3DVolume *self,
    const QVector3D *values) {
  self->sliceFrameThicknessesChanged(*values);
}

//  QCustom3DVolumePrivate *QCustom3DVolume::dptr()
extern "C" Q_DECL_EXPORT
QCustom3DVolumePrivate *ritual_ZN15QCustom3DVolume4dptrEv(
    QCustom3DVolume *self) {
  return self->dptr();
}

//  const QCustom3DVolumePrivate *QCustom3DVolume::dptrc() const
extern "C" Q_DECL_EXPORT
const QCustom3DVolumePrivate *ritual_ZNK15QCustom3DVolume5dptrcEv(
    const QCustom3DVolume *self) {
  return self->dptrc();
}

//  a Python function taken by a CuteQCustom3DVolume, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCustom3DVolume(
    QCustom3DVolume *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCustom3DVolume *>(self)->take(key, call);
}

//  a QList<QRgb> a ritual of QCustom3DVolume gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QCustom3DVolume__QList_QRgb(QList<QRgb> *self) {
  delete self;
}
