//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicksafearea_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicksafearea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickSafeAreaAttachable that Python can take functions over in. Every QQuickSafeAreaAttachable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickSafeAreaAttachableCall0)(const void *, int *);
class CuteQQuickSafeAreaAttachable : public QQuickSafeAreaAttachable {
public:
  using QQuickSafeAreaAttachable::QQuickSafeAreaAttachable;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QQuickSafeAreaAttachable22safeAreaAttachmentItemEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QQuickItem *QQuickSafeAreaAttachable::safeAreaAttachmentItem()
  QQuickItem *safeAreaAttachmentItem() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSafeAreaAttachableCall0 call = reinterpret_cast<CuteQQuickSafeAreaAttachableCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return {};
  }
};

//  QQuickSafeAreaAttachable::~QQuickSafeAreaAttachable()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSafeAreaAttachableD1Ev(
    QQuickSafeAreaAttachable *self) {
  delete self;
}

//  QQuickItem *QQuickSafeAreaAttachable::safeAreaAttachmentItem()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN24QQuickSafeAreaAttachable22safeAreaAttachmentItemEv(
    QQuickSafeAreaAttachable *self) {
  return self->safeAreaAttachmentItem();
}

//  a Python function taken by a CuteQQuickSafeAreaAttachable, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSafeAreaAttachable(
    QQuickSafeAreaAttachable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSafeAreaAttachable *>(self)->take(key, call);
}
