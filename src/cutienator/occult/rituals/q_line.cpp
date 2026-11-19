//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qline.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qline.h>
#include <QtCore/qpoint.h>

//  QLine::QLine()
extern "C" Q_DECL_EXPORT
QLine *ritual_ZN5QLineC1Ev() {
  return new QLine();
}

//  QLine::QLine(const QPoint &pt1, const QPoint &pt2)
extern "C" Q_DECL_EXPORT
QLine *ritual_ZN5QLineC1ERK6QPointS2_(const QPoint *pt1, const QPoint *pt2) {
  return new QLine(*pt1, *pt2);
}

//  QLine::QLine(int x1, int y1, int x2, int y2)
extern "C" Q_DECL_EXPORT
QLine *ritual_ZN5QLineC1Eiiii(int x1, int y1, int x2, int y2) {
  return new QLine(x1, y1, x2, y2);
}

//  bool QLine::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QLine6isNullEv(const QLine *self) {
  return self->isNull();
}

//  QPoint QLine::p1() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK5QLine2p1Ev(const QLine *self) {
  return new QPoint(self->p1());
}

//  QPoint QLine::p2() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK5QLine2p2Ev(const QLine *self) {
  return new QPoint(self->p2());
}

//  int QLine::x1() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QLine2x1Ev(const QLine *self) {
  return self->x1();
}

//  int QLine::y1() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QLine2y1Ev(const QLine *self) {
  return self->y1();
}

//  int QLine::x2() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QLine2x2Ev(const QLine *self) {
  return self->x2();
}

//  int QLine::y2() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QLine2y2Ev(const QLine *self) {
  return self->y2();
}

//  int QLine::dx() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QLine2dxEv(const QLine *self) {
  return self->dx();
}

//  int QLine::dy() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QLine2dyEv(const QLine *self) {
  return self->dy();
}

//  void QLine::translate(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QLine9translateERK6QPoint(QLine *self, const QPoint *p) {
  self->translate(*p);
}

//  void QLine::translate(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QLine9translateEii(QLine *self, int dx, int dy) {
  self->translate(dx, dy);
}

//  QLine QLine::translated(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QLine *ritual_ZNK5QLine10translatedERK6QPoint(
    const QLine *self,
    const QPoint *p) {
  return new QLine(self->translated(*p));
}

//  QLine QLine::translated(int dx, int dy) const
extern "C" Q_DECL_EXPORT
QLine *ritual_ZNK5QLine10translatedEii(const QLine *self, int dx, int dy) {
  return new QLine(self->translated(dx, dy));
}

//  QPoint QLine::center() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK5QLine6centerEv(const QLine *self) {
  return new QPoint(self->center());
}

//  void QLine::setP1(const QPoint &p1)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QLine5setP1ERK6QPoint(QLine *self, const QPoint *p1) {
  self->setP1(*p1);
}

//  void QLine::setP2(const QPoint &p2)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QLine5setP2ERK6QPoint(QLine *self, const QPoint *p2) {
  self->setP2(*p2);
}

//  void QLine::setPoints(const QPoint &p1, const QPoint &p2)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QLine9setPointsERK6QPointS2_(
    QLine *self,
    const QPoint *p1,
    const QPoint *p2) {
  self->setPoints(*p1, *p2);
}

//  void QLine::setLine(int x1, int y1, int x2, int y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QLine7setLineEiiii(
    QLine *self,
    int x1,
    int y1,
    int x2,
    int y2) {
  self->setLine(x1, y1, x2, y2);
}

//  QLineF QLine::toLineF() const
extern "C" Q_DECL_EXPORT
QLineF *ritual_ZNK5QLine7toLineFEv(const QLine *self) {
  return new QLineF(self->toLineF());
}

//  QLine::~QLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QLineD1Ev(QLine *self) {
  delete self;
}
