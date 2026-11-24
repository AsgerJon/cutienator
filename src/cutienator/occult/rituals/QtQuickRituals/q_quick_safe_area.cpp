//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicksafearea_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicksafearea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmargins.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qdebug.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickSafeArea that Python can take functions over in. Every QQuickSafeArea
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickSafeAreaCall0)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall1)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickSafeAreaCall2)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall3)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall4)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall5)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall6)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall7)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall8)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall9)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall10)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall11)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall12)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall13)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall14)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSafeAreaCall15)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickSafeAreaCall16)(const void *, QQuickItem *, int *);
typedef void * (*CuteQQuickSafeAreaCall17)(const void *, int *);
typedef bool (*CuteQQuickSafeAreaCall18)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuickSafeAreaCall19)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSafeAreaCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickSafeAreaCall21)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSafeAreaCall22)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSafeAreaCall23)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSafeAreaCall24)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSafeAreaCall25)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickSafeAreaCall26)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickSafeArea : public QQuickSafeArea {
public:
  using QQuickSafeArea::QQuickSafeArea;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener20itemTransformChangedEP10QQuickItemS1_")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13addSourceItemEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16removeSourceItemEP10QQuickItem")) {
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
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemChildRemovedEP10QQuickItemS1_")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener17itemParentChangedEP10QQuickItemS1_")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener19itemRotationChangedEP10QQuickItem")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener16itemScaleChangedEP10QQuickItem")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QQuickItemChangeListener13anchorPrivateEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener11baseDeletedEPK7QObject")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK24QQuickItemChangeListener9debugNameEv")) {
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

  //  void QQuickSafeArea::itemTransformChanged(QQuickItem *a0, QQuickItem
  //      *a1)
  void itemTransformChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSafeAreaCall0 call = reinterpret_cast<CuteQQuickSafeAreaCall0>(taken[0]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickSafeArea::itemTransformChanged(a0, a1);
  }

  //  void QQuickSafeArea::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSafeAreaCall1 call = reinterpret_cast<CuteQQuickSafeAreaCall1>(taken[1]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickSafeArea::itemGeometryChanged(a0, a1, a2);
  }

  //  void QQuickSafeArea::addSourceItem(QQuickItem *item)
  void addSourceItem(QQuickItem *item) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSafeAreaCall2 call = reinterpret_cast<CuteQQuickSafeAreaCall2>(taken[2]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickSafeArea::addSourceItem(item);
  }

  //  void QQuickSafeArea::removeSourceItem(QQuickItem *item)
  void removeSourceItem(QQuickItem *item) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSafeAreaCall3 call = reinterpret_cast<CuteQQuickSafeAreaCall3>(taken[3]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickSafeArea::removeSourceItem(item);
  }

  //  void QQuickItemChangeListener::itemSiblingOrderChanged(QQuickItem
  //      *a0)
  void itemSiblingOrderChanged(QQuickItem *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSafeAreaCall4 call = reinterpret_cast<CuteQQuickSafeAreaCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemSiblingOrderChanged(a0);
  }

  //  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
  void itemVisibilityChanged(QQuickItem *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSafeAreaCall5 call = reinterpret_cast<CuteQQuickSafeAreaCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemVisibilityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSafeAreaCall6 call = reinterpret_cast<CuteQQuickSafeAreaCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSafeAreaCall7 call = reinterpret_cast<CuteQQuickSafeAreaCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemOpacityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemDestroyed(QQuickItem *a0)
  void itemDestroyed(QQuickItem *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickSafeAreaCall8 call = reinterpret_cast<CuteQQuickSafeAreaCall8>(taken[8]);
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
      CuteQQuickSafeAreaCall9 call = reinterpret_cast<CuteQQuickSafeAreaCall9>(taken[9]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildAdded(a0, a1);
  }

  //  void QQuickItemChangeListener::itemChildRemoved(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemChildRemoved(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickSafeAreaCall10 call = reinterpret_cast<CuteQQuickSafeAreaCall10>(taken[10]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemChildRemoved(a0, a1);
  }

  //  void QQuickItemChangeListener::itemParentChanged(QQuickItem *a0,
  //      QQuickItem *a1)
  void itemParentChanged(QQuickItem *a0, QQuickItem *a1) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickSafeAreaCall11 call = reinterpret_cast<CuteQQuickSafeAreaCall11>(taken[11]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemParentChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickSafeAreaCall12 call = reinterpret_cast<CuteQQuickSafeAreaCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemRotationChanged(a0);
  }

  //  void QQuickItemChangeListener::itemImplicitWidthChanged(QQuickItem
  //      *a0)
  void itemImplicitWidthChanged(QQuickItem *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickSafeAreaCall13 call = reinterpret_cast<CuteQQuickSafeAreaCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemImplicitWidthChanged(a0);
  }

  //  void QQuickItemChangeListener::itemImplicitHeightChanged(QQuickItem
  //      *a0)
  void itemImplicitHeightChanged(QQuickItem *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickSafeAreaCall14 call = reinterpret_cast<CuteQQuickSafeAreaCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemImplicitHeightChanged(a0);
  }

  //  void QQuickItemChangeListener::itemFocusChanged(QQuickItem *a0,
  //      Qt::FocusReason a1)
  void itemFocusChanged(QQuickItem *a0, Qt::FocusReason a1) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickSafeAreaCall15 call = reinterpret_cast<CuteQQuickSafeAreaCall15>(taken[15]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickSafeAreaCall16 call = reinterpret_cast<CuteQQuickSafeAreaCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemScaleChanged(a0);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickSafeAreaCall17 call = reinterpret_cast<CuteQQuickSafeAreaCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnchorsPrivate *>(given);
    }
    return QQuickItemChangeListener::anchorPrivate();
  }

  //  bool QQuickItemChangeListener::baseDeleted(const QObject *caller)
  //      const
  bool baseDeleted(const QObject *caller) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickSafeAreaCall18 call = reinterpret_cast<CuteQQuickSafeAreaCall18>(taken[18]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickSafeAreaCall19 call = reinterpret_cast<CuteQQuickSafeAreaCall19>(taken[19]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QQuickItemChangeListener::debugName();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickSafeAreaCall20 call = reinterpret_cast<CuteQQuickSafeAreaCall20>(taken[20]);
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
      CuteQQuickSafeAreaCall21 call = reinterpret_cast<CuteQQuickSafeAreaCall21>(taken[21]);
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
      CuteQQuickSafeAreaCall22 call = reinterpret_cast<CuteQQuickSafeAreaCall22>(taken[22]);
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
      CuteQQuickSafeAreaCall23 call = reinterpret_cast<CuteQQuickSafeAreaCall23>(taken[23]);
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
      CuteQQuickSafeAreaCall24 call = reinterpret_cast<CuteQQuickSafeAreaCall24>(taken[24]);
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
      CuteQQuickSafeAreaCall25 call = reinterpret_cast<CuteQQuickSafeAreaCall25>(taken[25]);
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
      CuteQQuickSafeAreaCall26 call = reinterpret_cast<CuteQQuickSafeAreaCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickSafeArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickSafeArea10metaObjectEv(
    const QQuickSafeArea *self) {
  return self->metaObject();
}

//  QString QQuickSafeArea::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickSafeArea2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSafeArea::tr(s, c, n));
}

//  void QQuickSafeArea::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickSafeArea21qt_qmlMarker_attachedEv(
    QQuickSafeArea *self) {
  self->qt_qmlMarker_attached();
}

//  void QQuickSafeArea::qt_qmlMarker_uncreatable()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickSafeArea24qt_qmlMarker_uncreatableEv(
    QQuickSafeArea *self) {
  self->qt_qmlMarker_uncreatable();
}

//  QQuickSafeArea::QQuickSafeArea(QQuickItem *attachee)
extern "C" Q_DECL_EXPORT
QQuickSafeArea *ritual_ZN14QQuickSafeAreaC1EP10QQuickItem(
    QQuickItem *attachee) {
  return new CuteQQuickSafeArea(attachee);
}

//  QQuickSafeArea::~QQuickSafeArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickSafeAreaD1Ev(QQuickSafeArea *self) {
  delete self;
}

//  QQuickSafeArea *QQuickSafeArea::qmlAttachedProperties(QObject *attachee)
extern "C" Q_DECL_EXPORT
QQuickSafeArea *ritual_ZN14QQuickSafeArea21qmlAttachedPropertiesEP7QObject(
    QObject *attachee) {
  return QQuickSafeArea::qmlAttachedProperties(attachee);
}

//  QMarginsF QQuickSafeArea::margins() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK14QQuickSafeArea7marginsEv(const QQuickSafeArea *self) {
  return new QMarginsF(self->margins());
}

//  QMarginsF QQuickSafeArea::additionalMargins() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK14QQuickSafeArea17additionalMarginsEv(
    const QQuickSafeArea *self) {
  return new QMarginsF(self->additionalMargins());
}

//  void QQuickSafeArea::setAdditionalMargins(const QMarginsF
//      &additionalMargins)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickSafeArea20setAdditionalMarginsERK9QMarginsF(
    QQuickSafeArea *self,
    const QMarginsF *additionalMargins) {
  self->setAdditionalMargins(*additionalMargins);
}

//  void QQuickSafeArea::updateSafeAreasRecursively(QQuickItem *fromItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickSafeArea26updateSafeAreasRecursivelyEP10QQuickItem(
    QQuickItem *fromItem) {
  QQuickSafeArea::updateSafeAreasRecursively(fromItem);
}

//  void QQuickSafeArea::windowChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickSafeArea13windowChangedEv(QQuickSafeArea *self) {
  self->windowChanged();
}

//  void QQuickSafeArea::updateSafeArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickSafeArea14updateSafeAreaEv(QQuickSafeArea *self) {
  self->updateSafeArea();
}

//  void QQuickSafeArea::itemTransformChanged(QQuickItem *a0, QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickSafeArea20itemTransformChangedEP10QQuickItemS1_(
    QQuickSafeArea *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->itemTransformChanged(a0, a1);
}

//  void QQuickSafeArea::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickSafeArea19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickSafeArea *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->itemGeometryChanged(a0, *a1, *a2);
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QQuickSafeArea *safeArea)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugPK14QQuickSafeArea(
    const QDebug *debug,
    const QQuickSafeArea *safeArea) {
  return new QDebug(operator<<(*debug, safeArea));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  void QQuickSafeArea::addSourceItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickSafeArea13addSourceItemEP10QQuickItem(
    QQuickSafeArea *self,
    QQuickItem *item) {
  self->addSourceItem(item);
}

//  void QQuickSafeArea::removeSourceItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickSafeArea16removeSourceItemEP10QQuickItem(
    QQuickSafeArea *self,
    QQuickItem *item) {
  self->removeSourceItem(item);
}

//  QQuickSafeArea as the QQuickItemChangeListener it is built on
extern "C" Q_DECL_EXPORT
QQuickItemChangeListener *ritual_cast_QQuickSafeArea_QQuickItemChangeListener(
    QQuickSafeArea *self) {
  return static_cast<QQuickItemChangeListener *>(self);
}

//  a Python function taken by a CuteQQuickSafeArea, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSafeArea(
    QQuickSafeArea *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSafeArea *>(self)->take(key, call);
}

//  void QQuickSafeArea::itemTransformChanged(QQuickItem *a0, QQuickItem *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickSafeArea20itemTransformChangedEP10QQuickItemS1_(
    QQuickSafeArea *self,
    QQuickItem *a0,
    QQuickItem *a1) {
  self->QQuickSafeArea::itemTransformChanged(a0, a1);
}

//  void QQuickSafeArea::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickSafeArea19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickSafeArea *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->QQuickSafeArea::itemGeometryChanged(a0, *a1, *a2);
}

//  void QQuickSafeArea::addSourceItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickSafeArea13addSourceItemEP10QQuickItem(
    QQuickSafeArea *self,
    QQuickItem *item) {
  self->QQuickSafeArea::addSourceItem(item);
}

//  void QQuickSafeArea::removeSourceItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickSafeArea16removeSourceItemEP10QQuickItem(
    QQuickSafeArea *self,
    QQuickItem *item) {
  self->QQuickSafeArea::removeSourceItem(item);
}
