//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickvideooutput_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qtmultimediaquickglobal_p.h>
#include <QtMultimediaQuick/QtMultimediaQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimediaQuick/6.12.0/QtMultimediaQuick/private/qquickvideooutput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qsize.h>
#include <QtMultimedia/qvideoframe.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <optional>
#include <chrono>

//  Only a class built on QQuickVideoOutput may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickVideoOutput : QQuickVideoOutput {
  using QQuickVideoOutput::updatePaintNode;
  using QQuickVideoOutput::itemChange;
  using QQuickVideoOutput::geometryChange;
  using QQuickVideoOutput::releaseResources;
};

//  A QQuickVideoOutput that Python can take functions over in. Every QQuickVideoOutput
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQQuickVideoOutputCall0)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickVideoOutputCall1)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickVideoOutputCall2)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickVideoOutputCall3)(const void *, int *);
typedef const QRectF * (*CuteQQuickVideoOutputCall4)(const void *, int *);
typedef const QRectF * (*CuteQQuickVideoOutputCall5)(const void *, int *);
typedef bool (*CuteQQuickVideoOutputCall6)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickVideoOutputCall7)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickVideoOutputCall8)(const void *, int *);
typedef void * (*CuteQQuickVideoOutputCall9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickVideoOutputCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVideoOutputCall11)(const void *, int *);
typedef void (*CuteQQuickVideoOutputCall12)(const void *, int *);
typedef void (*CuteQQuickVideoOutputCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickVideoOutputCall14)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickVideoOutputCall15)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickVideoOutputCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickVideoOutputCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickVideoOutputCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickVideoOutputCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickVideoOutputCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickVideoOutputCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickVideoOutputCall22)(const void *, int *);
typedef void (*CuteQQuickVideoOutputCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickVideoOutputCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickVideoOutputCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickVideoOutputCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickVideoOutputCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickVideoOutputCall28)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickVideoOutputCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickVideoOutputCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickVideoOutputCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickVideoOutputCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickVideoOutputCall33)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickVideoOutputCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickVideoOutputCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVideoOutputCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVideoOutputCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVideoOutputCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVideoOutputCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickVideoOutputCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickVideoOutput : public QQuickVideoOutput {
public:
  using QQuickVideoOutput::QQuickVideoOutput;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[6] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[23] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[28] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSGNode *QQuickVideoOutput::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickVideoOutputCall0 call = reinterpret_cast<CuteQQuickVideoOutputCall0>(taken[0]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickVideoOutput::updatePaintNode(a0, a1);
  }

  //  void QQuickVideoOutput::itemChange(ItemChange change, const
  //      ItemChangeData &changeData)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &changeData) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickVideoOutputCall1 call = reinterpret_cast<CuteQQuickVideoOutputCall1>(taken[1]);
      call(this, static_cast<int>(change), &changeData, &handled);
      if (handled) return;
    }
    QQuickVideoOutput::itemChange(change, changeData);
  }

  //  void QQuickVideoOutput::geometryChange(const QRectF &newGeometry,
  //      const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickVideoOutputCall2 call = reinterpret_cast<CuteQQuickVideoOutputCall2>(taken[2]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickVideoOutput::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickVideoOutput::releaseResources()
  void releaseResources() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickVideoOutputCall3 call = reinterpret_cast<CuteQQuickVideoOutputCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickVideoOutput::releaseResources();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickVideoOutputCall4 call = reinterpret_cast<CuteQQuickVideoOutputCall4>(taken[4]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickVideoOutputCall5 call = reinterpret_cast<CuteQQuickVideoOutputCall5>(taken[5]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickVideoOutputCall6 call = reinterpret_cast<CuteQQuickVideoOutputCall6>(taken[6]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickVideoOutputCall7 call = reinterpret_cast<CuteQQuickVideoOutputCall7>(taken[7]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickVideoOutputCall8 call = reinterpret_cast<CuteQQuickVideoOutputCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickVideoOutputCall9 call = reinterpret_cast<CuteQQuickVideoOutputCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickVideoOutputCall10 call = reinterpret_cast<CuteQQuickVideoOutputCall10>(taken[10]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickVideoOutputCall11 call = reinterpret_cast<CuteQQuickVideoOutputCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickVideoOutputCall12 call = reinterpret_cast<CuteQQuickVideoOutputCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickVideoOutputCall13 call = reinterpret_cast<CuteQQuickVideoOutputCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickVideoOutputCall14 call = reinterpret_cast<CuteQQuickVideoOutputCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickVideoOutputCall15 call = reinterpret_cast<CuteQQuickVideoOutputCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickVideoOutputCall16 call = reinterpret_cast<CuteQQuickVideoOutputCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickVideoOutputCall17 call = reinterpret_cast<CuteQQuickVideoOutputCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickVideoOutputCall18 call = reinterpret_cast<CuteQQuickVideoOutputCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickVideoOutputCall19 call = reinterpret_cast<CuteQQuickVideoOutputCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickVideoOutputCall20 call = reinterpret_cast<CuteQQuickVideoOutputCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickVideoOutputCall21 call = reinterpret_cast<CuteQQuickVideoOutputCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickVideoOutputCall22 call = reinterpret_cast<CuteQQuickVideoOutputCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickVideoOutputCall23 call = reinterpret_cast<CuteQQuickVideoOutputCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickVideoOutputCall24 call = reinterpret_cast<CuteQQuickVideoOutputCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickVideoOutputCall25 call = reinterpret_cast<CuteQQuickVideoOutputCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickVideoOutputCall26 call = reinterpret_cast<CuteQQuickVideoOutputCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickVideoOutputCall27 call = reinterpret_cast<CuteQQuickVideoOutputCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickVideoOutputCall28 call = reinterpret_cast<CuteQQuickVideoOutputCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickVideoOutputCall29 call = reinterpret_cast<CuteQQuickVideoOutputCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickVideoOutputCall30 call = reinterpret_cast<CuteQQuickVideoOutputCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickVideoOutputCall31 call = reinterpret_cast<CuteQQuickVideoOutputCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickVideoOutputCall32 call = reinterpret_cast<CuteQQuickVideoOutputCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickVideoOutputCall33 call = reinterpret_cast<CuteQQuickVideoOutputCall33>(taken[33]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickVideoOutputCall34 call = reinterpret_cast<CuteQQuickVideoOutputCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickVideoOutputCall35 call = reinterpret_cast<CuteQQuickVideoOutputCall35>(taken[35]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickVideoOutputCall36 call = reinterpret_cast<CuteQQuickVideoOutputCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickVideoOutputCall37 call = reinterpret_cast<CuteQQuickVideoOutputCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickVideoOutputCall38 call = reinterpret_cast<CuteQQuickVideoOutputCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickVideoOutputCall39 call = reinterpret_cast<CuteQQuickVideoOutputCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQuickVideoOutputCall40 call = reinterpret_cast<CuteQQuickVideoOutputCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickVideoOutput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickVideoOutput10metaObjectEv(
    const QQuickVideoOutput *self) {
  return self->metaObject();
}

//  void *QQuickVideoOutput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickVideoOutput11qt_metacastEPKc(
    QQuickVideoOutput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickVideoOutput::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickVideoOutput11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickVideoOutput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickVideoOutput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickVideoOutput2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickVideoOutput::tr(s, c, n));
}

//  QQuickVideoOutput::QQuickVideoOutput(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickVideoOutput *ritual_ZN17QQuickVideoOutputC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickVideoOutput(parent);
}

//  QQuickVideoOutput::~QQuickVideoOutput()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutputD1Ev(QQuickVideoOutput *self) {
  delete self;
}

//  QVideoSink *QQuickVideoOutput::videoSink() const
extern "C" Q_DECL_EXPORT
QVideoSink *ritual_ZNK17QQuickVideoOutput9videoSinkEv(
    const QQuickVideoOutput *self) {
  return self->videoSink();
}

//  FillMode QQuickVideoOutput::fillMode() const
extern "C" Q_DECL_EXPORT
QQuickVideoOutput::FillMode ritual_ZNK17QQuickVideoOutput8fillModeEv(
    const QQuickVideoOutput *self) {
  return self->fillMode();
}

//  void QQuickVideoOutput::setFillMode(FillMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput11setFillModeENS_8FillModeE(
    QQuickVideoOutput *self,
    QQuickVideoOutput::FillMode mode) {
  self->setFillMode(mode);
}

//  int QQuickVideoOutput::orientation() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickVideoOutput11orientationEv(
    const QQuickVideoOutput *self) {
  return self->orientation();
}

//  void QQuickVideoOutput::setOrientation(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput14setOrientationEi(
    QQuickVideoOutput *self,
    int a0) {
  self->setOrientation(a0);
}

//  bool QQuickVideoOutput::mirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickVideoOutput8mirroredEv(
    const QQuickVideoOutput *self) {
  return self->mirrored();
}

//  void QQuickVideoOutput::setMirrored(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput11setMirroredEb(
    QQuickVideoOutput *self,
    bool a0) {
  self->setMirrored(a0);
}

//  QRectF QQuickVideoOutput::sourceRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickVideoOutput10sourceRectEv(
    const QQuickVideoOutput *self) {
  return new QRectF(self->sourceRect());
}

//  QRectF QQuickVideoOutput::contentRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickVideoOutput11contentRectEv(
    const QQuickVideoOutput *self) {
  return new QRectF(self->contentRect());
}

//  EndOfStreamPolicy QQuickVideoOutput::endOfStreamPolicy() const
extern "C" Q_DECL_EXPORT
QQuickVideoOutput::EndOfStreamPolicy ritual_ZNK17QQuickVideoOutput17endOfStreamPolicyEv(
    const QQuickVideoOutput *self) {
  return self->endOfStreamPolicy();
}

//  void QQuickVideoOutput::setEndOfStreamPolicy(EndOfStreamPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput20setEndOfStreamPolicyENS_17EndOfStreamPolicyE(
    QQuickVideoOutput *self,
    QQuickVideoOutput::EndOfStreamPolicy policy) {
  self->setEndOfStreamPolicy(policy);
}

//  void QQuickVideoOutput::clearOutput()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput11clearOutputEv(QQuickVideoOutput *self) {
  self->clearOutput();
}

//  void QQuickVideoOutput::sourceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput13sourceChangedEv(QQuickVideoOutput *self) {
  self->sourceChanged();
}

//  void QQuickVideoOutput::fillModeChanged(QQuickVideoOutput::FillMode a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput15fillModeChangedENS_8FillModeE(
    QQuickVideoOutput *self,
    QQuickVideoOutput::FillMode a0) {
  self->fillModeChanged(a0);
}

//  void QQuickVideoOutput::orientationChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput18orientationChangedEv(
    QQuickVideoOutput *self) {
  self->orientationChanged();
}

//  void QQuickVideoOutput::mirroredChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput15mirroredChangedEv(
    QQuickVideoOutput *self) {
  self->mirroredChanged();
}

//  void QQuickVideoOutput::sourceRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput17sourceRectChangedEv(
    QQuickVideoOutput *self) {
  self->sourceRectChanged();
}

//  void QQuickVideoOutput::contentRectChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput18contentRectChangedEv(
    QQuickVideoOutput *self) {
  self->contentRectChanged();
}

//  void QQuickVideoOutput::endOfStreamPolicyChanged(QQuickVideoOutput::EndOf
//      StreamPolicy a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput24endOfStreamPolicyChangedENS_17EndOfStreamPolicyE(
    QQuickVideoOutput *self,
    QQuickVideoOutput::EndOfStreamPolicy a0) {
  self->endOfStreamPolicyChanged(a0);
}

//  QSGNode *QQuickVideoOutput::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN17QQuickVideoOutput15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickVideoOutput *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuickVideoOutput::itemChange(ItemChange change, const
//      ItemChangeData &changeData)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickVideoOutput *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *changeData) {
  self->itemChange(change, *changeData);
}

//  void QQuickVideoOutput::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput14geometryChangeERK6QRectFS2_(
    QQuickVideoOutput *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  void QQuickVideoOutput::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput16releaseResourcesEv(
    QQuickVideoOutput *self) {
  self->releaseResources();
}

//  QSize QQuickVideoOutput::nativeSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK17QQuickVideoOutput10nativeSizeEv(
    const QQuickVideoOutput *self) {
  return new QSize(self->nativeSize());
}

//  void QQuickVideoOutput::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput14updateGeometryEv(
    QQuickVideoOutput *self) {
  self->updateGeometry();
}

//  QRectF QQuickVideoOutput::adjustedViewport() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickVideoOutput16adjustedViewportEv(
    const QQuickVideoOutput *self) {
  return new QRectF(self->adjustedViewport());
}

//  void QQuickVideoOutput::setFrame(const QVideoFrame &frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput8setFrameERK11QVideoFrame(
    QQuickVideoOutput *self,
    const QVideoFrame *frame) {
  self->setFrame(*frame);
}

//  void QQuickVideoOutput::initRhiForSink()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput14initRhiForSinkEv(
    QQuickVideoOutput *self) {
  self->initRhiForSink();
}

//  void QQuickVideoOutput::updateHdr(QSGVideoNode *videoNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput9updateHdrEP12QSGVideoNode(
    QQuickVideoOutput *self,
    QSGVideoNode *videoNode) {
  self->updateHdr(videoNode);
}

//  void QQuickVideoOutput::disconnectWindowConnections()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput27disconnectWindowConnectionsEv(
    QQuickVideoOutput *self) {
  self->disconnectWindowConnections();
}

//  void QQuickVideoOutput::_q_newFrame(QSize a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput11_q_newFrameE5QSize(
    QQuickVideoOutput *self,
    const QSize *a0) {
  self->_q_newFrame(*a0);
}

//  void QQuickVideoOutput::_q_updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput17_q_updateGeometryEv(
    QQuickVideoOutput *self) {
  self->_q_updateGeometry();
}

//  void QQuickVideoOutput::setSignalBackoff(std::optional<std::chrono::nanos
//      econds> a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickVideoOutput16setSignalBackoffESt8optionalINSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEE(
    const std::optional<std::chrono::nanoseconds> *a0) {
  QQuickVideoOutput::setSignalBackoff(*a0);
}

//  a Python function taken by a CuteQQuickVideoOutput, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickVideoOutput(
    QQuickVideoOutput *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickVideoOutput *>(self)->take(key, call);
}

//  QSGNode *QQuickVideoOutput::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN17QQuickVideoOutput15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuickVideoOutput *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuickVideoOutput *>(self)->OwnQQuickVideoOutput::updatePaintNode(
      a0,
      a1);
}

//  void QQuickVideoOutput::itemChange(ItemChange change, const
//      ItemChangeData &changeData)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickVideoOutput10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickVideoOutput *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *changeData) {
  static_cast<OwnQQuickVideoOutput *>(self)->OwnQQuickVideoOutput::itemChange(
      change,
      *changeData);
}

//  void QQuickVideoOutput::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickVideoOutput14geometryChangeERK6QRectFS2_(
    QQuickVideoOutput *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuickVideoOutput *>(self)->OwnQQuickVideoOutput::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  void QQuickVideoOutput::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickVideoOutput16releaseResourcesEv(
    QQuickVideoOutput *self) {
  static_cast<OwnQQuickVideoOutput *>(self)->OwnQQuickVideoOutput::releaseResources();
}
