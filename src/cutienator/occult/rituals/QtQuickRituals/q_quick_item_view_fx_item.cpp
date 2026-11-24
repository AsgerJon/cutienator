//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitemviewfxitem_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_itemview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemviewfxitem_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QQuickItemViewFxItem that Python can take functions over in. Every QQuickItemViewFxItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewFxItemCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewFxItemCall1)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewFxItemCall2)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef qreal (*CuteQQuickItemViewFxItemCall3)(const void *, int *);
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
typedef bool (*CuteQQuickItemViewFxItemCall4)(const void *, qreal, qreal, int *);
#endif  // QT_CONFIG(quick_itemview)
class CuteQQuickItemViewFxItem : public QQuickItemViewFxItem {
public:
  using QQuickItemViewFxItem::QQuickItemViewFxItem;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK20QQuickItemViewFxItem8positionEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK20QQuickItemViewFxItem11endPositionEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK20QQuickItemViewFxItem4sizeEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK20QQuickItemViewFxItem11sectionSizeEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
#if QT_CONFIG(quick_itemview)
    if (!std::strcmp(key, "_ZNK20QQuickItemViewFxItem8containsEdd")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_itemview)
    return false;
  }

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewFxItem::position() const
  qreal position() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickItemViewFxItemCall0 call = reinterpret_cast<CuteQQuickItemViewFxItemCall0>(taken[0]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewFxItem::endPosition() const
  qreal endPosition() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickItemViewFxItemCall1 call = reinterpret_cast<CuteQQuickItemViewFxItemCall1>(taken[1]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewFxItem::size() const
  qreal size() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickItemViewFxItemCall2 call = reinterpret_cast<CuteQQuickItemViewFxItemCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  qreal QQuickItemViewFxItem::sectionSize() const
  qreal sectionSize() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickItemViewFxItemCall3 call = reinterpret_cast<CuteQQuickItemViewFxItemCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)

#if QT_CONFIG(quick_itemview)
  //  bool QQuickItemViewFxItem::contains(qreal x, qreal y) const
  bool contains(qreal x, qreal y) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickItemViewFxItemCall4 call = reinterpret_cast<CuteQQuickItemViewFxItemCall4>(taken[4]);
      bool given = call(this, x, y, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(quick_itemview)
};

//  QQuickItemViewFxItem::~QQuickItemViewFxItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickItemViewFxItemD1Ev(QQuickItemViewFxItem *self) {
  delete self;
}

//  qreal QQuickItemViewFxItem::itemX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickItemViewFxItem5itemXEv(
    const QQuickItemViewFxItem *self) {
  return self->itemX();
}

//  qreal QQuickItemViewFxItem::itemY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickItemViewFxItem5itemYEv(
    const QQuickItemViewFxItem *self) {
  return self->itemY();
}

//  qreal QQuickItemViewFxItem::itemWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickItemViewFxItem9itemWidthEv(
    const QQuickItemViewFxItem *self) {
  return self->itemWidth();
}

//  qreal QQuickItemViewFxItem::itemHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickItemViewFxItem10itemHeightEv(
    const QQuickItemViewFxItem *self) {
  return self->itemHeight();
}

//  void QQuickItemViewFxItem::moveTo(const QPointF &pos, bool immediate)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickItemViewFxItem6moveToERK7QPointFb(
    QQuickItemViewFxItem *self,
    const QPointF *pos,
    bool immediate) {
  self->moveTo(*pos, immediate);
}

//  void QQuickItemViewFxItem::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickItemViewFxItem10setVisibleEb(
    QQuickItemViewFxItem *self,
    bool visible) {
  self->setVisible(visible);
}

//  void QQuickItemViewFxItem::trackGeometry(bool track)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickItemViewFxItem13trackGeometryEb(
    QQuickItemViewFxItem *self,
    bool track) {
  self->trackGeometry(track);
}

//  QRectF QQuickItemViewFxItem::geometry() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK20QQuickItemViewFxItem8geometryEv(
    const QQuickItemViewFxItem *self) {
  return new QRectF(self->geometry());
}

//  void QQuickItemViewFxItem::setGeometry(const QRectF &geometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickItemViewFxItem11setGeometryERK6QRectF(
    QQuickItemViewFxItem *self,
    const QRectF *geometry) {
  self->setGeometry(*geometry);
}

#if QT_CONFIG(quick_viewtransitions)
//  QQuickItemViewTransitioner::TransitionType
//      QQuickItemViewFxItem::scheduledTransitionType() const
extern "C" Q_DECL_EXPORT
QQuickItemViewTransitioner::TransitionType ritual_ZNK20QQuickItemViewFxItem23scheduledTransitionTypeEv(
    const QQuickItemViewFxItem *self) {
  return self->scheduledTransitionType();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  bool QQuickItemViewFxItem::transitionScheduledOrRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickItemViewFxItem28transitionScheduledOrRunningEv(
    const QQuickItemViewFxItem *self) {
  return self->transitionScheduledOrRunning();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  bool QQuickItemViewFxItem::transitionRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickItemViewFxItem17transitionRunningEv(
    const QQuickItemViewFxItem *self) {
  return self->transitionRunning();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  bool QQuickItemViewFxItem::isPendingRemoval() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickItemViewFxItem16isPendingRemovalEv(
    const QQuickItemViewFxItem *self) {
  return self->isPendingRemoval();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void
//      QQuickItemViewFxItem::transitionNextReposition(QQuickItemViewTransiti
//      oner *transitioner, QQuickItemViewTransitioner::TransitionType type,
//      bool asTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickItemViewFxItem24transitionNextRepositionEP26QQuickItemViewTransitionerNS0_14TransitionTypeEb(
    QQuickItemViewFxItem *self,
    QQuickItemViewTransitioner *transitioner,
    QQuickItemViewTransitioner::TransitionType type,
    bool asTarget) {
  self->transitionNextReposition(transitioner, type, asTarget);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  bool QQuickItemViewFxItem::prepareTransition(QQuickItemViewTransitioner
//      *transitioner, const QRectF &viewBounds)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickItemViewFxItem17prepareTransitionEP26QQuickItemViewTransitionerRK6QRectF(
    QQuickItemViewFxItem *self,
    QQuickItemViewTransitioner *transitioner,
    const QRectF *viewBounds) {
  return self->prepareTransition(transitioner, *viewBounds);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickItemViewFxItem::startTransition(QQuickItemViewTransitioner
//      *transitioner)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickItemViewFxItem15startTransitionEP26QQuickItemViewTransitioner(
    QQuickItemViewFxItem *self,
    QQuickItemViewTransitioner *transitioner) {
  self->startTransition(transitioner);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  qreal QQuickItemViewFxItem::position() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickItemViewFxItem8positionEv(
    const QQuickItemViewFxItem *self) {
  return self->position();
}

//  qreal QQuickItemViewFxItem::endPosition() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickItemViewFxItem11endPositionEv(
    const QQuickItemViewFxItem *self) {
  return self->endPosition();
}

//  qreal QQuickItemViewFxItem::size() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickItemViewFxItem4sizeEv(
    const QQuickItemViewFxItem *self) {
  return self->size();
}

//  qreal QQuickItemViewFxItem::sectionSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickItemViewFxItem11sectionSizeEv(
    const QQuickItemViewFxItem *self) {
  return self->sectionSize();
}

//  bool QQuickItemViewFxItem::contains(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickItemViewFxItem8containsEdd(
    const QQuickItemViewFxItem *self,
    qreal x,
    qreal y) {
  return self->contains(x, y);
}

//  a Python function taken by a CuteQQuickItemViewFxItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItemViewFxItem(
    QQuickItemViewFxItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickItemViewFxItem *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_itemview)
