//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextarea_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktextarea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qmargins.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickTextArea may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTextArea : QQuickTextArea {
  using QQuickTextArea::classBegin;
  using QQuickTextArea::componentComplete;
  using QQuickTextArea::itemChange;
  using QQuickTextArea::geometryChange;
  using QQuickTextArea::insetChange;
  using QQuickTextArea::updatePaintNode;
  using QQuickTextArea::focusInEvent;
  using QQuickTextArea::focusOutEvent;
  using QQuickTextArea::hoverEnterEvent;
  using QQuickTextArea::hoverLeaveEvent;
  using QQuickTextArea::mousePressEvent;
  using QQuickTextArea::mouseMoveEvent;
  using QQuickTextArea::mouseReleaseEvent;
  using QQuickTextArea::mouseDoubleClickEvent;
  using QQuickTextArea::timerEvent;
};

//  A QQuickTextArea that Python can take functions over in. Every QQuickTextArea
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickTextAreaCall0)(const void *, const QPointF *, int *);
typedef void (*CuteQQuickTextAreaCall1)(const void *, int *);
typedef void (*CuteQQuickTextAreaCall2)(const void *, int *);
typedef void (*CuteQQuickTextAreaCall3)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickTextAreaCall4)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickTextAreaCall5)(const void *, const QMarginsF *, const QMarginsF *, int *);
typedef void * (*CuteQQuickTextAreaCall6)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickTextAreaCall7)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTextAreaCall8)(const void *, QFocusEvent *, int *);
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickTextAreaCall9)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickTextAreaCall10)(const void *, QHoverEvent *, int *);
#endif  // QT_CONFIG(quicktemplates2_hover)
typedef void (*CuteQQuickTextAreaCall11)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextAreaCall12)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextAreaCall13)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextAreaCall14)(const void *, QMouseEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextAreaCall15)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickTextAreaCall16)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef const QRectF * (*CuteQQuickTextAreaCall17)(const void *, int *);
typedef const QRectF * (*CuteQQuickTextAreaCall18)(const void *, int *);
typedef void (*CuteQQuickTextAreaCall19)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextAreaCall20)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextAreaCall21)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickTextAreaCall22)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickTextAreaCall23)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickTextAreaCall24)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickTextAreaCall25)(const void *, int *);
typedef bool (*CuteQQuickTextAreaCall26)(const void *, int *);
typedef void * (*CuteQQuickTextAreaCall27)(const void *, int *);
typedef void (*CuteQQuickTextAreaCall28)(const void *, int *);
typedef void (*CuteQQuickTextAreaCall29)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTextAreaCall30)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTextAreaCall31)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextAreaCall32)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextAreaCall33)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextAreaCall34)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextAreaCall35)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickTextAreaCall36)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickTextAreaCall37)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextAreaCall38)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextAreaCall39)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextAreaCall40)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextAreaCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextAreaCall42)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTextArea : public QQuickTextArea {
public:
  using QQuickTextArea::QQuickTextArea;
  void *taken[43] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QQuickTextArea11insetChangeERK9QMarginsFS2_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
#if QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_hover)
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[14] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickTextInterface10invalidateEv")) {
      taken[19] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[20] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[29] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
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

  //  bool QQuickTextArea::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextAreaCall0 call = reinterpret_cast<CuteQQuickTextAreaCall0>(taken[0]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickTextArea::contains(point);
  }

  //  void QQuickTextArea::classBegin()
  void classBegin() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextAreaCall1 call = reinterpret_cast<CuteQQuickTextAreaCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextArea::classBegin();
  }

  //  void QQuickTextArea::componentComplete()
  void componentComplete() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextAreaCall2 call = reinterpret_cast<CuteQQuickTextAreaCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextArea::componentComplete();
  }

  //  void QQuickTextArea::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTextAreaCall3 call = reinterpret_cast<CuteQQuickTextAreaCall3>(taken[3]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickTextArea::itemChange(change, value);
  }

  //  void QQuickTextArea::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTextAreaCall4 call = reinterpret_cast<CuteQQuickTextAreaCall4>(taken[4]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickTextArea::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickTextArea::insetChange(const QMarginsF &newInset, const
  //      QMarginsF &oldInset)
  void insetChange(
      const QMarginsF &newInset,
      const QMarginsF &oldInset) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTextAreaCall5 call = reinterpret_cast<CuteQQuickTextAreaCall5>(taken[5]);
      call(this, &newInset, &oldInset, &handled);
      if (handled) return;
    }
    QQuickTextArea::insetChange(newInset, oldInset);
  }

  //  QSGNode *QQuickTextArea::updatePaintNode(QSGNode *oldNode,
  //      UpdatePaintNodeData *data)
  QSGNode *updatePaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *data) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTextAreaCall6 call = reinterpret_cast<CuteQQuickTextAreaCall6>(taken[6]);
      void * given = call(this, oldNode, data, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickTextArea::updatePaintNode(oldNode, data);
  }

  //  void QQuickTextArea::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTextAreaCall7 call = reinterpret_cast<CuteQQuickTextAreaCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextArea::focusInEvent(event);
  }

  //  void QQuickTextArea::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTextAreaCall8 call = reinterpret_cast<CuteQQuickTextAreaCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextArea::focusOutEvent(event);
  }

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickTextArea::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTextAreaCall9 call = reinterpret_cast<CuteQQuickTextAreaCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextArea::hoverEnterEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
  //  void QQuickTextArea::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTextAreaCall10 call = reinterpret_cast<CuteQQuickTextAreaCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextArea::hoverLeaveEvent(event);
  }
#endif  // QT_CONFIG(quicktemplates2_hover)

  //  void QQuickTextArea::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTextAreaCall11 call = reinterpret_cast<CuteQQuickTextAreaCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextArea::mousePressEvent(event);
  }

  //  void QQuickTextArea::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTextAreaCall12 call = reinterpret_cast<CuteQQuickTextAreaCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextArea::mouseMoveEvent(event);
  }

  //  void QQuickTextArea::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTextAreaCall13 call = reinterpret_cast<CuteQQuickTextAreaCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextArea::mouseReleaseEvent(event);
  }

  //  void QQuickTextArea::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTextAreaCall14 call = reinterpret_cast<CuteQQuickTextAreaCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextArea::mouseDoubleClickEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickTextArea::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTextAreaCall15 call = reinterpret_cast<CuteQQuickTextAreaCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextArea::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(im)
  //  QVariant QQuickTextEdit::inputMethodQuery(Qt::InputMethodQuery
  //      property) const
  QVariant inputMethodQuery(Qt::InputMethodQuery property) const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTextAreaCall16 call = reinterpret_cast<CuteQQuickTextAreaCall16>(taken[16]);
      const QVariant * given = call(this, static_cast<int>(property), &handled);
      if (handled && given) return *given;
    }
    return QQuickTextEdit::inputMethodQuery(property);
  }
#endif  // QT_CONFIG(im)

  //  QRectF QQuickTextEdit::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTextAreaCall17 call = reinterpret_cast<CuteQQuickTextAreaCall17>(taken[17]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextEdit::boundingRect();
  }

  //  QRectF QQuickTextEdit::clipRect() const
  QRectF clipRect() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTextAreaCall18 call = reinterpret_cast<CuteQQuickTextAreaCall18>(taken[18]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextEdit::clipRect();
  }

  //  void QQuickTextEdit::invalidate()
  void invalidate() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTextAreaCall19 call = reinterpret_cast<CuteQQuickTextAreaCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextEdit::invalidate();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickTextEdit::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTextAreaCall20 call = reinterpret_cast<CuteQQuickTextAreaCall20>(taken[20]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickTextEdit::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickTextEdit::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickTextAreaCall21 call = reinterpret_cast<CuteQQuickTextAreaCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickTextEdit::keyPressEvent(a0);
  }

  //  void QQuickTextEdit::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickTextAreaCall22 call = reinterpret_cast<CuteQQuickTextAreaCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickTextEdit::keyReleaseEvent(a0);
  }

  //  void QQuickTextEdit::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTextAreaCall23 call = reinterpret_cast<CuteQQuickTextAreaCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::hoverMoveEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickTextEdit::inputMethodEvent(QInputMethodEvent *e)
  void inputMethodEvent(QInputMethodEvent *e) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickTextAreaCall24 call = reinterpret_cast<CuteQQuickTextAreaCall24>(taken[24]);
      call(this, e, &handled);
      if (handled) return;
    }
    QQuickTextEdit::inputMethodEvent(e);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickTextEdit::updatePolish()
  void updatePolish() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickTextAreaCall25 call = reinterpret_cast<CuteQQuickTextAreaCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextEdit::updatePolish();
  }

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickTextAreaCall26 call = reinterpret_cast<CuteQQuickTextAreaCall26>(taken[26]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickTextAreaCall27 call = reinterpret_cast<CuteQQuickTextAreaCall27>(taken[27]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickTextAreaCall28 call = reinterpret_cast<CuteQQuickTextAreaCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickTextAreaCall29 call = reinterpret_cast<CuteQQuickTextAreaCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickTextAreaCall30 call = reinterpret_cast<CuteQQuickTextAreaCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickTextAreaCall31 call = reinterpret_cast<CuteQQuickTextAreaCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickTextAreaCall32 call = reinterpret_cast<CuteQQuickTextAreaCall32>(taken[32]);
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
      CuteQQuickTextAreaCall33 call = reinterpret_cast<CuteQQuickTextAreaCall33>(taken[33]);
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
      CuteQQuickTextAreaCall34 call = reinterpret_cast<CuteQQuickTextAreaCall34>(taken[34]);
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
      CuteQQuickTextAreaCall35 call = reinterpret_cast<CuteQQuickTextAreaCall35>(taken[35]);
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
      CuteQQuickTextAreaCall36 call = reinterpret_cast<CuteQQuickTextAreaCall36>(taken[36]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickTextAreaCall37 call = reinterpret_cast<CuteQQuickTextAreaCall37>(taken[37]);
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
      CuteQQuickTextAreaCall38 call = reinterpret_cast<CuteQQuickTextAreaCall38>(taken[38]);
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
      CuteQQuickTextAreaCall39 call = reinterpret_cast<CuteQQuickTextAreaCall39>(taken[39]);
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
      CuteQQuickTextAreaCall40 call = reinterpret_cast<CuteQQuickTextAreaCall40>(taken[40]);
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
      CuteQQuickTextAreaCall41 call = reinterpret_cast<CuteQQuickTextAreaCall41>(taken[41]);
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
      CuteQQuickTextAreaCall42 call = reinterpret_cast<CuteQQuickTextAreaCall42>(taken[42]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTextArea::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickTextArea10metaObjectEv(
    const QQuickTextArea *self) {
  return self->metaObject();
}

//  QString QQuickTextArea::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickTextArea2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTextArea::tr(s, c, n));
}

//  void QQuickTextArea::qt_qmlMarker_attached()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea21qt_qmlMarker_attachedEv(
    QQuickTextArea *self) {
  self->qt_qmlMarker_attached();
}

//  QQuickTextArea::QQuickTextArea(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTextArea *ritual_ZN14QQuickTextAreaC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickTextArea(parent);
}

//  QQuickTextArea::~QQuickTextArea()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextAreaD1Ev(QQuickTextArea *self) {
  delete self;
}

//  QQuickTextAreaAttached *QQuickTextArea::qmlAttachedProperties(QObject
//      *object)
extern "C" Q_DECL_EXPORT
QQuickTextAreaAttached *ritual_ZN14QQuickTextArea21qmlAttachedPropertiesEP7QObject(
    QObject *object) {
  return QQuickTextArea::qmlAttachedProperties(object);
}

//  QFont QQuickTextArea::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQuickTextArea4fontEv(const QQuickTextArea *self) {
  return new QFont(self->font());
}

//  void QQuickTextArea::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea7setFontERK5QFont(
    QQuickTextArea *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QQuickItem *QQuickTextArea::background() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK14QQuickTextArea10backgroundEv(
    const QQuickTextArea *self) {
  return self->background();
}

//  void QQuickTextArea::setBackground(QQuickItem *background)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea13setBackgroundEP10QQuickItem(
    QQuickTextArea *self,
    QQuickItem *background) {
  self->setBackground(background);
}

//  QString QQuickTextArea::placeholderText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickTextArea15placeholderTextEv(
    const QQuickTextArea *self) {
  return new QString(self->placeholderText());
}

//  void QQuickTextArea::setPlaceholderText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea18setPlaceholderTextERK7QString(
    QQuickTextArea *self,
    const QString *text) {
  self->setPlaceholderText(*text);
}

//  Qt::FocusReason QQuickTextArea::focusReason() const
extern "C" Q_DECL_EXPORT
Qt::FocusReason ritual_ZNK14QQuickTextArea11focusReasonEv(
    const QQuickTextArea *self) {
  return self->focusReason();
}

//  void QQuickTextArea::setFocusReason(Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea14setFocusReasonEN2Qt11FocusReasonE(
    QQuickTextArea *self,
    Qt::FocusReason reason) {
  self->setFocusReason(reason);
}

//  bool QQuickTextArea::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextArea8containsERK7QPointF(
    const QQuickTextArea *self,
    const QPointF *point) {
  return self->contains(*point);
}

//  bool QQuickTextArea::isHovered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextArea9isHoveredEv(const QQuickTextArea *self) {
  return self->isHovered();
}

//  void QQuickTextArea::setHovered(bool hovered)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea10setHoveredEb(
    QQuickTextArea *self,
    bool hovered) {
  self->setHovered(hovered);
}

//  bool QQuickTextArea::isHoverEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextArea14isHoverEnabledEv(
    const QQuickTextArea *self) {
  return self->isHoverEnabled();
}

//  void QQuickTextArea::setHoverEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea15setHoverEnabledEb(
    QQuickTextArea *self,
    bool enabled) {
  self->setHoverEnabled(enabled);
}

//  void QQuickTextArea::resetHoverEnabled()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea17resetHoverEnabledEv(QQuickTextArea *self) {
  self->resetHoverEnabled();
}

//  QColor QQuickTextArea::placeholderTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK14QQuickTextArea20placeholderTextColorEv(
    const QQuickTextArea *self) {
  return new QColor(self->placeholderTextColor());
}

//  void QQuickTextArea::setPlaceholderTextColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea23setPlaceholderTextColorERK6QColor(
    QQuickTextArea *self,
    const QColor *color) {
  self->setPlaceholderTextColor(*color);
}

//  qreal QQuickTextArea::implicitBackgroundWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextArea23implicitBackgroundWidthEv(
    const QQuickTextArea *self) {
  return self->implicitBackgroundWidth();
}

//  qreal QQuickTextArea::implicitBackgroundHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextArea24implicitBackgroundHeightEv(
    const QQuickTextArea *self) {
  return self->implicitBackgroundHeight();
}

//  qreal QQuickTextArea::topInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextArea8topInsetEv(const QQuickTextArea *self) {
  return self->topInset();
}

//  void QQuickTextArea::setTopInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea11setTopInsetEd(
    QQuickTextArea *self,
    qreal inset) {
  self->setTopInset(inset);
}

//  void QQuickTextArea::resetTopInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea13resetTopInsetEv(QQuickTextArea *self) {
  self->resetTopInset();
}

//  qreal QQuickTextArea::leftInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextArea9leftInsetEv(const QQuickTextArea *self) {
  return self->leftInset();
}

//  void QQuickTextArea::setLeftInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea12setLeftInsetEd(
    QQuickTextArea *self,
    qreal inset) {
  self->setLeftInset(inset);
}

//  void QQuickTextArea::resetLeftInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea14resetLeftInsetEv(QQuickTextArea *self) {
  self->resetLeftInset();
}

//  qreal QQuickTextArea::rightInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextArea10rightInsetEv(const QQuickTextArea *self) {
  return self->rightInset();
}

//  void QQuickTextArea::setRightInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea13setRightInsetEd(
    QQuickTextArea *self,
    qreal inset) {
  self->setRightInset(inset);
}

//  void QQuickTextArea::resetRightInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea15resetRightInsetEv(QQuickTextArea *self) {
  self->resetRightInset();
}

//  qreal QQuickTextArea::bottomInset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextArea11bottomInsetEv(const QQuickTextArea *self) {
  return self->bottomInset();
}

//  void QQuickTextArea::setBottomInset(qreal inset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea14setBottomInsetEd(
    QQuickTextArea *self,
    qreal inset) {
  self->setBottomInset(inset);
}

//  void QQuickTextArea::resetBottomInset()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea16resetBottomInsetEv(QQuickTextArea *self) {
  self->resetBottomInset();
}

//  void QQuickTextArea::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea10classBeginEv(QQuickTextArea *self) {
  self->classBegin();
}

//  void QQuickTextArea::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea17componentCompleteEv(QQuickTextArea *self) {
  self->componentComplete();
}

//  void QQuickTextArea::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickTextArea *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickTextArea::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea14geometryChangeERK6QRectFS2_(
    QQuickTextArea *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickTextArea::insetChange(const QMarginsF &newInset, const
//      QMarginsF &oldInset)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea11insetChangeERK9QMarginsFS2_(
    QQuickTextArea *self,
    const QMarginsF *newInset,
    const QMarginsF *oldInset) {
  self->insetChange(*newInset, *oldInset);
}

//  QSGNode *QQuickTextArea::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN14QQuickTextArea15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickTextArea *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->updatePaintNode(oldNode, data);
}

//  void QQuickTextArea::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea12focusInEventEP11QFocusEvent(
    QQuickTextArea *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickTextArea::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea13focusOutEventEP11QFocusEvent(
    QQuickTextArea *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickTextArea::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea15hoverEnterEventEP11QHoverEvent(
    QQuickTextArea *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickTextArea::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea15hoverLeaveEventEP11QHoverEvent(
    QQuickTextArea *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  void QQuickTextArea::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea15mousePressEventEP11QMouseEvent(
    QQuickTextArea *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickTextArea::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea14mouseMoveEventEP11QMouseEvent(
    QQuickTextArea *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickTextArea::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea17mouseReleaseEventEP11QMouseEvent(
    QQuickTextArea *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickTextArea::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea21mouseDoubleClickEventEP11QMouseEvent(
    QQuickTextArea *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QQuickTextArea::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextArea10timerEventEP11QTimerEvent(
    QQuickTextArea *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  QQuickTextAreaPrivate *QQuickTextArea::d_func()
extern "C" Q_DECL_EXPORT
QQuickTextAreaPrivate *ritual_ZN14QQuickTextArea6d_funcEv(
    QQuickTextArea *self) {
  return self->d_func();
}

//  const QQuickTextAreaPrivate *QQuickTextArea::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextAreaPrivate *ritual_ZNK14QQuickTextArea6d_funcEv(
    const QQuickTextArea *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickTextArea, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextArea(
    QQuickTextArea *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextArea *>(self)->take(key, call);
}

//  bool QQuickTextArea::contains(const QPointF &point) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK14QQuickTextArea8containsERK7QPointF(
    const QQuickTextArea *self,
    const QPointF *point) {
  return self->QQuickTextArea::contains(*point);
}

//  void QQuickTextArea::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea10classBeginEv(QQuickTextArea *self) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::classBegin();
}

//  void QQuickTextArea::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea17componentCompleteEv(
    QQuickTextArea *self) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::componentComplete();
}

//  void QQuickTextArea::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickTextArea *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::itemChange(
      change,
      *value);
}

//  void QQuickTextArea::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea14geometryChangeERK6QRectFS2_(
    QQuickTextArea *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickTextArea::insetChange(const QMarginsF &newInset, const
//      QMarginsF &oldInset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea11insetChangeERK9QMarginsFS2_(
    QQuickTextArea *self,
    const QMarginsF *newInset,
    const QMarginsF *oldInset) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::insetChange(
      *newInset,
      *oldInset);
}

//  QSGNode *QQuickTextArea::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN14QQuickTextArea15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickTextArea *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::updatePaintNode(
      oldNode,
      data);
}

//  void QQuickTextArea::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea12focusInEventEP11QFocusEvent(
    QQuickTextArea *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::focusInEvent(
      event);
}

//  void QQuickTextArea::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea13focusOutEventEP11QFocusEvent(
    QQuickTextArea *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::focusOutEvent(
      event);
}

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickTextArea::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea15hoverEnterEventEP11QHoverEvent(
    QQuickTextArea *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::hoverEnterEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

#if QT_CONFIG(quicktemplates2_hover)
//  void QQuickTextArea::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea15hoverLeaveEventEP11QHoverEvent(
    QQuickTextArea *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::hoverLeaveEvent(
      event);
}
#endif  // QT_CONFIG(quicktemplates2_hover)

//  void QQuickTextArea::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea15mousePressEventEP11QMouseEvent(
    QQuickTextArea *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::mousePressEvent(
      event);
}

//  void QQuickTextArea::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea14mouseMoveEventEP11QMouseEvent(
    QQuickTextArea *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::mouseMoveEvent(
      event);
}

//  void QQuickTextArea::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea17mouseReleaseEventEP11QMouseEvent(
    QQuickTextArea *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::mouseReleaseEvent(
      event);
}

//  void QQuickTextArea::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea21mouseDoubleClickEventEP11QMouseEvent(
    QQuickTextArea *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::mouseDoubleClickEvent(
      event);
}

//  void QQuickTextArea::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextArea10timerEventEP11QTimerEvent(
    QQuickTextArea *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickTextArea *>(self)->OwnQQuickTextArea::timerEvent(
      event);
}
