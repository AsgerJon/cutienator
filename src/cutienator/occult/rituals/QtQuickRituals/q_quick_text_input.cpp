//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextinput_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qfont.h>
#include <QtGui/qcolor.h>
#include <QtCore/qvariant.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QQuickTextInput may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTextInput : QQuickTextInput {
  using QQuickTextInput::geometryChange;
  using QQuickTextInput::itemChange;
  using QQuickTextInput::mousePressEvent;
  using QQuickTextInput::mouseMoveEvent;
  using QQuickTextInput::mouseReleaseEvent;
  using QQuickTextInput::mouseDoubleClickEvent;
  using QQuickTextInput::keyPressEvent;
  using QQuickTextInput::inputMethodEvent;
  using QQuickTextInput::mouseUngrabEvent;
  using QQuickTextInput::event;
  using QQuickTextInput::focusOutEvent;
  using QQuickTextInput::focusInEvent;
  using QQuickTextInput::timerEvent;
  using QQuickTextInput::updatePaintNode;
  using QQuickTextInput::updatePolish;
};

//  A QQuickTextInput that Python can take functions over in. Every QQuickTextInput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickTextInputCall0)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickTextInputCall1)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef const QRectF * (*CuteQQuickTextInputCall2)(const void *, int *);
typedef const QRectF * (*CuteQQuickTextInputCall3)(const void *, int *);
typedef void (*CuteQQuickTextInputCall4)(const void *, int *);
typedef void (*CuteQQuickTextInputCall5)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickTextInputCall6)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickTextInputCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextInputCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextInputCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextInputCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickTextInputCall11)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickTextInputCall12)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickTextInputCall13)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextInputCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextInputCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickTextInputCall16)(const void *, QFocusEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextInputCall17)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuickTextInputCall18)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickTextInputCall19)(const void *, int *);
typedef bool (*CuteQQuickTextInputCall20)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickTextInputCall21)(const void *, int *);
typedef void * (*CuteQQuickTextInputCall22)(const void *, int *);
typedef void (*CuteQQuickTextInputCall23)(const void *, int *);
typedef void (*CuteQQuickTextInputCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickTextInputCall25)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTextInputCall26)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickTextInputCall27)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickTextInputCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTextInputCall29)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickTextInputCall30)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextInputCall31)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextInputCall32)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextInputCall33)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickTextInputCall34)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickTextInputCall35)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickTextInputCall36)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextInputCall37)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextInputCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextInputCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextInputCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextInputCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTextInput : public QQuickTextInput {
public:
  using QQuickTextInput::QQuickTextInput;
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
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[11] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[13] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[25] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[30] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[33] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[34] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[36] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
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

  //  void QQuickTextInput::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextInputCall0 call = reinterpret_cast<CuteQQuickTextInputCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextInput::componentComplete();
  }

#if QT_CONFIG(im)
  //  QVariant QQuickTextInput::inputMethodQuery(Qt::InputMethodQuery
  //      property) const
  QVariant inputMethodQuery(Qt::InputMethodQuery property) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextInputCall1 call = reinterpret_cast<CuteQQuickTextInputCall1>(taken[1]);
      const QVariant * given = call(this, static_cast<int>(property), &handled);
      if (handled && given) return *given;
    }
    return QQuickTextInput::inputMethodQuery(property);
  }
#endif  // QT_CONFIG(im)

  //  QRectF QQuickTextInput::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextInputCall2 call = reinterpret_cast<CuteQQuickTextInputCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextInput::boundingRect();
  }

  //  QRectF QQuickTextInput::clipRect() const
  QRectF clipRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTextInputCall3 call = reinterpret_cast<CuteQQuickTextInputCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextInput::clipRect();
  }

  //  void QQuickTextInput::invalidate()
  void invalidate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTextInputCall4 call = reinterpret_cast<CuteQQuickTextInputCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextInput::invalidate();
  }

  //  void QQuickTextInput::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTextInputCall5 call = reinterpret_cast<CuteQQuickTextInputCall5>(taken[5]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickTextInput::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickTextInput::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTextInputCall6 call = reinterpret_cast<CuteQQuickTextInputCall6>(taken[6]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickTextInput::itemChange(change, value);
  }

  //  void QQuickTextInput::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTextInputCall7 call = reinterpret_cast<CuteQQuickTextInputCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextInput::mousePressEvent(event);
  }

  //  void QQuickTextInput::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTextInputCall8 call = reinterpret_cast<CuteQQuickTextInputCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextInput::mouseMoveEvent(event);
  }

  //  void QQuickTextInput::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTextInputCall9 call = reinterpret_cast<CuteQQuickTextInputCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextInput::mouseReleaseEvent(event);
  }

  //  void QQuickTextInput::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTextInputCall10 call = reinterpret_cast<CuteQQuickTextInputCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextInput::mouseDoubleClickEvent(event);
  }

  //  void QQuickTextInput::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTextInputCall11 call = reinterpret_cast<CuteQQuickTextInputCall11>(taken[11]);
      call(this, ev, &handled);
      if (handled) return;
    }
    QQuickTextInput::keyPressEvent(ev);
  }

#if QT_CONFIG(im)
  //  void QQuickTextInput::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTextInputCall12 call = reinterpret_cast<CuteQQuickTextInputCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickTextInput::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickTextInput::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTextInputCall13 call = reinterpret_cast<CuteQQuickTextInputCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextInput::mouseUngrabEvent();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickTextInput::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickTextInputCall14 call = reinterpret_cast<CuteQQuickTextInputCall14>(taken[14]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuickTextInput::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickTextInput::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickTextInputCall15 call = reinterpret_cast<CuteQQuickTextInputCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextInput::focusOutEvent(event);
  }

  //  void QQuickTextInput::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickTextInputCall16 call = reinterpret_cast<CuteQQuickTextInputCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextInput::focusInEvent(event);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickTextInput::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickTextInputCall17 call = reinterpret_cast<CuteQQuickTextInputCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextInput::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  QSGNode *QQuickTextInput::updatePaintNode(QSGNode *oldNode,
  //      UpdatePaintNodeData *data)
  QSGNode *updatePaintNode(
      QSGNode *oldNode,
      QQuickItem::UpdatePaintNodeData *data) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickTextInputCall18 call = reinterpret_cast<CuteQQuickTextInputCall18>(taken[18]);
      void * given = call(this, oldNode, data, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickTextInput::updatePaintNode(oldNode, data);
  }

  //  void QQuickTextInput::updatePolish()
  void updatePolish() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickTextInputCall19 call = reinterpret_cast<CuteQQuickTextInputCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextInput::updatePolish();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickTextInputCall20 call = reinterpret_cast<CuteQQuickTextInputCall20>(taken[20]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickTextInputCall21 call = reinterpret_cast<CuteQQuickTextInputCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickTextInputCall22 call = reinterpret_cast<CuteQQuickTextInputCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickTextInputCall23 call = reinterpret_cast<CuteQQuickTextInputCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickTextInputCall24 call = reinterpret_cast<CuteQQuickTextInputCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickTextInputCall25 call = reinterpret_cast<CuteQQuickTextInputCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickTextInputCall26 call = reinterpret_cast<CuteQQuickTextInputCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickTextInputCall27 call = reinterpret_cast<CuteQQuickTextInputCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickTextInputCall28 call = reinterpret_cast<CuteQQuickTextInputCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickTextInputCall29 call = reinterpret_cast<CuteQQuickTextInputCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickTextInputCall30 call = reinterpret_cast<CuteQQuickTextInputCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickTextInputCall31 call = reinterpret_cast<CuteQQuickTextInputCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickTextInputCall32 call = reinterpret_cast<CuteQQuickTextInputCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickTextInputCall33 call = reinterpret_cast<CuteQQuickTextInputCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickTextInputCall34 call = reinterpret_cast<CuteQQuickTextInputCall34>(taken[34]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickTextInputCall35 call = reinterpret_cast<CuteQQuickTextInputCall35>(taken[35]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickTextInputCall36 call = reinterpret_cast<CuteQQuickTextInputCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickTextInputCall37 call = reinterpret_cast<CuteQQuickTextInputCall37>(taken[37]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickTextInputCall38 call = reinterpret_cast<CuteQQuickTextInputCall38>(taken[38]);
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
      CuteQQuickTextInputCall39 call = reinterpret_cast<CuteQQuickTextInputCall39>(taken[39]);
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
      CuteQQuickTextInputCall40 call = reinterpret_cast<CuteQQuickTextInputCall40>(taken[40]);
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
      CuteQQuickTextInputCall41 call = reinterpret_cast<CuteQQuickTextInputCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTextInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QQuickTextInput10metaObjectEv(
    const QQuickTextInput *self) {
  return self->metaObject();
}

//  QString QQuickTextInput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQuickTextInput2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickTextInput::tr(s, c, n));
}

//  QQuickTextInput::QQuickTextInput(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickTextInput *ritual_ZN15QQuickTextInputC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickTextInput(parent);
}

//  QQuickTextInput::~QQuickTextInput()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInputD1Ev(QQuickTextInput *self) {
  delete self;
}

//  void QQuickTextInput::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput17componentCompleteEv(QQuickTextInput *self) {
  self->componentComplete();
}

//  int QQuickTextInput::positionAt(qreal x, qreal y,
//      QQuickTextInput::CursorPosition position) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTextInput10positionAtEddNS_14CursorPositionE(
    const QQuickTextInput *self,
    qreal x,
    qreal y,
    QQuickTextInput::CursorPosition position) {
  return self->positionAt(x, y, position);
}

//  QRectF QQuickTextInput::positionToRectangle(int pos) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QQuickTextInput19positionToRectangleEi(
    const QQuickTextInput *self,
    int pos) {
  return new QRectF(self->positionToRectangle(pos));
}

//  void QQuickTextInput::moveCursorSelection(int pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput19moveCursorSelectionEi(
    QQuickTextInput *self,
    int pos) {
  self->moveCursorSelection(pos);
}

//  void QQuickTextInput::moveCursorSelection(int pos,
//      QQuickTextInput::SelectionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput19moveCursorSelectionEiNS_13SelectionModeE(
    QQuickTextInput *self,
    int pos,
    QQuickTextInput::SelectionMode mode) {
  self->moveCursorSelection(pos, mode);
}

//  RenderType QQuickTextInput::renderType() const
extern "C" Q_DECL_EXPORT
QQuickTextInput::RenderType ritual_ZNK15QQuickTextInput10renderTypeEv(
    const QQuickTextInput *self) {
  return self->renderType();
}

//  void QQuickTextInput::setRenderType(RenderType renderType)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput13setRenderTypeENS_10RenderTypeE(
    QQuickTextInput *self,
    QQuickTextInput::RenderType renderType) {
  self->setRenderType(renderType);
}

//  QString QQuickTextInput::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickTextInput4textEv(const QQuickTextInput *self) {
  return new QString(self->text());
}

//  void QQuickTextInput::setText(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput7setTextERK7QString(
    QQuickTextInput *self,
    const QString *a0) {
  self->setText(*a0);
}

//  int QQuickTextInput::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTextInput6lengthEv(const QQuickTextInput *self) {
  return self->length();
}

//  QFont QQuickTextInput::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK15QQuickTextInput4fontEv(const QQuickTextInput *self) {
  return new QFont(self->font());
}

//  void QQuickTextInput::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput7setFontERK5QFont(
    QQuickTextInput *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QColor QQuickTextInput::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickTextInput5colorEv(const QQuickTextInput *self) {
  return new QColor(self->color());
}

//  void QQuickTextInput::setColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput8setColorERK6QColor(
    QQuickTextInput *self,
    const QColor *c) {
  self->setColor(*c);
}

//  QColor QQuickTextInput::selectionColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickTextInput14selectionColorEv(
    const QQuickTextInput *self) {
  return new QColor(self->selectionColor());
}

//  void QQuickTextInput::setSelectionColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput17setSelectionColorERK6QColor(
    QQuickTextInput *self,
    const QColor *c) {
  self->setSelectionColor(*c);
}

//  QColor QQuickTextInput::selectedTextColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK15QQuickTextInput17selectedTextColorEv(
    const QQuickTextInput *self) {
  return new QColor(self->selectedTextColor());
}

//  void QQuickTextInput::setSelectedTextColor(const QColor &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput20setSelectedTextColorERK6QColor(
    QQuickTextInput *self,
    const QColor *c) {
  self->setSelectedTextColor(*c);
}

//  HAlignment QQuickTextInput::hAlign() const
extern "C" Q_DECL_EXPORT
QQuickTextInput::HAlignment ritual_ZNK15QQuickTextInput6hAlignEv(
    const QQuickTextInput *self) {
  return self->hAlign();
}

//  void QQuickTextInput::setHAlign(HAlignment align)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput9setHAlignENS_10HAlignmentE(
    QQuickTextInput *self,
    QQuickTextInput::HAlignment align) {
  self->setHAlign(align);
}

//  void QQuickTextInput::resetHAlign()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput11resetHAlignEv(QQuickTextInput *self) {
  self->resetHAlign();
}

//  HAlignment QQuickTextInput::effectiveHAlign() const
extern "C" Q_DECL_EXPORT
QQuickTextInput::HAlignment ritual_ZNK15QQuickTextInput15effectiveHAlignEv(
    const QQuickTextInput *self) {
  return self->effectiveHAlign();
}

//  VAlignment QQuickTextInput::vAlign() const
extern "C" Q_DECL_EXPORT
QQuickTextInput::VAlignment ritual_ZNK15QQuickTextInput6vAlignEv(
    const QQuickTextInput *self) {
  return self->vAlign();
}

//  void QQuickTextInput::setVAlign(VAlignment align)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput9setVAlignENS_10VAlignmentE(
    QQuickTextInput *self,
    QQuickTextInput::VAlignment align) {
  self->setVAlign(align);
}

//  WrapMode QQuickTextInput::wrapMode() const
extern "C" Q_DECL_EXPORT
QQuickTextInput::WrapMode ritual_ZNK15QQuickTextInput8wrapModeEv(
    const QQuickTextInput *self) {
  return self->wrapMode();
}

//  void QQuickTextInput::setWrapMode(WrapMode w)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput11setWrapModeENS_8WrapModeE(
    QQuickTextInput *self,
    QQuickTextInput::WrapMode w) {
  self->setWrapMode(w);
}

//  bool QQuickTextInput::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextInput10isReadOnlyEv(const QQuickTextInput *self) {
  return self->isReadOnly();
}

//  void QQuickTextInput::setReadOnly(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput11setReadOnlyEb(
    QQuickTextInput *self,
    bool a0) {
  self->setReadOnly(a0);
}

//  bool QQuickTextInput::isCursorVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextInput15isCursorVisibleEv(
    const QQuickTextInput *self) {
  return self->isCursorVisible();
}

//  void QQuickTextInput::setCursorVisible(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput16setCursorVisibleEb(
    QQuickTextInput *self,
    bool on) {
  self->setCursorVisible(on);
}

//  int QQuickTextInput::cursorPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTextInput14cursorPositionEv(
    const QQuickTextInput *self) {
  return self->cursorPosition();
}

//  void QQuickTextInput::setCursorPosition(int cp)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput17setCursorPositionEi(
    QQuickTextInput *self,
    int cp) {
  self->setCursorPosition(cp);
}

//  QRectF QQuickTextInput::cursorRectangle() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QQuickTextInput15cursorRectangleEv(
    const QQuickTextInput *self) {
  return new QRectF(self->cursorRectangle());
}

//  int QQuickTextInput::selectionStart() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTextInput14selectionStartEv(
    const QQuickTextInput *self) {
  return self->selectionStart();
}

//  int QQuickTextInput::selectionEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTextInput12selectionEndEv(
    const QQuickTextInput *self) {
  return self->selectionEnd();
}

//  QString QQuickTextInput::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickTextInput12selectedTextEv(
    const QQuickTextInput *self) {
  return new QString(self->selectedText());
}

//  int QQuickTextInput::maxLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTextInput9maxLengthEv(const QQuickTextInput *self) {
  return self->maxLength();
}

//  void QQuickTextInput::setMaxLength(int ml)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput12setMaxLengthEi(
    QQuickTextInput *self,
    int ml) {
  self->setMaxLength(ml);
}

#if QT_CONFIG(validator)
//  QValidator *QQuickTextInput::validator() const
extern "C" Q_DECL_EXPORT
QValidator *ritual_ZNK15QQuickTextInput9validatorEv(
    const QQuickTextInput *self) {
  return self->validator();
}
#endif  // QT_CONFIG(validator)

#if QT_CONFIG(validator)
//  void QQuickTextInput::setValidator(QValidator *v)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput12setValidatorEP10QValidator(
    QQuickTextInput *self,
    QValidator *v) {
  self->setValidator(v);
}
#endif  // QT_CONFIG(validator)

//  QString QQuickTextInput::inputMask() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickTextInput9inputMaskEv(
    const QQuickTextInput *self) {
  return new QString(self->inputMask());
}

//  void QQuickTextInput::setInputMask(const QString &im)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput12setInputMaskERK7QString(
    QQuickTextInput *self,
    const QString *im) {
  self->setInputMask(*im);
}

//  EchoMode QQuickTextInput::echoMode() const
extern "C" Q_DECL_EXPORT
QQuickTextInput::EchoMode ritual_ZNK15QQuickTextInput8echoModeEv(
    const QQuickTextInput *self) {
  return self->echoMode();
}

//  void QQuickTextInput::setEchoMode(EchoMode echo)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput11setEchoModeENS_8EchoModeE(
    QQuickTextInput *self,
    QQuickTextInput::EchoMode echo) {
  self->setEchoMode(echo);
}

//  QString QQuickTextInput::passwordCharacter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickTextInput17passwordCharacterEv(
    const QQuickTextInput *self) {
  return new QString(self->passwordCharacter());
}

//  void QQuickTextInput::setPasswordCharacter(const QString &str)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput20setPasswordCharacterERK7QString(
    QQuickTextInput *self,
    const QString *str) {
  self->setPasswordCharacter(*str);
}

//  int QQuickTextInput::passwordMaskDelay() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTextInput17passwordMaskDelayEv(
    const QQuickTextInput *self) {
  return self->passwordMaskDelay();
}

//  void QQuickTextInput::setPasswordMaskDelay(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput20setPasswordMaskDelayEi(
    QQuickTextInput *self,
    int delay) {
  self->setPasswordMaskDelay(delay);
}

//  void QQuickTextInput::resetPasswordMaskDelay()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput22resetPasswordMaskDelayEv(
    QQuickTextInput *self) {
  self->resetPasswordMaskDelay();
}

//  QString QQuickTextInput::displayText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickTextInput11displayTextEv(
    const QQuickTextInput *self) {
  return new QString(self->displayText());
}

//  QString QQuickTextInput::preeditText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickTextInput11preeditTextEv(
    const QQuickTextInput *self) {
  return new QString(self->preeditText());
}

//  QQmlComponent *QQuickTextInput::cursorDelegate() const
extern "C" Q_DECL_EXPORT
QQmlComponent *ritual_ZNK15QQuickTextInput14cursorDelegateEv(
    const QQuickTextInput *self) {
  return self->cursorDelegate();
}

//  void QQuickTextInput::setCursorDelegate(QQmlComponent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput17setCursorDelegateEP13QQmlComponent(
    QQuickTextInput *self,
    QQmlComponent *a0) {
  self->setCursorDelegate(a0);
}

//  bool QQuickTextInput::overwriteMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextInput13overwriteModeEv(
    const QQuickTextInput *self) {
  return self->overwriteMode();
}

//  void QQuickTextInput::setOverwriteMode(bool overwrite)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput16setOverwriteModeEb(
    QQuickTextInput *self,
    bool overwrite) {
  self->setOverwriteMode(overwrite);
}

//  bool QQuickTextInput::focusOnPress() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextInput12focusOnPressEv(
    const QQuickTextInput *self) {
  return self->focusOnPress();
}

//  void QQuickTextInput::setFocusOnPress(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput15setFocusOnPressEb(
    QQuickTextInput *self,
    bool a0) {
  self->setFocusOnPress(a0);
}

//  bool QQuickTextInput::autoScroll() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextInput10autoScrollEv(const QQuickTextInput *self) {
  return self->autoScroll();
}

//  void QQuickTextInput::setAutoScroll(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput13setAutoScrollEb(
    QQuickTextInput *self,
    bool a0) {
  self->setAutoScroll(a0);
}

//  bool QQuickTextInput::selectByMouse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextInput13selectByMouseEv(
    const QQuickTextInput *self) {
  return self->selectByMouse();
}

//  void QQuickTextInput::setSelectByMouse(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput16setSelectByMouseEb(
    QQuickTextInput *self,
    bool a0) {
  self->setSelectByMouse(a0);
}

//  SelectionMode QQuickTextInput::mouseSelectionMode() const
extern "C" Q_DECL_EXPORT
QQuickTextInput::SelectionMode ritual_ZNK15QQuickTextInput18mouseSelectionModeEv(
    const QQuickTextInput *self) {
  return self->mouseSelectionMode();
}

//  void QQuickTextInput::setMouseSelectionMode(SelectionMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput21setMouseSelectionModeENS_13SelectionModeE(
    QQuickTextInput *self,
    QQuickTextInput::SelectionMode mode) {
  self->setMouseSelectionMode(mode);
}

//  bool QQuickTextInput::persistentSelection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextInput19persistentSelectionEv(
    const QQuickTextInput *self) {
  return self->persistentSelection();
}

//  void QQuickTextInput::setPersistentSelection(bool persist)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput22setPersistentSelectionEb(
    QQuickTextInput *self,
    bool persist) {
  self->setPersistentSelection(persist);
}

//  bool QQuickTextInput::hasAcceptableInput() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextInput18hasAcceptableInputEv(
    const QQuickTextInput *self) {
  return self->hasAcceptableInput();
}

#if QT_CONFIG(im)
//  QVariant QQuickTextInput::inputMethodQuery(Qt::InputMethodQuery property)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QQuickTextInput16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QQuickTextInput *self,
    Qt::InputMethodQuery property) {
  return new QVariant(self->inputMethodQuery(property));
}
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
//  QVariant QQuickTextInput::inputMethodQuery(Qt::InputMethodQuery query,
//      const QVariant &argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QQuickTextInput16inputMethodQueryEN2Qt16InputMethodQueryERK8QVariant(
    const QQuickTextInput *self,
    Qt::InputMethodQuery query,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(query, *argument));
}
#endif  // QT_CONFIG(im)

//  QRectF QQuickTextInput::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QQuickTextInput12boundingRectEv(
    const QQuickTextInput *self) {
  return new QRectF(self->boundingRect());
}

//  QRectF QQuickTextInput::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK15QQuickTextInput8clipRectEv(const QQuickTextInput *self) {
  return new QRectF(self->clipRect());
}

//  bool QQuickTextInput::canPaste() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextInput8canPasteEv(const QQuickTextInput *self) {
  return self->canPaste();
}

//  bool QQuickTextInput::canUndo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextInput7canUndoEv(const QQuickTextInput *self) {
  return self->canUndo();
}

//  bool QQuickTextInput::canRedo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextInput7canRedoEv(const QQuickTextInput *self) {
  return self->canRedo();
}

//  bool QQuickTextInput::isInputMethodComposing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QQuickTextInput22isInputMethodComposingEv(
    const QQuickTextInput *self) {
  return self->isInputMethodComposing();
}

//  Qt::InputMethodHints QQuickTextInput::inputMethodHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQuickTextInput16inputMethodHintsEv(
    const QQuickTextInput *self) {
  return static_cast<int>(self->inputMethodHints().toInt());
}

//  void QQuickTextInput::setInputMethodHints(Qt::InputMethodHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput19setInputMethodHintsE6QFlagsIN2Qt15InputMethodHintEE(
    QQuickTextInput *self,
    int hints) {
  self->setInputMethodHints(QFlags<Qt::InputMethodHint>::fromInt(hints));
}

//  QString QQuickTextInput::getText(int start, int end) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQuickTextInput7getTextEii(
    const QQuickTextInput *self,
    int start,
    int end) {
  return new QString(self->getText(start, end));
}

//  qreal QQuickTextInput::contentWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextInput12contentWidthEv(
    const QQuickTextInput *self) {
  return self->contentWidth();
}

//  qreal QQuickTextInput::contentHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextInput13contentHeightEv(
    const QQuickTextInput *self) {
  return self->contentHeight();
}

//  qreal QQuickTextInput::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextInput7paddingEv(const QQuickTextInput *self) {
  return self->padding();
}

//  void QQuickTextInput::setPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput10setPaddingEd(
    QQuickTextInput *self,
    qreal padding) {
  self->setPadding(padding);
}

//  void QQuickTextInput::resetPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput12resetPaddingEv(QQuickTextInput *self) {
  self->resetPadding();
}

//  qreal QQuickTextInput::topPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextInput10topPaddingEv(
    const QQuickTextInput *self) {
  return self->topPadding();
}

//  void QQuickTextInput::setTopPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput13setTopPaddingEd(
    QQuickTextInput *self,
    qreal padding) {
  self->setTopPadding(padding);
}

//  void QQuickTextInput::resetTopPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput15resetTopPaddingEv(QQuickTextInput *self) {
  self->resetTopPadding();
}

//  qreal QQuickTextInput::leftPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextInput11leftPaddingEv(
    const QQuickTextInput *self) {
  return self->leftPadding();
}

//  void QQuickTextInput::setLeftPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput14setLeftPaddingEd(
    QQuickTextInput *self,
    qreal padding) {
  self->setLeftPadding(padding);
}

//  void QQuickTextInput::resetLeftPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput16resetLeftPaddingEv(QQuickTextInput *self) {
  self->resetLeftPadding();
}

//  qreal QQuickTextInput::rightPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextInput12rightPaddingEv(
    const QQuickTextInput *self) {
  return self->rightPadding();
}

//  void QQuickTextInput::setRightPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput15setRightPaddingEd(
    QQuickTextInput *self,
    qreal padding) {
  self->setRightPadding(padding);
}

//  void QQuickTextInput::resetRightPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput17resetRightPaddingEv(QQuickTextInput *self) {
  self->resetRightPadding();
}

//  qreal QQuickTextInput::bottomPadding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QQuickTextInput13bottomPaddingEv(
    const QQuickTextInput *self) {
  return self->bottomPadding();
}

//  void QQuickTextInput::setBottomPadding(qreal padding)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput16setBottomPaddingEd(
    QQuickTextInput *self,
    qreal padding) {
  self->setBottomPadding(padding);
}

//  void QQuickTextInput::resetBottomPadding()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput18resetBottomPaddingEv(
    QQuickTextInput *self) {
  self->resetBottomPadding();
}

//  void QQuickTextInput::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput10invalidateEv(QQuickTextInput *self) {
  self->invalidate();
}

//  void QQuickTextInput::invalidateFontCaches()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput20invalidateFontCachesEv(
    QQuickTextInput *self) {
  self->invalidateFontCaches();
}

//  void QQuickTextInput::ensureActiveFocus(Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput17ensureActiveFocusEN2Qt11FocusReasonE(
    QQuickTextInput *self,
    Qt::FocusReason reason) {
  self->ensureActiveFocus(reason);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QQuickTextInput::setOldSelectionDefault()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput22setOldSelectionDefaultEv(
    QQuickTextInput *self) {
  self->setOldSelectionDefault();
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QQuickTextInput::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput14geometryChangeERK6QRectFS2_(
    QQuickTextInput *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickTextInput::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickTextInput *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickTextInput::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput15mousePressEventEP11QMouseEvent(
    QQuickTextInput *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QQuickTextInput::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput14mouseMoveEventEP11QMouseEvent(
    QQuickTextInput *self,
    QMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QQuickTextInput::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput17mouseReleaseEventEP11QMouseEvent(
    QQuickTextInput *self,
    QMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QQuickTextInput::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput21mouseDoubleClickEventEP11QMouseEvent(
    QQuickTextInput *self,
    QMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QQuickTextInput::keyPressEvent(QKeyEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput13keyPressEventEP9QKeyEvent(
    QQuickTextInput *self,
    QKeyEvent *ev) {
  self->keyPressEvent(ev);
}

#if QT_CONFIG(im)
//  void QQuickTextInput::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput16inputMethodEventEP17QInputMethodEvent(
    QQuickTextInput *self,
    QInputMethodEvent *a0) {
  self->inputMethodEvent(a0);
}
#endif  // QT_CONFIG(im)

//  void QQuickTextInput::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput16mouseUngrabEventEv(QQuickTextInput *self) {
  self->mouseUngrabEvent();
}

//  bool QQuickTextInput::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickTextInput5eventEP6QEvent(
    QQuickTextInput *self,
    QEvent *e) {
  return self->event(e);
}

//  void QQuickTextInput::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput13focusOutEventEP11QFocusEvent(
    QQuickTextInput *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QQuickTextInput::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput12focusInEventEP11QFocusEvent(
    QQuickTextInput *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QQuickTextInput::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput10timerEventEP11QTimerEvent(
    QQuickTextInput *self,
    QTimerEvent *event) {
  self->timerEvent(event);
}

//  QSGNode *QQuickTextInput::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN15QQuickTextInput15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickTextInput *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return self->updatePaintNode(oldNode, data);
}

//  void QQuickTextInput::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput12updatePolishEv(QQuickTextInput *self) {
  self->updatePolish();
}

//  void QQuickTextInput::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput9selectAllEv(QQuickTextInput *self) {
  self->selectAll();
}

//  void QQuickTextInput::selectWord()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput10selectWordEv(QQuickTextInput *self) {
  self->selectWord();
}

//  void QQuickTextInput::select(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput6selectEii(
    QQuickTextInput *self,
    int start,
    int end) {
  self->select(start, end);
}

//  void QQuickTextInput::deselect()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput8deselectEv(QQuickTextInput *self) {
  self->deselect();
}

//  bool QQuickTextInput::isRightToLeft(int start, int end)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QQuickTextInput13isRightToLeftEii(
    QQuickTextInput *self,
    int start,
    int end) {
  return self->isRightToLeft(start, end);
}

#if QT_CONFIG(clipboard)
//  void QQuickTextInput::cut()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput3cutEv(QQuickTextInput *self) {
  self->cut();
}
#endif  // QT_CONFIG(clipboard)

#if QT_CONFIG(clipboard)
//  void QQuickTextInput::copy()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput4copyEv(QQuickTextInput *self) {
  self->copy();
}
#endif  // QT_CONFIG(clipboard)

#if QT_CONFIG(clipboard)
//  void QQuickTextInput::paste()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput5pasteEv(QQuickTextInput *self) {
  self->paste();
}
#endif  // QT_CONFIG(clipboard)

//  void QQuickTextInput::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput4undoEv(QQuickTextInput *self) {
  self->undo();
}

//  void QQuickTextInput::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput4redoEv(QQuickTextInput *self) {
  self->redo();
}

//  void QQuickTextInput::insert(int position, const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput6insertEiRK7QString(
    QQuickTextInput *self,
    int position,
    const QString *text) {
  self->insert(position, *text);
}

//  void QQuickTextInput::remove(int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput6removeEii(
    QQuickTextInput *self,
    int start,
    int end) {
  self->remove(start, end);
}

//  void QQuickTextInput::ensureVisible(int position)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput13ensureVisibleEi(
    QQuickTextInput *self,
    int position) {
  self->ensureVisible(position);
}

//  void QQuickTextInput::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput5clearEv(QQuickTextInput *self) {
  self->clear();
}

//  void QQuickTextInput::selectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput16selectionChangedEv(QQuickTextInput *self) {
  self->selectionChanged();
}

//  void QQuickTextInput::createCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput12createCursorEv(QQuickTextInput *self) {
  self->createCursor();
}

//  void QQuickTextInput::updateCursorRectangle(bool scroll)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput21updateCursorRectangleEb(
    QQuickTextInput *self,
    bool scroll) {
  self->updateCursorRectangle(scroll);
}

//  void QQuickTextInput::q_canPasteChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput17q_canPasteChangedEv(QQuickTextInput *self) {
  self->q_canPasteChanged();
}

//  void QQuickTextInput::q_updateAlignment()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput17q_updateAlignmentEv(QQuickTextInput *self) {
  self->q_updateAlignment();
}

//  void QQuickTextInput::triggerPreprocess()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput17triggerPreprocessEv(QQuickTextInput *self) {
  self->triggerPreprocess();
}

#if QT_CONFIG(validator)
//  void QQuickTextInput::q_validatorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQuickTextInput18q_validatorChangedEv(
    QQuickTextInput *self) {
  self->q_validatorChanged();
}
#endif  // QT_CONFIG(validator)

//  QQuickTextInputPrivate *QQuickTextInput::d_func()
extern "C" Q_DECL_EXPORT
QQuickTextInputPrivate *ritual_ZN15QQuickTextInput6d_funcEv(
    QQuickTextInput *self) {
  return self->d_func();
}

//  const QQuickTextInputPrivate *QQuickTextInput::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextInputPrivate *ritual_ZNK15QQuickTextInput6d_funcEv(
    const QQuickTextInput *self) {
  return self->d_func();
}

//  QQuickTextInput as the QQuickTextInterface it is built on
extern "C" Q_DECL_EXPORT
QQuickTextInterface *ritual_cast_QQuickTextInput_QQuickTextInterface(
    QQuickTextInput *self) {
  return static_cast<QQuickTextInterface *>(self);
}

//  a Python function taken by a CuteQQuickTextInput, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextInput(
    QQuickTextInput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextInput *>(self)->take(key, call);
}

//  void QQuickTextInput::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput17componentCompleteEv(
    QQuickTextInput *self) {
  self->QQuickTextInput::componentComplete();
}

#if QT_CONFIG(im)
//  QVariant QQuickTextInput::inputMethodQuery(Qt::InputMethodQuery property)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK15QQuickTextInput16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QQuickTextInput *self,
    Qt::InputMethodQuery property) {
  return new QVariant(self->QQuickTextInput::inputMethodQuery(property));
}
#endif  // QT_CONFIG(im)

//  QRectF QQuickTextInput::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK15QQuickTextInput12boundingRectEv(
    const QQuickTextInput *self) {
  return new QRectF(self->QQuickTextInput::boundingRect());
}

//  QRectF QQuickTextInput::clipRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK15QQuickTextInput8clipRectEv(
    const QQuickTextInput *self) {
  return new QRectF(self->QQuickTextInput::clipRect());
}

//  void QQuickTextInput::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput10invalidateEv(QQuickTextInput *self) {
  self->QQuickTextInput::invalidate();
}

//  void QQuickTextInput::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput14geometryChangeERK6QRectFS2_(
    QQuickTextInput *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickTextInput::itemChange(ItemChange change, const ItemChangeData
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickTextInput *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::itemChange(
      change,
      *value);
}

//  void QQuickTextInput::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput15mousePressEventEP11QMouseEvent(
    QQuickTextInput *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::mousePressEvent(
      event);
}

//  void QQuickTextInput::mouseMoveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput14mouseMoveEventEP11QMouseEvent(
    QQuickTextInput *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::mouseMoveEvent(
      event);
}

//  void QQuickTextInput::mouseReleaseEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput17mouseReleaseEventEP11QMouseEvent(
    QQuickTextInput *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::mouseReleaseEvent(
      event);
}

//  void QQuickTextInput::mouseDoubleClickEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput21mouseDoubleClickEventEP11QMouseEvent(
    QQuickTextInput *self,
    QMouseEvent *event) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::mouseDoubleClickEvent(
      event);
}

//  void QQuickTextInput::keyPressEvent(QKeyEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput13keyPressEventEP9QKeyEvent(
    QQuickTextInput *self,
    QKeyEvent *ev) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::keyPressEvent(
      ev);
}

#if QT_CONFIG(im)
//  void QQuickTextInput::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput16inputMethodEventEP17QInputMethodEvent(
    QQuickTextInput *self,
    QInputMethodEvent *a0) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::inputMethodEvent(
      a0);
}
#endif  // QT_CONFIG(im)

//  void QQuickTextInput::mouseUngrabEvent()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput16mouseUngrabEventEv(
    QQuickTextInput *self) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::mouseUngrabEvent();
}

//  bool QQuickTextInput::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QQuickTextInput5eventEP6QEvent(
    QQuickTextInput *self,
    QEvent *e) {
  return static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::event(
      e);
}

//  void QQuickTextInput::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput13focusOutEventEP11QFocusEvent(
    QQuickTextInput *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::focusOutEvent(
      event);
}

//  void QQuickTextInput::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput12focusInEventEP11QFocusEvent(
    QQuickTextInput *self,
    QFocusEvent *event) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::focusInEvent(
      event);
}

//  void QQuickTextInput::timerEvent(QTimerEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput10timerEventEP11QTimerEvent(
    QQuickTextInput *self,
    QTimerEvent *event) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::timerEvent(
      event);
}

//  QSGNode *QQuickTextInput::updatePaintNode(QSGNode *oldNode,
//      UpdatePaintNodeData *data)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN15QQuickTextInput15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickTextInput *self,
    QSGNode *oldNode,
    QQuickItem::UpdatePaintNodeData *data) {
  return static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::updatePaintNode(
      oldNode,
      data);
}

//  void QQuickTextInput::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN15QQuickTextInput12updatePolishEv(QQuickTextInput *self) {
  static_cast<OwnQQuickTextInput *>(self)->OwnQQuickTextInput::updatePolish();
}
