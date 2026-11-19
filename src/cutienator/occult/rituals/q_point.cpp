//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpoint.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpoint.h>

//  QPoint::QPoint()
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN6QPointC1Ev() {
  return new QPoint();
}

//  QPoint::QPoint(int xpos, int ypos)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN6QPointC1Eii(int xpos, int ypos) {
  return new QPoint(xpos, ypos);
}

//  bool QPoint::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QPoint6isNullEv(const QPoint *self) {
  return self->isNull();
}

//  int QPoint::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QPoint1xEv(const QPoint *self) {
  return self->x();
}

//  int QPoint::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QPoint1yEv(const QPoint *self) {
  return self->y();
}

//  void QPoint::setX(int x)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPoint4setXEi(QPoint *self, int x) {
  self->setX(x);
}

//  void QPoint::setY(int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPoint4setYEi(QPoint *self, int y) {
  self->setY(y);
}

//  int QPoint::manhattanLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QPoint15manhattanLengthEv(const QPoint *self) {
  return self->manhattanLength();
}

//  QPoint QPoint::transposed() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK6QPoint10transposedEv(const QPoint *self) {
  return new QPoint(self->transposed());
}

//  int QPoint::dotProduct(const QPoint &p1, const QPoint &p2)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QPoint10dotProductERKS_S1_(
    const QPoint *p1,
    const QPoint *p2) {
  return QPoint::dotProduct(*p1, *p2);
}

//  QPointF QPoint::toPointF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK6QPoint8toPointFEv(const QPoint *self) {
  return new QPointF(self->toPointF());
}

//  QPoint::~QPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPointD1Ev(QPoint *self) {
  delete self;
}
