//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollbar_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickscrollbar_p.h>
#include <QtQuickTemplates2/private/qquickscrollbar_p_p.h>
#include <QtQuickTemplates2/private/qquickscrollview_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQuick/private/qquickflickable_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/private/qquickaccessibleattached_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 204, as _ZN22QQuickScrollBarPrivate12updateActiveEv
inline void QQuickScrollBarPrivate::updateActive()
{
    Q_Q(QQuickScrollBar);
#if QT_CONFIG(quicktemplates2_hover)
    bool hover = hovered;
#else
    bool hover = false;
#endif
    q->setActive(moving || (interactive && (pressed || hover)));
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 944, as _ZN30QQuickScrollBarAttachedPrivate12setFlickableEP15QQuickFlickable
inline void QQuickScrollBarAttachedPrivate::setFlickable(QQuickFlickable *item)
{
    if (flickable) {
        // NOTE: Use removeItemChangeListener(Geometry) instead of updateOrRemoveGeometryChangeListener(Size).
        // The latter doesn't remove the listener but only resets its types. Thus, it leaves behind a dangling
        // pointer on destruction.
        QQuickItemPrivate::get(flickable)->removeItemChangeListener(this, QQuickItemPrivate::Geometry);
        QQuickItemPrivate::get(flickable)->removeItemChangeListener(this, QQuickItemPrivate::Destroyed);
        if (horizontal)
            cleanupHorizontal();
        if (vertical)
            cleanupVertical();
    }

    flickable = item;

    if (item) {
        // Don't know how to combine these calls into one, and as long as they're separate calls,
        // the remove* calls above need to be separate too, otherwise they will have no effect.
        QQuickItemPrivate::get(item)->updateOrAddGeometryChangeListener(this, QQuickGeometryChange::Size);
        QQuickItemPrivate::get(item)->updateOrAddItemChangeListener(this, QQuickItemPrivate::Destroyed);
        if (horizontal)
            initHorizontal();
        if (vertical)
            initVertical();
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 972, as _ZN30QQuickScrollBarAttachedPrivate14initHorizontalEv
inline void QQuickScrollBarAttachedPrivate::initHorizontal()
{
    Q_ASSERT(flickable && horizontal);

    connect(flickable, &QQuickFlickable::movingHorizontallyChanged, this, &QQuickScrollBarAttachedPrivate::activateHorizontal);

    // TODO: export QQuickFlickableVisibleArea
    QObject *area = flickable->property("visibleArea").value<QObject *>();
    QObject::connect(area, SIGNAL(widthRatioChanged(qreal)), horizontal, SLOT(setSize(qreal)));
    QObject::connect(area, SIGNAL(xPositionChanged(qreal)), horizontal, SLOT(setPosition(qreal)));

    // ensure that the ScrollBar is stacked above the Flickable in a ScrollView
    QQuickItem *parent = horizontal->parentItem();
    if (parent && parent == flickable->parentItem())
        horizontal->stackAfter(flickable);

    // If a scroll bar was previously hidden (due to e.g. setting a new contentItem
    // on a ScrollView), we need to make sure that we un-hide it.
    if (auto control = qobject_cast<QQuickControl*>(q_func()->parent())) {
        const auto visibility = horizontal->policy() != QQuickScrollBar::AlwaysOff
            ? QQuickControlPrivate::UnhideVisibility::Show : QQuickControlPrivate::UnhideVisibility::Hide;
        QQuickControlPrivate::unhideOldItem(control, horizontal, visibility);
    }

    layoutHorizontal();
    horizontal->setSize(area->property("widthRatio").toReal());
    horizontal->setPosition(area->property("xPosition").toReal());
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 1001, as _ZN30QQuickScrollBarAttachedPrivate12initVerticalEv
inline void QQuickScrollBarAttachedPrivate::initVertical()
{
    Q_ASSERT(flickable && vertical);

    connect(flickable, &QQuickFlickable::movingVerticallyChanged, this, &QQuickScrollBarAttachedPrivate::activateVertical);

    // TODO: export QQuickFlickableVisibleArea
    QObject *area = flickable->property("visibleArea").value<QObject *>();
    QObject::connect(area, SIGNAL(heightRatioChanged(qreal)), vertical, SLOT(setSize(qreal)));
    QObject::connect(area, SIGNAL(yPositionChanged(qreal)), vertical, SLOT(setPosition(qreal)));

    // ensure that the ScrollBar is stacked above the Flickable in a ScrollView
    QQuickItem *parent = vertical->parentItem();
    if (parent && parent == flickable->parentItem())
        vertical->stackAfter(flickable);

    if (auto control = qobject_cast<QQuickControl*>(q_func()->parent())) {
        const auto visibility = vertical->policy() != QQuickScrollBar::AlwaysOff
            ? QQuickControlPrivate::UnhideVisibility::Show : QQuickControlPrivate::UnhideVisibility::Hide;
        QQuickControlPrivate::unhideOldItem(control, vertical, visibility);
    }

    layoutVertical();
    vertical->setSize(area->property("heightRatio").toReal());
    vertical->setPosition(area->property("yPosition").toReal());
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 1028, as _ZN30QQuickScrollBarAttachedPrivate17cleanupHorizontalEv
inline void QQuickScrollBarAttachedPrivate::cleanupHorizontal()
{
    Q_ASSERT(horizontal);

    QQuickControlPrivate::hideOldItem(horizontal);
    // ScrollBar.qml has a binding to visible and ScrollView.qml has a binding to parent.
    // If we just set visible to false and parent to null, these bindings will overwrite
    // them upon component completion as part of the binding evaluation.
    // That's why we remove the binding completely.
    const QQmlProperty visibleProperty(horizontal, QStringLiteral("visible"));
    const QQmlProperty parentProperty(horizontal, QStringLiteral("parent"));
    QQmlPropertyPrivate::removeBinding(visibleProperty);
    QQmlPropertyPrivate::removeBinding(parentProperty);

    if (!flickable)
        return;

    disconnect(flickable, &QQuickFlickable::movingHorizontallyChanged, this, &QQuickScrollBarAttachedPrivate::activateHorizontal);

    // TODO: export QQuickFlickableVisibleArea
    QObject *area = flickable->property("visibleArea").value<QObject *>();
    QObject::disconnect(area, SIGNAL(widthRatioChanged(qreal)), horizontal, SLOT(setSize(qreal)));
    QObject::disconnect(area, SIGNAL(xPositionChanged(qreal)), horizontal, SLOT(setPosition(qreal)));
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 1053, as _ZN30QQuickScrollBarAttachedPrivate15cleanupVerticalEv
inline void QQuickScrollBarAttachedPrivate::cleanupVertical()
{
    Q_ASSERT(vertical);

    QQuickControlPrivate::hideOldItem(vertical);
    const QQmlProperty visibleProperty(vertical, QStringLiteral("visible"));
    const QQmlProperty parentProperty(vertical, QStringLiteral("parent"));
    QQmlPropertyPrivate::removeBinding(visibleProperty);
    QQmlPropertyPrivate::removeBinding(parentProperty);

    if (!flickable)
        return;

    disconnect(flickable, &QQuickFlickable::movingVerticallyChanged, this, &QQuickScrollBarAttachedPrivate::activateVertical);

    // TODO: export QQuickFlickableVisibleArea
    QObject *area = flickable->property("visibleArea").value<QObject *>();
    QObject::disconnect(area, SIGNAL(heightRatioChanged(qreal)), vertical, SLOT(setSize(qreal)));
    QObject::disconnect(area, SIGNAL(yPositionChanged(qreal)), vertical, SLOT(setPosition(qreal)));
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 1074, as _ZN30QQuickScrollBarAttachedPrivate18activateHorizontalEv
inline void QQuickScrollBarAttachedPrivate::activateHorizontal()
{
    QQuickScrollBarPrivate *p = QQuickScrollBarPrivate::get(horizontal);
    p->moving = flickable->isMovingHorizontally();
    p->updateActive();
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 1081, as _ZN30QQuickScrollBarAttachedPrivate16activateVerticalEv
inline void QQuickScrollBarAttachedPrivate::activateVertical()
{
    QQuickScrollBarPrivate *p = QQuickScrollBarPrivate::get(vertical);
    p->moving = flickable->isMovingVertically();
    p->updateActive();
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 1124, as _ZN30QQuickScrollBarAttachedPrivate14mirrorVerticalEv
inline void QQuickScrollBarAttachedPrivate::mirrorVertical()
{
    layoutVertical(true);
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 1129, as _ZN30QQuickScrollBarAttachedPrivate16layoutHorizontalEb
inline void QQuickScrollBarAttachedPrivate::layoutHorizontal(bool move)
{
    Q_ASSERT(horizontal && flickable);
    if (horizontal->parentItem() != flickable)
        return;
    horizontal->setWidth(flickable->width());
    if (move)
        horizontal->setY(flickable->height() - horizontal->height());
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 1139, as _ZN30QQuickScrollBarAttachedPrivate14layoutVerticalEb
inline void QQuickScrollBarAttachedPrivate::layoutVertical(bool move)
{
    Q_ASSERT(vertical && flickable);
    if (vertical->parentItem() != flickable)
        return;
    vertical->setHeight(flickable->height());
    if (move)
        vertical->setX(vertical->isMirrored() ? 0 : flickable->width() - vertical->width());
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 1149, as _ZN30QQuickScrollBarAttachedPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickScrollBarAttachedPrivate::itemGeometryChanged(QQuickItem *item, const QQuickGeometryChange change, const QRectF &diff)
{
    Q_UNUSED(item);
    Q_UNUSED(change);
    if (horizontal && horizontal->height() > 0) {
#ifdef QT_QUICK_NEW_GEOMETRY_CHANGED_HANDLING // TODO: correct/rename diff to oldGeometry
        bool move = qFuzzyIsNull(horizontal->y()) || qFuzzyCompare(horizontal->y(), diff.height() - horizontal->height());
#else
        bool move = qFuzzyIsNull(horizontal->y()) || qFuzzyCompare(horizontal->y(), item->height() - diff.height() - horizontal->height());
#endif
        if (flickable)
            layoutHorizontal(move);
    }
    if (vertical && vertical->width() > 0) {
#ifdef QT_QUICK_NEW_GEOMETRY_CHANGED_HANDLING // TODO: correct/rename diff to oldGeometry
        bool move = qFuzzyIsNull(vertical->x()) || qFuzzyCompare(vertical->x(), diff.width() - vertical->width());
#else
        bool move = qFuzzyIsNull(vertical->x()) || qFuzzyCompare(vertical->x(), item->width() - diff.width() - vertical->width());
#endif
        if (flickable)
            layoutVertical(move);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 1173, as _ZN30QQuickScrollBarAttachedPrivate24itemImplicitWidthChangedEP10QQuickItem
inline void QQuickScrollBarAttachedPrivate::itemImplicitWidthChanged(QQuickItem *item)
{
    if (item == vertical && flickable)
        layoutVertical(true);
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 1179, as _ZN30QQuickScrollBarAttachedPrivate25itemImplicitHeightChangedEP10QQuickItem
inline void QQuickScrollBarAttachedPrivate::itemImplicitHeightChanged(QQuickItem *item)
{
    if (item == horizontal && flickable)
        layoutHorizontal(true);
}

//  from ../qtdeclarative/src/quicktemplates/qquickscrollbar.cpp, line 1185, as _ZN30QQuickScrollBarAttachedPrivate13itemDestroyedEP10QQuickItem
inline void QQuickScrollBarAttachedPrivate::itemDestroyed(QQuickItem *item)
{
    if (item == flickable)
        flickable = nullptr;
    if (item == horizontal)
        horizontal = nullptr;
    if (item == vertical)
        vertical = nullptr;
}
//  -----------------------------------------------------------------------

//  A QQuickScrollBarAttachedPrivate that Python can take functions over in. Every QQuickScrollBarAttachedPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickScrollBarAttachedPrivateCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickScrollBarAttachedPrivateCall1)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickScrollBarAttachedPrivateCall2)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickScrollBarAttachedPrivateCall3)(const void *, QQuickItem *, int *);
class CuteQQuickScrollBarAttachedPrivate : public QQuickScrollBarAttachedPrivate {
public:
  using QQuickScrollBarAttachedPrivate::QQuickScrollBarAttachedPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN30QQuickScrollBarAttachedPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuickScrollBarAttachedPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuickScrollBarAttachedPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QQuickScrollBarAttachedPrivate13itemDestroyedEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QQuickScrollBarAttachedPrivate::itemGeometryChanged(QQuickItem
  //      *item, QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickScrollBarAttachedPrivateCall0 call = reinterpret_cast<CuteQQuickScrollBarAttachedPrivateCall0>(taken[0]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickScrollBarAttachedPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void
  //      QQuickScrollBarAttachedPrivate::itemImplicitWidthChanged(QQuickIt
  //      em *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickScrollBarAttachedPrivateCall1 call = reinterpret_cast<CuteQQuickScrollBarAttachedPrivateCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickScrollBarAttachedPrivate::itemImplicitWidthChanged(item);
  }

  //  void
  //      QQuickScrollBarAttachedPrivate::itemImplicitHeightChanged(QQuickI
  //      tem *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickScrollBarAttachedPrivateCall2 call = reinterpret_cast<CuteQQuickScrollBarAttachedPrivateCall2>(taken[2]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickScrollBarAttachedPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickScrollBarAttachedPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickScrollBarAttachedPrivateCall3 call = reinterpret_cast<CuteQQuickScrollBarAttachedPrivateCall3>(taken[3]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickScrollBarAttachedPrivate::itemDestroyed(item);
  }
};

//  QQuickScrollBarAttachedPrivate
//      *QQuickScrollBarAttachedPrivate::get(QQuickScrollBarAttached
//      *attached)
extern "C" Q_DECL_EXPORT
QQuickScrollBarAttachedPrivate *ritual_ZN30QQuickScrollBarAttachedPrivate3getEP23QQuickScrollBarAttached(
    QQuickScrollBarAttached *attached) {
  return QQuickScrollBarAttachedPrivate::get(attached);
}

//  void QQuickScrollBarAttachedPrivate::setFlickable(QQuickFlickable
//      *flickable)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate12setFlickableEP15QQuickFlickable(
    QQuickScrollBarAttachedPrivate *self,
    QQuickFlickable *flickable) {
  self->setFlickable(flickable);
}

//  void QQuickScrollBarAttachedPrivate::initHorizontal()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate14initHorizontalEv(
    QQuickScrollBarAttachedPrivate *self) {
  self->initHorizontal();
}

//  void QQuickScrollBarAttachedPrivate::initVertical()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate12initVerticalEv(
    QQuickScrollBarAttachedPrivate *self) {
  self->initVertical();
}

//  void QQuickScrollBarAttachedPrivate::cleanupHorizontal()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate17cleanupHorizontalEv(
    QQuickScrollBarAttachedPrivate *self) {
  self->cleanupHorizontal();
}

//  void QQuickScrollBarAttachedPrivate::cleanupVertical()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate15cleanupVerticalEv(
    QQuickScrollBarAttachedPrivate *self) {
  self->cleanupVertical();
}

//  void QQuickScrollBarAttachedPrivate::activateHorizontal()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate18activateHorizontalEv(
    QQuickScrollBarAttachedPrivate *self) {
  self->activateHorizontal();
}

//  void QQuickScrollBarAttachedPrivate::activateVertical()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate16activateVerticalEv(
    QQuickScrollBarAttachedPrivate *self) {
  self->activateVertical();
}

//  void QQuickScrollBarAttachedPrivate::mirrorVertical()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate14mirrorVerticalEv(
    QQuickScrollBarAttachedPrivate *self) {
  self->mirrorVertical();
}

//  void QQuickScrollBarAttachedPrivate::layoutHorizontal(bool move)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate16layoutHorizontalEb(
    QQuickScrollBarAttachedPrivate *self,
    bool move) {
  self->layoutHorizontal(move);
}

//  void QQuickScrollBarAttachedPrivate::layoutVertical(bool move)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate14layoutVerticalEb(
    QQuickScrollBarAttachedPrivate *self,
    bool move) {
  self->layoutVertical(move);
}

//  void QQuickScrollBarAttachedPrivate::itemGeometryChanged(QQuickItem
//      *item, QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickScrollBarAttachedPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->itemGeometryChanged(item, *change, *diff);
}

//  void QQuickScrollBarAttachedPrivate::itemImplicitWidthChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickScrollBarAttachedPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickScrollBarAttachedPrivate::itemImplicitHeightChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickScrollBarAttachedPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  void QQuickScrollBarAttachedPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQuickScrollBarAttachedPrivate13itemDestroyedEP10QQuickItem(
    QQuickScrollBarAttachedPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  a Python function taken by a CuteQQuickScrollBarAttachedPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickScrollBarAttachedPrivate(
    QQuickScrollBarAttachedPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickScrollBarAttachedPrivate *>(self)->take(key, call);
}

//  void QQuickScrollBarAttachedPrivate::itemGeometryChanged(QQuickItem
//      *item, QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickScrollBarAttachedPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickScrollBarAttachedPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->QQuickScrollBarAttachedPrivate::itemGeometryChanged(
      item,
      *change,
      *diff);
}

//  void QQuickScrollBarAttachedPrivate::itemImplicitWidthChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickScrollBarAttachedPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickScrollBarAttachedPrivate *self,
    QQuickItem *item) {
  self->QQuickScrollBarAttachedPrivate::itemImplicitWidthChanged(item);
}

//  void QQuickScrollBarAttachedPrivate::itemImplicitHeightChanged(QQuickItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickScrollBarAttachedPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickScrollBarAttachedPrivate *self,
    QQuickItem *item) {
  self->QQuickScrollBarAttachedPrivate::itemImplicitHeightChanged(item);
}

//  void QQuickScrollBarAttachedPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QQuickScrollBarAttachedPrivate13itemDestroyedEP10QQuickItem(
    QQuickScrollBarAttachedPrivate *self,
    QQuickItem *item) {
  self->QQuickScrollBarAttachedPrivate::itemDestroyed(item);
}
