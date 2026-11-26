//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextedit_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qfont.h>
#include <QtGui/qcolor.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtGui/qtextobject.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickTextEdit may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTextEdit : QQuickTextEdit {
  using QQuickTextEdit::geometryChange;
  using QQuickTextEdit::itemChange;
  using QQuickTextEdit::event;
  using QQuickTextEdit::keyPressEvent;
  using QQuickTextEdit::keyReleaseEvent;
  using QQuickTextEdit::focusInEvent;
  using QQuickTextEdit::focusOutEvent;
  using QQuickTextEdit::hoverEnterEvent;
  using QQuickTextEdit::hoverMoveEvent;
  using QQuickTextEdit::hoverLeaveEvent;
  using QQuickTextEdit::mousePressEvent;
  using QQuickTextEdit::mouseReleaseEvent;
  using QQuickTextEdit::mouseDoubleClickEvent;
  using QQuickTextEdit::mouseMoveEvent;
  using QQuickTextEdit::inputMethodEvent;
  using QQuickTextEdit::updatePaintNode;
  using QQuickTextEdit::updatePolish;
};

//  A QQuickTextEdit that Python can take functions over in. Every QQuickTextEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTextEditCall0)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickTextEditCall1)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef const QRectF * (*CuteQQuickTextEditCall2)(const void *, int *);
typedef const QRectF * (*CuteQQuickTextEditCall3)(const void *, int *);
typedef void (*CuteQQuickTextEditCall4)(const void *, int *);
typedef void (*CuteQQuickTextEditCall5)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickTextEditCall6)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextEditCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextEditCall8)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickTextEditCall9)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickTextEditCall10)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTextEditCall11)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTextEditCall12)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTextEditCall13)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTextEditCall14)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTextEditCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextEditCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextEditCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextEditCall18)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickTextEditCall19)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void * (*CuteQQuickTextEditCall20)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickTextEditCall21)(const void *, int *);
typedef bool (*CuteQQuickTextEditCall22)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickTextEditCall23)(const void *, int *);
typedef void * (*CuteQQuickTextEditCall24)(const void *, int *);
typedef void (*CuteQQuickTextEditCall25)(const void *, int *);
typedef void (*CuteQQuickTextEditCall26)(const void *, int *);
typedef void (*CuteQQuickTextEditCall27)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTextEditCall28)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTextEditCall29)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextEditCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextEditCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextEditCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextEditCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickTextEditCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickTextEditCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextEditCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextEditCall37)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextEditCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextEditCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextEditCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextEditCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTextEdit : public QQuickTextEdit {
public:
  using QQuickTextEdit::QQuickTextEdit;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickTextInterface10invalidateEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[29] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[35] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[41] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QQuickTextEdit::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextEditCall0 call = reinterpret_cast<CuteQQuickTextEditCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextEdit::componentComplete();
  }

#if QT_CONFIG(im)
  //  QVariant QQuickTextEdit::inputMethodQuery(Qt::InputMethodQuery
  //      property) const
  QVariant inputMethodQuery(Qt::InputMethodQuery property) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextEditCall1 call = reinterpret_cast<CuteQQuickTextEditCall1>(taken[1]);
      const QVariant * given = call(this, static_cast<int>(property), &handled);
      if (handled && given) return *given;
    }
    return QQuickTextEdit::inputMethodQuery(property);
  }
#endif  // QT_CONFIG(im)

  //  QRectF QQuickTextEdit::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextEditCall2 call = reinterpret_cast<CuteQQuickTextEditCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextEdit::boundingRect();
  }

  //  QRectF QQuickTextEdit::clipRect() const
  QRectF clipRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTextEditCall3 call = reinterpret_cast<CuteQQuickTextEditCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextEdit::clipRect();
  }

  //  void QQuickTextEdit::invalidate()
  void invalidate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTextEditCall4 call = reinterpret_cast<CuteQQuickTextEditCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextEdit::invalidate();
  }

  //  void QQuickTextEdit::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTextEditCall5 call = reinterpret_cast<CuteQQuickTextEditCall5>(taken[5]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickTextEdit::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickTextEdit::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTextEditCall6 call = reinterpret_cast<CuteQQuickTextEditCall6>(taken[6]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickTextEdit::itemChange(change, value);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickTextEdit::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTextEditCall7 call = reinterpret_cast<CuteQQuickTextEditCall7>(taken[7]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickTextEdit::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickTextEdit::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTextEditCall8 call = reinterpret_cast<CuteQQuickTextEditCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickTextEdit::keyPressEvent(a0);
  }

  //  void QQuickTextEdit::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTextEditCall9 call = reinterpret_cast<CuteQQuickTextEditCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickTextEdit::keyReleaseEvent(a0);
  }

  //  void QQuickTextEdit::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTextEditCall10 call = reinterpret_cast<CuteQQuickTextEditCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::focusInEvent(event);
  }

  //  void QQuickTextEdit::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTextEditCall11 call = reinterpret_cast<CuteQQuickTextEditCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::focusOutEvent(event);
  }

  //  void QQuickTextEdit::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTextEditCall12 call = reinterpret_cast<CuteQQuickTextEditCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::hoverEnterEvent(event);
  }

  //  void QQuickTextEdit::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTextEditCall13 call = reinterpret_cast<CuteQQuickTextEditCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::hoverMoveEvent(event);
  }

  //  void QQuickTextEdit::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTextEditCall14 call = reinterpret_cast<CuteQQuickTextEditCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::hoverLeaveEvent(event);
  }

  //  void QQuickTextEdit::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTextEditCall15 call = reinterpret_cast<CuteQQuickTextEditCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::mousePressEvent(event);
  }

  //  void QQuickTextEdit::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTextEditCall16 call = reinterpret_cast<CuteQQuickTextEditCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::mouseReleaseEvent(event);
  }

  //  void QQuickTextEdit::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTextEditCall17 call = reinterpret_cast<CuteQQuickTextEditCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::mouseDoubleClickEvent(event);
  }

  //  void QQuickTextEdit::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTextEditCall18 call = reinterpret_cast<CuteQQuickTextEditCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::mouseMoveEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickTextEdit::inputMethodEvent(QInputMethodEvent *e)
  void inputMethodEvent(QInputMethodEvent *e) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTextEditCall19 call = reinterpret_cast<CuteQQuickTextEditCall19>(taken[19]);
      call(this, e, &handled);
      if (handled) return;
    }
    QQuickTextEdit::inputMethodEvent(e);
  }
#endif  // QT_CONFIG(im)

  //  QSGNode *QQuickTextEdit::updatePaintNode(QSGNode *oldNode,
  //      UpdatePaintNodeData *updatePaintNodeData)
  QSGNode *updatePaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *updatePaintNodeData) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTextEditCall20 call = reinterpret_cast<CuteQQuickTextEditCall20>(taken[20]);
      void * given = call(this, oldNode, updatePaintNodeData, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickTextEdit::updatePaintNode(oldNode, updatePaintNodeData);
  }

  //  void QQuickTextEdit::updatePolish()
  void updatePolish() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickTextEditCall21 call = reinterpret_cast<CuteQQuickTextEditCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextEdit::updatePolish();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickTextEditCall22 call = reinterpret_cast<CuteQQuickTextEditCall22>(taken[22]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTextEditCall23 call = reinterpret_cast<CuteQQuickTextEditCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickTextEditCall24 call = reinterpret_cast<CuteQQuickTextEditCall24>(taken[24]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickTextEditCall25 call = reinterpret_cast<CuteQQuickTextEditCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickTextEditCall26 call = reinterpret_cast<CuteQQuickTextEditCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickTextEditCall27 call = reinterpret_cast<CuteQQuickTextEditCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickTextEditCall28 call = reinterpret_cast<CuteQQuickTextEditCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickTextEditCall29 call = reinterpret_cast<CuteQQuickTextEditCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickTextEditCall30 call = reinterpret_cast<CuteQQuickTextEditCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickTextEditCall31 call = reinterpret_cast<CuteQQuickTextEditCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickTextEditCall32 call = reinterpret_cast<CuteQQuickTextEditCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickTextEditCall33 call = reinterpret_cast<CuteQQuickTextEditCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickTextEditCall34 call = reinterpret_cast<CuteQQuickTextEditCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickTextEditCall35 call = reinterpret_cast<CuteQQuickTextEditCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickTextEditCall36 call = reinterpret_cast<CuteQQuickTextEditCall36>(taken[36]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickTextEditCall37 call = reinterpret_cast<CuteQQuickTextEditCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickTextEditCall38 call = reinterpret_cast<CuteQQuickTextEditCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickTextEditCall39 call = reinterpret_cast<CuteQQuickTextEditCall39>(taken[39]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickTextEditCall40 call = reinterpret_cast<CuteQQuickTextEditCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQuickTextEditCall41 call = reinterpret_cast<CuteQQuickTextEditCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTextEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickTextEdit10metaObjectEv(
    const QQuickTextEdit *self) {
  return self->metaObject();
}

//  void *QQuickTextEdit::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QQuickTextEdit11qt_metacastEPKc(
    QQuickTextEdit *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTextEdit::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QQuickTextEdit11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTextEdit *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickTextEdit::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickTextEdit2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTextEdit::tr(s, c, n));
}

//  QQuickTextEdit::QQuickTextEdit(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTextEdit *ritual_ZN14QQuickTextEditC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickTextEdit(parent);
}

//  QQuickTextEdit::~QQuickTextEdit()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEditD1Ev(QQuickTextEdit *self) {
  delete self;
}

//  QString QQuickTextEdit::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickTextEdit4textEv(const QQuickTextEdit *self) {
  return new QString(self->text());
}

//  void QQuickTextEdit::setText(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit7setTextERK7QString(
    QQuickTextEdit *self,
    const QString *a0) {
  self->setText(*a0);
}

//  QString QQuickTextEdit::preeditText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickTextEdit11preeditTextEv(
    const QQuickTextEdit *self) {
  return new QString(self->preeditText());
}

//  TextFormat QQuickTextEdit::textFormat() const
extern "C" Q_DECL_EXPORT
QQuickTextEdit::TextFormat ritual_ZNK14QQuickTextEdit10textFormatEv(
    const QQuickTextEdit *self) {
  return self->textFormat();
}

//  void QQuickTextEdit::setTextFormat(TextFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit13setTextFormatENS_10TextFormatE(
    QQuickTextEdit *self,
    QQuickTextEdit::TextFormat format) {
  self->setTextFormat(format);
}

//  QFont QQuickTextEdit::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QQuickTextEdit4fontEv(const QQuickTextEdit *self) {
  return new QFont(self->font());
}

//  void QQuickTextEdit::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit7setFontERK5QFont(
    QQuickTextEdit *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QColor QQuickTextEdit::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK14QQuickTextEdit5colorEv(const QQuickTextEdit *self) {
  return new QColor(self->color());
}

//  void QQuickTextEdit::setColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit8setColorERK6QColor(
    QQuickTextEdit *self,
    const QColor *c) {
  self->setColor(*c);
}

//  QColor QQuickTextEdit::selectionColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK14QQuickTextEdit14selectionColorEv(
    const QQuickTextEdit *self) {
  return new QColor(self->selectionColor());
}

//  void QQuickTextEdit::setSelectionColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17setSelectionColorERK6QColor(
    QQuickTextEdit *self,
    const QColor *c) {
  self->setSelectionColor(*c);
}

//  QColor QQuickTextEdit::selectedTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK14QQuickTextEdit17selectedTextColorEv(
    const QQuickTextEdit *self) {
  return new QColor(self->selectedTextColor());
}

//  void QQuickTextEdit::setSelectedTextColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit20setSelectedTextColorERK6QColor(
    QQuickTextEdit *self,
    const QColor *c) {
  self->setSelectedTextColor(*c);
}

//  HAlignment QQuickTextEdit::hAlign() const
extern "C" Q_DECL_EXPORT
QQuickTextEdit::HAlignment ritual_ZNK14QQuickTextEdit6hAlignEv(
    const QQuickTextEdit *self) {
  return self->hAlign();
}

//  void QQuickTextEdit::setHAlign(HAlignment align)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit9setHAlignENS_10HAlignmentE(
    QQuickTextEdit *self,
    QQuickTextEdit::HAlignment align) {
  self->setHAlign(align);
}

//  void QQuickTextEdit::resetHAlign()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit11resetHAlignEv(QQuickTextEdit *self) {
  self->resetHAlign();
}

//  HAlignment QQuickTextEdit::effectiveHAlign() const
extern "C" Q_DECL_EXPORT
QQuickTextEdit::HAlignment ritual_ZNK14QQuickTextEdit15effectiveHAlignEv(
    const QQuickTextEdit *self) {
  return self->effectiveHAlign();
}

//  VAlignment QQuickTextEdit::vAlign() const
extern "C" Q_DECL_EXPORT
QQuickTextEdit::VAlignment ritual_ZNK14QQuickTextEdit6vAlignEv(
    const QQuickTextEdit *self) {
  return self->vAlign();
}

//  void QQuickTextEdit::setVAlign(VAlignment align)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit9setVAlignENS_10VAlignmentE(
    QQuickTextEdit *self,
    QQuickTextEdit::VAlignment align) {
  self->setVAlign(align);
}

//  WrapMode QQuickTextEdit::wrapMode() const
extern "C" Q_DECL_EXPORT
QQuickTextEdit::WrapMode ritual_ZNK14QQuickTextEdit8wrapModeEv(
    const QQuickTextEdit *self) {
  return self->wrapMode();
}

//  void QQuickTextEdit::setWrapMode(WrapMode w)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit11setWrapModeENS_8WrapModeE(
    QQuickTextEdit *self,
    QQuickTextEdit::WrapMode w) {
  self->setWrapMode(w);
}

//  int QQuickTextEdit::lineCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTextEdit9lineCountEv(const QQuickTextEdit *self) {
  return self->lineCount();
}

//  int QQuickTextEdit::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTextEdit6lengthEv(const QQuickTextEdit *self) {
  return self->length();
}

//  bool QQuickTextEdit::isCursorVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextEdit15isCursorVisibleEv(
    const QQuickTextEdit *self) {
  return self->isCursorVisible();
}

//  void QQuickTextEdit::setCursorVisible(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit16setCursorVisibleEb(
    QQuickTextEdit *self,
    bool on) {
  self->setCursorVisible(on);
}

//  int QQuickTextEdit::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTextEdit14cursorPositionEv(
    const QQuickTextEdit *self) {
  return self->cursorPosition();
}

//  void QQuickTextEdit::setCursorPosition(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17setCursorPositionEi(
    QQuickTextEdit *self,
    int pos) {
  self->setCursorPosition(pos);
}

//  QQmlComponent *QQuickTextEdit::cursorDelegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK14QQuickTextEdit14cursorDelegateEv(
    const QQuickTextEdit *self) {
  return self->cursorDelegate();
}

//  void QQuickTextEdit::setCursorDelegate(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17setCursorDelegateEP13QQmlComponent(
    QQuickTextEdit *self,
    QQmlComponent *a0) {
  self->setCursorDelegate(a0);
}

//  bool QQuickTextEdit::overwriteMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextEdit13overwriteModeEv(
    const QQuickTextEdit *self) {
  return self->overwriteMode();
}

//  void QQuickTextEdit::setOverwriteMode(bool overwrite)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit16setOverwriteModeEb(
    QQuickTextEdit *self,
    bool overwrite) {
  self->setOverwriteMode(overwrite);
}

//  int QQuickTextEdit::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTextEdit14selectionStartEv(
    const QQuickTextEdit *self) {
  return self->selectionStart();
}

//  int QQuickTextEdit::selectionEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTextEdit12selectionEndEv(const QQuickTextEdit *self) {
  return self->selectionEnd();
}

//  QString QQuickTextEdit::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickTextEdit12selectedTextEv(
    const QQuickTextEdit *self) {
  return new QString(self->selectedText());
}

//  bool QQuickTextEdit::focusOnPress() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextEdit12focusOnPressEv(const QQuickTextEdit *self) {
  return self->focusOnPress();
}

//  void QQuickTextEdit::setFocusOnPress(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15setFocusOnPressEb(
    QQuickTextEdit *self,
    bool on) {
  self->setFocusOnPress(on);
}

//  bool QQuickTextEdit::persistentSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextEdit19persistentSelectionEv(
    const QQuickTextEdit *self) {
  return self->persistentSelection();
}

//  void QQuickTextEdit::setPersistentSelection(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit22setPersistentSelectionEb(
    QQuickTextEdit *self,
    bool on) {
  self->setPersistentSelection(on);
}

//  qreal QQuickTextEdit::textMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextEdit10textMarginEv(const QQuickTextEdit *self) {
  return self->textMargin();
}

//  void QQuickTextEdit::setTextMargin(qreal margin)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit13setTextMarginEd(
    QQuickTextEdit *self,
    qreal margin) {
  self->setTextMargin(margin);
}

//  Qt::InputMethodHints QQuickTextEdit::inputMethodHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTextEdit16inputMethodHintsEv(
    const QQuickTextEdit *self) {
  return static_cast<int>(self->inputMethodHints().toInt());
}

//  void QQuickTextEdit::setInputMethodHints(Qt::InputMethodHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit19setInputMethodHintsE6QFlagsIN2Qt15InputMethodHintEE(
    QQuickTextEdit *self,
    int hints) {
  self->setInputMethodHints(QFlags<Qt::InputMethodHint>::fromInt(hints));
}

//  bool QQuickTextEdit::selectByKeyboard() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextEdit16selectByKeyboardEv(
    const QQuickTextEdit *self) {
  return self->selectByKeyboard();
}

//  void QQuickTextEdit::setSelectByKeyboard(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit19setSelectByKeyboardEb(
    QQuickTextEdit *self,
    bool a0) {
  self->setSelectByKeyboard(a0);
}

//  bool QQuickTextEdit::selectByMouse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextEdit13selectByMouseEv(
    const QQuickTextEdit *self) {
  return self->selectByMouse();
}

//  void QQuickTextEdit::setSelectByMouse(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit16setSelectByMouseEb(
    QQuickTextEdit *self,
    bool a0) {
  self->setSelectByMouse(a0);
}

//  SelectionMode QQuickTextEdit::mouseSelectionMode() const
extern "C" Q_DECL_EXPORT
QQuickTextEdit::SelectionMode ritual_ZNK14QQuickTextEdit18mouseSelectionModeEv(
    const QQuickTextEdit *self) {
  return self->mouseSelectionMode();
}

//  void QQuickTextEdit::setMouseSelectionMode(SelectionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit21setMouseSelectionModeENS_13SelectionModeE(
    QQuickTextEdit *self,
    QQuickTextEdit::SelectionMode mode) {
  self->setMouseSelectionMode(mode);
}

//  bool QQuickTextEdit::canPaste() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextEdit8canPasteEv(const QQuickTextEdit *self) {
  return self->canPaste();
}

//  bool QQuickTextEdit::canUndo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextEdit7canUndoEv(const QQuickTextEdit *self) {
  return self->canUndo();
}

//  bool QQuickTextEdit::canRedo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextEdit7canRedoEv(const QQuickTextEdit *self) {
  return self->canRedo();
}

//  void QQuickTextEdit::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17componentCompleteEv(QQuickTextEdit *self) {
  self->componentComplete();
}

//  int QQuickTextEdit::resourcesLoading() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTextEdit16resourcesLoadingEv(
    const QQuickTextEdit *self) {
  return self->resourcesLoading();
}

//  void QQuickTextEdit::setReadOnly(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit11setReadOnlyEb(
    QQuickTextEdit *self,
    bool a0) {
  self->setReadOnly(a0);
}

//  bool QQuickTextEdit::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextEdit10isReadOnlyEv(const QQuickTextEdit *self) {
  return self->isReadOnly();
}

//  QRectF QQuickTextEdit::cursorRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QQuickTextEdit15cursorRectangleEv(
    const QQuickTextEdit *self) {
  return new QRectF(self->cursorRectangle());
}

#if QT_CONFIG(im)
//  QVariant QQuickTextEdit::inputMethodQuery(Qt::InputMethodQuery property)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQuickTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QQuickTextEdit *self,
    Qt::InputMethodQuery property) {
  return new QVariant(self->inputMethodQuery(property));
}
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
//  QVariant QQuickTextEdit::inputMethodQuery(Qt::InputMethodQuery query,
//      QVariant argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QQuickTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE8QVariant(
    const QQuickTextEdit *self,
    Qt::InputMethodQuery query,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(query, *argument));
}
#endif  // QT_CONFIG(im)

//  qreal QQuickTextEdit::contentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextEdit12contentWidthEv(
    const QQuickTextEdit *self) {
  return self->contentWidth();
}

//  qreal QQuickTextEdit::contentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextEdit13contentHeightEv(
    const QQuickTextEdit *self) {
  return self->contentHeight();
}

//  QUrl QQuickTextEdit::baseUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK14QQuickTextEdit7baseUrlEv(const QQuickTextEdit *self) {
  return new QUrl(self->baseUrl());
}

//  void QQuickTextEdit::setBaseUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit10setBaseUrlERK4QUrl(
    QQuickTextEdit *self,
    const QUrl *url) {
  self->setBaseUrl(*url);
}

//  void QQuickTextEdit::resetBaseUrl()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit12resetBaseUrlEv(QQuickTextEdit *self) {
  self->resetBaseUrl();
}

//  QRectF QQuickTextEdit::positionToRectangle(int a0) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QQuickTextEdit19positionToRectangleEi(
    const QQuickTextEdit *self,
    int a0) {
  return new QRectF(self->positionToRectangle(a0));
}

//  int QQuickTextEdit::positionAt(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTextEdit10positionAtEdd(
    const QQuickTextEdit *self,
    qreal x,
    qreal y) {
  return self->positionAt(x, y);
}

//  void QQuickTextEdit::moveCursorSelection(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit19moveCursorSelectionEi(
    QQuickTextEdit *self,
    int pos) {
  self->moveCursorSelection(pos);
}

//  void QQuickTextEdit::moveCursorSelection(int pos,
//      QQuickTextEdit::SelectionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit19moveCursorSelectionEiNS_13SelectionModeE(
    QQuickTextEdit *self,
    int pos,
    QQuickTextEdit::SelectionMode mode) {
  self->moveCursorSelection(pos, mode);
}

//  QQuickTextSelection *QQuickTextEdit::cursorSelection() const
extern "C" Q_DECL_EXPORT
QQuickTextSelection *ritual_ZNK14QQuickTextEdit15cursorSelectionEv(
    const QQuickTextEdit *self) {
  return self->cursorSelection();
}

//  QRectF QQuickTextEdit::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QQuickTextEdit12boundingRectEv(
    const QQuickTextEdit *self) {
  return new QRectF(self->boundingRect());
}

//  QRectF QQuickTextEdit::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QQuickTextEdit8clipRectEv(const QQuickTextEdit *self) {
  return new QRectF(self->clipRect());
}

//  bool QQuickTextEdit::isInputMethodComposing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QQuickTextEdit22isInputMethodComposingEv(
    const QQuickTextEdit *self) {
  return self->isInputMethodComposing();
}

//  RenderType QQuickTextEdit::renderType() const
extern "C" Q_DECL_EXPORT
QQuickTextEdit::RenderType ritual_ZNK14QQuickTextEdit10renderTypeEv(
    const QQuickTextEdit *self) {
  return self->renderType();
}

//  void QQuickTextEdit::setRenderType(RenderType renderType)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit13setRenderTypeENS_10RenderTypeE(
    QQuickTextEdit *self,
    QQuickTextEdit::RenderType renderType) {
  self->setRenderType(renderType);
}

//  QString QQuickTextEdit::getText(int start, int end) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickTextEdit7getTextEii(
    const QQuickTextEdit *self,
    int start,
    int end) {
  return new QString(self->getText(start, end));
}

//  QString QQuickTextEdit::getFormattedText(int start, int end) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickTextEdit16getFormattedTextEii(
    const QQuickTextEdit *self,
    int start,
    int end) {
  return new QString(self->getFormattedText(start, end));
}

//  QQuickTextDocument *QQuickTextEdit::textDocument()
extern "C" Q_DECL_EXPORT
QQuickTextDocument *ritual_ZN14QQuickTextEdit12textDocumentEv(
    QQuickTextEdit *self) {
  return self->textDocument();
}

//  QString QQuickTextEdit::hoveredLink() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickTextEdit11hoveredLinkEv(
    const QQuickTextEdit *self) {
  return new QString(self->hoveredLink());
}

//  QString QQuickTextEdit::linkAt(qreal x, qreal y) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QQuickTextEdit6linkAtEdd(
    const QQuickTextEdit *self,
    qreal x,
    qreal y) {
  return new QString(self->linkAt(x, y));
}

//  qreal QQuickTextEdit::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextEdit7paddingEv(const QQuickTextEdit *self) {
  return self->padding();
}

//  void QQuickTextEdit::setPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit10setPaddingEd(
    QQuickTextEdit *self,
    qreal padding) {
  self->setPadding(padding);
}

//  void QQuickTextEdit::resetPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit12resetPaddingEv(QQuickTextEdit *self) {
  self->resetPadding();
}

//  qreal QQuickTextEdit::topPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextEdit10topPaddingEv(const QQuickTextEdit *self) {
  return self->topPadding();
}

//  void QQuickTextEdit::setTopPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit13setTopPaddingEd(
    QQuickTextEdit *self,
    qreal padding) {
  self->setTopPadding(padding);
}

//  void QQuickTextEdit::resetTopPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15resetTopPaddingEv(QQuickTextEdit *self) {
  self->resetTopPadding();
}

//  qreal QQuickTextEdit::leftPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextEdit11leftPaddingEv(const QQuickTextEdit *self) {
  return self->leftPadding();
}

//  void QQuickTextEdit::setLeftPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit14setLeftPaddingEd(
    QQuickTextEdit *self,
    qreal padding) {
  self->setLeftPadding(padding);
}

//  void QQuickTextEdit::resetLeftPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit16resetLeftPaddingEv(QQuickTextEdit *self) {
  self->resetLeftPadding();
}

//  qreal QQuickTextEdit::rightPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextEdit12rightPaddingEv(
    const QQuickTextEdit *self) {
  return self->rightPadding();
}

//  void QQuickTextEdit::setRightPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15setRightPaddingEd(
    QQuickTextEdit *self,
    qreal padding) {
  self->setRightPadding(padding);
}

//  void QQuickTextEdit::resetRightPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17resetRightPaddingEv(QQuickTextEdit *self) {
  self->resetRightPadding();
}

//  qreal QQuickTextEdit::bottomPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickTextEdit13bottomPaddingEv(
    const QQuickTextEdit *self) {
  return self->bottomPadding();
}

//  void QQuickTextEdit::setBottomPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit16setBottomPaddingEd(
    QQuickTextEdit *self,
    qreal padding) {
  self->setBottomPadding(padding);
}

//  void QQuickTextEdit::resetBottomPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit18resetBottomPaddingEv(QQuickTextEdit *self) {
  self->resetBottomPadding();
}

//  int QQuickTextEdit::tabStopDistance() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QQuickTextEdit15tabStopDistanceEv(
    const QQuickTextEdit *self) {
  return self->tabStopDistance();
}

//  void QQuickTextEdit::setTabStopDistance(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit18setTabStopDistanceEd(
    QQuickTextEdit *self,
    qreal distance) {
  self->setTabStopDistance(distance);
}

//  void QQuickTextEdit::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit10invalidateEv(QQuickTextEdit *self) {
  self->invalidate();
}

//  void QQuickTextEdit::textChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit11textChangedEv(QQuickTextEdit *self) {
  self->textChanged();
}

//  void QQuickTextEdit::preeditTextChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit18preeditTextChangedEv(QQuickTextEdit *self) {
  self->preeditTextChanged();
}

//  void QQuickTextEdit::contentSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit18contentSizeChangedEv(QQuickTextEdit *self) {
  self->contentSizeChanged();
}

//  void QQuickTextEdit::cursorPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit21cursorPositionChangedEv(
    QQuickTextEdit *self) {
  self->cursorPositionChanged();
}

//  void QQuickTextEdit::cursorRectangleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit22cursorRectangleChangedEv(
    QQuickTextEdit *self) {
  self->cursorRectangleChanged();
}

//  void QQuickTextEdit::selectionStartChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit21selectionStartChangedEv(
    QQuickTextEdit *self) {
  self->selectionStartChanged();
}

//  void QQuickTextEdit::selectionEndChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit19selectionEndChangedEv(QQuickTextEdit *self) {
  self->selectionEndChanged();
}

//  void QQuickTextEdit::selectedTextChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit19selectedTextChangedEv(QQuickTextEdit *self) {
  self->selectedTextChanged();
}

//  void QQuickTextEdit::colorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit12colorChangedERK6QColor(
    QQuickTextEdit *self,
    const QColor *color) {
  self->colorChanged(*color);
}

//  void QQuickTextEdit::selectionColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit21selectionColorChangedERK6QColor(
    QQuickTextEdit *self,
    const QColor *color) {
  self->selectionColorChanged(*color);
}

//  void QQuickTextEdit::selectedTextColorChanged(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit24selectedTextColorChangedERK6QColor(
    QQuickTextEdit *self,
    const QColor *color) {
  self->selectedTextColorChanged(*color);
}

//  void QQuickTextEdit::fontChanged(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit11fontChangedERK5QFont(
    QQuickTextEdit *self,
    const QFont *font) {
  self->fontChanged(*font);
}

//  void
//      QQuickTextEdit::horizontalAlignmentChanged(QQuickTextEdit::HAlignment
//      alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit26horizontalAlignmentChangedENS_10HAlignmentE(
    QQuickTextEdit *self,
    QQuickTextEdit::HAlignment alignment) {
  self->horizontalAlignmentChanged(alignment);
}

//  void QQuickTextEdit::verticalAlignmentChanged(QQuickTextEdit::VAlignment
//      alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit24verticalAlignmentChangedENS_10VAlignmentE(
    QQuickTextEdit *self,
    QQuickTextEdit::VAlignment alignment) {
  self->verticalAlignmentChanged(alignment);
}

//  void QQuickTextEdit::wrapModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15wrapModeChangedEv(QQuickTextEdit *self) {
  self->wrapModeChanged();
}

//  void QQuickTextEdit::lineCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit16lineCountChangedEv(QQuickTextEdit *self) {
  self->lineCountChanged();
}

//  void QQuickTextEdit::textFormatChanged(QQuickTextEdit::TextFormat
//      textFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17textFormatChangedENS_10TextFormatE(
    QQuickTextEdit *self,
    QQuickTextEdit::TextFormat textFormat) {
  self->textFormatChanged(textFormat);
}

//  void QQuickTextEdit::readOnlyChanged(bool isReadOnly)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15readOnlyChangedEb(
    QQuickTextEdit *self,
    bool isReadOnly) {
  self->readOnlyChanged(isReadOnly);
}

//  void QQuickTextEdit::cursorVisibleChanged(bool isCursorVisible)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit20cursorVisibleChangedEb(
    QQuickTextEdit *self,
    bool isCursorVisible) {
  self->cursorVisibleChanged(isCursorVisible);
}

//  void QQuickTextEdit::cursorDelegateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit21cursorDelegateChangedEv(
    QQuickTextEdit *self) {
  self->cursorDelegateChanged();
}

//  void QQuickTextEdit::overwriteModeChanged(bool overwriteMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit20overwriteModeChangedEb(
    QQuickTextEdit *self,
    bool overwriteMode) {
  self->overwriteModeChanged(overwriteMode);
}

//  void QQuickTextEdit::activeFocusOnPressChanged(bool activeFocusOnPressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit25activeFocusOnPressChangedEb(
    QQuickTextEdit *self,
    bool activeFocusOnPressed) {
  self->activeFocusOnPressChanged(activeFocusOnPressed);
}

//  void QQuickTextEdit::persistentSelectionChanged(bool
//      isPersistentSelection)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit26persistentSelectionChangedEb(
    QQuickTextEdit *self,
    bool isPersistentSelection) {
  self->persistentSelectionChanged(isPersistentSelection);
}

//  void QQuickTextEdit::textMarginChanged(qreal textMargin)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17textMarginChangedEd(
    QQuickTextEdit *self,
    qreal textMargin) {
  self->textMarginChanged(textMargin);
}

//  void QQuickTextEdit::selectByKeyboardChanged(bool selectByKeyboard)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit23selectByKeyboardChangedEb(
    QQuickTextEdit *self,
    bool selectByKeyboard) {
  self->selectByKeyboardChanged(selectByKeyboard);
}

//  void QQuickTextEdit::selectByMouseChanged(bool selectByMouse)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit20selectByMouseChangedEb(
    QQuickTextEdit *self,
    bool selectByMouse) {
  self->selectByMouseChanged(selectByMouse);
}

//  void
//      QQuickTextEdit::mouseSelectionModeChanged(QQuickTextEdit::SelectionMo
//      de mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit25mouseSelectionModeChangedENS_13SelectionModeE(
    QQuickTextEdit *self,
    QQuickTextEdit::SelectionMode mode) {
  self->mouseSelectionModeChanged(mode);
}

//  void QQuickTextEdit::linkActivated(const QString &link)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit13linkActivatedERK7QString(
    QQuickTextEdit *self,
    const QString *link) {
  self->linkActivated(*link);
}

//  void QQuickTextEdit::linkHovered(const QString &link)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit11linkHoveredERK7QString(
    QQuickTextEdit *self,
    const QString *link) {
  self->linkHovered(*link);
}

//  void QQuickTextEdit::canPasteChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15canPasteChangedEv(QQuickTextEdit *self) {
  self->canPasteChanged();
}

//  void QQuickTextEdit::canUndoChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit14canUndoChangedEv(QQuickTextEdit *self) {
  self->canUndoChanged();
}

//  void QQuickTextEdit::canRedoChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit14canRedoChangedEv(QQuickTextEdit *self) {
  self->canRedoChanged();
}

//  void QQuickTextEdit::inputMethodComposingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit27inputMethodComposingChangedEv(
    QQuickTextEdit *self) {
  self->inputMethodComposingChanged();
}

//  void QQuickTextEdit::effectiveHorizontalAlignmentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit35effectiveHorizontalAlignmentChangedEv(
    QQuickTextEdit *self) {
  self->effectiveHorizontalAlignmentChanged();
}

//  void QQuickTextEdit::baseUrlChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit14baseUrlChangedEv(QQuickTextEdit *self) {
  self->baseUrlChanged();
}

//  void QQuickTextEdit::inputMethodHintsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit23inputMethodHintsChangedEv(
    QQuickTextEdit *self) {
  self->inputMethodHintsChanged();
}

//  void QQuickTextEdit::renderTypeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17renderTypeChangedEv(QQuickTextEdit *self) {
  self->renderTypeChanged();
}

//  void QQuickTextEdit::editingFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15editingFinishedEv(QQuickTextEdit *self) {
  self->editingFinished();
}

//  void QQuickTextEdit::paddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit14paddingChangedEv(QQuickTextEdit *self) {
  self->paddingChanged();
}

//  void QQuickTextEdit::topPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17topPaddingChangedEv(QQuickTextEdit *self) {
  self->topPaddingChanged();
}

//  void QQuickTextEdit::leftPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit18leftPaddingChangedEv(QQuickTextEdit *self) {
  self->leftPaddingChanged();
}

//  void QQuickTextEdit::rightPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit19rightPaddingChangedEv(QQuickTextEdit *self) {
  self->rightPaddingChanged();
}

//  void QQuickTextEdit::bottomPaddingChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit20bottomPaddingChangedEv(
    QQuickTextEdit *self) {
  self->bottomPaddingChanged();
}

//  void QQuickTextEdit::tabStopDistanceChanged(qreal distance)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit22tabStopDistanceChangedEd(
    QQuickTextEdit *self,
    qreal distance) {
  self->tabStopDistanceChanged(distance);
}

//  void QQuickTextEdit::textEdited()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit10textEditedEv(QQuickTextEdit *self) {
  self->textEdited();
}

//  void QQuickTextEdit::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit9selectAllEv(QQuickTextEdit *self) {
  self->selectAll();
}

//  void QQuickTextEdit::selectWord()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit10selectWordEv(QQuickTextEdit *self) {
  self->selectWord();
}

//  void QQuickTextEdit::select(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit6selectEii(
    QQuickTextEdit *self,
    int start,
    int end) {
  self->select(start, end);
}

//  void QQuickTextEdit::deselect()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit8deselectEv(QQuickTextEdit *self) {
  self->deselect();
}

//  bool QQuickTextEdit::isRightToLeft(int start, int end)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickTextEdit13isRightToLeftEii(
    QQuickTextEdit *self,
    int start,
    int end) {
  return self->isRightToLeft(start, end);
}

#if QT_CONFIG(clipboard)
//  void QQuickTextEdit::cut()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit3cutEv(QQuickTextEdit *self) {
  self->cut();
}
#endif  // QT_CONFIG(clipboard)

#if QT_CONFIG(clipboard)
//  void QQuickTextEdit::copy()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit4copyEv(QQuickTextEdit *self) {
  self->copy();
}
#endif  // QT_CONFIG(clipboard)

#if QT_CONFIG(clipboard)
//  void QQuickTextEdit::paste()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit5pasteEv(QQuickTextEdit *self) {
  self->paste();
}
#endif  // QT_CONFIG(clipboard)

//  void QQuickTextEdit::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit4undoEv(QQuickTextEdit *self) {
  self->undo();
}

//  void QQuickTextEdit::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit4redoEv(QQuickTextEdit *self) {
  self->redo();
}

//  void QQuickTextEdit::insert(int position, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit6insertEiRK7QString(
    QQuickTextEdit *self,
    int position,
    const QString *text) {
  self->insert(position, *text);
}

//  void QQuickTextEdit::remove(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit6removeEii(
    QQuickTextEdit *self,
    int start,
    int end) {
  self->remove(start, end);
}

//  void QQuickTextEdit::append(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit6appendERK7QString(
    QQuickTextEdit *self,
    const QString *text) {
  self->append(*text);
}

//  void QQuickTextEdit::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit5clearEv(QQuickTextEdit *self) {
  self->clear();
}

//  void QQuickTextEdit::q_invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit12q_invalidateEv(QQuickTextEdit *self) {
  self->q_invalidate();
}

//  void QQuickTextEdit::q_textChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit13q_textChangedEv(QQuickTextEdit *self) {
  self->q_textChanged();
}

//  void QQuickTextEdit::q_contentsChange(int a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit16q_contentsChangeEiii(
    QQuickTextEdit *self,
    int a0,
    int a1,
    int a2) {
  self->q_contentsChange(a0, a1, a2);
}

//  void QQuickTextEdit::updateSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15updateSelectionEv(QQuickTextEdit *self) {
  self->updateSelection();
}

//  void QQuickTextEdit::moveCursorDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit18moveCursorDelegateEv(QQuickTextEdit *self) {
  self->moveCursorDelegate();
}

//  void QQuickTextEdit::createCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit12createCursorEv(QQuickTextEdit *self) {
  self->createCursor();
}

//  void QQuickTextEdit::q_canPasteChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17q_canPasteChangedEv(QQuickTextEdit *self) {
  self->q_canPasteChanged();
}

//  void QQuickTextEdit::updateWholeDocument()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit19updateWholeDocumentEv(QQuickTextEdit *self) {
  self->updateWholeDocument();
}

//  void QQuickTextEdit::invalidateBlock(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15invalidateBlockERK10QTextBlock(
    QQuickTextEdit *self,
    const QTextBlock *block) {
  self->invalidateBlock(*block);
}

//  void QQuickTextEdit::updateCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit12updateCursorEv(QQuickTextEdit *self) {
  self->updateCursor();
}

//  void QQuickTextEdit::q_linkHovered(const QString &link)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit13q_linkHoveredERK7QString(
    QQuickTextEdit *self,
    const QString *link) {
  self->q_linkHovered(*link);
}

//  void QQuickTextEdit::q_markerHovered(bool hovered)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15q_markerHoveredEb(
    QQuickTextEdit *self,
    bool hovered) {
  self->q_markerHovered(hovered);
}

//  void QQuickTextEdit::q_updateAlignment()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17q_updateAlignmentEv(QQuickTextEdit *self) {
  self->q_updateAlignment();
}

//  void QQuickTextEdit::updateSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit10updateSizeEv(QQuickTextEdit *self) {
  self->updateSize();
}

//  void QQuickTextEdit::triggerPreprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17triggerPreprocessEv(QQuickTextEdit *self) {
  self->triggerPreprocess();
}

//  QVariant QQuickTextEdit::loadResource(int type, const QUrl &source)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN14QQuickTextEdit12loadResourceEiRK4QUrl(
    QQuickTextEdit *self,
    int type,
    const QUrl *source) {
  return new QVariant(self->loadResource(type, *source));
}

//  void QQuickTextEdit::resourceRequestFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit23resourceRequestFinishedEv(
    QQuickTextEdit *self) {
  self->resourceRequestFinished();
}

//  void QQuickTextEdit::markDirtyNodesForRange(int start, int end, int
//      charDelta)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit22markDirtyNodesForRangeEiii(
    QQuickTextEdit *self,
    int start,
    int end,
    int charDelta) {
  self->markDirtyNodesForRange(start, end, charDelta);
}

//  void QQuickTextEdit::updateTotalLines()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit16updateTotalLinesEv(QQuickTextEdit *self) {
  self->updateTotalLines();
}

//  void QQuickTextEdit::invalidateFontCaches()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit20invalidateFontCachesEv(
    QQuickTextEdit *self) {
  self->invalidateFontCaches();
}

//  QTextDocument *QQuickTextEdit::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK14QQuickTextEdit8documentEv(
    const QQuickTextEdit *self) {
  return self->document();
}

//  void QQuickTextEdit::setDocument(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit11setDocumentEP13QTextDocument(
    QQuickTextEdit *self,
    QTextDocument *doc) {
  self->setDocument(doc);
}

//  QQuickTextEdit::QQuickTextEdit(QQuickTextEditPrivate &dd, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuickTextEdit *ritual_ZN14QQuickTextEditC1ER21QQuickTextEditPrivateP10QQuickItem(
    QQuickTextEditPrivate *dd,
    QQuickItem *parent) {
  return new CuteQQuickTextEdit(*dd, parent);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QQuickTextEdit::setOldSelectionDefault()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit22setOldSelectionDefaultEv(
    QQuickTextEdit *self) {
  self->setOldSelectionDefault();
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QQuickTextEdit::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit14geometryChangeERK6QRectFS2_(
    QQuickTextEdit *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickTextEdit::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickTextEdit *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  bool QQuickTextEdit::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QQuickTextEdit5eventEP6QEvent(
    QQuickTextEdit *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QQuickTextEdit::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit13keyPressEventEP9QKeyEvent(
    QQuickTextEdit *self,
    QKeyEvent *a0) {
  self->keyPressEvent(a0);
}

//  void QQuickTextEdit::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15keyReleaseEventEP9QKeyEvent(
    QQuickTextEdit *self,
    QKeyEvent *a0) {
  self->keyReleaseEvent(a0);
}

//  void QQuickTextEdit::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit12focusInEventEP11QFocusEvent(
    QQuickTextEdit *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickTextEdit::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit13focusOutEventEP11QFocusEvent(
    QQuickTextEdit *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QQuickTextEdit::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15hoverEnterEventEP11QHoverEvent(
    QQuickTextEdit *self,
    QHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void QQuickTextEdit::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit14hoverMoveEventEP11QHoverEvent(
    QQuickTextEdit *self,
    QHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void QQuickTextEdit::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15hoverLeaveEventEP11QHoverEvent(
    QQuickTextEdit *self,
    QHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void QQuickTextEdit::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit15mousePressEventEP11QMouseEvent(
    QQuickTextEdit *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickTextEdit::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit17mouseReleaseEventEP11QMouseEvent(
    QQuickTextEdit *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickTextEdit::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit21mouseDoubleClickEventEP11QMouseEvent(
    QQuickTextEdit *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QQuickTextEdit::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit14mouseMoveEventEP11QMouseEvent(
    QQuickTextEdit *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

#if QT_CONFIG(im)
//  void QQuickTextEdit::inputMethodEvent(QInputMethodEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit16inputMethodEventEP17QInputMethodEvent(
    QQuickTextEdit *self,
    QInputMethodEvent *e) {
  self->inputMethodEvent(e);
}
#endif  // QT_CONFIG(im)

//  QSGNode *QQuickTextEdit::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *updatePaintNodeData)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN14QQuickTextEdit15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickTextEdit *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *updatePaintNodeData) {
  return self->updatePaintNode(oldNode, updatePaintNodeData);
}

//  void QQuickTextEdit::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickTextEdit12updatePolishEv(QQuickTextEdit *self) {
  self->updatePolish();
}

//  QQuickTextEditPrivate *QQuickTextEdit::d_func()
extern "C" Q_DECL_EXPORT
QQuickTextEditPrivate *ritual_ZN14QQuickTextEdit6d_funcEv(
    QQuickTextEdit *self) {
  return self->d_func();
}

//  const QQuickTextEditPrivate *QQuickTextEdit::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextEditPrivate *ritual_ZNK14QQuickTextEdit6d_funcEv(
    const QQuickTextEdit *self) {
  return self->d_func();
}

//  QQuickTextEdit as the QQuickTextInterface it is built on
extern "C" Q_DECL_EXPORT
QQuickTextInterface *ritual_cast_QQuickTextEdit_QQuickTextInterface(
    QQuickTextEdit *self) {
  return static_cast<QQuickTextInterface *>(self);
}

//  a Python function taken by a CuteQQuickTextEdit, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextEdit(
    QQuickTextEdit *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextEdit *>(self)->take(key, call);
}

//  void QQuickTextEdit::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit17componentCompleteEv(
    QQuickTextEdit *self) {
  self->QQuickTextEdit::componentComplete();
}

#if QT_CONFIG(im)
//  QVariant QQuickTextEdit::inputMethodQuery(Qt::InputMethodQuery property)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK14QQuickTextEdit16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QQuickTextEdit *self,
    Qt::InputMethodQuery property) {
  return new QVariant(self->QQuickTextEdit::inputMethodQuery(property));
}
#endif  // QT_CONFIG(im)

//  QRectF QQuickTextEdit::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK14QQuickTextEdit12boundingRectEv(
    const QQuickTextEdit *self) {
  return new QRectF(self->QQuickTextEdit::boundingRect());
}

//  QRectF QQuickTextEdit::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK14QQuickTextEdit8clipRectEv(
    const QQuickTextEdit *self) {
  return new QRectF(self->QQuickTextEdit::clipRect());
}

//  void QQuickTextEdit::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit10invalidateEv(QQuickTextEdit *self) {
  self->QQuickTextEdit::invalidate();
}

//  void QQuickTextEdit::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit14geometryChangeERK6QRectFS2_(
    QQuickTextEdit *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickTextEdit::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickTextEdit *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::itemChange(
      change,
      *value);
}

//  bool QQuickTextEdit::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QQuickTextEdit5eventEP6QEvent(
    QQuickTextEdit *self,
    QEvent *a0) {
  return static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::event(
      a0);
}

//  void QQuickTextEdit::keyPressEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit13keyPressEventEP9QKeyEvent(
    QQuickTextEdit *self,
    QKeyEvent *a0) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::keyPressEvent(
      a0);
}

//  void QQuickTextEdit::keyReleaseEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit15keyReleaseEventEP9QKeyEvent(
    QQuickTextEdit *self,
    QKeyEvent *a0) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::keyReleaseEvent(
      a0);
}

//  void QQuickTextEdit::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit12focusInEventEP11QFocusEvent(
    QQuickTextEdit *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::focusInEvent(
      event);
}

//  void QQuickTextEdit::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit13focusOutEventEP11QFocusEvent(
    QQuickTextEdit *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::focusOutEvent(
      event);
}

//  void QQuickTextEdit::hoverEnterEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit15hoverEnterEventEP11QHoverEvent(
    QQuickTextEdit *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::hoverEnterEvent(
      event);
}

//  void QQuickTextEdit::hoverMoveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit14hoverMoveEventEP11QHoverEvent(
    QQuickTextEdit *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::hoverMoveEvent(
      event);
}

//  void QQuickTextEdit::hoverLeaveEvent(QHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit15hoverLeaveEventEP11QHoverEvent(
    QQuickTextEdit *self,
    QHoverEvent *event) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::hoverLeaveEvent(
      event);
}

//  void QQuickTextEdit::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit15mousePressEventEP11QMouseEvent(
    QQuickTextEdit *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::mousePressEvent(
      event);
}

//  void QQuickTextEdit::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit17mouseReleaseEventEP11QMouseEvent(
    QQuickTextEdit *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::mouseReleaseEvent(
      event);
}

//  void QQuickTextEdit::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit21mouseDoubleClickEventEP11QMouseEvent(
    QQuickTextEdit *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::mouseDoubleClickEvent(
      event);
}

//  void QQuickTextEdit::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit14mouseMoveEventEP11QMouseEvent(
    QQuickTextEdit *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::mouseMoveEvent(
      event);
}

#if QT_CONFIG(im)
//  void QQuickTextEdit::inputMethodEvent(QInputMethodEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit16inputMethodEventEP17QInputMethodEvent(
    QQuickTextEdit *self,
    QInputMethodEvent *e) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::inputMethodEvent(
      e);
}
#endif  // QT_CONFIG(im)

//  QSGNode *QQuickTextEdit::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *updatePaintNodeData)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN14QQuickTextEdit15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickTextEdit *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *updatePaintNodeData) {
  return static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::updatePaintNode(
      oldNode,
      updatePaintNodeData);
}

//  void QQuickTextEdit::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QQuickTextEdit12updatePolishEv(QQuickTextEdit *self) {
  static_cast<OwnQQuickTextEdit *>(self)->OwnQQuickTextEdit::updatePolish();
}
