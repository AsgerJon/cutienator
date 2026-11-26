//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextinput_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qrect.h>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickPre64TextInput that Python can take functions over in. Every QQuickPre64TextInput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPre64TextInputCall0)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickPre64TextInputCall1)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef const QRectF * (*CuteQQuickPre64TextInputCall2)(const void *, int *);
typedef const QRectF * (*CuteQQuickPre64TextInputCall3)(const void *, int *);
typedef void (*CuteQQuickPre64TextInputCall4)(const void *, int *);
typedef void (*CuteQQuickPre64TextInputCall5)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickPre64TextInputCall6)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickPre64TextInputCall7)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPre64TextInputCall8)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPre64TextInputCall9)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPre64TextInputCall10)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickPre64TextInputCall11)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickPre64TextInputCall12)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickPre64TextInputCall13)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPre64TextInputCall14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPre64TextInputCall15)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickPre64TextInputCall16)(const void *, QFocusEvent *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPre64TextInputCall17)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void * (*CuteQQuickPre64TextInputCall18)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickPre64TextInputCall19)(const void *, int *);
typedef bool (*CuteQQuickPre64TextInputCall20)(const void *, const QPointF *, int *);
typedef bool (*CuteQQuickPre64TextInputCall21)(const void *, int *);
typedef void * (*CuteQQuickPre64TextInputCall22)(const void *, int *);
typedef void (*CuteQQuickPre64TextInputCall23)(const void *, int *);
typedef void (*CuteQQuickPre64TextInputCall24)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickPre64TextInputCall25)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPre64TextInputCall26)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickPre64TextInputCall27)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickPre64TextInputCall28)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickPre64TextInputCall29)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickPre64TextInputCall30)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPre64TextInputCall31)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPre64TextInputCall32)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPre64TextInputCall33)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickPre64TextInputCall34)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickPre64TextInputCall35)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickPre64TextInputCall36)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickPre64TextInputCall37)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPre64TextInputCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPre64TextInputCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPre64TextInputCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickPre64TextInputCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickPre64TextInput : public QQuickPre64TextInput {
public:
  using QQuickPre64TextInput::QQuickPre64TextInput;
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
      CuteQQuickPre64TextInputCall0 call = reinterpret_cast<CuteQQuickPre64TextInputCall0>(taken[0]);
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
      CuteQQuickPre64TextInputCall1 call = reinterpret_cast<CuteQQuickPre64TextInputCall1>(taken[1]);
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
      CuteQQuickPre64TextInputCall2 call = reinterpret_cast<CuteQQuickPre64TextInputCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextInput::boundingRect();
  }

  //  QRectF QQuickTextInput::clipRect() const
  QRectF clipRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall3 call = reinterpret_cast<CuteQQuickPre64TextInputCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextInput::clipRect();
  }

  //  void QQuickTextInput::invalidate()
  void invalidate() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall4 call = reinterpret_cast<CuteQQuickPre64TextInputCall4>(taken[4]);
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
      CuteQQuickPre64TextInputCall5 call = reinterpret_cast<CuteQQuickPre64TextInputCall5>(taken[5]);
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
      CuteQQuickPre64TextInputCall6 call = reinterpret_cast<CuteQQuickPre64TextInputCall6>(taken[6]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickTextInput::itemChange(change, value);
  }

  //  void QQuickTextInput::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall7 call = reinterpret_cast<CuteQQuickPre64TextInputCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextInput::mousePressEvent(event);
  }

  //  void QQuickTextInput::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall8 call = reinterpret_cast<CuteQQuickPre64TextInputCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextInput::mouseMoveEvent(event);
  }

  //  void QQuickTextInput::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall9 call = reinterpret_cast<CuteQQuickPre64TextInputCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextInput::mouseReleaseEvent(event);
  }

  //  void QQuickTextInput::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall10 call = reinterpret_cast<CuteQQuickPre64TextInputCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextInput::mouseDoubleClickEvent(event);
  }

  //  void QQuickTextInput::keyPressEvent(QKeyEvent *ev)
  void keyPressEvent(QKeyEvent *ev) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall11 call = reinterpret_cast<CuteQQuickPre64TextInputCall11>(taken[11]);
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
      CuteQQuickPre64TextInputCall12 call = reinterpret_cast<CuteQQuickPre64TextInputCall12>(taken[12]);
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
      CuteQQuickPre64TextInputCall13 call = reinterpret_cast<CuteQQuickPre64TextInputCall13>(taken[13]);
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
      CuteQQuickPre64TextInputCall14 call = reinterpret_cast<CuteQQuickPre64TextInputCall14>(taken[14]);
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
      CuteQQuickPre64TextInputCall15 call = reinterpret_cast<CuteQQuickPre64TextInputCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickTextInput::focusOutEvent(event);
  }

  //  void QQuickTextInput::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall16 call = reinterpret_cast<CuteQQuickPre64TextInputCall16>(taken[16]);
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
      CuteQQuickPre64TextInputCall17 call = reinterpret_cast<CuteQQuickPre64TextInputCall17>(taken[17]);
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
      CuteQQuickPre64TextInputCall18 call = reinterpret_cast<CuteQQuickPre64TextInputCall18>(taken[18]);
      void * given = call(this, oldNode, data, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickTextInput::updatePaintNode(oldNode, data);
  }

  //  void QQuickTextInput::updatePolish()
  void updatePolish() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall19 call = reinterpret_cast<CuteQQuickPre64TextInputCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickTextInput::updatePolish();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall20 call = reinterpret_cast<CuteQQuickPre64TextInputCall20>(taken[20]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall21 call = reinterpret_cast<CuteQQuickPre64TextInputCall21>(taken[21]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall22 call = reinterpret_cast<CuteQQuickPre64TextInputCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall23 call = reinterpret_cast<CuteQQuickPre64TextInputCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall24 call = reinterpret_cast<CuteQQuickPre64TextInputCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall25 call = reinterpret_cast<CuteQQuickPre64TextInputCall25>(taken[25]);
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
      CuteQQuickPre64TextInputCall26 call = reinterpret_cast<CuteQQuickPre64TextInputCall26>(taken[26]);
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
      CuteQQuickPre64TextInputCall27 call = reinterpret_cast<CuteQQuickPre64TextInputCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall28 call = reinterpret_cast<CuteQQuickPre64TextInputCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall29 call = reinterpret_cast<CuteQQuickPre64TextInputCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall30 call = reinterpret_cast<CuteQQuickPre64TextInputCall30>(taken[30]);
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
      CuteQQuickPre64TextInputCall31 call = reinterpret_cast<CuteQQuickPre64TextInputCall31>(taken[31]);
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
      CuteQQuickPre64TextInputCall32 call = reinterpret_cast<CuteQQuickPre64TextInputCall32>(taken[32]);
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
      CuteQQuickPre64TextInputCall33 call = reinterpret_cast<CuteQQuickPre64TextInputCall33>(taken[33]);
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
      CuteQQuickPre64TextInputCall34 call = reinterpret_cast<CuteQQuickPre64TextInputCall34>(taken[34]);
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
      CuteQQuickPre64TextInputCall35 call = reinterpret_cast<CuteQQuickPre64TextInputCall35>(taken[35]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickPre64TextInputCall36 call = reinterpret_cast<CuteQQuickPre64TextInputCall36>(taken[36]);
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
      CuteQQuickPre64TextInputCall37 call = reinterpret_cast<CuteQQuickPre64TextInputCall37>(taken[37]);
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
      CuteQQuickPre64TextInputCall38 call = reinterpret_cast<CuteQQuickPre64TextInputCall38>(taken[38]);
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
      CuteQQuickPre64TextInputCall39 call = reinterpret_cast<CuteQQuickPre64TextInputCall39>(taken[39]);
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
      CuteQQuickPre64TextInputCall40 call = reinterpret_cast<CuteQQuickPre64TextInputCall40>(taken[40]);
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
      CuteQQuickPre64TextInputCall41 call = reinterpret_cast<CuteQQuickPre64TextInputCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickPre64TextInput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickPre64TextInput10metaObjectEv(
    const QQuickPre64TextInput *self) {
  return self->metaObject();
}

//  void *QQuickPre64TextInput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickPre64TextInput11qt_metacastEPKc(
    QQuickPre64TextInput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickPre64TextInput::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickPre64TextInput11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickPre64TextInput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  a Python function taken by a CuteQQuickPre64TextInput, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPre64TextInput(
    QQuickPre64TextInput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPre64TextInput *>(self)->take(key, call);
}

#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
