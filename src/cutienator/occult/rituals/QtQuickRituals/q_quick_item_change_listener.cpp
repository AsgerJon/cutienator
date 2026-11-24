//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QQuickItemChangeListener that Python can take functions over in. Every QQuickItemChangeListener
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickItemChangeListenerCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickItemChangeListenerCall1)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall2)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall3)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall4)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall5)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall6)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall7)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall8)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall9)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall10)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall11)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall12)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickItemChangeListenerCall13)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall14)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void * (*CuteQQuickItemChangeListenerCall15)(const void *, int *);
typedef bool (*CuteQQuickItemChangeListenerCall16)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuickItemChangeListenerCall17)(const void *, int *);
typedef void (*CuteQQuickItemChangeListenerCall18)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickItemChangeListenerCall19)(const void *, QQuickItem *, int *);
class CuteQQuickItemChangeListener : public QQuickItemChangeListener {
public:
  using QQuickItemChangeListener::QQuickItemChangeListener;
  CuteQQuickItemChangeListener(const QQuickItemChangeListener &other) : QQuickItemChangeListener(other) {}
  void *taken[20] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuickItemS1_")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickItemS1_")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickItemS1_")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuickItem")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickItem")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuickItemS1_")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13anchorPrivateEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener9debugNameEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickItem")) {
      taken[19] = call;
      return true;
    }
    return false;
  }

  //  void QQuickItemChangeListener::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall0 call = reinterpret_cast<CuteQQuickItemChangeListenerCall0>(taken[0]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickItemChangeListener::itemSiblingOrderChanged(QQuickItem
  //      *a0)
  void itemSiblingOrderChanged(QQuickItem *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall1 call = reinterpret_cast<CuteQQuickItemChangeListenerCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemSiblingOrderChanged(a0);
  }

  //  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
  void itemVisibilityChanged(QQuickItem *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall2 call = reinterpret_cast<CuteQQuickItemChangeListenerCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemVisibilityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall3 call = reinterpret_cast<CuteQQuickItemChangeListenerCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall4 call = reinterpret_cast<CuteQQuickItemChangeListenerCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemOpacityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemDestroyed(QQuickItem *a0)
  void itemDestroyed(QQuickItem *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall5 call = reinterpret_cast<CuteQQuickItemChangeListenerCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemDestroyed(a0);
  }

  //  void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildAdded(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall6 call = reinterpret_cast<CuteQQuickItemChangeListenerCall6>(taken[6]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildAdded(a0, a1);
  }

  //  void QQuickItemChangeListener::itemChildRemoved(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildRemoved(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall7 call = reinterpret_cast<CuteQQuickItemChangeListenerCall7>(taken[7]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildRemoved(a0, a1);
  }

  //  void QQuickItemChangeListener::itemParentChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemParentChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall8 call = reinterpret_cast<CuteQQuickItemChangeListenerCall8>(taken[8]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemParentChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall9 call = reinterpret_cast<CuteQQuickItemChangeListenerCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemRotationChanged(a0);
  }

  //  void QQuickItemChangeListener::itemImplicitWidthChanged(QQuickItem
  //      *a0)
  void itemImplicitWidthChanged(QQuickItem *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall10 call = reinterpret_cast<CuteQQuickItemChangeListenerCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemImplicitWidthChanged(a0);
  }

  //  void QQuickItemChangeListener::itemImplicitHeightChanged(QQuickItem
  //      *a0)
  void itemImplicitHeightChanged(QQuickItem *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall11 call = reinterpret_cast<CuteQQuickItemChangeListenerCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemImplicitHeightChanged(a0);
  }

  //  void QQuickItemChangeListener::itemFocusChanged(QQuickItem *a0,
  //      Qt::FocusReason a1)
  void itemFocusChanged(QQuickItem *a0, Qt::FocusReason a1) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall12 call = reinterpret_cast<CuteQQuickItemChangeListenerCall12>(taken[12]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall13 call = reinterpret_cast<CuteQQuickItemChangeListenerCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemScaleChanged(a0);
  }

  //  void QQuickItemChangeListener::itemTransformChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemTransformChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall14 call = reinterpret_cast<CuteQQuickItemChangeListenerCall14>(taken[14]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemTransformChanged(a0, a1);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall15 call = reinterpret_cast<CuteQQuickItemChangeListenerCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnchorsPrivate *>(given);
    }
    return QQuickItemChangeListener::anchorPrivate();
  }

  //  bool QQuickItemChangeListener::baseDeleted(const QObject *caller)
  //      const
  bool baseDeleted(const QObject *caller) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall16 call = reinterpret_cast<CuteQQuickItemChangeListenerCall16>(taken[16]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall17 call = reinterpret_cast<CuteQQuickItemChangeListenerCall17>(taken[17]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickItemChangeListener::debugName();
  }

  //  void QQuickItemChangeListener::addSourceItem(QQuickItem *a0)
  void addSourceItem(QQuickItem *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall18 call = reinterpret_cast<CuteQQuickItemChangeListenerCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::addSourceItem(a0);
  }

  //  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
  void removeSourceItem(QQuickItem *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickItemChangeListenerCall19 call = reinterpret_cast<CuteQQuickItemChangeListenerCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::removeSourceItem(a0);
  }
};

//  QQuickItemChangeListener::~QQuickItemChangeListener()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListenerD1Ev(
    QQuickItemChangeListener *self) {
  delete self;
}

//  void QQuickItemChangeListener::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickItemChangeListener *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->itemGeometryChanged(a0, *a1, *a2);
}

//  void QQuickItemChangeListener::itemSiblingOrderChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->itemSiblingOrderChanged(a0);
}

//  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->itemVisibilityChanged(a0);
}

//  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->itemEnabledChanged(a0);
}

//  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->itemOpacityChanged(a0);
}

//  void QQuickItemChangeListener::itemDestroyed(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->itemDestroyed(a0);
}

//  void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0, QQuickItem
//      *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuickItemS1_(
    QQuickItemChangeListener *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->itemChildAdded(a0, a1);
}

//  void QQuickItemChangeListener::itemChildRemoved(QQuickItem *a0,
//      QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickItemS1_(
    QQuickItemChangeListener *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->itemChildRemoved(a0, a1);
}

//  void QQuickItemChangeListener::itemParentChanged(QQuickItem *a0,
//      QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickItemS1_(
    QQuickItemChangeListener *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->itemParentChanged(a0, a1);
}

//  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->itemRotationChanged(a0);
}

//  void QQuickItemChangeListener::itemImplicitWidthChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->itemImplicitWidthChanged(a0);
}

//  void QQuickItemChangeListener::itemImplicitHeightChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->itemImplicitHeightChanged(a0);
}

//  void QQuickItemChangeListener::itemFocusChanged(QQuickItem *a0,
//      Qt::FocusReason a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE(
    QQuickItemChangeListener *self,
    QQuickItem *a0,
    Qt::FocusReason a1) {
  self->itemFocusChanged(a0, a1);
}

//  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->itemScaleChanged(a0);
}

//  void QQuickItemChangeListener::itemTransformChanged(QQuickItem *a0,
//      QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuickItemS1_(
    QQuickItemChangeListener *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->itemTransformChanged(a0, a1);
}

//  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
extern "C" Q_DECL_EXPORT
QQuickAnchorsPrivate *ritual_ZN24QQuickItemChangeListener13anchorPrivateEv(
    QQuickItemChangeListener *self) {
  return self->anchorPrivate();
}

//  bool QQuickItemChangeListener::baseDeleted(const QObject *caller) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject(
    const QQuickItemChangeListener *self,
    const QObject *caller) {
  return self->baseDeleted(caller);
}

//  QString QQuickItemChangeListener::debugName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QQuickItemChangeListener9debugNameEv(
    const QQuickItemChangeListener *self) {
  return new QString(self->debugName());
}

//  void QQuickItemChangeListener::addSourceItem(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->addSourceItem(a0);
}

//  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->removeSourceItem(a0);
}

//  a Python function taken by a CuteQQuickItemChangeListener, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItemChangeListener(
    QQuickItemChangeListener *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickItemChangeListener *>(self)->take(key, call);
}

//  void QQuickItemChangeListener::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickItemChangeListener *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->QQuickItemChangeListener::itemGeometryChanged(a0, *a1, *a2);
}

//  void QQuickItemChangeListener::itemSiblingOrderChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->QQuickItemChangeListener::itemSiblingOrderChanged(a0);
}

//  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->QQuickItemChangeListener::itemVisibilityChanged(a0);
}

//  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->QQuickItemChangeListener::itemEnabledChanged(a0);
}

//  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->QQuickItemChangeListener::itemOpacityChanged(a0);
}

//  void QQuickItemChangeListener::itemDestroyed(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->QQuickItemChangeListener::itemDestroyed(a0);
}

//  void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0, QQuickItem
//      *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuickItemS1_(
    QQuickItemChangeListener *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->QQuickItemChangeListener::itemChildAdded(a0, a1);
}

//  void QQuickItemChangeListener::itemChildRemoved(QQuickItem *a0,
//      QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickItemS1_(
    QQuickItemChangeListener *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->QQuickItemChangeListener::itemChildRemoved(a0, a1);
}

//  void QQuickItemChangeListener::itemParentChanged(QQuickItem *a0,
//      QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickItemS1_(
    QQuickItemChangeListener *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->QQuickItemChangeListener::itemParentChanged(a0, a1);
}

//  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->QQuickItemChangeListener::itemRotationChanged(a0);
}

//  void QQuickItemChangeListener::itemImplicitWidthChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->QQuickItemChangeListener::itemImplicitWidthChanged(a0);
}

//  void QQuickItemChangeListener::itemImplicitHeightChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->QQuickItemChangeListener::itemImplicitHeightChanged(a0);
}

//  void QQuickItemChangeListener::itemFocusChanged(QQuickItem *a0,
//      Qt::FocusReason a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE(
    QQuickItemChangeListener *self,
    QQuickItem *a0,
    Qt::FocusReason a1) {
  self->QQuickItemChangeListener::itemFocusChanged(a0, a1);
}

//  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->QQuickItemChangeListener::itemScaleChanged(a0);
}

//  void QQuickItemChangeListener::itemTransformChanged(QQuickItem *a0,
//      QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuickItemS1_(
    QQuickItemChangeListener *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->QQuickItemChangeListener::itemTransformChanged(a0, a1);
}

//  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
extern "C" Q_DECL_EXPORT
QQuickAnchorsPrivate *ritual_own_ZN24QQuickItemChangeListener13anchorPrivateEv(
    QQuickItemChangeListener *self) {
  return self->QQuickItemChangeListener::anchorPrivate();
}

//  bool QQuickItemChangeListener::baseDeleted(const QObject *caller) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject(
    const QQuickItemChangeListener *self,
    const QObject *caller) {
  return self->QQuickItemChangeListener::baseDeleted(caller);
}

//  QString QQuickItemChangeListener::debugName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK24QQuickItemChangeListener9debugNameEv(
    const QQuickItemChangeListener *self) {
  return new QString(self->QQuickItemChangeListener::debugName());
}

//  void QQuickItemChangeListener::addSourceItem(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->QQuickItemChangeListener::addSourceItem(a0);
}

//  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickItem(
    QQuickItemChangeListener *self,
    QQuickItem *a0) {
  self->QQuickItemChangeListener::removeSourceItem(a0);
}
