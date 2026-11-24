//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktext_p_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktext_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquicktext_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qtextlayout.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QQuickTextPrivate that Python can take functions over in. Every QQuickTextPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTextPrivateCall0)(const void *, int *);
typedef bool (*CuteQQuickTextPrivateCall1)(const void *, QQuickItem *, int *);
typedef qreal (*CuteQQuickTextPrivateCall2)(const void *, int *);
typedef qreal (*CuteQQuickTextPrivateCall3)(const void *, int *);
typedef void (*CuteQQuickTextPrivateCall4)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickTextPrivateCall5)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickTextPrivateCall6)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickTextPrivateCall7)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickTextPrivateCall8)(const void *, int, int *);
typedef void (*CuteQQuickTextPrivateCall9)(const void *, int *);
typedef void (*CuteQQuickTextPrivateCall10)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickTextPrivateCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickTextPrivateCall12)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickTextPrivateCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickTextPrivateCall14)(const void *, bool, int *);
typedef void * (*CuteQQuickTextPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickTextPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickTextPrivateCall17)(const void *, int, int *);
class CuteQQuickTextPrivate : public QQuickTextPrivate {
public:
  using QQuickTextPrivate::QQuickTextPrivate;
  void *taken[18] = {};

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
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
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
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[12] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QQuickTextPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextPrivateCall0 call = reinterpret_cast<CuteQQuickTextPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextPrivate::mirrorChange();
  }

  //  bool QQuickTextPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextPrivateCall1 call = reinterpret_cast<CuteQQuickTextPrivateCall1>(taken[1]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickTextPrivate::transformChanged(transformedItem);
  }

  //  qreal QQuickTextPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextPrivateCall2 call = reinterpret_cast<CuteQQuickTextPrivateCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTextPrivate::getImplicitWidth();
  }

  //  qreal QQuickTextPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTextPrivateCall3 call = reinterpret_cast<CuteQQuickTextPrivateCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickTextPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTextPrivateCall4 call = reinterpret_cast<CuteQQuickTextPrivateCall4>(taken[4]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTextPrivateCall5 call = reinterpret_cast<CuteQQuickTextPrivateCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTextPrivateCall6 call = reinterpret_cast<CuteQQuickTextPrivateCall6>(taken[6]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTextPrivateCall7 call = reinterpret_cast<CuteQQuickTextPrivateCall7>(taken[7]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTextPrivateCall8 call = reinterpret_cast<CuteQQuickTextPrivateCall8>(taken[8]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTextPrivateCall9 call = reinterpret_cast<CuteQQuickTextPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTextPrivateCall10 call = reinterpret_cast<CuteQQuickTextPrivateCall10>(taken[10]);
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
      CuteQQuickTextPrivateCall11 call = reinterpret_cast<CuteQQuickTextPrivateCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTextPrivateCall12 call = reinterpret_cast<CuteQQuickTextPrivateCall12>(taken[12]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTextPrivateCall13 call = reinterpret_cast<CuteQQuickTextPrivateCall13>(taken[13]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTextPrivateCall14 call = reinterpret_cast<CuteQQuickTextPrivateCall14>(taken[14]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTextPrivateCall15 call = reinterpret_cast<CuteQQuickTextPrivateCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTextPrivateCall16 call = reinterpret_cast<CuteQQuickTextPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTextPrivateCall17 call = reinterpret_cast<CuteQQuickTextPrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickText *QQuickTextPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickText *ritual_ZN17QQuickTextPrivate6q_funcEv(QQuickTextPrivate *self) {
  return self->q_func();
}

//  const QQuickText *QQuickTextPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickText *ritual_ZNK17QQuickTextPrivate6q_funcEv(
    const QQuickTextPrivate *self) {
  return self->q_func();
}

//  QQuickTextPrivate::QQuickTextPrivate()
extern "C" Q_DECL_EXPORT
QQuickTextPrivate *ritual_ZN17QQuickTextPrivateC1Ev() {
  return new CuteQQuickTextPrivate();
}

//  QQuickTextPrivate::~QQuickTextPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivateD1Ev(QQuickTextPrivate *self) {
  delete self;
}

//  void QQuickTextPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate4initEv(QQuickTextPrivate *self) {
  self->init();
}

//  void QQuickTextPrivate::updateBaseline(qreal baseline, qreal dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate14updateBaselineEdd(
    QQuickTextPrivate *self,
    qreal baseline,
    qreal dy) {
  self->updateBaseline(baseline, dy);
}

//  void QQuickTextPrivate::updateSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate10updateSizeEv(QQuickTextPrivate *self) {
  self->updateSize();
}

//  void QQuickTextPrivate::signalSizeChange(const QSizeF &previousSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate16signalSizeChangeERK6QSizeF(
    QQuickTextPrivate *self,
    const QSizeF *previousSize) {
  self->signalSizeChange(*previousSize);
}

//  void QQuickTextPrivate::updateLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate12updateLayoutEv(QQuickTextPrivate *self) {
  self->updateLayout();
}

//  bool QQuickTextPrivate::determineHorizontalAlignment()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickTextPrivate28determineHorizontalAlignmentEv(
    QQuickTextPrivate *self) {
  return self->determineHorizontalAlignment();
}

//  bool QQuickTextPrivate::setHAlign(QQuickText::HAlignment a0, bool
//      forceAlign)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickTextPrivate9setHAlignEN10QQuickText10HAlignmentEb(
    QQuickTextPrivate *self,
    QQuickText::HAlignment a0,
    bool forceAlign) {
  return self->setHAlign(a0, forceAlign);
}

//  void QQuickTextPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate12mirrorChangeEv(QQuickTextPrivate *self) {
  self->mirrorChange();
}

//  bool QQuickTextPrivate::isLineLaidOutConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickTextPrivate22isLineLaidOutConnectedEv(
    QQuickTextPrivate *self) {
  return self->isLineLaidOutConnected();
}

//  int QQuickTextPrivate::lineHeightOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickTextPrivate16lineHeightOffsetEv(
    const QQuickTextPrivate *self) {
  return self->lineHeightOffset();
}

//  QString QQuickTextPrivate::elidedText(qreal lineWidth, const QTextLine
//      &line) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickTextPrivate10elidedTextEdRK9QTextLine(
    const QQuickTextPrivate *self,
    qreal lineWidth,
    const QTextLine *line) {
  return new QString(self->elidedText(lineWidth, *line));
}

//  void QQuickTextPrivate::clearFormats()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate12clearFormatsEv(QQuickTextPrivate *self) {
  self->clearFormats();
}

//  void QQuickTextPrivate::processHoverEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate17processHoverEventEP11QHoverEvent(
    QQuickTextPrivate *self,
    QHoverEvent *event) {
  self->processHoverEvent(event);
}

//  bool QQuickTextPrivate::transformChanged(QQuickItem *transformedItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickTextPrivate16transformChangedEP10QQuickItem(
    QQuickTextPrivate *self,
    QQuickItem *transformedItem) {
  return self->transformChanged(transformedItem);
}

//  qreal QQuickTextPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickTextPrivate16getImplicitWidthEv(
    const QQuickTextPrivate *self) {
  return self->getImplicitWidth();
}

//  qreal QQuickTextPrivate::getImplicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickTextPrivate17getImplicitHeightEv(
    const QQuickTextPrivate *self) {
  return self->getImplicitHeight();
}

//  qreal QQuickTextPrivate::availableWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickTextPrivate14availableWidthEv(
    const QQuickTextPrivate *self) {
  return self->availableWidth();
}

//  qreal QQuickTextPrivate::availableHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickTextPrivate15availableHeightEv(
    const QQuickTextPrivate *self) {
  return self->availableHeight();
}

//  qreal QQuickTextPrivate::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickTextPrivate7paddingEv(
    const QQuickTextPrivate *self) {
  return self->padding();
}

//  void QQuickTextPrivate::setTopPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate13setTopPaddingEdb(
    QQuickTextPrivate *self,
    qreal value,
    bool reset) {
  self->setTopPadding(value, reset);
}

//  void QQuickTextPrivate::setLeftPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate14setLeftPaddingEdb(
    QQuickTextPrivate *self,
    qreal value,
    bool reset) {
  self->setLeftPadding(value, reset);
}

//  void QQuickTextPrivate::setRightPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate15setRightPaddingEdb(
    QQuickTextPrivate *self,
    qreal value,
    bool reset) {
  self->setRightPadding(value, reset);
}

//  void QQuickTextPrivate::setBottomPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate16setBottomPaddingEdb(
    QQuickTextPrivate *self,
    qreal value,
    bool reset) {
  self->setBottomPadding(value, reset);
}

//  void QQuickTextPrivate::ensureDoc()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate9ensureDocEv(QQuickTextPrivate *self) {
  self->ensureDoc();
}

//  void QQuickTextPrivate::updateDocumentText()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextPrivate18updateDocumentTextEv(
    QQuickTextPrivate *self) {
  self->updateDocumentText();
}

//  bool QQuickTextPrivate::isLinkActivatedConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickTextPrivate24isLinkActivatedConnectedEv(
    QQuickTextPrivate *self) {
  return self->isLinkActivatedConnected();
}

//  bool QQuickTextPrivate::isLinkHoveredConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickTextPrivate22isLinkHoveredConnectedEv(
    QQuickTextPrivate *self) {
  return self->isLinkHoveredConnected();
}

//  QString QQuickTextPrivate::anchorAt(const QTextLayout *layout, const
//      QPointF &mousePos)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickTextPrivate8anchorAtEPK11QTextLayoutRK7QPointF(
    const QTextLayout *layout,
    const QPointF *mousePos) {
  return new QString(QQuickTextPrivate::anchorAt(layout, *mousePos));
}

//  QString QQuickTextPrivate::anchorAt(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickTextPrivate8anchorAtERK7QPointF(
    const QQuickTextPrivate *self,
    const QPointF *pos) {
  return new QString(self->anchorAt(*pos));
}

//  qreal QQuickTextPrivate::lineHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickTextPrivate10lineHeightEv(
    const QQuickTextPrivate *self) {
  return self->lineHeight();
}

//  int QQuickTextPrivate::maximumLineCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickTextPrivate16maximumLineCountEv(
    const QQuickTextPrivate *self) {
  return self->maximumLineCount();
}

//  int QQuickTextPrivate::renderTypeQuality() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickTextPrivate17renderTypeQualityEv(
    const QQuickTextPrivate *self) {
  return self->renderTypeQuality();
}

//  QQuickText::LineHeightMode QQuickTextPrivate::lineHeightMode() const
extern "C" Q_DECL_EXPORT
QQuickText::LineHeightMode ritual_ZNK17QQuickTextPrivate14lineHeightModeEv(
    const QQuickTextPrivate *self) {
  return self->lineHeightMode();
}

//  QQuickText::FontSizeMode QQuickTextPrivate::fontSizeMode() const
extern "C" Q_DECL_EXPORT
QQuickText::FontSizeMode ritual_ZNK17QQuickTextPrivate12fontSizeModeEv(
    const QQuickTextPrivate *self) {
  return self->fontSizeMode();
}

//  int QQuickTextPrivate::minimumPixelSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickTextPrivate16minimumPixelSizeEv(
    const QQuickTextPrivate *self) {
  return self->minimumPixelSize();
}

//  int QQuickTextPrivate::minimumPointSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickTextPrivate16minimumPointSizeEv(
    const QQuickTextPrivate *self) {
  return self->minimumPointSize();
}

//  QQuickTextPrivate *QQuickTextPrivate::get(QQuickText *t)
extern "C" Q_DECL_EXPORT
QQuickTextPrivate *ritual_ZN17QQuickTextPrivate3getEP10QQuickText(
    QQuickText *t) {
  return QQuickTextPrivate::get(t);
}

//  a Python function taken by a CuteQQuickTextPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextPrivate(
    QQuickTextPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextPrivate *>(self)->take(key, call);
}

//  void QQuickTextPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickTextPrivate12mirrorChangeEv(
    QQuickTextPrivate *self) {
  self->QQuickTextPrivate::mirrorChange();
}

//  bool QQuickTextPrivate::transformChanged(QQuickItem *transformedItem)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickTextPrivate16transformChangedEP10QQuickItem(
    QQuickTextPrivate *self,
    QQuickItem *transformedItem) {
  return self->QQuickTextPrivate::transformChanged(transformedItem);
}

//  qreal QQuickTextPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK17QQuickTextPrivate16getImplicitWidthEv(
    const QQuickTextPrivate *self) {
  return self->QQuickTextPrivate::getImplicitWidth();
}

//  qreal QQuickTextPrivate::getImplicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK17QQuickTextPrivate17getImplicitHeightEv(
    const QQuickTextPrivate *self) {
  return self->QQuickTextPrivate::getImplicitHeight();
}
