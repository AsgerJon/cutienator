//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qrubberband.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qrubberband.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QRubberBand::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QRubberBand10metaObjectEv(
    const QRubberBand *self) {
  return self->metaObject();
}

//  QString QRubberBand::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QRubberBand2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRubberBand::tr(s, c, n));
}

//  QRubberBand::QRubberBand(Shape a0, QWidget *a1)
extern "C" Q_DECL_EXPORT
QRubberBand *ritual_ZN11QRubberBandC1ENS_5ShapeEP7QWidget(
    QRubberBand::Shape a0,
    QWidget *a1) {
  return new QRubberBand(a0, a1);
}

//  QRubberBand::~QRubberBand()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBandD1Ev(QRubberBand *self) {
  delete self;
}

//  Shape QRubberBand::shape() const
extern "C" Q_DECL_EXPORT
QRubberBand::Shape ritual_ZNK11QRubberBand5shapeEv(const QRubberBand *self) {
  return self->shape();
}

//  void QRubberBand::setGeometry(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBand11setGeometryERK5QRect(
    QRubberBand *self,
    const QRect *r) {
  self->setGeometry(*r);
}

//  void QRubberBand::setGeometry(int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBand11setGeometryEiiii(
    QRubberBand *self,
    int x,
    int y,
    int w,
    int h) {
  self->setGeometry(x, y, w, h);
}

//  void QRubberBand::move(int x, int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBand4moveEii(QRubberBand *self, int x, int y) {
  self->move(x, y);
}

//  void QRubberBand::move(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBand4moveERK6QPoint(
    QRubberBand *self,
    const QPoint *p) {
  self->move(*p);
}

//  void QRubberBand::resize(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBand6resizeEii(QRubberBand *self, int w, int h) {
  self->resize(w, h);
}

//  void QRubberBand::resize(const QSize &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRubberBand6resizeERK5QSize(
    QRubberBand *self,
    const QSize *s) {
  self->resize(*s);
}
