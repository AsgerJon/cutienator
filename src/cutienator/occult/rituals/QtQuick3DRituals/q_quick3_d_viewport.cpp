//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dviewport_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dviewport_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dpickresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qpoint.h>
#include <QtQuick3D/qquick3dobject.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderpickresult.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qeventpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>
#include <QtQuick3D/QQuick3DObject>
#include <QtCore/QPair>
#include <QtQuick/QQuickItem>
#include <QtCore/QPointF>
#include <QtCore/QVarLengthArray>
#include <QtGui/QVector3D>
#include <QtGui/QEventPoint>

//  Only a class built on QQuick3DViewport may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DViewport : QQuick3DViewport {
  using QQuick3DViewport::geometryChange;
  using QQuick3DViewport::updatePaintNode;
  using QQuick3DViewport::itemChange;
  using QQuick3DViewport::event;
  using QQuick3DViewport::componentComplete;
};

//  A QQuick3DViewport that Python can take functions over in. Every QQuick3DViewport
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuick3DViewportCall0)(const void *, int *);
typedef void * (*CuteQQuick3DViewportCall1)(const void *, int *);
typedef void (*CuteQQuick3DViewportCall2)(const void *, int *);
typedef void (*CuteQQuick3DViewportCall3)(const void *, const QRectF *, const QRectF *, int *);
typedef void * (*CuteQQuick3DViewportCall4)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuick3DViewportCall5)(const void *, int, const QQuickItem::ItemChangeData *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DViewportCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DViewportCall7)(const void *, int *);
typedef const QRectF * (*CuteQQuick3DViewportCall8)(const void *, int *);
typedef const QRectF * (*CuteQQuick3DViewportCall9)(const void *, int *);
typedef bool (*CuteQQuick3DViewportCall10)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuick3DViewportCall11)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuick3DViewportCall12)(const void *, int *);
typedef void (*CuteQQuick3DViewportCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuick3DViewportCall14)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuick3DViewportCall15)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuick3DViewportCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuick3DViewportCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuick3DViewportCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuick3DViewportCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuick3DViewportCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuick3DViewportCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuick3DViewportCall22)(const void *, int *);
typedef void (*CuteQQuick3DViewportCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuick3DViewportCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuick3DViewportCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuick3DViewportCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuick3DViewportCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuick3DViewportCall28)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuick3DViewportCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuick3DViewportCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuick3DViewportCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuick3DViewportCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuick3DViewportCall33)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuick3DViewportCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DViewportCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DViewportCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DViewportCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DViewportCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DViewportCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DViewportCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DViewport : public QQuick3DViewport {
public:
  using QQuick3DViewport::QQuick3DViewport;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
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

  //  bool QQuick3DViewport::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DViewportCall0 call = reinterpret_cast<CuteQQuick3DViewportCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuick3DViewport::isTextureProvider();
  }

  //  QSGTextureProvider *QQuick3DViewport::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DViewportCall1 call = reinterpret_cast<CuteQQuick3DViewportCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuick3DViewport::textureProvider();
  }

  //  void QQuick3DViewport::releaseResources()
  void releaseResources() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuick3DViewportCall2 call = reinterpret_cast<CuteQQuick3DViewportCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DViewport::releaseResources();
  }

  //  void QQuick3DViewport::geometryChange(const QRectF &newGeometry,
  //      const QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuick3DViewportCall3 call = reinterpret_cast<CuteQQuick3DViewportCall3>(taken[3]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuick3DViewport::geometryChange(newGeometry, oldGeometry);
  }

  //  QSGNode *QQuick3DViewport::updatePaintNode(QSGNode *a0,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *a0,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuick3DViewportCall4 call = reinterpret_cast<CuteQQuick3DViewportCall4>(taken[4]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuick3DViewport::updatePaintNode(a0, a1);
  }

  //  void QQuick3DViewport::itemChange(QQuickItem::ItemChange change,
  //      const QQuickItem::ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuick3DViewportCall5 call = reinterpret_cast<CuteQQuick3DViewportCall5>(taken[5]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuick3DViewport::itemChange(change, value);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuick3DViewport::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuick3DViewportCall6 call = reinterpret_cast<CuteQQuick3DViewportCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuick3DViewport::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuick3DViewport::componentComplete()
  void componentComplete() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuick3DViewportCall7 call = reinterpret_cast<CuteQQuick3DViewportCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuick3DViewport::componentComplete();
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuick3DViewportCall8 call = reinterpret_cast<CuteQQuick3DViewportCall8>(taken[8]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuick3DViewportCall9 call = reinterpret_cast<CuteQQuick3DViewportCall9>(taken[9]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuick3DViewportCall10 call = reinterpret_cast<CuteQQuick3DViewportCall10>(taken[10]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuick3DViewportCall11 call = reinterpret_cast<CuteQQuick3DViewportCall11>(taken[11]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuick3DViewportCall12 call = reinterpret_cast<CuteQQuick3DViewportCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuick3DViewportCall13 call = reinterpret_cast<CuteQQuick3DViewportCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuick3DViewportCall14 call = reinterpret_cast<CuteQQuick3DViewportCall14>(taken[14]);
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
      CuteQQuick3DViewportCall15 call = reinterpret_cast<CuteQQuick3DViewportCall15>(taken[15]);
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
      CuteQQuick3DViewportCall16 call = reinterpret_cast<CuteQQuick3DViewportCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuick3DViewportCall17 call = reinterpret_cast<CuteQQuick3DViewportCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuick3DViewportCall18 call = reinterpret_cast<CuteQQuick3DViewportCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuick3DViewportCall19 call = reinterpret_cast<CuteQQuick3DViewportCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuick3DViewportCall20 call = reinterpret_cast<CuteQQuick3DViewportCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuick3DViewportCall21 call = reinterpret_cast<CuteQQuick3DViewportCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuick3DViewportCall22 call = reinterpret_cast<CuteQQuick3DViewportCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuick3DViewportCall23 call = reinterpret_cast<CuteQQuick3DViewportCall23>(taken[23]);
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
      CuteQQuick3DViewportCall24 call = reinterpret_cast<CuteQQuick3DViewportCall24>(taken[24]);
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
      CuteQQuick3DViewportCall25 call = reinterpret_cast<CuteQQuick3DViewportCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuick3DViewportCall26 call = reinterpret_cast<CuteQQuick3DViewportCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuick3DViewportCall27 call = reinterpret_cast<CuteQQuick3DViewportCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuick3DViewportCall28 call = reinterpret_cast<CuteQQuick3DViewportCall28>(taken[28]);
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
      CuteQQuick3DViewportCall29 call = reinterpret_cast<CuteQQuick3DViewportCall29>(taken[29]);
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
      CuteQQuick3DViewportCall30 call = reinterpret_cast<CuteQQuick3DViewportCall30>(taken[30]);
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
      CuteQQuick3DViewportCall31 call = reinterpret_cast<CuteQQuick3DViewportCall31>(taken[31]);
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
      CuteQQuick3DViewportCall32 call = reinterpret_cast<CuteQQuick3DViewportCall32>(taken[32]);
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
      CuteQQuick3DViewportCall33 call = reinterpret_cast<CuteQQuick3DViewportCall33>(taken[33]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuick3DViewportCall34 call = reinterpret_cast<CuteQQuick3DViewportCall34>(taken[34]);
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
      CuteQQuick3DViewportCall35 call = reinterpret_cast<CuteQQuick3DViewportCall35>(taken[35]);
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
      CuteQQuick3DViewportCall36 call = reinterpret_cast<CuteQQuick3DViewportCall36>(taken[36]);
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
      CuteQQuick3DViewportCall37 call = reinterpret_cast<CuteQQuick3DViewportCall37>(taken[37]);
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
      CuteQQuick3DViewportCall38 call = reinterpret_cast<CuteQQuick3DViewportCall38>(taken[38]);
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
      CuteQQuick3DViewportCall39 call = reinterpret_cast<CuteQQuick3DViewportCall39>(taken[39]);
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
      CuteQQuick3DViewportCall40 call = reinterpret_cast<CuteQQuick3DViewportCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DViewport::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QQuick3DViewport10metaObjectEv(
    const QQuick3DViewport *self) {
  return self->metaObject();
}

//  void *QQuick3DViewport::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QQuick3DViewport11qt_metacastEPKc(
    QQuick3DViewport *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DViewport::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QQuick3DViewport11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DViewport *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DViewport::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QQuick3DViewport2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DViewport::tr(s, c, n));
}

//  QQuick3DViewport::QQuick3DViewport(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuick3DViewport *ritual_ZN16QQuick3DViewportC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuick3DViewport(parent);
}

//  QQuick3DViewport::~QQuick3DViewport()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewportD1Ev(QQuick3DViewport *self) {
  delete self;
}

//  QQmlListProperty<QObject> QQuick3DViewport::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN16QQuick3DViewport4dataEv(
    QQuick3DViewport *self) {
  return new QQmlListProperty<QObject>(self->data());
}

//  QQuick3DCamera *QQuick3DViewport::camera() const
extern "C" Q_DECL_EXPORT
QQuick3DCamera *ritual_ZNK16QQuick3DViewport6cameraEv(
    const QQuick3DViewport *self) {
  return self->camera();
}

//  QQuick3DSceneEnvironment *QQuick3DViewport::environment() const
extern "C" Q_DECL_EXPORT
QQuick3DSceneEnvironment *ritual_ZNK16QQuick3DViewport11environmentEv(
    const QQuick3DViewport *self) {
  return self->environment();
}

//  QQuick3DNode *QQuick3DViewport::scene() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK16QQuick3DViewport5sceneEv(
    const QQuick3DViewport *self) {
  return self->scene();
}

//  QQuick3DNode *QQuick3DViewport::importScene() const
extern "C" Q_DECL_EXPORT
QQuick3DNode *ritual_ZNK16QQuick3DViewport11importSceneEv(
    const QQuick3DViewport *self) {
  return self->importScene();
}

//  RenderMode QQuick3DViewport::renderMode() const
extern "C" Q_DECL_EXPORT
QQuick3DViewport::RenderMode ritual_ZNK16QQuick3DViewport10renderModeEv(
    const QQuick3DViewport *self) {
  return self->renderMode();
}

#if QT_CONFIG(quick_shadereffect)
//  QQuickShaderEffectSource::Format QQuick3DViewport::renderFormat() const
extern "C" Q_DECL_EXPORT
QQuickShaderEffectSource::Format ritual_ZNK16QQuick3DViewport12renderFormatEv(
    const QQuick3DViewport *self) {
  return self->renderFormat();
}
#endif  // QT_CONFIG(quick_shadereffect)

//  QQuick3DRenderStats *QQuick3DViewport::renderStats() const
extern "C" Q_DECL_EXPORT
QQuick3DRenderStats *ritual_ZNK16QQuick3DViewport11renderStatsEv(
    const QQuick3DViewport *self) {
  return self->renderStats();
}

//  QQuick3DSceneRenderer *QQuick3DViewport::createRenderer() const
extern "C" Q_DECL_EXPORT
QQuick3DSceneRenderer *ritual_ZNK16QQuick3DViewport14createRendererEv(
    const QQuick3DViewport *self) {
  return self->createRenderer();
}

//  bool QQuick3DViewport::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuick3DViewport17isTextureProviderEv(
    const QQuick3DViewport *self) {
  return self->isTextureProvider();
}

//  QSGTextureProvider *QQuick3DViewport::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_ZNK16QQuick3DViewport15textureProviderEv(
    const QQuick3DViewport *self) {
  return self->textureProvider();
}

//  void QQuick3DViewport::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport16releaseResourcesEv(
    QQuick3DViewport *self) {
  self->releaseResources();
}

//  QVector3D QQuick3DViewport::mapFrom3DScene(const QVector3D &scenePos)
//      const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuick3DViewport14mapFrom3DSceneERK9QVector3D(
    const QQuick3DViewport *self,
    const QVector3D *scenePos) {
  return new QVector3D(self->mapFrom3DScene(*scenePos));
}

//  QVector3D QQuick3DViewport::mapTo3DScene(const QVector3D &viewPos) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK16QQuick3DViewport12mapTo3DSceneERK9QVector3D(
    const QQuick3DViewport *self,
    const QVector3D *viewPos) {
  return new QVector3D(self->mapTo3DScene(*viewPos));
}

//  QQuick3DPickResult QQuick3DViewport::pick(float x, float y) const
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZNK16QQuick3DViewport4pickEff(
    const QQuick3DViewport *self,
    float x,
    float y) {
  return new QQuick3DPickResult(self->pick(x, y));
}

//  QQuick3DPickResult QQuick3DViewport::pick(float x, float y, QQuick3DModel
//      *model) const
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZNK16QQuick3DViewport4pickEffP13QQuick3DModel(
    const QQuick3DViewport *self,
    float x,
    float y,
    QQuick3DModel *model) {
  return new QQuick3DPickResult(self->pick(x, y, model));
}

//  QList<QQuick3DPickResult> QQuick3DViewport::pickSubset(float x, float y,
//      const QJSValue &models) const
extern "C" Q_DECL_EXPORT
QList<QQuick3DPickResult> *ritual_ZNK16QQuick3DViewport10pickSubsetEffRK8QJSValue(
    const QQuick3DViewport *self,
    float x,
    float y,
    const QJSValue *models) {
  return new QList<QQuick3DPickResult>(self->pickSubset(x, y, *models));
}

//  QList<QQuick3DPickResult> QQuick3DViewport::pickAll(float x, float y)
//      const
extern "C" Q_DECL_EXPORT
QList<QQuick3DPickResult> *ritual_ZNK16QQuick3DViewport7pickAllEff(
    const QQuick3DViewport *self,
    float x,
    float y) {
  return new QList<QQuick3DPickResult>(self->pickAll(x, y));
}

//  QQuick3DPickResult QQuick3DViewport::rayPick(const QVector3D &origin,
//      const QVector3D &direction) const
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZNK16QQuick3DViewport7rayPickERK9QVector3DS2_(
    const QQuick3DViewport *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return new QQuick3DPickResult(self->rayPick(*origin, *direction));
}

//  QList<QQuick3DPickResult> QQuick3DViewport::rayPickAll(const QVector3D
//      &origin, const QVector3D &direction) const
extern "C" Q_DECL_EXPORT
QList<QQuick3DPickResult> *ritual_ZNK16QQuick3DViewport10rayPickAllERK9QVector3DS2_(
    const QQuick3DViewport *self,
    const QVector3D *origin,
    const QVector3D *direction) {
  return new QList<QQuick3DPickResult>(
      self->rayPickAll(
          *origin,
          *direction));
}

//  QQuick3DPickResult QQuick3DViewport::rayPick(const QVector3D &origin,
//      const QVector3D &direction, QQuick3DModel *model) const
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZNK16QQuick3DViewport7rayPickERK9QVector3DS2_P13QQuick3DModel(
    const QQuick3DViewport *self,
    const QVector3D *origin,
    const QVector3D *direction,
    QQuick3DModel *model) {
  return new QQuick3DPickResult(self->rayPick(*origin, *direction, model));
}

//  QQuick3DPickResult QQuick3DViewport::closestPointPick(const QVector3D
//      &origin, float radius, QQuick3DModel *model) const
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZNK16QQuick3DViewport16closestPointPickERK9QVector3DfP13QQuick3DModel(
    const QQuick3DViewport *self,
    const QVector3D *origin,
    float radius,
    QQuick3DModel *model) {
  return new QQuick3DPickResult(
      self->closestPointPick(
          *origin,
          radius,
          model));
}

//  QList<QQuick3DObject *> QQuick3DViewport::pickInRect(const QPointF
//      &start, const QPointF &end) const
extern "C" Q_DECL_EXPORT
QList<QQuick3DObject *> *ritual_ZNK16QQuick3DViewport10pickInRectERK7QPointFS2_(
    const QQuick3DViewport *self,
    const QPointF *start,
    const QPointF *end) {
  return new QList<QQuick3DObject *>(self->pickInRect(*start, *end));
}

//  void QQuick3DViewport::processPointerEventFromRay(const QVector3D
//      &origin, const QVector3D &direction, QPointerEvent *event) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QQuick3DViewport26processPointerEventFromRayERK9QVector3DS2_P13QPointerEvent(
    const QQuick3DViewport *self,
    const QVector3D *origin,
    const QVector3D *direction,
    QPointerEvent *event) {
  self->processPointerEventFromRay(*origin, *direction, event);
}

//  bool QQuick3DViewport::singlePointPick(QSinglePointEvent *event, const
//      QVector3D &origin, const QVector3D &direction)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuick3DViewport15singlePointPickEP17QSinglePointEventRK9QVector3DS4_(
    QQuick3DViewport *self,
    QSinglePointEvent *event,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->singlePointPick(event, *origin, *direction);
}

//  void QQuick3DViewport::setTouchpoint(QQuickItem *target, const QPointF
//      &position, int pointId, bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport13setTouchpointEP10QQuickItemRK7QPointFib(
    QQuick3DViewport *self,
    QQuickItem *target,
    const QPointF *position,
    int pointId,
    bool active) {
  self->setTouchpoint(target, *position, pointId, active);
}

//  QQuick3DLightmapBaker *QQuick3DViewport::maybeLightmapBaker()
extern "C" Q_DECL_EXPORT
QQuick3DLightmapBaker *ritual_ZN16QQuick3DViewport18maybeLightmapBakerEv(
    QQuick3DViewport *self) {
  return self->maybeLightmapBaker();
}

//  QQuick3DLightmapBaker *QQuick3DViewport::lightmapBaker()
extern "C" Q_DECL_EXPORT
QQuick3DLightmapBaker *ritual_ZN16QQuick3DViewport13lightmapBakerEv(
    QQuick3DViewport *self) {
  return self->lightmapBaker();
}

//  void QQuick3DViewport::bakeLightmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport12bakeLightmapEv(QQuick3DViewport *self) {
  self->bakeLightmap();
}

//  void QQuick3DViewport::denoiseLightmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport15denoiseLightmapEv(QQuick3DViewport *self) {
  self->denoiseLightmap();
}

//  QQmlListProperty<QQuick3DObject> QQuick3DViewport::extensions()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QQuick3DObject> *ritual_ZN16QQuick3DViewport10extensionsEv(
    QQuick3DViewport *self) {
  return new QQmlListProperty<QQuick3DObject>(self->extensions());
}

//  int QQuick3DViewport::explicitTextureWidth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DViewport20explicitTextureWidthEv(
    const QQuick3DViewport *self) {
  return self->explicitTextureWidth();
}

//  int QQuick3DViewport::explicitTextureHeight() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DViewport21explicitTextureHeightEv(
    const QQuick3DViewport *self) {
  return self->explicitTextureHeight();
}

//  QSize QQuick3DViewport::effectiveTextureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QQuick3DViewport20effectiveTextureSizeEv(
    const QQuick3DViewport *self) {
  return new QSize(self->effectiveTextureSize());
}

//  bool QQuick3DViewport::extensionListDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuick3DViewport18extensionListDirtyEv(
    const QQuick3DViewport *self) {
  return self->extensionListDirty();
}

//  const QList<QQuick3DObject *> &QQuick3DViewport::extensionList() const
extern "C" Q_DECL_EXPORT
QList<QQuick3DObject *> *ritual_ZNK16QQuick3DViewport13extensionListEv(
    const QQuick3DViewport *self) {
  return new QList<QQuick3DObject *>(self->extensionList());
}

//  void QQuick3DViewport::clearExtensionListDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport23clearExtensionListDirtyEv(
    QQuick3DViewport *self) {
  self->clearExtensionListDirty();
}

//  void QQuick3DViewport::rebuildExtensionList()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport20rebuildExtensionListEv(
    QQuick3DViewport *self) {
  self->rebuildExtensionList();
}

//  QQuick3DViewport::QQuick3DViewport(PrivateInstanceType type, QQuickItem
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DViewport *ritual_ZN16QQuick3DViewportC1ENS_19PrivateInstanceTypeEP10QQuickItem(
    QQuick3DViewport::PrivateInstanceType type,
    QQuickItem *parent) {
  return new CuteQQuick3DViewport(type, parent);
}

//  bool QQuick3DViewport::isXrViewInstance() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuick3DViewport16isXrViewInstanceEv(
    const QQuick3DViewport *self) {
  return self->isXrViewInstance();
}

//  void QQuick3DViewport::updateCameraForLayer(const QQuick3DViewport
//      &view3D, QSSGRenderLayer &layerNode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport20updateCameraForLayerERKS_R15QSSGRenderLayer(
    const QQuick3DViewport *view3D,
    QSSGRenderLayer *layerNode) {
  QQuick3DViewport::updateCameraForLayer(*view3D, *layerNode);
}

//  RenderOverrides QQuick3DViewport::renderOverrides() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QQuick3DViewport15renderOverridesEv(
    const QQuick3DViewport *self) {
  return static_cast<int>(self->renderOverrides().toInt());
}

//  void QQuick3DViewport::setRenderOverrides(RenderOverrides
//      newRenderOverrides)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport18setRenderOverridesE6QFlagsINS_14RenderOverrideEE(
    QQuick3DViewport *self,
    int newRenderOverrides) {
  self->setRenderOverrides(
      QFlags<QQuick3DViewport::RenderOverride>::fromInt(newRenderOverrides));
}

//  void QQuick3DViewport::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport14geometryChangeERK6QRectFS2_(
    QQuick3DViewport *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  self->geometryChange(*newGeometry, *oldGeometry);
}

//  QSGNode *QQuick3DViewport::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN16QQuick3DViewport15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuick3DViewport *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return self->updatePaintNode(a0, a1);
}

//  void QQuick3DViewport::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DViewport *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  bool QQuick3DViewport::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QQuick3DViewport5eventEP6QEvent(
    QQuick3DViewport *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QQuick3DViewport::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport17componentCompleteEv(
    QQuick3DViewport *self) {
  self->componentComplete();
}

//  void QQuick3DViewport::setCamera(QQuick3DCamera *camera)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport9setCameraEP14QQuick3DCamera(
    QQuick3DViewport *self,
    QQuick3DCamera *camera) {
  self->setCamera(camera);
}

//  void QQuick3DViewport::setEnvironment(QQuick3DSceneEnvironment
//      *environment)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport14setEnvironmentEP24QQuick3DSceneEnvironment(
    QQuick3DViewport *self,
    QQuick3DSceneEnvironment *environment) {
  self->setEnvironment(environment);
}

//  void QQuick3DViewport::setImportScene(QQuick3DNode *inScene)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport14setImportSceneEP12QQuick3DNode(
    QQuick3DViewport *self,
    QQuick3DNode *inScene) {
  self->setImportScene(inScene);
}

//  void QQuick3DViewport::setRenderMode(QQuick3DViewport::RenderMode
//      renderMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport13setRenderModeENS_10RenderModeE(
    QQuick3DViewport *self,
    QQuick3DViewport::RenderMode renderMode) {
  self->setRenderMode(renderMode);
}

#if QT_CONFIG(quick_shadereffect)
//  void QQuick3DViewport::setRenderFormat(QQuickShaderEffectSource::Format
//      format)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport15setRenderFormatEN24QQuickShaderEffectSource6FormatE(
    QQuick3DViewport *self,
    QQuickShaderEffectSource::Format format) {
  self->setRenderFormat(format);
}
#endif  // QT_CONFIG(quick_shadereffect)

//  void QQuick3DViewport::setExplicitTextureWidth(int width)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport23setExplicitTextureWidthEi(
    QQuick3DViewport *self,
    int width) {
  self->setExplicitTextureWidth(width);
}

//  void QQuick3DViewport::setExplicitTextureHeight(int height)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport24setExplicitTextureHeightEi(
    QQuick3DViewport *self,
    int height) {
  self->setExplicitTextureHeight(height);
}

//  void QQuick3DViewport::cleanupDirectRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport21cleanupDirectRendererEv(
    QQuick3DViewport *self) {
  self->cleanupDirectRenderer();
}

//  void QQuick3DViewport::setGlobalPickingEnabled(bool isEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport23setGlobalPickingEnabledEb(
    QQuick3DViewport *self,
    bool isEnabled) {
  self->setGlobalPickingEnabled(isEnabled);
}

//  void QQuick3DViewport::invalidateSceneGraph()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport20invalidateSceneGraphEv(
    QQuick3DViewport *self) {
  self->invalidateSceneGraph();
}

//  void QQuick3DViewport::updateInputProcessing()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport21updateInputProcessingEv(
    QQuick3DViewport *self) {
  self->updateInputProcessing();
}

//  void QQuick3DViewport::onReleaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport24onReleaseCachedResourcesEv(
    QQuick3DViewport *self) {
  self->onReleaseCachedResources();
}

//  void QQuick3DViewport::cameraChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport13cameraChangedEv(QQuick3DViewport *self) {
  self->cameraChanged();
}

//  void QQuick3DViewport::environmentChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport18environmentChangedEv(
    QQuick3DViewport *self) {
  self->environmentChanged();
}

//  void QQuick3DViewport::sceneChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport12sceneChangedEv(QQuick3DViewport *self) {
  self->sceneChanged();
}

//  void QQuick3DViewport::importSceneChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport18importSceneChangedEv(
    QQuick3DViewport *self) {
  self->importSceneChanged();
}

//  void QQuick3DViewport::renderModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport17renderModeChangedEv(
    QQuick3DViewport *self) {
  self->renderModeChanged();
}

//  void QQuick3DViewport::renderFormatChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport19renderFormatChangedEv(
    QQuick3DViewport *self) {
  self->renderFormatChanged();
}

//  void QQuick3DViewport::explicitTextureWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport27explicitTextureWidthChangedEv(
    QQuick3DViewport *self) {
  self->explicitTextureWidthChanged();
}

//  void QQuick3DViewport::explicitTextureHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport28explicitTextureHeightChangedEv(
    QQuick3DViewport *self) {
  self->explicitTextureHeightChanged();
}

//  void QQuick3DViewport::effectiveTextureSizeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport27effectiveTextureSizeChangedEv(
    QQuick3DViewport *self) {
  self->effectiveTextureSizeChanged();
}

//  void QQuick3DViewport::renderOverridesChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport22renderOverridesChangedEv(
    QQuick3DViewport *self) {
  self->renderOverridesChanged();
}

//  void QQuick3DViewport::setMultiViewCameras(QQuick3DCamera **firstCamera,
//      int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport19setMultiViewCamerasEPP14QQuick3DCamerai(
    QQuick3DViewport *self,
    QQuick3DCamera **firstCamera,
    int count) {
  self->setMultiViewCameras(firstCamera, count);
}

//  QQuick3DSceneRenderer *QQuick3DViewport::getRenderer() const
extern "C" Q_DECL_EXPORT
QQuick3DSceneRenderer *ritual_ZNK16QQuick3DViewport11getRendererEv(
    const QQuick3DViewport *self) {
  return self->getRenderer();
}

//  void QQuick3DViewport::updateDynamicTextures()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport21updateDynamicTexturesEv(
    QQuick3DViewport *self) {
  self->updateDynamicTextures();
}

//  QSGNode *QQuick3DViewport::setupOffscreenRenderer(QSGNode *node)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN16QQuick3DViewport22setupOffscreenRendererEP7QSGNode(
    QQuick3DViewport *self,
    QSGNode *node) {
  return self->setupOffscreenRenderer(node);
}

//  QSGNode *QQuick3DViewport::setupInlineRenderer(QSGNode *node)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN16QQuick3DViewport19setupInlineRendererEP7QSGNode(
    QQuick3DViewport *self,
    QSGNode *node) {
  return self->setupInlineRenderer(node);
}

//  void QQuick3DViewport::setupDirectRenderer(RenderMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport19setupDirectRendererENS_10RenderModeE(
    QQuick3DViewport *self,
    QQuick3DViewport::RenderMode mode) {
  self->setupDirectRenderer(mode);
}

//  bool QQuick3DViewport::checkIsVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuick3DViewport14checkIsVisibleEv(
    const QQuick3DViewport *self) {
  return self->checkIsVisible();
}

//  bool QQuick3DViewport::internalPick(QPointerEvent *event, const QVector3D
//      &origin, const QVector3D &direction) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuick3DViewport12internalPickEP13QPointerEventRK9QVector3DS4_(
    const QQuick3DViewport *self,
    QPointerEvent *event,
    const QVector3D *origin,
    const QVector3D *direction) {
  return self->internalPick(event, *origin, *direction);
}

//  QPair<QQuickItem *, QPointF> QQuick3DViewport::getItemAndPosition(const
//      QSSGRenderPickResult &pickResult) const
extern "C" Q_DECL_EXPORT
QPair<QQuickItem *, QPointF> *ritual_ZNK16QQuick3DViewport18getItemAndPositionERK20QSSGRenderPickResult(
    const QQuick3DViewport *self,
    const QSSGRenderPickResult *pickResult) {
  return new QPair<QQuickItem *, QPointF>(
      self->getItemAndPosition(
          *pickResult));
}

//  QVarLengthArray<QSSGRenderPickResult, 20>
//      QQuick3DViewport::getPickResults(QQuick3DSceneRenderer *renderer,
//      const QVector3D &origin, const QVector3D &direction) const
extern "C" Q_DECL_EXPORT
QVarLengthArray<QSSGRenderPickResult, 20> *ritual_ZNK16QQuick3DViewport14getPickResultsEP21QQuick3DSceneRendererRK9QVector3DS4_(
    const QQuick3DViewport *self,
    QQuick3DSceneRenderer *renderer,
    const QVector3D *origin,
    const QVector3D *direction) {
  return new QVarLengthArray<QSSGRenderPickResult, 20>(
      self->getPickResults(
          renderer,
          *origin,
          *direction));
}

//  QVarLengthArray<QSSGRenderPickResult, 20>
//      QQuick3DViewport::getPickResults(QQuick3DSceneRenderer *renderer,
//      const QEventPoint &eventPoint) const
extern "C" Q_DECL_EXPORT
QVarLengthArray<QSSGRenderPickResult, 20> *ritual_ZNK16QQuick3DViewport14getPickResultsEP21QQuick3DSceneRendererRK11QEventPoint(
    const QQuick3DViewport *self,
    QQuick3DSceneRenderer *renderer,
    const QEventPoint *eventPoint) {
  return new QVarLengthArray<QSSGRenderPickResult, 20>(
      self->getPickResults(
          renderer,
          *eventPoint));
}

//  bool QQuick3DViewport::forwardEventToSubscenes(QPointerEvent *event, bool
//      useRayPicking, QQuick3DSceneRenderer *renderer, const
//      QFlatMap<QQuickItem *, SubsceneInfo> &visitedSubscenes) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QQuick3DViewport23forwardEventToSubscenesEP13QPointerEventbP21QQuick3DSceneRendererRK8QFlatMapIP10QQuickItemNS_12SubsceneInfoESt4lessIS6_E5QListIS6_ESA_IS7_EE(
    const QQuick3DViewport *self,
    QPointerEvent *event,
    bool useRayPicking,
    QQuick3DSceneRenderer *renderer,
    const QFlatMap<QQuickItem *, QQuick3DViewport::SubsceneInfo> *visitedSubscenes) {
  return self->forwardEventToSubscenes(
      event,
      useRayPicking,
      renderer,
      *visitedSubscenes);
}

//  void QQuick3DViewport::processPickedObject(const QSSGRenderPickResult
//      &pickResult, int pointIndex, QPointerEvent *event,
//      QFlatMap<QQuickItem *, SubsceneInfo> &vistedSubscenes) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QQuick3DViewport19processPickedObjectERK20QSSGRenderPickResultiP13QPointerEventR8QFlatMapIP10QQuickItemNS_12SubsceneInfoESt4lessIS7_E5QListIS7_ESB_IS8_EE(
    const QQuick3DViewport *self,
    const QSSGRenderPickResult *pickResult,
    int pointIndex,
    QPointerEvent *event,
    QFlatMap<QQuickItem *, QQuick3DViewport::SubsceneInfo> *vistedSubscenes) {
  self->processPickedObject(
      *pickResult,
      pointIndex,
      event,
      *vistedSubscenes);
}

//  QQuickItem *QQuick3DViewport::getSubSceneRootItem(QQuick3DMaterial
//      *material) const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK16QQuick3DViewport19getSubSceneRootItemEP16QQuick3DMaterial(
    const QQuick3DViewport *self,
    QQuick3DMaterial *material) {
  return self->getSubSceneRootItem(material);
}

//  QQuick3DPickResult QQuick3DViewport::getNearestPickResult(const
//      QVarLengthArray<QSSGRenderPickResult, 20> &pickResults) const
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZNK16QQuick3DViewport20getNearestPickResultERK15QVarLengthArrayI20QSSGRenderPickResultLx20EE(
    const QQuick3DViewport *self,
    const QVarLengthArray<QSSGRenderPickResult, 20> *pickResults) {
  return new QQuick3DPickResult(self->getNearestPickResult(*pickResults));
}

//  QQuick3DPickResult QQuick3DViewport::processPickResult(const
//      QSSGRenderPickResult &pickResult) const
extern "C" Q_DECL_EXPORT
QQuick3DPickResult *ritual_ZNK16QQuick3DViewport17processPickResultERK20QSSGRenderPickResult(
    const QQuick3DViewport *self,
    const QSSGRenderPickResult *pickResult) {
  return new QQuick3DPickResult(self->processPickResult(*pickResult));
}

//  QQuick3DObject *QQuick3DViewport::findFrontendNode(const
//      QSSGRenderGraphObject *backendObject) const
extern "C" Q_DECL_EXPORT
QQuick3DObject *ritual_ZNK16QQuick3DViewport16findFrontendNodeEPK21QSSGRenderGraphObject(
    const QQuick3DViewport *self,
    const QSSGRenderGraphObject *backendObject) {
  return self->findFrontendNode(backendObject);
}

//  QQuick3DSceneManager
//      *QQuick3DViewport::findChildSceneManager(QQuick3DObject *inObject,
//      QQuick3DSceneManager *manager)
extern "C" Q_DECL_EXPORT
QQuick3DSceneManager *ritual_ZN16QQuick3DViewport21findChildSceneManagerEP14QQuick3DObjectP20QQuick3DSceneManager(
    QQuick3DViewport *self,
    QQuick3DObject *inObject,
    QQuick3DSceneManager *manager) {
  return self->findChildSceneManager(inObject, manager);
}

//  void QQuick3DViewport::updateSceneManagerForImportScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuick3DViewport32updateSceneManagerForImportSceneEv(
    QQuick3DViewport *self) {
  self->updateSceneManagerForImportScene();
}

//  a Python function taken by a CuteQQuick3DViewport, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DViewport(
    QQuick3DViewport *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DViewport *>(self)->take(key, call);
}

//  bool QQuick3DViewport::isTextureProvider() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QQuick3DViewport17isTextureProviderEv(
    const QQuick3DViewport *self) {
  return self->QQuick3DViewport::isTextureProvider();
}

//  QSGTextureProvider *QQuick3DViewport::textureProvider() const
extern "C" Q_DECL_EXPORT
QSGTextureProvider *ritual_own_ZNK16QQuick3DViewport15textureProviderEv(
    const QQuick3DViewport *self) {
  return self->QQuick3DViewport::textureProvider();
}

//  void QQuick3DViewport::releaseResources()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DViewport16releaseResourcesEv(
    QQuick3DViewport *self) {
  self->QQuick3DViewport::releaseResources();
}

//  void QQuick3DViewport::geometryChange(const QRectF &newGeometry, const
//      QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DViewport14geometryChangeERK6QRectFS2_(
    QQuick3DViewport *self,
    const QRectF *newGeometry,
    const QRectF *oldGeometry) {
  static_cast<OwnQQuick3DViewport *>(self)->OwnQQuick3DViewport::geometryChange(
      *newGeometry,
      *oldGeometry);
}

//  QSGNode *QQuick3DViewport::updatePaintNode(QSGNode *a0,
//      UpdatePaintNodeData *a1)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_own_ZN16QQuick3DViewport15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    QQuick3DViewport *self,
    QSGNode *a0,
    QQuickItem::UpdatePaintNodeData *a1) {
  return static_cast<OwnQQuick3DViewport *>(self)->OwnQQuick3DViewport::updatePaintNode(
      a0,
      a1);
}

//  void QQuick3DViewport::itemChange(QQuickItem::ItemChange change, const
//      QQuickItem::ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DViewport10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuick3DViewport *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuick3DViewport *>(self)->OwnQQuick3DViewport::itemChange(
      change,
      *value);
}

//  bool QQuick3DViewport::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QQuick3DViewport5eventEP6QEvent(
    QQuick3DViewport *self,
    QEvent *a0) {
  return static_cast<OwnQQuick3DViewport *>(self)->OwnQQuick3DViewport::event(
      a0);
}

//  void QQuick3DViewport::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QQuick3DViewport17componentCompleteEv(
    QQuick3DViewport *self) {
  static_cast<OwnQQuick3DViewport *>(self)->OwnQQuick3DViewport::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of QQuick3DViewport gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DViewport__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

//  a QQmlListProperty<QQuick3DObject> a ritual of QQuick3DViewport gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DViewport__QQmlListProperty_QQuick3DObject(
    QQmlListProperty<QQuick3DObject> *self) {
  delete self;
}

//  a QPair<QQuickItem *, QPointF> a ritual of QQuick3DViewport gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DViewport__QPair_QQuickItem_QPointF(
    QPair<QQuickItem *, QPointF> *self) {
  delete self;
}

//  a QVarLengthArray<QSSGRenderPickResult, 20> a ritual of QQuick3DViewport
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuick3DViewport__QVarLengthArray_QSSGRenderPickResult_20(
    QVarLengthArray<QSSGRenderPickResult, 20> *self) {
  delete self;
}
