//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>

//  QRhiTextureCopyDescription::QRhiTextureCopyDescription()
extern "C" Q_DECL_EXPORT
QRhiTextureCopyDescription *ritual_ZN26QRhiTextureCopyDescriptionC1Ev() {
  return new QRhiTextureCopyDescription();
}

//  QSize QRhiTextureCopyDescription::pixelSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK26QRhiTextureCopyDescription9pixelSizeEv(
    const QRhiTextureCopyDescription *self) {
  return new QSize(self->pixelSize());
}

//  void QRhiTextureCopyDescription::setPixelSize(const QSize &sz)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiTextureCopyDescription12setPixelSizeERK5QSize(
    QRhiTextureCopyDescription *self,
    const QSize *sz) {
  self->setPixelSize(*sz);
}

//  int QRhiTextureCopyDescription::sourceLayer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QRhiTextureCopyDescription11sourceLayerEv(
    const QRhiTextureCopyDescription *self) {
  return self->sourceLayer();
}

//  void QRhiTextureCopyDescription::setSourceLayer(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiTextureCopyDescription14setSourceLayerEi(
    QRhiTextureCopyDescription *self,
    int layer) {
  self->setSourceLayer(layer);
}

//  int QRhiTextureCopyDescription::sourceLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QRhiTextureCopyDescription11sourceLevelEv(
    const QRhiTextureCopyDescription *self) {
  return self->sourceLevel();
}

//  void QRhiTextureCopyDescription::setSourceLevel(int level)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiTextureCopyDescription14setSourceLevelEi(
    QRhiTextureCopyDescription *self,
    int level) {
  self->setSourceLevel(level);
}

//  QPoint QRhiTextureCopyDescription::sourceTopLeft() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK26QRhiTextureCopyDescription13sourceTopLeftEv(
    const QRhiTextureCopyDescription *self) {
  return new QPoint(self->sourceTopLeft());
}

//  void QRhiTextureCopyDescription::setSourceTopLeft(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiTextureCopyDescription16setSourceTopLeftERK6QPoint(
    QRhiTextureCopyDescription *self,
    const QPoint *p) {
  self->setSourceTopLeft(*p);
}

//  int QRhiTextureCopyDescription::destinationLayer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QRhiTextureCopyDescription16destinationLayerEv(
    const QRhiTextureCopyDescription *self) {
  return self->destinationLayer();
}

//  void QRhiTextureCopyDescription::setDestinationLayer(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiTextureCopyDescription19setDestinationLayerEi(
    QRhiTextureCopyDescription *self,
    int layer) {
  self->setDestinationLayer(layer);
}

//  int QRhiTextureCopyDescription::destinationLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK26QRhiTextureCopyDescription16destinationLevelEv(
    const QRhiTextureCopyDescription *self) {
  return self->destinationLevel();
}

//  void QRhiTextureCopyDescription::setDestinationLevel(int level)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiTextureCopyDescription19setDestinationLevelEi(
    QRhiTextureCopyDescription *self,
    int level) {
  self->setDestinationLevel(level);
}

//  QPoint QRhiTextureCopyDescription::destinationTopLeft() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK26QRhiTextureCopyDescription18destinationTopLeftEv(
    const QRhiTextureCopyDescription *self) {
  return new QPoint(self->destinationTopLeft());
}

//  void QRhiTextureCopyDescription::setDestinationTopLeft(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiTextureCopyDescription21setDestinationTopLeftERK6QPoint(
    QRhiTextureCopyDescription *self,
    const QPoint *p) {
  self->setDestinationTopLeft(*p);
}

//  QRhiTextureCopyDescription::~QRhiTextureCopyDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QRhiTextureCopyDescriptionD1Ev(
    QRhiTextureCopyDescription *self) {
  delete self;
}
