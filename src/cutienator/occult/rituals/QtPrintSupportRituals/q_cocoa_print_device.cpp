//  Written by hand on 2026-11-25 from
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qcocoaprintdevice_p.h, Qt
//  6.12.0, as the Qt of macOS installs it. Kept as it is when the
//  generator runs again.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out.
//  Not written: the constructors, 'macPrinter' and 'macPaper', which
//  Qt's library offers not.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if defined(Q_OS_MACOS) && !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qcocoaprintdevice_p.h>
#include <QtCore/qmargins.h>
#include <QtGui/qpagelayout.h>
#include <QtGui/qpagesize.h>

//  QCocoaPrintDevice::~QCocoaPrintDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCocoaPrintDeviceD1Ev(QCocoaPrintDevice *self) {
  delete self;
}

//  bool QCocoaPrintDevice::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCocoaPrintDevice7isValidEv(const QCocoaPrintDevice *self) {
  return self->isValid();
}

//  bool QCocoaPrintDevice::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCocoaPrintDevice9isDefaultEv(
    const QCocoaPrintDevice *self) {
  return self->isDefault();
}

//  QPrint::DeviceState QCocoaPrintDevice::state() const
extern "C" Q_DECL_EXPORT
QPrint::DeviceState ritual_ZNK17QCocoaPrintDevice5stateEv(
    const QCocoaPrintDevice *self) {
  return self->state();
}

//  QPageSize QCocoaPrintDevice::defaultPageSize() const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK17QCocoaPrintDevice15defaultPageSizeEv(
    const QCocoaPrintDevice *self) {
  return new QPageSize(self->defaultPageSize());
}

//  QMarginsF QCocoaPrintDevice::printableMargins(const QPageSize &pageSize,
//      QPageLayout::Orientation orientation, int resolution) const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK17QCocoaPrintDevice16printableMarginsERK9QPageSizeN11QPageLayout11OrientationEi(
    const QCocoaPrintDevice *self,
    const QPageSize *pageSize,
    QPageLayout::Orientation orientation,
    int resolution) {
  return new QMarginsF(
      self->printableMargins(*pageSize, orientation, resolution));
}

//  int QCocoaPrintDevice::defaultResolution() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QCocoaPrintDevice17defaultResolutionEv(
    const QCocoaPrintDevice *self) {
  return self->defaultResolution();
}

//  QPrint::InputSlot QCocoaPrintDevice::defaultInputSlot() const
extern "C" Q_DECL_EXPORT
QPrint::InputSlot *ritual_ZNK17QCocoaPrintDevice16defaultInputSlotEv(
    const QCocoaPrintDevice *self) {
  return new QPrint::InputSlot(self->defaultInputSlot());
}

//  QPrint::OutputBin QCocoaPrintDevice::defaultOutputBin() const
extern "C" Q_DECL_EXPORT
QPrint::OutputBin *ritual_ZNK17QCocoaPrintDevice16defaultOutputBinEv(
    const QCocoaPrintDevice *self) {
  return new QPrint::OutputBin(self->defaultOutputBin());
}

//  QPrint::DuplexMode QCocoaPrintDevice::defaultDuplexMode() const
extern "C" Q_DECL_EXPORT
QPrint::DuplexMode ritual_ZNK17QCocoaPrintDevice17defaultDuplexModeEv(
    const QCocoaPrintDevice *self) {
  return self->defaultDuplexMode();
}

//  QPrint::ColorMode QCocoaPrintDevice::defaultColorMode() const
extern "C" Q_DECL_EXPORT
QPrint::ColorMode ritual_ZNK17QCocoaPrintDevice16defaultColorModeEv(
    const QCocoaPrintDevice *self) {
  return self->defaultColorMode();
}

//  void QCocoaPrintDevice::loadPageSizes() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QCocoaPrintDevice13loadPageSizesEv(
    const QCocoaPrintDevice *self) {
  self->loadPageSizes();
}

//  void QCocoaPrintDevice::loadResolutions() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QCocoaPrintDevice15loadResolutionsEv(
    const QCocoaPrintDevice *self) {
  self->loadResolutions();
}

//  void QCocoaPrintDevice::loadInputSlots() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QCocoaPrintDevice14loadInputSlotsEv(
    const QCocoaPrintDevice *self) {
  self->loadInputSlots();
}

//  void QCocoaPrintDevice::loadOutputBins() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QCocoaPrintDevice14loadOutputBinsEv(
    const QCocoaPrintDevice *self) {
  self->loadOutputBins();
}

//  void QCocoaPrintDevice::loadDuplexModes() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QCocoaPrintDevice15loadDuplexModesEv(
    const QCocoaPrintDevice *self) {
  self->loadDuplexModes();
}

//  void QCocoaPrintDevice::loadColorModes() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QCocoaPrintDevice14loadColorModesEv(
    const QCocoaPrintDevice *self) {
  self->loadColorModes();
}

#if QT_CONFIG(mimetype)
//  void QCocoaPrintDevice::loadMimeTypes() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QCocoaPrintDevice13loadMimeTypesEv(
    const QCocoaPrintDevice *self) {
  self->loadMimeTypes();
}
#endif  // QT_CONFIG(mimetype)

#endif  // defined(Q_OS_MACOS) && !defined(QT_NO_PRINTER)
