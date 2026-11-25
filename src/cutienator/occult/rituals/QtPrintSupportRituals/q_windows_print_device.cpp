//  Written by hand on 2026-11-25 from
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qwindowsprintdevice_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again.
//  Its Cute class is the one the generator wrote for
//  QPlatformPrintDevice, built on QWindowsPrintDevice. Not written:
//  'wcharId', which gives a 'wchar_t' text.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if defined(Q_OS_WIN) && !defined(QT_NO_PRINTER)
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qwindowsprintdevice_p.h>
#include <QtCore/qstring.h>
#include <QtGui/qpagelayout.h>
#include <QtGui/qpagesize.h>
#include <QtCore/qsize.h>
#include <QtCore/qmargins.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprint_p.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmimetype.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QWindowsPrintDevice may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWindowsPrintDevice : QWindowsPrintDevice {
  using QWindowsPrintDevice::loadPageSizes;
  using QWindowsPrintDevice::loadResolutions;
  using QWindowsPrintDevice::loadInputSlots;
  using QWindowsPrintDevice::loadOutputBins;
  using QWindowsPrintDevice::loadDuplexModes;
  using QWindowsPrintDevice::loadColorModes;
};

//  A QWindowsPrintDevice that Python can take functions over in. Every QWindowsPrintDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_PRINTER)
typedef QString * (*CuteQWindowsPrintDeviceCall0)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef QString * (*CuteQWindowsPrintDeviceCall1)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef QString * (*CuteQWindowsPrintDeviceCall2)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef QString * (*CuteQWindowsPrintDeviceCall3)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQWindowsPrintDeviceCall4)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQWindowsPrintDeviceCall5)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQWindowsPrintDeviceCall6)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQWindowsPrintDeviceCall7)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQWindowsPrintDeviceCall8)(const void *, const QPageLayout *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQWindowsPrintDeviceCall9)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQWindowsPrintDeviceCall10)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPageSize * (*CuteQWindowsPrintDeviceCall11)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPageSize * (*CuteQWindowsPrintDeviceCall12)(const void *, const QPageSize *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPageSize * (*CuteQWindowsPrintDeviceCall13)(const void *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPageSize * (*CuteQWindowsPrintDeviceCall14)(const void *, const QString *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPageSize * (*CuteQWindowsPrintDeviceCall15)(const void *, const QSize *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPageSize * (*CuteQWindowsPrintDeviceCall16)(const void *, const QSizeF *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQWindowsPrintDeviceCall17)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QSize * (*CuteQWindowsPrintDeviceCall18)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QSize * (*CuteQWindowsPrintDeviceCall19)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QMarginsF * (*CuteQWindowsPrintDeviceCall20)(const void *, const QPageSize *, int, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQWindowsPrintDeviceCall21)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPrint::InputSlot * (*CuteQWindowsPrintDeviceCall22)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QPrint::OutputBin * (*CuteQWindowsPrintDeviceCall23)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQWindowsPrintDeviceCall24)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef int (*CuteQWindowsPrintDeviceCall25)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef const QVariant * (*CuteQWindowsPrintDeviceCall26)(const void *, int, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQWindowsPrintDeviceCall27)(const void *, int, const QVariant *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef bool (*CuteQWindowsPrintDeviceCall28)(const void *, int, const QVariant *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQWindowsPrintDeviceCall29)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQWindowsPrintDeviceCall30)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQWindowsPrintDeviceCall31)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQWindowsPrintDeviceCall32)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQWindowsPrintDeviceCall33)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
typedef void (*CuteQWindowsPrintDeviceCall34)(const void *, int *);
#endif  // !defined(QT_NO_PRINTER)
#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(mimetype)
typedef void (*CuteQWindowsPrintDeviceCall35)(const void *, int *);
#endif  // QT_CONFIG(mimetype)
#endif  // !defined(QT_NO_PRINTER)
class CuteQWindowsPrintDevice : public QWindowsPrintDevice {
public:
  using QWindowsPrintDevice::QWindowsPrintDevice;
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
      CuteQWindowsPrintDeviceCall0 call = reinterpret_cast<CuteQWindowsPrintDeviceCall0>(taken[0]);
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
      CuteQWindowsPrintDeviceCall1 call = reinterpret_cast<CuteQWindowsPrintDeviceCall1>(taken[1]);
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
      CuteQWindowsPrintDeviceCall2 call = reinterpret_cast<CuteQWindowsPrintDeviceCall2>(taken[2]);
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
      CuteQWindowsPrintDeviceCall3 call = reinterpret_cast<CuteQWindowsPrintDeviceCall3>(taken[3]);
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
  //  bool QWindowsPrintDevice::isValid() const
  bool isValid() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall4 call = reinterpret_cast<CuteQWindowsPrintDeviceCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowsPrintDevice::isValid();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QWindowsPrintDevice::isDefault() const
  bool isDefault() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall5 call = reinterpret_cast<CuteQWindowsPrintDeviceCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowsPrintDevice::isDefault();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QPlatformPrintDevice::isRemote() const
  bool isRemote() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall6 call = reinterpret_cast<CuteQWindowsPrintDeviceCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::isRemote();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPrint::DeviceState QWindowsPrintDevice::state() const
  QPrint::DeviceState state() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall7 call = reinterpret_cast<CuteQWindowsPrintDeviceCall7>(taken[7]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPrint::DeviceState>(given);
    }
    return QWindowsPrintDevice::state();
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
      CuteQWindowsPrintDeviceCall8 call = reinterpret_cast<CuteQWindowsPrintDeviceCall8>(taken[8]);
      bool given = call(this, &layout, resolution, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::isValidPageLayout(layout, resolution);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QWindowsPrintDevice::supportsMultipleCopies() const
  bool supportsMultipleCopies() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall9 call = reinterpret_cast<CuteQWindowsPrintDeviceCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowsPrintDevice::supportsMultipleCopies();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QWindowsPrintDevice::supportsCollateCopies() const
  bool supportsCollateCopies() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall10 call = reinterpret_cast<CuteQWindowsPrintDeviceCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowsPrintDevice::supportsCollateCopies();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPageSize QWindowsPrintDevice::defaultPageSize() const
  QPageSize defaultPageSize() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall11 call = reinterpret_cast<CuteQWindowsPrintDeviceCall11>(taken[11]);
      const QPageSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowsPrintDevice::defaultPageSize();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPageSize QPlatformPrintDevice::supportedPageSize(const QPageSize
  //      &pageSize) const
  QPageSize supportedPageSize(const QPageSize &pageSize) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall12 call = reinterpret_cast<CuteQWindowsPrintDeviceCall12>(taken[12]);
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
      CuteQWindowsPrintDeviceCall13 call = reinterpret_cast<CuteQWindowsPrintDeviceCall13>(taken[13]);
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
      CuteQWindowsPrintDeviceCall14 call = reinterpret_cast<CuteQWindowsPrintDeviceCall14>(taken[14]);
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
      CuteQWindowsPrintDeviceCall15 call = reinterpret_cast<CuteQWindowsPrintDeviceCall15>(taken[15]);
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
      CuteQWindowsPrintDeviceCall16 call = reinterpret_cast<CuteQWindowsPrintDeviceCall16>(taken[16]);
      const QPageSize * given = call(this, &size, static_cast<int>(units), &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::supportedPageSize(size, units);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  bool QWindowsPrintDevice::supportsCustomPageSizes() const
  bool supportsCustomPageSizes() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall17 call = reinterpret_cast<CuteQWindowsPrintDeviceCall17>(taken[17]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowsPrintDevice::supportsCustomPageSizes();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QSize QWindowsPrintDevice::minimumPhysicalPageSize() const
  QSize minimumPhysicalPageSize() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall18 call = reinterpret_cast<CuteQWindowsPrintDeviceCall18>(taken[18]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowsPrintDevice::minimumPhysicalPageSize();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QSize QWindowsPrintDevice::maximumPhysicalPageSize() const
  QSize maximumPhysicalPageSize() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall19 call = reinterpret_cast<CuteQWindowsPrintDeviceCall19>(taken[19]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowsPrintDevice::maximumPhysicalPageSize();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QMarginsF QWindowsPrintDevice::printableMargins(const QPageSize
  //      &pageSize, QPageLayout::Orientation orientation, int resolution)
  //      const
  QMarginsF printableMargins(
      const QPageSize &pageSize,
      QPageLayout::Orientation orientation,
      int resolution) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall20 call = reinterpret_cast<CuteQWindowsPrintDeviceCall20>(taken[20]);
      const QMarginsF * given = call(this, &pageSize, static_cast<int>(orientation), resolution, &handled);
      if (handled && given) return *given;
    }
    return QWindowsPrintDevice::printableMargins(pageSize, orientation, resolution);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  int QWindowsPrintDevice::defaultResolution() const
  int defaultResolution() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall21 call = reinterpret_cast<CuteQWindowsPrintDeviceCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QWindowsPrintDevice::defaultResolution();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPrint::InputSlot QWindowsPrintDevice::defaultInputSlot() const
  QPrint::InputSlot defaultInputSlot() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall22 call = reinterpret_cast<CuteQWindowsPrintDeviceCall22>(taken[22]);
      const QPrint::InputSlot * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindowsPrintDevice::defaultInputSlot();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPrint::OutputBin QPlatformPrintDevice::defaultOutputBin() const
  QPrint::OutputBin defaultOutputBin() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall23 call = reinterpret_cast<CuteQWindowsPrintDeviceCall23>(taken[23]);
      const QPrint::OutputBin * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformPrintDevice::defaultOutputBin();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPrint::DuplexMode QWindowsPrintDevice::defaultDuplexMode() const
  QPrint::DuplexMode defaultDuplexMode() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall24 call = reinterpret_cast<CuteQWindowsPrintDeviceCall24>(taken[24]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPrint::DuplexMode>(given);
    }
    return QWindowsPrintDevice::defaultDuplexMode();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  QPrint::ColorMode QWindowsPrintDevice::defaultColorMode() const
  QPrint::ColorMode defaultColorMode() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall25 call = reinterpret_cast<CuteQWindowsPrintDeviceCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return static_cast<QPrint::ColorMode>(given);
    }
    return QWindowsPrintDevice::defaultColorMode();
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
      CuteQWindowsPrintDeviceCall26 call = reinterpret_cast<CuteQWindowsPrintDeviceCall26>(taken[26]);
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
      CuteQWindowsPrintDeviceCall27 call = reinterpret_cast<CuteQWindowsPrintDeviceCall27>(taken[27]);
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
      CuteQWindowsPrintDeviceCall28 call = reinterpret_cast<CuteQWindowsPrintDeviceCall28>(taken[28]);
      bool given = call(this, static_cast<int>(key), &params, &handled);
      if (handled) return given;
    }
    return QPlatformPrintDevice::isFeatureAvailable(key, params);
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QWindowsPrintDevice::loadPageSizes() const
  void loadPageSizes() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall29 call = reinterpret_cast<CuteQWindowsPrintDeviceCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsPrintDevice::loadPageSizes();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QWindowsPrintDevice::loadResolutions() const
  void loadResolutions() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall30 call = reinterpret_cast<CuteQWindowsPrintDeviceCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsPrintDevice::loadResolutions();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QWindowsPrintDevice::loadInputSlots() const
  void loadInputSlots() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall31 call = reinterpret_cast<CuteQWindowsPrintDeviceCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsPrintDevice::loadInputSlots();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QWindowsPrintDevice::loadOutputBins() const
  void loadOutputBins() const override {
    if (taken[32]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall32 call = reinterpret_cast<CuteQWindowsPrintDeviceCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsPrintDevice::loadOutputBins();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QWindowsPrintDevice::loadDuplexModes() const
  void loadDuplexModes() const override {
    if (taken[33]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall33 call = reinterpret_cast<CuteQWindowsPrintDeviceCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsPrintDevice::loadDuplexModes();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
  //  void QWindowsPrintDevice::loadColorModes() const
  void loadColorModes() const override {
    if (taken[34]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall34 call = reinterpret_cast<CuteQWindowsPrintDeviceCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsPrintDevice::loadColorModes();
  }
#endif  // !defined(QT_NO_PRINTER)

#if !defined(QT_NO_PRINTER)
#if QT_CONFIG(mimetype)
  //  void QPlatformPrintDevice::loadMimeTypes() const
  void loadMimeTypes() const override {
    if (taken[35]) {
      int handled = 0;
      CuteQWindowsPrintDeviceCall35 call = reinterpret_cast<CuteQWindowsPrintDeviceCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformPrintDevice::loadMimeTypes();
  }
#endif  // QT_CONFIG(mimetype)
#endif  // !defined(QT_NO_PRINTER)
};

//  QWindowsPrintDevice::QWindowsPrintDevice()
extern "C" Q_DECL_EXPORT
QWindowsPrintDevice *ritual_ZN19QWindowsPrintDeviceC1Ev() {
  return new CuteQWindowsPrintDevice();
}

//  QWindowsPrintDevice::QWindowsPrintDevice(const QString &id)
extern "C" Q_DECL_EXPORT
QWindowsPrintDevice *ritual_ZN19QWindowsPrintDeviceC1ERK7QString(
    const QString *id) {
  return new CuteQWindowsPrintDevice(*id);
}

//  QWindowsPrintDevice::~QWindowsPrintDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWindowsPrintDeviceD1Ev(QWindowsPrintDevice *self) {
  delete self;
}

//  bool QWindowsPrintDevice::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWindowsPrintDevice7isValidEv(
    const QWindowsPrintDevice *self) {
  return self->isValid();
}

//  bool QWindowsPrintDevice::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWindowsPrintDevice9isDefaultEv(
    const QWindowsPrintDevice *self) {
  return self->isDefault();
}

//  QPrint::DeviceState QWindowsPrintDevice::state() const
extern "C" Q_DECL_EXPORT
QPrint::DeviceState ritual_ZNK19QWindowsPrintDevice5stateEv(
    const QWindowsPrintDevice *self) {
  return self->state();
}

//  QPageSize QWindowsPrintDevice::defaultPageSize() const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_ZNK19QWindowsPrintDevice15defaultPageSizeEv(
    const QWindowsPrintDevice *self) {
  return new QPageSize(self->defaultPageSize());
}

//  QMarginsF QWindowsPrintDevice::printableMargins(const QPageSize
//      &pageSize, QPageLayout::Orientation orientation, int resolution)
//      const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK19QWindowsPrintDevice16printableMarginsERK9QPageSizeN11QPageLayout11OrientationEi(
    const QWindowsPrintDevice *self,
    const QPageSize *pageSize,
    QPageLayout::Orientation orientation,
    int resolution) {
  return new QMarginsF(
      self->printableMargins(*pageSize, orientation, resolution));
}

//  int QWindowsPrintDevice::defaultResolution() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QWindowsPrintDevice17defaultResolutionEv(
    const QWindowsPrintDevice *self) {
  return self->defaultResolution();
}

//  QPrint::InputSlot QWindowsPrintDevice::defaultInputSlot() const
extern "C" Q_DECL_EXPORT
QPrint::InputSlot *ritual_ZNK19QWindowsPrintDevice16defaultInputSlotEv(
    const QWindowsPrintDevice *self) {
  return new QPrint::InputSlot(self->defaultInputSlot());
}

//  QPrint::DuplexMode QWindowsPrintDevice::defaultDuplexMode() const
extern "C" Q_DECL_EXPORT
QPrint::DuplexMode ritual_ZNK19QWindowsPrintDevice17defaultDuplexModeEv(
    const QWindowsPrintDevice *self) {
  return self->defaultDuplexMode();
}

//  QPrint::ColorMode QWindowsPrintDevice::defaultColorMode() const
extern "C" Q_DECL_EXPORT
QPrint::ColorMode ritual_ZNK19QWindowsPrintDevice16defaultColorModeEv(
    const QWindowsPrintDevice *self) {
  return self->defaultColorMode();
}

//  bool QWindowsPrintDevice::supportsCollateCopies() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWindowsPrintDevice21supportsCollateCopiesEv(
    const QWindowsPrintDevice *self) {
  return self->supportsCollateCopies();
}

//  bool QWindowsPrintDevice::supportsMultipleCopies() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWindowsPrintDevice22supportsMultipleCopiesEv(
    const QWindowsPrintDevice *self) {
  return self->supportsMultipleCopies();
}

//  bool QWindowsPrintDevice::supportsCustomPageSizes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWindowsPrintDevice23supportsCustomPageSizesEv(
    const QWindowsPrintDevice *self) {
  return self->supportsCustomPageSizes();
}

//  QSize QWindowsPrintDevice::minimumPhysicalPageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QWindowsPrintDevice23minimumPhysicalPageSizeEv(
    const QWindowsPrintDevice *self) {
  return new QSize(self->minimumPhysicalPageSize());
}

//  QSize QWindowsPrintDevice::maximumPhysicalPageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QWindowsPrintDevice23maximumPhysicalPageSizeEv(
    const QWindowsPrintDevice *self) {
  return new QSize(self->maximumPhysicalPageSize());
}

//  QStringList QWindowsPrintDevice::availablePrintDeviceIds()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN19QWindowsPrintDevice23availablePrintDeviceIdsEv() {
  return new QList<QString>(QWindowsPrintDevice::availablePrintDeviceIds());
}

//  QString QWindowsPrintDevice::defaultPrintDeviceId()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QWindowsPrintDevice20defaultPrintDeviceIdEv() {
  return new QString(QWindowsPrintDevice::defaultPrintDeviceId());
}

//  void QWindowsPrintDevice::loadPageSizes() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QWindowsPrintDevice13loadPageSizesEv(
    const QWindowsPrintDevice *self) {
  self->loadPageSizes();
}

//  void QWindowsPrintDevice::loadResolutions() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QWindowsPrintDevice15loadResolutionsEv(
    const QWindowsPrintDevice *self) {
  self->loadResolutions();
}

//  void QWindowsPrintDevice::loadInputSlots() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QWindowsPrintDevice14loadInputSlotsEv(
    const QWindowsPrintDevice *self) {
  self->loadInputSlots();
}

//  void QWindowsPrintDevice::loadOutputBins() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QWindowsPrintDevice14loadOutputBinsEv(
    const QWindowsPrintDevice *self) {
  self->loadOutputBins();
}

//  void QWindowsPrintDevice::loadDuplexModes() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QWindowsPrintDevice15loadDuplexModesEv(
    const QWindowsPrintDevice *self) {
  self->loadDuplexModes();
}

//  void QWindowsPrintDevice::loadColorModes() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QWindowsPrintDevice14loadColorModesEv(
    const QWindowsPrintDevice *self) {
  self->loadColorModes();
}

//  void QWindowsPrintDevice::loadCopiesSupport() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QWindowsPrintDevice17loadCopiesSupportEv(
    const QWindowsPrintDevice *self) {
  self->loadCopiesSupport();
}

//  void QWindowsPrintDevice::loadMinMaxPageSizes() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QWindowsPrintDevice19loadMinMaxPageSizesEv(
    const QWindowsPrintDevice *self) {
  self->loadMinMaxPageSizes();
}

//  a Python function taken by a CuteQWindowsPrintDevice, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsPrintDevice(
    QWindowsPrintDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsPrintDevice *>(self)->take(key, call);
}

//  bool QWindowsPrintDevice::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QWindowsPrintDevice7isValidEv(
    const QWindowsPrintDevice *self) {
  return self->QWindowsPrintDevice::isValid();
}

//  bool QWindowsPrintDevice::isDefault() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QWindowsPrintDevice9isDefaultEv(
    const QWindowsPrintDevice *self) {
  return self->QWindowsPrintDevice::isDefault();
}

//  QPrint::DeviceState QWindowsPrintDevice::state() const
extern "C" Q_DECL_EXPORT
QPrint::DeviceState ritual_own_ZNK19QWindowsPrintDevice5stateEv(
    const QWindowsPrintDevice *self) {
  return self->QWindowsPrintDevice::state();
}

//  QPageSize QWindowsPrintDevice::defaultPageSize() const
extern "C" Q_DECL_EXPORT
QPageSize *ritual_own_ZNK19QWindowsPrintDevice15defaultPageSizeEv(
    const QWindowsPrintDevice *self) {
  return new QPageSize(self->QWindowsPrintDevice::defaultPageSize());
}

//  QMarginsF QWindowsPrintDevice::printableMargins(const QPageSize
//      &pageSize, QPageLayout::Orientation orientation, int resolution)
//      const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_own_ZNK19QWindowsPrintDevice16printableMarginsERK9QPageSizeN11QPageLayout11OrientationEi(
    const QWindowsPrintDevice *self,
    const QPageSize *pageSize,
    QPageLayout::Orientation orientation,
    int resolution) {
  return new QMarginsF(
      self->QWindowsPrintDevice::printableMargins(*pageSize, orientation, resolution));
}

//  int QWindowsPrintDevice::defaultResolution() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QWindowsPrintDevice17defaultResolutionEv(
    const QWindowsPrintDevice *self) {
  return self->QWindowsPrintDevice::defaultResolution();
}

//  QPrint::InputSlot QWindowsPrintDevice::defaultInputSlot() const
extern "C" Q_DECL_EXPORT
QPrint::InputSlot *ritual_own_ZNK19QWindowsPrintDevice16defaultInputSlotEv(
    const QWindowsPrintDevice *self) {
  return new QPrint::InputSlot(self->QWindowsPrintDevice::defaultInputSlot());
}

//  QPrint::DuplexMode QWindowsPrintDevice::defaultDuplexMode() const
extern "C" Q_DECL_EXPORT
QPrint::DuplexMode ritual_own_ZNK19QWindowsPrintDevice17defaultDuplexModeEv(
    const QWindowsPrintDevice *self) {
  return self->QWindowsPrintDevice::defaultDuplexMode();
}

//  QPrint::ColorMode QWindowsPrintDevice::defaultColorMode() const
extern "C" Q_DECL_EXPORT
QPrint::ColorMode ritual_own_ZNK19QWindowsPrintDevice16defaultColorModeEv(
    const QWindowsPrintDevice *self) {
  return self->QWindowsPrintDevice::defaultColorMode();
}

//  bool QWindowsPrintDevice::supportsCollateCopies() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QWindowsPrintDevice21supportsCollateCopiesEv(
    const QWindowsPrintDevice *self) {
  return self->QWindowsPrintDevice::supportsCollateCopies();
}

//  bool QWindowsPrintDevice::supportsMultipleCopies() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QWindowsPrintDevice22supportsMultipleCopiesEv(
    const QWindowsPrintDevice *self) {
  return self->QWindowsPrintDevice::supportsMultipleCopies();
}

//  bool QWindowsPrintDevice::supportsCustomPageSizes() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QWindowsPrintDevice23supportsCustomPageSizesEv(
    const QWindowsPrintDevice *self) {
  return self->QWindowsPrintDevice::supportsCustomPageSizes();
}

//  QSize QWindowsPrintDevice::minimumPhysicalPageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK19QWindowsPrintDevice23minimumPhysicalPageSizeEv(
    const QWindowsPrintDevice *self) {
  return new QSize(self->QWindowsPrintDevice::minimumPhysicalPageSize());
}

//  QSize QWindowsPrintDevice::maximumPhysicalPageSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK19QWindowsPrintDevice23maximumPhysicalPageSizeEv(
    const QWindowsPrintDevice *self) {
  return new QSize(self->QWindowsPrintDevice::maximumPhysicalPageSize());
}

//  void QWindowsPrintDevice::loadPageSizes() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QWindowsPrintDevice13loadPageSizesEv(
    const QWindowsPrintDevice *self) {
  static_cast<const OwnQWindowsPrintDevice *>(self)->OwnQWindowsPrintDevice::loadPageSizes();
}

//  void QWindowsPrintDevice::loadResolutions() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QWindowsPrintDevice15loadResolutionsEv(
    const QWindowsPrintDevice *self) {
  static_cast<const OwnQWindowsPrintDevice *>(self)->OwnQWindowsPrintDevice::loadResolutions();
}

//  void QWindowsPrintDevice::loadInputSlots() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QWindowsPrintDevice14loadInputSlotsEv(
    const QWindowsPrintDevice *self) {
  static_cast<const OwnQWindowsPrintDevice *>(self)->OwnQWindowsPrintDevice::loadInputSlots();
}

//  void QWindowsPrintDevice::loadOutputBins() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QWindowsPrintDevice14loadOutputBinsEv(
    const QWindowsPrintDevice *self) {
  static_cast<const OwnQWindowsPrintDevice *>(self)->OwnQWindowsPrintDevice::loadOutputBins();
}

//  void QWindowsPrintDevice::loadDuplexModes() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QWindowsPrintDevice15loadDuplexModesEv(
    const QWindowsPrintDevice *self) {
  static_cast<const OwnQWindowsPrintDevice *>(self)->OwnQWindowsPrintDevice::loadDuplexModes();
}

//  void QWindowsPrintDevice::loadColorModes() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK19QWindowsPrintDevice14loadColorModesEv(
    const QWindowsPrintDevice *self) {
  static_cast<const OwnQWindowsPrintDevice *>(self)->OwnQWindowsPrintDevice::loadColorModes();
}

#endif  // defined(Q_OS_WIN) && !defined(QT_NO_PRINTER)
