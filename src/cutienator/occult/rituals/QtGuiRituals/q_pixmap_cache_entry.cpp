//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpixmapcache_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpixmapcache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QPixmapCacheEntry that Python can take functions over in. Every QPixmapCacheEntry
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQPixmapCacheEntryCall0)(const void *, int *);
typedef void * (*CuteQPixmapCacheEntryCall1)(const void *, int *);
typedef int (*CuteQPixmapCacheEntryCall2)(const void *, int, int *);
typedef void (*CuteQPixmapCacheEntryCall3)(const void *, QPainter *, int *);
typedef void * (*CuteQPixmapCacheEntryCall4)(const void *, QPoint *, int *);
typedef void * (*CuteQPixmapCacheEntryCall5)(const void *, int *);
class CuteQPixmapCacheEntry : public QPixmapCacheEntry {
public:
  using QPixmapCacheEntry::QPixmapCacheEntry;
  CuteQPixmapCacheEntry(const QPixmapCacheEntry &other) : QPixmapCacheEntry(other) {}
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK12QPaintDevice7devTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11paintEngineEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice6metricENS_17PaintDeviceMetricE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice11initPainterEP8QPainter")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice10redirectedEP6QPoint")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK12QPaintDevice13sharedPainterEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  int QPixmap::devType() const
  int devType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPixmapCacheEntryCall0 call = reinterpret_cast<CuteQPixmapCacheEntryCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QPixmap::devType();
  }

  //  QPaintEngine *QPixmap::paintEngine() const
  QPaintEngine *paintEngine() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPixmapCacheEntryCall1 call = reinterpret_cast<CuteQPixmapCacheEntryCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPixmap::paintEngine();
  }

  //  int QPixmap::metric(PaintDeviceMetric a0) const
  int metric(QPaintDevice::PaintDeviceMetric a0) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPixmapCacheEntryCall2 call = reinterpret_cast<CuteQPixmapCacheEntryCall2>(taken[2]);
      int given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QPixmap::metric(a0);
  }

  //  void QPaintDevice::initPainter(QPainter *painter) const
  void initPainter(QPainter *painter) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPixmapCacheEntryCall3 call = reinterpret_cast<CuteQPixmapCacheEntryCall3>(taken[3]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QPaintDevice::initPainter(painter);
  }

  //  QPaintDevice *QPaintDevice::redirected(QPoint *offset) const
  QPaintDevice *redirected(QPoint *offset) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPixmapCacheEntryCall4 call = reinterpret_cast<CuteQPixmapCacheEntryCall4>(taken[4]);
      void * given = call(this, offset, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QPaintDevice::redirected(offset);
  }

  //  QPainter *QPaintDevice::sharedPainter() const
  QPainter *sharedPainter() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPixmapCacheEntryCall5 call = reinterpret_cast<CuteQPixmapCacheEntryCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPainter *>(given);
    }
    return QPaintDevice::sharedPainter();
  }
};

//  a Python function taken by a CuteQPixmapCacheEntry, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPixmapCacheEntry(
    QPixmapCacheEntry *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPixmapCacheEntry *>(self)->take(key, call);
}
