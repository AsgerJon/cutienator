//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpagelayout.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpagelayout.h>
#include <QtGui/qpagesize.h>
#include <QtCore/qmargins.h>
#include <QtCore/qrect.h>

//  QPageLayout::QPageLayout()
extern "C" Q_DECL_EXPORT
QPageLayout *ritual_ZN11QPageLayoutC1Ev() {
  return new QPageLayout();
}

//  QPageLayout::QPageLayout(const QPageSize &pageSize, Orientation
//      orientation, const QMarginsF &margins, Unit units, const QMarginsF
//      &minMargins)
extern "C" Q_DECL_EXPORT
QPageLayout *ritual_ZN11QPageLayoutC1ERK9QPageSizeNS_11OrientationERK9QMarginsFNS_4UnitES6_(
    const QPageSize *pageSize,
    QPageLayout::Orientation orientation,
    const QMarginsF *margins,
    QPageLayout::Unit units,
    const QMarginsF *minMargins) {
  return new QPageLayout(
      *pageSize,
      orientation,
      *margins,
      units,
      *minMargins);
}

//  QPageLayout::QPageLayout(const QPageLayout &other)
extern "C" Q_DECL_EXPORT
QPageLayout *ritual_ZN11QPageLayoutC1ERKS_(const QPageLayout *other) {
  return new QPageLayout(*other);
}

//  QPageLayout::~QPageLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageLayoutD1Ev(QPageLayout *self) {
  delete self;
}

//  bool QPageLayout::isEquivalentTo(const QPageLayout &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPageLayout14isEquivalentToERKS_(
    const QPageLayout *self,
    const QPageLayout *other) {
  return self->isEquivalentTo(*other);
}

//  bool QPageLayout::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QPageLayout7isValidEv(const QPageLayout *self) {
  return self->isValid();
}

//  void QPageLayout::setMode(Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageLayout7setModeENS_4ModeE(
    QPageLayout *self,
    QPageLayout::Mode mode) {
  self->setMode(mode);
}

//  Mode QPageLayout::mode() const
extern "C" Q_DECL_EXPORT
QPageLayout::Mode ritual_ZNK11QPageLayout4modeEv(const QPageLayout *self) {
  return self->mode();
}

//  void QPageLayout::setPageSize(const QPageSize &pageSize, const QMarginsF
//      &minMargins)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageLayout11setPageSizeERK9QPageSizeRK9QMarginsF(
    QPageLayout *self,
    const QPageSize *pageSize,
    const QMarginsF *minMargins) {
  self->setPageSize(*pageSize, *minMargins);
}

//  QPageSize QPageLayout::pageSize() const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK11QPageLayout8pageSizeEv(const QPageLayout *self) {
  return new QPageSize(self->pageSize());
}

//  void QPageLayout::setOrientation(Orientation orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageLayout14setOrientationENS_11OrientationE(
    QPageLayout *self,
    QPageLayout::Orientation orientation) {
  self->setOrientation(orientation);
}

//  Orientation QPageLayout::orientation() const
extern "C" Q_DECL_EXPORT
QPageLayout::Orientation ritual_ZNK11QPageLayout11orientationEv(
    const QPageLayout *self) {
  return self->orientation();
}

//  void QPageLayout::setUnits(Unit units)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageLayout8setUnitsENS_4UnitE(
    QPageLayout *self,
    QPageLayout::Unit units) {
  self->setUnits(units);
}

//  Unit QPageLayout::units() const
extern "C" Q_DECL_EXPORT
QPageLayout::Unit ritual_ZNK11QPageLayout5unitsEv(const QPageLayout *self) {
  return self->units();
}

//  bool QPageLayout::setMargins(const QMarginsF &margins, OutOfBoundsPolicy
//      outOfBoundsPolicy)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QPageLayout10setMarginsERK9QMarginsFNS_17OutOfBoundsPolicyE(
    QPageLayout *self,
    const QMarginsF *margins,
    QPageLayout::OutOfBoundsPolicy outOfBoundsPolicy) {
  return self->setMargins(*margins, outOfBoundsPolicy);
}

//  bool QPageLayout::setLeftMargin(qreal leftMargin, OutOfBoundsPolicy
//      outOfBoundsPolicy)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QPageLayout13setLeftMarginEdNS_17OutOfBoundsPolicyE(
    QPageLayout *self,
    qreal leftMargin,
    QPageLayout::OutOfBoundsPolicy outOfBoundsPolicy) {
  return self->setLeftMargin(leftMargin, outOfBoundsPolicy);
}

//  bool QPageLayout::setRightMargin(qreal rightMargin, OutOfBoundsPolicy
//      outOfBoundsPolicy)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QPageLayout14setRightMarginEdNS_17OutOfBoundsPolicyE(
    QPageLayout *self,
    qreal rightMargin,
    QPageLayout::OutOfBoundsPolicy outOfBoundsPolicy) {
  return self->setRightMargin(rightMargin, outOfBoundsPolicy);
}

//  bool QPageLayout::setTopMargin(qreal topMargin, OutOfBoundsPolicy
//      outOfBoundsPolicy)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QPageLayout12setTopMarginEdNS_17OutOfBoundsPolicyE(
    QPageLayout *self,
    qreal topMargin,
    QPageLayout::OutOfBoundsPolicy outOfBoundsPolicy) {
  return self->setTopMargin(topMargin, outOfBoundsPolicy);
}

//  bool QPageLayout::setBottomMargin(qreal bottomMargin, OutOfBoundsPolicy
//      outOfBoundsPolicy)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QPageLayout15setBottomMarginEdNS_17OutOfBoundsPolicyE(
    QPageLayout *self,
    qreal bottomMargin,
    QPageLayout::OutOfBoundsPolicy outOfBoundsPolicy) {
  return self->setBottomMargin(bottomMargin, outOfBoundsPolicy);
}

//  QMarginsF QPageLayout::margins() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK11QPageLayout7marginsEv(const QPageLayout *self) {
  return new QMarginsF(self->margins());
}

//  QMarginsF QPageLayout::margins(Unit units) const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK11QPageLayout7marginsENS_4UnitE(
    const QPageLayout *self,
    QPageLayout::Unit units) {
  return new QMarginsF(self->margins(units));
}

//  QMargins QPageLayout::marginsPoints() const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK11QPageLayout13marginsPointsEv(const QPageLayout *self) {
  return new QMargins(self->marginsPoints());
}

//  QMargins QPageLayout::marginsPixels(int resolution) const
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZNK11QPageLayout13marginsPixelsEi(
    const QPageLayout *self,
    int resolution) {
  return new QMargins(self->marginsPixels(resolution));
}

//  void QPageLayout::setMinimumMargins(const QMarginsF &minMargins)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPageLayout17setMinimumMarginsERK9QMarginsF(
    QPageLayout *self,
    const QMarginsF *minMargins) {
  self->setMinimumMargins(*minMargins);
}

//  QMarginsF QPageLayout::minimumMargins() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK11QPageLayout14minimumMarginsEv(
    const QPageLayout *self) {
  return new QMarginsF(self->minimumMargins());
}

//  QMarginsF QPageLayout::maximumMargins() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK11QPageLayout14maximumMarginsEv(
    const QPageLayout *self) {
  return new QMarginsF(self->maximumMargins());
}

//  QRectF QPageLayout::fullRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QPageLayout8fullRectEv(const QPageLayout *self) {
  return new QRectF(self->fullRect());
}

//  QRectF QPageLayout::fullRect(Unit units) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QPageLayout8fullRectENS_4UnitE(
    const QPageLayout *self,
    QPageLayout::Unit units) {
  return new QRectF(self->fullRect(units));
}

//  QRect QPageLayout::fullRectPoints() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QPageLayout14fullRectPointsEv(const QPageLayout *self) {
  return new QRect(self->fullRectPoints());
}

//  QRect QPageLayout::fullRectPixels(int resolution) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QPageLayout14fullRectPixelsEi(
    const QPageLayout *self,
    int resolution) {
  return new QRect(self->fullRectPixels(resolution));
}

//  QRectF QPageLayout::paintRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QPageLayout9paintRectEv(const QPageLayout *self) {
  return new QRectF(self->paintRect());
}

//  QRectF QPageLayout::paintRect(Unit units) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK11QPageLayout9paintRectENS_4UnitE(
    const QPageLayout *self,
    QPageLayout::Unit units) {
  return new QRectF(self->paintRect(units));
}

//  QRect QPageLayout::paintRectPoints() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QPageLayout15paintRectPointsEv(const QPageLayout *self) {
  return new QRect(self->paintRectPoints());
}

//  QRect QPageLayout::paintRectPixels(int resolution) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QPageLayout15paintRectPixelsEi(
    const QPageLayout *self,
    int resolution) {
  return new QRect(self->paintRectPixels(resolution));
}
