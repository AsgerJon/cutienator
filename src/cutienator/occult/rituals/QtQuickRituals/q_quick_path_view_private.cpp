//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpathview_p_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 11 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpathview_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickpathview_p_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtQuick/private/qquicktimeline_p_p.h>
#include <QtCore/QDebug>
#include <QtCore/QMutex>
#include <QtCore/QThread>
#include <QtCore/QWaitCondition>
#include <QtCore/QEvent>
#include <QtCore/QCoreApplication>
#include <QtCore/QEasingCurve>
#include <QtCore/QTime>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/QHash>
#include <algorithm>
#include <QtQuick/private/qquickpathview_p.h>
#include <QtQuick/private/qquickpathview_p_p.h>
#include <QtQuick/private/qquickflickablebehavior_p.h> //Contains flicking behavior defines
#include <QtQuick/private/qquicktext_p.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQuick/private/qquickpointerhandler_p.h>
#include <QtQuick/private/qquickstate_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlopenmetaobject_p.h>
#include <private/qqmlchangeset_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtQml/qqmlinfo.h>
#include <QtGui/private/qeventpoint_p.h>
#include <QtGui/qevent.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qstylehints.h>
#include <QtCore/qmath.h>
#include <cmath>
#if QT_CONFIG(quick_itemview)
#include <QtQuick/private/qquickitemview_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickitemview.cpp, line 14, as _Z27lcItemViewDelegateLifecyclev
inline const QLoggingCategory &lcItemViewDelegateLifecycle()
{
    static const QLoggingCategory category("qt.quick.itemview.lifecycle");
    return category;
}

//  from ../qtdeclarative/src/quick/util/qquicktimeline.cpp, line 889, as _ZN20QQuickTimeLineObjectC2Ev
inline QQuickTimeLineObject::QQuickTimeLineObject()
: _t(nullptr)
{
}

//  from ../qtdeclarative/src/quick/util/qquicktimeline.cpp, line 894, as _ZN20QQuickTimeLineObjectD2Ev
inline QQuickTimeLineObject::~QQuickTimeLineObject()
{
    if (_t) {
        _t->remove(this);
        _t = nullptr;
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 61, as _ZN22QQuickPathViewAttached8setValueERK10QByteArrayRK8QVariant
inline void QQuickPathViewAttached::setValue(const QByteArray &name, const QVariant &val)
{
    m_metaobject->setValue(name, val);
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 66, as _ZN21QQuickPathViewPrivateC1Ev
inline QQuickPathViewPrivate::QQuickPathViewPrivate()
  : path(nullptr), currentIndex(0), currentItemOffset(0), startPc(0)
    , offset(0), offsetAdj(0), mappedRange(1), mappedCache(0)
    , stealMouse(false), ownModel(false), interactive(true), haveHighlightRange(true)
    , autoHighlight(true), highlightUp(false), layoutScheduled(false)
    , moving(false), flicking(false), dragging(false), inRequest(false), delegateValidated(false)
    , inRefill(false)
    , dragMargin(0), deceleration(100)
    , maximumFlickVelocity(QGuiApplicationPrivate::platformTheme()->themeHint(QPlatformTheme::FlickMaximumVelocity).toReal())
    , moveOffset(this, &QQuickPathViewPrivate::setAdjustedOffset), flickDuration(0)
    , pathItems(-1), requestedIndex(-1), cacheSize(0), requestedCacheSize(0), requestedZ(0)
    , moveReason(Other), movementDirection(QQuickPathView::Shortest), moveDirection(QQuickPathView::Shortest)
    , attType(nullptr), highlightComponent(nullptr), highlightItem(nullptr)
    , moveHighlight(this, &QQuickPathViewPrivate::setHighlightPosition)
    , highlightPosition(0)
    , highlightRangeStart(0), highlightRangeEnd(0)
    , highlightRangeMode(QQuickPathView::StrictlyEnforceRange)
    , highlightMoveDuration(300), modelCount(0), snapMode(QQuickPathView::NoSnap)
{
    setSizePolicy(QLayoutPolicy::Preferred, QLayoutPolicy::Preferred);
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 88, as _ZN21QQuickPathViewPrivate4initEv
inline void QQuickPathViewPrivate::init()
{
    Q_Q(QQuickPathView);
    offset = 0;
    q->setAcceptedMouseButtons(Qt::LeftButton);
    q->setFlag(QQuickItem::ItemIsFocusScope);
    q->setFiltersChildMouseEvents(true);
    qmlobject_connect(&tl, QQuickTimeLine, SIGNAL(updated()),
                      q, QQuickPathView, SLOT(ticked()));
    timer.invalidate();
    qmlobject_connect(&tl, QQuickTimeLine, SIGNAL(completed()),
                      q, QQuickPathView, SLOT(movementEnding()));
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 102, as _ZN21QQuickPathViewPrivate7getItemEidb
inline QQuickItem *QQuickPathViewPrivate::getItem(int modelIndex, qreal z, bool async)
{
    Q_Q(QQuickPathView);
    requestedIndex = modelIndex;
    requestedZ = z;
    inRequest = true;
    QObject *object = model->object(modelIndex, async ? QQmlIncubator::Asynchronous : QQmlIncubator::AsynchronousIfNested);
    QQuickItem *item = qmlobject_cast<QQuickItem*>(object);
    if (!item) {
        if (object) {
            model->release(object);
            if (!delegateValidated) {
                delegateValidated = true;
                QObject* delegate = q->delegate();
                qmlWarning(delegate ? delegate : q) << QQuickPathView::tr("Delegate must be of Item type");
            }
        }
    } else {
        item->setParentItem(q);
        requestedIndex = -1;
        QQuickItemPrivate *itemPrivate = QQuickItemPrivate::get(item);
        itemPrivate->addItemChangeListener(
                    this, QQuickItemPrivate::Geometry | QQuickItemPrivate::Destroyed);
    }
    inRequest = false;
    return item;
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 175, as _ZN21QQuickPathViewPrivate11releaseItemEP10QQuickItem
inline void QQuickPathViewPrivate::releaseItem(QQuickItem *item)
{
    if (!item)
        return;
    qCDebug(lcItemViewDelegateLifecycle) << "release" << item;
    QQuickItemPrivate *itemPrivate = QQuickItemPrivate::get(item);
    itemPrivate->removeItemChangeListener(
                this, QQuickItemPrivate::Geometry | QQuickItemPrivate::Destroyed);
    if (!model)
        return;
    QQmlInstanceModel::ReleaseFlags flags = model->release(item);
    if (!flags) {
        // item was not destroyed, and we no longer reference it.
        if (QQuickPathViewAttached *att = attached(item))
            att->setOnPath(false);
    } else if (flags & QQmlInstanceModel::Destroyed) {
        // but we still reference it
        item->setParentItem(nullptr);
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 196, as _ZN21QQuickPathViewPrivate8attachedEP10QQuickItem
inline QQuickPathViewAttached *QQuickPathViewPrivate::attached(QQuickItem *item)
{
    return static_cast<QQuickPathViewAttached *>(qmlAttachedPropertiesObject<QQuickPathView>(item, false));
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 201, as _ZN21QQuickPathViewPrivate12attachedTypeEv
inline QQmlOpenMetaObjectType *QQuickPathViewPrivate::attachedType()
{
    if (!attType) {
        // pre-create one metatype to share with all attached objects
        attType = new QQmlOpenMetaObjectType(&QQuickPathViewAttached::staticMetaObject);
        if (path) {
            const auto attributes = path->attributes();
            for (const QString &attr : attributes)
                attType->createProperty(attr.toUtf8());
        }
    }

    return attType;
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 216, as _ZN21QQuickPathViewPrivate5clearEv
inline void QQuickPathViewPrivate::clear()
{
    releaseCurrentItem();

    for (QQuickItem *p : std::as_const(items))
        releaseItem(p);

    for (QQuickItem *p : std::as_const(itemCache))
        releaseItem(p);

    if (requestedIndex >= 0) {
        if (model)
            model->cancel(requestedIndex);
        requestedIndex = -1;
    }

    items.clear();
    itemCache.clear();
    tl.clear();
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 237, as _ZN21QQuickPathViewPrivate17updateMappedRangeEv
inline void QQuickPathViewPrivate::updateMappedRange()
{
    // Update the actual cache size to be at max
    // the available non-visible items.
    cacheSize = qMax(0, qMin(requestedCacheSize, modelCount - pathItems));

    if (model && pathItems != -1 && pathItems < modelCount) {
        mappedRange = qreal(modelCount)/pathItems;
        mappedCache = qreal(cacheSize)/pathItems/2; // Half of cache at each end
    } else {
        mappedRange = 1;
        mappedCache = 0;
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 252, as _ZNK21QQuickPathViewPrivate15positionOfIndexEd
inline qreal QQuickPathViewPrivate::positionOfIndex(qreal index) const
{
    qreal pos = -1;

    if (model && index >= 0 && index < modelCount) {
        qreal start = 0;
        if (haveHighlightRange && (highlightRangeMode != QQuickPathView::NoHighlightRange
                                   || snapMode != QQuickPathView::NoSnap))
            start = highlightRangeStart;
        qreal globalPos = index + offset;
        globalPos = std::fmod(globalPos, qreal(modelCount)) / modelCount;
        if (pathItems != -1 && pathItems < modelCount) {
            globalPos += start / mappedRange;
            globalPos = std::fmod(globalPos, qreal(1));
            pos = globalPos * mappedRange;
        } else {
            pos = std::fmod(globalPos + start, qreal(1));
        }
    }

    return pos;
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 277, as _ZNK21QQuickPathViewPrivate9isInBoundEdddb
inline bool QQuickPathViewPrivate::isInBound(qreal position, qreal lower,
                                      qreal upper, bool emptyRangeCheck) const
{
    if (emptyRangeCheck && qFuzzyCompare(lower, upper))
        return true;
    if (lower > upper) {
        if (position > upper && position > lower)
            position -= mappedRange;
        lower -= mappedRange;
    }
    return position >= lower && position < upper;
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 290, as _ZN21QQuickPathViewPrivate15createHighlightEv
inline void QQuickPathViewPrivate::createHighlight()
{
    Q_Q(QQuickPathView);
    if (!q->isComponentComplete())
        return;

    bool changed = false;
    if (highlightItem) {
        highlightItem->setParentItem(nullptr);
        highlightItem->deleteLater();
        highlightItem = nullptr;
        changed = true;
    }

    QQuickItem *item = nullptr;
    if (highlightComponent) {
        QQmlContext *creationContext = highlightComponent->creationContext();
        QQmlContext *highlightContext = new QQmlContext(
                creationContext ? creationContext : qmlContext(q));
        QObject *nobj = highlightComponent->create(highlightContext);
        if (nobj) {
            QQml_setParent_noEvent(highlightContext, nobj);
            item = qobject_cast<QQuickItem *>(nobj);
            if (!item)
                delete nobj;
        } else {
            delete highlightContext;
        }
    } else {
        item = new QQuickItem;
    }
    if (item) {
        QQml_setParent_noEvent(item, q);
        item->setParentItem(q);
        highlightItem = item;
        changed = true;
    }
    if (changed)
        emit q->highlightItemChanged();
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 331, as _ZN21QQuickPathViewPrivate15updateHighlightEv
inline void QQuickPathViewPrivate::updateHighlight()
{
    Q_Q(QQuickPathView);
    if (!q->isComponentComplete() || !isValid())
        return;
    if (highlightItem) {
        if (haveHighlightRange && highlightRangeMode == QQuickPathView::StrictlyEnforceRange) {
            updateItem(highlightItem, highlightRangeStart);
        } else {
            qreal target = currentIndex;

            offsetAdj = 0;
            tl.reset(moveHighlight);
            moveHighlight.setValue(highlightPosition);

            const int duration = highlightMoveDuration;

            if (target - highlightPosition > modelCount/2) {
                highlightUp = false;
                qreal distance = modelCount - target + highlightPosition;
                tl.move(moveHighlight, 0, QEasingCurve(QEasingCurve::InQuad), int(duration * highlightPosition / distance));
                tl.set(moveHighlight, modelCount-0.01);
                tl.move(moveHighlight, target, QEasingCurve(QEasingCurve::OutQuad), int(duration * (modelCount-target) / distance));
            } else if (target - highlightPosition <= -modelCount/2) {
                highlightUp = true;
                qreal distance = modelCount - highlightPosition + target;
                tl.move(moveHighlight, modelCount-0.01, QEasingCurve(QEasingCurve::InQuad), int(duration * (modelCount-highlightPosition) / distance));
                tl.set(moveHighlight, 0);
                tl.move(moveHighlight, target, QEasingCurve(QEasingCurve::OutQuad), int(duration * target / distance));
            } else {
                highlightUp = highlightPosition - target < 0;
                tl.move(moveHighlight, target, QEasingCurve(QEasingCurve::InOutQuad), duration);
            }
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 368, as _ZN21QQuickPathViewPrivate20setHighlightPositionEd
inline void QQuickPathViewPrivate::setHighlightPosition(qreal pos)
{
    if (!(qFuzzyCompare(pos, highlightPosition))) {
        qreal start = 0;
        qreal end = 1;
        if (haveHighlightRange && highlightRangeMode != QQuickPathView::NoHighlightRange) {
            start = highlightRangeStart;
            end = highlightRangeEnd;
        }

        qreal range = qreal(modelCount);
        // calc normalized position of highlight relative to offset
        qreal relativeHighlight = std::fmod(pos + offset, range) / range;

        if (!highlightUp && relativeHighlight > end / mappedRange) {
            qreal diff = 1 - relativeHighlight;
            setOffset(offset + diff * range);
        } else if (highlightUp && relativeHighlight >= (end - start) / mappedRange) {
            qreal diff = relativeHighlight - (end - start) / mappedRange;
            setOffset(offset - diff * range - 0.00001);
        }

        highlightPosition = pos;
        qreal pathPos = positionOfIndex(pos);
        updateItem(highlightItem, pathPos);
        if (QQuickPathViewAttached *att = attached(highlightItem))
            att->setOnPath(pathPos < 1);
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 1637, as _ZN21QQuickPathViewPrivate21handleMousePressEventEP11QMouseEvent
inline void QQuickPathViewPrivate::handleMousePressEvent(QMouseEvent *event)
{
    Q_Q(QQuickPathView);
    if (!interactive || !items.size() || !model || !modelCount)
        return;
    velocityBuffer.clear();
    int idx = 0;
    for (; idx < items.size(); ++idx) {
        QQuickItem *item = items.at(idx);
        if (item->contains(item->mapFromScene(event->scenePosition())))
            break;
    }
    if (idx == items.size() && qFuzzyIsNull(dragMargin))  // didn't click on an item
        return;

    startPoint = pointNear(event->position(), &startPc);
    startPos = event->position();
    if (idx == items.size()) {
        qreal distance = qAbs(event->position().x() - startPoint.x()) + qAbs(event->position().y() - startPoint.y());
        if (distance > dragMargin)
            return;
    }

    if (tl.isActive() && flicking && flickDuration && qreal(tl.time()) / flickDuration < 0.8) {
        stealMouse = true; // If we've been flicked then steal the click.
        q->grabMouse(); // grab it right now too, just to be sure (QTBUG-77173)
    } else {
        stealMouse = false;
    }
    q->setKeepMouseGrab(stealMouse);

    timer.start();
    lastPosTime = computeCurrentTime(event);
    tl.clear();
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 2315, as _ZN21QQuickPathViewPrivate16calcCurrentIndexEv
inline int QQuickPathViewPrivate::calcCurrentIndex()
{
    int current = 0;
    if (modelCount && model && items.size()) {
        offset = std::fmod(offset, qreal(modelCount));
        if (offset < 0)
            offset += modelCount;
        current = qRound(qAbs(std::fmod(modelCount - offset, qreal(modelCount))));
        current = current % modelCount;
    }

    return current;
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 2329, as _ZN21QQuickPathViewPrivate17createCurrentItemEv
inline void QQuickPathViewPrivate::createCurrentItem()
{
    if (requestedIndex != -1)
        return;

    bool inItems = false;
    for (QQuickItem *item : std::as_const(items)) {
        if (model->indexOf(item, nullptr) == currentIndex) {
            inItems = true;
            break;
        }
    }

    if (inItems) {
        if ((currentItem = getItem(currentIndex, currentIndex))) {
            currentItem->setFocus(true);
            if (QQuickPathViewAttached *att = attached(currentItem))
                att->setIsCurrentItem(true);
        }
    } else if (currentIndex >= 0 && currentIndex < modelCount) {
        if ((currentItem = getItem(currentIndex, currentIndex))) {
            updateItem(currentItem, 1);
            if (QQuickPathViewAttached *att = attached(currentItem))
                att->setIsCurrentItem(true);
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 2357, as _ZN21QQuickPathViewPrivate13updateCurrentEv
inline void QQuickPathViewPrivate::updateCurrent()
{
    Q_Q(QQuickPathView);
    if (moveReason == SetIndex)
        return;
    if (!modelCount || !haveHighlightRange || highlightRangeMode != QQuickPathView::StrictlyEnforceRange)
        return;

    int idx = calcCurrentIndex();
    if (model && (idx != currentIndex || !currentItem)) {
        if (currentItem) {
            if (QQuickPathViewAttached *att = attached(currentItem))
                att->setIsCurrentItem(false);
            releaseCurrentItem();
        }
        int oldCurrentIndex = currentIndex;
        currentIndex = idx;
        currentItem = nullptr;
        createCurrentItem();
        if (oldCurrentIndex != currentIndex)
            emit q->currentIndexChanged();
        emit q->currentItemChanged();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 2382, as _ZN21QQuickPathViewPrivate17fixOffsetCallbackEPv
inline void QQuickPathViewPrivate::fixOffsetCallback(void *d)
{
    static_cast<QQuickPathViewPrivate *>(d)->fixOffset();
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 2387, as _ZN21QQuickPathViewPrivate9fixOffsetEv
inline void QQuickPathViewPrivate::fixOffset()
{
    Q_Q(QQuickPathView);
    if (model && items.size()) {
        if (haveHighlightRange && (highlightRangeMode == QQuickPathView::StrictlyEnforceRange
                || snapMode != QQuickPathView::NoSnap)) {
            int curr = calcCurrentIndex();
            if (curr != currentIndex && highlightRangeMode == QQuickPathView::StrictlyEnforceRange)
                q->setCurrentIndex(curr);
            else
                snapToIndex(curr, Other);
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 826, as _ZN21QQuickPathViewPrivate9setOffsetEd
inline void QQuickPathViewPrivate::setOffset(qreal o)
{
    Q_Q(QQuickPathView);
    if (!qFuzzyCompare(offset, o)) {
        if (isValid() && q->isComponentComplete()) {
            qreal oldOffset = offset;
            offset = std::fmod(o, qreal(modelCount));
            if (offset < 0)
                offset += qreal(modelCount);
            qCDebug(lcItemViewDelegateLifecycle) << o << "was" << oldOffset << "now" << offset;
            q->refill();
        } else {
            offset = o;
        }
        emit q->offsetChanged();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 844, as _ZN21QQuickPathViewPrivate17setAdjustedOffsetEd
inline void QQuickPathViewPrivate::setAdjustedOffset(qreal o)
{
    setOffset(o+offsetAdj);
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 427, as _ZN21QQuickPathViewPrivate10regenerateEv
inline void QQuickPathViewPrivate::regenerate()
{
    Q_Q(QQuickPathView);
    if (!q->isComponentComplete())
        return;

    clear();

    if (!isValid())
        return;

    updateMappedRange();
    q->refill();
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 408, as _ZN21QQuickPathViewPrivate10updateItemEP10QQuickItemd
inline void QQuickPathViewPrivate::updateItem(QQuickItem *item, qreal percent)
{
    if (!path)
        return;
    if (QQuickPathViewAttached *att = attached(item)) {
        if (qFuzzyCompare(att->m_percent, percent))
            return;
        att->m_percent = percent;
        const auto attributes = path->attributes();
        for (const QString &attr : attributes)
            att->setValue(attr.toUtf8(), path->attributeAt(attr, percent));
        att->setOnPath(percent < 1);
    }
    QQuickItemPrivate::get(item)->setCulled(percent >= 1);
    QPointF pf = path->pointAtPercent(qMin(percent, qreal(1)));
    item->setX(pf.x() - item->width()/2);
    item->setY(pf.y() - item->height()/2);
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 2402, as _ZN21QQuickPathViewPrivate11snapToIndexEiNS_14MovementReasonE
inline void QQuickPathViewPrivate::snapToIndex(int index, MovementReason reason)
{
    if (!model || modelCount <= 0)
        return;

    qreal targetOffset = std::fmod(qreal(modelCount - index), qreal(modelCount));
    moveReason = reason;
    offsetAdj = 0;
    tl.reset(moveOffset);
    moveOffset.setValue(offset);

    const int duration = highlightMoveDuration;

    const qreal count = pathItems == -1 ? modelCount : qMin(pathItems, modelCount);
    const qreal averageItemLength = path->path().length() / count;
    const qreal threshold = 0.5 / averageItemLength; // if we are within .5 px, we want to immediately assign rather than animate

    if (!duration || qAbs(offset - targetOffset) < threshold || (qFuzzyIsNull(targetOffset) && qAbs(modelCount - offset) < threshold)) {
        tl.set(moveOffset, targetOffset);
    } else if (moveDirection == QQuickPathView::Positive || (moveDirection == QQuickPathView::Shortest && targetOffset - offset > modelCount/2)) {
        qreal distance = modelCount - targetOffset + offset;
        if (targetOffset > moveOffset) {
            tl.move(moveOffset, 0, QEasingCurve(QEasingCurve::InQuad), int(duration * offset / distance));
            tl.set(moveOffset, modelCount);
            tl.move(moveOffset, targetOffset, QEasingCurve(qFuzzyIsNull(offset) ? QEasingCurve::InOutQuad : QEasingCurve::OutQuad), int(duration * (modelCount-targetOffset) / distance));
        } else {
            tl.move(moveOffset, targetOffset, QEasingCurve(QEasingCurve::InOutQuad), duration);
        }
    } else if (moveDirection == QQuickPathView::Negative || targetOffset - offset <= -modelCount/2) {
        qreal distance = modelCount - offset + targetOffset;
        if (targetOffset < moveOffset) {
            tl.move(moveOffset, modelCount, QEasingCurve(qFuzzyIsNull(targetOffset) ? QEasingCurve::InOutQuad : QEasingCurve::InQuad), int(duration * (modelCount-offset) / distance));
            tl.set(moveOffset, 0);
            tl.move(moveOffset, targetOffset, QEasingCurve(QEasingCurve::OutQuad), int(duration * targetOffset / distance));
        } else {
            tl.move(moveOffset, targetOffset, QEasingCurve(QEasingCurve::InOutQuad), duration);
        }
    } else {
        tl.move(moveOffset, targetOffset, QEasingCurve(QEasingCurve::InOutQuad), duration);
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 1555, as _ZNK21QQuickPathViewPrivate9pointNearERK7QPointFPd
inline QPointF QQuickPathViewPrivate::pointNear(const QPointF &point, qreal *nearPercent) const
{
    const auto pathLength = path->path().length();
    qreal samples = qMin(pathLength / 5, qreal(500));
    qreal res = pathLength / samples;

    qreal mindist = 1e10; // big number
    QPointF nearPoint = path->pointAtPercent(0);
    qreal nearPc = 0;

    // get rough pos
    for (qreal i=1; i < samples; i++) {
        QPointF pt = path->pointAtPercent(i/samples);
        QPointF diff = pt - point;
        qreal dist = diff.x()*diff.x() + diff.y()*diff.y();
        if (dist < mindist) {
            nearPoint = pt;
            nearPc = i;
            mindist = dist;
        }
    }

    // now refine
    qreal approxPc = nearPc;
    for (qreal i = approxPc-1; i < approxPc+1; i += 1/(2*res)) {
        QPointF pt = path->pointAtPercent(i/samples);
        QPointF diff = pt - point;
        qreal dist = diff.x()*diff.x() + diff.y()*diff.y();
        if (dist < mindist) {
            nearPoint = pt;
            nearPc = i;
            mindist = dist;
        }
    }

    if (nearPercent)
        *nearPercent = nearPc / samples;

    return nearPoint;
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 1619, as _ZNK21QQuickPathViewPrivate18computeCurrentTimeEP11QInputEvent
inline qint64 QQuickPathViewPrivate::computeCurrentTime(QInputEvent *event) const
{
    if (0 != event->timestamp())
        return qint64(event->timestamp());
    return timer.elapsed();
}

//  from ../qtdeclarative/src/quick/items/qquickpathview.cpp, line 442, as _ZN21QQuickPathViewPrivate11setDraggingEb
inline void QQuickPathViewPrivate::setDragging(bool d)
{
    Q_Q(QQuickPathView);
    if (dragging == d)
        return;

    dragging = d;
    if (dragging)
        emit q->dragStarted();
    else
        emit q->dragEnded();

    emit q->draggingChanged();
}
//  -----------------------------------------------------------------------

//  A QQuickPathViewPrivate that Python can take functions over in. Every QQuickPathViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_pathview)
typedef void (*CuteQQuickPathViewPrivateCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
typedef void (*CuteQQuickPathViewPrivateCall1)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quick_pathview)
typedef void (*CuteQQuickPathViewPrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickPathViewPrivateCall3)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickPathViewPrivateCall4)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickPathViewPrivateCall5)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickPathViewPrivateCall6)(const void *, int, int *);
typedef qreal (*CuteQQuickPathViewPrivateCall7)(const void *, int *);
typedef qreal (*CuteQQuickPathViewPrivateCall8)(const void *, int *);
typedef void (*CuteQQuickPathViewPrivateCall9)(const void *, int *);
typedef void (*CuteQQuickPathViewPrivateCall10)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickPathViewPrivateCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickPathViewPrivateCall12)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickPathViewPrivateCall13)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickPathViewPrivateCall14)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickPathViewPrivateCall15)(const void *, bool, int *);
typedef void * (*CuteQQuickPathViewPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickPathViewPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickPathViewPrivateCall18)(const void *, int *);
typedef void (*CuteQQuickPathViewPrivateCall19)(const void *, int, int *);
class CuteQQuickPathViewPrivate : public QQuickPathViewPrivate {
public:
  using QQuickPathViewPrivate::QQuickPathViewPrivate;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_pathview)
    if (!std::strcmp(key, "_ZN21QQuickPathViewPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_pathview)
#if QT_CONFIG(quick_pathview)
    if (!std::strcmp(key, "_ZN21QQuickPathViewPrivate13itemDestroyedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_pathview)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[13] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[19] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(quick_pathview)
  //  void QQuickPathViewPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &a2) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall0 call = reinterpret_cast<CuteQQuickPathViewPrivateCall0>(taken[0]);
      call(this, item, &change, &a2, &handled);
      if (handled) return;
    }
    QQuickPathViewPrivate::itemGeometryChanged(item, change, a2);
  }
#endif  // QT_CONFIG(quick_pathview)

#if QT_CONFIG(quick_pathview)
  //  void QQuickPathViewPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall1 call = reinterpret_cast<CuteQQuickPathViewPrivateCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickPathViewPrivate::itemDestroyed(item);
  }
#endif  // QT_CONFIG(quick_pathview)

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall2 call = reinterpret_cast<CuteQQuickPathViewPrivateCall2>(taken[2]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall3 call = reinterpret_cast<CuteQQuickPathViewPrivateCall3>(taken[3]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::removePointerHandler(h);
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
  //      QMetaObject *attachedType)
  QtPrivate::QQuickAttachedPropertyPropagator *attachedPropertyPropagator_parent(
      const QMetaObject *attachedType) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall4 call = reinterpret_cast<CuteQQuickPathViewPrivateCall4>(taken[4]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall5 call = reinterpret_cast<CuteQQuickPathViewPrivateCall5>(taken[5]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall6 call = reinterpret_cast<CuteQQuickPathViewPrivateCall6>(taken[6]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall7 call = reinterpret_cast<CuteQQuickPathViewPrivateCall7>(taken[7]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall8 call = reinterpret_cast<CuteQQuickPathViewPrivateCall8>(taken[8]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall9 call = reinterpret_cast<CuteQQuickPathViewPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall10 call = reinterpret_cast<CuteQQuickPathViewPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall11 call = reinterpret_cast<CuteQQuickPathViewPrivateCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall12 call = reinterpret_cast<CuteQQuickPathViewPrivateCall12>(taken[12]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall13 call = reinterpret_cast<CuteQQuickPathViewPrivateCall13>(taken[13]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall14 call = reinterpret_cast<CuteQQuickPathViewPrivateCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall15 call = reinterpret_cast<CuteQQuickPathViewPrivateCall15>(taken[15]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall16 call = reinterpret_cast<CuteQQuickPathViewPrivateCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall17 call = reinterpret_cast<CuteQQuickPathViewPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall18 call = reinterpret_cast<CuteQQuickPathViewPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPathViewPrivateCall19 call = reinterpret_cast<CuteQQuickPathViewPrivateCall19>(taken[19]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickPathView *QQuickPathViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickPathView *ritual_ZN21QQuickPathViewPrivate6q_funcEv(
    QQuickPathViewPrivate *self) {
  return self->q_func();
}

//  const QQuickPathView *QQuickPathViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickPathView *ritual_ZNK21QQuickPathViewPrivate6q_funcEv(
    const QQuickPathViewPrivate *self) {
  return self->q_func();
}

//  QQuickPathViewPrivate::QQuickPathViewPrivate()
extern "C" Q_DECL_EXPORT
QQuickPathViewPrivate *ritual_ZN21QQuickPathViewPrivateC1Ev() {
  return new CuteQQuickPathViewPrivate();
}

//  void QQuickPathViewPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate4initEv(QQuickPathViewPrivate *self) {
  self->init();
}

//  void QQuickPathViewPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickPathViewPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *a2) {
  self->itemGeometryChanged(item, *change, *a2);
}

//  void QQuickPathViewPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate13itemDestroyedEP10QQuickItem(
    QQuickPathViewPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  void QQuickPathViewPrivate::scheduleLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate14scheduleLayoutEv(
    QQuickPathViewPrivate *self) {
  self->scheduleLayout();
}

//  QQuickItem *QQuickPathViewPrivate::getItem(int modelIndex, qreal z, bool
//      async)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN21QQuickPathViewPrivate7getItemEidb(
    QQuickPathViewPrivate *self,
    int modelIndex,
    qreal z,
    bool async) {
  return self->getItem(modelIndex, z, async);
}

//  void QQuickPathViewPrivate::releaseCurrentItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate18releaseCurrentItemEv(
    QQuickPathViewPrivate *self) {
  self->releaseCurrentItem();
}

//  void QQuickPathViewPrivate::releaseItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate11releaseItemEP10QQuickItem(
    QQuickPathViewPrivate *self,
    QQuickItem *item) {
  self->releaseItem(item);
}

//  QQuickPathViewAttached *QQuickPathViewPrivate::attached(QQuickItem *item)
extern "C" Q_DECL_EXPORT
QQuickPathViewAttached *ritual_ZN21QQuickPathViewPrivate8attachedEP10QQuickItem(
    QQuickPathViewPrivate *self,
    QQuickItem *item) {
  return self->attached(item);
}

//  QQmlOpenMetaObjectType *QQuickPathViewPrivate::attachedType()
extern "C" Q_DECL_EXPORT
QQmlOpenMetaObjectType *ritual_ZN21QQuickPathViewPrivate12attachedTypeEv(
    QQuickPathViewPrivate *self) {
  return self->attachedType();
}

//  void QQuickPathViewPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate5clearEv(QQuickPathViewPrivate *self) {
  self->clear();
}

//  void QQuickPathViewPrivate::updateMappedRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate17updateMappedRangeEv(
    QQuickPathViewPrivate *self) {
  self->updateMappedRange();
}

//  qreal QQuickPathViewPrivate::positionOfIndex(qreal index) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickPathViewPrivate15positionOfIndexEd(
    const QQuickPathViewPrivate *self,
    qreal index) {
  return self->positionOfIndex(index);
}

//  bool QQuickPathViewPrivate::isInBound(qreal position, qreal lower, qreal
//      upper, bool emptyRangeCheck) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickPathViewPrivate9isInBoundEdddb(
    const QQuickPathViewPrivate *self,
    qreal position,
    qreal lower,
    qreal upper,
    bool emptyRangeCheck) {
  return self->isInBound(position, lower, upper, emptyRangeCheck);
}

//  void QQuickPathViewPrivate::createHighlight()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate15createHighlightEv(
    QQuickPathViewPrivate *self) {
  self->createHighlight();
}

//  void QQuickPathViewPrivate::updateHighlight()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate15updateHighlightEv(
    QQuickPathViewPrivate *self) {
  self->updateHighlight();
}

//  void QQuickPathViewPrivate::setHighlightPosition(qreal pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate20setHighlightPositionEd(
    QQuickPathViewPrivate *self,
    qreal pos) {
  self->setHighlightPosition(pos);
}

//  bool QQuickPathViewPrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickPathViewPrivate7isValidEv(
    const QQuickPathViewPrivate *self) {
  return self->isValid();
}

//  void QQuickPathViewPrivate::handleMousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate21handleMousePressEventEP11QMouseEvent(
    QQuickPathViewPrivate *self,
    QMouseEvent *event) {
  self->handleMousePressEvent(event);
}

//  int QQuickPathViewPrivate::calcCurrentIndex()
extern "C" Q_DECL_EXPORT
int ritual_ZN21QQuickPathViewPrivate16calcCurrentIndexEv(
    QQuickPathViewPrivate *self) {
  return self->calcCurrentIndex();
}

//  void QQuickPathViewPrivate::createCurrentItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate17createCurrentItemEv(
    QQuickPathViewPrivate *self) {
  self->createCurrentItem();
}

//  void QQuickPathViewPrivate::updateCurrent()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate13updateCurrentEv(
    QQuickPathViewPrivate *self) {
  self->updateCurrent();
}

//  void QQuickPathViewPrivate::fixOffsetCallback(void *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate17fixOffsetCallbackEPv(void *a0) {
  QQuickPathViewPrivate::fixOffsetCallback(a0);
}

//  void QQuickPathViewPrivate::fixOffset()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate9fixOffsetEv(
    QQuickPathViewPrivate *self) {
  self->fixOffset();
}

//  void QQuickPathViewPrivate::setOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate9setOffsetEd(
    QQuickPathViewPrivate *self,
    qreal offset) {
  self->setOffset(offset);
}

//  void QQuickPathViewPrivate::setAdjustedOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate17setAdjustedOffsetEd(
    QQuickPathViewPrivate *self,
    qreal offset) {
  self->setAdjustedOffset(offset);
}

//  void QQuickPathViewPrivate::regenerate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate10regenerateEv(
    QQuickPathViewPrivate *self) {
  self->regenerate();
}

//  void QQuickPathViewPrivate::updateItem(QQuickItem *a0, qreal a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate10updateItemEP10QQuickItemd(
    QQuickPathViewPrivate *self,
    QQuickItem *a0,
    qreal a1) {
  self->updateItem(a0, a1);
}

//  void QQuickPathViewPrivate::snapToIndex(int index, MovementReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate11snapToIndexEiNS_14MovementReasonE(
    QQuickPathViewPrivate *self,
    int index,
    QQuickPathViewPrivate::MovementReason reason) {
  self->snapToIndex(index, reason);
}

//  QPointF QQuickPathViewPrivate::pointNear(const QPointF &point, qreal
//      *nearPercent) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK21QQuickPathViewPrivate9pointNearERK7QPointFPd(
    const QQuickPathViewPrivate *self,
    const QPointF *point,
    qreal *nearPercent) {
  return new QPointF(self->pointNear(*point, nearPercent));
}

//  qint64 QQuickPathViewPrivate::computeCurrentTime(QInputEvent *event)
//      const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QQuickPathViewPrivate18computeCurrentTimeEP11QInputEvent(
    const QQuickPathViewPrivate *self,
    QInputEvent *event) {
  return self->computeCurrentTime(event);
}

//  void QQuickPathViewPrivate::setDragging(bool d)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickPathViewPrivate11setDraggingEb(
    QQuickPathViewPrivate *self,
    bool d) {
  self->setDragging(d);
}

//  a Python function taken by a CuteQQuickPathViewPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPathViewPrivate(
    QQuickPathViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPathViewPrivate *>(self)->take(key, call);
}

//  void QQuickPathViewPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickPathViewPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickPathViewPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *a2) {
  self->QQuickPathViewPrivate::itemGeometryChanged(item, *change, *a2);
}

//  void QQuickPathViewPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickPathViewPrivate13itemDestroyedEP10QQuickItem(
    QQuickPathViewPrivate *self,
    QQuickItem *item) {
  self->QQuickPathViewPrivate::itemDestroyed(item);
}

#endif  // QT_CONFIG(quick_pathview)
#endif  // QT_CONFIG(quick_pathview)
