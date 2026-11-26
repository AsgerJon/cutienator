//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickpopupanchors_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopupanchors_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickPopupAnchors that Python can take functions over in. Every QQuickPopupAnchors
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPopupAnchorsCall0)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall1)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickPopupAnchorsCall2)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall3)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall4)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall5)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall6)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall7)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall8)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall9)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall10)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall11)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall12)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickPopupAnchorsCall13)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall14)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void * (*CuteQQuickPopupAnchorsCall15)(const void *, int *);
typedef bool (*CuteQQuickPopupAnchorsCall16)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuickPopupAnchorsCall17)(const void *, int *);
typedef void (*CuteQQuickPopupAnchorsCall18)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickPopupAnchorsCall19)(const void *, QQuickItem *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPopupAnchorsCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPopupAnchorsCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPopupAnchorsCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPopupAnchorsCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPopupAnchorsCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPopupAnchorsCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPopupAnchorsCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPopupAnchors : public QQuickPopupAnchors {
public:
  using QQuickPopupAnchors::QQuickPopupAnchors;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13itemDestroyedEP10QQuickItem")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener21itemVisibilityChangedEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemEnabledChangedEP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener18itemOpacityChangedEP10QQuickItem")) {
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
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickPopupAnchors::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall0 call = reinterpret_cast<CuteQQuickPopupAnchorsCall0>(taken[0]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPopupAnchors::itemDestroyed(item);
  }

  //  void QQuickItemChangeListener::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall1 call = reinterpret_cast<CuteQQuickPopupAnchorsCall1>(taken[1]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickItemChangeListener::itemSiblingOrderChanged(QQuickItem
  //      *a0)
  void itemSiblingOrderChanged(QQuickItem *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall2 call = reinterpret_cast<CuteQQuickPopupAnchorsCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemSiblingOrderChanged(a0);
  }

  //  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
  void itemVisibilityChanged(QQuickItem *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall3 call = reinterpret_cast<CuteQQuickPopupAnchorsCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemVisibilityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall4 call = reinterpret_cast<CuteQQuickPopupAnchorsCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall5 call = reinterpret_cast<CuteQQuickPopupAnchorsCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemOpacityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemChildAdded(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildAdded(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall6 call = reinterpret_cast<CuteQQuickPopupAnchorsCall6>(taken[6]);
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
      CuteQQuickPopupAnchorsCall7 call = reinterpret_cast<CuteQQuickPopupAnchorsCall7>(taken[7]);
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
      CuteQQuickPopupAnchorsCall8 call = reinterpret_cast<CuteQQuickPopupAnchorsCall8>(taken[8]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemParentChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall9 call = reinterpret_cast<CuteQQuickPopupAnchorsCall9>(taken[9]);
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
      CuteQQuickPopupAnchorsCall10 call = reinterpret_cast<CuteQQuickPopupAnchorsCall10>(taken[10]);
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
      CuteQQuickPopupAnchorsCall11 call = reinterpret_cast<CuteQQuickPopupAnchorsCall11>(taken[11]);
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
      CuteQQuickPopupAnchorsCall12 call = reinterpret_cast<CuteQQuickPopupAnchorsCall12>(taken[12]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall13 call = reinterpret_cast<CuteQQuickPopupAnchorsCall13>(taken[13]);
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
      CuteQQuickPopupAnchorsCall14 call = reinterpret_cast<CuteQQuickPopupAnchorsCall14>(taken[14]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemTransformChanged(a0, a1);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall15 call = reinterpret_cast<CuteQQuickPopupAnchorsCall15>(taken[15]);
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
      CuteQQuickPopupAnchorsCall16 call = reinterpret_cast<CuteQQuickPopupAnchorsCall16>(taken[16]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall17 call = reinterpret_cast<CuteQQuickPopupAnchorsCall17>(taken[17]);
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
      CuteQQuickPopupAnchorsCall18 call = reinterpret_cast<CuteQQuickPopupAnchorsCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::addSourceItem(a0);
  }

  //  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
  void removeSourceItem(QQuickItem *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall19 call = reinterpret_cast<CuteQQuickPopupAnchorsCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::removeSourceItem(a0);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall20 call = reinterpret_cast<CuteQQuickPopupAnchorsCall20>(taken[20]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall21 call = reinterpret_cast<CuteQQuickPopupAnchorsCall21>(taken[21]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall22 call = reinterpret_cast<CuteQQuickPopupAnchorsCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall23 call = reinterpret_cast<CuteQQuickPopupAnchorsCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall24 call = reinterpret_cast<CuteQQuickPopupAnchorsCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall25 call = reinterpret_cast<CuteQQuickPopupAnchorsCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickPopupAnchorsCall26 call = reinterpret_cast<CuteQQuickPopupAnchorsCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPopupAnchors::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQuickPopupAnchors10metaObjectEv(
    const QQuickPopupAnchors *self) {
  return self->metaObject();
}

//  void *QQuickPopupAnchors::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQuickPopupAnchors11qt_metacastEPKc(
    QQuickPopupAnchors *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPopupAnchors::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQuickPopupAnchors11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPopupAnchors *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickPopupAnchors::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQuickPopupAnchors2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickPopupAnchors::tr(s, c, n));
}

//  void QQuickPopupAnchors::qt_qmlMarker_anonymous()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupAnchors22qt_qmlMarker_anonymousEv(
    QQuickPopupAnchors *self) {
  self->qt_qmlMarker_anonymous();
}

//  QQuickPopupAnchors::QQuickPopupAnchors(QQuickPopup *popup)
extern "C" Q_DECL_EXPORT
QQuickPopupAnchors *ritual_ZN18QQuickPopupAnchorsC1EP11QQuickPopup(
    QQuickPopup *popup) {
  return new CuteQQuickPopupAnchors(popup);
}

//  QQuickPopupAnchors::~QQuickPopupAnchors()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupAnchorsD1Ev(QQuickPopupAnchors *self) {
  delete self;
}

//  QQuickItem *QQuickPopupAnchors::centerIn() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK18QQuickPopupAnchors8centerInEv(
    const QQuickPopupAnchors *self) {
  return self->centerIn();
}

//  void QQuickPopupAnchors::setCenterIn(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupAnchors11setCenterInEP10QQuickItem(
    QQuickPopupAnchors *self,
    QQuickItem *item) {
  self->setCenterIn(item);
}

//  void QQuickPopupAnchors::resetCenterIn()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupAnchors13resetCenterInEv(
    QQuickPopupAnchors *self) {
  self->resetCenterIn();
}

//  void QQuickPopupAnchors::centerInChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupAnchors15centerInChangedEv(
    QQuickPopupAnchors *self) {
  self->centerInChanged();
}

//  void QQuickPopupAnchors::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickPopupAnchors13itemDestroyedEP10QQuickItem(
    QQuickPopupAnchors *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  QQuickPopupAnchorsPrivate *QQuickPopupAnchors::d_func()
extern "C" Q_DECL_EXPORT
QQuickPopupAnchorsPrivate *ritual_ZN18QQuickPopupAnchors6d_funcEv(
    QQuickPopupAnchors *self) {
  return self->d_func();
}

//  const QQuickPopupAnchorsPrivate *QQuickPopupAnchors::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickPopupAnchorsPrivate *ritual_ZNK18QQuickPopupAnchors6d_funcEv(
    const QQuickPopupAnchors *self) {
  return self->d_func();
}

//  QQuickPopupAnchors as the QQuickItemChangeListener it is built on
extern "C" Q_DECL_EXPORT
QQuickItemChangeListener *ritual_cast_QQuickPopupAnchors_QQuickItemChangeListener(
    QQuickPopupAnchors *self) {
  return static_cast<QQuickItemChangeListener *>(self);
}

//  a Python function taken by a CuteQQuickPopupAnchors, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPopupAnchors(
    QQuickPopupAnchors *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPopupAnchors *>(self)->take(key, call);
}

//  void QQuickPopupAnchors::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickPopupAnchors13itemDestroyedEP10QQuickItem(
    QQuickPopupAnchors *self,
    QQuickItem *item) {
  self->QQuickPopupAnchors::itemDestroyed(item);
}
