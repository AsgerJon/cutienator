//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickstackelement_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickstackelement_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickstackview_p_p.h"
#include "qquickstackelement_p_p.h"
#if QT_CONFIG(quick_viewtransitions)
#include "qquickstacktransition_p_p.h"
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
#include "qquickstackelement_p_p.h"
#include "qquickstackview_p.h"
#include "qquickstackview_p_p.h"
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/qqmlincubator.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlincubator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickstackview_p.cpp, line 23, as _ZN22QQuickStackViewPrivate4warnERK7QString
inline void QQuickStackViewPrivate::warn(const QString &error)
{
    Q_Q(QQuickStackView);
    if (operation.isEmpty())
        qmlWarning(q) << error;
    else
        qmlWarning(q) << operation << ": " << error;
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackelement.cpp, line 195, as _ZN18QQuickStackElement8incubateEPN3QV415ExecutionEngineEP7QObjectP18RequiredProperties
inline void QQuickStackElement::incubate(
        QV4::ExecutionEngine *v4, QObject *object, RequiredProperties *requiredProperties)
{
    item = qmlobject_cast<QQuickItem *>(object);
    if (item) {
        QQmlEngine::setObjectOwnership(item, QQmlEngine::CppOwnership);
        item->setParent(view);
        initialize(v4, requiredProperties);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackelement.cpp, line 206, as _ZN18QQuickStackElement10initializeEPN3QV415ExecutionEngineEP18RequiredProperties
inline void QQuickStackElement::initialize(
        QV4::ExecutionEngine *v4, RequiredProperties *requiredProperties)
{
    if (!item || init)
        return;

    QQuickItemPrivate *p = QQuickItemPrivate::get(item);
    if (!(widthValid = p->widthValid()))
        item->setWidth(view->width());
    if (!(heightValid = p->heightValid()))
        item->setHeight(view->height());
    item->setParentItem(view);

    if (!properties.isUndefined()) {
        QV4::Scope scope(v4);
        Q_ASSERT(scope.engine);
        QV4::ScopedValue ipv(scope, properties.value());
        QV4::Scoped<QV4::QmlContext> qmlContext(scope, qmlCallingContext.value());
        QV4::ScopedValue qmlObject(scope, QV4::QObjectWrapper::wrap(scope.engine, item));
        QQmlComponentPrivate::setInitialProperties(
            scope.engine, qmlContext, qmlObject, ipv, requiredProperties, item,
            component ? QQmlComponentPrivate::get(component)->creator() : nullptr);
        properties.clear();
    }

    if (requiredProperties && !requiredProperties->empty()) {
        QString error;
        for (const auto &property: *requiredProperties) {
            error += QLatin1String("Property %1 was marked as required but not set.\n")
                    .arg(property.propertyName);
        }
        QQuickStackViewPrivate::get(view)->warn(error);
        item = nullptr;
    } else {
        p->addItemChangeListener(this, QQuickItemPrivate::Destroyed);
    }

    init = true;
}

//  from ../qtdeclarative/src/quicktemplates/qquickstackelement.cpp, line 321, as _ZN18QQuickStackElement24transitionNextRepositionEP26QQuickItemViewTransitionerNS0_14TransitionTypeEb
#if QT_CONFIG(quick_viewtransitions)
inline void QQuickStackElement::transitionNextReposition(QQuickItemViewTransitioner *transitioner, QQuickItemViewTransitioner::TransitionType type, bool asTarget)
{
    if (transitioner)
        transitioner->transitionNextReposition(this, type, asTarget);
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

//  from ../qtdeclarative/src/quicktemplates/qquickstackelement.cpp, line 359, as _ZN18QQuickStackElement13itemDestroyedEP10QQuickItem
inline void QQuickStackElement::itemDestroyed(QQuickItem *)
{
#if QT_CONFIG(quick_viewtransitions)
    item = nullptr;
#endif
}
//  -----------------------------------------------------------------------

//  A QQuickStackElement that Python can take functions over in. Every QQuickStackElement
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickStackElementCall0)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall1)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickStackElementCall2)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall3)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall4)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall5)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall6)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall7)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall8)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall9)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall10)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall11)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall12)(const void *, QQuickItem *, int, int *);
typedef void (*CuteQQuickStackElementCall13)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall14)(const void *, QQuickItem *, QQuickItem *, int *);
typedef void * (*CuteQQuickStackElementCall15)(const void *, int *);
typedef bool (*CuteQQuickStackElementCall16)(const void *, const QObject *, int *);
typedef QString * (*CuteQQuickStackElementCall17)(const void *, int *);
typedef void (*CuteQQuickStackElementCall18)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickStackElementCall19)(const void *, QQuickItem *, int *);
class CuteQQuickStackElement : public QQuickStackElement {
public:
  using QQuickStackElement::QQuickStackElement;
  CuteQQuickStackElement(const QQuickStackElement &other) : QQuickStackElement(other) {}
  void *taken[20] = {};

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
    return false;
  }

  //  void QQuickStackElement::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickStackElementCall0 call = reinterpret_cast<CuteQQuickStackElementCall0>(taken[0]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickStackElement::itemDestroyed(item);
  }

  //  void QQuickItemChangeListener::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange a1, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange a1,
      const QRectF &a2) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickStackElementCall1 call = reinterpret_cast<CuteQQuickStackElementCall1>(taken[1]);
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
      CuteQQuickStackElementCall2 call = reinterpret_cast<CuteQQuickStackElementCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemSiblingOrderChanged(a0);
  }

  //  void QQuickItemChangeListener::itemVisibilityChanged(QQuickItem *a0)
  void itemVisibilityChanged(QQuickItem *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickStackElementCall3 call = reinterpret_cast<CuteQQuickStackElementCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemVisibilityChanged(a0);
  }

  //  void QQuickItemChangeListener::itemEnabledChanged(QQuickItem *a0)
  void itemEnabledChanged(QQuickItem *a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickStackElementCall4 call = reinterpret_cast<CuteQQuickStackElementCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemEnabledChanged(a0);
  }

  //  void QQuickItemChangeListener::itemOpacityChanged(QQuickItem *a0)
  void itemOpacityChanged(QQuickItem *a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickStackElementCall5 call = reinterpret_cast<CuteQQuickStackElementCall5>(taken[5]);
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
      CuteQQuickStackElementCall6 call = reinterpret_cast<CuteQQuickStackElementCall6>(taken[6]);
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
      CuteQQuickStackElementCall7 call = reinterpret_cast<CuteQQuickStackElementCall7>(taken[7]);
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
      CuteQQuickStackElementCall8 call = reinterpret_cast<CuteQQuickStackElementCall8>(taken[8]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemParentChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemRotationChanged(QQuickItem *a0)
  void itemRotationChanged(QQuickItem *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickStackElementCall9 call = reinterpret_cast<CuteQQuickStackElementCall9>(taken[9]);
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
      CuteQQuickStackElementCall10 call = reinterpret_cast<CuteQQuickStackElementCall10>(taken[10]);
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
      CuteQQuickStackElementCall11 call = reinterpret_cast<CuteQQuickStackElementCall11>(taken[11]);
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
      CuteQQuickStackElementCall12 call = reinterpret_cast<CuteQQuickStackElementCall12>(taken[12]);
      call(this, a0, static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemFocusChanged(a0, a1);
  }

  //  void QQuickItemChangeListener::itemScaleChanged(QQuickItem *a0)
  void itemScaleChanged(QQuickItem *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickStackElementCall13 call = reinterpret_cast<CuteQQuickStackElementCall13>(taken[13]);
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
      CuteQQuickStackElementCall14 call = reinterpret_cast<CuteQQuickStackElementCall14>(taken[14]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::itemTransformChanged(a0, a1);
  }

  //  QQuickAnchorsPrivate *QQuickItemChangeListener::anchorPrivate()
  QQuickAnchorsPrivate *anchorPrivate() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickStackElementCall15 call = reinterpret_cast<CuteQQuickStackElementCall15>(taken[15]);
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
      CuteQQuickStackElementCall16 call = reinterpret_cast<CuteQQuickStackElementCall16>(taken[16]);
      bool given = call(this, caller, &handled);
      if (handled) return given;
    }
    return QQuickItemChangeListener::baseDeleted(caller);
  }

  //  QString QQuickItemChangeListener::debugName() const
  QString debugName() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickStackElementCall17 call = reinterpret_cast<CuteQQuickStackElementCall17>(taken[17]);
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
      CuteQQuickStackElementCall18 call = reinterpret_cast<CuteQQuickStackElementCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::addSourceItem(a0);
  }

  //  void QQuickItemChangeListener::removeSourceItem(QQuickItem *a0)
  void removeSourceItem(QQuickItem *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickStackElementCall19 call = reinterpret_cast<CuteQQuickStackElementCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItemChangeListener::removeSourceItem(a0);
  }
};

//  void QQuickStackElement::incubate(QV4::ExecutionEngine *v4, QObject
//      *object, RequiredProperties *requiredProperties)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStackElement8incubateEPN3QV415ExecutionEngineEP7QObjectP18RequiredProperties(
    QQuickStackElement *self,
    QV4::ExecutionEngine *v4,
    QObject *object,
    RequiredProperties *requiredProperties) {
  self->incubate(v4, object, requiredProperties);
}

//  void QQuickStackElement::initialize(QV4::ExecutionEngine *v4,
//      RequiredProperties *requiredProperties)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStackElement10initializeEPN3QV415ExecutionEngineEP18RequiredProperties(
    QQuickStackElement *self,
    QV4::ExecutionEngine *v4,
    RequiredProperties *requiredProperties) {
  self->initialize(v4, requiredProperties);
}

#if QT_CONFIG(quick_viewtransitions)
//  void
//      QQuickStackElement::transitionNextReposition(QQuickItemViewTransition
//      er *transitioner, QQuickItemViewTransitioner::TransitionType type,
//      bool asTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStackElement24transitionNextRepositionEP26QQuickItemViewTransitionerNS0_14TransitionTypeEb(
    QQuickStackElement *self,
    QQuickItemViewTransitioner *transitioner,
    QQuickItemViewTransitioner::TransitionType type,
    bool asTarget) {
  self->transitionNextReposition(transitioner, type, asTarget);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  bool QQuickStackElement::prepareTransition(QQuickItemViewTransitioner
//      *transitioner, const QRectF &viewBounds)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QQuickStackElement17prepareTransitionEP26QQuickItemViewTransitionerRK6QRectF(
    QQuickStackElement *self,
    QQuickItemViewTransitioner *transitioner,
    const QRectF *viewBounds) {
  return self->prepareTransition(transitioner, *viewBounds);
}
#endif  // QT_CONFIG(quick_viewtransitions)

#if QT_CONFIG(quick_viewtransitions)
//  void QQuickStackElement::completeTransition(QQuickTransition
//      *quickTransition)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStackElement18completeTransitionEP16QQuickTransition(
    QQuickStackElement *self,
    QQuickTransition *quickTransition) {
  self->completeTransition(quickTransition);
}
#endif  // QT_CONFIG(quick_viewtransitions)

//  void QQuickStackElement::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickStackElement13itemDestroyedEP10QQuickItem(
    QQuickStackElement *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  QQuickStackElement as the QQuickItemChangeListener it is built on
extern "C" Q_DECL_EXPORT
QQuickItemChangeListener *ritual_cast_QQuickStackElement_QQuickItemChangeListener(
    QQuickStackElement *self) {
  return static_cast<QQuickItemChangeListener *>(self);
}

//  a Python function taken by a CuteQQuickStackElement, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickStackElement(
    QQuickStackElement *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickStackElement *>(self)->take(key, call);
}

//  void QQuickStackElement::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickStackElement13itemDestroyedEP10QQuickItem(
    QQuickStackElement *self,
    QQuickItem *item) {
  self->QQuickStackElement::itemDestroyed(item);
}

//  QList<QQuickStackElement *>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuickStackElement *> *ritual_list_make_QQuickStackElement_ptr() {
  return new QList<QQuickStackElement *>();
}

//  void QList<QQuickStackElement *>::append(const QQuickStackElement *
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuickStackElement_ptr(
    QList<QQuickStackElement *> *self,
    QQuickStackElement *element) {
  self->append(element);
}

//  qsizetype QList<QQuickStackElement *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuickStackElement_ptr(
    const QList<QQuickStackElement *> *self) {
  return self->size();
}

//  const QQuickStackElement * &QList<QQuickStackElement *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QQuickStackElement *ritual_list_at_QQuickStackElement_ptr(
    const QList<QQuickStackElement *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QQuickStackElement *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuickStackElement_ptr(
    QList<QQuickStackElement *> *self) {
  delete self;
}
