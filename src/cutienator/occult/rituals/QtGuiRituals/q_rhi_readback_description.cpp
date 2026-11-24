//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  QRhiReadbackDescription::QRhiReadbackDescription()
extern "C" Q_DECL_EXPORT
QRhiReadbackDescription *ritual_ZN23QRhiReadbackDescriptionC1Ev() {
  return new QRhiReadbackDescription();
}

//  QRhiReadbackDescription::QRhiReadbackDescription(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
QRhiReadbackDescription *ritual_ZN23QRhiReadbackDescriptionC1EP11QRhiTexture(
    QRhiTexture *texture) {
  return new QRhiReadbackDescription(texture);
}

//  QRhiTexture *QRhiReadbackDescription::texture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK23QRhiReadbackDescription7textureEv(
    const QRhiReadbackDescription *self) {
  return self->texture();
}

//  void QRhiReadbackDescription::setTexture(QRhiTexture *tex)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiReadbackDescription10setTextureEP11QRhiTexture(
    QRhiReadbackDescription *self,
    QRhiTexture *tex) {
  self->setTexture(tex);
}

//  int QRhiReadbackDescription::layer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QRhiReadbackDescription5layerEv(
    const QRhiReadbackDescription *self) {
  return self->layer();
}

//  void QRhiReadbackDescription::setLayer(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiReadbackDescription8setLayerEi(
    QRhiReadbackDescription *self,
    int layer) {
  self->setLayer(layer);
}

//  int QRhiReadbackDescription::level() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QRhiReadbackDescription5levelEv(
    const QRhiReadbackDescription *self) {
  return self->level();
}

//  void QRhiReadbackDescription::setLevel(int level)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiReadbackDescription8setLevelEi(
    QRhiReadbackDescription *self,
    int level) {
  self->setLevel(level);
}

//  QRect QRhiReadbackDescription::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK23QRhiReadbackDescription4rectEv(
    const QRhiReadbackDescription *self) {
  return new QRect(self->rect());
}

//  void QRhiReadbackDescription::setRect(const QRect &rectangle)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiReadbackDescription7setRectERK5QRect(
    QRhiReadbackDescription *self,
    const QRect *rectangle) {
  self->setRect(*rectangle);
}

//  QRhiReadbackDescription::~QRhiReadbackDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QRhiReadbackDescriptionD1Ev(QRhiReadbackDescription *self) {
  delete self;
}
