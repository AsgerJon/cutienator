//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrect.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmargins.h>
#include <QtCore/qlist.h>

//  QRectF::QRectF()
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN6QRectFC1Ev() {
  return new QRectF();
}

//  QRectF::QRectF(const QPointF &topleft, const QSizeF &size)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN6QRectFC1ERK7QPointFRK6QSizeF(
    const QPointF *topleft,
    const QSizeF *size) {
  return new QRectF(*topleft, *size);
}

//  QRectF::QRectF(const QPointF &topleft, const QPointF &bottomRight)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN6QRectFC1ERK7QPointFS2_(
    const QPointF *topleft,
    const QPointF *bottomRight) {
  return new QRectF(*topleft, *bottomRight);
}

//  QRectF::QRectF(qreal left, qreal top, qreal width, qreal height)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN6QRectFC1Edddd(
    qreal left,
    qreal top,
    qreal width,
    qreal height) {
  return new QRectF(left, top, width, height);
}

//  QRectF::QRectF(const QRect &rect)
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZN6QRectFC1ERK5QRect(const QRect *rect) {
  return new QRectF(*rect);
}

//  bool QRectF::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QRectF6isNullEv(const QRectF *self) {
  return self->isNull();
}

//  bool QRectF::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QRectF7isEmptyEv(const QRectF *self) {
  return self->isEmpty();
}

//  bool QRectF::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QRectF7isValidEv(const QRectF *self) {
  return self->isValid();
}

//  QRectF QRectF::normalized() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK6QRectF10normalizedEv(const QRectF *self) {
  return new QRectF(self->normalized());
}

//  qreal QRectF::left() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QRectF4leftEv(const QRectF *self) {
  return self->left();
}

//  qreal QRectF::top() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QRectF3topEv(const QRectF *self) {
  return self->top();
}

//  qreal QRectF::right() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QRectF5rightEv(const QRectF *self) {
  return self->right();
}

//  qreal QRectF::bottom() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QRectF6bottomEv(const QRectF *self) {
  return self->bottom();
}

//  qreal QRectF::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QRectF1xEv(const QRectF *self) {
  return self->x();
}

//  qreal QRectF::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QRectF1yEv(const QRectF *self) {
  return self->y();
}

//  void QRectF::setLeft(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF7setLeftEd(QRectF *self, qreal pos) {
  self->setLeft(pos);
}

//  void QRectF::setTop(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF6setTopEd(QRectF *self, qreal pos) {
  self->setTop(pos);
}

//  void QRectF::setRight(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF8setRightEd(QRectF *self, qreal pos) {
  self->setRight(pos);
}

//  void QRectF::setBottom(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF9setBottomEd(QRectF *self, qreal pos) {
  self->setBottom(pos);
}

//  void QRectF::setX(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF4setXEd(QRectF *self, qreal pos) {
  self->setX(pos);
}

//  void QRectF::setY(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF4setYEd(QRectF *self, qreal pos) {
  self->setY(pos);
}

//  QPointF QRectF::topLeft() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK6QRectF7topLeftEv(const QRectF *self) {
  return new QPointF(self->topLeft());
}

//  QPointF QRectF::bottomRight() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK6QRectF11bottomRightEv(const QRectF *self) {
  return new QPointF(self->bottomRight());
}

//  QPointF QRectF::topRight() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK6QRectF8topRightEv(const QRectF *self) {
  return new QPointF(self->topRight());
}

//  QPointF QRectF::bottomLeft() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK6QRectF10bottomLeftEv(const QRectF *self) {
  return new QPointF(self->bottomLeft());
}

//  QPointF QRectF::center() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK6QRectF6centerEv(const QRectF *self) {
  return new QPointF(self->center());
}

//  void QRectF::setTopLeft(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF10setTopLeftERK7QPointF(
    QRectF *self,
    const QPointF *p) {
  self->setTopLeft(*p);
}

//  void QRectF::setBottomRight(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF14setBottomRightERK7QPointF(
    QRectF *self,
    const QPointF *p) {
  self->setBottomRight(*p);
}

//  void QRectF::setTopRight(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF11setTopRightERK7QPointF(
    QRectF *self,
    const QPointF *p) {
  self->setTopRight(*p);
}

//  void QRectF::setBottomLeft(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF13setBottomLeftERK7QPointF(
    QRectF *self,
    const QPointF *p) {
  self->setBottomLeft(*p);
}

//  void QRectF::moveLeft(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF8moveLeftEd(QRectF *self, qreal pos) {
  self->moveLeft(pos);
}

//  void QRectF::moveTop(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF7moveTopEd(QRectF *self, qreal pos) {
  self->moveTop(pos);
}

//  void QRectF::moveRight(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF9moveRightEd(QRectF *self, qreal pos) {
  self->moveRight(pos);
}

//  void QRectF::moveBottom(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF10moveBottomEd(QRectF *self, qreal pos) {
  self->moveBottom(pos);
}

//  void QRectF::moveTopLeft(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF11moveTopLeftERK7QPointF(
    QRectF *self,
    const QPointF *p) {
  self->moveTopLeft(*p);
}

//  void QRectF::moveBottomRight(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF15moveBottomRightERK7QPointF(
    QRectF *self,
    const QPointF *p) {
  self->moveBottomRight(*p);
}

//  void QRectF::moveTopRight(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF12moveTopRightERK7QPointF(
    QRectF *self,
    const QPointF *p) {
  self->moveTopRight(*p);
}

//  void QRectF::moveBottomLeft(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF14moveBottomLeftERK7QPointF(
    QRectF *self,
    const QPointF *p) {
  self->moveBottomLeft(*p);
}

//  void QRectF::moveCenter(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF10moveCenterERK7QPointF(
    QRectF *self,
    const QPointF *p) {
  self->moveCenter(*p);
}

//  void QRectF::translate(qreal dx, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF9translateEdd(QRectF *self, qreal dx, qreal dy) {
  self->translate(dx, dy);
}

//  void QRectF::translate(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF9translateERK7QPointF(QRectF *self, const QPointF *p) {
  self->translate(*p);
}

//  QRectF QRectF::translated(qreal dx, qreal dy) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK6QRectF10translatedEdd(
    const QRectF *self,
    qreal dx,
    qreal dy) {
  return new QRectF(self->translated(dx, dy));
}

//  QRectF QRectF::translated(const QPointF &p) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK6QRectF10translatedERK7QPointF(
    const QRectF *self,
    const QPointF *p) {
  return new QRectF(self->translated(*p));
}

//  QRectF QRectF::transposed() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK6QRectF10transposedEv(const QRectF *self) {
  return new QRectF(self->transposed());
}

//  void QRectF::moveTo(qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF6moveToEdd(QRectF *self, qreal x, qreal y) {
  self->moveTo(x, y);
}

//  void QRectF::moveTo(const QPointF &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF6moveToERK7QPointF(QRectF *self, const QPointF *p) {
  self->moveTo(*p);
}

//  void QRectF::setRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF7setRectEdddd(
    QRectF *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setRect(x, y, w, h);
}

//  void QRectF::getRect(qreal *x, qreal *y, qreal *w, qreal *h) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QRectF7getRectEPdS0_S0_S0_(
    const QRectF *self,
    qreal *x,
    qreal *y,
    qreal *w,
    qreal *h) {
  self->getRect(x, y, w, h);
}

//  void QRectF::setCoords(qreal x1, qreal y1, qreal x2, qreal y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF9setCoordsEdddd(
    QRectF *self,
    qreal x1,
    qreal y1,
    qreal x2,
    qreal y2) {
  self->setCoords(x1, y1, x2, y2);
}

//  void QRectF::getCoords(qreal *x1, qreal *y1, qreal *x2, qreal *y2) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK6QRectF9getCoordsEPdS0_S0_S0_(
    const QRectF *self,
    qreal *x1,
    qreal *y1,
    qreal *x2,
    qreal *y2) {
  self->getCoords(x1, y1, x2, y2);
}

//  void QRectF::adjust(qreal x1, qreal y1, qreal x2, qreal y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF6adjustEdddd(
    QRectF *self,
    qreal x1,
    qreal y1,
    qreal x2,
    qreal y2) {
  self->adjust(x1, y1, x2, y2);
}

//  QRectF QRectF::adjusted(qreal x1, qreal y1, qreal x2, qreal y2) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK6QRectF8adjustedEdddd(
    const QRectF *self,
    qreal x1,
    qreal y1,
    qreal x2,
    qreal y2) {
  return new QRectF(self->adjusted(x1, y1, x2, y2));
}

//  QSizeF QRectF::size() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK6QRectF4sizeEv(const QRectF *self) {
  return new QSizeF(self->size());
}

//  qreal QRectF::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QRectF5widthEv(const QRectF *self) {
  return self->width();
}

//  qreal QRectF::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QRectF6heightEv(const QRectF *self) {
  return self->height();
}

//  void QRectF::setWidth(qreal w)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF8setWidthEd(QRectF *self, qreal w) {
  self->setWidth(w);
}

//  void QRectF::setHeight(qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF9setHeightEd(QRectF *self, qreal h) {
  self->setHeight(h);
}

//  void QRectF::setSize(const QSizeF &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectF7setSizeERK6QSizeF(QRectF *self, const QSizeF *s) {
  self->setSize(*s);
}

//  QRectF QRectF::operator|(const QRectF &r) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK6QRectForERKS_(const QRectF *self, const QRectF *r) {
  return new QRectF(self->operator|(*r));
}

//  QRectF QRectF::operator&(const QRectF &r) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK6QRectFanERKS_(const QRectF *self, const QRectF *r) {
  return new QRectF(self->operator&(*r));
}

//  QRectF &QRectF::operator|=(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectFoRERKS_(QRectF *self, const QRectF *r) {
  self->operator|=(*r);
}

//  QRectF &QRectF::operator&=(const QRectF &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectFaNERKS_(QRectF *self, const QRectF *r) {
  self->operator&=(*r);
}

//  bool QRectF::contains(const QRectF &r) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QRectF8containsERKS_(const QRectF *self, const QRectF *r) {
  return self->contains(*r);
}

//  bool QRectF::contains(const QPointF &p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QRectF8containsERK7QPointF(
    const QRectF *self,
    const QPointF *p) {
  return self->contains(*p);
}

//  bool QRectF::contains(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QRectF8containsEdd(const QRectF *self, qreal x, qreal y) {
  return self->contains(x, y);
}

//  QRectF QRectF::united(const QRectF &other) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK6QRectF6unitedERKS_(
    const QRectF *self,
    const QRectF *other) {
  return new QRectF(self->united(*other));
}

//  QRectF QRectF::intersected(const QRectF &other) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK6QRectF11intersectedERKS_(
    const QRectF *self,
    const QRectF *other) {
  return new QRectF(self->intersected(*other));
}

//  bool QRectF::intersects(const QRectF &r) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QRectF10intersectsERKS_(
    const QRectF *self,
    const QRectF *r) {
  return self->intersects(*r);
}

//  QRectF QRectF::marginsAdded(const QMarginsF &margins) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK6QRectF12marginsAddedERK9QMarginsF(
    const QRectF *self,
    const QMarginsF *margins) {
  return new QRectF(self->marginsAdded(*margins));
}

//  QRectF QRectF::marginsRemoved(const QMarginsF &margins) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK6QRectF14marginsRemovedERK9QMarginsF(
    const QRectF *self,
    const QMarginsF *margins) {
  return new QRectF(self->marginsRemoved(*margins));
}

//  QRectF &QRectF::operator+=(const QMarginsF &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectFpLERK9QMarginsF(
    QRectF *self,
    const QMarginsF *margins) {
  self->operator+=(*margins);
}

//  QRectF &QRectF::operator-=(const QMarginsF &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectFmIERK9QMarginsF(
    QRectF *self,
    const QMarginsF *margins) {
  self->operator-=(*margins);
}

//  bool operator==(const QRectF &lhs, const QRectF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QRectFS1_(const QRectF *lhs, const QRectF *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QRectF &lhs, const QRectF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QRectFS1_(const QRectF *lhs, const QRectF *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QRectF &lhs, const QRect &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QRectFRK5QRect(const QRectF *lhs, const QRect *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QRectF &lhs, const QRect &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QRectFRK5QRect(const QRectF *lhs, const QRect *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QRect &lhs, const QRectF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QRectRK6QRectF(const QRect *lhs, const QRectF *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QRect &lhs, const QRectF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QRectRK6QRectF(const QRect *lhs, const QRectF *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QRect QRectF::toRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK6QRectF6toRectEv(const QRectF *self) {
  return new QRect(self->toRect());
}

//  QRect QRectF::toAlignedRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK6QRectF13toAlignedRectEv(const QRectF *self) {
  return new QRect(self->toAlignedRect());
}

//  QRectF::~QRectF()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QRectFD1Ev(QRectF *self) {
  delete self;
}

//  QList<QRectF>::QList()
extern "C" Q_DECL_EXPORT
QList<QRectF> *ritual_list_make_QRectF() {
  return new QList<QRectF>();
}

//  void QList<QRectF>::append(const QRectF &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QRectF(QList<QRectF> *self, const QRectF *element) {
  self->append(*element);
}

//  qsizetype QList<QRectF>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QRectF(const QList<QRectF> *self) {
  return self->size();
}

//  const QRectF &QList<QRectF>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_list_at_QRectF(const QList<QRectF> *self, long long index) {
  return new QRectF(self->at(index));
}

//  QList<QRectF>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QRectF(QList<QRectF> *self) {
  delete self;
}
