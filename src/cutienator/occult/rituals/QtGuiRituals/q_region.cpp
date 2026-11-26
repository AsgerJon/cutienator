//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qregion.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qregion.h>
#include <QtCore/qrect.h>
#include <QtGui/qpolygon.h>
#include <QtGui/qbitmap.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtGui/QRegion>
#include <QtCore/QSpan>
#include <QtCore/QRect>

//  QRegion::QRegion()
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN7QRegionC1Ev() {
  return new QRegion();
}

//  QRegion::QRegion(int x, int y, int w, int h, RegionType t)
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN7QRegionC1EiiiiNS_10RegionTypeE(
    int x,
    int y,
    int w,
    int h,
    QRegion::RegionType t) {
  return new QRegion(x, y, w, h, t);
}

//  QRegion::QRegion(const QRect &r, RegionType t)
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN7QRegionC1ERK5QRectNS_10RegionTypeE(
    const QRect *r,
    QRegion::RegionType t) {
  return new QRegion(*r, t);
}

//  QRegion::QRegion(const QPolygon &pa, Qt::FillRule fillRule)
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN7QRegionC1ERK8QPolygonN2Qt8FillRuleE(
    const QPolygon *pa,
    Qt::FillRule fillRule) {
  return new QRegion(*pa, fillRule);
}

//  QRegion::QRegion(const QRegion &region)
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN7QRegionC1ERKS_(const QRegion *region) {
  return new QRegion(*region);
}

//  QRegion::QRegion(QRegion &&other)
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN7QRegionC1EOS_(QRegion *other) {
  return new QRegion(std::move(*other));
}

//  QRegion::QRegion(const QBitmap &bitmap)
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN7QRegionC1ERK7QBitmap(const QBitmap *bitmap) {
  return new QRegion(*bitmap);
}

//  QRegion::~QRegion()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegionD1Ev(QRegion *self) {
  delete self;
}

//  QRegion &QRegion::operator=(const QRegion &a0)
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN7QRegionaSERKS_(QRegion *self, const QRegion *a0) {
  return &(self->operator=(*a0));
}

//  QRegion &QRegion::operator=(QRegion &&other)
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN7QRegionaSEOS_(QRegion *self, QRegion *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QRegion::swap(QRegion &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegion4swapERS_(QRegion *self, QRegion *other) {
  self->swap(*other);
}

//  bool QRegion::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegion7isEmptyEv(const QRegion *self) {
  return self->isEmpty();
}

//  bool QRegion::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegion6isNullEv(const QRegion *self) {
  return self->isNull();
}

//  const_iterator QRegion::begin() const
extern "C" Q_DECL_EXPORT
QRegion::const_iterator ritual_ZNK7QRegion5beginEv(const QRegion *self) {
  return self->begin();
}

//  const_iterator QRegion::cbegin() const
extern "C" Q_DECL_EXPORT
QRegion::const_iterator ritual_ZNK7QRegion6cbeginEv(const QRegion *self) {
  return self->cbegin();
}

//  const_iterator QRegion::end() const
extern "C" Q_DECL_EXPORT
QRegion::const_iterator ritual_ZNK7QRegion3endEv(const QRegion *self) {
  return self->end();
}

//  const_iterator QRegion::cend() const
extern "C" Q_DECL_EXPORT
QRegion::const_iterator ritual_ZNK7QRegion4cendEv(const QRegion *self) {
  return self->cend();
}

//  const_reverse_iterator QRegion::rbegin() const
extern "C" Q_DECL_EXPORT
QRegion::const_reverse_iterator *ritual_ZNK7QRegion6rbeginEv(
    const QRegion *self) {
  return new QRegion::const_reverse_iterator(self->rbegin());
}

//  const_reverse_iterator QRegion::crbegin() const
extern "C" Q_DECL_EXPORT
QRegion::const_reverse_iterator *ritual_ZNK7QRegion7crbeginEv(
    const QRegion *self) {
  return new QRegion::const_reverse_iterator(self->crbegin());
}

//  const_reverse_iterator QRegion::rend() const
extern "C" Q_DECL_EXPORT
QRegion::const_reverse_iterator *ritual_ZNK7QRegion4rendEv(
    const QRegion *self) {
  return new QRegion::const_reverse_iterator(self->rend());
}

//  const_reverse_iterator QRegion::crend() const
extern "C" Q_DECL_EXPORT
QRegion::const_reverse_iterator *ritual_ZNK7QRegion5crendEv(
    const QRegion *self) {
  return new QRegion::const_reverse_iterator(self->crend());
}

//  bool QRegion::contains(const QPoint &p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegion8containsERK6QPoint(
    const QRegion *self,
    const QPoint *p) {
  return self->contains(*p);
}

//  bool QRegion::contains(const QRect &r) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegion8containsERK5QRect(
    const QRegion *self,
    const QRect *r) {
  return self->contains(*r);
}

//  void QRegion::translate(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegion9translateEii(QRegion *self, int dx, int dy) {
  self->translate(dx, dy);
}

//  void QRegion::translate(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegion9translateERK6QPoint(QRegion *self, const QPoint *p) {
  self->translate(*p);
}

//  QRegion QRegion::translated(int dx, int dy) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegion10translatedEii(
    const QRegion *self,
    int dx,
    int dy) {
  return new QRegion(self->translated(dx, dy));
}

//  QRegion QRegion::translated(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegion10translatedERK6QPoint(
    const QRegion *self,
    const QPoint *p) {
  return new QRegion(self->translated(*p));
}

//  QRegion QRegion::united(const QRegion &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegion6unitedERKS_(
    const QRegion *self,
    const QRegion *r) {
  return new QRegion(self->united(*r));
}

//  QRegion QRegion::united(const QRect &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegion6unitedERK5QRect(
    const QRegion *self,
    const QRect *r) {
  return new QRegion(self->united(*r));
}

//  QRegion QRegion::intersected(const QRegion &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegion11intersectedERKS_(
    const QRegion *self,
    const QRegion *r) {
  return new QRegion(self->intersected(*r));
}

//  QRegion QRegion::intersected(const QRect &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegion11intersectedERK5QRect(
    const QRegion *self,
    const QRect *r) {
  return new QRegion(self->intersected(*r));
}

//  QRegion QRegion::subtracted(const QRegion &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegion10subtractedERKS_(
    const QRegion *self,
    const QRegion *r) {
  return new QRegion(self->subtracted(*r));
}

//  QRegion QRegion::xored(const QRegion &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegion5xoredERKS_(
    const QRegion *self,
    const QRegion *r) {
  return new QRegion(self->xored(*r));
}

//  bool QRegion::intersects(const QRegion &r) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegion10intersectsERKS_(
    const QRegion *self,
    const QRegion *r) {
  return self->intersects(*r);
}

//  bool QRegion::intersects(const QRect &r) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegion10intersectsERK5QRect(
    const QRegion *self,
    const QRect *r) {
  return self->intersects(*r);
}

//  QRect QRegion::boundingRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK7QRegion12boundingRectEv(const QRegion *self) {
  return new QRect(self->boundingRect());
}

//  void QRegion::setRects(const QRect *rect, int num)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegion8setRectsEPK5QRecti(
    QRegion *self,
    const QRect *rect,
    int num) {
  self->setRects(rect, num);
}

//  void QRegion::setRects(QSpan<const QRect> r)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegion8setRectsE5QSpanIK5QRectLm18446744073709551615EE(
    QRegion *self,
    const QSpan<const QRect> *r) {
  self->setRects(*r);
}

//  QSpan<const QRect> QRegion::rects() const
extern "C" Q_DECL_EXPORT
QSpan<const QRect> *ritual_ZNK7QRegion5rectsEv(const QRegion *self) {
  return new QSpan<const QRect>(self->rects());
}

//  int QRegion::rectCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QRegion9rectCountEv(const QRegion *self) {
  return self->rectCount();
}

//  QRegion QRegion::operator|(const QRegion &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegionorERKS_(const QRegion *self, const QRegion *r) {
  return new QRegion(self->operator|(*r));
}

//  QRegion QRegion::operator+(const QRegion &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegionplERKS_(const QRegion *self, const QRegion *r) {
  return new QRegion(self->operator+(*r));
}

//  QRegion QRegion::operator+(const QRect &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegionplERK5QRect(const QRegion *self, const QRect *r) {
  return new QRegion(self->operator+(*r));
}

//  QRegion QRegion::operator&(const QRegion &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegionanERKS_(const QRegion *self, const QRegion *r) {
  return new QRegion(self->operator&(*r));
}

//  QRegion QRegion::operator&(const QRect &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegionanERK5QRect(const QRegion *self, const QRect *r) {
  return new QRegion(self->operator&(*r));
}

//  QRegion QRegion::operator-(const QRegion &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegionmiERKS_(const QRegion *self, const QRegion *r) {
  return new QRegion(self->operator-(*r));
}

//  QRegion QRegion::operator^(const QRegion &r) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegioneoERKS_(const QRegion *self, const QRegion *r) {
  return new QRegion(self->operator^(*r));
}

//  QRegion &QRegion::operator|=(const QRegion &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegionoRERKS_(QRegion *self, const QRegion *r) {
  self->operator|=(*r);
}

//  QRegion &QRegion::operator+=(const QRegion &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegionpLERKS_(QRegion *self, const QRegion *r) {
  self->operator+=(*r);
}

//  QRegion &QRegion::operator+=(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegionpLERK5QRect(QRegion *self, const QRect *r) {
  self->operator+=(*r);
}

//  QRegion &QRegion::operator&=(const QRegion &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegionaNERKS_(QRegion *self, const QRegion *r) {
  self->operator&=(*r);
}

//  QRegion &QRegion::operator&=(const QRect &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegionaNERK5QRect(QRegion *self, const QRect *r) {
  self->operator&=(*r);
}

//  QRegion &QRegion::operator-=(const QRegion &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegionmIERKS_(QRegion *self, const QRegion *r) {
  self->operator-=(*r);
}

//  QRegion &QRegion::operator^=(const QRegion &r)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegioneOERKS_(QRegion *self, const QRegion *r) {
  self->operator^=(*r);
}

//  bool QRegion::operator==(const QRegion &r) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegioneqERKS_(const QRegion *self, const QRegion *r) {
  return self->operator==(*r);
}

//  bool QRegion::operator!=(const QRegion &r) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QRegionneERKS_(const QRegion *self, const QRegion *r) {
  return self->operator!=(*r);
}

//  QVariant QRegion::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK7QRegioncv8QVariantEv(const QRegion *self) {
  return new QVariant(self->operator QVariant());
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &a0, const QRegion &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK7QRegion(
    QDataStream *a0,
    const QRegion *a1) {
  return &(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &a0, QRegion &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR7QRegion(
    QDataStream *a0,
    QRegion *a1) {
  return &(operator>>(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

//  QRegion QRegion::copy() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK7QRegion4copyEv(const QRegion *self) {
  return new QRegion(self->copy());
}

//  void QRegion::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegion6detachEv(QRegion *self) {
  self->detach();
}

#if !defined(QT_NO_DATASTREAM)
//  void QRegion::exec(const QByteArray &ba, int ver, QDataStream::ByteOrder
//      byteOrder)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegion4execERK10QByteArrayiN11QDataStream9ByteOrderE(
    QRegion *self,
    const QByteArray *ba,
    int ver,
    QDataStream::ByteOrder byteOrder) {
  self->exec(*ba, ver, byteOrder);
}
#endif  // !defined(QT_NO_DATASTREAM)

//  void QRegion::cleanUp(QRegionData *x)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QRegion7cleanUpEPNS_11QRegionDataE(QRegion::QRegionData *x) {
  QRegion::cleanUp(x);
}

//  a QRegion::const_reverse_iterator a ritual of QRegion gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QRegion__QRegion_const_reverse_iterator(
    QRegion::const_reverse_iterator *self) {
  delete self;
}

//  a QSpan<const QRect> a ritual of QRegion gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QRegion__QSpan_const_QRect(QSpan<const QRect> *self) {
  delete self;
}
