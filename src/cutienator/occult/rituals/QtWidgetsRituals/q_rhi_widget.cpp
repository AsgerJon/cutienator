//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qrhiwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qrhiwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>

//  const QMetaObject *QRhiWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QRhiWidget10metaObjectEv(
    const QRhiWidget *self) {
  return self->metaObject();
}

//  QString QRhiWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QRhiWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRhiWidget::tr(s, c, n));
}

//  QRhiWidget::QRhiWidget(QWidget *parent, Qt::WindowFlags f)
extern "C" Q_DECL_EXPORT
QRhiWidget *ritual_ZN10QRhiWidgetC1EP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QWidget *parent,
    int f) {
  return new QRhiWidget(parent, QFlags<Qt::WindowType>::fromInt(f));
}

//  QRhiWidget::~QRhiWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidgetD1Ev(QRhiWidget *self) {
  delete self;
}

//  Api QRhiWidget::api() const
extern "C" Q_DECL_EXPORT
QRhiWidget::Api ritual_ZNK10QRhiWidget3apiEv(const QRhiWidget *self) {
  return self->api();
}

//  void QRhiWidget::setApi(Api api)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget6setApiENS_3ApiE(
    QRhiWidget *self,
    QRhiWidget::Api api) {
  self->setApi(api);
}

//  bool QRhiWidget::isDebugLayerEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRhiWidget19isDebugLayerEnabledEv(const QRhiWidget *self) {
  return self->isDebugLayerEnabled();
}

//  void QRhiWidget::setDebugLayerEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget20setDebugLayerEnabledEb(
    QRhiWidget *self,
    bool enable) {
  self->setDebugLayerEnabled(enable);
}

//  int QRhiWidget::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QRhiWidget11sampleCountEv(const QRhiWidget *self) {
  return self->sampleCount();
}

//  void QRhiWidget::setSampleCount(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget14setSampleCountEi(QRhiWidget *self, int samples) {
  self->setSampleCount(samples);
}

//  TextureFormat QRhiWidget::colorBufferFormat() const
extern "C" Q_DECL_EXPORT
QRhiWidget::TextureFormat ritual_ZNK10QRhiWidget17colorBufferFormatEv(
    const QRhiWidget *self) {
  return self->colorBufferFormat();
}

//  void QRhiWidget::setColorBufferFormat(TextureFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget20setColorBufferFormatENS_13TextureFormatE(
    QRhiWidget *self,
    QRhiWidget::TextureFormat format) {
  self->setColorBufferFormat(format);
}

//  QSize QRhiWidget::fixedColorBufferSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10QRhiWidget20fixedColorBufferSizeEv(
    const QRhiWidget *self) {
  return new QSize(self->fixedColorBufferSize());
}

//  void QRhiWidget::setFixedColorBufferSize(QSize pixelSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget23setFixedColorBufferSizeE5QSize(
    QRhiWidget *self,
    const QSize *pixelSize) {
  self->setFixedColorBufferSize(*pixelSize);
}

//  void QRhiWidget::setFixedColorBufferSize(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget23setFixedColorBufferSizeEii(
    QRhiWidget *self,
    int w,
    int h) {
  self->setFixedColorBufferSize(w, h);
}

//  bool QRhiWidget::isMirrorVerticallyEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QRhiWidget25isMirrorVerticallyEnabledEv(
    const QRhiWidget *self) {
  return self->isMirrorVerticallyEnabled();
}

//  void QRhiWidget::setMirrorVertically(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QRhiWidget19setMirrorVerticallyEb(
    QRhiWidget *self,
    bool enabled) {
  self->setMirrorVertically(enabled);
}

//  QImage QRhiWidget::grabFramebuffer() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK10QRhiWidget15grabFramebufferEv(const QRhiWidget *self) {
  return new QImage(self->grabFramebuffer());
}
