//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextinput_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextinput_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquicktextinput_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qchar.h>
#include <cstring>

//  A QQuickTextInputPrivate that Python can take functions over in. Every QQuickTextInputPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTextInputPrivateCall0)(const void *, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickTextInputPrivateCall1)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickTextInputPrivateCall2)(const void *, bool, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickTextInputPrivateCall3)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickTextInputPrivateCall4)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef qreal (*CuteQQuickTextInputPrivateCall5)(const void *, int *);
typedef void (*CuteQQuickTextInputPrivateCall6)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickTextInputPrivateCall7)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickTextInputPrivateCall8)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickTextInputPrivateCall9)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickTextInputPrivateCall10)(const void *, int, int *);
typedef qreal (*CuteQQuickTextInputPrivateCall11)(const void *, int *);
typedef void (*CuteQQuickTextInputPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickTextInputPrivateCall13)(const void *, int *);
typedef bool (*CuteQQuickTextInputPrivateCall14)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickTextInputPrivateCall15)(const void *, QPointerEvent *, bool, int *);
typedef void (*CuteQQuickTextInputPrivateCall16)(const void *, bool, int *);
typedef void * (*CuteQQuickTextInputPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickTextInputPrivateCall18)(const void *, int *);
typedef void (*CuteQQuickTextInputPrivateCall19)(const void *, int, int *);
class CuteQQuickTextInputPrivate : public QQuickTextInputPrivate {
public:
  using QQuickTextInputPrivate::QQuickTextInputPrivate;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[0] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN22QQuickTextInputPrivate15readOnlyChangedEb")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[5] = call;
      return true;
    }
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
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
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

  //  void QQuickTextInputPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall0 call = reinterpret_cast<CuteQQuickTextInputPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextInputPrivate::mirrorChange();
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickTextInputPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall1 call = reinterpret_cast<CuteQQuickTextInputPrivateCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickTextInputPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickTextInputPrivate::readOnlyChanged(bool isReadOnly)
  void readOnlyChanged(bool isReadOnly) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall2 call = reinterpret_cast<CuteQQuickTextInputPrivateCall2>(taken[2]);
      call(this, isReadOnly, &handled);
      if (handled) return;
    }
    QQuickTextInputPrivate::readOnlyChanged(isReadOnly);
  }

#if QT_CONFIG(accessibility)
  //  void QQuickTextInputPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall3 call = reinterpret_cast<CuteQQuickTextInputPrivateCall3>(taken[3]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickTextInputPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickTextInputPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall4 call = reinterpret_cast<CuteQQuickTextInputPrivateCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickTextInputPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  qreal QQuickTextInputPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall5 call = reinterpret_cast<CuteQQuickTextInputPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTextInputPrivate::getImplicitWidth();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall6 call = reinterpret_cast<CuteQQuickTextInputPrivateCall6>(taken[6]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall7 call = reinterpret_cast<CuteQQuickTextInputPrivateCall7>(taken[7]);
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
      CuteQQuickTextInputPrivateCall8 call = reinterpret_cast<CuteQQuickTextInputPrivateCall8>(taken[8]);
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
      CuteQQuickTextInputPrivateCall9 call = reinterpret_cast<CuteQQuickTextInputPrivateCall9>(taken[9]);
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
      CuteQQuickTextInputPrivateCall10 call = reinterpret_cast<CuteQQuickTextInputPrivateCall10>(taken[10]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall11 call = reinterpret_cast<CuteQQuickTextInputPrivateCall11>(taken[11]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall12 call = reinterpret_cast<CuteQQuickTextInputPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall13 call = reinterpret_cast<CuteQQuickTextInputPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall14 call = reinterpret_cast<CuteQQuickTextInputPrivateCall14>(taken[14]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall15 call = reinterpret_cast<CuteQQuickTextInputPrivateCall15>(taken[15]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall16 call = reinterpret_cast<CuteQQuickTextInputPrivateCall16>(taken[16]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall17 call = reinterpret_cast<CuteQQuickTextInputPrivateCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall18 call = reinterpret_cast<CuteQQuickTextInputPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTextInputPrivateCall19 call = reinterpret_cast<CuteQQuickTextInputPrivateCall19>(taken[19]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickTextInput *QQuickTextInputPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickTextInput *ritual_ZN22QQuickTextInputPrivate6q_funcEv(
    QQuickTextInputPrivate *self) {
  return self->q_func();
}

//  const QQuickTextInput *QQuickTextInputPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextInput *ritual_ZNK22QQuickTextInputPrivate6q_funcEv(
    const QQuickTextInputPrivate *self) {
  return self->q_func();
}

//  QQuickTextInputPrivate::QQuickTextInputPrivate()
extern "C" Q_DECL_EXPORT
QQuickTextInputPrivate *ritual_ZN22QQuickTextInputPrivateC1Ev() {
  return new CuteQQuickTextInputPrivate();
}

//  QQuickTextInputPrivate::~QQuickTextInputPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivateD1Ev(QQuickTextInputPrivate *self) {
  delete self;
}

//  void QQuickTextInputPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate4initEv(QQuickTextInputPrivate *self) {
  self->init();
}

//  void QQuickTextInputPrivate::cancelInput()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate11cancelInputEv(
    QQuickTextInputPrivate *self) {
  self->cancelInput();
}

//  void QQuickTextInputPrivate::ensureVisible(int position, int
//      preeditCursor, int preeditLength)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate13ensureVisibleEiii(
    QQuickTextInputPrivate *self,
    int position,
    int preeditCursor,
    int preeditLength) {
  self->ensureVisible(position, preeditCursor, preeditLength);
}

//  void QQuickTextInputPrivate::updateHorizontalScroll()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate22updateHorizontalScrollEv(
    QQuickTextInputPrivate *self) {
  self->updateHorizontalScroll();
}

//  void QQuickTextInputPrivate::updateVerticalScroll()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate20updateVerticalScrollEv(
    QQuickTextInputPrivate *self) {
  self->updateVerticalScroll();
}

//  bool QQuickTextInputPrivate::determineHorizontalAlignment()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTextInputPrivate28determineHorizontalAlignmentEv(
    QQuickTextInputPrivate *self) {
  return self->determineHorizontalAlignment();
}

//  bool QQuickTextInputPrivate::setHAlign(QQuickTextInput::HAlignment a0,
//      bool forceAlign)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTextInputPrivate9setHAlignEN15QQuickTextInput10HAlignmentEb(
    QQuickTextInputPrivate *self,
    QQuickTextInput::HAlignment a0,
    bool forceAlign) {
  return self->setHAlign(a0, forceAlign);
}

//  void QQuickTextInputPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate12mirrorChangeEv(
    QQuickTextInputPrivate *self) {
  self->mirrorChange();
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  bool QQuickTextInputPrivate::handleContextMenuEvent(QContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTextInputPrivate22handleContextMenuEventEP17QContextMenuEvent(
    QQuickTextInputPrivate *self,
    QContextMenuEvent *event) {
  return self->handleContextMenuEvent(event);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  bool QQuickTextInputPrivate::sendMouseEventToInputContext(QMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTextInputPrivate28sendMouseEventToInputContextEP11QMouseEvent(
    QQuickTextInputPrivate *self,
    QMouseEvent *event) {
  return self->sendMouseEventToInputContext(event);
}

#if QT_CONFIG(im)
//  Qt::InputMethodHints QQuickTextInputPrivate::effectiveInputMethodHints()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTextInputPrivate25effectiveInputMethodHintsEv(
    const QQuickTextInputPrivate *self) {
  return static_cast<int>(self->effectiveInputMethodHints().toInt());
}
#endif  // QT_CONFIG(im)

//  void QQuickTextInputPrivate::handleFocusEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate16handleFocusEventEP11QFocusEvent(
    QQuickTextInputPrivate *self,
    QFocusEvent *event) {
  self->handleFocusEvent(event);
}

//  void QQuickTextInputPrivate::readOnlyChanged(bool isReadOnly)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate15readOnlyChangedEb(
    QQuickTextInputPrivate *self,
    bool isReadOnly) {
  self->readOnlyChanged(isReadOnly);
}

//  void QQuickTextInputPrivate::echoModeChanged(QQuickTextInput::EchoMode
//      echoMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate15echoModeChangedEN15QQuickTextInput8EchoModeE(
    QQuickTextInputPrivate *self,
    QQuickTextInput::EchoMode echoMode) {
  self->echoModeChanged(echoMode);
}

#if QT_CONFIG(accessibility)
//  void QQuickTextInputPrivate::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate26accessibilityActiveChangedEb(
    QQuickTextInputPrivate *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickTextInputPrivate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK22QQuickTextInputPrivate14accessibleRoleEv(
    const QQuickTextInputPrivate *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  QQuickTextInputPrivate *QQuickTextInputPrivate::get(QQuickTextInput *t)
extern "C" Q_DECL_EXPORT
QQuickTextInputPrivate *ritual_ZN22QQuickTextInputPrivate3getEP15QQuickTextInput(
    QQuickTextInput *t) {
  return QQuickTextInputPrivate::get(t);
}

//  bool QQuickTextInputPrivate::hasPendingTripleClick() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTextInputPrivate21hasPendingTripleClickEv(
    const QQuickTextInputPrivate *self) {
  return self->hasPendingTripleClick();
}

//  void QQuickTextInputPrivate::setNativeCursorEnabled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate22setNativeCursorEnabledEb(
    QQuickTextInputPrivate *self,
    bool a0) {
  self->setNativeCursorEnabled(a0);
}

//  int QQuickTextInputPrivate::nextMaskBlank(int pos)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickTextInputPrivate13nextMaskBlankEi(
    QQuickTextInputPrivate *self,
    int pos) {
  return self->nextMaskBlank(pos);
}

//  int QQuickTextInputPrivate::prevMaskBlank(int pos)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickTextInputPrivate13prevMaskBlankEi(
    QQuickTextInputPrivate *self,
    int pos) {
  return self->prevMaskBlank(pos);
}

//  bool QQuickTextInputPrivate::isUndoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTextInputPrivate15isUndoAvailableEv(
    const QQuickTextInputPrivate *self) {
  return self->isUndoAvailable();
}

//  bool QQuickTextInputPrivate::isRedoAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTextInputPrivate15isRedoAvailableEv(
    const QQuickTextInputPrivate *self) {
  return self->isRedoAvailable();
}

//  void QQuickTextInputPrivate::clearUndo()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate9clearUndoEv(
    QQuickTextInputPrivate *self) {
  self->clearUndo();
}

//  bool QQuickTextInputPrivate::allSelected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTextInputPrivate11allSelectedEv(
    const QQuickTextInputPrivate *self) {
  return self->allSelected();
}

//  bool QQuickTextInputPrivate::hasSelectedText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTextInputPrivate15hasSelectedTextEv(
    const QQuickTextInputPrivate *self) {
  return self->hasSelectedText();
}

//  void QQuickTextInputPrivate::setSelection(int start, int length)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate12setSelectionEii(
    QQuickTextInputPrivate *self,
    int start,
    int length) {
  self->setSelection(start, length);
}

//  QString QQuickTextInputPrivate::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickTextInputPrivate12selectedTextEv(
    const QQuickTextInputPrivate *self) {
  return new QString(self->selectedText());
}

//  QString QQuickTextInputPrivate::textBeforeSelection() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickTextInputPrivate19textBeforeSelectionEv(
    const QQuickTextInputPrivate *self) {
  return new QString(self->textBeforeSelection());
}

//  QString QQuickTextInputPrivate::textAfterSelection() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickTextInputPrivate18textAfterSelectionEv(
    const QQuickTextInputPrivate *self) {
  return new QString(self->textAfterSelection());
}

//  int QQuickTextInputPrivate::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTextInputPrivate14selectionStartEv(
    const QQuickTextInputPrivate *self) {
  return self->selectionStart();
}

//  int QQuickTextInputPrivate::selectionEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTextInputPrivate12selectionEndEv(
    const QQuickTextInputPrivate *self) {
  return self->selectionEnd();
}

//  QRectF QQuickTextInputPrivate::anchorRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK22QQuickTextInputPrivate15anchorRectangleEv(
    const QQuickTextInputPrivate *self) {
  return new QRectF(self->anchorRectangle());
}

//  int QQuickTextInputPrivate::positionAt(qreal x, qreal y,
//      QTextLine::CursorPosition position) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTextInputPrivate10positionAtEddN9QTextLine14CursorPositionE(
    const QQuickTextInputPrivate *self,
    qreal x,
    qreal y,
    QTextLine::CursorPosition position) {
  return self->positionAt(x, y, position);
}

//  int QQuickTextInputPrivate::positionAt(const QPointF &point,
//      QTextLine::CursorPosition position) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTextInputPrivate10positionAtERK7QPointFN9QTextLine14CursorPositionE(
    const QQuickTextInputPrivate *self,
    const QPointF *point,
    QTextLine::CursorPosition position) {
  return self->positionAt(*point, position);
}

//  void QQuickTextInputPrivate::removeSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate15removeSelectionEv(
    QQuickTextInputPrivate *self) {
  self->removeSelection();
}

//  int QQuickTextInputPrivate::start() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTextInputPrivate5startEv(
    const QQuickTextInputPrivate *self) {
  return self->start();
}

//  int QQuickTextInputPrivate::end() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTextInputPrivate3endEv(
    const QQuickTextInputPrivate *self) {
  return self->end();
}

//  QString QQuickTextInputPrivate::realText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickTextInputPrivate8realTextEv(
    const QQuickTextInputPrivate *self) {
  return new QString(self->realText());
}

#if QT_CONFIG(clipboard)
//  void QQuickTextInputPrivate::copy(QClipboard::Mode mode) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QQuickTextInputPrivate4copyEN10QClipboard4ModeE(
    const QQuickTextInputPrivate *self,
    QClipboard::Mode mode) {
  self->copy(mode);
}
#endif  // QT_CONFIG(clipboard)

#if QT_CONFIG(clipboard)
//  void QQuickTextInputPrivate::paste(QClipboard::Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate5pasteEN10QClipboard4ModeE(
    QQuickTextInputPrivate *self,
    QClipboard::Mode mode) {
  self->paste(mode);
}
#endif  // QT_CONFIG(clipboard)

#if QT_CONFIG(im)
//  void QQuickTextInputPrivate::commitPreedit()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate13commitPreeditEv(
    QQuickTextInputPrivate *self) {
  self->commitPreedit();
}
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
//  void QQuickTextInputPrivate::cancelPreedit()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate13cancelPreeditEv(
    QQuickTextInputPrivate *self) {
  self->cancelPreedit();
}
#endif  // QT_CONFIG(im)

//  Qt::CursorMoveStyle QQuickTextInputPrivate::cursorMoveStyle() const
extern "C" Q_DECL_EXPORT
Qt::CursorMoveStyle ritual_ZNK22QQuickTextInputPrivate15cursorMoveStyleEv(
    const QQuickTextInputPrivate *self) {
  return self->cursorMoveStyle();
}

//  void QQuickTextInputPrivate::setCursorMoveStyle(Qt::CursorMoveStyle
//      style)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate18setCursorMoveStyleEN2Qt15CursorMoveStyleE(
    QQuickTextInputPrivate *self,
    Qt::CursorMoveStyle style) {
  self->setCursorMoveStyle(style);
}

//  void QQuickTextInputPrivate::moveCursor(int pos, bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate10moveCursorEib(
    QQuickTextInputPrivate *self,
    int pos,
    bool mark) {
  self->moveCursor(pos, mark);
}

//  void QQuickTextInputPrivate::cursorForward(bool mark, int steps)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate13cursorForwardEbi(
    QQuickTextInputPrivate *self,
    bool mark,
    int steps) {
  self->cursorForward(mark, steps);
}

//  void QQuickTextInputPrivate::cursorWordForward(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate17cursorWordForwardEb(
    QQuickTextInputPrivate *self,
    bool mark) {
  self->cursorWordForward(mark);
}

//  void QQuickTextInputPrivate::cursorWordBackward(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate18cursorWordBackwardEb(
    QQuickTextInputPrivate *self,
    bool mark) {
  self->cursorWordBackward(mark);
}

//  void QQuickTextInputPrivate::home(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate4homeEb(
    QQuickTextInputPrivate *self,
    bool mark) {
  self->home(mark);
}

//  void QQuickTextInputPrivate::end(bool mark)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate3endEb(
    QQuickTextInputPrivate *self,
    bool mark) {
  self->end(mark);
}

//  void QQuickTextInputPrivate::backspace()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate9backspaceEv(
    QQuickTextInputPrivate *self) {
  self->backspace();
}

//  void QQuickTextInputPrivate::del()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate3delEv(QQuickTextInputPrivate *self) {
  self->del();
}

//  void QQuickTextInputPrivate::deselect()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate8deselectEv(
    QQuickTextInputPrivate *self) {
  self->deselect();
}

//  void QQuickTextInputPrivate::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate9selectAllEv(
    QQuickTextInputPrivate *self) {
  self->selectAll();
}

//  void QQuickTextInputPrivate::insert(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate6insertERK7QString(
    QQuickTextInputPrivate *self,
    const QString *a0) {
  self->insert(*a0);
}

//  void QQuickTextInputPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate5clearEv(
    QQuickTextInputPrivate *self) {
  self->clear();
}

//  void QQuickTextInputPrivate::selectWordAtPos(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate15selectWordAtPosEi(
    QQuickTextInputPrivate *self,
    int a0) {
  self->selectWordAtPos(a0);
}

//  void QQuickTextInputPrivate::setCursorPosition(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate17setCursorPositionEi(
    QQuickTextInputPrivate *self,
    int pos) {
  self->setCursorPosition(pos);
}

//  bool QQuickTextInputPrivate::fixup()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTextInputPrivate5fixupEv(
    QQuickTextInputPrivate *self) {
  return self->fixup();
}

//  QString QQuickTextInputPrivate::inputMask() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickTextInputPrivate9inputMaskEv(
    const QQuickTextInputPrivate *self) {
  return new QString(self->inputMask());
}

//  void QQuickTextInputPrivate::setInputMask(const QString &mask)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate12setInputMaskERK7QString(
    QQuickTextInputPrivate *self,
    const QString *mask) {
  self->setInputMask(*mask);
}

#if QT_CONFIG(im)
//  bool QQuickTextInputPrivate::composeMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTextInputPrivate11composeModeEv(
    const QQuickTextInputPrivate *self) {
  return self->composeMode();
}
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
//  QString QQuickTextInputPrivate::preeditAreaText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickTextInputPrivate15preeditAreaTextEv(
    const QQuickTextInputPrivate *self) {
  return new QString(self->preeditAreaText());
}
#endif  // QT_CONFIG(im)

//  void QQuickTextInputPrivate::updatePasswordEchoEditing(bool editing)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate25updatePasswordEchoEditingEb(
    QQuickTextInputPrivate *self,
    bool editing) {
  self->updatePasswordEchoEditing(editing);
}

//  void QQuickTextInputPrivate::cancelPasswordEchoTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate23cancelPasswordEchoTimerEv(
    QQuickTextInputPrivate *self) {
  self->cancelPasswordEchoTimer();
}

//  Qt::LayoutDirection QQuickTextInputPrivate::textDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK22QQuickTextInputPrivate13textDirectionEv(
    const QQuickTextInputPrivate *self) {
  return self->textDirection();
}

//  Qt::LayoutDirection QQuickTextInputPrivate::layoutDirection() const
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZNK22QQuickTextInputPrivate15layoutDirectionEv(
    const QQuickTextInputPrivate *self) {
  return self->layoutDirection();
}

//  void QQuickTextInputPrivate::setLayoutDirection(Qt::LayoutDirection
//      direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate18setLayoutDirectionEN2Qt15LayoutDirectionE(
    QQuickTextInputPrivate *self,
    Qt::LayoutDirection direction) {
  self->setLayoutDirection(direction);
}

#if QT_CONFIG(im)
//  void QQuickTextInputPrivate::processInputMethodEvent(QInputMethodEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate23processInputMethodEventEP17QInputMethodEvent(
    QQuickTextInputPrivate *self,
    QInputMethodEvent *event) {
  self->processInputMethodEvent(event);
}
#endif  // QT_CONFIG(im)

//  void QQuickTextInputPrivate::processKeyEvent(QKeyEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate15processKeyEventEP9QKeyEvent(
    QQuickTextInputPrivate *self,
    QKeyEvent *ev) {
  self->processKeyEvent(ev);
}

//  void QQuickTextInputPrivate::setBlinkingCursorEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate24setBlinkingCursorEnabledEb(
    QQuickTextInputPrivate *self,
    bool enable) {
  self->setBlinkingCursorEnabled(enable);
}

//  void QQuickTextInputPrivate::updateCursorBlinking()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate20updateCursorBlinkingEv(
    QQuickTextInputPrivate *self) {
  self->updateCursorBlinking();
}

//  void QQuickTextInputPrivate::updateLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate12updateLayoutEv(
    QQuickTextInputPrivate *self) {
  self->updateLayout();
}

//  void QQuickTextInputPrivate::updateBaselineOffset()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate20updateBaselineOffsetEv(
    QQuickTextInputPrivate *self) {
  self->updateBaselineOffset();
}

//  qreal QQuickTextInputPrivate::calculateImplicitWidthForText(const QString
//      &text) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTextInputPrivate29calculateImplicitWidthForTextERK7QString(
    const QQuickTextInputPrivate *self,
    const QString *text) {
  return self->calculateImplicitWidthForText(*text);
}

//  qreal QQuickTextInputPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTextInputPrivate16getImplicitWidthEv(
    const QQuickTextInputPrivate *self) {
  return self->getImplicitWidth();
}

//  qreal QQuickTextInputPrivate::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickTextInputPrivate7paddingEv(
    const QQuickTextInputPrivate *self) {
  return self->padding();
}

//  void QQuickTextInputPrivate::setTopPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate13setTopPaddingEdb(
    QQuickTextInputPrivate *self,
    qreal value,
    bool reset) {
  self->setTopPadding(value, reset);
}

//  void QQuickTextInputPrivate::setLeftPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate14setLeftPaddingEdb(
    QQuickTextInputPrivate *self,
    qreal value,
    bool reset) {
  self->setLeftPadding(value, reset);
}

//  void QQuickTextInputPrivate::setRightPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate15setRightPaddingEdb(
    QQuickTextInputPrivate *self,
    qreal value,
    bool reset) {
  self->setRightPadding(value, reset);
}

//  void QQuickTextInputPrivate::setBottomPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate16setBottomPaddingEdb(
    QQuickTextInputPrivate *self,
    qreal value,
    bool reset) {
  self->setBottomPadding(value, reset);
}

//  bool QQuickTextInputPrivate::isImplicitResizeEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTextInputPrivate23isImplicitResizeEnabledEv(
    const QQuickTextInputPrivate *self) {
  return self->isImplicitResizeEnabled();
}

//  void QQuickTextInputPrivate::setImplicitResizeEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate24setImplicitResizeEnabledEb(
    QQuickTextInputPrivate *self,
    bool enabled) {
  self->setImplicitResizeEnabled(enabled);
}

//  void QQuickTextInputPrivate::removeSelectedText()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate18removeSelectedTextEv(
    QQuickTextInputPrivate *self) {
  self->removeSelectedText();
}

//  void QQuickTextInputPrivate::internalSetText(const QString &txt, int pos,
//      bool edited)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate15internalSetTextERK7QStringib(
    QQuickTextInputPrivate *self,
    const QString *txt,
    int pos,
    bool edited) {
  self->internalSetText(*txt, pos, edited);
}

//  void QQuickTextInputPrivate::updateDisplayText(bool forceUpdate)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate17updateDisplayTextEb(
    QQuickTextInputPrivate *self,
    bool forceUpdate) {
  self->updateDisplayText(forceUpdate);
}

//  void QQuickTextInputPrivate::internalInsert(const QString &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate14internalInsertERK7QString(
    QQuickTextInputPrivate *self,
    const QString *s) {
  self->internalInsert(*s);
}

//  void QQuickTextInputPrivate::internalDelete(bool wasBackspace)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate14internalDeleteEb(
    QQuickTextInputPrivate *self,
    bool wasBackspace) {
  self->internalDelete(wasBackspace);
}

//  void QQuickTextInputPrivate::internalDeselect()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate16internalDeselectEv(
    QQuickTextInputPrivate *self) {
  self->internalDeselect();
}

//  void QQuickTextInputPrivate::internalUndo(int until)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate12internalUndoEi(
    QQuickTextInputPrivate *self,
    int until) {
  self->internalUndo(until);
}

//  void QQuickTextInputPrivate::internalRedo()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate12internalRedoEv(
    QQuickTextInputPrivate *self) {
  self->internalRedo();
}

//  void QQuickTextInputPrivate::emitUndoRedoChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate19emitUndoRedoChangedEv(
    QQuickTextInputPrivate *self) {
  self->emitUndoRedoChanged();
}

//  bool QQuickTextInputPrivate::emitCursorPositionChanged()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTextInputPrivate25emitCursorPositionChangedEv(
    QQuickTextInputPrivate *self) {
  return self->emitCursorPositionChanged();
}

//  bool QQuickTextInputPrivate::finishChange(int validateFromState, bool
//      update, bool edited)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTextInputPrivate12finishChangeEibb(
    QQuickTextInputPrivate *self,
    int validateFromState,
    bool update,
    bool edited) {
  return self->finishChange(validateFromState, update, edited);
}

//  void QQuickTextInputPrivate::addCommand(const Command &cmd)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate10addCommandERKNS_7CommandE(
    QQuickTextInputPrivate *self,
    const QQuickTextInputPrivate::Command *cmd) {
  self->addCommand(*cmd);
}

//  void QQuickTextInputPrivate::separate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate8separateEv(
    QQuickTextInputPrivate *self) {
  self->separate();
}

//  bool QQuickTextInputPrivate::separateSelection()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickTextInputPrivate17separateSelectionEv(
    QQuickTextInputPrivate *self) {
  return self->separateSelection();
}

//  void QQuickTextInputPrivate::deleteStartOfWord()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate17deleteStartOfWordEv(
    QQuickTextInputPrivate *self) {
  self->deleteStartOfWord();
}

//  void QQuickTextInputPrivate::deleteEndOfWord()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate15deleteEndOfWordEv(
    QQuickTextInputPrivate *self) {
  self->deleteEndOfWord();
}

//  void QQuickTextInputPrivate::deleteEndOfLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate15deleteEndOfLineEv(
    QQuickTextInputPrivate *self) {
  self->deleteEndOfLine();
}

//  void QQuickTextInputPrivate::parseInputMask(const QString &maskFields)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate14parseInputMaskERK7QString(
    QQuickTextInputPrivate *self,
    const QString *maskFields) {
  self->parseInputMask(*maskFields);
}

//  bool QQuickTextInputPrivate::isValidInput(QChar key, QChar mask) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQuickTextInputPrivate12isValidInputE5QCharS0_(
    const QQuickTextInputPrivate *self,
    const QChar *key,
    const QChar *mask) {
  return self->isValidInput(*key, *mask);
}

//  ValidatorState QQuickTextInputPrivate::hasAcceptableInput(const QString
//      &text) const
extern "C" Q_DECL_EXPORT
QQuickTextInputPrivate::ValidatorState ritual_ZNK22QQuickTextInputPrivate18hasAcceptableInputERK7QString(
    const QQuickTextInputPrivate *self,
    const QString *text) {
  return self->hasAcceptableInput(*text);
}

//  void QQuickTextInputPrivate::checkIsValid()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate12checkIsValidEv(
    QQuickTextInputPrivate *self) {
  self->checkIsValid();
}

//  QString QQuickTextInputPrivate::maskString(uint pos, const QString &str,
//      bool clear) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickTextInputPrivate10maskStringEjRK7QStringb(
    const QQuickTextInputPrivate *self,
    uint pos,
    const QString *str,
    bool clear) {
  return new QString(self->maskString(pos, *str, clear));
}

//  QString QQuickTextInputPrivate::clearString(uint pos, uint len) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickTextInputPrivate11clearStringEjj(
    const QQuickTextInputPrivate *self,
    uint pos,
    uint len) {
  return new QString(self->clearString(pos, len));
}

//  QString QQuickTextInputPrivate::stripString(const QString &str) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QQuickTextInputPrivate11stripStringERK7QString(
    const QQuickTextInputPrivate *self,
    const QString *str) {
  return new QString(self->stripString(*str));
}

//  int QQuickTextInputPrivate::findInMask(int pos, bool forward, bool
//      findSeparator, QChar searchChar) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QQuickTextInputPrivate10findInMaskEibb5QChar(
    const QQuickTextInputPrivate *self,
    int pos,
    bool forward,
    bool findSeparator,
    const QChar *searchChar) {
  return self->findInMask(pos, forward, findSeparator, *searchChar);
}

//  QQuickTextInputPrivate as the QAccessible::ActivationObserver it is built
//      on
extern "C" Q_DECL_EXPORT
QAccessible::ActivationObserver *ritual_cast_QQuickTextInputPrivate_QAccessible_ActivationObserver(
    QQuickTextInputPrivate *self) {
  return static_cast<QAccessible::ActivationObserver *>(self);
}

//  a Python function taken by a CuteQQuickTextInputPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextInputPrivate(
    QQuickTextInputPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextInputPrivate *>(self)->take(key, call);
}

//  void QQuickTextInputPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTextInputPrivate12mirrorChangeEv(
    QQuickTextInputPrivate *self) {
  self->QQuickTextInputPrivate::mirrorChange();
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  bool QQuickTextInputPrivate::handleContextMenuEvent(QContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickTextInputPrivate22handleContextMenuEventEP17QContextMenuEvent(
    QQuickTextInputPrivate *self,
    QContextMenuEvent *event) {
  return self->QQuickTextInputPrivate::handleContextMenuEvent(event);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QQuickTextInputPrivate::readOnlyChanged(bool isReadOnly)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTextInputPrivate15readOnlyChangedEb(
    QQuickTextInputPrivate *self,
    bool isReadOnly) {
  self->QQuickTextInputPrivate::readOnlyChanged(isReadOnly);
}

#if QT_CONFIG(accessibility)
//  void QQuickTextInputPrivate::accessibilityActiveChanged(bool active)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QQuickTextInputPrivate26accessibilityActiveChangedEb(
    QQuickTextInputPrivate *self,
    bool active) {
  self->QQuickTextInputPrivate::accessibilityActiveChanged(active);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickTextInputPrivate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK22QQuickTextInputPrivate14accessibleRoleEv(
    const QQuickTextInputPrivate *self) {
  return self->QQuickTextInputPrivate::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  qreal QQuickTextInputPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK22QQuickTextInputPrivate16getImplicitWidthEv(
    const QQuickTextInputPrivate *self) {
  return self->QQuickTextInputPrivate::getImplicitWidth();
}
