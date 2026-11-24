//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextengine_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextengine_p.h>
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>

//  glyph_metrics_t::glyph_metrics_t()
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN15glyph_metrics_tC1Ev() {
  return new glyph_metrics_t();
}

//  glyph_metrics_t::glyph_metrics_t(QFixed _x, QFixed _y, QFixed _width,
//      QFixed _height, QFixed _xoff, QFixed _yoff)
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZN15glyph_metrics_tC1E6QFixedS0_S0_S0_S0_S0_(
    const QFixed *_x,
    const QFixed *_y,
    const QFixed *_width,
    const QFixed *_height,
    const QFixed *_xoff,
    const QFixed *_yoff) {
  return new glyph_metrics_t(*_x, *_y, *_width, *_height, *_xoff, *_yoff);
}

//  glyph_metrics_t glyph_metrics_t::transformed(const QTransform &xform)
//      const
extern "C" Q_DECL_EXPORT
glyph_metrics_t *ritual_ZNK15glyph_metrics_t11transformedERK10QTransform(
    const glyph_metrics_t *self,
    const QTransform *xform) {
  return new glyph_metrics_t(self->transformed(*xform));
}

//  bool glyph_metrics_t::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15glyph_metrics_t7isValidEv(const glyph_metrics_t *self) {
  return self->isValid();
}

//  QFixed glyph_metrics_t::leftBearing() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK15glyph_metrics_t11leftBearingEv(
    const glyph_metrics_t *self) {
  return new QFixed(self->leftBearing());
}

//  QFixed glyph_metrics_t::rightBearing() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK15glyph_metrics_t12rightBearingEv(
    const glyph_metrics_t *self) {
  return new QFixed(self->rightBearing());
}

//  glyph_metrics_t::~glyph_metrics_t()
extern "C" Q_DECL_EXPORT
void ritual_ZN15glyph_metrics_tD1Ev(glyph_metrics_t *self) {
  delete self;
}
