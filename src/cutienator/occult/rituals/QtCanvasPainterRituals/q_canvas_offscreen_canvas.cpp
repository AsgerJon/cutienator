//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvasoffscreencanvas.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCanvasPainter/qcanvasoffscreencanvas.h>
#include <QtCore/qsize.h>
#include <QtGui/qcolor.h>

//  QCanvasOffscreenCanvas::QCanvasOffscreenCanvas()
extern "C" Q_DECL_EXPORT
QCanvasOffscreenCanvas *ritual_ZN22QCanvasOffscreenCanvasC1Ev() {
  return new QCanvasOffscreenCanvas();
}

//  QCanvasOffscreenCanvas::QCanvasOffscreenCanvas(const
//      QCanvasOffscreenCanvas &canvas)
extern "C" Q_DECL_EXPORT
QCanvasOffscreenCanvas *ritual_ZN22QCanvasOffscreenCanvasC1ERKS_(
    const QCanvasOffscreenCanvas *canvas) {
  return new QCanvasOffscreenCanvas(*canvas);
}

//  QCanvasOffscreenCanvas::~QCanvasOffscreenCanvas()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanvasOffscreenCanvasD1Ev(QCanvasOffscreenCanvas *self) {
  delete self;
}

//  QCanvasOffscreenCanvas &QCanvasOffscreenCanvas::operator=(const
//      QCanvasOffscreenCanvas &canvas)
extern "C" Q_DECL_EXPORT
QCanvasOffscreenCanvas *ritual_ZN22QCanvasOffscreenCanvasaSERKS_(
    QCanvasOffscreenCanvas *self,
    const QCanvasOffscreenCanvas *canvas) {
  return &(self->operator=(*canvas));
}

//  QCanvasOffscreenCanvas::QCanvasOffscreenCanvas(QCanvasOffscreenCanvas
//      &&other)
extern "C" Q_DECL_EXPORT
QCanvasOffscreenCanvas *ritual_ZN22QCanvasOffscreenCanvasC1EOS_(
    QCanvasOffscreenCanvas *other) {
  return new QCanvasOffscreenCanvas(std::move(*other));
}

//  QCanvasOffscreenCanvas
//      &QCanvasOffscreenCanvas::operator=(QCanvasOffscreenCanvas &&other)
extern "C" Q_DECL_EXPORT
QCanvasOffscreenCanvas *ritual_ZN22QCanvasOffscreenCanvasaSEOS_(
    QCanvasOffscreenCanvas *self,
    QCanvasOffscreenCanvas *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QCanvasOffscreenCanvas::swap(QCanvasOffscreenCanvas &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanvasOffscreenCanvas4swapERS_(
    QCanvasOffscreenCanvas *self,
    QCanvasOffscreenCanvas *other) {
  self->swap(*other);
}

//  bool QCanvasOffscreenCanvas::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QCanvasOffscreenCanvas6isNullEv(
    const QCanvasOffscreenCanvas *self) {
  return self->isNull();
}

//  int QCanvasOffscreenCanvas::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QCanvasOffscreenCanvas5widthEv(
    const QCanvasOffscreenCanvas *self) {
  return self->width();
}

//  int QCanvasOffscreenCanvas::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QCanvasOffscreenCanvas6heightEv(
    const QCanvasOffscreenCanvas *self) {
  return self->height();
}

//  QSize QCanvasOffscreenCanvas::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK22QCanvasOffscreenCanvas4sizeEv(
    const QCanvasOffscreenCanvas *self) {
  return new QSize(self->size());
}

//  Flags QCanvasOffscreenCanvas::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QCanvasOffscreenCanvas5flagsEv(
    const QCanvasOffscreenCanvas *self) {
  return static_cast<int>(self->flags().toInt());
}

//  QColor QCanvasOffscreenCanvas::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK22QCanvasOffscreenCanvas9fillColorEv(
    const QCanvasOffscreenCanvas *self) {
  return new QColor(self->fillColor());
}

//  void QCanvasOffscreenCanvas::setFillColor(QColor color)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCanvasOffscreenCanvas12setFillColorE6QColor(
    QCanvasOffscreenCanvas *self,
    const QColor *color) {
  self->setFillColor(*color);
}

//  QRhiTexture *QCanvasOffscreenCanvas::texture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK22QCanvasOffscreenCanvas7textureEv(
    const QCanvasOffscreenCanvas *self) {
  return self->texture();
}

//  bool operator==(const QCanvasOffscreenCanvas &lhs, const
//      QCanvasOffscreenCanvas &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK22QCanvasOffscreenCanvasS1_(
    const QCanvasOffscreenCanvas *lhs,
    const QCanvasOffscreenCanvas *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCanvasOffscreenCanvas &lhs, const
//      QCanvasOffscreenCanvas &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK22QCanvasOffscreenCanvasS1_(
    const QCanvasOffscreenCanvas *lhs,
    const QCanvasOffscreenCanvas *rhs) {
  return operator!=(*lhs, *rhs);
}
