//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qprintdevice_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: 'qprintdevice_p.h', 'qprint_p.h' and
//  the rituals stand under '__has_include(<cups/ppd.h>)' where Qt's
//  'qprint_p.h' includes that header of CUPS (macOS, and Unix where Qt
//  has 'cups'), as a Linux without the headers of CUPS refused the
//  file; elsewhere, as on Windows, they stay as they were. The other
//  includes moved above them, unchanged. Kept as it is when the
//  generator runs again.
#include <QtCore/qglobal.h>
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#include <QtCore/qstring.h>
#include <QtGui/qpagelayout.h>
#include <QtGui/qpagesize.h>
#include <QtCore/qsize.h>
#include <QtCore/qmargins.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmimetype.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#if __has_include(<cups/ppd.h>) \
    || !(defined(Q_OS_MACOS) || (defined(Q_OS_UNIX) && QT_CONFIG(cups)))
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprintdevice_p.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPrintDevice::QPrintDevice()
extern "C" Q_DECL_EXPORT
QPrintDevice *ritual_ZN12QPrintDeviceC1Ev() {
  return new QPrintDevice();
}

//  QPrintDevice::QPrintDevice(const QString &id)
extern "C" Q_DECL_EXPORT
QPrintDevice *ritual_ZN12QPrintDeviceC1ERK7QString(const QString *id) {
  return new QPrintDevice(*id);
}

//  QPrintDevice::QPrintDevice(const QPrintDevice &other)
extern "C" Q_DECL_EXPORT
QPrintDevice *ritual_ZN12QPrintDeviceC1ERKS_(const QPrintDevice *other) {
  return new QPrintDevice(*other);
}

//  QPrintDevice::~QPrintDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPrintDeviceD1Ev(QPrintDevice *self) {
  delete self;
}

//  bool QPrintDevice::operator==(const QPrintDevice &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrintDeviceeqERKS_(
    const QPrintDevice *self,
    const QPrintDevice *other) {
  return self->operator==(*other);
}

//  QString QPrintDevice::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QPrintDevice2idEv(const QPrintDevice *self) {
  return new QString(self->id());
}

//  QString QPrintDevice::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QPrintDevice4nameEv(const QPrintDevice *self) {
  return new QString(self->name());
}

//  QString QPrintDevice::location() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QPrintDevice8locationEv(const QPrintDevice *self) {
  return new QString(self->location());
}

//  QString QPrintDevice::makeAndModel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QPrintDevice12makeAndModelEv(const QPrintDevice *self) {
  return new QString(self->makeAndModel());
}

//  bool QPrintDevice::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrintDevice7isValidEv(const QPrintDevice *self) {
  return self->isValid();
}

//  bool QPrintDevice::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrintDevice9isDefaultEv(const QPrintDevice *self) {
  return self->isDefault();
}

//  bool QPrintDevice::isRemote() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrintDevice8isRemoteEv(const QPrintDevice *self) {
  return self->isRemote();
}

//  QPrint::DeviceState QPrintDevice::state() const
extern "C" Q_DECL_EXPORT
QPrint::DeviceState ritual_ZNK12QPrintDevice5stateEv(
    const QPrintDevice *self) {
  return self->state();
}

//  bool QPrintDevice::isValidPageLayout(const QPageLayout &layout, int
//      resolution) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrintDevice17isValidPageLayoutERK11QPageLayouti(
    const QPrintDevice *self,
    const QPageLayout *layout,
    int resolution) {
  return self->isValidPageLayout(*layout, resolution);
}

//  bool QPrintDevice::supportsMultipleCopies() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrintDevice22supportsMultipleCopiesEv(
    const QPrintDevice *self) {
  return self->supportsMultipleCopies();
}

//  bool QPrintDevice::supportsCollateCopies() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrintDevice21supportsCollateCopiesEv(
    const QPrintDevice *self) {
  return self->supportsCollateCopies();
}

//  QPageSize QPrintDevice::defaultPageSize() const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK12QPrintDevice15defaultPageSizeEv(
    const QPrintDevice *self) {
  return new QPageSize(self->defaultPageSize());
}

//  QList<QPageSize> QPrintDevice::supportedPageSizes() const
extern "C" Q_DECL_EXPORT
QList<QPageSize> *ritual_ZNK12QPrintDevice18supportedPageSizesEv(
    const QPrintDevice *self) {
  return new QList<QPageSize>(self->supportedPageSizes());
}

//  QPageSize QPrintDevice::supportedPageSize(const QPageSize &pageSize)
//      const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK12QPrintDevice17supportedPageSizeERK9QPageSize(
    const QPrintDevice *self,
    const QPageSize *pageSize) {
  return new QPageSize(self->supportedPageSize(*pageSize));
}

//  QPageSize QPrintDevice::supportedPageSize(QPageSize::PageSizeId
//      pageSizeId) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK12QPrintDevice17supportedPageSizeEN9QPageSize10PageSizeIdE(
    const QPrintDevice *self,
    QPageSize::PageSizeId pageSizeId) {
  return new QPageSize(self->supportedPageSize(pageSizeId));
}

//  QPageSize QPrintDevice::supportedPageSize(const QString &pageName) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK12QPrintDevice17supportedPageSizeERK7QString(
    const QPrintDevice *self,
    const QString *pageName) {
  return new QPageSize(self->supportedPageSize(*pageName));
}

//  QPageSize QPrintDevice::supportedPageSize(const QSize &pointSize) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK12QPrintDevice17supportedPageSizeERK5QSize(
    const QPrintDevice *self,
    const QSize *pointSize) {
  return new QPageSize(self->supportedPageSize(*pointSize));
}

//  QPageSize QPrintDevice::supportedPageSize(const QSizeF &size,
//      QPageSize::Unit units) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK12QPrintDevice17supportedPageSizeERK6QSizeFN9QPageSize4UnitE(
    const QPrintDevice *self,
    const QSizeF *size,
    QPageSize::Unit units) {
  return new QPageSize(self->supportedPageSize(*size, units));
}

//  bool QPrintDevice::supportsCustomPageSizes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrintDevice23supportsCustomPageSizesEv(
    const QPrintDevice *self) {
  return self->supportsCustomPageSizes();
}

//  QSize QPrintDevice::minimumPhysicalPageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QPrintDevice23minimumPhysicalPageSizeEv(
    const QPrintDevice *self) {
  return new QSize(self->minimumPhysicalPageSize());
}

//  QSize QPrintDevice::maximumPhysicalPageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK12QPrintDevice23maximumPhysicalPageSizeEv(
    const QPrintDevice *self) {
  return new QSize(self->maximumPhysicalPageSize());
}

//  QMarginsF QPrintDevice::printableMargins(const QPageSize &pageSize,
//      QPageLayout::Orientation orientation, int resolution) const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK12QPrintDevice16printableMarginsERK9QPageSizeN11QPageLayout11OrientationEi(
    const QPrintDevice *self,
    const QPageSize *pageSize,
    QPageLayout::Orientation orientation,
    int resolution) {
  return new QMarginsF(
      self->printableMargins(
          *pageSize,
          orientation,
          resolution));
}

//  int QPrintDevice::defaultResolution() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPrintDevice17defaultResolutionEv(const QPrintDevice *self) {
  return self->defaultResolution();
}

//  QPrint::InputSlot QPrintDevice::defaultInputSlot() const
extern "C" Q_DECL_EXPORT
QPrint::InputSlot *ritual_ZNK12QPrintDevice16defaultInputSlotEv(
    const QPrintDevice *self) {
  return new QPrint::InputSlot(self->defaultInputSlot());
}

//  QPrint::OutputBin QPrintDevice::defaultOutputBin() const
extern "C" Q_DECL_EXPORT
QPrint::OutputBin *ritual_ZNK12QPrintDevice16defaultOutputBinEv(
    const QPrintDevice *self) {
  return new QPrint::OutputBin(self->defaultOutputBin());
}

//  QPrint::DuplexMode QPrintDevice::defaultDuplexMode() const
extern "C" Q_DECL_EXPORT
QPrint::DuplexMode ritual_ZNK12QPrintDevice17defaultDuplexModeEv(
    const QPrintDevice *self) {
  return self->defaultDuplexMode();
}

//  QPrint::ColorMode QPrintDevice::defaultColorMode() const
extern "C" Q_DECL_EXPORT
QPrint::ColorMode ritual_ZNK12QPrintDevice16defaultColorModeEv(
    const QPrintDevice *self) {
  return self->defaultColorMode();
}

//  QVariant QPrintDevice::property(PrintDevicePropertyKey key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12QPrintDevice8propertyENS_22PrintDevicePropertyKeyE(
    const QPrintDevice *self,
    QPrintDevice::PrintDevicePropertyKey key) {
  return new QVariant(self->property(key));
}

//  bool QPrintDevice::setProperty(PrintDevicePropertyKey key, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QPrintDevice11setPropertyENS_22PrintDevicePropertyKeyERK8QVariant(
    QPrintDevice *self,
    QPrintDevice::PrintDevicePropertyKey key,
    const QVariant *value) {
  return self->setProperty(key, *value);
}

//  bool QPrintDevice::isFeatureAvailable(PrintDevicePropertyKey key, const
//      QVariant &params) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPrintDevice18isFeatureAvailableENS_22PrintDevicePropertyKeyERK8QVariant(
    const QPrintDevice *self,
    QPrintDevice::PrintDevicePropertyKey key,
    const QVariant *params) {
  return self->isFeatureAvailable(key, *params);
}

#if QT_CONFIG(mimetype)
//  QList<QMimeType> QPrintDevice::supportedMimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QMimeType> *ritual_ZNK12QPrintDevice18supportedMimeTypesEv(
    const QPrintDevice *self) {
  return new QList<QMimeType>(self->supportedMimeTypes());
}
#endif  // QT_CONFIG(mimetype)

#if !defined(QT_NO_DEBUG_STREAM)
//  void QPrintDevice::format(QDebug debug) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QPrintDevice6formatE6QDebug(
    const QPrintDevice *self,
    const QDebug *debug) {
  self->format(*debug);
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QPrintDevice::QPrintDevice(QPlatformPrintDevice *dd)
extern "C" Q_DECL_EXPORT
QPrintDevice *ritual_ZN12QPrintDeviceC1EP20QPlatformPrintDevice(
    QPlatformPrintDevice *dd) {
  return new QPrintDevice(dd);
}

#endif  // __has_include(<cups/ppd.h>) || !(defined(Q_OS_MACOS)
        //     || (defined(Q_OS_UNIX) && QT_CONFIG(cups)))
#endif  // !defined(QT_NO_PRINTER)
