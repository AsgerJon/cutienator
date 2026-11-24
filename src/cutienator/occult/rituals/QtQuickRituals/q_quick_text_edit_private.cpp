//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextedit_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextedit_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquicktextedit_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  A QQuickTextEditPrivate that Python can take functions over in. Every QQuickTextEditPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTextEditPrivateCall0)(const void *, int *);
typedef bool (*CuteQQuickTextEditPrivateCall1)(const void *, QQuickItem *, int *);
typedef qreal (*CuteQQuickTextEditPrivateCall2)(const void *, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickTextEditPrivateCall3)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickTextEditPrivateCall4)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickTextEditPrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickTextEditPrivateCall6)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickTextEditPrivateCall7)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickTextEditPrivateCall8)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickTextEditPrivateCall9)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickTextEditPrivateCall10)(const void *, int, int *);
typedef qreal (*CuteQQuickTextEditPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickTextEditPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickTextEditPrivateCall13)(const void *, int *);
typedef bool (*CuteQQuickTextEditPrivateCall14)(const void *, QPointerEvent *, bool, int *);
typedef void (*CuteQQuickTextEditPrivateCall15)(const void *, bool, int *);
typedef void * (*CuteQQuickTextEditPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickTextEditPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickTextEditPrivateCall18)(const void *, int, int *);
class CuteQQuickTextEditPrivate : public QQuickTextEditPrivate {
public:
  using QQuickTextEditPrivate::QQuickTextEditPrivate;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[2] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

  //  void QQuickTextEditPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall0 call = reinterpret_cast<CuteQQuickTextEditPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextEditPrivate::mirrorChange();
  }

  //  bool QQuickTextEditPrivate::transformChanged(QQuickItem
  //      *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall1 call = reinterpret_cast<CuteQQuickTextEditPrivateCall1>(taken[1]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickTextEditPrivate::transformChanged(transformedItem);
  }

  //  qreal QQuickTextEditPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall2 call = reinterpret_cast<CuteQQuickTextEditPrivateCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTextEditPrivate::getImplicitWidth();
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickTextEditPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall3 call = reinterpret_cast<CuteQQuickTextEditPrivateCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickTextEditPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_CONFIG(accessibility)
  //  void QQuickTextEditPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall4 call = reinterpret_cast<CuteQQuickTextEditPrivateCall4>(taken[4]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickTextEditPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickTextEditPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall5 call = reinterpret_cast<CuteQQuickTextEditPrivateCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickTextEditPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall6 call = reinterpret_cast<CuteQQuickTextEditPrivateCall6>(taken[6]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall7 call = reinterpret_cast<CuteQQuickTextEditPrivateCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall8 call = reinterpret_cast<CuteQQuickTextEditPrivateCall8>(taken[8]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall9 call = reinterpret_cast<CuteQQuickTextEditPrivateCall9>(taken[9]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall10 call = reinterpret_cast<CuteQQuickTextEditPrivateCall10>(taken[10]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall11 call = reinterpret_cast<CuteQQuickTextEditPrivateCall11>(taken[11]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall12 call = reinterpret_cast<CuteQQuickTextEditPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall13 call = reinterpret_cast<CuteQQuickTextEditPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall14 call = reinterpret_cast<CuteQQuickTextEditPrivateCall14>(taken[14]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall15 call = reinterpret_cast<CuteQQuickTextEditPrivateCall15>(taken[15]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall16 call = reinterpret_cast<CuteQQuickTextEditPrivateCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall17 call = reinterpret_cast<CuteQQuickTextEditPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTextEditPrivateCall18 call = reinterpret_cast<CuteQQuickTextEditPrivateCall18>(taken[18]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickTextEdit *QQuickTextEditPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickTextEdit *ritual_ZN21QQuickTextEditPrivate6q_funcEv(
    QQuickTextEditPrivate *self) {
  return self->q_func();
}

//  const QQuickTextEdit *QQuickTextEditPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextEdit *ritual_ZNK21QQuickTextEditPrivate6q_funcEv(
    const QQuickTextEditPrivate *self) {
  return self->q_func();
}

//  QQuickTextEditPrivate::QQuickTextEditPrivate()
extern "C" Q_DECL_EXPORT
QQuickTextEditPrivate *ritual_ZN21QQuickTextEditPrivateC1Ev() {
  return new CuteQQuickTextEditPrivate();
}

//  QQuickTextEditPrivate::~QQuickTextEditPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivateD1Ev(QQuickTextEditPrivate *self) {
  delete self;
}

//  QQuickTextEditPrivate *QQuickTextEditPrivate::get(QQuickTextEdit *item)
extern "C" Q_DECL_EXPORT
QQuickTextEditPrivate *ritual_ZN21QQuickTextEditPrivate3getEP14QQuickTextEdit(
    QQuickTextEdit *item) {
  return QQuickTextEditPrivate::get(item);
}

//  void QQuickTextEditPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate4initEv(QQuickTextEditPrivate *self) {
  self->init();
}

//  void QQuickTextEditPrivate::resetInputMethod()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate16resetInputMethodEv(
    QQuickTextEditPrivate *self) {
  self->resetInputMethod();
}

//  void QQuickTextEditPrivate::updateDefaultTextOption()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate23updateDefaultTextOptionEv(
    QQuickTextEditPrivate *self) {
  self->updateDefaultTextOption();
}

//  void QQuickTextEditPrivate::onDocumentStatusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate23onDocumentStatusChangedEv(
    QQuickTextEditPrivate *self) {
  self->onDocumentStatusChanged();
}

//  bool QQuickTextEditPrivate::determineHorizontalAlignment()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickTextEditPrivate28determineHorizontalAlignmentEv(
    QQuickTextEditPrivate *self) {
  return self->determineHorizontalAlignment();
}

//  bool QQuickTextEditPrivate::setHAlign(QQuickTextEdit::HAlignment a0, bool
//      forceAlign)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickTextEditPrivate9setHAlignEN14QQuickTextEdit10HAlignmentEb(
    QQuickTextEditPrivate *self,
    QQuickTextEdit::HAlignment a0,
    bool forceAlign) {
  return self->setHAlign(a0, forceAlign);
}

//  void QQuickTextEditPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate12mirrorChangeEv(
    QQuickTextEditPrivate *self) {
  self->mirrorChange();
}

//  bool QQuickTextEditPrivate::transformChanged(QQuickItem *transformedItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickTextEditPrivate16transformChangedEP10QQuickItem(
    QQuickTextEditPrivate *self,
    QQuickItem *transformedItem) {
  return self->transformChanged(transformedItem);
}

//  qreal QQuickTextEditPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTextEditPrivate16getImplicitWidthEv(
    const QQuickTextEditPrivate *self) {
  return self->getImplicitWidth();
}

//  Qt::LayoutDirection QQuickTextEditPrivate::textDirection(const QString
//      &text) const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK21QQuickTextEditPrivate13textDirectionERK7QString(
    const QQuickTextEditPrivate *self,
    const QString *text) {
  return self->textDirection(*text);
}

//  bool QQuickTextEditPrivate::isLinkHoveredConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickTextEditPrivate22isLinkHoveredConnectedEv(
    QQuickTextEditPrivate *self) {
  return self->isLinkHoveredConnected();
}

#if QT_CONFIG(cursor)
//  void QQuickTextEditPrivate::updateMouseCursorShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate22updateMouseCursorShapeEv(
    QQuickTextEditPrivate *self) {
  self->updateMouseCursorShape();
}
#endif  // QT_CONFIG(cursor)

//  void QQuickTextEditPrivate::setNativeCursorEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate22setNativeCursorEnabledEb(
    QQuickTextEditPrivate *self,
    bool a0) {
  self->setNativeCursorEnabled(a0);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  bool QQuickTextEditPrivate::handleContextMenuEvent(QContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickTextEditPrivate22handleContextMenuEventEP17QContextMenuEvent(
    QQuickTextEditPrivate *self,
    QContextMenuEvent *event) {
  return self->handleContextMenuEvent(event);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QQuickTextEditPrivate::handleFocusEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate16handleFocusEventEP11QFocusEvent(
    QQuickTextEditPrivate *self,
    QFocusEvent *event) {
  self->handleFocusEvent(event);
}

//  QSGInternalTextNode *QQuickTextEditPrivate::createTextNode()
extern "C" Q_DECL_EXPORT
QSGInternalTextNode *ritual_ZN21QQuickTextEditPrivate14createTextNodeEv(
    QQuickTextEditPrivate *self) {
  return self->createTextNode();
}

#if QT_CONFIG(im)
//  Qt::InputMethodHints QQuickTextEditPrivate::effectiveInputMethodHints()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickTextEditPrivate25effectiveInputMethodHintsEv(
    const QQuickTextEditPrivate *self) {
  return static_cast<int>(self->effectiveInputMethodHints().toInt());
}
#endif  // QT_CONFIG(im)

#if QT_CONFIG(accessibility)
//  void QQuickTextEditPrivate::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate26accessibilityActiveChangedEb(
    QQuickTextEditPrivate *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickTextEditPrivate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK21QQuickTextEditPrivate14accessibleRoleEv(
    const QQuickTextEditPrivate *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  qreal QQuickTextEditPrivate::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickTextEditPrivate7paddingEv(
    const QQuickTextEditPrivate *self) {
  return self->padding();
}

//  void QQuickTextEditPrivate::setTopPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate13setTopPaddingEdb(
    QQuickTextEditPrivate *self,
    qreal value,
    bool reset) {
  self->setTopPadding(value, reset);
}

//  void QQuickTextEditPrivate::setLeftPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate14setLeftPaddingEdb(
    QQuickTextEditPrivate *self,
    qreal value,
    bool reset) {
  self->setLeftPadding(value, reset);
}

//  void QQuickTextEditPrivate::setRightPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate15setRightPaddingEdb(
    QQuickTextEditPrivate *self,
    qreal value,
    bool reset) {
  self->setRightPadding(value, reset);
}

//  void QQuickTextEditPrivate::setBottomPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate16setBottomPaddingEdb(
    QQuickTextEditPrivate *self,
    qreal value,
    bool reset) {
  self->setBottomPadding(value, reset);
}

//  bool QQuickTextEditPrivate::isImplicitResizeEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickTextEditPrivate23isImplicitResizeEnabledEv(
    const QQuickTextEditPrivate *self) {
  return self->isImplicitResizeEnabled();
}

//  void QQuickTextEditPrivate::setImplicitResizeEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate24setImplicitResizeEnabledEb(
    QQuickTextEditPrivate *self,
    bool enabled) {
  self->setImplicitResizeEnabled(enabled);
}

//  QQuickTextEditPrivate as the QAccessible::ActivationObserver it is built
//      on
extern "C" Q_DECL_EXPORT
QAccessible::ActivationObserver *ritual_cast_QQuickTextEditPrivate_QAccessible_ActivationObserver(
    QQuickTextEditPrivate *self) {
  return static_cast<QAccessible::ActivationObserver *>(self);
}

//  a Python function taken by a CuteQQuickTextEditPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextEditPrivate(
    QQuickTextEditPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextEditPrivate *>(self)->take(key, call);
}

//  void QQuickTextEditPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickTextEditPrivate12mirrorChangeEv(
    QQuickTextEditPrivate *self) {
  self->QQuickTextEditPrivate::mirrorChange();
}

//  bool QQuickTextEditPrivate::transformChanged(QQuickItem *transformedItem)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QQuickTextEditPrivate16transformChangedEP10QQuickItem(
    QQuickTextEditPrivate *self,
    QQuickItem *transformedItem) {
  return self->QQuickTextEditPrivate::transformChanged(transformedItem);
}

//  qreal QQuickTextEditPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK21QQuickTextEditPrivate16getImplicitWidthEv(
    const QQuickTextEditPrivate *self) {
  return self->QQuickTextEditPrivate::getImplicitWidth();
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  bool QQuickTextEditPrivate::handleContextMenuEvent(QContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QQuickTextEditPrivate22handleContextMenuEventEP17QContextMenuEvent(
    QQuickTextEditPrivate *self,
    QContextMenuEvent *event) {
  return self->QQuickTextEditPrivate::handleContextMenuEvent(event);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_CONFIG(accessibility)
//  void QQuickTextEditPrivate::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickTextEditPrivate26accessibilityActiveChangedEb(
    QQuickTextEditPrivate *self,
    bool active) {
  self->QQuickTextEditPrivate::accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickTextEditPrivate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK21QQuickTextEditPrivate14accessibleRoleEv(
    const QQuickTextEditPrivate *self) {
  return self->QQuickTextEditPrivate::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)
