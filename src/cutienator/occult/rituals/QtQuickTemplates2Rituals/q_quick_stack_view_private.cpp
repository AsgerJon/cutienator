//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackview_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qpoint.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickstackelement_p_p.h>
#include <QtQuickTemplates2/private/qquickstackview_p.h>
#include <QtQuickTemplates2/private/qquickstackview_p_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/qqmlincubator.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlincubator_p.h>
#include <QtQuickTemplates2/private/qquickstackview_p_p.h>
#include <QtQuickTemplates2/private/qquickstackelement_p_p.h>
#if QT_CONFIG(quick_viewtransitions)
#include <QtQuickTemplates2/private/qquickstacktransition_p_p.h>
#endif
#include <QtCore/qscopedvaluerollback.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmllist.h>
#include <QtQml/private/qv4qmlcontext_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4variantobject_p.h>
#include <QtQml/private/qv4urlobject_p.h>
#include <QtQuick/private/qquickanimation_p.h>
#include <QtQuick/private/qquicktransition_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickstackelement.cpp, line 135, as _ZN18QQuickStackElement16fromStackViewArgEP10QQmlEngineP15QQuickStackView18QQuickStackViewArg
inline QQuickStackElement *QQuickStackElement::fromStackViewArg(
        QQmlEngine *engine, QQuickStackView *view, QQuickStackViewArg arg)
{
    QQuickStackElement *element = new QQuickStackElement;
#if QT_CONFIG(quick_viewtransitions)
    element->item = arg.mItem;
    if (element->item) {
        element->originalParent = element->item->parentItem();

        Q_ASSERT(!arg.mComponent);
        Q_ASSERT(!arg.mUrl.isValid());
    } else
#endif
    if (arg.mComponent) {
        element->component = arg.mComponent;

        Q_ASSERT(!arg.mUrl.isValid());
    } else if (arg.mUrl.isValid()) {
        element->component = new QQmlComponent(engine, arg.mUrl, view);
        element->ownComponent = true;
    } else {
        qFatal("No Item, Component or URL set on arg passed to fromStrictArg");
    }
    return element;
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackelement.cpp, line 346, as _ZN18QQuickStackElement15startTransitionEP26QQuickItemViewTransitionerN15QQuickStackView6StatusE
#if QT_CONFIG(quick_viewtransitions)
inline void QQuickStackElement::startTransition(QQuickItemViewTransitioner *transitioner, QQuickStackView::Status status)
{
    setStatus(status);
    if (transitioner)
        QQuickItemViewTransitionableItem::startTransition(transitioner, index);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  from ../qtdeclarative/src/quicktemplates/qquickstackelement.cpp, line 327, as _ZN18QQuickStackElement17prepareTransitionEP26QQuickItemViewTransitionerRK6QRectF
#if QT_CONFIG(quick_viewtransitions)
inline bool QQuickStackElement::prepareTransition(QQuickItemViewTransitioner *transitioner, const QRectF &viewBounds)
{
    if (transitioner) {
        if (item) {
            QQuickAnchors *anchors = QQuickItemPrivate::get(item)->_anchors;
            // TODO: expose QQuickAnchorLine so we can test for other conflicting anchors
            if (anchors && (anchors->fill() || anchors->centerIn()))
                qmlWarning(item) << "StackView has detected conflicting anchors. Transitions may not execute properly.";
        }

        // TODO: add force argument to QQuickItemViewTransitionableItem::prepareTransition()?
        nextTransitionToSet = true;
        nextTransitionFromSet = true;
        nextTransitionFrom += QPointF(1, 1);
        return QQuickItemViewTransitionableItem::prepareTransition(transitioner, index, viewBounds);
    }
    return false;
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  from ../qtdeclarative/src/quicktemplates/qquickstackelement.cpp, line 353, as _ZN18QQuickStackElement18completeTransitionEP16QQuickTransition
#if QT_CONFIG(quick_viewtransitions)
inline void QQuickStackElement::completeTransition(QQuickTransition *quickTransition)
{
    QQuickItemViewTransitionableItem::completeTransition(quickTransition);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  from ../qtdeclarative/src/quicktemplates/qquickstackelement.cpp, line 321, as _ZN18QQuickStackElement24transitionNextRepositionEP26QQuickItemViewTransitionerNS0_14TransitionTypeEb
#if QT_CONFIG(quick_viewtransitions)
inline void QQuickStackElement::transitionNextReposition(QQuickItemViewTransitioner *transitioner, QQuickItemViewTransitioner::TransitionType type, bool asTarget)
{
    if (transitioner)
        transitioner->transitionNextReposition(this, type, asTarget);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  from ../qtdeclarative/src/quicktemplates/qquickstackelement.cpp, line 53, as _ZN18QQuickStackElementC1Ev
inline QQuickStackElement::QQuickStackElement()
#if QT_CONFIG(quick_viewtransitions)
    : QQuickItemViewTransitionableItem(nullptr)
#endif
{
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackview_p.cpp, line 23, as _ZN22QQuickStackViewPrivate4warnERK7QString
inline void QQuickStackViewPrivate::warn(const QString &error)
{
    Q_Q(QQuickStackView);
    if (operation.isEmpty())
        qmlWarning(q) << error;
    else
        qmlWarning(q) << operation << ": " << error;
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackview_p.cpp, line 32, as _ZN22QQuickStackViewPrivate18warnOfInterruptionERK7QString
inline void QQuickStackViewPrivate::warnOfInterruption(const QString &attemptedOperation)
{
    Q_Q(QQuickStackView);
    qmlWarning(q) << "cannot " << attemptedOperation << " while already in the process of completing a " << operation;
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackview_p.cpp, line 155, as _ZNK22QQuickStackViewPrivate11findElementEP10QQuickItem
inline QQuickStackElement *QQuickStackViewPrivate::findElement(QQuickItem *item) const
{
    if (item) {
        for (QQuickStackElement *e : std::as_const(elements)) {
            if (e->item == item)
                return e;
        }
    }
    return nullptr;
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackview_p.cpp, line 166, as _ZNK22QQuickStackViewPrivate11findElementERKN3QV45ValueE
inline QQuickStackElement *QQuickStackViewPrivate::findElement(const QV4::Value &value) const
{
    if (const QV4::QObjectWrapper *o = value.as<QV4::QObjectWrapper>())
        return findElement(qobject_cast<QQuickItem *>(o->object()));
    return nullptr;
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackview_p.cpp, line 336, as _ZN22QQuickStackViewPrivate18ensureTransitionerEv
#if QT_CONFIG(quick_viewtransitions)
inline void QQuickStackViewPrivate::ensureTransitioner()
{
    if (!transitioner) {
        transitioner = new QQuickItemViewTransitioner;
        transitioner->setChangeListener(this);
    }
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  from ../qtdeclarative/src/quicktemplates/qquickstackview_p.cpp, line 395, as _ZN22QQuickStackViewPrivate26viewItemTransitionFinishedEP32QQuickItemViewTransitionableItem
#if QT_CONFIG(quick_viewtransitions)
inline void QQuickStackViewPrivate::viewItemTransitionFinished(QQuickItemViewTransitionableItem *transitionable)
{
    QQuickStackElement *element = static_cast<QQuickStackElement *>(transitionable);
    if (element->status == QQuickStackView::Activating) {
        element->setStatus(QQuickStackView::Active);
    } else if (element->status == QQuickStackView::Deactivating) {
        element->setStatus(QQuickStackView::Inactive);
        QQuickStackElement *existingElement = element->item ? findElement(element->item) : nullptr;
        // If a different element with the same item is found,
        // do not call setVisible(false) since it needs to be visible.
        if (!existingElement || element == existingElement)
            element->setVisible(false);
        if (element->removal || element->isPendingRemoval())
            removed += element;
    }

    if (transitioner && transitioner->runningJobs.isEmpty()) {
        // ~QQuickStackElement() emits QQuickStackViewAttached::removed(), which may be used
        // to modify the stack. Set the status first and make a copy of the destroyable stack
        // elements to exclude any modifications that may happen during qDeleteAll(). (QTBUG-62153)
        setBusy(false);
        QList<QQuickStackElement*> removedElements = removed;
        removed.clear();

        for (QQuickStackElement *removedElement : std::as_const(removedElements)) {
            // If an element with the same item is found in the active stack list,
            // forget about the item so that we don't hide it.
            if (removedElement->item && findElement(removedElement->item)) {
                QQuickItemPrivate::get(removedElement->item)->removeItemChangeListener(removedElement, QQuickItemPrivate::Destroyed);
                removedElement->item = nullptr;
            }
        }

        qDeleteAll(removedElements);
    }

    removing.remove(element);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  from ../qtdeclarative/src/quicktemplates/qquickstackview_p.cpp, line 435, as _ZN22QQuickStackViewPrivate7setBusyEb
inline void QQuickStackViewPrivate::setBusy(bool b)
{
    Q_Q(QQuickStackView);
    if (busy == b)
        return;

    busy = b;
    q->setFiltersChildMouseEvents(busy);
    emit q->busyChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackview_p.cpp, line 446, as _ZN22QQuickStackViewPrivate11depthChangeEii
inline void QQuickStackViewPrivate::depthChange(int newDepth, int oldDepth)
{
    Q_Q(QQuickStackView);
    if (newDepth == oldDepth)
        return;

    emit q->depthChanged();
    if (newDepth == 0 || oldDepth == 0)
        emit q->emptyChanged();
}
//  -----------------------------------------------------------------------

//  A QQuickStackViewPrivate that Python can take functions over in. Every QQuickStackViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_viewtransitions)
typedef void (*CuteQQuickStackViewPrivateCall0)(const void *, QQuickItemViewTransitionableItem *, int *);
#endif  // QT_CONFIG(quick_viewtransitions)
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickStackViewPrivateCall1)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickStackViewPrivateCall2)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickStackViewPrivateCall3)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickStackViewPrivateCall4)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickStackViewPrivateCall5)(const void *, int *);
typedef void (*CuteQQuickStackViewPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickStackViewPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickStackViewPrivateCall8)(const void *, int *);
typedef void * (*CuteQQuickStackViewPrivateCall9)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickStackViewPrivateCall10)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickStackViewPrivateCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickStackViewPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickStackViewPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickStackViewPrivateCall14)(const void *, bool, int *);
typedef void (*CuteQQuickStackViewPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickStackViewPrivateCall16)(const void *, bool, int *);
typedef void (*CuteQQuickStackViewPrivateCall17)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackViewPrivateCall18)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackViewPrivateCall19)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickStackViewPrivateCall20)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackViewPrivateCall21)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickStackViewPrivateCall22)(const void *, int, int *);
typedef qreal (*CuteQQuickStackViewPrivateCall23)(const void *, int *);
typedef qreal (*CuteQQuickStackViewPrivateCall24)(const void *, int *);
typedef const QPalette * (*CuteQQuickStackViewPrivateCall25)(const void *, int *);
typedef void (*CuteQQuickStackViewPrivateCall26)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickStackViewPrivateCall27)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickStackViewPrivateCall28)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickStackViewPrivateCall29)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickStackViewPrivateCall30)(const void *, int *);
typedef qreal (*CuteQQuickStackViewPrivateCall31)(const void *, int *);
typedef void (*CuteQQuickStackViewPrivateCall32)(const void *, int *);
typedef void (*CuteQQuickStackViewPrivateCall33)(const void *, int *);
typedef bool (*CuteQQuickStackViewPrivateCall34)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickStackViewPrivateCall35)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickStackViewPrivateCall36)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickStackViewPrivateCall37)(const void *, bool, int *);
typedef void * (*CuteQQuickStackViewPrivateCall38)(const void *, int *);
typedef void (*CuteQQuickStackViewPrivateCall39)(const void *, int *);
typedef void (*CuteQQuickStackViewPrivateCall40)(const void *, int, int *);
class CuteQQuickStackViewPrivate : public QQuickStackViewPrivate {
public:
  using QQuickStackViewPrivate::QQuickStackViewPrivate;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_viewtransitions)
    if (!std::strcmp(key, "_ZN38QQuickItemViewTransitionChangeListener26viewItemTransitionFinishedEP32QQuickItemViewTransitionableItem")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_viewtransitions)
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
      taken[9] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11resolveFontEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17cancelContentItemEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate18executeContentItemEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16cancelBackgroundEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17executeBackgroundEb")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate15getContentWidthEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate16getContentHeightEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate14defaultPaletteEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[35] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[40] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(quick_viewtransitions)
  //  void QQuickStackViewPrivate::viewItemTransitionFinished(QQuickItemVie
  //      wTransitionableItem *item)
  void viewItemTransitionFinished(
      QQuickItemViewTransitionableItem *item) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall0 call = reinterpret_cast<CuteQQuickStackViewPrivateCall0>(taken[0]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickStackViewPrivate::viewItemTransitionFinished(item);
  }
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall1 call = reinterpret_cast<CuteQQuickStackViewPrivateCall1>(taken[1]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickControlPrivate::handlePress(const QPointF &point, ulong
  //      timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall2 call = reinterpret_cast<CuteQQuickStackViewPrivateCall2>(taken[2]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleMove(const QPointF &point, ulong
  //      timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall3 call = reinterpret_cast<CuteQQuickStackViewPrivateCall3>(taken[3]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleRelease(const QPointF &point, ulong
  //      timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall4 call = reinterpret_cast<CuteQQuickStackViewPrivateCall4>(taken[4]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickControlPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall5 call = reinterpret_cast<CuteQQuickStackViewPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::handleUngrab();
  }

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall6 call = reinterpret_cast<CuteQQuickStackViewPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall7 call = reinterpret_cast<CuteQQuickStackViewPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  void QQuickControlPrivate::resizeContent()
  void resizeContent() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall8 call = reinterpret_cast<CuteQQuickStackViewPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeContent();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall9 call = reinterpret_cast<CuteQQuickStackViewPrivateCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickControlPrivate::getContentItem();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall10 call = reinterpret_cast<CuteQQuickStackViewPrivateCall10>(taken[10]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControlPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall11 call = reinterpret_cast<CuteQQuickStackViewPrivateCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControlPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControlPrivate::resolveFont()
  void resolveFont() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall12 call = reinterpret_cast<CuteQQuickStackViewPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall13 call = reinterpret_cast<CuteQQuickStackViewPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall14 call = reinterpret_cast<CuteQQuickStackViewPrivateCall14>(taken[14]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall15 call = reinterpret_cast<CuteQQuickStackViewPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall16 call = reinterpret_cast<CuteQQuickStackViewPrivateCall16>(taken[16]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeBackground(complete);
  }

  //  void QQuickControlPrivate::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall17 call = reinterpret_cast<CuteQQuickStackViewPrivateCall17>(taken[17]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickControlPrivate::itemImplicitHeightChanged(QQuickItem
  //      *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall18 call = reinterpret_cast<CuteQQuickStackViewPrivateCall18>(taken[18]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickControlPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall19 call = reinterpret_cast<CuteQQuickStackViewPrivateCall19>(taken[19]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickControlPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall20 call = reinterpret_cast<CuteQQuickStackViewPrivateCall20>(taken[20]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemDestroyed(item);
  }

  //  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
  //      Qt::FocusReason reason)
  void itemFocusChanged(QQuickItem *item, Qt::FocusReason reason) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall21 call = reinterpret_cast<CuteQQuickStackViewPrivateCall21>(taken[21]);
      call(this, item, static_cast<int>(reason), &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemFocusChanged(item, reason);
  }

  //  bool QQuickControlPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      a0)
  bool setLastFocusChangeReason(Qt::FocusReason a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall22 call = reinterpret_cast<CuteQQuickStackViewPrivateCall22>(taken[22]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  qreal QQuickControlPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall23 call = reinterpret_cast<CuteQQuickStackViewPrivateCall23>(taken[23]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentWidth();
  }

  //  qreal QQuickControlPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall24 call = reinterpret_cast<CuteQQuickStackViewPrivateCall24>(taken[24]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentHeight();
  }

  //  QPalette QQuickControlPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall25 call = reinterpret_cast<CuteQQuickStackViewPrivateCall25>(taken[25]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControlPrivate::defaultPalette();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall26 call = reinterpret_cast<CuteQQuickStackViewPrivateCall26>(taken[26]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall27 call = reinterpret_cast<CuteQQuickStackViewPrivateCall27>(taken[27]);
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
    if (taken[28]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall28 call = reinterpret_cast<CuteQQuickStackViewPrivateCall28>(taken[28]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall29 call = reinterpret_cast<CuteQQuickStackViewPrivateCall29>(taken[29]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall30 call = reinterpret_cast<CuteQQuickStackViewPrivateCall30>(taken[30]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall31 call = reinterpret_cast<CuteQQuickStackViewPrivateCall31>(taken[31]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall32 call = reinterpret_cast<CuteQQuickStackViewPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall33 call = reinterpret_cast<CuteQQuickStackViewPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall34 call = reinterpret_cast<CuteQQuickStackViewPrivateCall34>(taken[34]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall35 call = reinterpret_cast<CuteQQuickStackViewPrivateCall35>(taken[35]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall36 call = reinterpret_cast<CuteQQuickStackViewPrivateCall36>(taken[36]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall37 call = reinterpret_cast<CuteQQuickStackViewPrivateCall37>(taken[37]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall38 call = reinterpret_cast<CuteQQuickStackViewPrivateCall38>(taken[38]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall39 call = reinterpret_cast<CuteQQuickStackViewPrivateCall39>(taken[39]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickStackViewPrivateCall40 call = reinterpret_cast<CuteQQuickStackViewPrivateCall40>(taken[40]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickStackView *QQuickStackViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickStackView *ritual_ZN22QQuickStackViewPrivate6q_funcEv(
    QQuickStackViewPrivate *self) {
  return self->q_func();
}

//  const QQuickStackView *QQuickStackViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickStackView *ritual_ZNK22QQuickStackViewPrivate6q_funcEv(
    const QQuickStackViewPrivate *self) {
  return self->q_func();
}

//  QQuickStackViewPrivate *QQuickStackViewPrivate::get(QQuickStackView
//      *view)
extern "C" Q_DECL_EXPORT
QQuickStackViewPrivate *ritual_ZN22QQuickStackViewPrivate3getEP15QQuickStackView(
    QQuickStackView *view) {
  return QQuickStackViewPrivate::get(view);
}

//  void QQuickStackViewPrivate::warn(const QString &error)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStackViewPrivate4warnERK7QString(
    QQuickStackViewPrivate *self,
    const QString *error) {
  self->warn(*error);
}

//  void QQuickStackViewPrivate::warnOfInterruption(const QString
//      &attemptedOperation)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStackViewPrivate18warnOfInterruptionERK7QString(
    QQuickStackViewPrivate *self,
    const QString *attemptedOperation) {
  self->warnOfInterruption(*attemptedOperation);
}

//  QQuickStackElement *QQuickStackViewPrivate::findElement(QQuickItem *item)
//      const
extern "C" Q_DECL_EXPORT
QQuickStackElement *ritual_ZNK22QQuickStackViewPrivate11findElementEP10QQuickItem(
    const QQuickStackViewPrivate *self,
    QQuickItem *item) {
  return self->findElement(item);
}

//  QQuickStackElement *QQuickStackViewPrivate::findElement(const QV4::Value
//      &value) const
extern "C" Q_DECL_EXPORT
QQuickStackElement *ritual_ZNK22QQuickStackViewPrivate11findElementERKN3QV45ValueE(
    const QQuickStackViewPrivate *self,
    const QV4::Value *value) {
  return self->findElement(*value);
}

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickStackViewPrivate::ensureTransitioner()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStackViewPrivate18ensureTransitionerEv(
    QQuickStackViewPrivate *self) {
  self->ensureTransitioner();
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickStackViewPrivate::viewItemTransitionFinished(QQuickItemViewTra
//      nsitionableItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStackViewPrivate26viewItemTransitionFinishedEP32QQuickItemViewTransitionableItem(
    QQuickStackViewPrivate *self,
    QQuickItemViewTransitionableItem *item) {
  self->viewItemTransitionFinished(item);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  void QQuickStackViewPrivate::setBusy(bool busy)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStackViewPrivate7setBusyEb(
    QQuickStackViewPrivate *self,
    bool busy) {
  self->setBusy(busy);
}

//  void QQuickStackViewPrivate::depthChange(int newDepth, int oldDepth)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStackViewPrivate11depthChangeEii(
    QQuickStackViewPrivate *self,
    int newDepth,
    int oldDepth) {
  self->depthChange(newDepth, oldDepth);
}

//  QQuickStackViewPrivate as the QQuickItemViewTransitionChangeListener it
//      is built on
extern "C" Q_DECL_EXPORT
QQuickItemViewTransitionChangeListener *ritual_cast_QQuickStackViewPrivate_QQuickItemViewTransitionChangeListener(
    QQuickStackViewPrivate *self) {
  return static_cast<QQuickItemViewTransitionChangeListener *>(self);
}

//  a Python function taken by a CuteQQuickStackViewPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickStackViewPrivate(
    QQuickStackViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickStackViewPrivate *>(self)->take(key, call);
}
