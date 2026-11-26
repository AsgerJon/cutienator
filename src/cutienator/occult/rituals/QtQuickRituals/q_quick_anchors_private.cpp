//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickanchors_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanchors_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickanchors_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickanchors_p_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQml/qqmlinfo.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 13, as local:qquickanchors.cpp:readParentItem
static Q_ALWAYS_INLINE QQuickItem *readParentItem(const QQuickItem *item)
{
    return QQuickItemPrivate::get(item)->parentItem;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 18, as local:qquickanchors.cpp:readX
static Q_ALWAYS_INLINE qreal readX(const QQuickItem *item)
{
    return QQuickItemPrivate::get(item)->x;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 23, as local:qquickanchors.cpp:readY
static Q_ALWAYS_INLINE qreal readY(const QQuickItem *item)
{
    return QQuickItemPrivate::get(item)->y;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 28, as local:qquickanchors.cpp:readWidth
static Q_ALWAYS_INLINE qreal readWidth(const QQuickItem *item)
{
    return QQuickItemPrivate::get(item)->width;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 33, as local:qquickanchors.cpp:readHeight
static Q_ALWAYS_INLINE qreal readHeight(const QQuickItem *item)
{
    return QQuickItemPrivate::get(item)->height;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 38, as local:qquickanchors.cpp:readBaselineOffset
static Q_ALWAYS_INLINE qreal readBaselineOffset(const QQuickItem *item)
{
    return QQuickItemPrivate::get(item)->baselineOffset;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 46, as local:qquickanchors.cpp:hcenter
static inline qreal hcenter(const QQuickItem *item)
{
    qreal width = readWidth(item);
    if (QQuickAnchors *anchors = QQuickItemPrivate::get(item)->_anchors) {
        if (!QQuickAnchorsPrivate::get(anchors)->centerAligned)
            return width / 2;
    }
    return qRound(width / 2);
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 56, as local:qquickanchors.cpp:vcenter
static inline qreal vcenter(const QQuickItem *item)
{
    qreal height = readHeight(item);
    if (QQuickAnchors *anchors = QQuickItemPrivate::get(item)->_anchors) {
        if (!QQuickAnchorsPrivate::get(anchors)->centerAligned)
            return height / 2;
    }
    return qRound(height / 2);
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 100, as local:qquickanchors.cpp:adjustedPosition
static inline qreal adjustedPosition(QQuickItem *item, QQuickAnchors::Anchor anchorLine)
{
    qreal ret = 0.0;
    switch (anchorLine) {
    case QQuickAnchors::LeftAnchor:
        ret = 0.0;
        break;
    case QQuickAnchors::RightAnchor:
        ret = readWidth(item);
        break;
    case QQuickAnchors::TopAnchor:
        ret = 0.0;
        break;
    case QQuickAnchors::BottomAnchor:
        ret = readHeight(item);
        break;
    case QQuickAnchors::HCenterAnchor:
        ret = hcenter(item);
        break;
    case QQuickAnchors::VCenterAnchor:
        ret = vcenter(item);
        break;
    case QQuickAnchors::BaselineAnchor:
        ret = readBaselineOffset(item);
        break;
    default:
        break;
    }

    return ret;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 648, as local:qquickanchors.cpp:reverseAnchorLine
static inline QQuickAnchors::Anchor reverseAnchorLine(QQuickAnchors::Anchor anchorLine)
{
    if (anchorLine == QQuickAnchors::LeftAnchor) {
        return QQuickAnchors::RightAnchor;
    } else if (anchorLine == QQuickAnchors::RightAnchor) {
        return QQuickAnchors::LeftAnchor;
    } else {
        return anchorLine;
    }
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 452, as _ZN20QQuickAnchorsPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickAnchorsPrivate::itemGeometryChanged(QQuickItem *, QQuickGeometryChange change, const QRectF &)
{
    if (!isItemComplete())
        return;

    if (fill) {
        fillChanged();
    } else if (centerIn) {
        centerInChanged();
    } else {
        if ((usedAnchors & QQuickAnchors::Horizontal_Mask) && change.horizontalChange())
            updateHorizontalAnchors();
        if ((usedAnchors & QQuickAnchors::Vertical_Mask) && change.verticalChange())
            updateVerticalAnchors();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 245, as _ZNK20QQuickAnchorsPrivate19calculateDependencyEP10QQuickItem
inline QQuickGeometryChange QQuickAnchorsPrivate::calculateDependency(QQuickItem *controlItem) const
{
    QQuickGeometryChange dependency;

    if (!controlItem || inDestructor)
        return dependency;

    if (fill == controlItem) {
        if (controlItem == readParentItem(item))
            dependency.setSizeChange(true);
        else    //sibling
            dependency.setAllChanged(true);
        return dependency;  //exit early
    }

    if (centerIn == controlItem) {
        if (controlItem == readParentItem(item))
            dependency.setSizeChange(true);
        else    //sibling
            dependency.setAllChanged(true);
        return dependency;  //exit early
    }

    if ((usedAnchors & QQuickAnchors::LeftAnchor && leftAnchorItem == controlItem) ||
        (usedAnchors & QQuickAnchors::RightAnchor && rightAnchorItem == controlItem) ||
        (usedAnchors & QQuickAnchors::HCenterAnchor && hCenterAnchorItem == controlItem)) {
        if (controlItem == readParentItem(item))
            dependency.setWidthChange(true);
        else    //sibling
            dependency.setHorizontalChange(true);
    }

    if ((usedAnchors & QQuickAnchors::TopAnchor && topAnchorItem == controlItem) ||
        (usedAnchors & QQuickAnchors::BottomAnchor && bottomAnchorItem == controlItem) ||
        (usedAnchors & QQuickAnchors::VCenterAnchor && vCenterAnchorItem == controlItem) ||
        (usedAnchors & QQuickAnchors::BaselineAnchor && baselineAnchorItem == controlItem)) {
        if (controlItem == readParentItem(item))
            dependency.setHeightChange(true);
        else    //sibling
            dependency.setVerticalChange(true);
    }

    return dependency;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 207, as _ZN20QQuickAnchorsPrivate9clearItemEP10QQuickItem
inline void QQuickAnchorsPrivate::clearItem(QQuickItem *item)
{
    if (!item)
        return;
    if (fill == item)
        fill = nullptr;
    if (centerIn == item)
        centerIn = nullptr;
    if (leftAnchorItem == item) {
        leftAnchorItem = nullptr;
        usedAnchors &= ~QQuickAnchors::LeftAnchor;
    }
    if (rightAnchorItem == item) {
        rightAnchorItem = nullptr;
        usedAnchors &= ~QQuickAnchors::RightAnchor;
    }
    if (topAnchorItem == item) {
        topAnchorItem = nullptr;
        usedAnchors &= ~QQuickAnchors::TopAnchor;
    }
    if (bottomAnchorItem == item) {
        bottomAnchorItem = nullptr;
        usedAnchors &= ~QQuickAnchors::BottomAnchor;
    }
    if (vCenterAnchorItem == item) {
        vCenterAnchorItem = nullptr;
        usedAnchors &= ~QQuickAnchors::VCenterAnchor;
    }
    if (hCenterAnchorItem == item) {
        hCenterAnchorItem = nullptr;
        usedAnchors &= ~QQuickAnchors::HCenterAnchor;
    }
    if (baselineAnchorItem == item) {
        baselineAnchorItem = nullptr;
        usedAnchors &= ~QQuickAnchors::BaselineAnchor;
    }
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 290, as _ZN20QQuickAnchorsPrivate9addDependEP10QQuickItem
inline void QQuickAnchorsPrivate::addDepend(QQuickItem *item)
{
    if (!item || !componentComplete)
        return;

    QQuickItemPrivate *p = QQuickItemPrivate::get(item);
    p->updateOrAddGeometryChangeListener(this, calculateDependency(item));
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 299, as _ZN20QQuickAnchorsPrivate9remDependEP10QQuickItem
inline void QQuickAnchorsPrivate::remDepend(QQuickItem *item)
{
    if (!item || !componentComplete)
        return;

    QQuickItemPrivate *p = QQuickItemPrivate::get(item);
    p->updateOrRemoveGeometryChangeListener(this, calculateDependency(item));
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 337, as _ZNK20QQuickAnchorsPrivate14isItemCompleteEv
inline bool QQuickAnchorsPrivate::isItemComplete() const
{
    return componentComplete;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 354, as _ZN20QQuickAnchorsPrivate13setItemHeightEd
inline void QQuickAnchorsPrivate::setItemHeight(qreal v)
{
    updatingMe = true;
    item->setHeight(v);
    updatingMe = false;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 361, as _ZN20QQuickAnchorsPrivate12setItemWidthEd
inline void QQuickAnchorsPrivate::setItemWidth(qreal v)
{
    updatingMe = true;
    item->setWidth(v);
    updatingMe = false;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 368, as _ZN20QQuickAnchorsPrivate8setItemXEd
inline void QQuickAnchorsPrivate::setItemX(qreal v)
{
    updatingMe = true;
    item->setX(v);
    updatingMe = false;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 375, as _ZN20QQuickAnchorsPrivate8setItemYEd
inline void QQuickAnchorsPrivate::setItemY(qreal v)
{
    updatingMe = true;
    item->setY(v);
    updatingMe = false;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 382, as _ZN20QQuickAnchorsPrivate10setItemPosERK7QPointF
inline void QQuickAnchorsPrivate::setItemPos(const QPointF &v)
{
    updatingMe = true;
    item->setPosition(v);
    updatingMe = false;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 389, as _ZN20QQuickAnchorsPrivate11setItemSizeERK6QSizeF
inline void QQuickAnchorsPrivate::setItemSize(const QSizeF &v)
{
    updatingMe = true;
    item->setSize(v);
    updatingMe = false;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 1297, as _ZNK20QQuickAnchorsPrivate11checkHValidEv
inline bool QQuickAnchorsPrivate::checkHValid() const
{
    if (usedAnchors & QQuickAnchors::LeftAnchor &&
        usedAnchors & QQuickAnchors::RightAnchor &&
        usedAnchors & QQuickAnchors::HCenterAnchor) {
        qmlWarning(item) << QQuickAnchors::tr("Cannot specify left, right, and horizontalCenter anchors at the same time.");
        return false;
    }

    return true;
}

//  from ../qtdeclarative/src/quick/items/qquickanchors.cpp, line 1329, as _ZNK20QQuickAnchorsPrivate11checkVValidEv
inline bool QQuickAnchorsPrivate::checkVValid() const
{
    if (usedAnchors & QQuickAnchors::TopAnchor &&
        usedAnchors & QQuickAnchors::BottomAnchor &&
        usedAnchors & QQuickAnchors::VCenterAnchor) {
        qmlWarning(item) << QQuickAnchors::tr("Cannot specify top, bottom, and verticalCenter anchors at the same time.");
        return false;
    } else if (usedAnchors & QQuickAnchors::BaselineAnchor &&
               (usedAnchors & QQuickAnchors::TopAnchor ||
                usedAnchors & QQuickAnchors::BottomAnchor ||
                usedAnchors & QQuickAnchors::VCenterAnchor)) {
        qmlWarning(item) << QQuickAnchors::tr("Baseline anchor cannot be used in conjunction with top, bottom, or verticalCenter anchors.");
        return false;
    }

    return true;
}
//  -----------------------------------------------------------------------

//  A QQuickAnchorsPrivate that Python can take functions over in. Every QQuickAnchorsPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickAnchorsPrivateCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void * (*CuteQQuickAnchorsPrivateCall1)(const void *, int *);
class CuteQQuickAnchorsPrivate : public QQuickAnchorsPrivate {
public:
  using QQuickAnchorsPrivate::QQuickAnchorsPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickAnchorsPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickAnchorsPrivate13anchorPrivateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QQuickAnchorsPrivate::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickAnchorsPrivateCall0 call = reinterpret_cast<CuteQQuickAnchorsPrivateCall0>(taken[0]);
      call(this, a0, &a1, &a2, &handled);
      if (handled) return;
    }
    QQuickAnchorsPrivate::itemGeometryChanged(a0, a1, a2);
  }

  //  QQuickAnchorsPrivate *QQuickAnchorsPrivate::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickAnchorsPrivateCall1 call = reinterpret_cast<CuteQQuickAnchorsPrivateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickAnchorsPrivate *>(given);
    }
    return QQuickAnchorsPrivate::anchorPrivate();
  }
};

//  QQuickAnchors *QQuickAnchorsPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickAnchors *ritual_ZN20QQuickAnchorsPrivate6q_funcEv(
    QQuickAnchorsPrivate *self) {
  return self->q_func();
}

//  const QQuickAnchors *QQuickAnchorsPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickAnchors *ritual_ZNK20QQuickAnchorsPrivate6q_funcEv(
    const QQuickAnchorsPrivate *self) {
  return self->q_func();
}

//  void QQuickAnchorsPrivate::clearItem(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnchorsPrivate9clearItemEP10QQuickItem(
    QQuickAnchorsPrivate *self,
    QQuickItem *a0) {
  self->clearItem(a0);
}

//  void QQuickAnchorsPrivate::addDepend(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnchorsPrivate9addDependEP10QQuickItem(
    QQuickAnchorsPrivate *self,
    QQuickItem *a0) {
  self->addDepend(a0);
}

//  void QQuickAnchorsPrivate::remDepend(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnchorsPrivate9remDependEP10QQuickItem(
    QQuickAnchorsPrivate *self,
    QQuickItem *a0) {
  self->remDepend(a0);
}

//  bool QQuickAnchorsPrivate::isItemComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAnchorsPrivate14isItemCompleteEv(
    const QQuickAnchorsPrivate *self) {
  return self->isItemComplete();
}

//  void QQuickAnchorsPrivate::setItemHeight(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnchorsPrivate13setItemHeightEd(
    QQuickAnchorsPrivate *self,
    qreal a0) {
  self->setItemHeight(a0);
}

//  void QQuickAnchorsPrivate::setItemWidth(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnchorsPrivate12setItemWidthEd(
    QQuickAnchorsPrivate *self,
    qreal a0) {
  self->setItemWidth(a0);
}

//  void QQuickAnchorsPrivate::setItemX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnchorsPrivate8setItemXEd(
    QQuickAnchorsPrivate *self,
    qreal a0) {
  self->setItemX(a0);
}

//  void QQuickAnchorsPrivate::setItemY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnchorsPrivate8setItemYEd(
    QQuickAnchorsPrivate *self,
    qreal a0) {
  self->setItemY(a0);
}

//  void QQuickAnchorsPrivate::setItemPos(const QPointF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnchorsPrivate10setItemPosERK7QPointF(
    QQuickAnchorsPrivate *self,
    const QPointF *a0) {
  self->setItemPos(*a0);
}

//  void QQuickAnchorsPrivate::setItemSize(const QSizeF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnchorsPrivate11setItemSizeERK6QSizeF(
    QQuickAnchorsPrivate *self,
    const QSizeF *a0) {
  self->setItemSize(*a0);
}

//  void QQuickAnchorsPrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange a1, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickAnchorsPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickAnchorsPrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *a1,
    const QRectF *a2) {
  self->itemGeometryChanged(a0, *a1, *a2);
}

//  QQuickAnchorsPrivate *QQuickAnchorsPrivate::anchorPrivate()
extern "C" Q_DECL_EXPORT
QQuickAnchorsPrivate *ritual_ZN20QQuickAnchorsPrivate13anchorPrivateEv(
    QQuickAnchorsPrivate *self) {
  return self->anchorPrivate();
}

//  bool QQuickAnchorsPrivate::checkHValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAnchorsPrivate11checkHValidEv(
    const QQuickAnchorsPrivate *self) {
  return self->checkHValid();
}

//  bool QQuickAnchorsPrivate::checkVValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickAnchorsPrivate11checkVValidEv(
    const QQuickAnchorsPrivate *self) {
  return self->checkVValid();
}

//  QQuickAnchorsPrivate *QQuickAnchorsPrivate::get(QQuickAnchors *o)
extern "C" Q_DECL_EXPORT
QQuickAnchorsPrivate *ritual_ZN20QQuickAnchorsPrivate3getEP13QQuickAnchors(
    QQuickAnchors *o) {
  return QQuickAnchorsPrivate::get(o);
}

//  a Python function taken by a CuteQQuickAnchorsPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickAnchorsPrivate(
    QQuickAnchorsPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickAnchorsPrivate *>(self)->take(key, call);
}

//  QQuickAnchorsPrivate *QQuickAnchorsPrivate::anchorPrivate()
extern "C" Q_DECL_EXPORT
QQuickAnchorsPrivate *ritual_own_ZN20QQuickAnchorsPrivate13anchorPrivateEv(
    QQuickAnchorsPrivate *self) {
  return self->QQuickAnchorsPrivate::anchorPrivate();
}
