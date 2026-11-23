//  Written by dev_tooling.RitualGenerator from the records of QtGui/qpen.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpen.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtCore/qvariant.h>

//  QPen::QPen()
extern "C" Q_DECL_EXPORT
QPen *ritual_ZN4QPenC1Ev() {
  return new QPen();
}

//  QPen::QPen(Qt::PenStyle a0)
extern "C" Q_DECL_EXPORT
QPen *ritual_ZN4QPenC1EN2Qt8PenStyleE(Qt::PenStyle a0) {
  return new QPen(a0);
}

//  QPen::QPen(const QColor &color)
extern "C" Q_DECL_EXPORT
QPen *ritual_ZN4QPenC1ERK6QColor(const QColor *color) {
  return new QPen(*color);
}

//  QPen::QPen(const QBrush &brush, qreal width, Qt::PenStyle s,
//      Qt::PenCapStyle c, Qt::PenJoinStyle j)
extern "C" Q_DECL_EXPORT
QPen *ritual_ZN4QPenC1ERK6QBrushdN2Qt8PenStyleENS3_11PenCapStyleENS3_12PenJoinStyleE(
    const QBrush *brush,
    qreal width,
    Qt::PenStyle s,
    Qt::PenCapStyle c,
    Qt::PenJoinStyle j) {
  return new QPen(*brush, width, s, c, j);
}

//  QPen::QPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
QPen *ritual_ZN4QPenC1ERKS_(const QPen *pen) {
  return new QPen(*pen);
}

//  QPen::~QPen()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPenD1Ev(QPen *self) {
  delete self;
}

//  Qt::PenStyle QPen::style() const
extern "C" Q_DECL_EXPORT
Qt::PenStyle ritual_ZNK4QPen5styleEv(const QPen *self) {
  return self->style();
}

//  void QPen::setStyle(Qt::PenStyle a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPen8setStyleEN2Qt8PenStyleE(QPen *self, Qt::PenStyle a0) {
  self->setStyle(a0);
}

//  qreal QPen::dashOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK4QPen10dashOffsetEv(const QPen *self) {
  return self->dashOffset();
}

//  void QPen::setDashOffset(qreal doffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPen13setDashOffsetEd(QPen *self, qreal doffset) {
  self->setDashOffset(doffset);
}

//  qreal QPen::miterLimit() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK4QPen10miterLimitEv(const QPen *self) {
  return self->miterLimit();
}

//  void QPen::setMiterLimit(qreal limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPen13setMiterLimitEd(QPen *self, qreal limit) {
  self->setMiterLimit(limit);
}

//  qreal QPen::widthF() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK4QPen6widthFEv(const QPen *self) {
  return self->widthF();
}

//  void QPen::setWidthF(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPen9setWidthFEd(QPen *self, qreal width) {
  self->setWidthF(width);
}

//  int QPen::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QPen5widthEv(const QPen *self) {
  return self->width();
}

//  void QPen::setWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPen8setWidthEi(QPen *self, int width) {
  self->setWidth(width);
}

//  QColor QPen::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK4QPen5colorEv(const QPen *self) {
  return new QColor(self->color());
}

//  void QPen::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPen8setColorERK6QColor(QPen *self, const QColor *color) {
  self->setColor(*color);
}

//  QBrush QPen::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK4QPen5brushEv(const QPen *self) {
  return new QBrush(self->brush());
}

//  void QPen::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPen8setBrushERK6QBrush(QPen *self, const QBrush *brush) {
  self->setBrush(*brush);
}

//  bool QPen::isSolid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QPen7isSolidEv(const QPen *self) {
  return self->isSolid();
}

//  Qt::PenCapStyle QPen::capStyle() const
extern "C" Q_DECL_EXPORT
Qt::PenCapStyle ritual_ZNK4QPen8capStyleEv(const QPen *self) {
  return self->capStyle();
}

//  void QPen::setCapStyle(Qt::PenCapStyle pcs)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPen11setCapStyleEN2Qt11PenCapStyleE(
    QPen *self,
    Qt::PenCapStyle pcs) {
  self->setCapStyle(pcs);
}

//  Qt::PenJoinStyle QPen::joinStyle() const
extern "C" Q_DECL_EXPORT
Qt::PenJoinStyle ritual_ZNK4QPen9joinStyleEv(const QPen *self) {
  return self->joinStyle();
}

//  void QPen::setJoinStyle(Qt::PenJoinStyle pcs)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPen12setJoinStyleEN2Qt12PenJoinStyleE(
    QPen *self,
    Qt::PenJoinStyle pcs) {
  self->setJoinStyle(pcs);
}

//  bool QPen::isCosmetic() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QPen10isCosmeticEv(const QPen *self) {
  return self->isCosmetic();
}

//  void QPen::setCosmetic(bool cosmetic)
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPen11setCosmeticEb(QPen *self, bool cosmetic) {
  self->setCosmetic(cosmetic);
}

//  bool QPen::operator==(const QPen &p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QPeneqERKS_(const QPen *self, const QPen *p) {
  return self->operator==(*p);
}

//  bool QPen::operator!=(const QPen &p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QPenneERKS_(const QPen *self, const QPen *p) {
  return self->operator!=(*p);
}

//  QVariant QPen::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK4QPencv8QVariantEv(const QPen *self) {
  return new QVariant(self->operator QVariant());
}

//  bool QPen::isDetached()
extern "C" Q_DECL_EXPORT
bool ritual_ZN4QPen10isDetachedEv(QPen *self) {
  return self->isDetached();
}

//  bool QPen::isSolidDefaultLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QPen18isSolidDefaultLineEv(const QPen *self) {
  return self->isSolidDefaultLine();
}

//  bool QPen::doCompareEqualColor(QColor rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QPen19doCompareEqualColorE6QColor(
    const QPen *self,
    const QColor *rhs) {
  return self->doCompareEqualColor(*rhs);
}

//  bool operator==(const QPen &lhs, const QColor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK4QPenRK6QColor(const QPen *lhs, const QColor *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPen &lhs, const QColor &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK4QPenRK6QColor(const QPen *lhs, const QColor *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QColor &lhs, const QPen &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QColorRK4QPen(const QColor *lhs, const QPen *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QColor &lhs, const QPen &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QColorRK4QPen(const QColor *lhs, const QPen *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool QPen::doCompareEqualStyle(Qt::PenStyle rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK4QPen19doCompareEqualStyleEN2Qt8PenStyleE(
    const QPen *self,
    Qt::PenStyle rhs) {
  return self->doCompareEqualStyle(rhs);
}

//  void QPen::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QPen6detachEv(QPen *self) {
  self->detach();
}
