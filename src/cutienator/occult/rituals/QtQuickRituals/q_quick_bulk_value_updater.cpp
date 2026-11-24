//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>
#include <cstring>

//  A QQuickBulkValueUpdater that Python can take functions over in. Every QQuickBulkValueUpdater
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickBulkValueUpdaterCall0)(const void *, qreal, int *);
typedef void (*CuteQQuickBulkValueUpdaterCall1)(const void *, const QDebug *, int, int *);
class CuteQQuickBulkValueUpdater : public QQuickBulkValueUpdater {
public:
  using QQuickBulkValueUpdater::QQuickBulkValueUpdater;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QQuickBulkValueUpdater8setValueEd")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK22QQuickBulkValueUpdater12debugUpdaterE6QDebugi")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QQuickBulkValueUpdater::setValue(qreal value)
  void setValue(qreal value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickBulkValueUpdaterCall0 call = reinterpret_cast<CuteQQuickBulkValueUpdaterCall0>(taken[0]);
      call(this, value, &handled);
      if (handled) return;
    }
  }

  //  void QQuickBulkValueUpdater::debugUpdater(QDebug a0, int a1) const
  void debugUpdater(QDebug a0, int a1) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickBulkValueUpdaterCall1 call = reinterpret_cast<CuteQQuickBulkValueUpdaterCall1>(taken[1]);
      call(this, &a0, a1, &handled);
      if (handled) return;
    }
    QQuickBulkValueUpdater::debugUpdater(a0, a1);
  }
};

//  QQuickBulkValueUpdater::~QQuickBulkValueUpdater()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickBulkValueUpdaterD1Ev(QQuickBulkValueUpdater *self) {
  delete self;
}

//  void QQuickBulkValueUpdater::setValue(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickBulkValueUpdater8setValueEd(
    QQuickBulkValueUpdater *self,
    qreal value) {
  self->setValue(value);
}

//  void QQuickBulkValueUpdater::debugUpdater(QDebug a0, int a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QQuickBulkValueUpdater12debugUpdaterE6QDebugi(
    const QQuickBulkValueUpdater *self,
    const QDebug *a0,
    int a1) {
  self->debugUpdater(*a0, a1);
}

//  a Python function taken by a CuteQQuickBulkValueUpdater, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickBulkValueUpdater(
    QQuickBulkValueUpdater *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickBulkValueUpdater *>(self)->take(key, call);
}

//  void QQuickBulkValueUpdater::debugUpdater(QDebug a0, int a1) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK22QQuickBulkValueUpdater12debugUpdaterE6QDebugi(
    const QQuickBulkValueUpdater *self,
    const QDebug *a0,
    int a1) {
  self->QQuickBulkValueUpdater::debugUpdater(*a0, a1);
}
