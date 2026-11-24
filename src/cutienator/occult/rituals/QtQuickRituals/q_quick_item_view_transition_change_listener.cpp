//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_viewtransitions)
#if QT_CONFIG(quick_viewtransitions)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemviewtransition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickItemViewTransitionChangeListener that Python can take functions over in. Every QQuickItemViewTransitionChangeListener
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_viewtransitions)
typedef void (*CuteQQuickItemViewTransitionChangeListenerCall0)(const void *, QQuickItemViewTransitionableItem *, int *);
#endif  // QT_CONFIG(quick_viewtransitions)
class CuteQQuickItemViewTransitionChangeListener : public QQuickItemViewTransitionChangeListener {
public:
  using QQuickItemViewTransitionChangeListener::QQuickItemViewTransitionChangeListener;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_viewtransitions)
    if (!std::strcmp(key, "_ZN38QQuickItemViewTransitionChangeListener26viewItemTransitionFinishedEP32QQuickItemViewTransitionableItem")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_viewtransitions)
    return false;
  }

#if QT_CONFIG(quick_viewtransitions)
  //  void QQuickItemViewTransitionChangeListener::viewItemTransitionFinish
  //      ed(QQuickItemViewTransitionableItem *item)
  void viewItemTransitionFinished(
      QQuickItemViewTransitionableItem *item) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickItemViewTransitionChangeListenerCall0 call = reinterpret_cast<CuteQQuickItemViewTransitionChangeListenerCall0>(taken[0]);
      call(this, item, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_viewtransitions)
};

//  QQuickItemViewTransitionChangeListener::~QQuickItemViewTransitionChangeLi
//      stener()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuickItemViewTransitionChangeListenerD1Ev(
    QQuickItemViewTransitionChangeListener *self) {
  delete self;
}

//  void QQuickItemViewTransitionChangeListener::viewItemTransitionFinished(Q
//      QuickItemViewTransitionableItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN38QQuickItemViewTransitionChangeListener26viewItemTransitionFinishedEP32QQuickItemViewTransitionableItem(
    QQuickItemViewTransitionChangeListener *self,
    QQuickItemViewTransitionableItem *item) {
  self->viewItemTransitionFinished(item);
}

//  a Python function taken by a CuteQQuickItemViewTransitionChangeListener,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItemViewTransitionChangeListener(
    QQuickItemViewTransitionChangeListener *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickItemViewTransitionChangeListener *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_viewtransitions)
#endif  // QT_CONFIG(quick_viewtransitions)
