//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktooltip_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktooltip_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktooltip_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquicktooltip_p.h>
#include <QtQuickTemplates2/private/qquicktooltip_p_p.h>
#include <QtQuickTemplates2/private/qquickpopup_p_p.h>
#include <QtQuickTemplates2/private/qquickpopupitem_p_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p_p.h>
#include <QtCore/qbasictimer.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQuick/qquickwindow.h>
#include <QtCore/q26numeric.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquicktooltip.cpp, line 373, as _ZNK28QQuickToolTipAttachedPrivate8instanceEb
inline QQuickToolTip *QQuickToolTipAttachedPrivate::instance(bool create) const
{
    QQmlEngine *engine = qmlEngine(parent);
    if (!engine)
        return nullptr;

    // QQuickAttachedPropertyPropagator uses "_q_QQuickToolTip", so we add "shared_"
    // to make this unique.
    static const char *name = "_q_shared_QQuickToolTip";

    QQuickToolTip *tip = engine->property(name).value<QQuickToolTip *>();
    if (!tip && create) {
        QQmlComponent component(engine, "QtQuick.Controls", "ToolTip");

        QObject *object = component.create();
        if (object)
            object->setParent(engine);

        tip = qobject_cast<QQuickToolTip *>(object);
        if (!tip)
            delete object;
        else
            engine->setProperty(name, QVariant::fromValue(object));
    }
    return tip;
}

//  from ../qtdeclarative/src/quicktemplates/qquicktooltip.cpp, line 400, as _ZN28QQuickToolTipAttachedPrivate25maybeSetVisibleImplicitlyEPK7QObjectb
inline void QQuickToolTipAttachedPrivate::maybeSetVisibleImplicitly(
    const QObject *attachee, bool visible)
{
    auto *toolTipAttached = qobject_cast<QQuickToolTipAttached *>(
        qmlAttachedPropertiesObject<QQuickToolTip>(attachee, false));
    // Not using an attached tool tip.
    if (!toolTipAttached)
        return;

    auto *toolTipAttachedPrivate = toolTipAttached->d_func();
    // Don't interfere if the user has set ToolTip.visible explicitly or if they've
    // set a manual policy.
    if (toolTipAttachedPrivate->isVisibleExplicitlySet()
            || toolTipAttachedPrivate->policy == QQuickToolTip::Manual) {
        return;
    }

    // Don't show ourselves if we have no text. We save calling code having to get our text and
    // instead just test it here.
    const bool effectiveVisible = visible ? visible && !toolTipAttachedPrivate->text.isEmpty() : false;
    toolTipAttachedPrivate->setVisible(effectiveVisible, QQml::PropertyUtils::State::ImplicitlySet);
}

//  from ../qtdeclarative/src/quicktemplates/qquicktooltip.cpp, line 423, as _ZN28QQuickToolTipAttachedPrivate10setVisibleEbN4QQml13PropertyUtils5StateE
inline void QQuickToolTipAttachedPrivate::setVisible(bool visible, QQml::PropertyUtils::State propertyState)
{
    Q_Q(QQuickToolTipAttached);
    if (warnIfAttacheeIsNotAnItem(QStringLiteral("setVisible")))
        return;

    explicitVisible = isExplicitlySet(propertyState);

    if (!complete && visible) {
        pendingShow = true;
        return;
    }

    if (visible)
        q->show(text);
    else
        q->hide();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktooltip.cpp, line 442, as _ZNK28QQuickToolTipAttachedPrivate22isVisibleExplicitlySetEv
inline bool QQuickToolTipAttachedPrivate::isVisibleExplicitlySet() const
{
    return explicitVisible;
}

//  from ../qtdeclarative/src/quicktemplates/qquicktooltip.cpp, line 447, as _ZN28QQuickToolTipAttachedPrivate8setDelayEiN4QQml13PropertyUtils5StateE
inline void QQuickToolTipAttachedPrivate::setDelay(int delay, QQml::PropertyUtils::State propertyState)
{
    Q_Q(QQuickToolTipAttached);
    if (warnIfAttacheeIsNotAnItem(QStringLiteral("setDelay")))
        return;

    explicitDelay = isExplicitlySet(propertyState);

    if (this->delay == delay)
        return;

    this->delay = delay;
    emit q->delayChanged();

    if (q->isVisible())
        instance(true)->setDelay(delay);
}

//  from ../qtdeclarative/src/quicktemplates/qquicktooltip.cpp, line 465, as _ZNK28QQuickToolTipAttachedPrivate20isDelayExplicitlySetEv
inline bool QQuickToolTipAttachedPrivate::isDelayExplicitlySet() const
{
    return explicitDelay;
}

//  from ../qtdeclarative/src/quicktemplates/qquicktooltip.cpp, line 470, as _ZN28QQuickToolTipAttachedPrivate10setTimeoutEiN4QQml13PropertyUtils5StateE
inline void QQuickToolTipAttachedPrivate::setTimeout(int timeout, QQml::PropertyUtils::State propertyState)
{
    Q_Q(QQuickToolTipAttached);
    if (warnIfAttacheeIsNotAnItem(QStringLiteral("setTimeout")))
        return;

    explicitTimeout = isExplicitlySet(propertyState);

    if (this->timeout == timeout)
        return;

    this->timeout = timeout;
    emit q->timeoutChanged();

    if (q->isVisible())
        instance(true)->setTimeout(timeout);
}

//  from ../qtdeclarative/src/quicktemplates/qquicktooltip.cpp, line 488, as _ZNK28QQuickToolTipAttachedPrivate22isTimeoutExplicitlySetEv
inline bool QQuickToolTipAttachedPrivate::isTimeoutExplicitlySet() const
{
    return explicitTimeout;
}

//  from ../qtdeclarative/src/quicktemplates/qquicktooltip.cpp, line 493, as _ZN28QQuickToolTipAttachedPrivate13inheritPolicyEN13QQuickToolTip6PolicyE
inline void QQuickToolTipAttachedPrivate::inheritPolicy(QQuickToolTip::Policy policy)
{
    Q_Q(QQuickToolTipAttached);
    if (this->policy == policy)
        return;

    this->policy = policy;
    propagatePolicy();
    emit q->policyChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquicktooltip.cpp, line 504, as _ZN28QQuickToolTipAttachedPrivate15propagatePolicyEv
inline void QQuickToolTipAttachedPrivate::propagatePolicy()
{
    Q_Q(QQuickToolTipAttached);
    const auto attachedToolTipChildren = q->attachedChildren();
    for (QtPrivate::QQuickAttachedPropertyPropagator *child : attachedToolTipChildren) {
        auto *attachedToolTipChild = qobject_cast<QQuickToolTipAttached *>(child);
        if (attachedToolTipChild)
            attachedToolTipChild->d_func()->inheritPolicy(policy);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicktooltip.cpp, line 523, as _ZN28QQuickToolTipAttachedPrivate25warnIfAttacheeIsNotAnItemERK7QString
inline bool QQuickToolTipAttachedPrivate::warnIfAttacheeIsNotAnItem(const QString &functionName)
{
    QQuickItem *item = qobject_cast<QQuickItem *>(parent);
    if (Q_LIKELY(item))
        return false;

    qmlWarning(parent).nospace().noquote() << "The attached function ToolTip::" << functionName
        << " can only be called when the attachee derives from Item";
    return true;
}
//  -----------------------------------------------------------------------

//  A QQuickToolTipAttachedPrivate that Python can take functions over in. Every QQuickToolTipAttachedPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickToolTipAttachedPrivateCall0)(const void *, QQuickItem *, QQuickItem *, int *);
class CuteQQuickToolTipAttachedPrivate : public QQuickToolTipAttachedPrivate {
public:
  using QQuickToolTipAttachedPrivate::QQuickToolTipAttachedPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QtPrivate39QQuickAttachedPropertyPropagatorPrivate17itemParentChangedEP10QQuickItemS2_")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QtPrivate::QQuickAttachedPropertyPropagatorPrivate::itemParentCh
  //      anged(QQuickItem *item, QQuickItem *parent)
  void itemParentChanged(QQuickItem *item, QQuickItem *parent) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickToolTipAttachedPrivateCall0 call = reinterpret_cast<CuteQQuickToolTipAttachedPrivateCall0>(taken[0]);
      call(this, item, parent, &handled);
      if (handled) return;
    }
    QtPrivate::QQuickAttachedPropertyPropagatorPrivate::itemParentChanged(item, parent);
  }
};

//  QQuickToolTipAttached *QQuickToolTipAttachedPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickToolTipAttached *ritual_ZN28QQuickToolTipAttachedPrivate6q_funcEv(
    QQuickToolTipAttachedPrivate *self) {
  return self->q_func();
}

//  const QQuickToolTipAttached *QQuickToolTipAttachedPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickToolTipAttached *ritual_ZNK28QQuickToolTipAttachedPrivate6q_funcEv(
    const QQuickToolTipAttachedPrivate *self) {
  return self->q_func();
}

//  QQuickToolTip *QQuickToolTipAttachedPrivate::instance(bool create) const
extern "C" Q_DECL_EXPORT
QQuickToolTip *ritual_ZNK28QQuickToolTipAttachedPrivate8instanceEb(
    const QQuickToolTipAttachedPrivate *self,
    bool create) {
  return self->instance(create);
}

//  QQuickToolTipAttachedPrivate
//      *QQuickToolTipAttachedPrivate::get(QQuickToolTipAttached
//      *toolTipAttached)
extern "C" Q_DECL_EXPORT
QQuickToolTipAttachedPrivate *ritual_ZN28QQuickToolTipAttachedPrivate3getEP21QQuickToolTipAttached(
    QQuickToolTipAttached *toolTipAttached) {
  return QQuickToolTipAttachedPrivate::get(toolTipAttached);
}

//  void QQuickToolTipAttachedPrivate::maybeSetVisibleImplicitly(const
//      QObject *attachee, bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickToolTipAttachedPrivate25maybeSetVisibleImplicitlyEPK7QObjectb(
    const QObject *attachee,
    bool visible) {
  QQuickToolTipAttachedPrivate::maybeSetVisibleImplicitly(attachee, visible);
}

//  void QQuickToolTipAttachedPrivate::setVisible(bool visible,
//      QQml::PropertyUtils::State propertyState)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickToolTipAttachedPrivate10setVisibleEbN4QQml13PropertyUtils5StateE(
    QQuickToolTipAttachedPrivate *self,
    bool visible,
    QQml::PropertyUtils::State propertyState) {
  self->setVisible(visible, propertyState);
}

//  bool QQuickToolTipAttachedPrivate::isVisibleExplicitlySet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QQuickToolTipAttachedPrivate22isVisibleExplicitlySetEv(
    const QQuickToolTipAttachedPrivate *self) {
  return self->isVisibleExplicitlySet();
}

//  void QQuickToolTipAttachedPrivate::setDelay(int delay,
//      QQml::PropertyUtils::State propertyState)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickToolTipAttachedPrivate8setDelayEiN4QQml13PropertyUtils5StateE(
    QQuickToolTipAttachedPrivate *self,
    int delay,
    QQml::PropertyUtils::State propertyState) {
  self->setDelay(delay, propertyState);
}

//  bool QQuickToolTipAttachedPrivate::isDelayExplicitlySet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QQuickToolTipAttachedPrivate20isDelayExplicitlySetEv(
    const QQuickToolTipAttachedPrivate *self) {
  return self->isDelayExplicitlySet();
}

//  void QQuickToolTipAttachedPrivate::setTimeout(int timeout,
//      QQml::PropertyUtils::State propertyState)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickToolTipAttachedPrivate10setTimeoutEiN4QQml13PropertyUtils5StateE(
    QQuickToolTipAttachedPrivate *self,
    int timeout,
    QQml::PropertyUtils::State propertyState) {
  self->setTimeout(timeout, propertyState);
}

//  bool QQuickToolTipAttachedPrivate::isTimeoutExplicitlySet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QQuickToolTipAttachedPrivate22isTimeoutExplicitlySetEv(
    const QQuickToolTipAttachedPrivate *self) {
  return self->isTimeoutExplicitlySet();
}

//  void QQuickToolTipAttachedPrivate::inheritPolicy(QQuickToolTip::Policy
//      policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickToolTipAttachedPrivate13inheritPolicyEN13QQuickToolTip6PolicyE(
    QQuickToolTipAttachedPrivate *self,
    QQuickToolTip::Policy policy) {
  self->inheritPolicy(policy);
}

//  void QQuickToolTipAttachedPrivate::propagatePolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickToolTipAttachedPrivate15propagatePolicyEv(
    QQuickToolTipAttachedPrivate *self) {
  self->propagatePolicy();
}

//  bool QQuickToolTipAttachedPrivate::warnIfAttacheeIsNotAnItem(const
//      QString &functionName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QQuickToolTipAttachedPrivate25warnIfAttacheeIsNotAnItemERK7QString(
    QQuickToolTipAttachedPrivate *self,
    const QString *functionName) {
  return self->warnIfAttacheeIsNotAnItem(*functionName);
}

//  a Python function taken by a CuteQQuickToolTipAttachedPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickToolTipAttachedPrivate(
    QQuickToolTipAttachedPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickToolTipAttachedPrivate *>(self)->take(key, call);
}
