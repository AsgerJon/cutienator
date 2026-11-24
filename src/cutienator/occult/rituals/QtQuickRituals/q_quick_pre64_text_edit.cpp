//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextedit_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickPre64TextEdit that Python can take functions over in. Every QQuickPre64TextEdit
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPre64TextEditCall0)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickPre64TextEditCall1)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef const QRectF * (*CuteQQuickPre64TextEditCall2)(const void *, int *);
typedef const QRectF * (*CuteQQuickPre64TextEditCall3)(const void *, int *);
typedef void (*CuteQQuickPre64TextEditCall4)(const void *, int *);
typedef void (*CuteQQuickPre64TextEditCall5)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickPre64TextEditCall6)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPre64TextEditCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPre64TextEditCall8)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickPre64TextEditCall9)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickPre64TextEditCall10)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPre64TextEditCall11)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPre64TextEditCall12)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickPre64TextEditCall13)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickPre64TextEditCall14)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickPre64TextEditCall15)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPre64TextEditCall16)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPre64TextEditCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPre64TextEditCall18)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickPre64TextEditCall19)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void * (*CuteQQuickPre64TextEditCall20)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickPre64TextEditCall21)(const void *, int *);
typedef bool (*CuteQQuickPre64TextEditCall22)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickPre64TextEditCall23)(const void *, int *);
typedef void * (*CuteQQuickPre64TextEditCall24)(const void *, int *);
typedef void (*CuteQQuickPre64TextEditCall25)(const void *, int *);
typedef void (*CuteQQuickPre64TextEditCall26)(const void *, int *);
typedef void (*CuteQQuickPre64TextEditCall27)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPre64TextEditCall28)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPre64TextEditCall29)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPre64TextEditCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPre64TextEditCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPre64TextEditCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPre64TextEditCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickPre64TextEditCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickPre64TextEditCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPre64TextEditCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPre64TextEditCall37)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPre64TextEditCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPre64TextEditCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPre64TextEditCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPre64TextEditCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPre64TextEdit : public QQuickPre64TextEdit {
public:
  using QQuickPre64TextEdit::QQuickPre64TextEdit;
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
      CuteQQuickPre64TextEditCall0 call = reinterpret_cast<CuteQQuickPre64TextEditCall0>(taken[0]);
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
      CuteQQuickPre64TextEditCall1 call = reinterpret_cast<CuteQQuickPre64TextEditCall1>(taken[1]);
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
      CuteQQuickPre64TextEditCall2 call = reinterpret_cast<CuteQQuickPre64TextEditCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextEdit::boundingRect();
  }

  //  QRectF QQuickTextEdit::clipRect() const
  QRectF clipRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall3 call = reinterpret_cast<CuteQQuickPre64TextEditCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextEdit::clipRect();
  }

  //  void QQuickTextEdit::invalidate()
  void invalidate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall4 call = reinterpret_cast<CuteQQuickPre64TextEditCall4>(taken[4]);
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
      CuteQQuickPre64TextEditCall5 call = reinterpret_cast<CuteQQuickPre64TextEditCall5>(taken[5]);
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
      CuteQQuickPre64TextEditCall6 call = reinterpret_cast<CuteQQuickPre64TextEditCall6>(taken[6]);
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
      CuteQQuickPre64TextEditCall7 call = reinterpret_cast<CuteQQuickPre64TextEditCall7>(taken[7]);
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
      CuteQQuickPre64TextEditCall8 call = reinterpret_cast<CuteQQuickPre64TextEditCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickTextEdit::keyPressEvent(a0);
  }

  //  void QQuickTextEdit::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall9 call = reinterpret_cast<CuteQQuickPre64TextEditCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickTextEdit::keyReleaseEvent(a0);
  }

  //  void QQuickTextEdit::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall10 call = reinterpret_cast<CuteQQuickPre64TextEditCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::focusInEvent(event);
  }

  //  void QQuickTextEdit::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall11 call = reinterpret_cast<CuteQQuickPre64TextEditCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::focusOutEvent(event);
  }

  //  void QQuickTextEdit::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall12 call = reinterpret_cast<CuteQQuickPre64TextEditCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::hoverEnterEvent(event);
  }

  //  void QQuickTextEdit::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall13 call = reinterpret_cast<CuteQQuickPre64TextEditCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::hoverMoveEvent(event);
  }

  //  void QQuickTextEdit::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall14 call = reinterpret_cast<CuteQQuickPre64TextEditCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::hoverLeaveEvent(event);
  }

  //  void QQuickTextEdit::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall15 call = reinterpret_cast<CuteQQuickPre64TextEditCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::mousePressEvent(event);
  }

  //  void QQuickTextEdit::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall16 call = reinterpret_cast<CuteQQuickPre64TextEditCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::mouseReleaseEvent(event);
  }

  //  void QQuickTextEdit::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall17 call = reinterpret_cast<CuteQQuickPre64TextEditCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextEdit::mouseDoubleClickEvent(event);
  }

  //  void QQuickTextEdit::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall18 call = reinterpret_cast<CuteQQuickPre64TextEditCall18>(taken[18]);
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
      CuteQQuickPre64TextEditCall19 call = reinterpret_cast<CuteQQuickPre64TextEditCall19>(taken[19]);
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
      CuteQQuickPre64TextEditCall20 call = reinterpret_cast<CuteQQuickPre64TextEditCall20>(taken[20]);
      void * given = call(this, oldNode, updatePaintNodeData, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickTextEdit::updatePaintNode(oldNode, updatePaintNodeData);
  }

  //  void QQuickTextEdit::updatePolish()
  void updatePolish() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall21 call = reinterpret_cast<CuteQQuickPre64TextEditCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextEdit::updatePolish();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall22 call = reinterpret_cast<CuteQQuickPre64TextEditCall22>(taken[22]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall23 call = reinterpret_cast<CuteQQuickPre64TextEditCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall24 call = reinterpret_cast<CuteQQuickPre64TextEditCall24>(taken[24]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall25 call = reinterpret_cast<CuteQQuickPre64TextEditCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall26 call = reinterpret_cast<CuteQQuickPre64TextEditCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall27 call = reinterpret_cast<CuteQQuickPre64TextEditCall27>(taken[27]);
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
      CuteQQuickPre64TextEditCall28 call = reinterpret_cast<CuteQQuickPre64TextEditCall28>(taken[28]);
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
      CuteQQuickPre64TextEditCall29 call = reinterpret_cast<CuteQQuickPre64TextEditCall29>(taken[29]);
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
      CuteQQuickPre64TextEditCall30 call = reinterpret_cast<CuteQQuickPre64TextEditCall30>(taken[30]);
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
      CuteQQuickPre64TextEditCall31 call = reinterpret_cast<CuteQQuickPre64TextEditCall31>(taken[31]);
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
      CuteQQuickPre64TextEditCall32 call = reinterpret_cast<CuteQQuickPre64TextEditCall32>(taken[32]);
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
      CuteQQuickPre64TextEditCall33 call = reinterpret_cast<CuteQQuickPre64TextEditCall33>(taken[33]);
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
      CuteQQuickPre64TextEditCall34 call = reinterpret_cast<CuteQQuickPre64TextEditCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickPre64TextEditCall35 call = reinterpret_cast<CuteQQuickPre64TextEditCall35>(taken[35]);
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
      CuteQQuickPre64TextEditCall36 call = reinterpret_cast<CuteQQuickPre64TextEditCall36>(taken[36]);
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
      CuteQQuickPre64TextEditCall37 call = reinterpret_cast<CuteQQuickPre64TextEditCall37>(taken[37]);
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
      CuteQQuickPre64TextEditCall38 call = reinterpret_cast<CuteQQuickPre64TextEditCall38>(taken[38]);
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
      CuteQQuickPre64TextEditCall39 call = reinterpret_cast<CuteQQuickPre64TextEditCall39>(taken[39]);
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
      CuteQQuickPre64TextEditCall40 call = reinterpret_cast<CuteQQuickPre64TextEditCall40>(taken[40]);
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
      CuteQQuickPre64TextEditCall41 call = reinterpret_cast<CuteQQuickPre64TextEditCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPre64TextEdit::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QQuickPre64TextEdit10metaObjectEv(
    const QQuickPre64TextEdit *self) {
  return self->metaObject();
}

//  a Python function taken by a CuteQQuickPre64TextEdit, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPre64TextEdit(
    QQuickPre64TextEdit *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPre64TextEdit *>(self)->take(key, call);
}

#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
