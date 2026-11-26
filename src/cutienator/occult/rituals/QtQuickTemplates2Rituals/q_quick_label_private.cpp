//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicklabel_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicklabel_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicklabel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmargins.h>
#include <QtGui/qfont.h>
#include <QtCore/qstring.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquicklabel_p.h>
#include <QtQuickTemplates2/private/qquicklabel_p_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p_p.h>
#include <QtQuickTemplates2/private/qquickdeferredexecute_p_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qquicktext_p.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/private/qquickaccessibleattached_p.h>
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

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 51, as _ZN18QQuickLabelPrivateC1Ev
inline QQuickLabelPrivate::QQuickLabelPrivate()
{
#if QT_CONFIG(accessibility)
    QAccessible::installActivationObserver(this);
    setAccessible();
#endif
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 59, as _ZN18QQuickLabelPrivateD1Ev
inline QQuickLabelPrivate::~QQuickLabelPrivate()
{
#if QT_CONFIG(accessibility)
    QAccessible::removeActivationObserver(this);
#endif
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 66, as _ZN18QQuickLabelPrivate11setTopInsetEdb
inline void QQuickLabelPrivate::setTopInset(qreal value, bool reset)
{
    Q_Q(QQuickLabel);
    const QMarginsF oldInset = getInset();
    extra.value().topInset = value;
    extra.value().hasTopInset = !reset;
    if (!qFuzzyCompare(oldInset.top(), value)) {
        emit q->topInsetChanged();
        q->insetChange(getInset(), oldInset);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 78, as _ZN18QQuickLabelPrivate12setLeftInsetEdb
inline void QQuickLabelPrivate::setLeftInset(qreal value, bool reset)
{
    Q_Q(QQuickLabel);
    const QMarginsF oldInset = getInset();
    extra.value().leftInset = value;
    extra.value().hasLeftInset = !reset;
    if (!qFuzzyCompare(oldInset.left(), value)) {
        emit q->leftInsetChanged();
        q->insetChange(getInset(), oldInset);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 90, as _ZN18QQuickLabelPrivate13setRightInsetEdb
inline void QQuickLabelPrivate::setRightInset(qreal value, bool reset)
{
    Q_Q(QQuickLabel);
    const QMarginsF oldInset = getInset();
    extra.value().rightInset = value;
    extra.value().hasRightInset = !reset;
    if (!qFuzzyCompare(oldInset.right(), value)) {
        emit q->rightInsetChanged();
        q->insetChange(getInset(), oldInset);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 102, as _ZN18QQuickLabelPrivate14setBottomInsetEdb
inline void QQuickLabelPrivate::setBottomInset(qreal value, bool reset)
{
    Q_Q(QQuickLabel);
    const QMarginsF oldInset = getInset();
    extra.value().bottomInset = value;
    extra.value().hasBottomInset = !reset;
    if (!qFuzzyCompare(oldInset.bottom(), value)) {
        emit q->bottomInsetChanged();
        q->insetChange(getInset(), oldInset);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 114, as _ZN18QQuickLabelPrivate16resizeBackgroundEv
inline void QQuickLabelPrivate::resizeBackground()
{
    if (!background)
        return;

    resizingBackground = true;

    QQuickItemPrivate *p = QQuickItemPrivate::get(background);
    if (((!p->widthValid() || !extra.isAllocated() || !extra->hasBackgroundWidth) && qFuzzyIsNull(background->x()))
            || (extra.isAllocated() && (extra->hasLeftInset || extra->hasRightInset))) {
        background->setX(getLeftInset());
        background->setWidth(width - getLeftInset() - getRightInset());
    }
    if (((!p->heightValid() || !extra.isAllocated() || !extra->hasBackgroundHeight) && qFuzzyIsNull(background->y()))
            || (extra.isAllocated() && (extra->hasTopInset || extra->hasBottomInset))) {
        background->setY(getTopInset());
        background->setHeight(height - getTopInset() - getBottomInset());
    }

    resizingBackground = false;
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 144, as _ZN18QQuickLabelPrivate11resolveFontEv
inline void QQuickLabelPrivate::resolveFont()
{
    Q_Q(QQuickLabel);
    inheritFont(QQuickControlPrivate::parentFont(q));
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 150, as _ZN18QQuickLabelPrivate11inheritFontERK5QFont
inline void QQuickLabelPrivate::inheritFont(const QFont &font)
{
    QFont parentFont = extra.isAllocated() ? extra->requestedFont.resolve(font) : font;
    parentFont.setResolveMask(extra.isAllocated() ? extra->requestedFont.resolveMask() | font.resolveMask() : font.resolveMask());

    const QFont defaultFont = QQuickTheme::font(QQuickTheme::Label);
    QFont resolvedFont = parentFont.resolve(defaultFont);

    setFont_helper(resolvedFont);
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 166, as _ZN18QQuickLabelPrivate10updateFontERK5QFont
inline void QQuickLabelPrivate::updateFont(const QFont &font)
{
    Q_Q(QQuickLabel);
    QFont oldFont = sourceFont;
    q->QQuickText::setFont(font);

    QQuickControlPrivate::updateFontRecur(q, font);

    if (oldFont != font)
        emit q->fontChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 178, as _ZN18QQuickLabelPrivate11textChangedERK7QString
inline void QQuickLabelPrivate::textChanged(const QString &text)
{
#if QT_CONFIG(accessibility)
    maybeSetAccessibleName(text);
#else
    Q_UNUSED(text);
#endif
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 188, as _ZN18QQuickLabelPrivate26accessibilityActiveChangedEb
#if QT_CONFIG(accessibility)
inline void QQuickLabelPrivate::accessibilityActiveChanged(bool active)
{
    if (!active)
        return;

    Q_Q(QQuickLabel);
    QQuickAccessibleAttached *accessibleAttached = qobject_cast<QQuickAccessibleAttached *>(qmlAttachedPropertiesObject<QQuickAccessibleAttached>(q, true));
    Q_ASSERT(accessibleAttached);
    accessibleAttached->setRole(effectiveAccessibleRole());
    maybeSetAccessibleName(text);
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 200, as _ZNK18QQuickLabelPrivate14accessibleRoleEv
#if QT_CONFIG(accessibility)
inline QAccessible::Role QQuickLabelPrivate::accessibleRole() const
{
    return QAccessible::StaticText;
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 205, as _ZN18QQuickLabelPrivate22maybeSetAccessibleNameERK7QString
#if QT_CONFIG(accessibility)
inline void QQuickLabelPrivate::maybeSetAccessibleName(const QString &name)
{
    Q_Q(QQuickLabel);
    auto accessibleAttached = qobject_cast<QQuickAccessibleAttached *>(
        qmlAttachedPropertiesObject<QQuickAccessibleAttached>(q, true));
    if (accessibleAttached) {
        if (!accessibleAttached->wasNameExplicitlySet())
            accessibleAttached->setNameImplicitly(name);
    }
}
#endif  // QT_CONFIG(accessibility)

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 217, as _ZN18QQuickLabelPrivate16cancelBackgroundEv
inline void QQuickLabelPrivate::cancelBackground()
{
    Q_Q(QQuickLabel);
    quickCancelDeferred(q, backgroundName());
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 223, as _ZN18QQuickLabelPrivate17executeBackgroundEb
inline void QQuickLabelPrivate::executeBackground(bool complete)
{
    Q_Q(QQuickLabel);
    if (background.wasExecuted())
        return;

    if (!background || complete)
        quickBeginDeferred(q, backgroundName(), background);
    if (complete)
        quickCompleteDeferred(q, backgroundName(), background);
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 235, as _ZN18QQuickLabelPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickLabelPrivate::itemGeometryChanged(QQuickItem *item, QQuickGeometryChange change, const QRectF &diff)
{
    Q_UNUSED(diff);
    if (resizingBackground || item != background || !change.sizeChange())
        return;

    QQuickItemPrivate *p = QQuickItemPrivate::get(item);
    extra.value().hasBackgroundWidth = p->widthValid();
    extra.value().hasBackgroundHeight = p->heightValid();
    resizeBackground();
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 247, as _ZN18QQuickLabelPrivate24itemImplicitWidthChangedEP10QQuickItem
inline void QQuickLabelPrivate::itemImplicitWidthChanged(QQuickItem *item)
{
    Q_Q(QQuickLabel);
    if (item == background)
        emit q->implicitBackgroundWidthChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 254, as _ZN18QQuickLabelPrivate25itemImplicitHeightChangedEP10QQuickItem
inline void QQuickLabelPrivate::itemImplicitHeightChanged(QQuickItem *item)
{
    Q_Q(QQuickLabel);
    if (item == background)
        emit q->implicitBackgroundHeightChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 261, as _ZN18QQuickLabelPrivate13itemDestroyedEP10QQuickItem
inline void QQuickLabelPrivate::itemDestroyed(QQuickItem *item)
{
    Q_Q(QQuickLabel);
    if (item == background) {
        background = nullptr;
        emit q->implicitBackgroundWidthChanged();
        emit q->implicitBackgroundHeightChanged();
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquicklabel.cpp, line 271, as _ZNK18QQuickLabelPrivate14defaultPaletteEv
inline QPalette QQuickLabelPrivate::defaultPalette() const
{
    return QQuickTheme::palette(QQuickTheme::Label);
}
//  -----------------------------------------------------------------------

//  A QQuickLabelPrivate that Python can take functions over in. Every QQuickLabelPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickLabelPrivateCall0)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickLabelPrivateCall1)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickLabelPrivateCall2)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickLabelPrivateCall3)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLabelPrivateCall4)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLabelPrivateCall5)(const void *, QQuickItem *, int *);
typedef const QPalette * (*CuteQQuickLabelPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickLabelPrivateCall7)(const void *, int *);
typedef bool (*CuteQQuickLabelPrivateCall8)(const void *, QQuickItem *, int *);
typedef qreal (*CuteQQuickLabelPrivateCall9)(const void *, int *);
typedef qreal (*CuteQQuickLabelPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickLabelPrivateCall11)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickLabelPrivateCall12)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickLabelPrivateCall13)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickLabelPrivateCall14)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickLabelPrivateCall15)(const void *, int, int *);
typedef void (*CuteQQuickLabelPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickLabelPrivateCall17)(const void *, int *);
typedef bool (*CuteQQuickLabelPrivateCall18)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickLabelPrivateCall19)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickLabelPrivateCall20)(const void *, bool, int *);
typedef void * (*CuteQQuickLabelPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickLabelPrivateCall22)(const void *, int *);
typedef void (*CuteQQuickLabelPrivateCall23)(const void *, int, int *);
class CuteQQuickLabelPrivate : public QQuickLabelPrivate {
public:
  using QQuickLabelPrivate::QQuickLabelPrivate;
  void *taken[24] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN18QQuickLabelPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickLabelPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickLabelPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN18QQuickLabelPrivate13itemDestroyedEP10QQuickItem")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK18QQuickLabelPrivate14defaultPaletteEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[18] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[23] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(accessibility)
  //  void QQuickLabelPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall0 call = reinterpret_cast<CuteQQuickLabelPrivateCall0>(taken[0]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickLabelPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickLabelPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall1 call = reinterpret_cast<CuteQQuickLabelPrivateCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickLabelPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickLabelPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall2 call = reinterpret_cast<CuteQQuickLabelPrivateCall2>(taken[2]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickLabelPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickLabelPrivate::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall3 call = reinterpret_cast<CuteQQuickLabelPrivateCall3>(taken[3]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLabelPrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickLabelPrivate::itemImplicitHeightChanged(QQuickItem *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall4 call = reinterpret_cast<CuteQQuickLabelPrivateCall4>(taken[4]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLabelPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickLabelPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall5 call = reinterpret_cast<CuteQQuickLabelPrivateCall5>(taken[5]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickLabelPrivate::itemDestroyed(item);
  }

  //  QPalette QQuickLabelPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall6 call = reinterpret_cast<CuteQQuickLabelPrivateCall6>(taken[6]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickLabelPrivate::defaultPalette();
  }

  //  void QQuickTextPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall7 call = reinterpret_cast<CuteQQuickLabelPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextPrivate::mirrorChange();
  }

  //  bool QQuickTextPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall8 call = reinterpret_cast<CuteQQuickLabelPrivateCall8>(taken[8]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickTextPrivate::transformChanged(transformedItem);
  }

  //  qreal QQuickTextPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall9 call = reinterpret_cast<CuteQQuickLabelPrivateCall9>(taken[9]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTextPrivate::getImplicitWidth();
  }

  //  qreal QQuickTextPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall10 call = reinterpret_cast<CuteQQuickLabelPrivateCall10>(taken[10]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTextPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall11 call = reinterpret_cast<CuteQQuickLabelPrivateCall11>(taken[11]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall12 call = reinterpret_cast<CuteQQuickLabelPrivateCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall13 call = reinterpret_cast<CuteQQuickLabelPrivateCall13>(taken[13]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall14 call = reinterpret_cast<CuteQQuickLabelPrivateCall14>(taken[14]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall15 call = reinterpret_cast<CuteQQuickLabelPrivateCall15>(taken[15]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall16 call = reinterpret_cast<CuteQQuickLabelPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall17 call = reinterpret_cast<CuteQQuickLabelPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall18 call = reinterpret_cast<CuteQQuickLabelPrivateCall18>(taken[18]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall19 call = reinterpret_cast<CuteQQuickLabelPrivateCall19>(taken[19]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall20 call = reinterpret_cast<CuteQQuickLabelPrivateCall20>(taken[20]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall21 call = reinterpret_cast<CuteQQuickLabelPrivateCall21>(taken[21]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall22 call = reinterpret_cast<CuteQQuickLabelPrivateCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickLabelPrivateCall23 call = reinterpret_cast<CuteQQuickLabelPrivateCall23>(taken[23]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickLabel *QQuickLabelPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickLabel *ritual_ZN18QQuickLabelPrivate6q_funcEv(
    QQuickLabelPrivate *self) {
  return self->q_func();
}

//  const QQuickLabel *QQuickLabelPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickLabel *ritual_ZNK18QQuickLabelPrivate6q_funcEv(
    const QQuickLabelPrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(accessibility)
//  QQuickLabelPrivate::QQuickLabelPrivate()
extern "C" Q_DECL_EXPORT
QQuickLabelPrivate *ritual_ZN18QQuickLabelPrivateC1Ev() {
  return new CuteQQuickLabelPrivate();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickLabelPrivate::~QQuickLabelPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivateD1Ev(QQuickLabelPrivate *self) {
  delete self;
}

//  QQuickLabelPrivate *QQuickLabelPrivate::get(QQuickLabel *item)
extern "C" Q_DECL_EXPORT
QQuickLabelPrivate *ritual_ZN18QQuickLabelPrivate3getEP11QQuickLabel(
    QQuickLabel *item) {
  return QQuickLabelPrivate::get(item);
}

//  QMarginsF QQuickLabelPrivate::getInset() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK18QQuickLabelPrivate8getInsetEv(
    const QQuickLabelPrivate *self) {
  return new QMarginsF(self->getInset());
}

//  qreal QQuickLabelPrivate::getTopInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickLabelPrivate11getTopInsetEv(
    const QQuickLabelPrivate *self) {
  return self->getTopInset();
}

//  qreal QQuickLabelPrivate::getLeftInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickLabelPrivate12getLeftInsetEv(
    const QQuickLabelPrivate *self) {
  return self->getLeftInset();
}

//  qreal QQuickLabelPrivate::getRightInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickLabelPrivate13getRightInsetEv(
    const QQuickLabelPrivate *self) {
  return self->getRightInset();
}

//  qreal QQuickLabelPrivate::getBottomInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickLabelPrivate14getBottomInsetEv(
    const QQuickLabelPrivate *self) {
  return self->getBottomInset();
}

//  void QQuickLabelPrivate::setTopInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate11setTopInsetEdb(
    QQuickLabelPrivate *self,
    qreal value,
    bool reset) {
  self->setTopInset(value, reset);
}

//  void QQuickLabelPrivate::setLeftInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate12setLeftInsetEdb(
    QQuickLabelPrivate *self,
    qreal value,
    bool reset) {
  self->setLeftInset(value, reset);
}

//  void QQuickLabelPrivate::setRightInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate13setRightInsetEdb(
    QQuickLabelPrivate *self,
    qreal value,
    bool reset) {
  self->setRightInset(value, reset);
}

//  void QQuickLabelPrivate::setBottomInset(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate14setBottomInsetEdb(
    QQuickLabelPrivate *self,
    qreal value,
    bool reset) {
  self->setBottomInset(value, reset);
}

//  void QQuickLabelPrivate::resizeBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate16resizeBackgroundEv(
    QQuickLabelPrivate *self) {
  self->resizeBackground();
}

//  void QQuickLabelPrivate::resolveFont()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate11resolveFontEv(QQuickLabelPrivate *self) {
  self->resolveFont();
}

//  void QQuickLabelPrivate::inheritFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate11inheritFontERK5QFont(
    QQuickLabelPrivate *self,
    const QFont *font) {
  self->inheritFont(*font);
}

//  void QQuickLabelPrivate::updateFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate10updateFontERK5QFont(
    QQuickLabelPrivate *self,
    const QFont *font) {
  self->updateFont(*font);
}

//  void QQuickLabelPrivate::setFont_helper(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate14setFont_helperERK5QFont(
    QQuickLabelPrivate *self,
    const QFont *font) {
  self->setFont_helper(*font);
}

#if QT_CONFIG(accessibility)
//  void QQuickLabelPrivate::textChanged(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate11textChangedERK7QString(
    QQuickLabelPrivate *self,
    const QString *text) {
  self->textChanged(*text);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickLabelPrivate::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate26accessibilityActiveChangedEb(
    QQuickLabelPrivate *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickLabelPrivate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK18QQuickLabelPrivate14accessibleRoleEv(
    const QQuickLabelPrivate *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QQuickLabelPrivate::maybeSetAccessibleName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate22maybeSetAccessibleNameERK7QString(
    QQuickLabelPrivate *self,
    const QString *name) {
  self->maybeSetAccessibleName(*name);
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickLabelPrivate::cancelBackground()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate16cancelBackgroundEv(
    QQuickLabelPrivate *self) {
  self->cancelBackground();
}

//  void QQuickLabelPrivate::executeBackground(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate17executeBackgroundEb(
    QQuickLabelPrivate *self,
    bool complete) {
  self->executeBackground(complete);
}

//  void QQuickLabelPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickLabelPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->itemGeometryChanged(item, *change, *diff);
}

//  void QQuickLabelPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickLabelPrivate *self,
    QQuickItem *item) {
  self->itemImplicitWidthChanged(item);
}

//  void QQuickLabelPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickLabelPrivate *self,
    QQuickItem *item) {
  self->itemImplicitHeightChanged(item);
}

//  void QQuickLabelPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickLabelPrivate13itemDestroyedEP10QQuickItem(
    QQuickLabelPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  QPalette QQuickLabelPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK18QQuickLabelPrivate14defaultPaletteEv(
    const QQuickLabelPrivate *self) {
  return new QPalette(self->defaultPalette());
}

//  QQuickLabelPrivate as the QAccessible::ActivationObserver it is built on
extern "C" Q_DECL_EXPORT
QAccessible::ActivationObserver *ritual_cast_QQuickLabelPrivate_QAccessible_ActivationObserver(
    QQuickLabelPrivate *self) {
  return static_cast<QAccessible::ActivationObserver *>(self);
}

//  a Python function taken by a CuteQQuickLabelPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLabelPrivate(
    QQuickLabelPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLabelPrivate *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
//  void QQuickLabelPrivate::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickLabelPrivate26accessibilityActiveChangedEb(
    QQuickLabelPrivate *self,
    bool active) {
  self->QQuickLabelPrivate::accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickLabelPrivate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK18QQuickLabelPrivate14accessibleRoleEv(
    const QQuickLabelPrivate *self) {
  return self->QQuickLabelPrivate::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickLabelPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickLabelPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickLabelPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->QQuickLabelPrivate::itemGeometryChanged(item, *change, *diff);
}

//  void QQuickLabelPrivate::itemImplicitWidthChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickLabelPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickLabelPrivate *self,
    QQuickItem *item) {
  self->QQuickLabelPrivate::itemImplicitWidthChanged(item);
}

//  void QQuickLabelPrivate::itemImplicitHeightChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickLabelPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickLabelPrivate *self,
    QQuickItem *item) {
  self->QQuickLabelPrivate::itemImplicitHeightChanged(item);
}

//  void QQuickLabelPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQuickLabelPrivate13itemDestroyedEP10QQuickItem(
    QQuickLabelPrivate *self,
    QQuickItem *item) {
  self->QQuickLabelPrivate::itemDestroyed(item);
}

//  QPalette QQuickLabelPrivate::defaultPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_own_ZNK18QQuickLabelPrivate14defaultPaletteEv(
    const QQuickLabelPrivate *self) {
  return new QPalette(self->QQuickLabelPrivate::defaultPalette());
}
