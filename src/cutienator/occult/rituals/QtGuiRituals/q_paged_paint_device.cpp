//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpagedpaintdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpagedpaintdevice.h>
#include <QtGui/qpagelayout.h>
#include <QtGui/qpagesize.h>
#include <QtCore/qmargins.h>
#include <QtGui/qpageranges.h>

//  QPagedPaintDevice::~QPagedPaintDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPagedPaintDeviceD1Ev(QPagedPaintDevice *self) {
  delete self;
}

//  bool QPagedPaintDevice::newPage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QPagedPaintDevice7newPageEv(QPagedPaintDevice *self) {
  return self->newPage();
}

//  bool QPagedPaintDevice::setPageLayout(const QPageLayout &pageLayout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QPagedPaintDevice13setPageLayoutERK11QPageLayout(
    QPagedPaintDevice *self,
    const QPageLayout *pageLayout) {
  return self->setPageLayout(*pageLayout);
}

//  bool QPagedPaintDevice::setPageSize(const QPageSize &pageSize)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QPagedPaintDevice11setPageSizeERK9QPageSize(
    QPagedPaintDevice *self,
    const QPageSize *pageSize) {
  return self->setPageSize(*pageSize);
}

//  bool QPagedPaintDevice::setPageOrientation(QPageLayout::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QPagedPaintDevice18setPageOrientationEN11QPageLayout11OrientationE(
    QPagedPaintDevice *self,
    QPageLayout::Orientation orientation) {
  return self->setPageOrientation(orientation);
}

//  bool QPagedPaintDevice::setPageMargins(const QMarginsF &margins,
//      QPageLayout::Unit units)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QPagedPaintDevice14setPageMarginsERK9QMarginsFN11QPageLayout4UnitE(
    QPagedPaintDevice *self,
    const QMarginsF *margins,
    QPageLayout::Unit units) {
  return self->setPageMargins(*margins, units);
}

//  QPageLayout QPagedPaintDevice::pageLayout() const
extern "C" Q_DECL_EXPORT
QPageLayout *ritual_ZNK17QPagedPaintDevice10pageLayoutEv(
    const QPagedPaintDevice *self) {
  return new QPageLayout(self->pageLayout());
}

//  void QPagedPaintDevice::setPageRanges(const QPageRanges &ranges)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPagedPaintDevice13setPageRangesERK11QPageRanges(
    QPagedPaintDevice *self,
    const QPageRanges *ranges) {
  self->setPageRanges(*ranges);
}

//  QPageRanges QPagedPaintDevice::pageRanges() const
extern "C" Q_DECL_EXPORT
QPageRanges *ritual_ZNK17QPagedPaintDevice10pageRangesEv(
    const QPagedPaintDevice *self) {
  return new QPageRanges(self->pageRanges());
}
