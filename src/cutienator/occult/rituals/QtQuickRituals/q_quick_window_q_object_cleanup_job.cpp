//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickwindow_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickWindowQObjectCleanupJob that Python can take functions over in. Every QQuickWindowQObjectCleanupJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickWindowQObjectCleanupJobCall0)(const void *, int *);
class CuteQQuickWindowQObjectCleanupJob : public QQuickWindowQObjectCleanupJob {
public:
  using QQuickWindowQObjectCleanupJob::QQuickWindowQObjectCleanupJob;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QRunnable3runEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QQuickWindowQObjectCleanupJob::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickWindowQObjectCleanupJobCall0 call = reinterpret_cast<CuteQQuickWindowQObjectCleanupJobCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickWindowQObjectCleanupJob::run();
  }
};

//  QQuickWindowQObjectCleanupJob::QQuickWindowQObjectCleanupJob(QObject *o)
extern "C" Q_DECL_EXPORT
QQuickWindowQObjectCleanupJob *ritual_ZN29QQuickWindowQObjectCleanupJobC1EP7QObject(
    QObject *o) {
  return new CuteQQuickWindowQObjectCleanupJob(o);
}

//  void QQuickWindowQObjectCleanupJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickWindowQObjectCleanupJob3runEv(
    QQuickWindowQObjectCleanupJob *self) {
  self->run();
}

//  void QQuickWindowQObjectCleanupJob::schedule(QQuickWindow *window,
//      QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickWindowQObjectCleanupJob8scheduleEP12QQuickWindowP7QObject(
    QQuickWindow *window,
    QObject *object) {
  QQuickWindowQObjectCleanupJob::schedule(window, object);
}

//  a Python function taken by a CuteQQuickWindowQObjectCleanupJob, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickWindowQObjectCleanupJob(
    QQuickWindowQObjectCleanupJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickWindowQObjectCleanupJob *>(self)->take(key, call);
}

//  void QQuickWindowQObjectCleanupJob::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuickWindowQObjectCleanupJob3runEv(
    QQuickWindowQObjectCleanupJob *self) {
  self->QQuickWindowQObjectCleanupJob::run();
}
