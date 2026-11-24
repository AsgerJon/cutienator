//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickchecklabel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickchecklabel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQuickCheckLabel that Python can take functions over in. Every QQuickCheckLabel
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickCheckLabelCall0)(const void *, int *);
typedef const QRectF * (*CuteQQuickCheckLabelCall1)(const void *, int *);
typedef const QRectF * (*CuteQQuickCheckLabelCall2)(const void *, int *);
typedef void (*CuteQQuickCheckLabelCall3)(const void *, int *);
typedef void (*CuteQQuickCheckLabelCall4)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickCheckLabelCall5)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickCheckLabelCall6)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickCheckLabelCall7)(const void *, const QRectF *, const QRectF *, int *);
typedef void * (*CuteQQuickCheckLabelCall8)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickCheckLabelCall9)(const void *, int *);
typedef void (*CuteQQuickCheckLabelCall10)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickCheckLabelCall11)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickCheckLabelCall12)(const void *, QHoverEvent *, int *);
typedef bool (*CuteQQuickCheckLabelCall13)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickCheckLabelCall14)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickCheckLabelCall15)(const void *, int *);
typedef void * (*CuteQQuickCheckLabelCall16)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickCheckLabelCall17)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCheckLabelCall18)(const void *, int *);
typedef void (*CuteQQuickCheckLabelCall19)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickCheckLabelCall20)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickCheckLabelCall21)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickCheckLabelCall22)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickCheckLabelCall23)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickCheckLabelCall24)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickCheckLabelCall25)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickCheckLabelCall26)(const void *, int *);
typedef void (*CuteQQuickCheckLabelCall27)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickCheckLabelCall28)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickCheckLabelCall29)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickCheckLabelCall30)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickCheckLabelCall31)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickCheckLabelCall32)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickCheckLabelCall33)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickCheckLabelCall34)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickCheckLabelCall35)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickCheckLabelCall36)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCheckLabelCall37)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCheckLabelCall38)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCheckLabelCall39)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCheckLabelCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickCheckLabelCall41)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickCheckLabel : public QQuickCheckLabel {
public:
  using QQuickCheckLabel::QQuickCheckLabel;
  void *taken[42] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickTextInterface10invalidateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[16] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
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

  //  void QQuickText::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickCheckLabelCall0 call = reinterpret_cast<CuteQQuickCheckLabelCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickText::componentComplete();
  }

  //  QRectF QQuickText::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickCheckLabelCall1 call = reinterpret_cast<CuteQQuickCheckLabelCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickText::boundingRect();
  }

  //  QRectF QQuickText::clipRect() const
  QRectF clipRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickCheckLabelCall2 call = reinterpret_cast<CuteQQuickCheckLabelCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickText::clipRect();
  }

  //  void QQuickText::invalidate()
  void invalidate() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickCheckLabelCall3 call = reinterpret_cast<CuteQQuickCheckLabelCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickText::invalidate();
  }

  //  void QQuickText::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickCheckLabelCall4 call = reinterpret_cast<CuteQQuickCheckLabelCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::mousePressEvent(event);
  }

  //  void QQuickText::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickCheckLabelCall5 call = reinterpret_cast<CuteQQuickCheckLabelCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::mouseReleaseEvent(event);
  }

  //  void QQuickText::itemChange(ItemChange change, const ItemChangeData
  //      &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickCheckLabelCall6 call = reinterpret_cast<CuteQQuickCheckLabelCall6>(taken[6]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickText::itemChange(change, value);
  }

  //  void QQuickText::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickCheckLabelCall7 call = reinterpret_cast<CuteQQuickCheckLabelCall7>(taken[7]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickText::geometryChange(newGeometry, oldGeometry);
  }

  //  QSGNode *QQuickText::updatePaintNode(QSGNode *a0, UpdatePaintNodeData
  //      *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickCheckLabelCall8 call = reinterpret_cast<CuteQQuickCheckLabelCall8>(taken[8]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickText::updatePaintNode(a0, a1);
  }

  //  void QQuickText::updatePolish()
  void updatePolish() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickCheckLabelCall9 call = reinterpret_cast<CuteQQuickCheckLabelCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickText::updatePolish();
  }

  //  void QQuickText::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickCheckLabelCall10 call = reinterpret_cast<CuteQQuickCheckLabelCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::hoverEnterEvent(event);
  }

  //  void QQuickText::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickCheckLabelCall11 call = reinterpret_cast<CuteQQuickCheckLabelCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::hoverMoveEvent(event);
  }

  //  void QQuickText::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickCheckLabelCall12 call = reinterpret_cast<CuteQQuickCheckLabelCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickText::hoverLeaveEvent(event);
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickCheckLabelCall13 call = reinterpret_cast<CuteQQuickCheckLabelCall13>(taken[13]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickCheckLabelCall14 call = reinterpret_cast<CuteQQuickCheckLabelCall14>(taken[14]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickCheckLabelCall15 call = reinterpret_cast<CuteQQuickCheckLabelCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickCheckLabelCall16 call = reinterpret_cast<CuteQQuickCheckLabelCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickCheckLabelCall17 call = reinterpret_cast<CuteQQuickCheckLabelCall17>(taken[17]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickCheckLabelCall18 call = reinterpret_cast<CuteQQuickCheckLabelCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickCheckLabelCall19 call = reinterpret_cast<CuteQQuickCheckLabelCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickCheckLabelCall20 call = reinterpret_cast<CuteQQuickCheckLabelCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickCheckLabelCall21 call = reinterpret_cast<CuteQQuickCheckLabelCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickCheckLabelCall22 call = reinterpret_cast<CuteQQuickCheckLabelCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickCheckLabelCall23 call = reinterpret_cast<CuteQQuickCheckLabelCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickCheckLabelCall24 call = reinterpret_cast<CuteQQuickCheckLabelCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickCheckLabelCall25 call = reinterpret_cast<CuteQQuickCheckLabelCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickCheckLabelCall26 call = reinterpret_cast<CuteQQuickCheckLabelCall26>(taken[26]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickCheckLabelCall27 call = reinterpret_cast<CuteQQuickCheckLabelCall27>(taken[27]);
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
      CuteQQuickCheckLabelCall28 call = reinterpret_cast<CuteQQuickCheckLabelCall28>(taken[28]);
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
      CuteQQuickCheckLabelCall29 call = reinterpret_cast<CuteQQuickCheckLabelCall29>(taken[29]);
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
      CuteQQuickCheckLabelCall30 call = reinterpret_cast<CuteQQuickCheckLabelCall30>(taken[30]);
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
      CuteQQuickCheckLabelCall31 call = reinterpret_cast<CuteQQuickCheckLabelCall31>(taken[31]);
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
      CuteQQuickCheckLabelCall32 call = reinterpret_cast<CuteQQuickCheckLabelCall32>(taken[32]);
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
      CuteQQuickCheckLabelCall33 call = reinterpret_cast<CuteQQuickCheckLabelCall33>(taken[33]);
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
      CuteQQuickCheckLabelCall34 call = reinterpret_cast<CuteQQuickCheckLabelCall34>(taken[34]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickCheckLabelCall35 call = reinterpret_cast<CuteQQuickCheckLabelCall35>(taken[35]);
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
      CuteQQuickCheckLabelCall36 call = reinterpret_cast<CuteQQuickCheckLabelCall36>(taken[36]);
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
      CuteQQuickCheckLabelCall37 call = reinterpret_cast<CuteQQuickCheckLabelCall37>(taken[37]);
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
      CuteQQuickCheckLabelCall38 call = reinterpret_cast<CuteQQuickCheckLabelCall38>(taken[38]);
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
      CuteQQuickCheckLabelCall39 call = reinterpret_cast<CuteQQuickCheckLabelCall39>(taken[39]);
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
      CuteQQuickCheckLabelCall40 call = reinterpret_cast<CuteQQuickCheckLabelCall40>(taken[40]);
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
      CuteQQuickCheckLabelCall41 call = reinterpret_cast<CuteQQuickCheckLabelCall41>(taken[41]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickCheckLabel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuickCheckLabel10metaObjectEv(
    const QQuickCheckLabel *self) {
  return self->metaObject();
}

//  QString QQuickCheckLabel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuickCheckLabel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickCheckLabel::tr(s, c, n));
}

//  QQuickCheckLabel::QQuickCheckLabel(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickCheckLabel *ritual_ZN16QQuickCheckLabelC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickCheckLabel(parent);
}

//  a Python function taken by a CuteQQuickCheckLabel, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickCheckLabel(
    QQuickCheckLabel *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickCheckLabel *>(self)->take(key, call);
}
