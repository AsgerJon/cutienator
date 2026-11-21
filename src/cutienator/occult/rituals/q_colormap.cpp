//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qcolormap.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qcolormap.h>
#include <QtGui/qcolor.h>

//  void QColormap::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QColormap10initializeEv() {
  QColormap::initialize();
}

//  void QColormap::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QColormap7cleanupEv() {
  QColormap::cleanup();
}

//  QColormap QColormap::instance(int screen)
extern "C" Q_DECL_EXPORT
QColormap *ritual_ZN9QColormap8instanceEi(int screen) {
  return new QColormap(QColormap::instance(screen));
}

//  QColormap::QColormap(const QColormap &colormap)
extern "C" Q_DECL_EXPORT
QColormap *ritual_ZN9QColormapC1ERKS_(const QColormap *colormap) {
  return new QColormap(*colormap);
}

//  QColormap::~QColormap()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QColormapD1Ev(QColormap *self) {
  delete self;
}

//  Mode QColormap::mode() const
extern "C" Q_DECL_EXPORT
QColormap::Mode ritual_ZNK9QColormap4modeEv(const QColormap *self) {
  return self->mode();
}

//  int QColormap::depth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QColormap5depthEv(const QColormap *self) {
  return self->depth();
}

//  int QColormap::size() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QColormap4sizeEv(const QColormap *self) {
  return self->size();
}

//  uint QColormap::pixel(const QColor &color) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK9QColormap5pixelERK6QColor(
    const QColormap *self,
    const QColor *color) {
  return self->pixel(*color);
}

//  const QColor QColormap::colorAt(uint pixel) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK9QColormap7colorAtEj(const QColormap *self, uint pixel) {
  return new QColor(self->colorAt(pixel));
}
