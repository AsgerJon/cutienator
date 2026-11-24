//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextfield_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextfield_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qvariant.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickTextField may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTextField : QQuickTextField {
  using QQuickTextField::classBegin;
  using QQuickTextField::componentComplete;
  using QQuickTextField::itemChange;
  using QQuickTextField::geometryChange;
  using QQuickTextField::insetChange;
  using QQuickTextField::updatePaintNode;
  using QQuickTextField::focusInEvent;
  using QQuickTextField::focusOutEvent;
  using QQuickTextField::hoverEnterEvent;
  using QQuickTextField::hoverLeaveEvent;
  using QQuickTextField::mousePressEvent;
  using QQuickTextField::mouseMoveEvent;
  using QQuickTextField::mouseReleaseEvent;
  using QQuickTextField::mouseDoubleClickEvent;
  using QQuickTextField::timerEvent;
};

//  A QQuickTextField that Python can take functions over in. Every QQuickTextField
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTextFieldCall0)(const void *, int *);
typedef void (*CuteQQuickTextFieldCall1)(const void *, int *);
typedef void (*CuteQQuickTextFieldCall2)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickTextFieldCall3)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickTextFieldCall4)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void * (*CuteQQuickTextFieldCall5)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickTextFieldCall6)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTextFieldCall7)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickTextFieldCall8)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickTextFieldCall9)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickTextFieldCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextFieldCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextFieldCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextFieldCall13)(const void *, QMouseEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextFieldCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickTextFieldCall15)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef const QRectF * (*CuteQQuickTextFieldCall16)(const void *, int *);
typedef const QRectF * (*CuteQQuickTextFieldCall17)(const void *, int *);
typedef void (*CuteQQuickTextFieldCall18)(const void *, int *);
typedef void (*CuteQQuickTextFieldCall19)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickTextFieldCall20)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickTextFieldCall21)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextFieldCall22)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextFieldCall23)(const void *, int *);
typedef bool (*CuteQQuickTextFieldCall24)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickTextFieldCall25)(const void *, int *);
typedef void * (*CuteQQuickTextFieldCall26)(const void *, int *);
typedef void (*CuteQQuickTextFieldCall27)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickTextFieldCall28)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTextFieldCall29)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTextFieldCall30)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickTextFieldCall31)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextFieldCall32)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextFieldCall33)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextFieldCall34)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextFieldCall35)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickTextFieldCall36)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickTextFieldCall37)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextFieldCall38)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextFieldCall39)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextFieldCall40)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextFieldCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextFieldCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTextField : public QQuickTextField {
public:
  using QQuickTextField::QQuickTextField;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN15QQuickTextField11insetChangeERK9QMarginsFS2_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickTextInterface10invalidateEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[28] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[31] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[37] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[42] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickTextField::classBegin()
  void classBegin() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextFieldCall0 call = reinterpret_cast<CuteQQuickTextFieldCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextField::classBegin();
  }

  //  void QQuickTextField::componentComplete()
  void componentComplete() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextFieldCall1 call = reinterpret_cast<CuteQQuickTextFieldCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextField::componentComplete();
  }

  //  void QQuickTextField::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextFieldCall2 call = reinterpret_cast<CuteQQuickTextFieldCall2>(taken[2]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickTextField::itemChange(change, value);
  }

  //  void QQuickTextField::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTextFieldCall3 call = reinterpret_cast<CuteQQuickTextFieldCall3>(taken[3]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickTextField::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickTextField::insetChange(const QMarginsF &newInset, const
  //      QMarginsF &oldInset)
  void insetChange(
      const QMarginsF &newInset,
      const QMarginsF &oldInset) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTextFieldCall4 call = reinterpret_cast<CuteQQuickTextFieldCall4>(taken[4]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickTextField::insetChange(newInset, oldInset);
  }

  //  QSGNode *QQuickTextField::updatePaintNode(QSGNode *oldNode,
  //      UpdatePaintNodeData *data)
  QSGNode *updatePaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *data) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTextFieldCall5 call = reinterpret_cast<CuteQQuickTextFieldCall5>(taken[5]);
      void * given = call(this, oldNode, data, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickTextField::updatePaintNode(oldNode, data);
  }

  //  void QQuickTextField::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTextFieldCall6 call = reinterpret_cast<CuteQQuickTextFieldCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextField::focusInEvent(event);
  }

  //  void QQuickTextField::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTextFieldCall7 call = reinterpret_cast<CuteQQuickTextFieldCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextField::focusOutEvent(event);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickTextField::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTextFieldCall8 call = reinterpret_cast<CuteQQuickTextFieldCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextField::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickTextField::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTextFieldCall9 call = reinterpret_cast<CuteQQuickTextFieldCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextField::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickTextField::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTextFieldCall10 call = reinterpret_cast<CuteQQuickTextFieldCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextField::mousePressEvent(event);
  }

  //  void QQuickTextField::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTextFieldCall11 call = reinterpret_cast<CuteQQuickTextFieldCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextField::mouseMoveEvent(event);
  }

  //  void QQuickTextField::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTextFieldCall12 call = reinterpret_cast<CuteQQuickTextFieldCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextField::mouseReleaseEvent(event);
  }

  //  void QQuickTextField::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTextFieldCall13 call = reinterpret_cast<CuteQQuickTextFieldCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextField::mouseDoubleClickEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickTextField::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTextFieldCall14 call = reinterpret_cast<CuteQQuickTextFieldCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextField::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(im)
  //  QVariant QQuickTextInput::inputMethodQuery(Qt::InputMethodQuery
  //      property) const
  QVariant inputMethodQuery(Qt::InputMethodQuery property) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTextFieldCall15 call = reinterpret_cast<CuteQQuickTextFieldCall15>(taken[15]);
      const QVariant * given = call(this, static_cast<int>(property), &handled);
      if (handled && given) return *given;
    }
    return QQuickTextInput::inputMethodQuery(property);
  }
#endif  // QT_CONFIG(im)

  //  QRectF QQuickTextInput::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTextFieldCall16 call = reinterpret_cast<CuteQQuickTextFieldCall16>(taken[16]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextInput::boundingRect();
  }

  //  QRectF QQuickTextInput::clipRect() const
  QRectF clipRect() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTextFieldCall17 call = reinterpret_cast<CuteQQuickTextFieldCall17>(taken[17]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextInput::clipRect();
  }

  //  void QQuickTextInput::invalidate()
  void invalidate() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTextFieldCall18 call = reinterpret_cast<CuteQQuickTextFieldCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextInput::invalidate();
  }

  //  void QQuickTextInput::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTextFieldCall19 call = reinterpret_cast<CuteQQuickTextFieldCall19>(taken[19]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QQuickTextInput::keyPressEvent(ev);
  }

#if QT_CONFIG(im)
  //  void QQuickTextInput::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTextFieldCall20 call = reinterpret_cast<CuteQQuickTextFieldCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickTextInput::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickTextInput::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickTextFieldCall21 call = reinterpret_cast<CuteQQuickTextFieldCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextInput::mouseUngrabEvent();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickTextInput::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickTextFieldCall22 call = reinterpret_cast<CuteQQuickTextFieldCall22>(taken[22]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuickTextInput::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickTextInput::updatePolish()
  void updatePolish() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTextFieldCall23 call = reinterpret_cast<CuteQQuickTextFieldCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextInput::updatePolish();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickTextFieldCall24 call = reinterpret_cast<CuteQQuickTextFieldCall24>(taken[24]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickTextFieldCall25 call = reinterpret_cast<CuteQQuickTextFieldCall25>(taken[25]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickTextFieldCall26 call = reinterpret_cast<CuteQQuickTextFieldCall26>(taken[26]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickTextFieldCall27 call = reinterpret_cast<CuteQQuickTextFieldCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickTextFieldCall28 call = reinterpret_cast<CuteQQuickTextFieldCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickTextFieldCall29 call = reinterpret_cast<CuteQQuickTextFieldCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickTextFieldCall30 call = reinterpret_cast<CuteQQuickTextFieldCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickTextFieldCall31 call = reinterpret_cast<CuteQQuickTextFieldCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickTextFieldCall32 call = reinterpret_cast<CuteQQuickTextFieldCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickTextFieldCall33 call = reinterpret_cast<CuteQQuickTextFieldCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickTextFieldCall34 call = reinterpret_cast<CuteQQuickTextFieldCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickTextFieldCall35 call = reinterpret_cast<CuteQQuickTextFieldCall35>(taken[35]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickTextFieldCall36 call = reinterpret_cast<CuteQQuickTextFieldCall36>(taken[36]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickTextFieldCall37 call = reinterpret_cast<CuteQQuickTextFieldCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickTextFieldCall38 call = reinterpret_cast<CuteQQuickTextFieldCall38>(taken[38]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickTextFieldCall39 call = reinterpret_cast<CuteQQuickTextFieldCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickTextFieldCall40 call = reinterpret_cast<CuteQQuickTextFieldCall40>(taken[40]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickTextFieldCall41 call = reinterpret_cast<CuteQQuickTextFieldCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQuickTextFieldCall42 call = reinterpret_cast<CuteQQuickTextFieldCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTextField::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickTextField10metaObjectEv(
    const QQuickTextField *self) {
  return self->metaObject();
}

//  QString QQuickTextField::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickTextField2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTextField::tr(s, c, n));
}

//  QQuickTextField::QQuickTextField(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTextField *ritual_ZN15QQuickTextFieldC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickTextField(parent);
}

//  QQuickTextField::~QQuickTextField()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextFieldD1Ev(QQuickTextField *self) {
  delete self;
}

//  QFont QQuickTextField::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK15QQuickTextField4fontEv(const QQuickTextField *self) {
  return new QFont(self->font());
}

//  void QQuickTextField::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField7setFontERK5QFont(
    QQuickTextField *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QQuickItem *QQuickTextField::background() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK15QQuickTextField10backgroundEv(
    const QQuickTextField *self) {
  return self->background();
}

//  void QQuickTextField::setBackground(QQuickItem *background)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField13setBackgroundEP10QQuickItem(
    QQuickTextField *self,
    QQuickItem *background) {
  self->setBackground(background);
}

//  QString QQuickTextField::placeholderText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickTextField15placeholderTextEv(
    const QQuickTextField *self) {
  return new QString(self->placeholderText());
}

//  void QQuickTextField::setPlaceholderText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField18setPlaceholderTextERK7QString(
    QQuickTextField *self,
    const QString *text) {
  self->setPlaceholderText(*text);
}

//  Qt::FocusReason QQuickTextField::focusReason() const
extern "C" Q_DECL_EXPORT
Qt::FocusReason ritual_ZNK15QQuickTextField11focusReasonEv(
    const QQuickTextField *self) {
  return self->focusReason();
}

//  void QQuickTextField::setFocusReason(Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField14setFocusReasonEN2Qt11FocusReasonE(
    QQuickTextField *self,
    Qt::FocusReason reason) {
  self->setFocusReason(reason);
}

//  bool QQuickTextField::isHovered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextField9isHoveredEv(const QQuickTextField *self) {
  return self->isHovered();
}

//  void QQuickTextField::setHovered(bool hovered)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField10setHoveredEb(
    QQuickTextField *self,
    bool hovered) {
  self->setHovered(hovered);
}

//  bool QQuickTextField::isHoverEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextField14isHoverEnabledEv(
    const QQuickTextField *self) {
  return self->isHoverEnabled();
}

//  void QQuickTextField::setHoverEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField15setHoverEnabledEb(
    QQuickTextField *self,
    bool enabled) {
  self->setHoverEnabled(enabled);
}

//  void QQuickTextField::resetHoverEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField17resetHoverEnabledEv(QQuickTextField *self) {
  self->resetHoverEnabled();
}

//  QColor QQuickTextField::placeholderTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickTextField20placeholderTextColorEv(
    const QQuickTextField *self) {
  return new QColor(self->placeholderTextColor());
}

//  void QQuickTextField::setPlaceholderTextColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField23setPlaceholderTextColorERK6QColor(
    QQuickTextField *self,
    const QColor *color) {
  self->setPlaceholderTextColor(*color);
}

//  qreal QQuickTextField::implicitBackgroundWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextField23implicitBackgroundWidthEv(
    const QQuickTextField *self) {
  return self->implicitBackgroundWidth();
}

//  qreal QQuickTextField::implicitBackgroundHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextField24implicitBackgroundHeightEv(
    const QQuickTextField *self) {
  return self->implicitBackgroundHeight();
}

//  qreal QQuickTextField::topInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextField8topInsetEv(const QQuickTextField *self) {
  return self->topInset();
}

//  void QQuickTextField::setTopInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField11setTopInsetEd(
    QQuickTextField *self,
    qreal inset) {
  self->setTopInset(inset);
}

//  void QQuickTextField::resetTopInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField13resetTopInsetEv(QQuickTextField *self) {
  self->resetTopInset();
}

//  qreal QQuickTextField::leftInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextField9leftInsetEv(const QQuickTextField *self) {
  return self->leftInset();
}

//  void QQuickTextField::setLeftInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField12setLeftInsetEd(
    QQuickTextField *self,
    qreal inset) {
  self->setLeftInset(inset);
}

//  void QQuickTextField::resetLeftInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField14resetLeftInsetEv(QQuickTextField *self) {
  self->resetLeftInset();
}

//  qreal QQuickTextField::rightInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextField10rightInsetEv(
    const QQuickTextField *self) {
  return self->rightInset();
}

//  void QQuickTextField::setRightInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField13setRightInsetEd(
    QQuickTextField *self,
    qreal inset) {
  self->setRightInset(inset);
}

//  void QQuickTextField::resetRightInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField15resetRightInsetEv(QQuickTextField *self) {
  self->resetRightInset();
}

//  qreal QQuickTextField::bottomInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextField11bottomInsetEv(
    const QQuickTextField *self) {
  return self->bottomInset();
}

//  void QQuickTextField::setBottomInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField14setBottomInsetEd(
    QQuickTextField *self,
    qreal inset) {
  self->setBottomInset(inset);
}

//  void QQuickTextField::resetBottomInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField16resetBottomInsetEv(QQuickTextField *self) {
  self->resetBottomInset();
}

//  void QQuickTextField::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField10classBeginEv(QQuickTextField *self) {
  self->classBegin();
}

//  void QQuickTextField::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField17componentCompleteEv(QQuickTextField *self) {
  self->componentComplete();
}

//  void QQuickTextField::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickTextField *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickTextField::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField14geometryChangeERK6QRectFS2_(
    QQuickTextField *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickTextField::insetChange(const QMarginsF &newInset, const
//      QMarginsF &oldInset)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField11insetChangeERK9QMarginsFS2_(
    QQuickTextField *self,
    const QMarginsF *newInset,
    const QMarginsF *oldInset) {
  self->insetChange(*newInset, *oldInset);
}

//  QSGNode *QQuickTextField::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN15QQuickTextField15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickTextField *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->updatePaintNode(oldNode, data);
}

//  void QQuickTextField::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField12focusInEventEP11QFocusEvent(
    QQuickTextField *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickTextField::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField13focusOutEventEP11QFocusEvent(
    QQuickTextField *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickTextField::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField15hoverEnterEventEP11QHoverEvent(
    QQuickTextField *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickTextField::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField15hoverLeaveEventEP11QHoverEvent(
    QQuickTextField *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  void QQuickTextField::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField15mousePressEventEP11QMouseEvent(
    QQuickTextField *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickTextField::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField14mouseMoveEventEP11QMouseEvent(
    QQuickTextField *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickTextField::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField17mouseReleaseEventEP11QMouseEvent(
    QQuickTextField *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickTextField::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField21mouseDoubleClickEventEP11QMouseEvent(
    QQuickTextField *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QQuickTextField::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextField10timerEventEP11QTimerEvent(
    QQuickTextField *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  QQuickTextFieldPrivate *QQuickTextField::d_func()
extern "C" Q_DECL_EXPORT
QQuickTextFieldPrivate *ritual_ZN15QQuickTextField6d_funcEv(
    QQuickTextField *self) {
  return self->d_func();
}

//  const QQuickTextFieldPrivate *QQuickTextField::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextFieldPrivate *ritual_ZNK15QQuickTextField6d_funcEv(
    const QQuickTextField *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickTextField, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextField(
    QQuickTextField *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextField *>(self)->take(key, call);
}

//  void QQuickTextField::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField10classBeginEv(QQuickTextField *self) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::classBegin();
}

//  void QQuickTextField::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField17componentCompleteEv(
    QQuickTextField *self) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::componentComplete();
}

//  void QQuickTextField::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickTextField *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::itemChange(
      change,
      *value);
}

//  void QQuickTextField::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField14geometryChangeERK6QRectFS2_(
    QQuickTextField *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickTextField::insetChange(const QMarginsF &newInset, const
//      QMarginsF &oldInset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField11insetChangeERK9QMarginsFS2_(
    QQuickTextField *self,
    const QMarginsF *newInset,
    const QMarginsF *oldInset) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::insetChange(
      *newInset,
      *oldInset);
}

//  QSGNode *QQuickTextField::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN15QQuickTextField15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickTextField *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::updatePaintNode(
      oldNode,
      data);
}

//  void QQuickTextField::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField12focusInEventEP11QFocusEvent(
    QQuickTextField *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::focusInEvent(
      event);
}

//  void QQuickTextField::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField13focusOutEventEP11QFocusEvent(
    QQuickTextField *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::focusOutEvent(
      event);
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickTextField::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField15hoverEnterEventEP11QHoverEvent(
    QQuickTextField *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::hoverEnterEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickTextField::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField15hoverLeaveEventEP11QHoverEvent(
    QQuickTextField *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::hoverLeaveEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  void QQuickTextField::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField15mousePressEventEP11QMouseEvent(
    QQuickTextField *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::mousePressEvent(
      event);
}

//  void QQuickTextField::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField14mouseMoveEventEP11QMouseEvent(
    QQuickTextField *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::mouseMoveEvent(
      event);
}

//  void QQuickTextField::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField17mouseReleaseEventEP11QMouseEvent(
    QQuickTextField *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::mouseReleaseEvent(
      event);
}

//  void QQuickTextField::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField21mouseDoubleClickEventEP11QMouseEvent(
    QQuickTextField *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::mouseDoubleClickEvent(
      event);
}

//  void QQuickTextField::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextField10timerEventEP11QTimerEvent(
    QQuickTextField *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickTextField *>(self)->OwnQQuickTextField::timerEvent(
      event);
}
