//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qline.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qline.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>

//  QLineF::QLineF()
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZN6QLineFC1Ev() {
  return new QLineF();
}

//  QLineF::QLineF(const QPointF &pt1, const QPointF &pt2)
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZN6QLineFC1ERK7QPointFS2_(
    const QPointF *pt1,
    const QPointF *pt2) {
  return new QLineF(*pt1, *pt2);
}

//  QLineF::QLineF(qreal x1, qreal y1, qreal x2, qreal y2)
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZN6QLineFC1Edddd(qreal x1, qreal y1, qreal x2, qreal y2) {
  return new QLineF(x1, y1, x2, y2);
}

//  QLineF::QLineF(const QLine &line)
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZN6QLineFC1ERK5QLine(const QLine *line) {
  return new QLineF(*line);
}

//  QLineF QLineF::fromPolar(qreal length, qreal angle)
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZN6QLineF9fromPolarEdd(qreal length, qreal angle) {
  return new QLineF(QLineF::fromPolar(length, angle));
}

//  bool QLineF::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QLineF6isNullEv(const QLineF *self) {
  return self->isNull();
}

//  QPointF QLineF::p1() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK6QLineF2p1Ev(const QLineF *self) {
  return new QPointF(self->p1());
}

//  QPointF QLineF::p2() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK6QLineF2p2Ev(const QLineF *self) {
  return new QPointF(self->p2());
}

//  qreal QLineF::x1() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QLineF2x1Ev(const QLineF *self) {
  return self->x1();
}

//  qreal QLineF::y1() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QLineF2y1Ev(const QLineF *self) {
  return self->y1();
}

//  qreal QLineF::x2() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QLineF2x2Ev(const QLineF *self) {
  return self->x2();
}

//  qreal QLineF::y2() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QLineF2y2Ev(const QLineF *self) {
  return self->y2();
}

//  qreal QLineF::dx() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QLineF2dxEv(const QLineF *self) {
  return self->dx();
}

//  qreal QLineF::dy() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QLineF2dyEv(const QLineF *self) {
  return self->dy();
}

//  qreal QLineF::length() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QLineF6lengthEv(const QLineF *self) {
  return self->length();
}

//  void QLineF::setLength(qreal len)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLineF9setLengthEd(QLineF *self, qreal len) {
  self->setLength(len);
}

//  qreal QLineF::angle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QLineF5angleEv(const QLineF *self) {
  return self->angle();
}

//  void QLineF::setAngle(qreal angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLineF8setAngleEd(QLineF *self, qreal angle) {
  self->setAngle(angle);
}

//  qreal QLineF::angleTo(const QLineF &l) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QLineF7angleToERKS_(const QLineF *self, const QLineF *l) {
  return self->angleTo(*l);
}

//  QLineF QLineF::unitVector() const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK6QLineF10unitVectorEv(const QLineF *self) {
  return new QLineF(self->unitVector());
}

//  QLineF QLineF::normalVector() const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK6QLineF12normalVectorEv(const QLineF *self) {
  return new QLineF(self->normalVector());
}

//  IntersectionType QLineF::intersects(const QLineF &l, QPointF
//      *intersectionPoint) const
extern "C" Q_DECL_EXPORT
QLineF::IntersectionType ritual_ZNK6QLineF10intersectsERKS_P7QPointF(
    const QLineF *self,
    const QLineF *l,
    QPointF *intersectionPoint) {
  return self->intersects(*l, intersectionPoint);
}

//  QPointF QLineF::pointAt(qreal t) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK6QLineF7pointAtEd(const QLineF *self, qreal t) {
  return new QPointF(self->pointAt(t));
}

//  void QLineF::translate(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLineF9translateERK7QPointF(QLineF *self, const QPointF *p) {
  self->translate(*p);
}

//  void QLineF::translate(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLineF9translateEdd(QLineF *self, qreal dx, qreal dy) {
  self->translate(dx, dy);
}

//  QLineF QLineF::translated(const QPointF &p) const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK6QLineF10translatedERK7QPointF(
    const QLineF *self,
    const QPointF *p) {
  return new QLineF(self->translated(*p));
}

//  QLineF QLineF::translated(qreal dx, qreal dy) const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK6QLineF10translatedEdd(
    const QLineF *self,
    qreal dx,
    qreal dy) {
  return new QLineF(self->translated(dx, dy));
}

//  QPointF QLineF::center() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK6QLineF6centerEv(const QLineF *self) {
  return new QPointF(self->center());
}

//  void QLineF::setP1(const QPointF &p1)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLineF5setP1ERK7QPointF(QLineF *self, const QPointF *p1) {
  self->setP1(*p1);
}

//  void QLineF::setP2(const QPointF &p2)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLineF5setP2ERK7QPointF(QLineF *self, const QPointF *p2) {
  self->setP2(*p2);
}

//  void QLineF::setPoints(const QPointF &p1, const QPointF &p2)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLineF9setPointsERK7QPointFS2_(
    QLineF *self,
    const QPointF *p1,
    const QPointF *p2) {
  self->setPoints(*p1, *p2);
}

//  void QLineF::setLine(qreal x1, qreal y1, qreal x2, qreal y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLineF7setLineEdddd(
    QLineF *self,
    qreal x1,
    qreal y1,
    qreal x2,
    qreal y2) {
  self->setLine(x1, y1, x2, y2);
}

//  QLine QLineF::toLine() const
extern "C" Q_DECL_EXPORT
QLine *ritual_ZNK6QLineF6toLineEv(const QLineF *self) {
  return new QLine(self->toLine());
}

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator==(const QLineF &lhs, const QLineF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QLineFS1_(const QLineF *lhs, const QLineF *rhs) {
  return operator==(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator!=(const QLineF &lhs, const QLineF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QLineFS1_(const QLineF *lhs, const QLineF *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

//  bool operator==(const QLineF &lhs, const QLine &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QLineFRK5QLine(const QLineF *lhs, const QLine *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QLineF &lhs, const QLine &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QLineFRK5QLine(const QLineF *lhs, const QLine *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QLine &lhs, const QLineF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QLineRK6QLineF(const QLine *lhs, const QLineF *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QLine &lhs, const QLineF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QLineRK6QLineF(const QLine *lhs, const QLineF *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QLineF::~QLineF()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLineFD1Ev(QLineF *self) {
  delete self;
}

//  QList<QLineF>::QList()
extern "C" Q_DECL_EXPORT
QList<QLineF> *ritual_list_make_QLineF() {
  return new QList<QLineF>();
}

//  void QList<QLineF>::append(const QLineF &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QLineF(QList<QLineF> *self, const QLineF *element) {
  self->append(*element);
}

//  qsizetype QList<QLineF>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QLineF(const QList<QLineF> *self) {
  return self->size();
}

//  const QLineF &QList<QLineF>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QLineF *ritual_list_at_QLineF(const QList<QLineF> *self, long long index) {
  return new QLineF(self->at(index));
}

//  QList<QLineF>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QLineF(QList<QLineF> *self) {
  delete self;
}
