//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapesD
//  esignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickrectanglesha
//  pe_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickshapesdesignhelpersglobal_p.h>
#include <QtQuickShapesDesignHelpers/QtQuickShapesDesignHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickrectangleshape_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qcolor.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>

//  Only a class built on QQuickRectangleShape may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickRectangleShape : QQuickRectangleShape {
  using QQuickRectangleShape::componentComplete;
  using QQuickRectangleShape::itemChange;
};

//  A QQuickRectangleShape that Python can take functions over in. Every QQuickRectangleShape
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickRectangleShapeCall0)(const void *, int *);
typedef void (*CuteQQuickRectangleShapeCall1)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQQuickRectangleShapeCall2)(const void *, int *);
typedef const QRectF * (*CuteQQuickRectangleShapeCall3)(const void *, int *);
typedef bool (*CuteQQuickRectangleShapeCall4)(const void *, const QPointF *, int *);
typedef void * (*CuteQQuickRectangleShapeCall5)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQQuickRectangleShapeCall6)(const void *, int *);
typedef const QRectF * (*CuteQQuickRectangleShapeCall7)(const void *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickRectangleShapeCall8)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQQuickRectangleShapeCall9)(const void *, int *);
typedef void * (*CuteQQuickRectangleShapeCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRectangleShapeCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRectangleShapeCall12)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQQuickRectangleShapeCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQQuickRectangleShapeCall14)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQQuickRectangleShapeCall15)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQQuickRectangleShapeCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRectangleShapeCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQQuickRectangleShapeCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRectangleShapeCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRectangleShapeCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRectangleShapeCall21)(const void *, QMouseEvent *, int *);
typedef void (*CuteQQuickRectangleShapeCall22)(const void *, int *);
typedef void (*CuteQQuickRectangleShapeCall23)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRectangleShapeCall24)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQQuickRectangleShapeCall25)(const void *, QTouchEvent *, int *);
typedef void (*CuteQQuickRectangleShapeCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRectangleShapeCall27)(const void *, QHoverEvent *, int *);
typedef void (*CuteQQuickRectangleShapeCall28)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRectangleShapeCall29)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRectangleShapeCall30)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRectangleShapeCall31)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQQuickRectangleShapeCall32)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQQuickRectangleShapeCall33)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQQuickRectangleShapeCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickRectangleShapeCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRectangleShapeCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRectangleShapeCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRectangleShapeCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRectangleShapeCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickRectangleShapeCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickRectangleShape : public QQuickRectangleShape {
public:
  using QQuickRectangleShape::QQuickRectangleShape;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[7] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
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
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
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

  //  void QQuickRectangleShape::componentComplete()
  void componentComplete() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall0 call = reinterpret_cast<CuteQQuickRectangleShapeCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickRectangleShape::componentComplete();
  }

  //  void QQuickRectangleShape::itemChange(ItemChange change, const
  //      ItemChangeData &value)
  void itemChange(
      QQuickItem::ItemChange change,
      const QQuickItem::ItemChangeData &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall1 call = reinterpret_cast<CuteQQuickRectangleShapeCall1>(taken[1]);
      call(this, static_cast<int>(change), &value, &handled);
      if (handled) return;
    }
    QQuickRectangleShape::itemChange(change, value);
  }

  //  void QQuickRectangleShape::updatePolish()
  void updatePolish() override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall2 call = reinterpret_cast<CuteQQuickRectangleShapeCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickRectangleShape::updatePolish();
  }

  //  QRectF QQuickShape::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall3 call = reinterpret_cast<CuteQQuickRectangleShapeCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickShape::boundingRect();
  }

  //  bool QQuickShape::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall4 call = reinterpret_cast<CuteQQuickRectangleShapeCall4>(taken[4]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickShape::contains(point);
  }

  //  QSGNode *QQuickShape::updatePaintNode(QSGNode *node,
  //      UpdatePaintNodeData *a1)
  QSGNode *updatePaintNode(
      QSGNode *node,
      QQuickItem::UpdatePaintNodeData *a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall5 call = reinterpret_cast<CuteQQuickRectangleShapeCall5>(taken[5]);
      void * given = call(this, node, a1, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return QQuickShape::updatePaintNode(node, a1);
  }

  //  void QQuickShape::classBegin()
  void classBegin() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall6 call = reinterpret_cast<CuteQQuickRectangleShapeCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShape::classBegin();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall7 call = reinterpret_cast<CuteQQuickRectangleShapeCall7>(taken[7]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall8 call = reinterpret_cast<CuteQQuickRectangleShapeCall8>(taken[8]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall9 call = reinterpret_cast<CuteQQuickRectangleShapeCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall10 call = reinterpret_cast<CuteQQuickRectangleShapeCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall11 call = reinterpret_cast<CuteQQuickRectangleShapeCall11>(taken[11]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall12 call = reinterpret_cast<CuteQQuickRectangleShapeCall12>(taken[12]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall13 call = reinterpret_cast<CuteQQuickRectangleShapeCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall14 call = reinterpret_cast<CuteQQuickRectangleShapeCall14>(taken[14]);
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
      CuteQQuickRectangleShapeCall15 call = reinterpret_cast<CuteQQuickRectangleShapeCall15>(taken[15]);
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
      CuteQQuickRectangleShapeCall16 call = reinterpret_cast<CuteQQuickRectangleShapeCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall17 call = reinterpret_cast<CuteQQuickRectangleShapeCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall18 call = reinterpret_cast<CuteQQuickRectangleShapeCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mousePressEvent(event);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall19 call = reinterpret_cast<CuteQQuickRectangleShapeCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall20 call = reinterpret_cast<CuteQQuickRectangleShapeCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall21 call = reinterpret_cast<CuteQQuickRectangleShapeCall21>(taken[21]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall22 call = reinterpret_cast<CuteQQuickRectangleShapeCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall23 call = reinterpret_cast<CuteQQuickRectangleShapeCall23>(taken[23]);
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
      CuteQQuickRectangleShapeCall24 call = reinterpret_cast<CuteQQuickRectangleShapeCall24>(taken[24]);
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
      CuteQQuickRectangleShapeCall25 call = reinterpret_cast<CuteQQuickRectangleShapeCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall26 call = reinterpret_cast<CuteQQuickRectangleShapeCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall27 call = reinterpret_cast<CuteQQuickRectangleShapeCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall28 call = reinterpret_cast<CuteQQuickRectangleShapeCall28>(taken[28]);
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
      CuteQQuickRectangleShapeCall29 call = reinterpret_cast<CuteQQuickRectangleShapeCall29>(taken[29]);
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
      CuteQQuickRectangleShapeCall30 call = reinterpret_cast<CuteQQuickRectangleShapeCall30>(taken[30]);
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
      CuteQQuickRectangleShapeCall31 call = reinterpret_cast<CuteQQuickRectangleShapeCall31>(taken[31]);
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
      CuteQQuickRectangleShapeCall32 call = reinterpret_cast<CuteQQuickRectangleShapeCall32>(taken[32]);
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
      CuteQQuickRectangleShapeCall33 call = reinterpret_cast<CuteQQuickRectangleShapeCall33>(taken[33]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall34 call = reinterpret_cast<CuteQQuickRectangleShapeCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickRectangleShapeCall35 call = reinterpret_cast<CuteQQuickRectangleShapeCall35>(taken[35]);
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
      CuteQQuickRectangleShapeCall36 call = reinterpret_cast<CuteQQuickRectangleShapeCall36>(taken[36]);
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
      CuteQQuickRectangleShapeCall37 call = reinterpret_cast<CuteQQuickRectangleShapeCall37>(taken[37]);
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
      CuteQQuickRectangleShapeCall38 call = reinterpret_cast<CuteQQuickRectangleShapeCall38>(taken[38]);
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
      CuteQQuickRectangleShapeCall39 call = reinterpret_cast<CuteQQuickRectangleShapeCall39>(taken[39]);
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
      CuteQQuickRectangleShapeCall40 call = reinterpret_cast<CuteQQuickRectangleShapeCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickRectangleShape::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickRectangleShape10metaObjectEv(
    const QQuickRectangleShape *self) {
  return self->metaObject();
}

//  void *QQuickRectangleShape::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuickRectangleShape11qt_metacastEPKc(
    QQuickRectangleShape *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickRectangleShape::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuickRectangleShape11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickRectangleShape *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickRectangleShape::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickRectangleShape2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRectangleShape::tr(s, c, n));
}

//  QQuickRectangleShape::QQuickRectangleShape(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickRectangleShape *ritual_ZN20QQuickRectangleShapeC1EP10QQuickItem(
    QQuickItem *parent) {
  return new CuteQQuickRectangleShape(parent);
}

//  QQuickRectangleShape::~QQuickRectangleShape()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShapeD1Ev(QQuickRectangleShape *self) {
  delete self;
}

//  bool QQuickRectangleShape::drawTop() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickRectangleShape7drawTopEv(
    const QQuickRectangleShape *self) {
  return self->drawTop();
}

//  void QQuickRectangleShape::setDrawTop(bool drawTop)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape10setDrawTopEb(
    QQuickRectangleShape *self,
    bool drawTop) {
  self->setDrawTop(drawTop);
}

//  void QQuickRectangleShape::resetDrawTop()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape12resetDrawTopEv(
    QQuickRectangleShape *self) {
  self->resetDrawTop();
}

//  bool QQuickRectangleShape::drawRight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickRectangleShape9drawRightEv(
    const QQuickRectangleShape *self) {
  return self->drawRight();
}

//  void QQuickRectangleShape::setDrawRight(bool drawRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape12setDrawRightEb(
    QQuickRectangleShape *self,
    bool drawRight) {
  self->setDrawRight(drawRight);
}

//  void QQuickRectangleShape::resetDrawRight()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape14resetDrawRightEv(
    QQuickRectangleShape *self) {
  self->resetDrawRight();
}

//  bool QQuickRectangleShape::drawBottom() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickRectangleShape10drawBottomEv(
    const QQuickRectangleShape *self) {
  return self->drawBottom();
}

//  void QQuickRectangleShape::setDrawBottom(bool drawBottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape13setDrawBottomEb(
    QQuickRectangleShape *self,
    bool drawBottom) {
  self->setDrawBottom(drawBottom);
}

//  void QQuickRectangleShape::resetDrawBottom()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape15resetDrawBottomEv(
    QQuickRectangleShape *self) {
  self->resetDrawBottom();
}

//  bool QQuickRectangleShape::drawLeft() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickRectangleShape8drawLeftEv(
    const QQuickRectangleShape *self) {
  return self->drawLeft();
}

//  void QQuickRectangleShape::setDrawLeft(bool drawLeft)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape11setDrawLeftEb(
    QQuickRectangleShape *self,
    bool drawLeft) {
  self->setDrawLeft(drawLeft);
}

//  void QQuickRectangleShape::resetDrawLeft()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape13resetDrawLeftEv(
    QQuickRectangleShape *self) {
  self->resetDrawLeft();
}

//  int QQuickRectangleShape::radius() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickRectangleShape6radiusEv(
    const QQuickRectangleShape *self) {
  return self->radius();
}

//  void QQuickRectangleShape::setRadius(int radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape9setRadiusEi(
    QQuickRectangleShape *self,
    int radius) {
  self->setRadius(radius);
}

//  void QQuickRectangleShape::resetRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape11resetRadiusEv(
    QQuickRectangleShape *self) {
  self->resetRadius();
}

//  int QQuickRectangleShape::topLeftRadius() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickRectangleShape13topLeftRadiusEv(
    const QQuickRectangleShape *self) {
  return self->topLeftRadius();
}

//  void QQuickRectangleShape::setTopLeftRadius(int topLeftRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape16setTopLeftRadiusEi(
    QQuickRectangleShape *self,
    int topLeftRadius) {
  self->setTopLeftRadius(topLeftRadius);
}

//  void QQuickRectangleShape::resetTopLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape18resetTopLeftRadiusEv(
    QQuickRectangleShape *self) {
  self->resetTopLeftRadius();
}

//  int QQuickRectangleShape::topRightRadius() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickRectangleShape14topRightRadiusEv(
    const QQuickRectangleShape *self) {
  return self->topRightRadius();
}

//  void QQuickRectangleShape::setTopRightRadius(int topRightRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape17setTopRightRadiusEi(
    QQuickRectangleShape *self,
    int topRightRadius) {
  self->setTopRightRadius(topRightRadius);
}

//  void QQuickRectangleShape::resetTopRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape19resetTopRightRadiusEv(
    QQuickRectangleShape *self) {
  self->resetTopRightRadius();
}

//  int QQuickRectangleShape::bottomLeftRadius() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickRectangleShape16bottomLeftRadiusEv(
    const QQuickRectangleShape *self) {
  return self->bottomLeftRadius();
}

//  void QQuickRectangleShape::setBottomLeftRadius(int bottomLeftRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape19setBottomLeftRadiusEi(
    QQuickRectangleShape *self,
    int bottomLeftRadius) {
  self->setBottomLeftRadius(bottomLeftRadius);
}

//  void QQuickRectangleShape::resetBottomLeftRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape21resetBottomLeftRadiusEv(
    QQuickRectangleShape *self) {
  self->resetBottomLeftRadius();
}

//  int QQuickRectangleShape::bottomRightRadius() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickRectangleShape17bottomRightRadiusEv(
    const QQuickRectangleShape *self) {
  return self->bottomRightRadius();
}

//  void QQuickRectangleShape::setBottomRightRadius(int bottomRightRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape20setBottomRightRadiusEi(
    QQuickRectangleShape *self,
    int bottomRightRadius) {
  self->setBottomRightRadius(bottomRightRadius);
}

//  void QQuickRectangleShape::resetBottomRightRadius()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape22resetBottomRightRadiusEv(
    QQuickRectangleShape *self) {
  self->resetBottomRightRadius();
}

//  bool QQuickRectangleShape::hasBevel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickRectangleShape8hasBevelEv(
    const QQuickRectangleShape *self) {
  return self->hasBevel();
}

//  void QQuickRectangleShape::setBevel(bool bevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape8setBevelEb(
    QQuickRectangleShape *self,
    bool bevel) {
  self->setBevel(bevel);
}

//  void QQuickRectangleShape::resetBevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape10resetBevelEv(
    QQuickRectangleShape *self) {
  self->resetBevel();
}

//  bool QQuickRectangleShape::hasTopLeftBevel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickRectangleShape15hasTopLeftBevelEv(
    const QQuickRectangleShape *self) {
  return self->hasTopLeftBevel();
}

//  void QQuickRectangleShape::setTopLeftBevel(bool topLeftBevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape15setTopLeftBevelEb(
    QQuickRectangleShape *self,
    bool topLeftBevel) {
  self->setTopLeftBevel(topLeftBevel);
}

//  void QQuickRectangleShape::resetTopLeftBevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape17resetTopLeftBevelEv(
    QQuickRectangleShape *self) {
  self->resetTopLeftBevel();
}

//  bool QQuickRectangleShape::hasTopRightBevel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickRectangleShape16hasTopRightBevelEv(
    const QQuickRectangleShape *self) {
  return self->hasTopRightBevel();
}

//  void QQuickRectangleShape::setTopRightBevel(bool topRightBevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape16setTopRightBevelEb(
    QQuickRectangleShape *self,
    bool topRightBevel) {
  self->setTopRightBevel(topRightBevel);
}

//  void QQuickRectangleShape::resetTopRightBevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape18resetTopRightBevelEv(
    QQuickRectangleShape *self) {
  self->resetTopRightBevel();
}

//  bool QQuickRectangleShape::hasBottomLeftBevel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickRectangleShape18hasBottomLeftBevelEv(
    const QQuickRectangleShape *self) {
  return self->hasBottomLeftBevel();
}

//  void QQuickRectangleShape::setBottomLeftBevel(bool bottomLeftBevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape18setBottomLeftBevelEb(
    QQuickRectangleShape *self,
    bool bottomLeftBevel) {
  self->setBottomLeftBevel(bottomLeftBevel);
}

//  void QQuickRectangleShape::resetBottomLeftBevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape20resetBottomLeftBevelEv(
    QQuickRectangleShape *self) {
  self->resetBottomLeftBevel();
}

//  bool QQuickRectangleShape::hasBottomRightBevel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickRectangleShape19hasBottomRightBevelEv(
    const QQuickRectangleShape *self) {
  return self->hasBottomRightBevel();
}

//  void QQuickRectangleShape::setBottomRightBevel(bool bottomRightBevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape19setBottomRightBevelEb(
    QQuickRectangleShape *self,
    bool bottomRightBevel) {
  self->setBottomRightBevel(bottomRightBevel);
}

//  void QQuickRectangleShape::resetBottomRightBevel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape21resetBottomRightBevelEv(
    QQuickRectangleShape *self) {
  self->resetBottomRightBevel();
}

//  QColor QQuickRectangleShape::strokeColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickRectangleShape11strokeColorEv(
    const QQuickRectangleShape *self) {
  return new QColor(self->strokeColor());
}

//  void QQuickRectangleShape::setStrokeColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape14setStrokeColorERK6QColor(
    QQuickRectangleShape *self,
    const QColor *color) {
  self->setStrokeColor(*color);
}

//  qreal QQuickRectangleShape::strokeWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickRectangleShape11strokeWidthEv(
    const QQuickRectangleShape *self) {
  return self->strokeWidth();
}

//  void QQuickRectangleShape::setStrokeWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape14setStrokeWidthEd(
    QQuickRectangleShape *self,
    qreal width) {
  self->setStrokeWidth(width);
}

//  QColor QQuickRectangleShape::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK20QQuickRectangleShape9fillColorEv(
    const QQuickRectangleShape *self) {
  return new QColor(self->fillColor());
}

//  void QQuickRectangleShape::setFillColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape12setFillColorERK6QColor(
    QQuickRectangleShape *self,
    const QColor *color) {
  self->setFillColor(*color);
}

//  QQuickShapePath::FillRule QQuickRectangleShape::fillRule() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::FillRule ritual_ZNK20QQuickRectangleShape8fillRuleEv(
    const QQuickRectangleShape *self) {
  return self->fillRule();
}

//  void QQuickRectangleShape::setFillRule(QQuickShapePath::FillRule
//      fillRule)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape11setFillRuleEN15QQuickShapePath8FillRuleE(
    QQuickRectangleShape *self,
    QQuickShapePath::FillRule fillRule) {
  self->setFillRule(fillRule);
}

//  QQuickShapePath::JoinStyle QQuickRectangleShape::joinStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::JoinStyle ritual_ZNK20QQuickRectangleShape9joinStyleEv(
    const QQuickRectangleShape *self) {
  return self->joinStyle();
}

//  void QQuickRectangleShape::setJoinStyle(QQuickShapePath::JoinStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape12setJoinStyleEN15QQuickShapePath9JoinStyleE(
    QQuickRectangleShape *self,
    QQuickShapePath::JoinStyle style) {
  self->setJoinStyle(style);
}

//  int QQuickRectangleShape::miterLimit() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQuickRectangleShape10miterLimitEv(
    const QQuickRectangleShape *self) {
  return self->miterLimit();
}

//  void QQuickRectangleShape::setMiterLimit(int limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape13setMiterLimitEi(
    QQuickRectangleShape *self,
    int limit) {
  self->setMiterLimit(limit);
}

//  QQuickShapePath::CapStyle QQuickRectangleShape::capStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::CapStyle ritual_ZNK20QQuickRectangleShape8capStyleEv(
    const QQuickRectangleShape *self) {
  return self->capStyle();
}

//  void QQuickRectangleShape::setCapStyle(QQuickShapePath::CapStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape11setCapStyleEN15QQuickShapePath8CapStyleE(
    QQuickRectangleShape *self,
    QQuickShapePath::CapStyle style) {
  self->setCapStyle(style);
}

//  QQuickShapePath::StrokeStyle QQuickRectangleShape::strokeStyle() const
extern "C" Q_DECL_EXPORT
QQuickShapePath::StrokeStyle ritual_ZNK20QQuickRectangleShape11strokeStyleEv(
    const QQuickRectangleShape *self) {
  return self->strokeStyle();
}

//  void QQuickRectangleShape::setStrokeStyle(QQuickShapePath::StrokeStyle
//      style)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape14setStrokeStyleEN15QQuickShapePath11StrokeStyleE(
    QQuickRectangleShape *self,
    QQuickShapePath::StrokeStyle style) {
  self->setStrokeStyle(style);
}

//  qreal QQuickRectangleShape::dashOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK20QQuickRectangleShape10dashOffsetEv(
    const QQuickRectangleShape *self) {
  return self->dashOffset();
}

//  void QQuickRectangleShape::setDashOffset(qreal offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape13setDashOffsetEd(
    QQuickRectangleShape *self,
    qreal offset) {
  self->setDashOffset(offset);
}

//  QList<qreal> QQuickRectangleShape::dashPattern() const
extern "C" Q_DECL_EXPORT
QList<qreal> *ritual_ZNK20QQuickRectangleShape11dashPatternEv(
    const QQuickRectangleShape *self) {
  return new QList<qreal>(self->dashPattern());
}

//  void QQuickRectangleShape::setDashPattern(const QList<qreal> &array)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape14setDashPatternERK5QListIdE(
    QQuickRectangleShape *self,
    const QList<qreal> *array) {
  self->setDashPattern(*array);
}

//  QQuickShapeGradient *QQuickRectangleShape::fillGradient() const
extern "C" Q_DECL_EXPORT
QQuickShapeGradient *ritual_ZNK20QQuickRectangleShape12fillGradientEv(
    const QQuickRectangleShape *self) {
  return self->fillGradient();
}

//  void QQuickRectangleShape::setFillGradient(QQuickShapeGradient
//      *fillGradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape15setFillGradientEP19QQuickShapeGradient(
    QQuickRectangleShape *self,
    QQuickShapeGradient *fillGradient) {
  self->setFillGradient(fillGradient);
}

//  void QQuickRectangleShape::resetFillGradient()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape17resetFillGradientEv(
    QQuickRectangleShape *self) {
  self->resetFillGradient();
}

//  BorderMode QQuickRectangleShape::borderMode() const
extern "C" Q_DECL_EXPORT
QQuickRectangleShape::BorderMode ritual_ZNK20QQuickRectangleShape10borderModeEv(
    const QQuickRectangleShape *self) {
  return self->borderMode();
}

//  void QQuickRectangleShape::setBorderMode(BorderMode borderMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape13setBorderModeENS_10BorderModeE(
    QQuickRectangleShape *self,
    QQuickRectangleShape::BorderMode borderMode) {
  self->setBorderMode(borderMode);
}

//  void QQuickRectangleShape::resetBorderMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape15resetBorderModeEv(
    QQuickRectangleShape *self) {
  self->resetBorderMode();
}

//  QQuickItem *QQuickRectangleShape::fillItem() const
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZNK20QQuickRectangleShape8fillItemEv(
    const QQuickRectangleShape *self) {
  return self->fillItem();
}

//  void QQuickRectangleShape::setFillItem(QQuickItem *newFillItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape11setFillItemEP10QQuickItem(
    QQuickRectangleShape *self,
    QQuickItem *newFillItem) {
  self->setFillItem(newFillItem);
}

//  void QQuickRectangleShape::drawTopChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape14drawTopChangedEv(
    QQuickRectangleShape *self) {
  self->drawTopChanged();
}

//  void QQuickRectangleShape::drawRightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape16drawRightChangedEv(
    QQuickRectangleShape *self) {
  self->drawRightChanged();
}

//  void QQuickRectangleShape::drawBottomChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape17drawBottomChangedEv(
    QQuickRectangleShape *self) {
  self->drawBottomChanged();
}

//  void QQuickRectangleShape::drawLeftChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape15drawLeftChangedEv(
    QQuickRectangleShape *self) {
  self->drawLeftChanged();
}

//  void QQuickRectangleShape::fillGradientChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape19fillGradientChangedEv(
    QQuickRectangleShape *self) {
  self->fillGradientChanged();
}

//  void QQuickRectangleShape::radiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape13radiusChangedEv(
    QQuickRectangleShape *self) {
  self->radiusChanged();
}

//  void QQuickRectangleShape::topLeftRadiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape20topLeftRadiusChangedEv(
    QQuickRectangleShape *self) {
  self->topLeftRadiusChanged();
}

//  void QQuickRectangleShape::topRightRadiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape21topRightRadiusChangedEv(
    QQuickRectangleShape *self) {
  self->topRightRadiusChanged();
}

//  void QQuickRectangleShape::bottomLeftRadiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape23bottomLeftRadiusChangedEv(
    QQuickRectangleShape *self) {
  self->bottomLeftRadiusChanged();
}

//  void QQuickRectangleShape::bottomRightRadiusChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape24bottomRightRadiusChangedEv(
    QQuickRectangleShape *self) {
  self->bottomRightRadiusChanged();
}

//  void QQuickRectangleShape::bevelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape12bevelChangedEv(
    QQuickRectangleShape *self) {
  self->bevelChanged();
}

//  void QQuickRectangleShape::topLeftBevelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape19topLeftBevelChangedEv(
    QQuickRectangleShape *self) {
  self->topLeftBevelChanged();
}

//  void QQuickRectangleShape::topRightBevelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape20topRightBevelChangedEv(
    QQuickRectangleShape *self) {
  self->topRightBevelChanged();
}

//  void QQuickRectangleShape::bottomLeftBevelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape22bottomLeftBevelChangedEv(
    QQuickRectangleShape *self) {
  self->bottomLeftBevelChanged();
}

//  void QQuickRectangleShape::bottomRightBevelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape23bottomRightBevelChangedEv(
    QQuickRectangleShape *self) {
  self->bottomRightBevelChanged();
}

//  void QQuickRectangleShape::shapePathChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape16shapePathChangedEv(
    QQuickRectangleShape *self) {
  self->shapePathChanged();
}

//  void QQuickRectangleShape::strokeColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape18strokeColorChangedEv(
    QQuickRectangleShape *self) {
  self->strokeColorChanged();
}

//  void QQuickRectangleShape::strokeWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape18strokeWidthChangedEv(
    QQuickRectangleShape *self) {
  self->strokeWidthChanged();
}

//  void QQuickRectangleShape::fillColorChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape16fillColorChangedEv(
    QQuickRectangleShape *self) {
  self->fillColorChanged();
}

//  void QQuickRectangleShape::fillRuleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape15fillRuleChangedEv(
    QQuickRectangleShape *self) {
  self->fillRuleChanged();
}

//  void QQuickRectangleShape::joinStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape16joinStyleChangedEv(
    QQuickRectangleShape *self) {
  self->joinStyleChanged();
}

//  void QQuickRectangleShape::miterLimitChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape17miterLimitChangedEv(
    QQuickRectangleShape *self) {
  self->miterLimitChanged();
}

//  void QQuickRectangleShape::capStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape15capStyleChangedEv(
    QQuickRectangleShape *self) {
  self->capStyleChanged();
}

//  void QQuickRectangleShape::strokeStyleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape18strokeStyleChangedEv(
    QQuickRectangleShape *self) {
  self->strokeStyleChanged();
}

//  void QQuickRectangleShape::dashOffsetChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape17dashOffsetChangedEv(
    QQuickRectangleShape *self) {
  self->dashOffsetChanged();
}

//  void QQuickRectangleShape::dashPatternChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape18dashPatternChangedEv(
    QQuickRectangleShape *self) {
  self->dashPatternChanged();
}

//  void QQuickRectangleShape::borderModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape17borderModeChangedEv(
    QQuickRectangleShape *self) {
  self->borderModeChanged();
}

//  void QQuickRectangleShape::fillItemChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape15fillItemChangedEv(
    QQuickRectangleShape *self) {
  self->fillItemChanged();
}

//  void QQuickRectangleShape::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape17componentCompleteEv(
    QQuickRectangleShape *self) {
  self->componentComplete();
}

//  void QQuickRectangleShape::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickRectangleShape *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  self->itemChange(change, *value);
}

//  void QQuickRectangleShape::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickRectangleShape12updatePolishEv(
    QQuickRectangleShape *self) {
  self->updatePolish();
}

//  QQuickRectangleShapePrivate *QQuickRectangleShape::d_func()
extern "C" Q_DECL_EXPORT
QQuickRectangleShapePrivate *ritual_ZN20QQuickRectangleShape6d_funcEv(
    QQuickRectangleShape *self) {
  return self->d_func();
}

//  const QQuickRectangleShapePrivate *QQuickRectangleShape::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickRectangleShapePrivate *ritual_ZNK20QQuickRectangleShape6d_funcEv(
    const QQuickRectangleShape *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQQuickRectangleShape, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRectangleShape(
    QQuickRectangleShape *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRectangleShape *>(self)->take(key, call);
}

//  void QQuickRectangleShape::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickRectangleShape17componentCompleteEv(
    QQuickRectangleShape *self) {
  static_cast<OwnQQuickRectangleShape *>(self)->OwnQQuickRectangleShape::componentComplete();
}

//  void QQuickRectangleShape::itemChange(ItemChange change, const
//      ItemChangeData &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickRectangleShape10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickRectangleShape *self,
    QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData *value) {
  static_cast<OwnQQuickRectangleShape *>(self)->OwnQQuickRectangleShape::itemChange(
      change,
      *value);
}

//  void QQuickRectangleShape::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickRectangleShape12updatePolishEv(
    QQuickRectangleShape *self) {
  self->QQuickRectangleShape::updatePolish();
}

//  a QList<qreal> a ritual of QQuickRectangleShape gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuickRectangleShape__QList_qreal(QList<qreal> *self) {
  delete self;
}
