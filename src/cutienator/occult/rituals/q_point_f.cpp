//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpoint.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpoint.h>

//  QPointF::QPointF()
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN7QPointFC1Ev() {
  return new QPointF();
}

//  QPointF::QPointF(const QPoint &p)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN7QPointFC1ERK6QPoint(const QPoint *p) {
  return new QPointF(*p);
}

//  QPointF::QPointF(qreal xpos, qreal ypos)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN7QPointFC1Edd(qreal xpos, qreal ypos) {
  return new QPointF(xpos, ypos);
}

//  qreal QPointF::manhattanLength() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QPointF15manhattanLengthEv(const QPointF *self) {
  return self->manhattanLength();
}

//  bool QPointF::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QPointF6isNullEv(const QPointF *self) {
  return self->isNull();
}

//  qreal QPointF::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QPointF1xEv(const QPointF *self) {
  return self->x();
}

//  qreal QPointF::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK7QPointF1yEv(const QPointF *self) {
  return self->y();
}

//  void QPointF::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPointF4setXEd(QPointF *self, qreal x) {
  self->setX(x);
}

//  void QPointF::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPointF4setYEd(QPointF *self, qreal y) {
  self->setY(y);
}

//  QPointF QPointF::transposed() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK7QPointF10transposedEv(const QPointF *self) {
  return new QPointF(self->transposed());
}

//  qreal QPointF::dotProduct(const QPointF &p1, const QPointF &p2)
extern "C" Q_DECL_EXPORT
qreal ritual_ZN7QPointF10dotProductERKS_S1_(
    const QPointF *p1,
    const QPointF *p2) {
  return QPointF::dotProduct(*p1, *p2);
}

//  QPoint QPointF::toPoint() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK7QPointF7toPointEv(const QPointF *self) {
  return new QPoint(self->toPoint());
}

//  QPointF::~QPointF()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QPointFD1Ev(QPointF *self) {
  delete self;
}
