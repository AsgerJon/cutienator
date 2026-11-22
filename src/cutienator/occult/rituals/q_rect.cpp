//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrect.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qmargins.h>

//  QRect::QRect()
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN5QRectC1Ev() {
  return new QRect();
}

//  QRect::QRect(const QPoint &topleft, const QPoint &bottomright)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN5QRectC1ERK6QPointS2_(
    const QPoint *topleft,
    const QPoint *bottomright) {
  return new QRect(*topleft, *bottomright);
}

//  QRect::QRect(const QPoint &topleft, const QSize &size)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN5QRectC1ERK6QPointRK5QSize(
    const QPoint *topleft,
    const QSize *size) {
  return new QRect(*topleft, *size);
}

//  QRect::QRect(int left, int top, int width, int height)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN5QRectC1Eiiii(int left, int top, int width, int height) {
  return new QRect(left, top, width, height);
}

//  bool QRect::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QRect6isNullEv(const QRect *self) {
  return self->isNull();
}

//  bool QRect::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QRect7isEmptyEv(const QRect *self) {
  return self->isEmpty();
}

//  bool QRect::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QRect7isValidEv(const QRect *self) {
  return self->isValid();
}

//  int QRect::left() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QRect4leftEv(const QRect *self) {
  return self->left();
}

//  int QRect::top() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QRect3topEv(const QRect *self) {
  return self->top();
}

//  int QRect::right() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QRect5rightEv(const QRect *self) {
  return self->right();
}

//  int QRect::bottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QRect6bottomEv(const QRect *self) {
  return self->bottom();
}

//  QRect QRect::normalized() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QRect10normalizedEv(const QRect *self) {
  return new QRect(self->normalized());
}

//  int QRect::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QRect1xEv(const QRect *self) {
  return self->x();
}

//  int QRect::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QRect1yEv(const QRect *self) {
  return self->y();
}

//  void QRect::setLeft(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect7setLeftEi(QRect *self, int pos) {
  self->setLeft(pos);
}

//  void QRect::setTop(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect6setTopEi(QRect *self, int pos) {
  self->setTop(pos);
}

//  void QRect::setRight(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect8setRightEi(QRect *self, int pos) {
  self->setRight(pos);
}

//  void QRect::setBottom(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect9setBottomEi(QRect *self, int pos) {
  self->setBottom(pos);
}

//  void QRect::setX(int x)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect4setXEi(QRect *self, int x) {
  self->setX(x);
}

//  void QRect::setY(int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect4setYEi(QRect *self, int y) {
  self->setY(y);
}

//  void QRect::setTopLeft(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect10setTopLeftERK6QPoint(QRect *self, const QPoint *p) {
  self->setTopLeft(*p);
}

//  void QRect::setBottomRight(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect14setBottomRightERK6QPoint(
    QRect *self,
    const QPoint *p) {
  self->setBottomRight(*p);
}

//  void QRect::setTopRight(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect11setTopRightERK6QPoint(QRect *self, const QPoint *p) {
  self->setTopRight(*p);
}

//  void QRect::setBottomLeft(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect13setBottomLeftERK6QPoint(QRect *self, const QPoint *p) {
  self->setBottomLeft(*p);
}

//  QPoint QRect::topLeft() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK5QRect7topLeftEv(const QRect *self) {
  return new QPoint(self->topLeft());
}

//  QPoint QRect::bottomRight() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK5QRect11bottomRightEv(const QRect *self) {
  return new QPoint(self->bottomRight());
}

//  QPoint QRect::topRight() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK5QRect8topRightEv(const QRect *self) {
  return new QPoint(self->topRight());
}

//  QPoint QRect::bottomLeft() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK5QRect10bottomLeftEv(const QRect *self) {
  return new QPoint(self->bottomLeft());
}

//  QPoint QRect::center() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK5QRect6centerEv(const QRect *self) {
  return new QPoint(self->center());
}

//  void QRect::moveLeft(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect8moveLeftEi(QRect *self, int pos) {
  self->moveLeft(pos);
}

//  void QRect::moveTop(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect7moveTopEi(QRect *self, int pos) {
  self->moveTop(pos);
}

//  void QRect::moveRight(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect9moveRightEi(QRect *self, int pos) {
  self->moveRight(pos);
}

//  void QRect::moveBottom(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect10moveBottomEi(QRect *self, int pos) {
  self->moveBottom(pos);
}

//  void QRect::moveTopLeft(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect11moveTopLeftERK6QPoint(QRect *self, const QPoint *p) {
  self->moveTopLeft(*p);
}

//  void QRect::moveBottomRight(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect15moveBottomRightERK6QPoint(
    QRect *self,
    const QPoint *p) {
  self->moveBottomRight(*p);
}

//  void QRect::moveTopRight(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect12moveTopRightERK6QPoint(QRect *self, const QPoint *p) {
  self->moveTopRight(*p);
}

//  void QRect::moveBottomLeft(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect14moveBottomLeftERK6QPoint(
    QRect *self,
    const QPoint *p) {
  self->moveBottomLeft(*p);
}

//  void QRect::moveCenter(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect10moveCenterERK6QPoint(QRect *self, const QPoint *p) {
  self->moveCenter(*p);
}

//  void QRect::translate(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect9translateEii(QRect *self, int dx, int dy) {
  self->translate(dx, dy);
}

//  void QRect::translate(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect9translateERK6QPoint(QRect *self, const QPoint *p) {
  self->translate(*p);
}

//  QRect QRect::translated(int dx, int dy) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QRect10translatedEii(const QRect *self, int dx, int dy) {
  return new QRect(self->translated(dx, dy));
}

//  QRect QRect::translated(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QRect10translatedERK6QPoint(
    const QRect *self,
    const QPoint *p) {
  return new QRect(self->translated(*p));
}

//  QRect QRect::transposed() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QRect10transposedEv(const QRect *self) {
  return new QRect(self->transposed());
}

//  void QRect::moveTo(int x, int t)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect6moveToEii(QRect *self, int x, int t) {
  self->moveTo(x, t);
}

//  void QRect::moveTo(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect6moveToERK6QPoint(QRect *self, const QPoint *p) {
  self->moveTo(*p);
}

//  void QRect::setRect(int x, int y, int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect7setRectEiiii(QRect *self, int x, int y, int w, int h) {
  self->setRect(x, y, w, h);
}

//  void QRect::getRect(int *x, int *y, int *w, int *h) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK5QRect7getRectEPiS0_S0_S0_(
    const QRect *self,
    int *x,
    int *y,
    int *w,
    int *h) {
  self->getRect(x, y, w, h);
}

//  void QRect::setCoords(int x1, int y1, int x2, int y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect9setCoordsEiiii(
    QRect *self,
    int x1,
    int y1,
    int x2,
    int y2) {
  self->setCoords(x1, y1, x2, y2);
}

//  void QRect::getCoords(int *x1, int *y1, int *x2, int *y2) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK5QRect9getCoordsEPiS0_S0_S0_(
    const QRect *self,
    int *x1,
    int *y1,
    int *x2,
    int *y2) {
  self->getCoords(x1, y1, x2, y2);
}

//  void QRect::adjust(int x1, int y1, int x2, int y2)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect6adjustEiiii(
    QRect *self,
    int x1,
    int y1,
    int x2,
    int y2) {
  self->adjust(x1, y1, x2, y2);
}

//  QRect QRect::adjusted(int x1, int y1, int x2, int y2) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QRect8adjustedEiiii(
    const QRect *self,
    int x1,
    int y1,
    int x2,
    int y2) {
  return new QRect(self->adjusted(x1, y1, x2, y2));
}

//  QSize QRect::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK5QRect4sizeEv(const QRect *self) {
  return new QSize(self->size());
}

//  int QRect::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QRect5widthEv(const QRect *self) {
  return self->width();
}

//  int QRect::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK5QRect6heightEv(const QRect *self) {
  return self->height();
}

//  void QRect::setWidth(int w)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect8setWidthEi(QRect *self, int w) {
  self->setWidth(w);
}

//  void QRect::setHeight(int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect9setHeightEi(QRect *self, int h) {
  self->setHeight(h);
}

//  void QRect::setSize(const QSize &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRect7setSizeERK5QSize(QRect *self, const QSize *s) {
  self->setSize(*s);
}

//  QRect QRect::operator|(const QRect &r) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QRectorERKS_(const QRect *self, const QRect *r) {
  return new QRect(self->operator|(*r));
}

//  QRect QRect::operator&(const QRect &r) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QRectanERKS_(const QRect *self, const QRect *r) {
  return new QRect(self->operator&(*r));
}

//  QRect &QRect::operator|=(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRectoRERKS_(QRect *self, const QRect *r) {
  self->operator|=(*r);
}

//  QRect &QRect::operator&=(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRectaNERKS_(QRect *self, const QRect *r) {
  self->operator&=(*r);
}

//  bool QRect::contains(const QRect &r, bool proper) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QRect8containsERKS_b(
    const QRect *self,
    const QRect *r,
    bool proper) {
  return self->contains(*r, proper);
}

//  bool QRect::contains(const QPoint &p, bool proper) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QRect8containsERK6QPointb(
    const QRect *self,
    const QPoint *p,
    bool proper) {
  return self->contains(*p, proper);
}

//  bool QRect::contains(int x, int y) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QRect8containsEii(const QRect *self, int x, int y) {
  return self->contains(x, y);
}

//  bool QRect::contains(int x, int y, bool proper) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QRect8containsEiib(
    const QRect *self,
    int x,
    int y,
    bool proper) {
  return self->contains(x, y, proper);
}

//  QRect QRect::united(const QRect &other) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QRect6unitedERKS_(const QRect *self, const QRect *other) {
  return new QRect(self->united(*other));
}

//  QRect QRect::intersected(const QRect &other) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QRect11intersectedERKS_(
    const QRect *self,
    const QRect *other) {
  return new QRect(self->intersected(*other));
}

//  bool QRect::intersects(const QRect &r) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QRect10intersectsERKS_(const QRect *self, const QRect *r) {
  return self->intersects(*r);
}

//  QRect QRect::marginsAdded(const QMargins &margins) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QRect12marginsAddedERK8QMargins(
    const QRect *self,
    const QMargins *margins) {
  return new QRect(self->marginsAdded(*margins));
}

//  QRect QRect::marginsRemoved(const QMargins &margins) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK5QRect14marginsRemovedERK8QMargins(
    const QRect *self,
    const QMargins *margins) {
  return new QRect(self->marginsRemoved(*margins));
}

//  QRect &QRect::operator+=(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRectpLERK8QMargins(QRect *self, const QMargins *margins) {
  self->operator+=(*margins);
}

//  QRect &QRect::operator-=(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRectmIERK8QMargins(QRect *self, const QMargins *margins) {
  self->operator-=(*margins);
}

//  QRect QRect::span(const QPoint &p1, const QPoint &p2)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN5QRect4spanERK6QPointS2_(
    const QPoint *p1,
    const QPoint *p2) {
  return new QRect(QRect::span(*p1, *p2));
}

//  bool operator==(const QRect &lhs, const QRect &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QRectS1_(const QRect *lhs, const QRect *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QRect &lhs, const QRect &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QRectS1_(const QRect *lhs, const QRect *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QRectF QRect::toRectF() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK5QRect7toRectFEv(const QRect *self) {
  return new QRectF(self->toRectF());
}

//  QRect::~QRect()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QRectD1Ev(QRect *self) {
  delete self;
}
