//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpagedpaintdevice_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpagedpaintdevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpagelayout.h>
#include <QtGui/qpagesize.h>
#include <QtCore/qmargins.h>
#include <cstring>

//  A QPagedPaintDevicePrivate that Python can take functions over in. Every QPagedPaintDevicePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPagedPaintDevicePrivateCall0)(const void *, const QPageLayout *, int *);
typedef bool (*CuteQPagedPaintDevicePrivateCall1)(const void *, const QPageSize *, int *);
typedef bool (*CuteQPagedPaintDevicePrivateCall2)(const void *, int, int *);
typedef bool (*CuteQPagedPaintDevicePrivateCall3)(const void *, const QMarginsF *, int, int *);
typedef const QPageLayout * (*CuteQPagedPaintDevicePrivateCall4)(const void *, int *);
class CuteQPagedPaintDevicePrivate : public QPagedPaintDevicePrivate {
public:
  using QPagedPaintDevicePrivate::QPagedPaintDevicePrivate;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QPagedPaintDevicePrivate13setPageLayoutERK11QPageLayout")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QPagedPaintDevicePrivate11setPageSizeERK9QPageSize")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QPagedPaintDevicePrivate18setPageOrientationEN11QPageLayout11OrientationE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QPagedPaintDevicePrivate14setPageMarginsERK9QMarginsFN11QPageLayout4UnitE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QPagedPaintDevicePrivate10pageLayoutEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  bool QPagedPaintDevicePrivate::setPageLayout(const QPageLayout
  //      &newPageLayout)
  bool setPageLayout(const QPageLayout &newPageLayout) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPagedPaintDevicePrivateCall0 call = reinterpret_cast<CuteQPagedPaintDevicePrivateCall0>(taken[0]);
      bool given = call(this, &newPageLayout, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QPagedPaintDevicePrivate::setPageSize(const QPageSize &pageSize)
  bool setPageSize(const QPageSize &pageSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPagedPaintDevicePrivateCall1 call = reinterpret_cast<CuteQPagedPaintDevicePrivateCall1>(taken[1]);
      bool given = call(this, &pageSize, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool
  //      QPagedPaintDevicePrivate::setPageOrientation(QPageLayout::Orienta
  //      tion orientation)
  bool setPageOrientation(QPageLayout::Orientation orientation) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPagedPaintDevicePrivateCall2 call = reinterpret_cast<CuteQPagedPaintDevicePrivateCall2>(taken[2]);
      bool given = call(this, static_cast<int>(orientation), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool QPagedPaintDevicePrivate::setPageMargins(const QMarginsF
  //      &margins, QPageLayout::Unit units)
  bool setPageMargins(
      const QMarginsF &margins,
      QPageLayout::Unit units) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPagedPaintDevicePrivateCall3 call = reinterpret_cast<CuteQPagedPaintDevicePrivateCall3>(taken[3]);
      bool given = call(this, &margins, static_cast<int>(units), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QPageLayout QPagedPaintDevicePrivate::pageLayout() const
  QPageLayout pageLayout() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPagedPaintDevicePrivateCall4 call = reinterpret_cast<CuteQPagedPaintDevicePrivateCall4>(taken[4]);
      const QPageLayout * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  QPagedPaintDevicePrivate::QPagedPaintDevicePrivate()
extern "C" Q_DECL_EXPORT
QPagedPaintDevicePrivate *ritual_ZN24QPagedPaintDevicePrivateC1Ev() {
  return new CuteQPagedPaintDevicePrivate();
}

//  QPagedPaintDevicePrivate::~QPagedPaintDevicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QPagedPaintDevicePrivateD1Ev(
    QPagedPaintDevicePrivate *self) {
  delete self;
}

//  bool QPagedPaintDevicePrivate::setPageLayout(const QPageLayout
//      &newPageLayout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QPagedPaintDevicePrivate13setPageLayoutERK11QPageLayout(
    QPagedPaintDevicePrivate *self,
    const QPageLayout *newPageLayout) {
  return self->setPageLayout(*newPageLayout);
}

//  bool QPagedPaintDevicePrivate::setPageSize(const QPageSize &pageSize)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QPagedPaintDevicePrivate11setPageSizeERK9QPageSize(
    QPagedPaintDevicePrivate *self,
    const QPageSize *pageSize) {
  return self->setPageSize(*pageSize);
}

//  bool
//      QPagedPaintDevicePrivate::setPageOrientation(QPageLayout::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QPagedPaintDevicePrivate18setPageOrientationEN11QPageLayout11OrientationE(
    QPagedPaintDevicePrivate *self,
    QPageLayout::Orientation orientation) {
  return self->setPageOrientation(orientation);
}

//  bool QPagedPaintDevicePrivate::setPageMargins(const QMarginsF &margins,
//      QPageLayout::Unit units)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QPagedPaintDevicePrivate14setPageMarginsERK9QMarginsFN11QPageLayout4UnitE(
    QPagedPaintDevicePrivate *self,
    const QMarginsF *margins,
    QPageLayout::Unit units) {
  return self->setPageMargins(*margins, units);
}

//  QPageLayout QPagedPaintDevicePrivate::pageLayout() const
extern "C" Q_DECL_EXPORT
QPageLayout *ritual_ZNK24QPagedPaintDevicePrivate10pageLayoutEv(
    const QPagedPaintDevicePrivate *self) {
  return new QPageLayout(self->pageLayout());
}

//  QPagedPaintDevicePrivate *QPagedPaintDevicePrivate::get(QPagedPaintDevice
//      *pd)
extern "C" Q_DECL_EXPORT
QPagedPaintDevicePrivate *ritual_ZN24QPagedPaintDevicePrivate3getEP17QPagedPaintDevice(
    QPagedPaintDevice *pd) {
  return QPagedPaintDevicePrivate::get(pd);
}

//  a Python function taken by a CuteQPagedPaintDevicePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPagedPaintDevicePrivate(
    QPagedPaintDevicePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPagedPaintDevicePrivate *>(self)->take(key, call);
}
