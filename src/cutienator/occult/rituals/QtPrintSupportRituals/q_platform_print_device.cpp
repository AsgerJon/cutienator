//  Written by dev_tooling.RitualGenerator from the records of
//  QtPrintSupport/6.12.0/QtPrintSupport/qpa/qplatformprintdevice.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#include <QtPrintSupport/QtPrintSupport>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/qpa/qplatformprintdevice.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qpagelayout.h>
#include <QtGui/qpagesize.h>
#include <QtCore/qsize.h>
#include <QtCore/qmargins.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qmimetype.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QPlatformPrintDevice may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPlatformPrintDevice : QPlatformPrintDevice {
  using QPlatformPrintDevice::loadPageSizes;
  using QPlatformPrintDevice::loadResolutions;
  using QPlatformPrintDevice::loadInputSlots;
  using QPlatformPrintDevice::loadOutputBins;
  using QPlatformPrintDevice::loadDuplexModes;
  using QPlatformPrintDevice::loadColorModes;
  using QPlatformPrintDevice::loadMimeTypes;
};

//  A QPlatformPrintDevice that Python can take functions over in. Every QPlatformPrintDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PRINTER)
typedef QString * (*CuteQPlatformPrintDeviceCall0)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef QString * (*CuteQPlatformPrintDeviceCall1)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef QString * (*CuteQPlatformPrintDeviceCall2)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef QString * (*CuteQPlatformPrintDeviceCall3)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPlatformPrintDeviceCall4)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPlatformPrintDeviceCall5)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPlatformPrintDeviceCall6)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQPlatformPrintDeviceCall7)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPlatformPrintDeviceCall8)(const void *, const QPageLayout *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPlatformPrintDeviceCall9)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPlatformPrintDeviceCall10)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPageSize * (*CuteQPlatformPrintDeviceCall11)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPageSize * (*CuteQPlatformPrintDeviceCall12)(const void *, const QPageSize *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPageSize * (*CuteQPlatformPrintDeviceCall13)(const void *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPageSize * (*CuteQPlatformPrintDeviceCall14)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPageSize * (*CuteQPlatformPrintDeviceCall15)(const void *, const QSize *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPageSize * (*CuteQPlatformPrintDeviceCall16)(const void *, const QSizeF *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPlatformPrintDeviceCall17)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QSize * (*CuteQPlatformPrintDeviceCall18)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QSize * (*CuteQPlatformPrintDeviceCall19)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QMarginsF * (*CuteQPlatformPrintDeviceCall20)(const void *, const QPageSize *, int, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQPlatformPrintDeviceCall21)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPrint::InputSlot * (*CuteQPlatformPrintDeviceCall22)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPrint::OutputBin * (*CuteQPlatformPrintDeviceCall23)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQPlatformPrintDeviceCall24)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQPlatformPrintDeviceCall25)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QVariant * (*CuteQPlatformPrintDeviceCall26)(const void *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPlatformPrintDeviceCall27)(const void *, int, const QVariant *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQPlatformPrintDeviceCall28)(const void *, int, const QVariant *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQPlatformPrintDeviceCall29)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQPlatformPrintDeviceCall30)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQPlatformPrintDeviceCall31)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQPlatformPrintDeviceCall32)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQPlatformPrintDeviceCall33)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQPlatformPrintDeviceCall34)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(mimetype)
typedef void (*CuteQPlatformPrintDeviceCall35)(const void *, int *);
#endif  // QT_CONFIG(mimetype)
#endif  // !defined(QT_NO_PRINTER)
class CuteQPlatformPrintDevice : public QPlatformPrintDevice {
public:
  using QPlatformPrintDevice::QPlatformPrintDevice;
  void *taken[36] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice2idEv")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice4nameEv")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice8locationEv")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice12makeAndModelEv")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice7isValidEv")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice9isDefaultEv")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice8isRemoteEv")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice5stateEv")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice17isValidPageLayoutERK11QPageLayouti")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice22supportsMultipleCopiesEv")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice21supportsCollateCopiesEv")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice15defaultPageSizeEv")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice17supportedPageSizeERK9QPageSize")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice17supportedPageSizeEN9QPageSize10PageSizeIdE")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice17supportedPageSizeERK7QString")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice17supportedPageSizeERK5QSize")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice17supportedPageSizeERK6QSizeFN9QPageSize4UnitE")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice23supportsCustomPageSizesEv")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice23minimumPhysicalPageSizeEv")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice23maximumPhysicalPageSizeEv")) {
      taken[19] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice16printableMarginsERK9QPageSizeN11QPageLayout11OrientationEi")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice17defaultResolutionEv")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice16defaultInputSlotEv")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice16defaultOutputBinEv")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice17defaultDuplexModeEv")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice16defaultColorModeEv")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice8propertyEN12QPrintDevice22PrintDevicePropertyKeyE")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZN20QPlatformPrintDevice11setPropertyEN12QPrintDevice22PrintDevicePropertyKeyERK8QVariant")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice18isFeatureAvailableEN12QPrintDevice22PrintDevicePropertyKeyERK8QVariant")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice13loadPageSizesEv")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice15loadResolutionsEv")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice14loadInputSlotsEv")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice14loadOutputBinsEv")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice15loadDuplexModesEv")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice14loadColorModesEv")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZNK20QPlatformPrintDevice13loadMimeTypesEv")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
#endif  // !defined(QT_NO_PRINTER)
    return false;
  }

#if !defined(QT_NO_PRINTER)
  //  QString QPlatformPrintDevice::id() const
  QString id() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall0 call = reinterpret_cast<CuteQPlatformPrintDeviceCall0>(taken[0]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformPrintDevice::id();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QString QPlatformPrintDevice::name() const
  QString name() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall1 call = reinterpret_cast<CuteQPlatformPrintDeviceCall1>(taken[1]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformPrintDevice::name();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QString QPlatformPrintDevice::location() const
  QString location() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall2 call = reinterpret_cast<CuteQPlatformPrintDeviceCall2>(taken[2]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformPrintDevice::location();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QString QPlatformPrintDevice::makeAndModel() const
  QString makeAndModel() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall3 call = reinterpret_cast<CuteQPlatformPrintDeviceCall3>(taken[3]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QPlatformPrintDevice::makeAndModel();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPlatformPrintDevice::isValid() const
  bool isValid() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall4 call = reinterpret_cast<CuteQPlatformPrintDeviceCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::isValid();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPlatformPrintDevice::isDefault() const
  bool isDefault() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall5 call = reinterpret_cast<CuteQPlatformPrintDeviceCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::isDefault();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPlatformPrintDevice::isRemote() const
  bool isRemote() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall6 call = reinterpret_cast<CuteQPlatformPrintDeviceCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::isRemote();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPrint::DeviceState QPlatformPrintDevice::state() const
  QPrint::DeviceState state() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall7 call = reinterpret_cast<CuteQPlatformPrintDeviceCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPrint::DeviceState>(given);
    }
    return QPlatformPrintDevice::state();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPlatformPrintDevice::isValidPageLayout(const QPageLayout
  //      &layout, int resolution) const
  bool isValidPageLayout(
      const QPageLayout &layout,
      int resolution) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall8 call = reinterpret_cast<CuteQPlatformPrintDeviceCall8>(taken[8]);
      bool given = call(this, &layout, resolution, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::isValidPageLayout(layout, resolution);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPlatformPrintDevice::supportsMultipleCopies() const
  bool supportsMultipleCopies() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall9 call = reinterpret_cast<CuteQPlatformPrintDeviceCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::supportsMultipleCopies();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPlatformPrintDevice::supportsCollateCopies() const
  bool supportsCollateCopies() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall10 call = reinterpret_cast<CuteQPlatformPrintDeviceCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::supportsCollateCopies();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPageSize QPlatformPrintDevice::defaultPageSize() const
  QPageSize defaultPageSize() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall11 call = reinterpret_cast<CuteQPlatformPrintDeviceCall11>(taken[11]);
      const QPageSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::defaultPageSize();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPageSize QPlatformPrintDevice::supportedPageSize(const QPageSize
  //      &pageSize) const
  QPageSize supportedPageSize(const QPageSize &pageSize) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall12 call = reinterpret_cast<CuteQPlatformPrintDeviceCall12>(taken[12]);
      const QPageSize * given = call(this, &pageSize, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::supportedPageSize(pageSize);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPageSize
  //      QPlatformPrintDevice::supportedPageSize(QPageSize::PageSizeId
  //      pageSizeId) const
  QPageSize supportedPageSize(
      QPageSize::PageSizeId pageSizeId) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall13 call = reinterpret_cast<CuteQPlatformPrintDeviceCall13>(taken[13]);
      const QPageSize * given = call(this, static_cast<int>(pageSizeId), &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::supportedPageSize(pageSizeId);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPageSize QPlatformPrintDevice::supportedPageSize(const QString
  //      &pageName) const
  QPageSize supportedPageSize(const QString &pageName) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall14 call = reinterpret_cast<CuteQPlatformPrintDeviceCall14>(taken[14]);
      const QPageSize * given = call(this, &pageName, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::supportedPageSize(pageName);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPageSize QPlatformPrintDevice::supportedPageSize(const QSize
  //      &pointSize) const
  QPageSize supportedPageSize(const QSize &pointSize) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall15 call = reinterpret_cast<CuteQPlatformPrintDeviceCall15>(taken[15]);
      const QPageSize * given = call(this, &pointSize, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::supportedPageSize(pointSize);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPageSize QPlatformPrintDevice::supportedPageSize(const QSizeF &size,
  //      QPageSize::Unit units) const
  QPageSize supportedPageSize(
      const QSizeF &size,
      QPageSize::Unit units) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall16 call = reinterpret_cast<CuteQPlatformPrintDeviceCall16>(taken[16]);
      const QPageSize * given = call(this, &size, static_cast<int>(units), &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::supportedPageSize(size, units);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPlatformPrintDevice::supportsCustomPageSizes() const
  bool supportsCustomPageSizes() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall17 call = reinterpret_cast<CuteQPlatformPrintDeviceCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::supportsCustomPageSizes();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QSize QPlatformPrintDevice::minimumPhysicalPageSize() const
  QSize minimumPhysicalPageSize() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall18 call = reinterpret_cast<CuteQPlatformPrintDeviceCall18>(taken[18]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::minimumPhysicalPageSize();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QSize QPlatformPrintDevice::maximumPhysicalPageSize() const
  QSize maximumPhysicalPageSize() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall19 call = reinterpret_cast<CuteQPlatformPrintDeviceCall19>(taken[19]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::maximumPhysicalPageSize();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QMarginsF QPlatformPrintDevice::printableMargins(const QPageSize
  //      &pageSize, QPageLayout::Orientation orientation, int resolution)
  //      const
  QMarginsF printableMargins(
      const QPageSize &pageSize,
      QPageLayout::Orientation orientation,
      int resolution) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall20 call = reinterpret_cast<CuteQPlatformPrintDeviceCall20>(taken[20]);
      const QMarginsF * given = call(this, &pageSize, static_cast<int>(orientation), resolution, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::printableMargins(pageSize, orientation, resolution);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  int QPlatformPrintDevice::defaultResolution() const
  int defaultResolution() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall21 call = reinterpret_cast<CuteQPlatformPrintDeviceCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::defaultResolution();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPrint::InputSlot QPlatformPrintDevice::defaultInputSlot() const
  QPrint::InputSlot defaultInputSlot() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall22 call = reinterpret_cast<CuteQPlatformPrintDeviceCall22>(taken[22]);
      const QPrint::InputSlot * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::defaultInputSlot();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPrint::OutputBin QPlatformPrintDevice::defaultOutputBin() const
  QPrint::OutputBin defaultOutputBin() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall23 call = reinterpret_cast<CuteQPlatformPrintDeviceCall23>(taken[23]);
      const QPrint::OutputBin * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::defaultOutputBin();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPrint::DuplexMode QPlatformPrintDevice::defaultDuplexMode() const
  QPrint::DuplexMode defaultDuplexMode() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall24 call = reinterpret_cast<CuteQPlatformPrintDeviceCall24>(taken[24]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPrint::DuplexMode>(given);
    }
    return QPlatformPrintDevice::defaultDuplexMode();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPrint::ColorMode QPlatformPrintDevice::defaultColorMode() const
  QPrint::ColorMode defaultColorMode() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall25 call = reinterpret_cast<CuteQPlatformPrintDeviceCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPrint::ColorMode>(given);
    }
    return QPlatformPrintDevice::defaultColorMode();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QVariant
  //      QPlatformPrintDevice::property(QPrintDevice::PrintDevicePropertyK
  //      ey key) const
  QVariant property(
      QPrintDevice::PrintDevicePropertyKey key) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall26 call = reinterpret_cast<CuteQPlatformPrintDeviceCall26>(taken[26]);
      const QVariant * given = call(this, static_cast<int>(key), &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::property(key);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPlatformPrintDevice::setProperty(QPrintDevice::PrintDevicePrope
  //      rtyKey key, const QVariant &value)
  bool setProperty(
      QPrintDevice::PrintDevicePropertyKey key,
      const QVariant &value) override {
    if (taken[27]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall27 call = reinterpret_cast<CuteQPlatformPrintDeviceCall27>(taken[27]);
      bool given = call(this, static_cast<int>(key), &value, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::setProperty(key, value);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPlatformPrintDevice::isFeatureAvailable(QPrintDevice::PrintDevi
  //      cePropertyKey key, const QVariant &params) const
  bool isFeatureAvailable(
      QPrintDevice::PrintDevicePropertyKey key,
      const QVariant &params) const override {
    if (taken[28]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall28 call = reinterpret_cast<CuteQPlatformPrintDeviceCall28>(taken[28]);
      bool given = call(this, static_cast<int>(key), &params, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::isFeatureAvailable(key, params);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QPlatformPrintDevice::loadPageSizes() const
  void loadPageSizes() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall29 call = reinterpret_cast<CuteQPlatformPrintDeviceCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformPrintDevice::loadPageSizes();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QPlatformPrintDevice::loadResolutions() const
  void loadResolutions() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall30 call = reinterpret_cast<CuteQPlatformPrintDeviceCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformPrintDevice::loadResolutions();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QPlatformPrintDevice::loadInputSlots() const
  void loadInputSlots() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall31 call = reinterpret_cast<CuteQPlatformPrintDeviceCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformPrintDevice::loadInputSlots();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QPlatformPrintDevice::loadOutputBins() const
  void loadOutputBins() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall32 call = reinterpret_cast<CuteQPlatformPrintDeviceCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformPrintDevice::loadOutputBins();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QPlatformPrintDevice::loadDuplexModes() const
  void loadDuplexModes() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall33 call = reinterpret_cast<CuteQPlatformPrintDeviceCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformPrintDevice::loadDuplexModes();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QPlatformPrintDevice::loadColorModes() const
  void loadColorModes() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall34 call = reinterpret_cast<CuteQPlatformPrintDeviceCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformPrintDevice::loadColorModes();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(mimetype)
  //  void QPlatformPrintDevice::loadMimeTypes() const
  void loadMimeTypes() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQPlatformPrintDeviceCall35 call = reinterpret_cast<CuteQPlatformPrintDeviceCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformPrintDevice::loadMimeTypes();
  }
#endif  // QT_CONFIG(mimetype)
#endif  // !defined(QT_NO_PRINTER)
};

//  QPlatformPrintDevice::QPlatformPrintDevice(const QString &id)
extern "C" Q_DECL_EXPORT
QPlatformPrintDevice *ritual_ZN20QPlatformPrintDeviceC1ERK7QString(
    const QString *id) {
  return new CuteQPlatformPrintDevice(*id);
}

//  QPlatformPrintDevice::~QPlatformPrintDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformPrintDeviceD1Ev(QPlatformPrintDevice *self) {
  delete self;
}

//  QString QPlatformPrintDevice::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QPlatformPrintDevice2idEv(
    const QPlatformPrintDevice *self) {
  return new QString(self->id());
}

//  QString QPlatformPrintDevice::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QPlatformPrintDevice4nameEv(
    const QPlatformPrintDevice *self) {
  return new QString(self->name());
}

//  QString QPlatformPrintDevice::location() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QPlatformPrintDevice8locationEv(
    const QPlatformPrintDevice *self) {
  return new QString(self->location());
}

//  QString QPlatformPrintDevice::makeAndModel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QPlatformPrintDevice12makeAndModelEv(
    const QPlatformPrintDevice *self) {
  return new QString(self->makeAndModel());
}

//  bool QPlatformPrintDevice::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformPrintDevice7isValidEv(
    const QPlatformPrintDevice *self) {
  return self->isValid();
}

//  bool QPlatformPrintDevice::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformPrintDevice9isDefaultEv(
    const QPlatformPrintDevice *self) {
  return self->isDefault();
}

//  bool QPlatformPrintDevice::isRemote() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformPrintDevice8isRemoteEv(
    const QPlatformPrintDevice *self) {
  return self->isRemote();
}

//  QPrint::DeviceState QPlatformPrintDevice::state() const
extern "C" Q_DECL_EXPORT
QPrint::DeviceState ritual_ZNK20QPlatformPrintDevice5stateEv(
    const QPlatformPrintDevice *self) {
  return self->state();
}

//  bool QPlatformPrintDevice::isValidPageLayout(const QPageLayout &layout,
//      int resolution) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformPrintDevice17isValidPageLayoutERK11QPageLayouti(
    const QPlatformPrintDevice *self,
    const QPageLayout *layout,
    int resolution) {
  return self->isValidPageLayout(*layout, resolution);
}

//  bool QPlatformPrintDevice::supportsMultipleCopies() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformPrintDevice22supportsMultipleCopiesEv(
    const QPlatformPrintDevice *self) {
  return self->supportsMultipleCopies();
}

//  bool QPlatformPrintDevice::supportsCollateCopies() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformPrintDevice21supportsCollateCopiesEv(
    const QPlatformPrintDevice *self) {
  return self->supportsCollateCopies();
}

//  QPageSize QPlatformPrintDevice::defaultPageSize() const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK20QPlatformPrintDevice15defaultPageSizeEv(
    const QPlatformPrintDevice *self) {
  return new QPageSize(self->defaultPageSize());
}

//  QList<QPageSize> QPlatformPrintDevice::supportedPageSizes() const
extern "C" Q_DECL_EXPORT
QList<QPageSize> *ritual_ZNK20QPlatformPrintDevice18supportedPageSizesEv(
    const QPlatformPrintDevice *self) {
  return new QList<QPageSize>(self->supportedPageSizes());
}

//  QPageSize QPlatformPrintDevice::supportedPageSize(const QPageSize
//      &pageSize) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK20QPlatformPrintDevice17supportedPageSizeERK9QPageSize(
    const QPlatformPrintDevice *self,
    const QPageSize *pageSize) {
  return new QPageSize(self->supportedPageSize(*pageSize));
}

//  QPageSize QPlatformPrintDevice::supportedPageSize(QPageSize::PageSizeId
//      pageSizeId) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK20QPlatformPrintDevice17supportedPageSizeEN9QPageSize10PageSizeIdE(
    const QPlatformPrintDevice *self,
    QPageSize::PageSizeId pageSizeId) {
  return new QPageSize(self->supportedPageSize(pageSizeId));
}

//  QPageSize QPlatformPrintDevice::supportedPageSize(const QString
//      &pageName) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK20QPlatformPrintDevice17supportedPageSizeERK7QString(
    const QPlatformPrintDevice *self,
    const QString *pageName) {
  return new QPageSize(self->supportedPageSize(*pageName));
}

//  QPageSize QPlatformPrintDevice::supportedPageSize(const QSize &pointSize)
//      const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK20QPlatformPrintDevice17supportedPageSizeERK5QSize(
    const QPlatformPrintDevice *self,
    const QSize *pointSize) {
  return new QPageSize(self->supportedPageSize(*pointSize));
}

//  QPageSize QPlatformPrintDevice::supportedPageSize(const QSizeF &size,
//      QPageSize::Unit units) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK20QPlatformPrintDevice17supportedPageSizeERK6QSizeFN9QPageSize4UnitE(
    const QPlatformPrintDevice *self,
    const QSizeF *size,
    QPageSize::Unit units) {
  return new QPageSize(self->supportedPageSize(*size, units));
}

//  bool QPlatformPrintDevice::supportsCustomPageSizes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformPrintDevice23supportsCustomPageSizesEv(
    const QPlatformPrintDevice *self) {
  return self->supportsCustomPageSizes();
}

//  QSize QPlatformPrintDevice::minimumPhysicalPageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK20QPlatformPrintDevice23minimumPhysicalPageSizeEv(
    const QPlatformPrintDevice *self) {
  return new QSize(self->minimumPhysicalPageSize());
}

//  QSize QPlatformPrintDevice::maximumPhysicalPageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK20QPlatformPrintDevice23maximumPhysicalPageSizeEv(
    const QPlatformPrintDevice *self) {
  return new QSize(self->maximumPhysicalPageSize());
}

//  QMarginsF QPlatformPrintDevice::printableMargins(const QPageSize
//      &pageSize, QPageLayout::Orientation orientation, int resolution)
//      const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK20QPlatformPrintDevice16printableMarginsERK9QPageSizeN11QPageLayout11OrientationEi(
    const QPlatformPrintDevice *self,
    const QPageSize *pageSize,
    QPageLayout::Orientation orientation,
    int resolution) {
  return new QMarginsF(
      self->printableMargins(
          *pageSize,
          orientation,
          resolution));
}

//  int QPlatformPrintDevice::defaultResolution() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QPlatformPrintDevice17defaultResolutionEv(
    const QPlatformPrintDevice *self) {
  return self->defaultResolution();
}

//  QPrint::InputSlot QPlatformPrintDevice::defaultInputSlot() const
extern "C" Q_DECL_EXPORT
QPrint::InputSlot *ritual_ZNK20QPlatformPrintDevice16defaultInputSlotEv(
    const QPlatformPrintDevice *self) {
  return new QPrint::InputSlot(self->defaultInputSlot());
}

//  QPrint::OutputBin QPlatformPrintDevice::defaultOutputBin() const
extern "C" Q_DECL_EXPORT
QPrint::OutputBin *ritual_ZNK20QPlatformPrintDevice16defaultOutputBinEv(
    const QPlatformPrintDevice *self) {
  return new QPrint::OutputBin(self->defaultOutputBin());
}

//  QPrint::DuplexMode QPlatformPrintDevice::defaultDuplexMode() const
extern "C" Q_DECL_EXPORT
QPrint::DuplexMode ritual_ZNK20QPlatformPrintDevice17defaultDuplexModeEv(
    const QPlatformPrintDevice *self) {
  return self->defaultDuplexMode();
}

//  QPrint::ColorMode QPlatformPrintDevice::defaultColorMode() const
extern "C" Q_DECL_EXPORT
QPrint::ColorMode ritual_ZNK20QPlatformPrintDevice16defaultColorModeEv(
    const QPlatformPrintDevice *self) {
  return self->defaultColorMode();
}

//  QVariant
//      QPlatformPrintDevice::property(QPrintDevice::PrintDevicePropertyKey
//      key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QPlatformPrintDevice8propertyEN12QPrintDevice22PrintDevicePropertyKeyE(
    const QPlatformPrintDevice *self,
    QPrintDevice::PrintDevicePropertyKey key) {
  return new QVariant(self->property(key));
}

//  bool
//      QPlatformPrintDevice::setProperty(QPrintDevice::PrintDevicePropertyKe
//      y key, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QPlatformPrintDevice11setPropertyEN12QPrintDevice22PrintDevicePropertyKeyERK8QVariant(
    QPlatformPrintDevice *self,
    QPrintDevice::PrintDevicePropertyKey key,
    const QVariant *value) {
  return self->setProperty(key, *value);
}

//  bool QPlatformPrintDevice::isFeatureAvailable(QPrintDevice::PrintDevicePr
//      opertyKey key, const QVariant &params) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformPrintDevice18isFeatureAvailableEN12QPrintDevice22PrintDevicePropertyKeyERK8QVariant(
    const QPlatformPrintDevice *self,
    QPrintDevice::PrintDevicePropertyKey key,
    const QVariant *params) {
  return self->isFeatureAvailable(key, *params);
}

#if QT_CONFIG(mimetype)
//  QList<QMimeType> QPlatformPrintDevice::supportedMimeTypes() const
extern "C" Q_DECL_EXPORT
QList<QMimeType> *ritual_ZNK20QPlatformPrintDevice18supportedMimeTypesEv(
    const QPlatformPrintDevice *self) {
  return new QList<QMimeType>(self->supportedMimeTypes());
}
#endif  // QT_CONFIG(mimetype)

//  QPageSize QPlatformPrintDevice::createPageSize(const QString &key, const
//      QSize &size, const QString &localizedName)
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZN20QPlatformPrintDevice14createPageSizeERK7QStringRK5QSizeS2_(
    const QString *key,
    const QSize *size,
    const QString *localizedName) {
  return new QPageSize(
      QPlatformPrintDevice::createPageSize(
          *key,
          *size,
          *localizedName));
}

//  QPageSize QPlatformPrintDevice::createPageSize(int windowsId, const QSize
//      &size, const QString &localizedName)
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZN20QPlatformPrintDevice14createPageSizeEiRK5QSizeRK7QString(
    int windowsId,
    const QSize *size,
    const QString *localizedName) {
  return new QPageSize(
      QPlatformPrintDevice::createPageSize(
          windowsId,
          *size,
          *localizedName));
}

//  void QPlatformPrintDevice::loadPageSizes() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QPlatformPrintDevice13loadPageSizesEv(
    const QPlatformPrintDevice *self) {
  self->loadPageSizes();
}

//  void QPlatformPrintDevice::loadResolutions() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QPlatformPrintDevice15loadResolutionsEv(
    const QPlatformPrintDevice *self) {
  self->loadResolutions();
}

//  void QPlatformPrintDevice::loadInputSlots() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QPlatformPrintDevice14loadInputSlotsEv(
    const QPlatformPrintDevice *self) {
  self->loadInputSlots();
}

//  void QPlatformPrintDevice::loadOutputBins() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QPlatformPrintDevice14loadOutputBinsEv(
    const QPlatformPrintDevice *self) {
  self->loadOutputBins();
}

//  void QPlatformPrintDevice::loadDuplexModes() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QPlatformPrintDevice15loadDuplexModesEv(
    const QPlatformPrintDevice *self) {
  self->loadDuplexModes();
}

//  void QPlatformPrintDevice::loadColorModes() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QPlatformPrintDevice14loadColorModesEv(
    const QPlatformPrintDevice *self) {
  self->loadColorModes();
}

#if QT_CONFIG(mimetype)
//  void QPlatformPrintDevice::loadMimeTypes() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QPlatformPrintDevice13loadMimeTypesEv(
    const QPlatformPrintDevice *self) {
  self->loadMimeTypes();
}
#endif  // QT_CONFIG(mimetype)

//  QPageSize QPlatformPrintDevice::supportedPageSizeMatch(const QPageSize
//      &pageSize) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK20QPlatformPrintDevice22supportedPageSizeMatchERK9QPageSize(
    const QPlatformPrintDevice *self,
    const QPageSize *pageSize) {
  return new QPageSize(self->supportedPageSizeMatch(*pageSize));
}

//  a Python function taken by a CuteQPlatformPrintDevice, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformPrintDevice(
    QPlatformPrintDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformPrintDevice *>(self)->take(key, call);
}

//  QString QPlatformPrintDevice::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QPlatformPrintDevice2idEv(
    const QPlatformPrintDevice *self) {
  return new QString(self->QPlatformPrintDevice::id());
}

//  QString QPlatformPrintDevice::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QPlatformPrintDevice4nameEv(
    const QPlatformPrintDevice *self) {
  return new QString(self->QPlatformPrintDevice::name());
}

//  QString QPlatformPrintDevice::location() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QPlatformPrintDevice8locationEv(
    const QPlatformPrintDevice *self) {
  return new QString(self->QPlatformPrintDevice::location());
}

//  QString QPlatformPrintDevice::makeAndModel() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK20QPlatformPrintDevice12makeAndModelEv(
    const QPlatformPrintDevice *self) {
  return new QString(self->QPlatformPrintDevice::makeAndModel());
}

//  bool QPlatformPrintDevice::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformPrintDevice7isValidEv(
    const QPlatformPrintDevice *self) {
  return self->QPlatformPrintDevice::isValid();
}

//  bool QPlatformPrintDevice::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformPrintDevice9isDefaultEv(
    const QPlatformPrintDevice *self) {
  return self->QPlatformPrintDevice::isDefault();
}

//  bool QPlatformPrintDevice::isRemote() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformPrintDevice8isRemoteEv(
    const QPlatformPrintDevice *self) {
  return self->QPlatformPrintDevice::isRemote();
}

//  QPrint::DeviceState QPlatformPrintDevice::state() const
extern "C" Q_DECL_EXPORT
QPrint::DeviceState ritual_own_ZNK20QPlatformPrintDevice5stateEv(
    const QPlatformPrintDevice *self) {
  return self->QPlatformPrintDevice::state();
}

//  bool QPlatformPrintDevice::isValidPageLayout(const QPageLayout &layout,
//      int resolution) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformPrintDevice17isValidPageLayoutERK11QPageLayouti(
    const QPlatformPrintDevice *self,
    const QPageLayout *layout,
    int resolution) {
  return self->QPlatformPrintDevice::isValidPageLayout(*layout, resolution);
}

//  bool QPlatformPrintDevice::supportsMultipleCopies() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformPrintDevice22supportsMultipleCopiesEv(
    const QPlatformPrintDevice *self) {
  return self->QPlatformPrintDevice::supportsMultipleCopies();
}

//  bool QPlatformPrintDevice::supportsCollateCopies() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformPrintDevice21supportsCollateCopiesEv(
    const QPlatformPrintDevice *self) {
  return self->QPlatformPrintDevice::supportsCollateCopies();
}

//  QPageSize QPlatformPrintDevice::defaultPageSize() const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_own_ZNK20QPlatformPrintDevice15defaultPageSizeEv(
    const QPlatformPrintDevice *self) {
  return new QPageSize(self->QPlatformPrintDevice::defaultPageSize());
}

//  QPageSize QPlatformPrintDevice::supportedPageSize(const QPageSize
//      &pageSize) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_own_ZNK20QPlatformPrintDevice17supportedPageSizeERK9QPageSize(
    const QPlatformPrintDevice *self,
    const QPageSize *pageSize) {
  return new QPageSize(
      self->QPlatformPrintDevice::supportedPageSize(
          *pageSize));
}

//  QPageSize QPlatformPrintDevice::supportedPageSize(QPageSize::PageSizeId
//      pageSizeId) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_own_ZNK20QPlatformPrintDevice17supportedPageSizeEN9QPageSize10PageSizeIdE(
    const QPlatformPrintDevice *self,
    QPageSize::PageSizeId pageSizeId) {
  return new QPageSize(
      self->QPlatformPrintDevice::supportedPageSize(
          pageSizeId));
}

//  QPageSize QPlatformPrintDevice::supportedPageSize(const QString
//      &pageName) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_own_ZNK20QPlatformPrintDevice17supportedPageSizeERK7QString(
    const QPlatformPrintDevice *self,
    const QString *pageName) {
  return new QPageSize(
      self->QPlatformPrintDevice::supportedPageSize(
          *pageName));
}

//  QPageSize QPlatformPrintDevice::supportedPageSize(const QSize &pointSize)
//      const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_own_ZNK20QPlatformPrintDevice17supportedPageSizeERK5QSize(
    const QPlatformPrintDevice *self,
    const QSize *pointSize) {
  return new QPageSize(
      self->QPlatformPrintDevice::supportedPageSize(
          *pointSize));
}

//  QPageSize QPlatformPrintDevice::supportedPageSize(const QSizeF &size,
//      QPageSize::Unit units) const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_own_ZNK20QPlatformPrintDevice17supportedPageSizeERK6QSizeFN9QPageSize4UnitE(
    const QPlatformPrintDevice *self,
    const QSizeF *size,
    QPageSize::Unit units) {
  return new QPageSize(
      self->QPlatformPrintDevice::supportedPageSize(
          *size,
          units));
}

//  bool QPlatformPrintDevice::supportsCustomPageSizes() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformPrintDevice23supportsCustomPageSizesEv(
    const QPlatformPrintDevice *self) {
  return self->QPlatformPrintDevice::supportsCustomPageSizes();
}

//  QSize QPlatformPrintDevice::minimumPhysicalPageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK20QPlatformPrintDevice23minimumPhysicalPageSizeEv(
    const QPlatformPrintDevice *self) {
  return new QSize(self->QPlatformPrintDevice::minimumPhysicalPageSize());
}

//  QSize QPlatformPrintDevice::maximumPhysicalPageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK20QPlatformPrintDevice23maximumPhysicalPageSizeEv(
    const QPlatformPrintDevice *self) {
  return new QSize(self->QPlatformPrintDevice::maximumPhysicalPageSize());
}

//  QMarginsF QPlatformPrintDevice::printableMargins(const QPageSize
//      &pageSize, QPageLayout::Orientation orientation, int resolution)
//      const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_own_ZNK20QPlatformPrintDevice16printableMarginsERK9QPageSizeN11QPageLayout11OrientationEi(
    const QPlatformPrintDevice *self,
    const QPageSize *pageSize,
    QPageLayout::Orientation orientation,
    int resolution) {
  return new QMarginsF(
      self->QPlatformPrintDevice::printableMargins(
          *pageSize,
          orientation,
          resolution));
}

//  int QPlatformPrintDevice::defaultResolution() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QPlatformPrintDevice17defaultResolutionEv(
    const QPlatformPrintDevice *self) {
  return self->QPlatformPrintDevice::defaultResolution();
}

//  QPrint::InputSlot QPlatformPrintDevice::defaultInputSlot() const
extern "C" Q_DECL_EXPORT
QPrint::InputSlot *ritual_own_ZNK20QPlatformPrintDevice16defaultInputSlotEv(
    const QPlatformPrintDevice *self) {
  return new QPrint::InputSlot(
      self->QPlatformPrintDevice::defaultInputSlot());
}

//  QPrint::OutputBin QPlatformPrintDevice::defaultOutputBin() const
extern "C" Q_DECL_EXPORT
QPrint::OutputBin *ritual_own_ZNK20QPlatformPrintDevice16defaultOutputBinEv(
    const QPlatformPrintDevice *self) {
  return new QPrint::OutputBin(
      self->QPlatformPrintDevice::defaultOutputBin());
}

//  QPrint::DuplexMode QPlatformPrintDevice::defaultDuplexMode() const
extern "C" Q_DECL_EXPORT
QPrint::DuplexMode ritual_own_ZNK20QPlatformPrintDevice17defaultDuplexModeEv(
    const QPlatformPrintDevice *self) {
  return self->QPlatformPrintDevice::defaultDuplexMode();
}

//  QPrint::ColorMode QPlatformPrintDevice::defaultColorMode() const
extern "C" Q_DECL_EXPORT
QPrint::ColorMode ritual_own_ZNK20QPlatformPrintDevice16defaultColorModeEv(
    const QPlatformPrintDevice *self) {
  return self->QPlatformPrintDevice::defaultColorMode();
}

//  QVariant
//      QPlatformPrintDevice::property(QPrintDevice::PrintDevicePropertyKey
//      key) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QPlatformPrintDevice8propertyEN12QPrintDevice22PrintDevicePropertyKeyE(
    const QPlatformPrintDevice *self,
    QPrintDevice::PrintDevicePropertyKey key) {
  return new QVariant(self->QPlatformPrintDevice::property(key));
}

//  bool
//      QPlatformPrintDevice::setProperty(QPrintDevice::PrintDevicePropertyKe
//      y key, const QVariant &value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QPlatformPrintDevice11setPropertyEN12QPrintDevice22PrintDevicePropertyKeyERK8QVariant(
    QPlatformPrintDevice *self,
    QPrintDevice::PrintDevicePropertyKey key,
    const QVariant *value) {
  return self->QPlatformPrintDevice::setProperty(key, *value);
}

//  bool QPlatformPrintDevice::isFeatureAvailable(QPrintDevice::PrintDevicePr
//      opertyKey key, const QVariant &params) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformPrintDevice18isFeatureAvailableEN12QPrintDevice22PrintDevicePropertyKeyERK8QVariant(
    const QPlatformPrintDevice *self,
    QPrintDevice::PrintDevicePropertyKey key,
    const QVariant *params) {
  return self->QPlatformPrintDevice::isFeatureAvailable(key, *params);
}

//  void QPlatformPrintDevice::loadPageSizes() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QPlatformPrintDevice13loadPageSizesEv(
    const QPlatformPrintDevice *self) {
  static_cast<const OwnQPlatformPrintDevice *>(self)->OwnQPlatformPrintDevice::loadPageSizes();
}

//  void QPlatformPrintDevice::loadResolutions() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QPlatformPrintDevice15loadResolutionsEv(
    const QPlatformPrintDevice *self) {
  static_cast<const OwnQPlatformPrintDevice *>(self)->OwnQPlatformPrintDevice::loadResolutions();
}

//  void QPlatformPrintDevice::loadInputSlots() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QPlatformPrintDevice14loadInputSlotsEv(
    const QPlatformPrintDevice *self) {
  static_cast<const OwnQPlatformPrintDevice *>(self)->OwnQPlatformPrintDevice::loadInputSlots();
}

//  void QPlatformPrintDevice::loadOutputBins() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QPlatformPrintDevice14loadOutputBinsEv(
    const QPlatformPrintDevice *self) {
  static_cast<const OwnQPlatformPrintDevice *>(self)->OwnQPlatformPrintDevice::loadOutputBins();
}

//  void QPlatformPrintDevice::loadDuplexModes() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QPlatformPrintDevice15loadDuplexModesEv(
    const QPlatformPrintDevice *self) {
  static_cast<const OwnQPlatformPrintDevice *>(self)->OwnQPlatformPrintDevice::loadDuplexModes();
}

//  void QPlatformPrintDevice::loadColorModes() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QPlatformPrintDevice14loadColorModesEv(
    const QPlatformPrintDevice *self) {
  static_cast<const OwnQPlatformPrintDevice *>(self)->OwnQPlatformPrintDevice::loadColorModes();
}

#if QT_CONFIG(mimetype)
//  void QPlatformPrintDevice::loadMimeTypes() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QPlatformPrintDevice13loadMimeTypesEv(
    const QPlatformPrintDevice *self) {
  static_cast<const OwnQPlatformPrintDevice *>(self)->OwnQPlatformPrintDevice::loadMimeTypes();
}
#endif  // QT_CONFIG(mimetype)

#endif  // !defined(QT_NO_PRINTER)
