//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpagedpaintdevice.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpagedpaintdevice.h>
#include <QtGui/qpagelayout.h>
#include <QtGui/qpagesize.h>
#include <QtCore/qmargins.h>
#include <QtGui/qpageranges.h>
#include <cstring>

//  A QPagedPaintDevice that Python can take functions over in. Every QPagedPaintDevice
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPagedPaintDeviceCall0)(const void *, int *);
typedef bool (*CuteQPagedPaintDeviceCall1)(const void *, const QPageLayout *, int *);
typedef bool (*CuteQPagedPaintDeviceCall2)(const void *, const QPageSize *, int *);
typedef bool (*CuteQPagedPaintDeviceCall3)(const void *, int, int *);
typedef bool (*CuteQPagedPaintDeviceCall4)(const void *, const QMarginsF *, int, int *);
typedef void (*CuteQPagedPaintDeviceCall5)(const void *, const QPageRanges *, int *);
typedef int (*CuteQPagedPaintDeviceCall6)(const void *, int *);
typedef void * (*CuteQPagedPaintDeviceCall7)(const void *, int *);
typedef int (*CuteQPagedPaintDeviceCall8)(const void *, int, int *);
typedef void (*CuteQPagedPaintDeviceCall9)(const void *, QPainter *, int *);
typedef void * (*CuteQPagedPaintDeviceCall10)(const void *, QPoint *, int *);
typedef void * (*CuteQPagedPaintDeviceCall11)(const void *, int *);
class CuteQPagedPaintDevice : public QPagedPaintDevice {
public:
  using QPagedPaintDevice::QPagedPaintDevice;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice7newPageEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice13setPageLayoutERK11QPageLayout")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice11setPageSizeERK9QPageSize")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice18setPageOrientationEN11QPageLayout11OrientationE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice14setPageMarginsERK9QMarginsFN11QPageLayout4UnitE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPagedPaintDevice13setPageRangesERK11QPageRanges")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

  //  bool QPagedPaintDevice::newPage()
  bool newPage() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPagedPaintDeviceCall0 call = reinterpret_cast<CuteQPagedPaintDeviceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QPagedPaintDevice::setPageLayout(const QPageLayout &pageLayout)
  bool setPageLayout(const QPageLayout &pageLayout) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPagedPaintDeviceCall1 call = reinterpret_cast<CuteQPagedPaintDeviceCall1>(taken[1]);
      bool given = call(this, &pageLayout, &handled);
      if (handled) return given;
    }
    return QPagedPaintDevice::setPageLayout(pageLayout);
  }

  //  bool QPagedPaintDevice::setPageSize(const QPageSize &pageSize)
  bool setPageSize(const QPageSize &pageSize) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPagedPaintDeviceCall2 call = reinterpret_cast<CuteQPagedPaintDeviceCall2>(taken[2]);
      bool given = call(this, &pageSize, &handled);
      if (handled) return given;
    }
    return QPagedPaintDevice::setPageSize(pageSize);
  }

  //  bool QPagedPaintDevice::setPageOrientation(QPageLayout::Orientation
  //      orientation)
  bool setPageOrientation(QPageLayout::Orientation orientation) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPagedPaintDeviceCall3 call = reinterpret_cast<CuteQPagedPaintDeviceCall3>(taken[3]);
      bool given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return given;
    }
    return QPagedPaintDevice::setPageOrientation(orientation);
  }

  //  bool QPagedPaintDevice::setPageMargins(const QMarginsF &margins,
  //      QPageLayout::Unit units)
  bool setPageMargins(
      const QMarginsF &margins,
      QPageLayout::Unit units) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPagedPaintDeviceCall4 call = reinterpret_cast<CuteQPagedPaintDeviceCall4>(taken[4]);
      bool given = call(this, &margins, static_cast<int>(units), &handled);
      if (handled) return given;
    }
    return QPagedPaintDevice::setPageMargins(margins, units);
  }

  //  void QPagedPaintDevice::setPageRanges(const QPageRanges &ranges)
  void setPageRanges(const QPageRanges &ranges) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPagedPaintDeviceCall5 call = reinterpret_cast<CuteQPagedPaintDeviceCall5>(taken[5]);
      call(this, &ranges, &handled);
      if (handled) return;
    }
    QPagedPaintDevice::setPageRanges(ranges);
  }

  //  int QPaintDevice::devType() const
  int devType() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPagedPaintDeviceCall6 call = reinterpret_cast<CuteQPagedPaintDeviceCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPaintDevice::devType();
  }

  //  QPaintEngine *QPaintDevice::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPagedPaintDeviceCall7 call = reinterpret_cast<CuteQPagedPaintDeviceCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return {};
  }

  //  int QPaintDevice::metric(PaintDeviceMetric metric) const
  int metric(QPaintDevice::PaintDeviceMetric metric) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPagedPaintDeviceCall8 call = reinterpret_cast<CuteQPagedPaintDeviceCall8>(taken[8]);
      int given = call(this, static_cast<int>(metric), &handled);
      if (handled) return given;
    }
    return QPaintDevice::metric(metric);
  }

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPagedPaintDeviceCall9 call = reinterpret_cast<CuteQPagedPaintDeviceCall9>(taken[9]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPagedPaintDeviceCall10 call = reinterpret_cast<CuteQPagedPaintDeviceCall10>(taken[10]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QPaintDevice::redirected(offset);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPagedPaintDeviceCall11 call = reinterpret_cast<CuteQPagedPaintDeviceCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }
};

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

//  QPagedPaintDevicePrivate *QPagedPaintDevice::dd()
extern "C" Q_DECL_EXPORT
QPagedPaintDevicePrivate *ritual_ZN17QPagedPaintDevice2ddEv(
    QPagedPaintDevice *self) {
  return self->dd();
}

//  a Python function taken by a CuteQPagedPaintDevice, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPagedPaintDevice(
    QPagedPaintDevice *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPagedPaintDevice *>(self)->take(key, call);
}

//  bool QPagedPaintDevice::setPageLayout(const QPageLayout &pageLayout)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QPagedPaintDevice13setPageLayoutERK11QPageLayout(
    QPagedPaintDevice *self,
    const QPageLayout *pageLayout) {
  return self->QPagedPaintDevice::setPageLayout(*pageLayout);
}

//  bool QPagedPaintDevice::setPageSize(const QPageSize &pageSize)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QPagedPaintDevice11setPageSizeERK9QPageSize(
    QPagedPaintDevice *self,
    const QPageSize *pageSize) {
  return self->QPagedPaintDevice::setPageSize(*pageSize);
}

//  bool QPagedPaintDevice::setPageOrientation(QPageLayout::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QPagedPaintDevice18setPageOrientationEN11QPageLayout11OrientationE(
    QPagedPaintDevice *self,
    QPageLayout::Orientation orientation) {
  return self->QPagedPaintDevice::setPageOrientation(orientation);
}

//  bool QPagedPaintDevice::setPageMargins(const QMarginsF &margins,
//      QPageLayout::Unit units)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QPagedPaintDevice14setPageMarginsERK9QMarginsFN11QPageLayout4UnitE(
    QPagedPaintDevice *self,
    const QMarginsF *margins,
    QPageLayout::Unit units) {
  return self->QPagedPaintDevice::setPageMargins(*margins, units);
}

//  void QPagedPaintDevice::setPageRanges(const QPageRanges &ranges)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QPagedPaintDevice13setPageRangesERK11QPageRanges(
    QPagedPaintDevice *self,
    const QPageRanges *ranges) {
  self->QPagedPaintDevice::setPageRanges(*ranges);
}
