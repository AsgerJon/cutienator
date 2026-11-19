//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpagesize.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpagesize.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>

//  QPageSize::QPageSize()
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZN9QPageSizeC1Ev() {
  return new QPageSize();
}

//  QPageSize::QPageSize(PageSizeId pageSizeId)
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZN9QPageSizeC1ENS_10PageSizeIdE(
    QPageSize::PageSizeId pageSizeId) {
  return new QPageSize(pageSizeId);
}

//  QPageSize::QPageSize(const QSize &pointSize, const QString &name,
//      SizeMatchPolicy matchPolicy)
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZN9QPageSizeC1ERK5QSizeRK7QStringNS_15SizeMatchPolicyE(
    const QSize *pointSize,
    const QString *name,
    QPageSize::SizeMatchPolicy matchPolicy) {
  return new QPageSize(*pointSize, *name, matchPolicy);
}

//  QPageSize::QPageSize(const QSizeF &size, Unit units, const QString &name,
//      SizeMatchPolicy matchPolicy)
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZN9QPageSizeC1ERK6QSizeFNS_4UnitERK7QStringNS_15SizeMatchPolicyE(
    const QSizeF *size,
    QPageSize::Unit units,
    const QString *name,
    QPageSize::SizeMatchPolicy matchPolicy) {
  return new QPageSize(*size, units, *name, matchPolicy);
}

//  QPageSize::QPageSize(const QPageSize &other)
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZN9QPageSizeC1ERKS_(const QPageSize *other) {
  return new QPageSize(*other);
}

//  QPageSize::~QPageSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QPageSizeD1Ev(QPageSize *self) {
  delete self;
}

//  bool QPageSize::isEquivalentTo(const QPageSize &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QPageSize14isEquivalentToERKS_(
    const QPageSize *self,
    const QPageSize *other) {
  return self->isEquivalentTo(*other);
}

//  bool QPageSize::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QPageSize7isValidEv(const QPageSize *self) {
  return self->isValid();
}

//  QString QPageSize::key() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QPageSize3keyEv(const QPageSize *self) {
  return new QString(self->key());
}

//  QString QPageSize::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QPageSize4nameEv(const QPageSize *self) {
  return new QString(self->name());
}

//  PageSizeId QPageSize::id() const
extern "C" Q_DECL_EXPORT
QPageSize::PageSizeId ritual_ZNK9QPageSize2idEv(const QPageSize *self) {
  return self->id();
}

//  int QPageSize::windowsId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9QPageSize9windowsIdEv(const QPageSize *self) {
  return self->windowsId();
}

//  QSizeF QPageSize::definitionSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK9QPageSize14definitionSizeEv(const QPageSize *self) {
  return new QSizeF(self->definitionSize());
}

//  Unit QPageSize::definitionUnits() const
extern "C" Q_DECL_EXPORT
QPageSize::Unit ritual_ZNK9QPageSize15definitionUnitsEv(
    const QPageSize *self) {
  return self->definitionUnits();
}

//  QSizeF QPageSize::size(Unit units) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK9QPageSize4sizeENS_4UnitE(
    const QPageSize *self,
    QPageSize::Unit units) {
  return new QSizeF(self->size(units));
}

//  QSize QPageSize::sizePoints() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QPageSize10sizePointsEv(const QPageSize *self) {
  return new QSize(self->sizePoints());
}

//  QSize QPageSize::sizePixels(int resolution) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK9QPageSize10sizePixelsEi(
    const QPageSize *self,
    int resolution) {
  return new QSize(self->sizePixels(resolution));
}

//  QRectF QPageSize::rect(Unit units) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK9QPageSize4rectENS_4UnitE(
    const QPageSize *self,
    QPageSize::Unit units) {
  return new QRectF(self->rect(units));
}

//  QRect QPageSize::rectPoints() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK9QPageSize10rectPointsEv(const QPageSize *self) {
  return new QRect(self->rectPoints());
}

//  QRect QPageSize::rectPixels(int resolution) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK9QPageSize10rectPixelsEi(
    const QPageSize *self,
    int resolution) {
  return new QRect(self->rectPixels(resolution));
}

//  QString QPageSize::key(PageSizeId pageSizeId)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QPageSize3keyENS_10PageSizeIdE(
    QPageSize::PageSizeId pageSizeId) {
  return new QString(QPageSize::key(pageSizeId));
}

//  QString QPageSize::name(PageSizeId pageSizeId)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QPageSize4nameENS_10PageSizeIdE(
    QPageSize::PageSizeId pageSizeId) {
  return new QString(QPageSize::name(pageSizeId));
}

//  PageSizeId QPageSize::id(const QSize &pointSize, SizeMatchPolicy
//      matchPolicy)
extern "C" Q_DECL_EXPORT
QPageSize::PageSizeId ritual_ZN9QPageSize2idERK5QSizeNS_15SizeMatchPolicyE(
    const QSize *pointSize,
    QPageSize::SizeMatchPolicy matchPolicy) {
  return QPageSize::id(*pointSize, matchPolicy);
}

//  PageSizeId QPageSize::id(const QSizeF &size, Unit units, SizeMatchPolicy
//      matchPolicy)
extern "C" Q_DECL_EXPORT
QPageSize::PageSizeId ritual_ZN9QPageSize2idERK6QSizeFNS_4UnitENS_15SizeMatchPolicyE(
    const QSizeF *size,
    QPageSize::Unit units,
    QPageSize::SizeMatchPolicy matchPolicy) {
  return QPageSize::id(*size, units, matchPolicy);
}

//  PageSizeId QPageSize::id(int windowsId)
extern "C" Q_DECL_EXPORT
QPageSize::PageSizeId ritual_ZN9QPageSize2idEi(int windowsId) {
  return QPageSize::id(windowsId);
}

//  int QPageSize::windowsId(PageSizeId pageSizeId)
extern "C" Q_DECL_EXPORT
int ritual_ZN9QPageSize9windowsIdENS_10PageSizeIdE(
    QPageSize::PageSizeId pageSizeId) {
  return QPageSize::windowsId(pageSizeId);
}

//  QSizeF QPageSize::definitionSize(PageSizeId pageSizeId)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN9QPageSize14definitionSizeENS_10PageSizeIdE(
    QPageSize::PageSizeId pageSizeId) {
  return new QSizeF(QPageSize::definitionSize(pageSizeId));
}

//  Unit QPageSize::definitionUnits(PageSizeId pageSizeId)
extern "C" Q_DECL_EXPORT
QPageSize::Unit ritual_ZN9QPageSize15definitionUnitsENS_10PageSizeIdE(
    QPageSize::PageSizeId pageSizeId) {
  return QPageSize::definitionUnits(pageSizeId);
}

//  QSizeF QPageSize::size(PageSizeId pageSizeId, Unit units)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN9QPageSize4sizeENS_10PageSizeIdENS_4UnitE(
    QPageSize::PageSizeId pageSizeId,
    QPageSize::Unit units) {
  return new QSizeF(QPageSize::size(pageSizeId, units));
}

//  QSize QPageSize::sizePoints(PageSizeId pageSizeId)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN9QPageSize10sizePointsENS_10PageSizeIdE(
    QPageSize::PageSizeId pageSizeId) {
  return new QSize(QPageSize::sizePoints(pageSizeId));
}

//  QSize QPageSize::sizePixels(PageSizeId pageSizeId, int resolution)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN9QPageSize10sizePixelsENS_10PageSizeIdEi(
    QPageSize::PageSizeId pageSizeId,
    int resolution) {
  return new QSize(QPageSize::sizePixels(pageSizeId, resolution));
}
