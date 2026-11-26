//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickpopuppositioner_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopuppositioner_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qstring.h>
#include <cstring>

//  Only a class built on QQuickPopupPositioner may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickPopupPositioner : QQuickPopupPositioner {
  using QQuickPopupPositioner::itemGeometryChanged;
  using QQuickPopupPositioner::itemParentChanged;
  using QQuickPopupPositioner::itemChildRemoved;
};

//  A QQuickPopupPositioner that Python can take functions over in. Every QQuickPopupPositioner
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPopupPositionerCall0)(const void *, int *);
typedef void (*CuteQQuickPopupPositionerCall1)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickPopupPositionerCall2)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall3)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall4)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall5)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall7)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall8)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall9)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall10)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall11)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall12)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall13)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickPopupPositionerCall14)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall15)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void * (*CuteQQuickPopupPositionerCall16)(const void *, int *);
typedef bool (*CuteQQuickPopupPositionerCall17)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuickPopupPositionerCall18)(const void *, int *);
typedef void (*CuteQQuickPopupPositionerCall19)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupPositionerCall20)(const void *, QQuickItem *, int *);
class CuteQQuickPopupPositioner : public QQuickPopupPositioner {
public:
  using QQuickPopupPositioner::QQuickPopupPositioner;
  CuteQQuickPopupPositioner(const QQuickPopupPositioner & other) : QQuickPopupPositioner(other) {}
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QQuickPopupPositioner10repositionEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickItemS1_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickItemS1_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickItem")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickItem")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickItem")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener14itemChildAddedEP10QQuickItemS1_")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickItem")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuickItemS1_")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13anchorPrivateEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener9debugNameEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickItem")) {
      taken[20] = call;
      return true;
    }
    return false;
  }

  //  void QQuickPopupPositioner::reposition()
  void reposition() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall0 call = reinterpret_cast<CuteQQuickPopupPositionerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickPopupPositioner::reposition();
  }

  //  void QQuickPopupPositioner::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall1 call = reinterpret_cast<CuteQQuickPopupPositionerCall1>(taken[1]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickPopupPositioner::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickPopupPositioner::itemParentChanged(QQuickItem *a0,
  //      QQuickItem *parent)
  void itemParentChanged(QQuickItem *a0, QQuickItem *parent) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall2 call = reinterpret_cast<CuteQQuickPopupPositionerCall2>(taken[2]);
      call(this, a0, parent, &handled);
      if (handled) return;
    }
    QQuickPopupPositioner::itemParentChanged(a0, parent);
  }

  //  void QQuickPopupPositioner::itemChildRemoved(QQuickItem *a0,
  //      QQuickItem *child)
  void itemChildRemoved(QQuickItem *a0, QQuickItem *child) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall3 call = reinterpret_cast<CuteQQuickPopupPositionerCall3>(taken[3]);
      call(this, a0, child, &handled);
      if (handled) return;
    }
    QQuickPopupPositioner::itemChildRemoved(a0, child);
  }

  //  void QQuickItemChangeListener::itemSiblingOrderChanged(QQuickItem
  //      *a0)
  void itemSiblingOrderChanged(QQuickItem *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall4 call = reinterpret_cast<CuteQQuickPopupPositionerCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemSiblingOrderChanged(a0);
  }

  //  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
  void itemVisibilityChanged(QQuickItem *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall5 call = reinterpret_cast<CuteQQuickPopupPositionerCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemVisibilityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall6 call = reinterpret_cast<CuteQQuickPopupPositionerCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall7 call = reinterpret_cast<CuteQQuickPopupPositionerCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemOpacityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemDestroyed(QQuickItem *a0)
  void itemDestroyed(QQuickItem *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall8 call = reinterpret_cast<CuteQQuickPopupPositionerCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemDestroyed(a0);
  }

  //  void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildAdded(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall9 call = reinterpret_cast<CuteQQuickPopupPositionerCall9>(taken[9]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildAdded(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall10 call = reinterpret_cast<CuteQQuickPopupPositionerCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemRotationChanged(a0);
  }

  //  void QQuickItemChangeListener::itemImplicitWidthChanged(QQuickItem
  //      *a0)
  void itemImplicitWidthChanged(QQuickItem *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall11 call = reinterpret_cast<CuteQQuickPopupPositionerCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemImplicitWidthChanged(a0);
  }

  //  void QQuickItemChangeListener::itemImplicitHeightChanged(QQuickItem
  //      *a0)
  void itemImplicitHeightChanged(QQuickItem *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall12 call = reinterpret_cast<CuteQQuickPopupPositionerCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemImplicitHeightChanged(a0);
  }

  //  void QQuickItemChangeListener::itemFocusChanged(QQuickItem *a0,
  //      Qt::FocusReason a1)
  void itemFocusChanged(QQuickItem *a0, Qt::FocusReason a1) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall13 call = reinterpret_cast<CuteQQuickPopupPositionerCall13>(taken[13]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall14 call = reinterpret_cast<CuteQQuickPopupPositionerCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemScaleChanged(a0);
  }

  //  void QQuickItemChangeListener::itemTransformChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemTransformChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall15 call = reinterpret_cast<CuteQQuickPopupPositionerCall15>(taken[15]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemTransformChanged(a0, a1);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall16 call = reinterpret_cast<CuteQQuickPopupPositionerCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnchorsPrivate *>(given);
    }
    return QQuickItemChangeListener::anchorPrivate();
  }

  //  bool QQuickItemChangeListener::baseDeleted(const QObject *caller)
  //      const
  bool baseDeleted(const QObject *caller) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall17 call = reinterpret_cast<CuteQQuickPopupPositionerCall17>(taken[17]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall18 call = reinterpret_cast<CuteQQuickPopupPositionerCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall19 call = reinterpret_cast<CuteQQuickPopupPositionerCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::addSourceItem(a0);
  }

  //  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
  void removeSourceItem(QQuickItem *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPopupPositionerCall20 call = reinterpret_cast<CuteQQuickPopupPositionerCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::removeSourceItem(a0);
  }
};

//  QQuickPopupPositioner::QQuickPopupPositioner(QQuickPopup *popup)
extern "C" Q_DECL_EXPORT
QQuickPopupPositioner *ritual_ZN21QQuickPopupPositionerC1EP11QQuickPopup(
    QQuickPopup *popup) {
  return new CuteQQuickPopupPositioner(popup);
}

//  QQuickPopupPositioner::~QQuickPopupPositioner()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPopupPositionerD1Ev(QQuickPopupPositioner *self) {
  delete self;
}

//  QQuickPopup *QQuickPopupPositioner::popup() const
extern "C" Q_DECL_EXPORT
QQuickPopup *ritual_ZNK21QQuickPopupPositioner5popupEv(
    const QQuickPopupPositioner *self) {
  return self->popup();
}

//  QQuickItem *QQuickPopupPositioner::parentItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK21QQuickPopupPositioner10parentItemEv(
    const QQuickPopupPositioner *self) {
  return self->parentItem();
}

//  void QQuickPopupPositioner::setParentItem(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPopupPositioner13setParentItemEP10QQuickItem(
    QQuickPopupPositioner *self,
    QQuickItem *parent) {
  self->setParentItem(parent);
}

//  void QQuickPopupPositioner::reposition()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPopupPositioner10repositionEv(
    QQuickPopupPositioner *self) {
  self->reposition();
}

//  void QQuickPopupPositioner::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPopupPositioner19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickPopupPositioner *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->itemGeometryChanged(a0, *a1, *a2);
}

//  void QQuickPopupPositioner::itemParentChanged(QQuickItem *a0, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPopupPositioner17itemParentChangedEP10QQuickItemS1_(
    QQuickPopupPositioner *self,
    QQuickItem *a0,
    QQuickItem *parent) {
  self->itemParentChanged(a0, parent);
}

//  void QQuickPopupPositioner::itemChildRemoved(QQuickItem *a0, QQuickItem
//      *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPopupPositioner16itemChildRemovedEP10QQuickItemS1_(
    QQuickPopupPositioner *self,
    QQuickItem *a0,
    QQuickItem *child) {
  self->itemChildRemoved(a0, child);
}

//  void QQuickPopupPositioner::removeAncestorListeners(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPopupPositioner23removeAncestorListenersEP10QQuickItem(
    QQuickPopupPositioner *self,
    QQuickItem *item) {
  self->removeAncestorListeners(item);
}

//  void QQuickPopupPositioner::addAncestorListeners(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPopupPositioner20addAncestorListenersEP10QQuickItem(
    QQuickPopupPositioner *self,
    QQuickItem *item) {
  self->addAncestorListeners(item);
}

//  void QQuickPopupPositioner::repositionPopupWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPopupPositioner21repositionPopupWindowEv(
    QQuickPopupPositioner *self) {
  self->repositionPopupWindow();
}

//  a Python function taken by a CuteQQuickPopupPositioner, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPopupPositioner(
    QQuickPopupPositioner *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPopupPositioner *>(self)->take(key, call);
}

//  void QQuickPopupPositioner::reposition()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickPopupPositioner10repositionEv(
    QQuickPopupPositioner *self) {
  self->QQuickPopupPositioner::reposition();
}

//  void QQuickPopupPositioner::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickPopupPositioner19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickPopupPositioner *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  static_cast<OwnQQuickPopupPositioner *>(self)->OwnQQuickPopupPositioner::itemGeometryChanged(
      a0,
      *a1,
      *a2);
}

//  void QQuickPopupPositioner::itemParentChanged(QQuickItem *a0, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickPopupPositioner17itemParentChangedEP10QQuickItemS1_(
    QQuickPopupPositioner *self,
    QQuickItem *a0,
    QQuickItem *parent) {
  static_cast<OwnQQuickPopupPositioner *>(self)->OwnQQuickPopupPositioner::itemParentChanged(
      a0,
      parent);
}

//  void QQuickPopupPositioner::itemChildRemoved(QQuickItem *a0, QQuickItem
//      *child)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickPopupPositioner16itemChildRemovedEP10QQuickItemS1_(
    QQuickPopupPositioner *self,
    QQuickItem *a0,
    QQuickItem *child) {
  static_cast<OwnQQuickPopupPositioner *>(self)->OwnQQuickPopupPositioner::itemChildRemoved(
      a0,
      child);
}
